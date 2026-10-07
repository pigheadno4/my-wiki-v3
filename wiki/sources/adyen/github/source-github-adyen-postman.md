---
title: "GitHub: adyen/adyen-postman"
type: source
date_ingested: 2026-08-12
date_updated: 2026-10-07
original_format: github-repo
raw_files:
  - "github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/manifest.json"
  - "github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/manifest.json"
tags: [adyen, postman, checkout-api, terminal-api, recurring-payments, bin-lookup, github-repository]
---

## Overview

`adyen/adyen-postman` contains generated Postman collections for Adyen APIs plus a separately maintained Terminal API collection. The first retained baseline is commit `ecb2907c79a0aef2208aa2796a2bd0fc8ffd0cd7`, with Checkout API v72, Recurring API v68, BIN Lookup API v54, Test Card API v1, and an unversioned Terminal API collection.

Repository: <https://github.com/adyen/adyen-postman>

An additive delta ingested on 2026-10-07 extends this history to `default-branch@78874d7`, exact SHA `78874d7b10d8cb438ed15eb01dd732c8d86540a7` (commit date 2026-09-28). The original baseline remains below; this repository uses commit identities, not package releases.

## Evidence boundary

- Baseline findings describe exact commit `ecb2907c79a0aef2208aa2796a2bd0fc8ffd0cd7`; the additive update below describes `78874d7b10d8cb438ed15eb01dd732c8d86540a7`. Neither proves current merchant eligibility, account enablement, payment-method availability, or production behavior.
- The four versioned API collections are generated from `adyen-openapi`; the Terminal API collection is maintained separately and is commit-qualified rather than API-version-qualified.
- Example requests can demonstrate payload shape and intended flow, but the current API reference, merchant configuration, shopper context, and actual API response remain authoritative.
- Secrets belong in a private Postman environment. No retained example value should be treated as a production credential or merchant identifier.

## Grounding excerpts

> "This repository contains declaration files in the Postman format. The files are automatically generated based on the latest adyen-openapi definition files."
>
> `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/README.md:5`

> "Before running API calls, you will have to set some variables."
>
> `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/README.md:27`

> "The Recurring API is a legacy API for managing tokens. We strongly recommend to use Checkout API recurring endpoints instead when possible."
>
> `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/postman/RecurringService-v68.json:5`

> "The response contains encrypted payment session data. The front end then uses the session data to make any required server-side calls for the payment flow."
>
> `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/postman/CheckoutService-v72.json:5343`

> "The collection consists of only operations using terminal API."
>
> `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/in-person-payments/ipp.json:5`

## Collection generation and setup

The versioned collections are generated from Adyen OpenAPI definitions by `generateAll.sh`, while the workflow synchronizes generated collections and the Terminal collection to Adyen's public Postman workspace. The repository release notes record improvements to response examples, Postman-style path variables, environment handling, workspace publication, and the addition of Terminal API examples.

Requests use environment variables such as `X-API-Key`, merchant account, company account, endpoint prefix, terminal ID, sale ID, and currency. Test and live endpoints differ, and live PAL endpoints require a company-specific prefix. The Terminal collection explicitly advises forking its environment into a private workspace.

## Checkout API v72

The `ecb2907` baseline's 60 retained Checkout requests cover the core online-payment lifecycle. The later `78874d7` collection contains 58 requests; the two removed donation examples are preserved in the historical snapshot and documented below.

| Area | Example operations |
| --- | --- |
| Discovery and payment | payment methods, payments, payment details, card details, co-badged cards |
| Sessions | create, retrieve result, update amount or payable amount |
| Modifications | cancel, capture, refund, reversal, authorization amount update |
| Orders and balance | create or cancel an order, gift-card balance |
| Stored methods | create, list, and delete stored payment methods; forward request |
| Payment links | create, retrieve, and expire links |
| Utilities | Apple Pay session, PayPal order update, shopper-ID validation, deprecated origin keys |

`/sessions` supports Drop-in, Components, and Hosted Checkout. Its response carries encrypted session data used by the frontend, while the payment outcome is delivered asynchronously through an `AUTHORISATION` webhook. Session update examples limit changes to amount or payable amount before the session becomes payable.

The collection distinguishes direct payment responses from responses that require an `action` and a later `/payments/details` call. Examples include cards, 3D Secure, Apple Pay, Google Pay, iDEAL, Klarna, split payments, stored credentials, subscriptions, and card-on-file use. Their presence is example coverage, not proof that each method is available to a given merchant.

Modification examples include partial capture and refund, multiple-capture caveats, split capture, reference-based cancellation, and reversal. A reversal requests a full cancel-or-refund decision and is not a replacement for multiple partial-capture handling.

## Tokenization and recurring operations

Checkout v72 includes encrypted and unencrypted stored-payment-method creation, list and deletion operations, and examples for `Subscription`, `CardOnFile`, and one-click use. This is the preferred recurring-management surface in the retained collection when applicable.

Recurring API v68 remains as a legacy token-management collection. Its seven requests cover listing and disabling stored details, scheduling Account Updater with card details or a token, India-only shopper notification, and deprecated permit operations. The collection explicitly recommends Checkout recurring endpoints when possible, so new integrations should not infer that the legacy API is the default architecture.

## BIN lookup and test cards

BIN Lookup API v54 demonstrates 3D Secure availability checks and payment-method cost estimates using card number, encrypted card data, merchant details, recurring-detail references, and 3D Secure assumptions. The collection states a regional boundary for cost estimation; the example does not prove current availability outside the documented context.

Test Card API v1 contains a single request for creating test-card ranges. It is test-environment evidence and does not describe production card issuance or payment processing.

## Terminal API

The unversioned Terminal collection contains 82 requests using Nexo `SaleToPOIRequest` messages. Core payment examples cover standard payment, cashback, platform splits, tokenization, MOTO, manual key entry, preauthorization, referenced and unreferenced refund, abort, and transaction-status lookup.

The collection also demonstrates terminal interaction and operations: login/logout and reconciliation, shopper confirmation/signature/menu/text input, pay-at-table and split-tender orchestration, card acquisition and tag flows, barcode or QR scanning, terminal sessions, printing, Mexico and Brazil instalment choices, tipping, and gift-card activation, payment, balance, load, reversal, and refund.

The boundary between API families is explicit. Terminal API owns terminal messages and interactions. Capture, token-based recurring charges, and authorization adjustments use Checkout API examples; store and terminal-fleet administration belong to Management API. The collection's Postman scripts persist in-process identifiers, inspect result/error fields, parse receipts, and route multi-step examples, but they are demonstration orchestration rather than a production POS state machine.

## Update `ecb2907` to `78874d7`: Stored-Method Roles and Donation Examples

Only `postman/CheckoutService-v72.json` changed among the 11 retained files. All ten other files, including the Terminal API collection, have identical hashes. The upstream comparison lists only this Checkout file; no API-version upgrade is established.

### Stored-payment-method credential role

The descriptions for GET and POST `/storedPaymentMethods`, and DELETE `/storedPaymentMethods/{storedPaymentMethodId}`, now explicitly require the `API tokenise payment details` role on the API credential. The description is also updated in retained original-request response examples. Existing request methods, URLs, headers, bodies, query configuration and example responses are otherwise unchanged.

This is a newly documented requirement in this repository comparison, not proof that the role or server-side enforcement was newly introduced on the commit date. The original query flags and idempotency-header defaults are not changed or repaired by this update. Merchant integrations should verify credential permissions rather than assume that an API key alone suffices; no live permission or payment test was performed.

### Donation example history

The collection removes two named requests, reducing Checkout examples from 60 to 58:

- `Make a donation to a donation account`: the historical payload combines `donationAccount`, a payment-generated `donationToken` and `donationOriginalPspReference`, with `shopperInteraction: ContAuth`.
- `Make a donation to a donation account with a token`: the historical payload uses `donationAccount`, `paymentMethod.recurringDetailReference`, `shopperReference`, `shopperInteraction: ContAuth` and `recurringProcessingModel: CardOnFile`.

Both are retained in the [old Checkout collection](../../../../raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/postman/CheckoutService-v72.json). Their removal from Postman is not evidence that the endpoint, parameters or payment capabilities were removed or deprecated by the API.

`Make a donation to a campaign` remains at POST `/donations`, using `donationCampaignId`, `donationToken` and `donationOriginalPspReference`. Its request and example response are unchanged; it was already present in the old collection and must not be described as a new donation flow. See the [new Checkout collection](../../../../raw/github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/files/postman/CheckoutService-v72.json).

### Reading and grounding

The user approved delta mode over the collector's path-based `payment-behavior-signal` full recommendation, plus a one-time focused-reading exception. The complete affected stored-method and donation sections in both snapshots, complete comparison and cumulative source/changelog were read; snapshot inventories, ten unchanged files and unaffected Checkout request structures were checked mechanically. This does not claim a complete reread of either snapshot or every Checkout description.

> "API tokenise payment details"
>
> `raw/github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/files/postman/CheckoutService-v72.json:2327` (list), `:2441` (create), `:2663` (delete).

> "Make a donation to a donation account"
>
> `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/postman/CheckoutService-v72.json:2950`

> "Make a donation to a donation account with a token"
>
> `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/postman/CheckoutService-v72.json:3058`

> "Make a donation to a campaign"
>
> `raw/github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/files/postman/CheckoutService-v72.json:2842`

[Snapshot record](../../../../raw/github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/manifest.json), [comparison record](../../../../tracking/github/repos/adyen/adyen-postman/comparisons/default-branch/ecb2907--78874d7/comparison.json), [comparison](../../../../tracking/github/repos/adyen/adyen-postman/comparisons/default-branch/ecb2907--78874d7/comparison.md), [full patch](../../../../tracking/github/repos/adyen/adyen-postman/comparisons/default-branch/ecb2907--78874d7/diff.patch), [ingest packet](../../../../tracking/github/repos/adyen/adyen-postman/ingest-packets/github-1b49bd6b9d94ec92f190/packet.md).

## Related

- [[changelog-github-adyen-postman]] - commit-qualified repository history
- [[adyen-terminal-api]] - Terminal API architecture and collection boundary
- [[adyen-node-api-library]] - typed Checkout v72 and Cloud Device API evidence
- [[recurring-payments]] - cross-provider recurring-payment concepts
- [[adyen]] - company and knowledge-status page

## Raw Sources

- [2026-10-07 snapshot manifest](../../../../raw/github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/manifest.json) - immutable inventory; focused read of stored-method and donation sections only, unchanged files verified by hash.
- [2026-10-07 Checkout v72 collection](../../../../raw/github/adyen/adyen-postman/snapshots/2026-10-07-78874d7/files/postman/CheckoutService-v72.json) - affected sections used for this approved focused delta.
- [Historical Checkout v72 collection](../../../../raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/files/postman/CheckoutService-v72.json) - baseline and prior affected sections, including removed donation examples.
- Snapshot manifest: `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/manifest.json`
- Repository and generation: `files/README.md`, `files/generateAll.sh`, `files/.github/workflows/sync-collections.yml`, and `files/adyendev-postman-release-notes.md`
- API collections: `files/postman/CheckoutService-v72.json`, `RecurringService-v68.json`, `BinLookupService-v54.json`, and `TestCardService-v1.json`
- Terminal collection: `files/in-person-payments/ipp.json` and `files/in-person-payments/readme.md`
