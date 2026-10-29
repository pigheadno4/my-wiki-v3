---
title: "Adyen Cash App Afterpay iOS Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/ios-drop-in/2026-09-15.md"
tags: [adyen, cash-app-afterpay, ios, drop-in, capture, refunds]
---

## Overview

This 2026-09-15-captured Adyen guide adds Cash App Afterpay to an existing iOS Drop-in integration. It separates Sessions and Advanced flows, then covers method request fields, capture and refund behavior, discounts, and test/live setup. Its examples are US/USD and the `/payments` example uses method type `afterpaytouch_US`. The page does not establish current merchant eligibility, live operation or payment success. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Both flows require an existing iOS Drop-in integration and Cash App Afterpay added in Customer Area. The API reference calls `/sessions` the default for Drop-in v5.0.0 or later; `/payments` is shown for an additional use case. Both tables mark shopper name, email, unique `shopperReference` of at least three characters, countryCode, billing and delivery addresses, and lineItems required; phone is optional. The `/payments` sample uses `paymentMethod.type=afterpaytouch_US`, US and USD (pinned raw lines 21–56, 740–774). The sample's empty shopper reference and name fields need the warning below.
- The page says there is no Cash App Afterpay-specific Drop-in integration required for v5.0.0+ or v4.x.x (lines 1210–1218). That does not remove its base integration and API request requirements.
- Capture depends on merchant account configuration: automatic after authorisation or manual. A delayed capture needs capture-delay setup or manual capture; a partial capture needs manual capture. Capture must occur within **13 days** of authorisation; otherwise Cash App Afterpay cancels and refunds the first installment charged during authorisation. Test authorisations expire after **one day**, so manual test captures must occur within that day (lines 1220–1230).
- A manual capture request can specify full or partial `amount.value`, with optional lineItems. An initial partial capture normally cancels the unclaimed balance; when the account is enabled for multiple partial captures, that balance is retained and each capture creates a new invoice. Support must enable multiple partial captures. Uncaptured payments can be cancelled; captured payments need refunds, with full/partial `amount.value` and optional lineItems (lines 1231–1250).
- Discounts are expressed as negative amounts in payment line items. The example describes a “1 USD” discount on Item #2 but shows quantity 2 at -100 minor units each, with total amount 800 from a 1000 base. That is consistent with one USD **per unit** (two USD total), though the prose does not say per unit. The sample also contains ellipsis and a missing comma between item objects, so it is illustrative rather than valid JSON (lines 1252–1286).
- Testing requires an Afterpay sandbox shopper account for US, a test card, and the source's documented test setup. The guide says to submit a Cash App Afterpay request in the live Customer Area before accepting live payments (lines 1288–1306).

> [!warning] Required fields versus examples
> Both API tables require a unique `shopperReference` of at least three characters, but the Sessions and Payments examples populate it with an empty string (raw lines 51, 74, 748, 774; repeated across language samples). The tables also call for a shopper's full name while examples use empty first and last names. Do not copy the empty values as compliant request data.

## Detail locators

- Flow requirements and Sessions table/examples: pinned raw lines 15–739.
- Payments table, `afterpaytouch_US` and language examples: lines 740–1209.
- Drop-in version notes, capture limits and partial capture conditions: lines 1210–1239.
- Cancel/refund, discount sample and test/live setup: lines 1241–1312.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-cash-app-afterpay]] — method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/ios-drop-in/2026-09-15|Cash App Afterpay iOS Drop-in guide, captured 2026-09-15]]
