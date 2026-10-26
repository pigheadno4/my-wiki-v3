# Stripe Terminal Android serial ingest review - 2026-10-26

## Authorization and Sequence

User approved 5.8.1 delta, then 5.8.2 delta, then additive full 6.0.0, preserving all older knowledge. User approved focused reading for all three: fully read changed authored code, semantic API documentation, affected prior code, new changelog entries and cumulative wiki history; mechanically verify version-only documentation, unchanged history, manifests and duplicated generated diffs.

Each work item was claimed separately. Both deltas reached `ingested` before the next work item started. This review covers completion checks for the final full ingest; publication requires separate approval.

| Package release | Exact SHA | Mode | Finding |
| --- | --- | --- | --- |
| stripeterminal@5.8.1 | 846d401d1f7bc686a2c12d6def4342471c25a625 | Delta | China UnionPay support in Hong Kong for Tap to Pay on Android |
| stripeterminal@5.8.2 | abb16f502cbe0fcc82f673c246c86c883a5c2fdc | Delta | Fixes China UnionPay Tap to Pay payment failures |
| stripeterminal@6.0.0 | 0829be9e77842bc12a6ba56d64fd152b53506025 | Full | Incompatible capture, reader-interaction, consent/model and initialization changes |

## Reading and Grounding

- Both patch comparisons have 337 generated API pages changing only version strings. Authored changelog, README and Gradle changes were read fully, together with affected prior code and wiki history. The 5.8.2 changelog also corrects the older spelling "Union Pay"; the original wiki quote remains preserved.
- The 6.0.0 effective assignment contains 94 paths / 6,520,286 bytes. Changed authored files were read fully, including affected Java/Kotlin event/model code beyond normal selectors. Structurally parsed API main-content changes cover 105 current pages and five removed prior pages. Version-only/generated material was mechanically verified under the exception.
- All 1,791 files across baseline and three update snapshots passed size, SHA-256 and Git blob identity checks. Packet evidence gaps and unclassified changes are zero. Functional release claims use exact-SHA changelogs, not the release bodies' mutable master links.
- Located grounding quotes and immutable evidence links are recorded in the cumulative source. No proprietary implementation, merged SDK manifest, build, device or payment execution is claimed.

## Important Qualifications

- The v6 SDK builder defaults to AutomaticAsync; receipt tipping, incremental and extended authorization require explicit Manual. Older retained API text conflicts with that default. Reciprocal contradiction warnings were added.
- The Java example still unconditionally requests backend capture after a successful Intent ID. This is a static integration risk, not proof of a duplicate charge. Kotlin's in-memory ledger is not durable reconciliation.
- Required reader interaction without a listener fails the transaction. The separate Tap to Pay update-requirements callback is advisory and does not itself install updates or block acceptance.
- Compile SDK 35+ is not the device minimum: the retained minimum remains API 26. The MODIFY_AUDIO_SETTINGS requirement is recorded without claiming the merged application manifest omits it.
- Refund preview and renamed/removed APIs remain version-qualified. Types outside the capsule are attributed to release notes, not inspected implementation.
- Retrospective generated_card notes identify affected 5.4.0-5.6.0 and the 5.7.0 fix; they are not a newly fixed v6 defect. No v6 support end date is inferred from the unchanged v5-only schedule.

## Wiki and Validation

Six related concepts were updated before the corresponding source additions. One cumulative source and separate changelog retain v5 history; company/catalog/log entries were updated without adding sources (company source_count remains 666). All pre-existing changelog sections from 5.8.0 onward remain byte-identical to HEAD.

- Scoped wiki validation: 10 typed pages passed.
- Android registry test: 1 passed.
- Collection-index tests: 9 passed.
- Whitespace validation: passed.
- Global GitHub validation is recorded separately in the operator result; unrelated historical failures are not repaired by this ingest.

No registry policy, collector code, raw evidence or unrelated provider content was changed during ingestion. No commit or push is authorized by this review.
