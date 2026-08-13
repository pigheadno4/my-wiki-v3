# Rule: GitHub repository collection and serial ingest

> This is the common GitHub workflow authority. Read it first, then read the strategy rule selected below before acting.

## Route by registry policy

Load `tracking/github/repo-registry.toml` and route by `version_strategy`:

- `monorepo-packages`, `semver-tags`, or `github-release`: read `rules/github/release-tracked.md`.
- `commit`: read `rules/github/commit-tracked.md`.
- any `supplement` command: also read `rules/github/supplements.md` before collection.

Scripts execute adapters from reviewed registry data. Scripts do not parse Markdown rules to choose behavior. Do not create a rule file per repository; repository-specific paths and limits belong in its registry capsule.

Tests and fixtures may be excluded by reviewed capsule policy. Stories remain eligible when they document supported component states or integration behavior; do not classify stories as tests by default.

## Authorities and generated state

`tracking/github/repo-registry.toml` is the only human-maintained repository registry. It stores stable intent: identity, company, URL, priority, cadence, strategy, and capsule policy. Mutable SHAs, versions, dates, failures, comparisons, and ingest progress belong under `tracking/github/`.

The collector atomically maintains two repository-level views:

```text
tracking/github/collection-index.json
tracking/github/collection-index.md
```

Use the index to find each repository's strategy, cadence, latest state, and next action. `tracking/github/status.md` remains the detailed work-item lifecycle view. Neither generated file is manually edited.

Raw evidence is immutable. One exact SHA snapshot lives at:

```text
raw/github/<company>/<repo>/snapshots/<collection-date>-<short-sha>/
+-- manifest.json
+-- files/
```

Generated comparisons and packets are navigation and review evidence. Exact claims remain grounded in linked immutable snapshots.

## Common commands and approval boundary

```bash
python3 scripts/collect_github_repos.py collect --repo <owner/repo> --mode backfill
python3 scripts/collect_github_repos.py collect --repo <owner/repo> --mode future
python3 scripts/collect_github_repos.py collect-ref --repo <owner/repo> --from <full-sha> --to <full-sha>
python3 scripts/collect_github_repos.py status
python3 scripts/collect_github_repos.py approve --item <id> --mode <full|delta>
python3 scripts/collect_github_repos.py next-ingest
python3 scripts/collect_github_repos.py complete-ingest --item <id>
python3 scripts/collect_github_repos.py fail-ingest --item <id> --error <bounded-reason>
python3 scripts/collect_github_repos.py retry --item <id>
```

Collection may discover and download more than one upstream item, but it must stop at `awaiting_approval`. Collection never approves, starts ingest, or edits wiki knowledge.

Use `collect-ref` only for a reviewed ancestor-to-descendant boundary, including an untagged documentation or policy change. It stores immutable snapshots for both exact SHAs, compares the selected capsule, and creates one approval-gated ref work item. It does not create a package release record or imply that the ending commit was released.

The required operator sequence is:

```text
collect -> review packet -> user approve -> next-ingest
```

Read both packet files and every path in the combined required-reading list before approval. Any evidence gap, unclassified retained change, invalid identity, failed hash, unsafe path, secret finding, or exceeded budget requires correction or manual review.

## Full and delta decisions

Use `full` for an initial baseline, major boundary, broad architecture or payment-behavior change, incompatible public API change, capsule-policy change, missing prior evidence, or unbounded security impact.

Use `delta` only for a contained update where every upstream change has a disposition, retained changes are classified, required evidence exists, and no full signal applies. Version numbers alone do not override evidence.

The collector recommends mode and priority. Only the user approves or overrides mode.

## Serial ingest boundary

Ingest exactly one approved SHA work item at a time. `next-ingest` atomically claims the oldest approved item and fails while another item is `ingesting`.

For every ingest, read the complete cumulative source page first. Then read every packet and attachment path in full, one by one.

For `full`, read the complete current snapshot and relevant prior history. Add the new baseline or major knowledge to the cumulative page; do not replace validated older-version knowledge.

For `delta`, read every changed retained file and linked comparison/history section in full. Update affected knowledge and append history. Unchanged historical raw files need not be reread.

Follow `rules/ingest.md` for concept audit, contradiction checks, indexes, logs, and focused validation. Do not begin another work item until the current item reaches a terminal ingest state.

## Wiki output and query use

One repository uses one cumulative source page and one separate changelog:

```text
wiki/sources/<company>/github/source-github-<repo>.md
wiki/sources/<company>/github/changelog-github-<repo>.md
```

The source page owns durable architecture, APIs, version-qualified behavior, compatibility, evidence gaps, and immutable evidence links. Full ingest adds history rather than refreshing to latest-only content.

The changelog owns chronological release or commit synthesis and must retain version/ref identities, impact, migration notes, updated sections, and raw links. For repository-version or update questions, search both the cumulative source page and that repository's changelog before drawing a conclusion. The changelog alone is insufficient for deep implementation claims.

Keep repositories independent. Cross-repository questions must identify which repository owns each claim and must not merge their evidence histories.

## Failure protection

Build evidence in temporary storage and publish only after selection, hashing, UTF-8 checks, secret scanning, budgets, and manifest validation succeed. Failure must not publish partial raw evidence, enter approval, alter accepted snapshots, or change wiki knowledge.

Retry transient Git, network, and filesystem-read failures at most three times in one run. After exhaustion, record `collection_failed` with bounded error text, attempt count, and date. After three consecutive failed runs, set `needs_manual_review` and stop automatic retries.

Invalid policy, invalid refs, access denial, unsafe paths, secrets, and budget overflow go directly to `needs_manual_review`. An explicit retry may resume after correction. Existing accepted evidence remains immutable.

## Validation

Run:

```bash
python3 scripts/validate_github_collection.py
```

The validator checks registry policy, snapshots, release/ref comparisons, packets, work items, generated status and collection indexes, and cumulative source/changelog links. It is offline and deterministic.
