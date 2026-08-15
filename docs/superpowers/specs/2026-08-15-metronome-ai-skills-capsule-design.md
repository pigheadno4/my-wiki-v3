# Metronome AI Skills Capsule Design

**Date:** 2026-08-15
**Repository:** `metronome-industries/ai`
**Strategy:** commit-tracked default-branch baseline

## Goal

Collect a bounded exact-SHA baseline of Metronome's public AI skills and billing guidance for later serial wiki ingest. Preserve useful billing scenarios while excluding test-operation artifacts.

## Registry Policy

Enable the existing `metronome-industries/ai` tier-2 monthly registry entry. Keep `track = "default-branch"` and `version_strategy = "commit"`.

Add exactly one capsule:

- ID: `metronome-ai-skills`
- Adapter: `commit-tree-v1`
- Source identity: `metronome-ai`
- Dependency scope: `configured-repository-paths`
- Changed-path policy: `policy-bounded`
- Required root: `skills/`
- Excluded categories: tests and fixtures

Use conservative limits above the observed 39-file, 227,137-byte selected corpus:

- Maximum file size: 512 KB
- Maximum capsule files: 80
- Maximum capsule UTF-8 bytes: 1 MB
- Maximum packet files: 100
- Maximum packet UTF-8 bytes: 1.5 MB

## Selected Evidence

Collect all tracked files below `skills/`, including every `SKILL.md` and reference document. Explicitly include:

- `README.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `tests/dogfood/scenarios/add-new-product-to-existing.md`
- `tests/dogfood/scenarios/change-pricing-raise-rate.md`
- `tests/dogfood/scenarios/start-billing-saas-with-credits.md`

The three scenario files are retained as story-style integration evidence. Their location under `tests/` does not make them executable test authority.

Exclude:

- `tests/dogfood/runs/`
- `tests/dogfood/scorecards/`
- `tests/dogfood/README.md`
- fixtures and future ordinary test artifacts unless separately reviewed

## Collection Flow

1. Validate the registry and capsule policy.
2. Resolve the upstream default branch and exact full SHA.
3. Select, scan, hash, and publish the bounded immutable snapshot.
4. Create one baseline work item using `ref_changes`, recommended as `full`.
5. Generate the review packet and stop at `awaiting_approval`.

Collection must not approve the item, call `next-ingest`, or edit wiki knowledge.

## Expected Wiki Targets

After a separate user approval and complete serial read:

- `wiki/sources/metronome/github/source-github-ai.md`
- `wiki/sources/metronome/github/changelog-github-ai.md`

The cumulative source will distinguish repository-authored AI guidance from canonical Metronome API behavior. Scenario outcomes are test expectations and examples, not proof of production behavior or merchant configuration.

## Validation

Before packet review:

- `python3 scripts/validate_github_collection.py`
- focused registry tests for the new capsule
- `git diff --check`

Success means one valid immutable baseline and one approval-gated work item with no evidence gaps, unsafe paths, secret findings, unclassified retained changes, or exceeded budgets.

## Failure Handling

Network or Git failures use the common retry policy. Invalid policy, unsafe paths, secret findings, or budget overflow stop in `needs_manual_review` without publishing partial evidence or changing wiki pages.
