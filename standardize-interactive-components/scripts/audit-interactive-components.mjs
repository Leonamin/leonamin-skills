#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';

const categories = new Set(['non-semantic-action', 'raw-button', 'raw-anchor', 'raw-action-input', 'direct-next-link', 'clickable-abstraction']);
const nonSemanticTags = new Set(['article', 'div', 'img', 'li', 'section', 'span', 'svg', 'td', 'tr']);
const handlerNames = new Set(['onClick', 'onDoubleClick', 'onMouseDown', 'onMouseUp', 'onPointerDown', 'onPointerUp']);
const inputTypes = new Set(['button', 'checkbox', 'file', 'radio', 'reset', 'submit']);
const ignoredDirectories = new Set(['node_modules', '.git', 'dist', 'build', '.next']);

function parseArgs(args) {
  const options = { root: process.cwd(), sources: [], isJson: false, shouldCheck: false };
  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    if (arg === '--json') options.isJson = true;
    else if (arg === '--check') options.shouldCheck = true;
    else if (['--root', '--source', '--config', '--typescript'].includes(arg)) {
      const value = args[++index];
      if (!value || value.startsWith('--')) throw new Error(`${arg} requires a value`);
      if (arg === '--source') options.sources.push(value);
      else options[arg.slice(2)] = value;
    } else throw new Error(`Unknown argument: ${arg}`);
  }
  return options;
}

function isStringArray(value) {
  return Array.isArray(value) && value.every((item) => typeof item === 'string' && item.trim().length > 0);
}

function relativePath(root, value) {
  if (path.isAbsolute(value)) throw new Error(`Expected repository-relative path: ${value}`);
  const relative = path.relative(root, path.resolve(root, value));
  if (relative === '..' || relative.startsWith(`..${path.sep}`)) throw new Error(`Path outside repository: ${value}`);
  return relative.split(path.sep).join('/');
}

function run() {
  const options = parseArgs(process.argv.slice(2));
  const root = path.resolve(options.root);
  const config = options.config ? JSON.parse(fs.readFileSync(path.resolve(root, options.config), 'utf8')) : {};
  if (!config || typeof config !== 'object' || Array.isArray(config)) throw new Error('Config must be an object');
  for (const key of Object.keys(config)) {
    if (!['sourceRoots', 'failCategories', 'exceptions'].includes(key)) throw new Error(`Unknown config key: ${key}`);
  }
  const sources = options.sources.length ? options.sources : config.sourceRoots;
  if (!isStringArray(sources) || !sources.length) throw new Error('Provide --source or nonempty sourceRoots');
  const failCategories = config.failCategories ?? ['non-semantic-action'];
  if (!isStringArray(failCategories) || failCategories.some((item) => !categories.has(item))) throw new Error('Invalid failCategories');
  const exceptions = config.exceptions ?? [];
  if (!Array.isArray(exceptions)) throw new Error('exceptions must be an array');
  for (const entry of exceptions) {
    if (!entry || typeof entry !== 'object' || Array.isArray(entry) ||
        Object.keys(entry).some((key) => !['file', 'category', 'reason', 'marker'].includes(key)) ||
        typeof entry.file !== 'string' || !entry.file.trim() || !categories.has(entry.category) ||
        typeof entry.reason !== 'string' || !entry.reason.trim() ||
        (entry.marker !== undefined && (typeof entry.marker !== 'string' || !entry.marker.trim()))) {
      throw new Error('Each exception requires file, category, reason and optional literal marker');
    }
    entry.file = relativePath(root, entry.file);
  }
  const files = new Set();
  function collect(directory) {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      const target = path.join(directory, entry.name);
      if (entry.isDirectory() && !ignoredDirectories.has(entry.name)) collect(target);
      else if (entry.isFile() && /\.[tj]sx$/.test(entry.name) && !/\.(test|spec|stories)\.[tj]sx$/.test(entry.name)) files.add(target);
    }
  }
  for (const source of sources) {
    const directory = path.join(root, relativePath(root, source));
    if (!fs.existsSync(directory) || !fs.statSync(directory).isDirectory()) throw new Error(`Missing source directory: ${source}`);
    collect(directory);
  }
  if (!files.size) throw new Error('No TSX/JSX files scanned');
  const requireFromProject = createRequire(path.join(root, 'package.json'));
  let ts;
  try {
    ts = requireFromProject(options.typescript ? path.resolve(options.typescript) : 'typescript');
  } catch {
    throw new Error('TypeScript unavailable; install project dependencies or pass --typescript <compiler-file>');
  }
  if (!ts.createSourceFile) throw new Error('Requires TypeScript JavaScript compiler API (tested with 5.x); pass --typescript <compatible-compiler-file>');
  const findings = [];
  function literal(initializer) {
    if (initializer && ts.isJsxExpression(initializer)) initializer = initializer.expression;
    return initializer && ts.isStringLiteral(initializer) ? initializer.text : undefined;
  }
  for (const file of [...files].sort()) {
    const sourceFile = ts.createSourceFile(file, fs.readFileSync(file, 'utf8'), ts.ScriptTarget.Latest, true,
      file.endsWith('.jsx') ? ts.ScriptKind.JSX : ts.ScriptKind.TSX);
    if (sourceFile.parseDiagnostics.length) throw new Error(`Cannot parse ${file}: ${ts.flattenDiagnosticMessageText(sourceFile.parseDiagnostics[0].messageText, ' ')}`);
    const relative = path.relative(root, file).split(path.sep).join('/');
    function add(node, category, detail, marker) {
      const exception = exceptions.find((entry) => entry.file === relative && entry.category === category &&
        (entry.marker === undefined || entry.marker === marker));
      findings.push({ file: relative, line: sourceFile.getLineAndCharacterOfPosition(node.getStart(sourceFile)).line + 1,
        category, detail, ...(exception ? { exceptionReason: exception.reason } : {}) });
    }
    function visit(node) {
      if (ts.isImportDeclaration(node) && node.moduleSpecifier.text === 'next/link') add(node, 'direct-next-link', 'next/link import');
      if (ts.isJsxOpeningElement(node) || ts.isJsxSelfClosingElement(node)) {
        const tag = node.tagName.getText(sourceFile);
        const attributes = new Map(node.attributes.properties.filter(ts.isJsxAttribute).map((attr) => [attr.name.getText(sourceFile), attr.initializer]));
        const marker = literal(attributes.get('data-interaction-exception'));
        const handlers = [...attributes.keys()].filter((name) => handlerNames.has(name));
        if (nonSemanticTags.has(tag) && handlers.length) add(node, 'non-semantic-action', `<${tag}> ${handlers.join(', ')}`, marker);
        if (tag === 'button') add(node, 'raw-button', '<button>', marker);
        if (tag === 'a') add(node, 'raw-anchor', '<a>', marker);
        const inputType = literal(attributes.get('type'));
        if (tag === 'input' && inputTypes.has(inputType)) add(node, 'raw-action-input', `<input type=${inputType}>`, marker);
        if (attributes.has('clickable') || attributes.has('onTap')) add(node, 'clickable-abstraction', `<${tag}> clickable/onTap`, marker);
      }
      ts.forEachChild(node, visit);
    }
    visit(sourceFile);
  }
  const violations = findings.filter((finding) => failCategories.includes(finding.category) && !finding.exceptionReason);
  const summary = {};
  for (const finding of findings) summary[finding.category] = (summary[finding.category] ?? 0) + 1;
  const report = { filesScanned: files.size, summary, findings, violations };
  if (options.isJson) console.log(JSON.stringify(report, null, 2));
  else {
    console.log(`Scanned ${files.size} files; ${violations.length} policy violations`);
    for (const finding of findings) console.log(`${finding.file}:${finding.line}\t${finding.category}\t${finding.detail}${finding.exceptionReason ? ` [exception: ${finding.exceptionReason}]` : ''}`);
  }
  if (options.shouldCheck && violations.length) process.exitCode = 1;
}

try { run(); } catch (error) {
  console.error(error.message);
  process.exitCode = 2;
}
