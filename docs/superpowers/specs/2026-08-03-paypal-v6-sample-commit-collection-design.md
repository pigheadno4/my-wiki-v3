# PayPal v6 Sample Commit Collection Design

**Date:** 2026-08-03
**Status:** Approved design, pending written-spec review
**Pilot repository:** `paypal-examples/v6-web-sdk-sample-integration`

## Purpose

Collect the current default-branch state of PayPal's v6 Web SDK sample application as bounded, immutable GitHub evidence and prepare it for approval-gated serial ingest.

This pilot also adds a reusable collection and comparison strategy for repositories that evolve through default-branch commits rather than package releases. It must not fabricate semantic versions or release records for sample applications, specifications, documentation sources, or API collections.

## Approved Scope

The first pilot collects one current default-branch SHA only. It does not select a historical commit and does not perform an initial commit-to-commit comparison.

During design discovery on 2026-08-03, the remote default branch resolved to commit `b5f2df209b0bfd10b1a3cde600088ddf21e43523`, committed on 2026-07-15. The actual collection run must resolve the default branch again and use the exact SHA found at run time. The design-time SHA is context, not a pinned collection target.

The baseline includes all selected browser and Node server payment integration source. It excludes tests, lockfiles, images, CI, deployment files, generated output, dependencies, Git metadata, and real environment files.

Collection does not authorize wiki ingest. A successfully collected work item stops at `awaiting_approval` until the user approves it.

## Why Commit Tracking Is Required

Existing executable repository profiles are release-oriented:

- `npm-tracked-source-v1` resolves package-qualified releases in an NPM workspace.
- `tagged-tree-v1` maps a semantic Git tag to one package-qualified release.

The sample repository has browser and server package manifests reporting internal version `1.0.0`, but those versions are not advanced as the default branch changes. Treating them as release identities would cause distinct repository states to appear unchanged. Creating a synthetic semantic version would also misrepresent upstream evidence.

Commit-tracked repositories therefore use repository identity, default-branch identity, and exact Git SHA. Package-release repositories continue using package-qualified versions without any behavior change.

## Strategy Layers

The GitHub workflow uses three distinct layers.

### Stable intent

`tracking/github/repo-registry.toml` remains the only human-maintained repository registry. It records stable configuration:

- repository identity and URL;
- company, type, and priority;
- collection frequency;
- tracking and version strategy;
- enabled state; and
- source-capsule policy.

Mutable SHAs, dates, failures, comparisons, and ingest states must not be written into the registry.

### Operational rules

`rules/github-repos.md` remains the common authority for immutable evidence, temporary clones, secret scanning, budgets, approval, serial ingest, retries, and validation.

Strategy-specific details move under:

```text
rules/github/
|-- release-tracked.md
|-- commit-tracked.md
+-- supplements.md
```

- `release-tracked.md` governs package releases, semantic tags, release notes, and release comparisons.
- `commit-tracked.md` governs default-branch SHA resolution, commit baselines, selected-evidence comparison, and commit history.
- `supplements.md` governs approved exact-SHA evidence additions without modifying accepted snapshots.

Repository-specific path differences stay in registry capsule configuration. The project must not create one rule file per repository.

### Generated collection index

The collector atomically maintains:

```text
tracking/github/collection-index.json
tracking/github/collection-index.md
```

The JSON file is the machine-readable repository-level collection and scheduling state. The Markdown file is a deterministic operator view generated from the JSON. Neither file is manually edited.

`tracking/github/status.md` remains the detailed work-item lifecycle view. The collection index is repository-oriented and does not replace work-item status.

## Adapter Design

Add `commit-tree-v1` as a third capsule adapter.

### Registry compatibility

An enabled release-tracked repository continues to require:

- `version_strategy` of `monorepo-packages`, `semver-tags`, or a supported release strategy;
- package-qualified version tracks; and
- exactly one supported release capsule.

An enabled commit-tracked repository instead requires:

- `version_strategy = "commit"`;
- `track = "default-branch"`;
- no semantic version tracks;
- exactly one `commit-tree-v1` capsule; and
- one safe repository evidence identity in `source_id`.

Capsule schema becomes adapter-specific:

- release adapters require `focus_packages` and forbid `source_id`;
- `commit-tree-v1` requires `source_id` and forbids `focus_packages`, generated target paths, and package overrides.

This prevents package terminology from being reused for a repository commit.

### Pilot registry shape

The executable pilot row will follow this structure:

```toml
[[repos]]
id = "paypal-examples/v6-web-sdk-sample-integration"
collection_frequency = "monthly"
company = "paypal"
url = "https://github.com/paypal-examples/v6-web-sdk-sample-integration"
enabled = true
repo_type = "sample-app"
priority = "tier1"
track = "default-branch"
version_strategy = "commit"

[[repos.capsules]]
id = "paypal-v6-sample-source"
adapter = "commit-tree-v1"
source_id = "v6-web-sdk-sample-integration"
dependency_scope = "configured-repository-paths"
changed_path_policy = "policy-bounded"
default_required_roots = [
  "client/components",
  "client/prebuiltPages/react/src",
  "client/shared",
  "server/node/src",
]
include_paths = [
  ".env.sample",
  "LICENSE",
  "README.md",
  "client/index.html",
  "client/package.json",
  "client/prebuiltPages/react/README.md",
  "client/prebuiltPages/react/package.json",
  "client/prebuiltPages/react/tsconfig.json",
  "client/prebuiltPages/react/vite.config.ts",
  "server/node/README.md",
  "server/node/package.json",
  "server/node/tsconfig.json",
]
excluded_categories = ["tests", "fixtures"]
secret_detector = "text-secrets-v1"
```

Final numeric file and byte budgets must be set from a dry-run inventory with modest headroom. Budget values are reviewed configuration, not discovered mutable state.

## Pilot Evidence Boundary

### Included

The capsule retains:

- root and server documentation;
- `.env.sample` placeholders needed to understand configuration;
- browser JavaScript, TypeScript, HTML, and CSS examples;
- React prebuilt-page source;
- Node server source;
- package manifests and selected TypeScript or build configuration;
- PayPal one-time payment, redirect, direct app switch, async validation, and iframe examples;
- PayPal and card save-payment flows;
- vault-with-purchase flows;
- subscriptions;
- Venmo;
- Card Fields and 3D Secure;
- Apple Pay and Google Pay;
- ACH, Fastlane, Messages, guest checkout, and local payment methods;
- server authentication, Orders, capture, Vault, Subscriptions, eligibility, and product-catalog validation.

### Excluded

The capsule excludes:

- test files and test configuration used only to run tests;
- package lockfiles;
- image assets;
- `.github/` configuration and workflows;
- deployment files such as `fly.toml` and deployment-only Docker configuration;
- generated output and dependency directories;
- `.git/` data; and
- real `.env` files.

The snapshot is example implementation evidence. It does not prove merchant eligibility, regional availability, production certification, or complete behavior of delegated PayPal SDK and API runtimes.

## Commit Work-Item Contract

Commit-tracked work items must not create package release records.

A work item contains exactly one change family:

- release-tracked items use existing `package_changes`; or
- commit-tracked items use `ref_changes`.

They cannot contain both.

One `ref_changes` entry records:

```json
{
  "ref_kind": "default-branch",
  "ref_name": "main",
  "from_sha": "",
  "to_sha": "b5f2df209b0bfd10b1a3cde600088ddf21e43523",
  "display_identity": "default-branch@b5f2df2",
  "comparison_manifest": "",
  "reasons": ["initial-commit-baseline"],
  "recommended_mode": "full"
}
```

The baseline has an empty `from_sha`. Later work items use the last accepted selected-evidence SHA as `from_sha` and the newly resolved exact SHA as `to_sha`.

The review packet includes:

- repository and exact ref identity;
- author and commit dates;
- snapshot manifest;
- selected and excluded file inventories;
- required reading;
- existing wiki context;
- selected-evidence changes;
- unclassified changes and evidence gaps;
- full or delta recommendation; and
- expected cumulative source, commit changelog, company, concept, index, and log targets.

## Snapshot and Comparison Layout

The immutable snapshot uses the existing layout:

```text
raw/github/paypal-examples/v6-web-sdk-sample-integration/
+-- snapshots/<collection-date>-<short-sha>/
    |-- manifest.json
    +-- files/
```

No directory is created under `releases/` for a commit baseline.

Later comparisons use:

```text
tracking/github/repos/paypal-examples/v6-web-sdk-sample-integration/
+-- comparisons/default-branch/<from-short-sha>--<to-short-sha>/
    |-- comparison.json
    |-- comparison.md
    +-- diff.patch
```

Comparison artifacts are navigation evidence. Wiki implementation claims remain grounded in exact immutable snapshot files.

## Collection Procedure

For `version_strategy = "commit"`:

1. Clone into temporary storage using the existing retry policy.
2. Resolve the remote default branch and its exact commit SHA.
3. Pin all subsequent tree reads to that exact SHA.
4. Read the configured `commit-tree-v1` capsule policy.
5. Select required roots and literal include paths.
6. Classify and record excluded files.
7. Scan selected text for secrets, unsafe paths, unsupported blobs, and size violations.
8. Hash every selected file and construct the manifest in temporary storage.
9. Compare the selected-evidence fingerprint with the last accepted commit snapshot.
10. Publish the snapshot atomically only when selected evidence is new and valid.
11. Create a baseline or comparison packet and a commit work item.
12. Regenerate repository collection index and work-item status views.
13. Stop at `awaiting_approval`.

Existing commands retain strategy-specific semantics:

- `collect --repo <commit-repo> --mode backfill` collects the current default branch only when no accepted baseline exists.
- `collect --repo <commit-repo> --mode future` checks the current default branch against the accepted baseline.
- `collect --repo <commit-repo> --release ...` fails because commit repositories do not expose package releases.

## Future Comparison Classification

The collector first compares exact SHA and selected-evidence fingerprint.

| Condition | Result |
| --- | --- |
| Default-branch SHA unchanged | `unchanged` |
| SHA changed but selected evidence is byte-identical | Record check; no snapshot or work item |
| Only excluded files changed | Record check; no snapshot or work item |
| Contained selected-source change | Publish comparison; recommend `delta` |
| Initial baseline | Publish snapshot; recommend `full` |
| Broad architecture or payment-flow change | Publish comparison; recommend `full` |
| Unsafe, secret, unsupported, or over-budget evidence | `needs_manual_review` |

Broad-change signals include:

- server route or authentication architecture changes;
- new or removed payment flows;
- broad Web SDK initialization changes;
- Vault, Orders, Subscriptions, eligibility, or capture-flow changes;
- source movement across major client or server boundaries; and
- a change set exceeding reviewed file or byte thresholds.

Tests, lockfiles, images, CI, and deployment-only changes cannot trigger wiki ingest because they are outside the capsule.

## Generated Collection Index

The repository-level JSON row records at least:

```json
{
  "repo_id": "paypal-examples/v6-web-sdk-sample-integration",
  "company": "paypal",
  "enabled": true,
  "priority": "tier1",
  "strategy": "commit",
  "adapter": "commit-tree-v1",
  "frequency": "monthly",
  "last_checked_date": "2026-08-03",
  "last_accepted_ref": "default-branch@b5f2df2",
  "latest_discovered_ref": "default-branch@b5f2df2",
  "comparison_base": "b5f2df209b0bfd10b1a3cde600088ddf21e43523",
  "queue_state": "awaiting_approval",
  "next_due_date": "2026-09-03",
  "next_action": "review-full",
  "last_error": ""
}
```

Dates and refs above illustrate the schema. Generated values come from the actual collection run.

`next_action` is one of:

- `disabled`;
- `collect-baseline`;
- `wait`;
- `review-delta`;
- `review-full`;
- `ingest`;
- `retry`; or
- `manual-review`.

The index includes enabled and disabled registry repositories so it also represents remaining coverage. Only enabled and due rows are executable.

The first implementation generates scheduling state and retains per-repository collection commands. It does not add a batch scheduler or unattended wiki ingest.

## Ingest and Wiki Output

After explicit approval, `next-ingest` selects the oldest approved item and moves it to `ingesting`. Baseline ingest reads every required packet and snapshot file in full, one by one.

The pilot creates or updates:

```text
wiki/sources/paypal/github/source-github-v6-web-sdk-sample-integration.md
wiki/sources/paypal/github/changelog-github-v6-web-sdk-sample-integration.md
wiki/companies/paypal.md
wiki/paypal-index.md
wiki/paypal-log.md
wiki/log.md
```

Concept pages are created or updated only after the required concept audit. The source page owns cumulative integration knowledge. The separate changelog owns chronological commit history and uses commit-qualified entries rather than package release entries.

The source page must distinguish:

- sample implementation from product documentation;
- browser responsibilities from merchant-server responsibilities;
- payment presentation from final server status;
- sample support from merchant eligibility; and
- repository evidence from delegated PayPal SDK and API runtime behavior.

## Failure Handling

- Transient clone, network, and filesystem-read failures retry at most three times in one run.
- The default branch is resolved once per run; subsequent reads use the exact resolved SHA even if the remote branch moves.
- Snapshots are published only after complete selection, hashing, scanning, budget, and manifest validation.
- A failed collection leaves no partial snapshot, release record, comparison, or approval item.
- Secret findings, unsafe paths, unsupported selected files, and capsule-budget overflow go directly to `needs_manual_review`.
- Later runs retain stable failure identity and follow the existing consecutive-run retry threshold.
- Accepted snapshots remain immutable and are never rewritten by a retry.
- Generated JSON and Markdown must be regenerated atomically and validate as equal views of the same state.

## Verification Strategy

Fixture-based tests cover:

- parsing and validation of commit adapter registry policy;
- rejection of version tracks or `focus_packages` on commit adapters;
- rejection of `source_id` on release adapters;
- default-branch baseline resolution;
- unchanged exact SHA;
- changed SHA with byte-identical selected evidence;
- excluded-only changes;
- contained selected-source delta;
- broad full recommendation;
- added, deleted, renamed, and modified selected files;
- secret, unsafe-path, binary, file-budget, and byte-budget rejection;
- atomic failure with no published partial evidence;
- `package_changes` and `ref_changes` mutual exclusion;
- commit packet and comparison rendering;
- collection-index JSON and Markdown agreement;
- approval, `next-ingest`, failure, retry, and completion transitions; and
- coexistence with NPM and tagged-tree repositories without changed behavior.

Deterministic verification runs the focused unit tests, the complete GitHub collection tests, and `scripts/validate_github_collection.py`.

After deterministic tests pass, one network-enabled dry run checks the current PayPal sample repository. The actual baseline collection is a separate approved action after dry-run findings are reviewed.

## Non-Goals

This enhancement does not:

- automatically edit wiki pages;
- automatically approve or ingest work items;
- add an unattended periodic scheduler;
- backfill arbitrary historical commits;
- collect complete Git history;
- infer product eligibility from sample presence;
- execute sample builds or package managers during collection;
- recursively download dependencies, submodules, or Git LFS assets; or
- create repository-specific collector code.

## Acceptance Criteria

The design is implemented when:

1. Commit-tracked rows can be enabled without fake package versions.
2. Release-tracked behavior remains unchanged and fully validated.
3. The PayPal sample dry run produces a bounded, inspectable selected-file inventory without publishing raw evidence.
4. The approved real collection publishes one immutable exact-SHA snapshot and one commit work item, with no release record.
5. The generated collection index routes the repository to the commit strategy and reports its lifecycle state.
6. Collection stops before ingest and requires explicit user approval.
7. All deterministic validators and GitHub collection tests pass.
