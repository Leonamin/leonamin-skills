# Artifacts

Use lightweight artifacts when the task needs auditability, handoff, or review. Prefer repository-local conventions if they exist.

## Contract

Create or identify a contract before implementation for high-risk or ticket-bound work. If the repository has no convention, use a path such as:

```text
.agents/tasks/{task-id}/contract.md
```

Include:

- Goal
- Non-goals
- Allowed files or modules
- Forbidden files or modules
- Constraints and assumptions
- Verification plan
- Required evidence
- Completion criteria
- Approval criteria, if user approval is needed

## Evidence

After implementation, write evidence when the work is nontrivial, reviewed, or delegated. If the repository has no convention, use:

```text
.agents/tasks/{task-id}/evidence.md
```

Include:

- Change summary
- Changed files
- Verification commands actually run
- Command results, including failures
- Screenshot or recording paths for UI work
- Migration, deployment, or operational impact
- Remaining risks

## Review

For read-only review output, use the repository convention or:

```text
.agents/tasks/{task-id}/review.md
```

Include:

- Findings, ordered by severity
- Open questions
- Verification gaps
- Scope or contract deviations
- Completion judgment: Complete, Needs fixes, or Blocked

## Handoff

Use a handoff note when the work spans sessions, agents, or worktrees. Include:

- User request
- Current repository, branch, and worktree
- Diff base or latest commit
- Scope and non-goals
- Completed work
- Remaining work
- Commands run and outcomes
- Running local services and how to stop them
- Known risks or blockers

## Do Not Claim Completion When

- Required approval is missing.
- Required verification did not run.
- Evidence is missing for evidence-required work.
- Review is missing for review-required work.
- UI work lacks screenshot or browser evidence.
- Blocking reviewer findings are unresolved.
- Production-impacting changes were not validated in the required environment.
