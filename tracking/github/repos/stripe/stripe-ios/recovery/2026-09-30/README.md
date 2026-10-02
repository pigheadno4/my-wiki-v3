# Stripe iOS comparison recovery

User approved preserving and retiring the failed broad-scope comparison on
2026-09-30. The three original generated files are retained unchanged in
`26.5.0--26.6.0-broad-scope/`.

Original location: `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.5.0--26.6.0/`.
Work item: `github-27c39776069e90865f25` (not approved or ingested).

The earlier attempt compared the whole Checkout subtree. The corrected policy
requires the two confirmation implementations and uses validated historical
snapshot scope for the prior release. Regenerate the active comparison through
the collector; do not treat this retired comparison as an ingest packet.

Raw snapshots and release records are unchanged. This recovery does not approve
ingest, commit, or push.

## Recovery result

Exact-release recollection succeeded on 2026-09-30. The same work item is now
`awaiting_approval`, with its consecutive failure counter reset to zero. The
active comparison was regenerated (30 changed paths versus 46 in the retired
comparison). The existing broader raw snapshot was reused without modification.

The new packet recommends full ingest, reports no evidence gaps or unclassified
changes, and assigns 92 reading paths. Extra files retained by the earlier broad
snapshot remain available; snapshot additions do not necessarily mean upstream
feature additions. No ingest was started.

Verification: four focused regression tests passed; the GitHub validator passed
with 141 snapshots, 126 release records, 83 comparisons, and 140 work items.
The full-suite failures reported before this recovery remain unresolved.
