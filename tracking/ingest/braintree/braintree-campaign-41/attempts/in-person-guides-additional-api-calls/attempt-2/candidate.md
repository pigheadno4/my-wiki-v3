---
title: "Braintree In-Person Additional API Calls"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/additional-api-calls"
raw_files:
  - "braintree/in-person/guides/additional-api-calls-2026-09-16.md"
tags: [braintree, in-person, graphql, card-reader, locations, transactions, reconciliation]
---

## Overview

This collected [[braintree|Braintree]] website guide is a retrieval page for additional GraphQL reads and one reader-local ping: querying a reader's reported status and firmware, testing the offline ping endpoint without requesting a charge, listing locations or readers, and searching transaction records for reconciliation. It is an unversioned website snapshot, not GitHub or exact-commit schema evidence, current feature or account eligibility, reader pairing or health proof, request-charge or In-Store Context state, or proof of authorization, capture, settlement, funding, or successful reconciliation.

## Key takeaways

- `pingInStoreReader` is presented as a query for a specific reader's reported online/offline status, firmware version, timestamps, location, and other selected fields. The page warns that its response is accurate only within several minutes, not in real time. For offline-transaction request routing, it instead recommends the reader status returned by the request-charge mutation; a ping response is reader-state observation, not a charge request, In-Store Context, transaction, or payment outcome.
- For the reader-local offline ping at the displayed `https://readerIPaddress:3030/graphql` endpoint, the prose calls the API call a mutation while the captured example is labeled `GraphQL Query` and shows `{ping}`; this snapshot does not resolve the operation type. The displayed variables object contains `readerId`, but the shown `{ping}` operation text does not reference that variable, so the snapshot alone does not establish whether `readerId` is required or consumed. The stated purpose remains validating that the offline endpoint can be pinged without sending a charge request, and the example `pong` is an action response rather than evidence of transaction creation, authorization, storage, upload, settlement, or funding.
- The page supplies example GraphQL queries for `inStoreLocations(first: 100)` and `search { inStoreReaders(...) }`. The first selects pagination, identity, coordinates, QR-payment, payer and address fields; the second selects reader identity, reported status, software, location and vendor fields and shows an optional `locationId` `is` filter. These examples retrieve records; they do not create locations, pair readers, change reader state, or establish current exact-schema support.
- A transaction-search example is offered as one way to automate or streamline reconciliation. Its illustrative input filters amount at or above `800.00` and status within `SETTLED` or `VOIDED`, and its selected output includes transaction ID, status and amount. The example is not a merchant-specific result, does not prove completeness or freshness, and does not itself execute, authorize, capture, settle, fund, void, or reconcile a payment.
- The page links to separate GraphQL reference, offline-transaction, request-charge, search-construction and receipt-printing documentation. Those linked targets were not read as evidence for this entry, so their schemas, prerequisites and behavior must be verified separately.

## Detail locators

- `## Ping Reader` (raw lines 19-26) — query purpose, reported reader fields, several-minute freshness warning, request-charge routing recommendation, and the full query/variables/response example.
- `## Offline Ping` (raw lines 27-33) — no-charge purpose and displayed reader-local endpoint; prose calling the call an API mutation; captured example labeled `GraphQL Query` and showing `{ping}`; displayed `readerId` variables not referenced by that operation text; and the `pong` example.
- `## Query a list of Locations` (raw lines 34-38) — location-query purpose plus complete pagination, field-selection, variables and sample-response detail.
- `## Query a list of Readers` (raw lines 39-45) — location-or-merchant-account association statement, base reader-search example and the separate `locationId` `is` filter example.
- `## Query a list of Transactions` (raw lines 46-53) — reconciliation framing, linked search references, illustrative amount/status criteria, selected result fields and sample response.

## Related

- Company: [[braintree]]
- Concept: [[braintree-in-person]]

## Related raw API references

- Braintree GraphQL `pingInStoreReader` reference (`/braintree/graphql/reference/#Query--pingInStoreReader`) — linked navigation only; not read as evidence.
- Braintree In-Person offline-transactions guide (`/braintree/in-person/guides/offline-transactions/`) — linked navigation only; not read as evidence.
- Braintree In-Person request-charge guide (`/braintree/in-person/guides/making-a-transaction/#initializing-the-reader-for-charging`) — linked navigation only; not read as evidence.
- Braintree GraphQL Search object and constructing-searches guides — linked navigation only; not read as evidence.
- Braintree In-Person receipt-printing guide — linked navigation only; not read as evidence.

## Raw Sources

- [[raw/braintree/in-person/guides/additional-api-calls-2026-09-16|Braintree In-Person Additional API Calls (fetched 2026-09-16)]]
