# Adyen Node API Library serial ingest review

Approved order: `@adyen/api-library@32.1.0` additive full, then `32.2.0` delta.
User approved focused reading for both: changed implementation, affected prior
code, comparisons and release notes; unchanged inventory verified by hash.
No full upstream-tree, merchant API, build or payment-test claim. No commit/push.

## 32.1.0

- [x] Read cumulative source/changelog, packet, release and comparison evidence.
- [x] Verify manifests, retained hashes, packet and comparison hashes.
- [x] Read changed code and affected prior/dependency context; extract grounding.
- [x] Concept audit and updates before source.
- [x] Add source/changelog history without replacing 32.0.0 knowledge.
- [x] Company, index and logs; contradiction and scope review.
- [x] Focused wiki/GitHub validation and terminal completion.

Five typed pages pass validate_wiki; GitHub validator passes 166 snapshots,
152 releases, 109 comparisons and 166 work items. git diff --check passes.
Provider index/root log are existing untyped navigation/chronology files;
explicitly passing the index to the typed-page validator reports its pre-existing
missing frontmatter, so no unrelated schema retrofit was made. Index entries and
log links reviewed directly. CLI marked 32.1.0 ingested before starting 32.2.0.

## 32.2.0

- [x] Start only after 32.1.0 completion; read cumulative context and packet.
- [x] Verify hashes; read changed implementation, prior context and notes.

32.2.0: complete cumulative source/changelog and packet Markdown read; structured
packet/release/comparison metadata checked; full patch, VERSION, package and
HTTP implementation read. Prior HTTP/client/certificate helper context reviewed.
All 1,132 prior/current file sizes/hashes match; three changed and 563 unchanged
paths; all ten upstream dispositions accounted for. Packet, snapshot, notes and
comparison hashes/identities verified. Grounding: HTTP constructor lines 45-48,
cached agent line 137, certificate-path cache lines 294-315. Payments App models
remain excluded and release-note-qualified. No default keep-alive, performance,
proxy cache or automatic certificate-file rotation claim.
- [x] Grounding and concept-first updates.
- [x] Add source/changelog, company, index and log updates.
- [x] Validate and complete separately.

Final checks: five typed wiki pages pass; 61 packet tests pass; GitHub validator
passes all 166 snapshots, 152 release records, 109 comparisons and 166 work items.
Grounding quotes checked against raw text; old versions and unique provider-index
entries preserved; git diff --check passes. 32.2.0 marked ingested separately.
No full-suite success claim: the earlier pre-existing SecretFindingsBlocked
traceback-assignment failure remains outside this correction. No commit/push.

## Collector correction

32.1.0 reading: all 103 added/modified retained files read fully, four removed
retained paths and affected prior transport/Checkout dispatch context read.
Both snapshots' 1,111 retained file sizes/hashes verified; packet, snapshot,
comparison Markdown/patch and release-note hashes match. All 135 upstream
dispositions are retained evidence or intentional policy exclusion. Five newly
retained notification types match the older supplement byte for byte.
Grounding: session request lines 14/16/20-22; payment method mapping line 93;
token redundancy template lines 13/17-19; ClientInterface line 25, all under
the 2026-10-04-afd3bb4 snapshot. These are recorded in the source update.

Rename out of required scope uses retained prior evidence without requiring the
out-of-scope destination. Missing prior evidence and missing in-scope destination
still block. Moves wholly outside selected scope preserve prior behavior.
61 packet tests pass. Full suite stops at the pre-existing
`test_release_notes_are_secret_scanned_before_publication` traceback-assignment
failure in immutable `SecretFindingsBlocked`; not changed by this scoped fix.
