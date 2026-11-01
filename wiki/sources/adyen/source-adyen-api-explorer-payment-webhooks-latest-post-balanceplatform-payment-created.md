---
title: "Adyen deprecated Payment webhook: payment.created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/payment-webhooks/latest/post/balancePlatform.payment.created"
raw_files:
  - "adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.payment.created/2026-09-15.md"
tags: [adyen, platforms, payment-webhooks, deprecated, authorisation, transfers]
---

## Overview

Captured incoming `balancePlatform.payment.created` reference in the Payment webhooks v1 family. Adyen sends it when a payment authorisation, refund, or funds transfer is initiated. It informs the recipient of a request and, for payments, the authorisation result; Adyen directs actual fund-movement tracking to subsequent outgoing or incoming transfer webhooks. The separately captured [[source-adyen-api-explorer-payment-webhooks-latest-overview|Payment webhooks family overview]] calls this family **deprecated** and directs readers to accounting webhooks; this endpoint's fields should not be applied by analogy to the newer Transfer or Transaction webhook families.

## Key takeaways

- Distinguish the request from its content: a payment has an authorisation result, processing-merchant information and a negative amount; a refund identifies the payment instrument and has a positive amount; an incoming or outgoing funds transfer has a direction-dependent signed amount. The prose says it includes only balance-account information, but the funds-transfer example includes an `accountHolder` object (raw lines 200–204). This is a discrepancy; the schema marks `accountHolder` optional, so neither passage establishes universal presence or absence.
- `data`, `environment` (`test` or `live`), and `type` are top-level required fields. Nested `data` properties are marked optional at the parent level; `currency` and minor-unit `value` are required **within** `amount` and `originalAmount` when those objects occur. The schema describes `amount` in the balance-account currency and `originalAmount` in the transaction currency. Do not infer that either optional amount is always present.
- For this exact event type, `data.status` values are `Authorised`, `Refused`, or `Error`; the shared status row also lists values for other webhook types. An `Authorised` request is not a booked transfer or settled payout. The examples show authorised payment, funds-transfer and refund requests, plus a refused payment; their values are illustrations, not universal payload shapes.
- The optional `merchantData` object is described as included only for payment authorisation requests and captures. The optional `modification` object reports the triggering modification, with examples such as partial cancellation or partial expiry. `platformPayment` contains separate payment and modification PSP/merchant references and split information; `reference` and `referenceForBeneficiary` have separate transfer-request and counterparty meanings.
- The `200 Success` section says any HTTP `2xx` accepts the webhook; optional `notificationResponse` is shown. Acceptance does not prove booking, settlement, refund completion, bank receipt, or the later transfer result. This reference does not specify delivery order, retries, deduplication, or signatures.

## Detail locators

- Event purpose, request-versus-movement distinction, and signed-amount cases: raw lines 5–15.
- Body table, including nested requiredness, identities, references, status by event type, validation/rule details, and optional timestamps: raw lines 17–87.
- Authorised-payment example and validation results: raw lines 89–191.
- Funds-transfer and refund-request examples: raw lines 193–272.
- Refused-payment example and transaction-rule result: raw lines 274–380.
- Webhook response/acceptance: raw lines 381–389.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[source-adyen-api-explorer-payment-webhooks-latest-overview]] — family-level deprecation and migration route.

## Raw Sources

- [[raw/adyen/api-explorer/payment-webhooks/latest/post/balancePlatform.payment.created/2026-09-15|Payment-created webhook reference, captured 2026-09-15]]
