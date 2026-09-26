# Braintree C16 execution notes

Status: COMPLETE. Exact ten-page manifest approved and closed 2026-09-23.
Runtime started 2026-09-23T12:02:21Z. Preflight verified all ten pinned
hashes/canonical URLs, absent ownership and source targets, C15 completion,
the 121-source baseline and available three native child slots. Initial
orders dispatched Managing Authorizations, Email Receipts and Bank
Identification Numbers. Windows recorded at close may overlap; do not sum
them. C16 approval does not authorize raw edits, collection, code/rule changes,
GitHub ingest, commit, push or a next campaign.

## Result and elapsed time

- Runtime: `2026-09-23T12:02:21Z` to `12:45:07Z`, **42m46s** wall time.
- Ten initial worker handoffs were accepted; nine received first-pass content
  approval. Email Receipts needed one bounded wording correction and targeted
  review, with no repeated full review. All ten sources were promoted.
- Ten initial full reviews plus one targeted review. Five fixed query groups
  passed 20/20; their reads and reports overlapped the tail of ingestion.
- Company/index/log aggregation occurred once; the campaign-scoped mechanical
  check, 15 typed-page checks and scoped whitespace check passed before close.

This was slower than C15's 33m29s despite the same ten-page count. C16's 734
raw lines and Managing Authorizations' 164-line conflicted-eligibility page
made the early full-read/review path heavier; dynamic dispatch also left a
review candidate waiting while a worker slot was reserved. These are visible
contributors, not precise per-stage measurements. The one first-pass defect
was narrow: the worker merged manual Control Panel receipt generation with
separate merchant-built receipts. A future approved campaign can improve the
handoff by making such page-internal object/action contrasts explicit up front;
this run does not justify adding another validator, audit layer or hard cap.
