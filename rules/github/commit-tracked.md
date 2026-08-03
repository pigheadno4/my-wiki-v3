# Rule: Commit-tracked GitHub repositories

> Read `rules/github-repos.md` first. This rule applies when `version_strategy = "commit"`.

## Identity and policy

An enabled commit repository requires `track = "default-branch"`, no version tracks, and exactly one `commit-tree-v1` capsule with a safe `source_id`. The source identity is repository evidence metadata, not a package name or fabricated semantic release.

Resolve the upstream default branch once per run and pin every read to its exact full SHA. A commit work item uses only `ref_changes`; it must not contain `package_changes` or create package release records.

## Collection and comparison

For a new repository, collect one bounded baseline of all policy-selected source. For later runs:

1. Resolve the current default-branch SHA.
2. Compare its selected path/hash fingerprint with the latest accepted snapshot.
3. If the SHA and selected evidence are unchanged, record the check and publish no work item.
4. If only excluded files changed, record the new ref check and publish no snapshot or ingest item.
5. If selected evidence changed, publish a new exact-SHA snapshot, a default-branch comparison, and one `ref_changes` work item.
6. Build the commit review packet and stop at `awaiting_approval`.

Commit comparisons live at:

```text
tracking/github/repos/<company>/<repo>/comparisons/default-branch/<from-short-sha>--<to-short-sha>/
```

The packet records selected and excluded changes, author/commit dates, required reading, expected wiki targets, evidence gaps, and the deterministic full/delta recommendation. Do not infer merchant eligibility, regional availability, certification, or delegated runtime behavior from sample source alone.

## Scheduling and ingest

Use `tracking/github/collection-index.json` or its Markdown view to route periodic checks. Only enabled and due repositories are executable. The index invokes common collector behavior through registry strategy; it is not a batch-ingest queue.

A baseline is `full`. A later bounded change may be `delta`; broad server architecture, authentication, payment-flow, initialization, or policy changes require `full` review.

The cumulative source page keeps current and historical commit-qualified findings. The changelog records `default-branch@<short-sha>` transitions, exact SHAs, dates, impact, changed source sections, and comparison/snapshot links.
