import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const script = fileURLToPath(new URL('./audit-interactive-components.mjs', import.meta.url));
const compiler = process.env.INTERACTION_TYPESCRIPT_PATH ?? createRequire(path.join(process.cwd(), 'package.json')).resolve('typescript');
function fixture(context, files = { 'src/View.tsx': 'export const View = () => <button>Open</button>;' }) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'interaction-audit-'));
  context.after(() => fs.rmSync(root, { recursive: true, force: true }));
  for (const [name, content] of Object.entries(files)) {
    fs.mkdirSync(path.dirname(path.join(root, name)), { recursive: true });
    fs.writeFileSync(path.join(root, name), content);
  }
  return root;
}
function audit(root, extra = [], config) {
  if (config) fs.writeFileSync(path.join(root, 'policy.json'), JSON.stringify(config));
  return spawnSync(process.execPath, [script, '--root', root, '--source', 'src', '--typescript', compiler,
    '--json', '--check', ...(config ? ['--config', 'policy.json'] : []), ...extra], { encoding: 'utf8' });
}

test('raw controls are candidates until a project adopts a policy', (context) => {
  const root = fixture(context, { 'src/View.tsx': 'export const View = () => <input type="checkbox" />;' });
  const result = audit(root);
  assert.equal(result.status, 0, result.stderr);
  assert.equal(JSON.parse(result.stdout).findings[0].category, 'raw-action-input');
  assert.equal(audit(root, [], { failCategories: ['raw-action-input'] }).status, 1);
});

test('reports pointer handlers and does not exempt stopPropagation text', (context) => {
  const root = fixture(context, { 'src/View.jsx': 'export const View = () => <div onPointerDown={e => { e.stopPropagation(); open(); }} />;' });
  const result = audit(root);
  assert.equal(result.status, 1, result.stderr);
  assert.equal(JSON.parse(result.stdout).violations[0].category, 'non-semantic-action');
});

test('exceptions require exact file, category and literal marker', (context) => {
  const root = fixture(context, {
    'src/Dialog.tsx': 'export const View = () => <><div data-interaction-exception="backdrop" onClick={close} /><div data-interaction-exception={marker} onClick={close} /></>;',
    'src/Other.tsx': 'export const Other = () => <div data-interaction-exception="backdrop" onClick={close} />;'
  });
  const result = audit(root, [], { exceptions: [{ file: 'src/Dialog.tsx', category: 'non-semantic-action', marker: 'backdrop', reason: 'keyboard dismissal separately supported' }] });
  const report = JSON.parse(result.stdout);
  assert.equal(result.status, 1);
  assert.equal(report.findings.length, 3);
  assert.equal(report.violations.length, 2);
  assert.equal(report.findings.filter((entry) => entry.exceptionReason).length, 1);
});

test('file exception does not exempt adjacent primitive files', (context) => {
  const root = fixture(context, { 'src/Checkbox.tsx': 'export const A = () => <input type="checkbox" />;', 'src/Other.tsx': 'export const B = () => <input type="checkbox" />;' });
  const report = JSON.parse(audit(root, [], { failCategories: ['raw-action-input'], exceptions: [{ file: 'src/Checkbox.tsx', category: 'raw-action-input', reason: 'native implementation' }] }).stdout);
  assert.deepEqual(report.violations.map((entry) => entry.file), ['src/Other.tsx']);
});

test('missing paths, empty scans and unsupported-only sources fail', (context) => {
  const root = fixture(context, { 'src/View.vue': '<template />' });
  assert.equal(audit(root).status, 2);
  assert.equal(audit(root, ['--source', 'absent']).status, 2);
});

test('deduplicates roots and excludes dependencies and test files', (context) => {
  const root = fixture(context, {
    'src/View.tsx': 'export const View = () => <button />;',
    'src/View.test.tsx': 'export const View = () => <div onClick={go} />;',
    'src/node_modules/Dep.tsx': 'export const Dep = () => <div onClick={go} />;'
  });
  const result = audit(root, ['--source', 'src']);
  assert.equal(result.status, 0);
  assert.equal(JSON.parse(result.stdout).filesScanned, 1);
});

test('rejects malformed configuration, arguments, parser input and compiler paths', (context) => {
  const root = fixture(context);
  for (const config of [{ failCategories: ['typo'] }, { failCategory: [] }, { exceptions: [{ file: 'src/View.tsx', category: 'raw-button' }] }]) {
    assert.equal(audit(root, [], config).status, 2);
  }
  assert.equal(audit(root, ['--unknown']).status, 2);
  assert.equal(audit(root, ['--typescript', path.join(root, 'missing.js')]).status, 2);
  fs.writeFileSync(path.join(root, 'src/View.tsx'), 'const x = <div');
  assert.equal(audit(root).status, 2);
});

test('config roots work independently of cwd; ordinary audit does not fail on findings', (context) => {
  const root = fixture(context, { 'widgets/View.jsx': 'export const View = () => <div onClick={go} />;' });
  fs.writeFileSync(path.join(root, 'policy.json'), JSON.stringify({ sourceRoots: ['widgets'] }));
  const result = spawnSync(process.execPath, [script, '--root', root, '--config', 'policy.json', '--typescript', compiler, '--json'], { cwd: os.tmpdir(), encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr);
  assert.equal(JSON.parse(result.stdout).violations.length, 1);
});
