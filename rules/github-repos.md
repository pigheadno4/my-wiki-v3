# Rule: GitHub repository collection and versioned ingest

> This rule governs release-driven collection of SDKs, libraries, samples, tools, and specifications from GitHub. Collection may batch discovery, but wiki ingest is always user-approved and serial.

## Authority and scope

`tracking/github/repo-registry.toml` is the only human-maintained repository registry. Each row contains stable intent such as repository identity, company, URL, priority, release policy, and source-capsule policy. Mutable versions, SHAs, dates, failures, and ingest progress belong in generated state under `tracking/github/`.

Package releases always use package-qualified identities such as:

```text
@paypal/paypal-js@10.0.3
@paypal/react-paypal-js@10.0.0
```

Never interpret `v10` without first identifying the package. A repository can publish multiple independently versioned packages at one SHA.

The focused PayPal JS pilot retains:

- latest stable v8, latest stable v9, and every stable v10 release of `@paypal/paypal-js`;
- latest stable v8, latest stable v9, and every stable v10 release of `@paypal/react-paypal-js`; and
- chronological processing from v8 to v9 to v10, with semantic version, release date, and package tag as deterministic ordering inputs.

For a track configured with `future = "all-stable"`, periodic collection selects every stable release newer than the highest retained version. It does not backfill unretained historical gaps below that version; use an explicit release request or reviewed backfill policy for those.

The policy is registry-driven rather than hard-coded to PayPal. Add future repositories or companies by adding reviewed registry rows and capsule policies.
`enabled = true` means the row is executable by the current collector: it must have package-qualified version tracks and exactly one supported capsule policy. Keep inventory-only or unsupported rows disabled.

For the focused PayPal JS pilot, changed tests and fixtures remain excluded by capsule policy. Stories remain eligible because they document supported component states and integration behavior. Explicitly required public targets still take precedence over category exclusions.

### Tagged repository profile

Use `tagged-tree-v1` when one semantic Git tag maps to one package-qualified release identity but the repository does not expose an NPM workspace. The adapter resolves the exact tag and emits one synthetic root package; repository roots, literal includes, exclusions, and limits remain reviewed data in `tracking/github/repo-registry.toml`.

The adapter does not run language parsers, package managers, or builds, and it does not create a synthetic `package.json`. A tagged capsule is bounded public API, implementation, build, and example evidence rather than a complete repository mirror. Missing implementation needed for a later approved query must be collected as an immutable supplement tied to the existing release SHA.

## Evidence layout

One exact repository SHA has one immutable source snapshot:

```text
raw/github/<company>/<repo>/snapshots/<collection-date>-<short-sha>/
+-- manifest.json
+-- files/
```

The snapshot contains the bounded public-source capsule, changed package evidence assigned to the release, and standard repository context such as README and license files. `manifest.json` records hashes, sizes, Git object IDs, classification reasons, package ownership, triggering release IDs, and the full SHA.

Each package release has a separate immutable release record:

```text
raw/github/<company>/<repo>/releases/<package-slug>/<version>/<collection-date>/
+-- manifest.json
+-- release-notes.md
```

Multiple package releases may link to the same SHA snapshot. Recollection with the same release-note hash reuses the existing record. Changed upstream notes create a new immutable dated revision; accepted evidence is never overwritten.

Generated package comparisons live under:

```text
tracking/github/repos/<company>/<repo>/comparisons/<package-slug>/<from>--<to>/
+-- comparison.json
+-- comparison.md
+-- diff.patch
+-- review-packet.json     # only after an ad hoc compare
+-- review-packet.md       # only after an ad hoc compare
```

Generated comparisons are navigation evidence. Exact source claims must remain grounded in the linked immutable snapshots.

Each newly collected work item has one immutable review packet:

```text
tracking/github/repos/<company>/<repo>/ingest-packets/<work-item-id>/
+-- packet.json
+-- packet.md
```

`packet.json` is the canonical machine-readable review contract. It records retained transitions, upstream dispositions, dependency and public-API changes, evidence gaps, unclassified changes, required reading, existing wiki context, expected wiki targets, and the deterministic mode and priority recommendation. `packet.md` is its hashed operator view. Historical work items created before this format may remain packetless; every newly finalized collection requires a packet.

When an approved query needs a source file excluded from the bounded snapshot, collect a separate immutable supplement under `raw/github/<company>/<repo>/supplements/`. A supplement never modifies or replaces the accepted snapshot.

## Collection procedure

Use `scripts/collect_github_repos.py` for the focused operations:

```bash
python3 scripts/collect_github_repos.py collect --repo <owner/repo> --mode backfill
python3 scripts/collect_github_repos.py collect --repo <owner/repo> --mode future
python3 scripts/collect_github_repos.py collect --repo <owner/repo> --release <package@version>
python3 scripts/collect_github_repos.py status
python3 scripts/collect_github_repos.py compare --repo <owner/repo> --from <package@version> --to <package@version>
python3 scripts/collect_github_repos.py supplement --repo <owner/repo> --sha <full-sha> --path <repo-relative-path>
python3 scripts/collect_github_repos.py approve --item <id> --mode full
python3 scripts/collect_github_repos.py next-ingest
python3 scripts/collect_github_repos.py complete-ingest --item <id>
python3 scripts/collect_github_repos.py fail-ingest --item <id> --error <bounded-reason>
python3 scripts/collect_github_repos.py retry --item <id>
```

Collection performs these steps:

1. Discover configured package releases before publishing queue state.
2. Recheck retained release tag SHAs and release-note hashes; skip only exact matches.
3. Group releases that share one SHA into one work item with separate package changes.
4. Fetch release-note evidence without publishing it.
5. Resolve the bounded source capsule, including changed source, docs, examples, and tests owned by included packages.
6. Publish or reuse the exact-SHA snapshot only after hashing and validation, then publish immutable release records.
7. Generate package-scoped comparisons against the prior selected release.
8. Build and atomically publish the ingest review packet.
9. Derive the work-item recommendation from that packet.
10. Stop in `awaiting_approval`.

Collection never approves an item, starts ingest, or changes wiki knowledge.

The required operator sequence is:

```text
collect -> review packet -> user approve -> next-ingest
```

Run `status` to see the packet link, priority, required-reading count, unclassified-change count, and evidence-gap count. Read both packet files before approval. `next-ingest` returns the selected work item and its packet summary; it is a lifecycle transition, not permission to skip packet evidence.

`compare` creates or reuses the package comparison and writes `review-packet.json` plus `review-packet.md` beside it. It is an ad hoc review operation only: it must not create or advance a work item, approve ingest, or edit wiki pages.

## Full and delta recommendation

Use `full` for a package baseline, major-version transition, incompatible public export change, capsule-policy change, missing prior snapshot, or a security impact that cannot be bounded by retained evidence.

Use `delta` for a contained patch or minor release when every upstream change has a disposition, no blocking evidence gap exists, no changed retained file is unclassified, and no full-ingest signal applies. Semantic version alone never overrides the evidence.

Priority is separate from mode. Payment, security, public-API, and policy-history signals may require `high` review even when the bounded ingest mode remains `delta`.

Any packet with an evidence gap, unclassified changed file, invalid identity, failed hash, or exceeded packet budget requires correction or manual review. Do not approve it as delta merely because the release is a patch.

The collector recommends; the user approves or overrides the mode. Packet generation is never ingest approval, and scripts do not edit wiki knowledge.

## Serial ingest boundary

Ingest exactly one approved SHA work item at a time. Never batch wiki ingest, even when collection discovered many releases.

`next-ingest` atomically changes the oldest approved item to `ingesting`. It fails while another item is already `ingesting`. End the lifecycle with `complete-ingest`; use `fail-ingest` when grounding or wiki validation cannot be completed.

For every ingest, read the complete current cumulative source page first.

For `full` ingest, also read in full:

- every path in the packet's `required_reading` and `wiki_context`;
- the complete current snapshot, including every retained file;
- all listed release and comparison history; and
- relevant prior-version source and changelog context.

A full ingest adds the new package or major-version knowledge to the stable source page. It does not replace the page with latest-only content. Preserve older validated version findings and evidence links unless correcting a proven factual error, exact duplicate, or wrong package/version attribution.

For `delta` ingest, also read in full:

- every path in the packet's `required_reading`;
- every path in the packet's `wiki_context`;
- each changed retained source, documentation, example, and story file; and
- every linked release note, comparison, and affected history section.

Do not batch or partially sample these lists: read each file in full, one by one. Update only affected knowledge and append the release history. Unchanged historical raw files do not need to be reread during delta ingest.

Follow `rules/ingest.md` for concept audit, contradiction checks, indexes, logs, and focused validation. Do not begin another work item until the current one reaches its terminal ingest state.

## Cumulative source and changelog

One repository uses one cumulative source page and one separate changelog:

```text
wiki/sources/<company>/github/source-github-<repo>.md
wiki/sources/<company>/github/changelog-github-<repo>.md
```

The source page owns durable repository knowledge:

- current package versions;
- purpose, architecture, and responsibility boundaries;
- separate package sections;
- separate major-version subsections where evidence exists;
- current and historical public APIs and integration behavior;
- compatibility and migration findings;
- evidence gaps; and
- path-qualified links to immutable snapshots.

The changelog owns chronological release synthesis. Keep separate package timelines and group releases sharing a SHA as one repository change set. Each entry records package-qualified from/to versions, release date, SHA, approved ingest mode, important change, developer or merchant impact, migration action, updated source sections, and links to release records, comparisons, snapshot manifests, and exact raw files.

The changelog is not sufficient evidence for deep implementation claims.

`paypal/paypal-checkout-components` is an independently collected repository with its own source page and history. It is not a subdirectory of `paypal/paypal-js`, and its behavior must not be merged into the PayPal JS evidence history. Cross-repository questions must identify which repository owns each claim.

## Failure protection

Build snapshots in temporary storage and publish only after collection, hashing, secret scanning, budgets, and manifest validation succeed. A failed attempt must not publish a partial snapshot, enter approval, alter the last successful snapshot, or change accepted wiki knowledge.

Retry transient Git, network, and filesystem-read failures at most three times in one run. After exhaustion, record `collection_failed` with bounded error text, attempt count, and date. A later periodic run may retry the same stable work-item identity. After three consecutive failed runs, set `needs_manual_review` and stop automatic retries.

Invalid registry policy, invalid tags, access denial, unsafe paths, secret findings, and budget overflow go directly to `needs_manual_review`. An explicit retry may resume after correction. Valid evidence collected before a later failure remains immutable and is reused.

## Validation

Run:

```bash
python3 scripts/validate_github_collection.py
```

The validator checks registry package policy, snapshot and release hashes, SHA links, package comparisons, canonical packet content and Markdown hashes, packet/work-item linkage, deterministic recommendations, required-reading containment, strict work-item state, generated status equality, and cumulative source/changelog evidence for ingested items. It is offline and deterministic.
