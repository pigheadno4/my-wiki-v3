# Adyen React Native 2.14.0 Ingest Review - 2026-11-07

## Authorization and Scope

- User approved full additive ingestion with focused reading after the collection findings. Commit and push remain separate approval gates.
- Work item: `github-01b194e7c644e7ff1f60`; package `@adyen/react-native@2.14.0`; SHA `08e15ac5e38d925780895093844edc7ca4cdb811`; released 2026-11-02.
- The collector recommended delta/high; explicit user approval overrides it to full because the supported Android platform/toolchain baseline changes. Packet evidence remains immutable and the full effective assignment is 315 paths / 958,275 bytes.
- All 13 added/modified retained files, their 12 available prior versions, release notes, comparison, cumulative source/changelog and affected appearance/parser/plugin/CardView dependencies read completely. Unchanged source and generated inventories verified mechanically under the approved exception; no whole-repository read claimed.
- All 611 current/prior files pass size, SHA-256 and Git blob identity checks. Packet/snapshot/comparison hashes pass; 36 upstream dispositions reconcile to 13 retained and 23 intentional exclusions, with no gaps or unclassified changes.
- No SDK/package install, build, upstream test, device/payment operation, additional collection, rule/registry change, commit or push.

## Located Grounding Excerpts

Paths below are relative to `raw/github/adyen/adyen-react-native/snapshots/2026-11-07-08e15ac/files/`.

1. `docs/Compatibility.md:9`: "Supported versions are React Native 0.79 and newer, and Expo SDK 54 and newer."
2. `docs/Compatibility.md:42`: "Keep any version that is already newer than the snippet."
3. `android/build.gradle:23`: `if (project.extensions.findByName('kotlin') == null) {`
4. `ios/Views/CardView/CardComponentViewProxy.swift:148`: `cardConfig.style = Self.appearanceProvider()?.formComponent ?? FormComponentStyle()`
5. `docs/Customization.md:19`: "The `formComponent` style of the returned `Adyen.DropInComponent.Style` also styles the embedded `CardView`."

## Workflow Checklist

- [x] 1. Approved focused reading, effective assignment and evidence/hash checks; grounding gate.
- [x] 2. Concept audit and existing concept update before source edits.
- [x] 3. Additive cumulative source/changelog with historical raw links retained.
- [x] 4. Company summary; source count field unchanged at 3206 (count reconciliation at close).
- [x] 5. Complete durable concept and reciprocal-citation review.
- [x] 6. Comparison decision: no cross-company substantive comparison; no new page.
- [x] 7. Contradiction/version-scope check: matching source/concept warnings, historical platform/pin prose qualified, no invented published-metadata or executed-build claims.
- [x] 8. Provider catalog update; no root-index change needed.
- [x] 9. Provider and root operation logs, preserving unrelated changes.
- [x] 10. Focused wiki/evidence/history checks and terminal work-item state: ingested/full, no pending items.

## Concept Audit

Existing `adyen-react-native-sdk` owns wrapper compatibility, platform setup and CardView behavior. Update it rather than creating a new concept. Native iOS/Android concepts own independently versioned SDK evidence; their histories are not merged. Generic React Native/Expo/Gradle concepts and a company-comparison page are not warranted by this contained wrapper source.

## Validation

- `validate_wiki.py` passes for all five typed pages: wrapper concept, cumulative source, cumulative changelog, Adyen company and Adyen log. No issues.
- The existing untyped `adyen-index.md` reports missing YAML frontmatter when included in the typed validator. Confirmed the same untyped format at HEAD; no unrelated schema migration. Its two wrapper catalog entries are unique, updated and independently link-checked. Root log remains untyped; only this ingest's concise entry was inserted, preserving other work.
- Exact located grounding excerpts pass mechanical checks. Source Markdown evidence targets resolve. All older raw frontmatter entries remain in their original order after the new pair; historical 2.12.0 implementation/revision sections and the complete 2.13.0 integration section are preserved. The complete previous changelog history is byte-preserved below the new entry.
- Company source_count reconciles to 3206 source summaries, unchanged. Distinct ingested Adyen repository/package release identities now reconcile to 31 (previously 30); a notes revision does not add an identity.
- Final `validate_github_collection.py` reports the same 13 historical structural errors, none for this item: six older packet-budget rebuild failures plus six resulting invalid-packet reports, and the existing Adyen PHP package-alias ledger mismatch. Pending work items: 0. No global all-green claim.
- Scoped `git diff --check` passes. No production script, registry or rule edits; full unit suite not rerun for this documentation/tracking-only ingest. No upstream execution.
- Work item completed as `ingested`, approved mode `full`; collector-generated collection index accepts `@adyen/react-native@2.14.0`, queue `ingested`, next action `wait`, next due 2026-11-14. Packet and accepted raw evidence were not rewritten.

## Outcome and Next Step

Full additive ingestion completed with the approved focused-reading exception. Source/concept preserve Android peer-range and AGP-literal qualifications, Kotlin/Expo exceptions, bounded plugin coverage, native appearance propagation and independent native evidence ownership. No new concept/source/comparison page was needed. All earlier wiki history remains retrievable.

Next: user-approved scoped commit and push of this collection/ingest evidence and wiki/tracking changes, preserving unrelated dirty work. No commit or push performed in this turn.
