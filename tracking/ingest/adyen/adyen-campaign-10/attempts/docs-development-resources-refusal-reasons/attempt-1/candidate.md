---
title: "Adyen Online Payment Refusal Reasons"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/refusal-reasons"
raw_files:
  - "adyen/docs/development-resources/refusal-reasons/2026-09-15.md"
tags: [adyen, online-payments, refusal-reasons, authorization, result-codes]
---

## Overview

This [[adyen]] development-resources reference catalogs `refusalReasonCode` and `refusalReason` values for unsuccessful online payment authorization. It explains how to interpret these alongside `resultCode`, while separating the HTTP status of an API request from the outcome of the payment or modification. See [[adyen-online-payments]] and [[source-adyen-docs-development-resources-response-handling]] for the wider response boundary.

## Key takeaways

- A payment authorization request can return HTTP `200 OK` when Adyen processed the request correctly even though the payment or modification was unsuccessful. In an unsuccessful case, `resultCode`, `refusalReason`, and `refusalReasonCode` describe the issue. Do not treat HTTP success as payment authorization or later capture or settlement.
- The page describes `refusalReason` as a short explanation, `refusalReasonCode` as its numeral, and `resultCode` as the refused-payment category (`Refused`, `Error`, or `Cancelled`). It also says the same refusal fields appear in `additionalData` of `CAPTURE_FAILED` and `REFUND_FAILED` webhooks when an online capture or refund is refused; those are modification-failure events, not a new payment-authorization result.
- Do not expose refusal-reason details to shoppers; the page cites malicious-use risk. This applies even when a detailed diagnostic is available to the merchant integration.
- Read the table row and `resultCode` together: code `0` can accompany `Authorised`, in which case the page says to ignore the refusal code. The table includes issuer, card, authentication, risk, cancellation and processing conditions; its labels are mapped refusal reasons, not a universal raw issuer-response contract.
- Retry instructions are specific to table rows and prerequisites: code `38` says retry with 3D Secure after an issuer declines an authentication exemption; code `40` says use a different payment method; codes `41` and `42` give their own retry paths. Code `46` describes Adyen blocking excessive retries to avoid penalty fees. The catalog does not authorize a blanket repeat of a pending or uncertain payment.
- This is a 2026-09-15 documentation snapshot of an unversioned page. Its test-environment trigger link describes simulation, not live issuer behavior or an individual transaction outcome.

## Detail locators

- Test-environment refusal triggers and HTTP `200` versus payment outcome: raw lines 19–25.
- Shopper-disclosure warning and online-payments/Standard-webhook requirements: raw lines 27–34.
- Example object and field definitions: raw lines 36–53.
- Full `refusalReasonCode`/`refusalReason` table, including code `0` with `Authorised`: `## Refusal responses`, raw lines 55–107. Consult the row before using a diagnostic or conditional retry instruction.
- Authentication and network retry rows plus excessive-retry prevention: raw lines 101–106.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-development-resources-response-handling]] — HTTP request status and conditional response handling.
- [[source-adyen-docs-online-payments-build-your-integration-payment-result-codes]] — online payment result-code lifecycle.
- [[source-adyen-docs-online-payments-capture-failure-reasons]] — capture and refund failure events.

## Raw Sources

- [[raw/adyen/docs/development-resources/refusal-reasons/2026-09-15|Adyen refusal reasons — collected 2026-09-15]]
