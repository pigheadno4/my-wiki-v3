---
title: "Braintree In-Person Card-Present Authorization"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization"
raw_files:
  - "braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization-2026-09-16.md"
tags: [braintree, in-person, card-present, authorization, capture, graphql]
---

## Overview

This Braintree-hosted In-Person guide covers separate authorization from capture for a card-present transaction: the application requests an authorization on a reader, monitors the resulting In-Store Context, and sends a later capture request rather than having Braintree capture automatically. It is a website snapshot fetched 2026-09-16, with page metadata last updated 2025-01-20; it is not exact-version GraphQL schema authority, current firmware or payment-method support, account enablement, reader compatibility, or evidence that an authorization, capture, settlement, or funding event succeeded. See [[braintree]] and [[braintree-payment-platform]].

## Key takeaways

- The page says separate authorization and capture through the linked request-authorization mutation is supported starting with reader firmware 5.1.0. To initialize the reader, the application supplies at least `readerId`, `merchantAccountId`, and `transaction.amount`; the page says `merchantAccountId` is not validated in Sandbox but is required in Production for all card-reader interactions.
- A successful authorization does not capture the transaction. The merchant must retain the returned transaction ID and make a separate capture request. Card-present authorization permits only one capture attempt, and any authorized amount remaining after the initial capture request is automatically voided.
- The authorization request must include a unique `Idempotency-Key` HTTP header; UUIDv4 is recommended. The page explains that reusing the same key lets a POS recover the original transaction after an ambiguous communication timeout instead of accidentally creating a duplicate charge.
- After initialization, the application waits for customer interaction and polls the GraphQL `node` query at two-second intervals using the In-Store Context ID. The request sample shows a context in `PENDING` with an `ONLINE` reader; these are example values, not guarantees. When the authorization context becomes `COMPLETE`, the page says the transaction is `AUTHORIZED`, not `SUBMITTED_FOR_SETTLEMENT`, and directs the merchant to save its ID for later capture, authorization adjustment, or void operations.
- Capture uses the Capture Transaction mutation and requires the transaction to be `Authorized`. The page gives a 24-hour capture window, except that eligible lodging MCCs may have windows up to 30 days. A merchant may capture less than the authorized amount or, subject to eligibility, up to its maximum over-capture threshold; for ineligible MCCs, capture cannot exceed the authorized amount. The sample capture response is `SUBMITTED_FOR_SETTLEMENT`, which is distinct from authorization and is not proof of settlement or funding.
- Incremental authorization is account- and MCC-eligible, requires an `Authorized` transaction, and is not supported for Amex or some other transaction types. The guide recommends estimated authorization when using incremental authorization and routes the `paymentInitiator: ESTIMATED` field to the example. Over-capture and incremental authorization require corresponding Braintree account configuration; direct Amex contracts may require separate Amex configuration for over-capture.
- The page says request authorization is supported for offline transactions, but PayPal and Venmo QRC transactions do not support separate authorization from capture. L2/L3 data is not accepted in the authorization request, though the guide says it may be supplied in the separate capture request. These collected statements retain their firmware, environment, account, MCC, card-brand, payment-method, hardware, and snapshot-time qualifications.

## Detail locators

- `Feature Overview` (raw lines 19-24): delayed-capture use cases, authorization-versus-charge purpose, API-caller capture cadence, and firmware 5.1.0 starting point.
- `Initializing the Reader for Authorization` (raw lines 27-41): minimum initialization inputs, Sandbox/Production merchant-account distinction, authorization-versus-capture effect, single-capture rule, idempotency requirement, and mutation/request/response examples.
- `Checking the Reader Authorization Status` (raw lines 42-50): customer interaction, two-second polling, context/reader/transaction state examples, saved transaction ID, test-amount guidance, and the full query/response example.
- `Capturing funds against an Authorization` (raw lines 51-61): capture window, lodging exception, single-attempt and automatic-void behavior, over-capture eligibility, `Authorized` prerequisite, and sample request/response.
- `Using Incremental Authorizations` and `Using Estimated Auth (Pre-Auth)` (raw lines 62-77): MCC, Amex and transaction-type eligibility; required transaction state; update mutation; estimated-authorization recommendation; and example input.
- `AMEX Over Capture Rules` (raw lines 78-84): listed MCC percentage examples and direct-contract configuration qualification.
- `Important Tips When Integrating Separate Auth from Capture` (raw lines 87-108): offline support, account configuration, Amex incremental-auth exclusion, PayPal/Venmo QRC exclusion, and L2/L3 authorization-versus-capture boundary.

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Related raw API references

The captured guide links to the Braintree GraphQL reference for request authorization, node lookup, capture transaction, update transaction amount, and payment initiator. Those linked reference bodies were not read for this entry and remain navigation rather than exact-schema or behavioral evidence.

## Raw Sources

- [[raw/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization-2026-09-16|Braintree In-Person guide — Initiate a Card Present Authorization (fetched 2026-09-16)]]
