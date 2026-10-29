---
title: "Cash App Afterpay | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/2026-09-15.md"
tags: [adyen, cash-app-afterpay, buy-now-pay-later, redirect, chargebacks]
---

## Overview

This 2026-09-15-captured [[adyen]] overview describes **Cash App Afterpay** as a US/USD buy now, pay later **redirect** method for US merchants. It says the shopper may pay in four installments and that Cash App Afterpay checks shopper risk before approval. **If successful**, the page says it takes full fraud risk for the payment and pays the merchant up front (raw lines 23–29). These statements do not prove a particular merchant's current eligibility, a shopper's approval, guaranteed settlement or a completed payment. See [[adyen-online-payments]].

## Key takeaways

- **Regional product identity:** The page also calls the US service `$Afterpay`. It points to Afterpay in Australia and New Zealand and Clearpay in the UK as regional names (raw line 31). Its own US/USD table should not be applied unchanged to those regional products.
- **Captured feature matrix:** The table marks recurring unavailable. It marks refunds, partial and multiple partial refunds, separate captures, partial and multiple partial captures, and chargebacks available. The refunds checkmark says **“See note”**, but this captured page does not include note text; do not treat it as an unconditional refund rule. These marks are method-level indicators, not an account entitlement or transaction procedure (raw lines 27–29).
- **Chargeback windows:** The page says shoppers may initiate chargebacks directly with Cash App Afterpay up to **120 days** after payment, cancellation or expected receipt of goods or services. Once Cash App Afterpay opens a dispute, the merchant has **13 days** to defend or accept. No response or acceptance loses the dispute and debits the account; if defended, Cash App Afterpay has **30 days** to decide (raw lines 33–37). These are captured source statements, not proof of current account terms.
- **Integration navigation:** The overview links Web, iOS, Android, API-only and Pay by Link routes (raw lines 39–69). The API-only label describes building one's own UI for a website or iOS/Android app; Pay by Link points to a payment-link API route. Read the selected route for request fields, redirect/return, capture, refund and version conditions. The overview itself does not define those implementation steps.

## Detail locators

- US merchant, four-installment, conditional risk/fraud statement and US/USD feature matrix: pinned raw lines 15–29.
- Regional names and chargeback timing/consequence: pinned raw lines 31–37.
- Web, iOS, Android, API-only and Pay by Link routes: pinned raw `## How do you want to integrate?`, lines 39–69.

## Related

- [[adyen-online-payments]] — provider online checkout context.
- [[source-adyen-docs-payment-methods-afterpaytouch]] — separate AU/CA/NZ Afterpay overview.
- [[source-adyen-docs-payment-methods-clearpay]] — separate GB/GBP Clearpay overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/2026-09-15|Cash App Afterpay overview, captured 2026-09-15]]
