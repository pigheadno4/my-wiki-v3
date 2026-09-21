# stripe@22.5.0 ingest review

- Work item: `github-fdb611aa510b593685f6`
- Boundary: `stripe@22.4.0` -> `stripe@22.5.0`, SHA `65d99a2b76d0786d7cec8544920affadccc8b670`.
- User approved delta ingest and a focused-reading exception for this release only: fully read changed implementation and affected prior code, read the complete diff, mechanically verify manifests and unchanged historical evidence. No commit or push authorized.
- Raw snapshots and packet remain immutable. Other queued versions remain unapproved.

## Checklist

- [x] Evidence reading, hash verification, and grounding excerpts.
- [x] Concept audit and concept update before source changes. Updated existing `stripe-node-sdk`; no new concept needed. Checkout resource files are unchanged, so no unrelated checkout/payment concept expansion.
- [x] Cumulative source and separate changelog; retain prior versions. Added version-qualified facts and exact evidence links after concept update.
- [x] Company update; source count unchanged at 666 (existing sources updated, none created).
- [x] Concept reciprocity, comparison applicability, and contradiction check. Source/concept record wrong constant/helper names, low-level timestamp default and core/ESM object-check divergence; retain retry conflict. No substantive cross-company comparison, so none created.
- [x] Provider index update. Existing source/changelog/concept entries advanced; no root catalog addition needed.
- [x] Provider and root operation logs. Added one bounded entry without changing unrelated history.
- [x] Focused validation, complete this work item, and final state check.

## Reading progress

- Read cumulative source and changelog, packet Markdown, comparison Markdown, release manifest and notes.
- Read complete 3,575-line comparison diff, including excluded-file changes. Upstream `.claude/CLAUDE.md` is evidence, not local instructions. Reading upstream test diffs does not mean tests were run.
- Fully read all 14 changed retained files (the cumulative changelog under the approved exception). The two added implementation files were read completely in the diff and mechanically matched byte-for-byte to raw. Read all 2,732 lines of current `stripe.core.ts`, current Webhooks/RequestSender/utils/transport/platform files, package and VERSION. Read affected prior event functions separately; the complete diff supplies prior changed code for other functions. Also read unchanged `src/apiVersion.ts` for the constant value.
- Parsed both complete snapshot inventories and packet/comparison metadata. Verified all 66 prior and 68 current files against manifest byte sizes, SHA256 and Git blob hashes; all 54 unchanged retained files match. Collection validator passed: 121 snapshots, 106 release records, 63 comparisons, 120 work items.
- Read both changelog changes: new release entry and retrospective OtherString explanation under 22.4.0. The other 4,868 historical lines (502,465 bytes) match; equal-block SHA256 `6243ac2e40ed67efd82706156b1ebb83a9ca02485c7e1afffa262b224ab16181`.
- CLI approved and claimed only this item as delta. Next-ingest assigned the same 23 paths, with no new attachments.

## Grounding excerpts

Paths below are relative to `raw/github/stripe/stripe-node/snapshots/2026-09-21-65d99a2/files/`.

1. `src/Webhooks.ts:200-201`: `constructEventWithoutVerification(payload: string): Event {` / `return buildEvent(maybeExtractFromCloudProviderEnvelope(payload));`
2. `src/stripe.core.ts:966`: `static MAJOR_API_VERSION = ApiMajorVersion;` (`src/apiVersion.ts` gives `dahlia`).
3. `src/stripe.core.ts:1610`: `if (parsed.object != null && parsed.object !== 'v2.core.event') {`
4. `src/platform/ExtensibilityPlatformFunctions.ts:43-44`: `getDefaultMaxNetworkRetries(): number {` / `return 0;`
5. `src/RequestSender.ts:688-689`: `if (error instanceof HttpClientRuntimeError) {` / `return callback(error);`

## Review disposition

Delta remains bounded to parsing/metadata and an opt-in runtime; no generated checkout resource changed, API marker and runtime dependencies are unchanged. Record stricter unexpected-object rejection and core/ESM missing-object divergence explicitly, not a claim of universal behavior parity. Tests were read as diff evidence, not executed; no live provider or packaged-runtime proof.

The capsule excludes standalone ESM entrypoint and emitter files, but their changed implementation is preserved in the complete SHA-to-SHA diff. Use that comparison for narrowly scoped findings; do not claim a complete ESM source capsule. No supplement or collection-policy change is made.

## Validation and completion

- `validate_wiki.py`: five schema-bearing touched pages pass. Including the provider index and root log reports only their pre-existing missing-frontmatter warnings; verified both also lack frontmatter at HEAD. No unrelated metadata rewrite.
- `validate_github_collection.py`: passes before and after `complete-ingest` (121 snapshots, 106 release records, 63 comparisons, 120 work items).
- Scoped `git diff --check` passes. Prior source history and complete older changelog entries remain byte-identical; every local Markdown evidence link in source/changelog resolves. Reverse catalogs have one list entry per source/changelog and company source count remains 666.
- Work item `github-fdb611aa510b593685f6` is `ingested`. The 22.6.0, 22.6.1 and 22.6.2 items remain `awaiting_approval`; no active ingest remains.
- No code/rule changes, SDK build, upstream tests, network payment execution, commit or push performed for this ingest.
