# Adyen React Native 2.12.0 release-note revision ingest

Work item: `github-318cfc2eff0d537cfc99`. User approved documentation-only delta.
Exact SHA: `2912c913266b2d1df73882980303b563ea04ab63`.

## Progress

- [x] Read assigned release record, complete revised/prior notes, cumulative source/changelog, packet and snapshot inventory; decoded repeated inventory fields with exact manifest references. Verify 301 retained file hashes/sizes and both note hashes. No unchanged source reread or runtime test claimed.
- [x] Concept audit: existing `adyen-react-native-sdk` already records both dependency versions. No new durable concept facts; leave concept unchanged.
- [x] Update cumulative source and separate changelog, preserving historical baseline.
- [x] Update company provenance; source count unchanged.
- [x] Concept disposition: no change required.
- [x] Comparison disposition: no cross-company comparison required.
- [x] Contradiction check: dependency identities unchanged; no new conflict.
- [x] Update provider index.
- [x] Append provider/root operation logs.
- [x] Validate touched pages, grounding, evidence links and lifecycle; complete this work item.

## Grounding

Complete revised raw: `raw/github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-10-04/release-notes.md`.

- Line 19: `| Name | New version |`
- Line 21: `| [Android Drop-in/Components](https://github.com/Adyen/adyen-android/releases/tag/5.19.0) | 5.19.0 |`
- Line 22: `| [iOS Drop-in/Components](https://github.com/Adyen/adyen-ios/releases/tag/5.25.1) | 5.25.1 |`

Only substantive text additions are the dependency table/links; existing dependency bullets receive bold formatting. Same release and SHA; 301 unchanged retained files. This is not a dependency upgrade or a new feature release.

No commit or push authorized in this ingest step.

## Validation outcome

- `validate_wiki.py`: three typed pages passed.
- `validate_github_collection.py`: 159 snapshots, 145 release records, 102 comparisons, 159 work items; no structural errors.
- All 301 retained file hashes/sizes, snapshot manifest hash and both note hashes match.
- Grounding lines 19/21/22 verified; historical headings and raw links preserved. Evidence-link checking strips citation line suffixes before filesystem resolution.
- Company source count unchanged; index/log routes resolve. No concept, comparison, runtime or integration changes.
- Work item state: `ingested`. Commit and push remain separate.
