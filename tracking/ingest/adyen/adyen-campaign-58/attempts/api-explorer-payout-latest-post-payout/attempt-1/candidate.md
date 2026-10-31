---
title: "Adyen Payout API v68: POST /payout instant card payout"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payout/latest/post/payout"
raw_files:
  - "adyen/api-explorer/Payout/latest/post/payout/2026-09-15.md"
tags: [adyen, payouts, cards, payout-api, deprecated]
---

## Overview

This captured Payout API reference describes `POST /payout` for instant payouts to a customer's Visa or Mastercard card. The endpoint is **deprecated and does not support new integrations**. Adyen directs new integrations to Transfers API `POST /transfers`, and existing Payout API users to their Adyen contact for migration. Its listed server is Payout v68 TEST, `https://pal-test.adyen.com/pal/servlet/Payout/v68`. The stated availability of funds within 30 minutes on the cardholder's bank account depends on issuer support; it is not a guaranteed receipt time.

## Key takeaways

- The request table marks `amount` (with required `currency` and minor-unit `value`), `merchantAccount` (the processing merchant account identifier), and `reference` required. The page recommends a unique reference per payment but explicitly says uniqueness is **not** required; this does not establish an idempotency guarantee. The generic amount description's zero-value BIN/card-verification instruction is not an instant-payout amount rule.
- The top-level `card` container carries recipient card data; `fundSource`, when supplied, describes the person or entity funding the money and may itself contain a card. Do not exchange recipient and funding identities. The request table also contains generic payment/recurring fields, including a generic “either `bankAccount` or `card`” sentence inside `card`; the endpoint's stated instant-payout scope is Visa/Mastercard **cards**, and this capture does not document a bank-payout request route.
- Conditional request descriptions include `billingAddress` for 3DS2 browser/mobile transactions and cross-border payouts to/from Canada, with required nested address fields; `stateOrProvince` is required for US/Canada addresses. For recurring use, `shopperReference` is required, case-sensitive, at least three characters, and must exclude PII. The table also gives conditional Visa/JCB 3DS2 email/telephone alternatives, a stored-detail selector `selectedRecurringDetailReference` (including `LATEST`), and `shopperInteraction` channel values; these generic schema details should not expand the stated Visa/Mastercard payout support. See pinned raw for exact field conditions and formats.
- The 200 schema uses payment-style `resultCode`, `pspReference`, `authCode`, and `refusalReason` descriptions. In particular, `Received` means Adyen received a payment for processing, `Pending` lacks final payment status, and `Authorised` is described as a final **payment authorisation** state. These descriptions do not prove payout settlement or cardholder bank receipt. The page lists 400, 401 (authentication), 403 (permissions), 422, and 500 responses. The TEST snapshot does not prove merchant enablement, live eligibility, a successful payout, or current availability.

## Detail locators

- Deprecation, migration, card scheme/timing qualification, and v68 TEST server: pinned raw lines 5–26.
- Required amount, merchant account and reference; conditional address, card, funding source, recurring, shopper and channel fields: pinned raw lines 30–91.
- Illustrative B2C and P2P request JSON, with distinct recipient and funding cards: pinned raw lines 93–176.
- 200 response metadata and payment-style result-code vocabulary: pinned raw lines 177–200.
- Error response schemas and illustrative 400 JSON: pinned raw lines 203–284.

## Related

- [[adyen-card-payouts]] — legacy instant card-payout context and its migration boundary.
- [[adyen-payouts]] — broader payout families, distinct from this legacy endpoint.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Payout/latest/post/payout/2026-09-15|Payout API v68 POST /payout capture (2026-09-15)]]
