# Adyen Postman Checkout And Terminal Capsule Design

## Goal

Collect `Adyen/adyen-postman` as immutable commit-qualified evidence for practical Checkout API, recurring, card-analysis, test-card, and Terminal API requests without duplicating every generated historical collection or every non-checkout Adyen API family.

## Upstream Shape

The repository publishes generated Postman Collection v2.1 JSON derived from `adyen/adyen-openapi`. It retains many historical files, including Checkout API v37 through v72 and Recurring API v25 through v68. It also contains one unversioned, manually maintained Terminal API collection at `in-person-payments/ipp.json`.

At default-branch commit `ecb2907c79a0aef2208aa2796a2bd0fc8ffd0cd7`, the selected checkout evidence is:

- Checkout API v72: 60 requests and 51 response examples
- Recurring API v68: 7 requests and 4 response examples
- BinLookup API v54: 6 requests and 5 response examples
- Test Cards API v1: 1 request
- Terminal API: 82 requests across 16 top-level workflow groups

The README identifies the collections as generated from Adyen OpenAPI definitions and recommends the hosted Postman workspace as the always-current source. Repository evidence therefore proves exact request examples at one commit, not current production availability.

## Approaches Considered

### Current checkout and Terminal capsule

Collect only the latest checkout-focused JSON files, the Terminal API, and enough provenance metadata to detect version changes. This is the selected approach. It is approximately 852 KB across ten files and remains feasible for complete serial reading.

### All historical Checkout and Recurring collections

Collect every retained version from Checkout v37-v72 and Recurring v25-v68. This would preserve immediate version history but duplicate generated schemas, enlarge every baseline review, and make full serial ingest unnecessarily expensive. Historical versions remain available for on-demand version comparison.

### Latest collection from every API family

Collect Management, Balance Platform, Legal Entity, Transfers, Payouts, and every other latest service. This provides breadth but conflicts with the checkout-focused wiki and overlaps with Adyen OpenAPI and server SDK evidence. Those domains remain available through temporary cloning or future dedicated capsules.

## Collection Design

Enable the existing tier-2, monthly, commit-tracked registry entry and configure one `commit-tree-v1` capsule with these exact paths:

1. `postman/CheckoutService-v72.json`
2. `postman/RecurringService-v68.json`
3. `postman/BinLookupService-v54.json`
4. `postman/TestCardService-v1.json`
5. `in-person-payments/ipp.json`
6. `in-person-payments/readme.md`
7. `README.md`
8. `adyendev-postman-release-notes.md`
9. `generateAll.sh`
10. `.github/workflows/sync-collections.yml`

The JSON files provide executable examples. The README, release notes, and generator script establish provenance and usage boundaries. The sync workflow is a required version sentinel because it names the collection files Adyen currently publishes to its Postman workspace. The common collector also retains root `LICENSE` as repository context, so the published snapshot contains these ten policy-selected files plus that one automatic context file.

Use limits narrowly above the observed corpus: 600,000 bytes per file, 11 published files and 1,100,000 UTF-8 bytes per capsule, and 30 paths and 3,000,000 UTF-8 bytes per packet. Images, CI files other than the required sentinel, superseded generated collections, and unrelated API families are outside this capsule.

The source identity is the default-branch commit, expressed as `default-branch@<short-sha>`. API labels such as Checkout v72 remain evidence attributes and must not be treated as repository releases.

## Future Version Handling

The exact current collection paths are intentionally explicit. In-place changes to a selected JSON file produce normal default-branch comparisons.

When Adyen advances a filename, such as Checkout v72 to v73, the retained sync workflow should change and force a work item even if the old v72 file remains unchanged. Packet review must compare the workflow's referenced current collection names with the registry paths. A mismatch is an evidence gap: do not approve or ingest that packet. Update the registry to the new filenames, retry collection at the same resolved commit, and review the corrected packet.

If Adyen changes a latest collection filename without updating the retained sync workflow, manual upstream inspection during a scheduled review remains the fallback. The workflow sentinel reduces silent drift but is not represented as a universal discovery mechanism.

Historical versions are collected only for an approved comparison request. They must be pinned to an exact commit and added through a reviewed supplement or a separately approved capsule change rather than silently expanding the baseline.

## Ingest Boundary

The initial baseline requires full ingest and complete serial reading of all selected files, the packet, manifest, cumulative source context, and relevant Adyen indexes and logs.

Deep online-checkout coverage includes:

- payment methods, Sessions, Payments, and payment details
- cards, Apple Pay, Google Pay, 3D Secure, iDEAL, Klarna, and stored details
- tokenization, one-click, subscription, and recurring examples
- capture, cancel, reversal, refund, amount update, orders, and payment links
- request variables, authentication placeholders, example responses, and Postman usage boundaries

Deep Terminal API coverage includes payments, refunds, status and abort, preauthorization, reconciliation, input collection, pay-at-table and split, shopper engagement, barcode or QR scanning, sessions, printing, installments, tipping, and gift cards.

BinLookup and Test Cards are supporting checkout evidence. Non-selected API domains receive only a provenance note and a pointer to temporary cloning or dedicated collection.

Create one cumulative source page and one separate commit-qualified changelog under `wiki/sources/adyen/github/`. Keep this evidence independent from `adyen/adyen-node-api-library`, `adyen/adyen-web`, and `adyen/adyen-openapi`; cross-repository conclusions must identify which repository owns each claim.

## Approval And Failure Boundaries

Collection publishes one exact-SHA snapshot and review packet, then stops at `awaiting_approval`. It never auto-ingests or edits wiki pages.

Missing required files, invalid Postman JSON, strict UTF-8 failure, hash mismatch, secret finding, path mismatch with the sync sentinel, or budget overflow blocks approval. Existing accepted evidence remains immutable. Transient failures follow the common retry policy.

## Validation

Add a focused registry contract test for the enabled repository and exact capsule. Add or reuse deterministic checks that every selected JSON file parses and declares the Postman Collection v2.1 schema. Validate that the sync workflow references the four current generated collection filenames before collection is accepted.

Run the focused tests, the full GitHub test suite, and `scripts/validate_github_collection.py`. A dry run must show the ten selected files and no unexpected paths before publishing the baseline.

## Success Criteria

- `adyen/adyen-postman` is enabled with one reviewed commit capsule.
- The snapshot contains exactly the ten approved policy-selected files plus the collector-retained root `LICENSE` at one full SHA.
- Checkout v72, Recurring v68, BinLookup v54, Test Cards v1, and Terminal API JSON parse successfully.
- The sync-workflow sentinel references the selected generated collection filenames.
- The baseline packet recommends `full`, has no unclassified selected changes, and stops at `awaiting_approval`.
- No wiki knowledge changes before packet review and explicit ingest approval.
