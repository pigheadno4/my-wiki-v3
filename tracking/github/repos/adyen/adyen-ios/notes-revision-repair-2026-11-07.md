# Adyen iOS Notes-Revision Queue Repair - 2026-11-07

## Approved Scope

User approved the bounded queueing repair, regression coverage and regeneration of the 5.26.0 notes-revision packet, with findings before ingestion. No ingestion, registry/budget/rule change, clone/network collection, commit or push is authorized or performed in this repair. Existing unrelated work remains untouched.

## Root Cause and Fix

The notes-revision producer intentionally omits a code comparison, but previously copied the preceding package version into PackageChange.from_version. Queue validation then required a comparison for that populated version boundary. Existing revision coverage only exercised an initial release without an earlier retained version, so it did not catch this case.

- scripts/collect_github_repos.py now emits same-version from/to identities for notes revisions, matching the packet's existing same-version/same-SHA semantics.
- scripts/github_work_items.py allows a comparison-free package change only with a nonempty validated evidence_revision, equal from/to versions, delta recommendation and the release-notes-revision reason. Normal upgrades, ref comparisons and approval requirements remain unchanged.
- Three regression tests cover collection after an earlier retained release, atomic queue finalization, and rejection of incomplete/incorrect revision markers. The integration case preserves every prior work item and raw file byte-for-byte.

Red/green: before the implementation change, the integration case returned "work-item state requires all applicable comparisons" and the same-version finalization case raised that error. After the fix, all three regression tests pass, including the negative-marker cases. The focused work-item/collector/packet suites pass 150 tests.

## Regenerated Retained Packet

- Item: github-03f5682f5c6d30579f8c.
- Package boundary: adyen-ios@5.26.0 -> adyen-ios@5.26.0; SHA da347498d07b843e5af3f9eb871376514ffdf38c unchanged.
- Evidence revision: 150add119593315c95baaf53265469d17cfc35acdb37111ca4f9218b09950c31.
- New release record: raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-11-07/manifest.json.
- Reused snapshot: raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/manifest.json, 689 unchanged files.
- Packet: tracking/github/repos/adyen/adyen-ios/ingest-packets/github-03f5682f5c6d30579f8c/packet.json and packet.md.
- Existing build/publish/finalize APIs rebuilt the packet from retained inputs and confirmed its JSON/Markdown are byte-identical to the prior draft. Canonical publication reused that pair; no accepted packet, snapshot or notes were overwritten. Finalization added the missing work item atomically, preserving all 283 existing items, including pending 5.27.0.
- State: awaiting_approval; recommended delta; approved_mode null. Five required paths / 251,034 bytes, including unchanged snapshot inventory and cumulative wiki context. No code diff is fabricated for a documentation-only revision.

## Findings Before Ingestion

The 5.26.0 release-note revision removes the CocoaPods final-release notice and changes its heading to iPhone Duo only. All iPhone Duo, Apple Pay partial-order, CVC and accessibility implementation highlights remain. The final-CocoaPods-release notice now appears on 5.27.0. Both dated 5.26.0 notes remain immutable; the old wiki statement must be qualified as historical evidence rather than silently erased in a later approved ingest.

No SDK source or binary changes belong to this note revision. The wiki still records last ingestion on 2026-10-15 at 5.26.0; neither this revision nor 5.27.0 has been ingested.

## Validation and Next Gate

Offline GitHub validation returns to the 13 pre-existing unrelated structural errors; the orphan-packet error is gone. Two items await approval: notes-only 5.26.0 and full-recommended 5.27.0. Scoped whitespace checks pass. No global all-green claim.

Full unit discovery ran 834 tests in 134.543 seconds: 829 passed, five failed. The focused 150-test work-item/collector/packet suite passes. Full-suite failures:

- test_fetch_stripe.StripeCollectionTests.test_cli_reference_starting_at_heading_two_is_valid_markdown: rejects heading-two Markdown in the full run; passes on isolated rerun. Full-suite-only discrepancy is unresolved and outside this repair; do not claim this failure was reproduced in the baseline check.
- test_github_registry.RegistryTests.test_adyen_postman_has_reviewed_checkout_terminal_policy: expects packet limit 30, registry has 40.
- test_github_registry.RegistryTests.test_braintree_graphql_api_has_reviewed_commit_policy: expects packet limit 15, registry has 20.
- test_github_registry.RegistryTests.test_paypal_messages_ios_uses_the_reviewed_release_capsule: expects only the v1 track, registry also contains v2.
- test_github_registry.RegistryTests.test_registry_matches_appendix_a_inventory_and_collection_cadence: expects the older monthly cadence rather than on-demand.

Reran these five tests with unmodified HEAD versions of both changed production modules loaded in memory, without reverting workspace files. All four registry mismatches reproduce; the Stripe test passes in that isolated run. HEAD baseline is 388c50863a0f6ce0ded0021e3c2777d08852f9ea. No unrelated collector, registry or cadence repair was made. The repair is scoped-tested, not an entirely green full suite.

Next recommendation: separately approve delta ingestion of the 5.26.0 notes revision first, then full additive 5.27.0 with focused reading. Preserve all prior knowledge. Publication remains a separate approval gate.

Later, separately approved execution completed the notes delta and then the 5.27.0 full additive ingest, preserving all history. See ingest-review-2026-11-07.md for final ingest state and validation. The repair-stage approval boundary and pre-ingest findings above remain a historical record; no publication has occurred.
