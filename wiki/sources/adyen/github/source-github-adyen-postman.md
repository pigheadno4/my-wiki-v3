---
title: "GitHub: adyen/adyen-postman"
type: source
date_ingested: 2026-08-12
original_format: github-repo
raw_files:
  - "github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/manifest.json"
tags: [adyen, postman, checkout-api, terminal-api, recurring-payments, bin-lookup, github-repository]
---

## Overview

`adyen/adyen-postman` contains generated Postman collections for Adyen APIs plus a separately maintained Terminal API collection. The first retained baseline is commit `ecb2907c79a0aef2208aa2796a2bd0fc8ffd0cd7`, with Checkout API v72, Recurring API v68, BIN Lookup API v54, Test Card API v1, and an unversioned Terminal API collection.

Repository: <https://github.com/adyen/adyen-postman>

## Evidence boundary

- This page describes request examples and explanatory text retained at exact commit `ecb2907c79a0aef2208aa2796a2bd0fc8ffd0cd7`. It does not prove current merchant eligibility, account enablement, payment-method availability, or production behavior.
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

The 60 retained Checkout requests cover the core online-payment lifecycle:

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

## Related

- [[changelog-github-adyen-postman]] - commit-qualified repository history
- [[adyen-terminal-api]] - Terminal API architecture and collection boundary
- [[adyen-node-api-library]] - typed Checkout v72 and Cloud Device API evidence
- [[recurring-payments]] - cross-provider recurring-payment concepts
- [[adyen]] - company and knowledge-status page

## Raw Sources

- Snapshot manifest: `raw/github/adyen/adyen-postman/snapshots/2026-08-12-ecb2907/manifest.json`
- Repository and generation: `files/README.md`, `files/generateAll.sh`, `files/.github/workflows/sync-collections.yml`, and `files/adyendev-postman-release-notes.md`
- API collections: `files/postman/CheckoutService-v72.json`, `RecurringService-v68.json`, `BinLookupService-v54.json`, and `TestCardService-v1.json`
- Terminal collection: `files/in-person-payments/ipp.json` and `files/in-person-payments/readme.md`
