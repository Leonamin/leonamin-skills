# Decision Rules

## Use Role Separation

Use Planner, Architect, Executor, and Reviewer roles when at least one condition is true:

- The user asks for role separation, delegation, sub-agents, parallel work, or swarm.
- The task has a ticket, contract, acceptance criteria, or explicit approval gate.
- The change touches data model, migrations, auth, permissions, billing, payments, deployment, infrastructure, or production behavior.
- The change spans multiple apps, packages, services, repositories, or ownership areas.
- The work modifies core user flows or externally visible behavior.
- The work needs screenshots, evidence, reviewer reports, or auditable completion.
- The cost of a wrong implementation is high enough that independent design or review is useful.

## Stay In One Session

Skip role separation when the work is small and local:

- Answering questions
- Reading or summarizing code
- Fixing a typo or small documentation issue
- Making a clear single-file change with low blast radius
- Running a straightforward command and reporting the result

## Architect Can Be Skipped

Skip the Architect pass when all of these are true:

- The implementation pattern is already obvious from nearby code.
- The write scope is small and cohesive.
- Failure is easy to detect and low impact.
- The Planner has inspected the relevant files and repository rules.

## Reviewer Should Not Be Skipped

Use a Reviewer when any of these are true:

- A PR will be opened or merged.
- A ticket or contract will be marked complete.
- UI behavior changed.
- Data, auth, payments, infra, deployment, or production behavior changed.
- Multiple Executors contributed changes.
- The user described the task as important, urgent, risky, or asked for review.

## Stop And Ask

Pause for user confirmation when:

- Required credentials, access, or files are missing.
- A contract is required but absent.
- The user request conflicts with repository rules or the contract.
- The implementation requires modifying forbidden or out-of-scope files.
- Existing local changes overlap with planned edits and ownership is unclear.
- The next step may affect production data, billing, deployment, or external users.
- Verification would require a long-running service, paid resource, or destructive operation the user has not approved.

## Model And Agent Selection

- Assign the strongest available model to Architect or Reviewer when the user explicitly asks for highest-quality reasoning.
- Prefer fewer agents when the task is tightly coupled.
- Add Executors only when file ownership and integration boundaries are clear.
- Keep Planner responsible for final integration, verification, and user-facing conclusions.
