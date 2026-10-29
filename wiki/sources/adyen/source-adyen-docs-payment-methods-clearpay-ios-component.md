---
title: "Adyen Clearpay iOS Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/clearpay/ios-component/2026-09-15.md"
tags: [adyen, clearpay, ios, components, redirect, capture, refund]
---

## Overview

This 2026-09-15 Adyen Docs guide adds Clearpay to an **existing iOS Components** integration using Sessions or Advanced flow. It requires Customer Area method setup and redirect handling, then uses `InstantPaymentComponent` with method type `clearpay`. The GB/GBP examples illustrate a test request, not current merchant eligibility, a successful redirect or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires Checkout API v68 or later and an existing Sessions iOS Components integration; Advanced requires an existing Advanced integration. Both require `action.type: redirect` handling and Customer Area setup. The guide says no extra Clearpay configuration parameters are needed, and shows the Component initialized with `.other("clearpay")`; Sessions delegates to the session, while Advanced delegates to `self` (pinned raw lines 25–36, 116–142, 231–268).
- Both `/sessions` and `/payments` tables mark shopper name, email, reference (minimum three characters), country code, billing and delivery addresses and `lineItems` required; phone is optional. The Advanced example supplies `paymentMethod.type: clearpay` and returns a `redirect` action with `RedirectShopper`, which is a redirect step, not evidence of authorization or capture. Example API URLs use v71 for Sessions and v72 for payments; the stated minimum v68 applies to the Sessions requirement (lines 40–114, 270–365).
- Capture depends on merchant-account configuration: automatic after authorization or manual. Capture after sending goods needs a delay or manual capture, and partial capture requires manual capture. Clearpay says capture within 13 days after authorization; otherwise it cancels and refunds the first installment charged during authorization. In test, manual capture must occur within one day (lines 144–154 and 367–377).
- Manual capture uses `/payments/{paymentPspReference}/captures` with full or partial `amount.value` and optional `lineItems`. A first partial capture cancels the remaining amount unless multiple partial captures are enabled through Support; each such capture creates a new invoice. Cancel before capture; refund after capture, including full or partial refunds via `/payments/{paymentPspReference}/refunds` amount, with optional line items (lines 156–176 and 379–399).
- A negative line amount is described for discounts, but the illustrated discount request has material arithmetic and JSON problems noted below. The testing section requires a Clearpay sandbox shopper account, links regional test resources and says a live Customer Area request is needed before accepting live payments (lines 178–229 and 401–452).

> [!warning] Example and navigation inconsistencies
> The Advanced iOS **Components** requirement links to a base URL with `integration=Drop-in` (raw line 239), while its redirect link specifies Components (line 240). The discount prose says a 1 GBP discount on Item #2, but the sample uses quantity 2 at `amountIncludingTax: "-100"` and lowers the order from 1000 to 800 minor units, indicating a 2 GBP discount; the sample also contains an ellipsis and lacks a comma between item objects, so it is not copy-ready JSON (lines 180–212 and 403–435). Both curl examples place `-X POST` on a separate line without a continuation before `-d` (lines 62–63 and 294–295); verify shell syntax before use.

## Detail locators

- Sessions scope, field table, sample request and Component setup: pinned raw lines 25–142.
- Sessions capture/refund/discount/test-live sections: lines 144–229.
- Advanced scope, field table, redirect example, lifecycle and test-live sections: lines 231–452.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-clearpay]] — method overview for GB/GBP and feature qualifications
- [[source-adyen-docs-payment-methods-clearpay-ios]] — iOS integration chooser

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/ios-component/2026-09-15|Clearpay iOS Component guide, captured 2026-09-15]]
