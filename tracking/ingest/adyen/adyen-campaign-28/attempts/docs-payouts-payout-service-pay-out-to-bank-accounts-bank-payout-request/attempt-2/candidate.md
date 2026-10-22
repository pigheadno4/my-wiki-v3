---
title: "Adyen Payout Service third-party bank payout request"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts/bank-payout-request"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/bank-payout-request/2026-09-15.md"
tags: [adyen, payout-service, bank-payouts, transfers-api, third-party]
---

## Overview

This Payout Service guide (last modified 2023-11-30; captured 2026-09-15) explains a Transfers API request to move funds **from a source balance account to a third-party bank account**. It offers one-off bank details or a stored bank-account token, optional priority fallback, one additional review, and a future execution date. The request response and TEST examples do not establish booking or receipt by the beneficiary bank. See [[adyen]] and [[adyen-payouts]].

## Key takeaways

- **Prerequisites and request shape:** The API credential needs the Transfers API roles; a server must accept webhooks; and Support must enable transfers on the **source balance account**. POST `/transfers` specifies `amount`, source `balanceAccountId`, `category=bank`, destination `counterparty.bankAccount` and transfer priority. The table marks `priorities` required if `priority` is absent. Bank-account owner details and account identification vary by individual status, country and currency. A one-off request supplies identification; the token example uses `storedPaymentMethodId`. Descriptions and references have separate roles, including a `referenceForBeneficiary` sent to the recipient and related webhooks.
- **Accepted request versus movement:** A successful API call yields HTTP 2XX and a transfer-request `id`. This is request acceptance, not proof of a booked debit, external bank receipt or completed payout. The guide directs readers to payout webhooks for received, authorised and booked/debited stages, plus estimated arrival information; actual transfer-specific events/details are needed to substantiate an outcome.
- **Priority fallback and review:** A list of priorities lets Adyen try the first route and then another available priority if the first is unavailable; route availability depends on location, currency and counterparty. The example has unavailable `fast` and selected `regular` with `routingDetails`; it is illustrative, not a general routing guarantee. Including `review.numberOfApprovalsRequired=1` triggers the only additional review count described here; a team member must approve before Adyen continues processing.
- **Future execution and failure:** A request may include `executionDate.date` within 30 days in YYYY-MM-DD form and an optional timezone. The guide says a successful future request remains `received/pending` until execution; on that date, between 00:00 and 03:00 in the balance-platform-configured default time zone, Adyen checks funds and any required team approval. The timing prose uses the Balance Platform's configured default time zone for the 00:00–03:00 processing window (raw line 2133), while the optional `executionDate.timezone` table labels **Europe/Amsterdam** as its default (line 2148). The page does not reconcile these defaults or establish which controls the processing window when a request supplies a timezone. The table also marks `executionDate.date` **required** (lines 2144-2148), but the Java, PHP, C#, Go and TypeScript future-date SDK examples create `executionDate` with **timezone only** (lines 2235-2246, 2307-2321, 2385-2401, 2511-2524, 2679-2692). Do not treat those samples as complete future-date requests or infer API validation behavior from this mismatch. It attempts processing **once**; errors such as insufficient funds end in `failed` with a webhook. Cancellation via `POST /transfers/cancel` is described **before** execution date, not as a general reversal after processing. Consult the detailed status and cancel guides for event semantics.
- **TEST fixtures:** Country/currency/priority tables give successful and unsuccessful bank-account fixtures for TEST only. Unsuccessful rows distinguish `return` from `failure` scenarios and show reason codes including account-not-found, account-closed, refused-by-bank and timeout. Those test fixtures do not prove a live route or recipient receipt.

## Detail locators

- Roles, accepting webhooks, Support enablement and request fields: pinned raw lines 15-64.
- One-off versus token request and SDK/TEST examples: pinned raw lines 66-1044.
- Priority fallback, selected-route response and received/pending example: pinned raw lines 1048-1555.
- Optional one-person review and team approval: pinned raw lines 1559-2125.
- Future-date requirement, incomplete SDK examples, conflicting timezone defaults, one-attempt failure and pre-execution cancellation: pinned raw lines 2129-2148, 2235-2246, 2307-2321, 2385-2401, 2511-2524, 2679-2706.
- Transfer-status webhooks and TEST success/return/failure fixtures: pinned raw lines 2708-2867.

## Related

- [[adyen-payouts]] — main Payout Service and payout-lifecycle concept route.

## Related raw API references

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/payout-webhooks/2026-09-15|Payout webhook guide]] — linked status and tracking reference; not separately assessed here.
- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/approve-cancel-payouts/2026-09-15|Approve/cancel payout guide]] — linked review and cancellation reference; not separately assessed here.
- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/transfer-routes/2026-09-15|Bank transfer routes guide]] — linked priority-route reference; not separately assessed here.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/bank-payout-request/2026-09-15|Payout Service third-party bank payout request guide, captured 2026-09-15]]
