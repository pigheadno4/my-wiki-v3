---
title: "Optional server configuration | Adyen Standard Drop-in"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/drop-in/optional-server-configuration"
raw_files:
  - "adyen/docs/standard/integration/drop-in/optional-server-configuration/2026-09-15.md"
tags: [adyen, standard-integration, online-payments, drop-in, sessions]
---

## Overview

This 2026-09-15 [[adyen]] **Standard Drop-in** guide offers two optional payment-server features: changing a session amount before shopper submission and retrieving a payment-session result on the server. It belongs to the bounded [[adyen-online-payments]] Standard path; these are conditional configuration steps, not evidence that a payment was authorized, captured or settled. [Raw: lines 15–26, 174–182]

## Key takeaways

- To permit a later amount change, create the session with `payable: false` and confirm that value in the response. The guide's TEST example uses Checkout API `POST /v72/sessions`; this initial state prevents shopper submission while the amount is updateable. [Raw: lines 24–81]
- For a changed amount, the merchant server makes `PATCH /sessions/{sessionId}` with the original response's `sessionData`, updated amount in minor units/currency and optionally `payable`. Once `payable: true` marks the final amount, the session **cannot be updated again**. If it remains false, another update setting it true is required before shopper submission. [Raw: lines 83–123]
- Drop-in can display revised amounts multiple times before the server-side session is patched. Before payment submission, `beforeSubmit` must obtain the final amount **from the merchant server, not the client**, patch the session and pass returned `sessionData` via `actions.resolve`; the example rejects on failure. The display-only example uses currency USD with `amount.value: 1000`, while the server request examples use currency EUR with `amount.value: 1900` then `10000`; these integers are in minor units and the snippets are illustrative rather than one reconciled cart/session trace. [Raw: lines 38–57, 95–171]
- Optionally, the server can retrieve a result with the session `id` and `sessionResult` from `onPaymentCompleted` or `onPaymentFailed` using `GET /sessions/{id}?sessionResult=...`. The statuses shown are `completed` (the guide describes this as authorized), `paymentPending` for asynchronous methods, `canceled` and `expired`. The returned `status` **does not update**; later changes require webhooks or Customer Area Transactions, not repeated GET polling. A session result does not itself prove capture or settlement. [Raw: lines 174–182, 340–378]
- The result-lookup curl sample uses Checkout API **v70** and several older language-library examples, while the session-create/PATCH samples use **v72**. Treat those as dated, mixed-version examples, not proof that a v70 lookup is the required or compatible version for a v72 Standard integration. [Raw: lines 40–45, 97–111, 184–337]

## Detail locators

- Optional feature choices and `payable: false` creation: raw lines 15–81.
- PATCH fields and irreversible `payable: true` transition: raw lines 83–123.
- Drop-in display versus server-authoritative final amount and `beforeSubmit` resolution: raw lines 125–171.
- Server result lookup and illustrative API-library versions: raw lines 174–337.
- Result statuses, immutable snapshot and webhook/Transactions follow-up: raw lines 340–378.

## Related

- [[adyen-online-payments]] — Standard online-payments concept
- [[source-adyen-docs-standard]] — bounded Standard checklist
- [[source-adyen-docs-standard-integration-drop-in]] — parent Drop-in integration route
- [[source-adyen-docs-standard-integration-drop-in-optional-drop-in-configuration]] — optional client configuration route

## Raw Sources

- [[raw/adyen/docs/standard/integration/drop-in/optional-server-configuration/2026-09-15|Pinned Standard Drop-in optional server guide]]
