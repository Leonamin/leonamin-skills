---
name: swarm
description: 복잡하거나 중요한 작업을 Planner, Read-only Architect, Executor, Reviewer 역할로 분리해 진행한다. 사용자가 중요한 작업, 급한 구현 위임, 여러 에이전트 역할 분리, sub-agent, 병렬 작업, 설계 검토, read-only 리뷰, evidence, handoff, reviewer report를 요청할 때 사용한다.
---

# Swarm Orchestrator

## Purpose

Use this skill to split complex or high-risk work into explicit roles, evidence, and review gates. Treat it as an orchestration workflow, not as a requirement to use sub-agents for every task.

The current session is the Planner. The Planner owns scope, completion criteria, role assignment, integration, and final reporting.

## Core Principles

- Discover and follow the target repository's local rules before assigning work.
- Keep Architect and Reviewer read-only.
- Give Executor agents narrow ownership of files, modules, or worktrees.
- Avoid overlapping write sets unless the Planner will manually integrate the work.
- Never ask agents to modify files outside the approved scope.
- Do not mark work complete until verification evidence has been produced and reviewed.
- If a repository has stronger local rules than this skill, follow the repository rules.

## Start Here

Inspect the project before deciding how much orchestration is needed:

```bash
git branch --show-current
git status --short --branch
git worktree list
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'README.md' -g 'docs/**' -g '.agents/**'
```

Also check any user-provided issue, ticket, contract, spec, or PR link. Do not assume branch names, worktree layout, package manager, test commands, or artifact paths; infer them from the repository or ask only when they cannot be discovered safely.

## Decide the Workflow

Use a single session for small, clear, local tasks:

- Questions or analysis-only requests
- Documentation typo fixes
- Single-file edits with obvious behavior
- Local changes that do not need independent design or review

Use role separation when any of these apply:

- The user asks for swarm, sub-agents, role separation, delegation, parallel work, Architect, Executor, or Reviewer.
- The task affects data, auth, billing, permissions, deployment, migrations, infrastructure, or production behavior.
- The task spans multiple apps, packages, services, repositories, or owners.
- There is a ticket, contract, acceptance criteria, or nontrivial spec to satisfy.
- UI work needs screenshots, browser verification, or user-flow validation.
- The user calls the task important, urgent, risky, or asks for evidence/reviewer reports.

For more detail, read `references/decision-rules.md`.

## Standard Workflow

1. Scope Intake
   - Summarize the goal, non-goals, constraints, allowed files, forbidden files, verification commands, and completion criteria.
   - Identify the repository rules and any ticket/spec/contract that controls the work.

2. Planning Gate
   - For high-risk work, create or identify a lightweight contract before implementation.
   - Include objective, non-goals, allowed scope, forbidden scope, validation, evidence, and approval criteria.
   - Pause if the user request conflicts with the controlling contract or repository rules.

3. Architect Pass
   - Use a Read-only Architect when design risk, unknown patterns, or broad impact justify it.
   - Ask for implementation shape, existing patterns, risks, likely files, and verification plan.
   - Do not let the Architect edit files, run formatters, commit, or start long-lived services.

4. Execution
   - Assign implementation only after scope and ownership are clear.
   - Use one Executor for a tightly coupled change.
   - Use multiple Executors only when their write sets are disjoint.
   - Require each Executor to report changed files, verification commands, outputs, and remaining risks.

5. Review
   - Use a read-only Reviewer for important, risky, UI, PR-bound, or user-requested review work.
   - Review against the contract, repository rules, diff, tests, screenshots, and evidence.
   - Treat blocking findings as Planner work to resolve before completion.

6. Completion
   - Confirm required artifacts exist and verification actually ran.
   - Report the final state, changed files, tests, evidence, review result, and residual risk.

For artifact expectations, read `references/artifacts.md`. For copy-ready role prompts, read `references/role-prompts.md`.

## Sub-Agent Rules

- Use sub-agents only when the user requests them or the task risk justifies the overhead.
- Pass raw task context, paths, constraints, and expected output format; do not pass hidden conclusions as facts.
- Keep read-only roles read-only in the prompt and verify they did not change files.
- Give each Executor a specific working directory, branch/worktree if applicable, allowed files, forbidden files, and verification commands.
- Do not send the same broad prompt to several agents unless the goal is independent review.
- After each agent returns, inspect its claims against the filesystem, diff, and command output.

## Reference Files

- `references/decision-rules.md`: role split, skip, and stop conditions.
- `references/artifacts.md`: contract, evidence, review, and handoff expectations.
- `references/role-prompts.md`: generic prompts for Architect, Executor, Reviewer, and handoff.
