---
title: "Adyen Atome API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/api-only"
raw_files:
  - "adyen/docs/payment-methods/atome/api-only/2026-09-15.md"
tags: [adyen, atome, api-only, advanced-flow, malaysia, singapore, redirect]
---

## Overview

This [[adyen|Adyen]] page, fetched and marked last modified 2026-09-15, adds Atome to an existing **Web API-only Advanced-flow** integration. The merchant builds the payment form, makes Checkout API discovery/payment requests, and handles the redirect action through its base integration. See [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-atome|Atome overview]] for method-level product limits. This captured guide is not evidence of current merchant eligibility or payment success.

## Key takeaways

- **Prerequisites and form:** Start with an existing API-only integration configured for additional `action.type: redirect` handling, then add Atome in Customer Area. The merchant-built form collects the shopper's full name, email, phone, billing and delivery addresses for Atome risk checks and includes purchase-item details in the payment request. For method discovery, use supported country/currency pairs **MY/MYR** and **SG/SGD**; `/paymentMethods` examples show `type: atome` when available. A sample response does not guarantee account availability.
- **Payment request:** The `/payments` table marks `paymentMethod.type: atome`, name, email, phone, billing address, line items, and country code required. It describes delivery address as optional when billing and delivery addresses are the same. The TEST v72 sample uses SG/SGD and an HTTPS `returnUrl`. The response has `resultCode: RedirectShopper` and `action.type: redirect`; the shopper must be redirected and return handling completed under the base flow. This is a redirect instruction, not a settled payment.
- **Refund and test/live:** For a partial refund, the page calls for the refunded `amount` in `/payments/{paymentPspReference}/refunds`. Its refunds/cancellations heading supplies no additional method-specific cancellation instructions. Testing requires an Atome sandbox shopper account from the Adyen contact, with a different account for each country/region tested; QR test apps and test Customer Area status are linked. Live acceptance requires contacting Adyen Support to add Atome in the **live** Customer Area.
- **Sample and method boundaries:** The TEST curl examples for both `/paymentMethods` and `/payments` omit a shell continuation between `-X POST` and `-d`, so they are not copy-ready. The discovery sample's `shopperLocale: sg-SG` is an example value, not a required locale rule. The separate captured overview excludes portable electronics and says Atome payments capture automatically after authorization; this API-only add-on does not repeat those product/capture qualifications.

## Detail locators

- Purpose, existing API-only and redirect prerequisites: pinned raw lines 15–29. Merchant-built form, risk-check data and country/currency pairs: lines 31–57. `/paymentMethods` filters, v72 TEST examples and response: lines 59–355.
- `/payments` required/optional table and SG/SGD v72 TEST example: lines 357–1085. Redirect response: lines 1087–1101. Partial refund and test/live steps: lines 1103–1133. Method-level product/capture limits reside in [[source-adyen-docs-payment-methods-atome]].

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-atome]] — method overview and product restrictions

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/api-only/2026-09-15|Atome API-only guide, fetched 2026-09-15]]
