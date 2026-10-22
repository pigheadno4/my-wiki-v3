---
title: "Webhooks for payouts to bank accounts | Adyen Docs"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts/payout-webhooks"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/payout-webhooks/2026-09-15.md"
tags: [adyen, payout-service, bank-payouts, webhooks, transfers]
---

## Overview

This Payout Service guide, captured 2026-09-15, maps `balancePlatform.transfer.created` and `.updated` webhooks for outgoing bank-transfer requests from a platform balance account, including authorisation, booking, review, tracking, tracing, crediting, failure, and return. Its opening describes payout to “your bank account,” while its worked use case explicitly pays a user's balance account to a third-party bank account; retain the example's beneficiary scope rather than treating those phrasings as identical. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The stated prerequisites are a Payout Service integration, a server able to receive and accept webhooks, and Customer Area subscriptions to **Transfer** and **Transaction** webhooks. Identify the payout Transfer events using `category=bank`, `direction=outgoing` from the balance account's perspective, and `type=bankTransfer` (raw lines 19–49). These are configuration and classifier requirements, not proof of a delivered event.
- `transfer.created` says an outgoing request was created; an `updated` event with `status=authorised` says the amount was reserved. If funds are insufficient, `updated` may instead report `status=refused` and `reason=notEnoughBalance`; the guide calls for funding the account and sending a **new** request (raw lines 60–62, 148–150, 250–257).
- `status=booked` reports deduction from the user's balance account and supplies a transaction ID, but the guide explicitly says it is **not final**: instant bank payouts can fail after counterparty rejection, while regular or wire payouts can be returned. Post-booking internal review may appear as a tracking event with `trackingData.status=pending` and `type=internalReview`; failed review reports `trackingData.status=failed` and `reason=refusedForRegulatoryReasons`, even while its example retains top-level `data.status=booked` (raw lines 352–361, 478–488, 620–640, 755–778).
- Tracking `estimatedArrivalTime` is an **estimate**, subject to beneficiary-bank timing; the captured guide says ETA is available for local payouts but not instant or cross-border payouts. Tracing data is a distinct event carrying network identifiers for UK FPS/GBP and US ACH/USD when funds leave Adyen. For completed instant-priority transfers, a `tracking` event with `status=credited` is the guide's credit confirmation; its sample still has top-level `data.status=booked`, so inspect the tracking event rather than reading that top-level status as receipt (raw lines 924–930, 1059–1083, 1220–1222, 1320–1343).
- External-bank rejection or unsuccessful automatic retries can produce `status=failed`; counterparty-bank return produces `status=returned` with transaction and reason information. Some permanent return reasons block later use of the transfer instrument and yield HTTP 422 on new requests. The reason-code table nonetheless lists retry-oriented actions for some account-detail reasons: do not infer that every listed reason is safely retryable without checking the actual blocked state. Network returns can include `networkReason`; FPS/ACH return history includes earlier tracing because funds had left Adyen (raw lines 784–793, 1352–1358, 1490–1510, 1673–1688).

## Detail locators

- Prerequisites, classification, and request/authorisation/refusal: raw lines 19–49, 60–257.
- Booking, screening, review outcome and external failure: raw lines 352–790; example JSON occupies intervening lines.
- ETA, rail-specific tracing and instant credit confirmation: raw lines 924–930, 1059–1083, 1220–1222.
- Return, blocking, network reason and reason-code table: raw lines 1352–1358, 1490–1510, 1673–1688.
- The failed-review sample has `categoryData.type=bank`, unlike the guide's `bankTransfer` classifier and most examples (raw lines 42–49, 664–668); confirm the event schema before copying that illustrative value.

## Related

- [[adyen-webhooks]]
- [[source-adyen-docs-payouts-payout-service-webhook-types]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/payout-webhooks/2026-09-15|Pinned Payout Service bank-payout webhook guide]]
