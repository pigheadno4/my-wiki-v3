---
title: "Online banking Poland iOS Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/ios-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/ios-component/2026-09-15.md"
tags: [adyen, online-payments, online-banking-poland, ios, components]
---

## Overview

This 2026-09-15-captured Adyen add-on describes Online banking Poland in an existing **iOS Components** integration, separately for Sessions and Advanced flows. It covers method setup, shopper email, Component presentation, and redirect handling. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-poland]] for the method overview. This source is a dated integration guide, not proof of current merchant eligibility or a completed payment.

## Key takeaways

- Both flows require an existing iOS Components integration and Online banking Poland setup in Customer Area. The Sessions requirements specify Checkout API v68 or later and redirect handling. In the Sessions /sessions request, shopperEmail is marked required and limited to 50 characters; the sample uses PL/PLN and an app-style returnUrl. See raw lines 25–69.
- The page says no additional Online banking Poland configuration parameters are needed. Its Sessions and Advanced Swift initialization text nevertheless names a `None` class and supplies `onlineBankingPolandConfiguration`; these placeholders/conflicting instructions do not establish a usable Component class or a complete executable initialization recipe. See raw lines 270–299 and 320–346.
- In Advanced flow, the /payments table marks shopperEmail required (50 characters maximum) and lists paymentMethod.issuer for the shopper-selected bank without marking that field required. The example uses type `onlineBanking_PL`, issuer `141`, PLN 1000, and a web returnUrl; those example values are not universal requirements. The illustrated response has resultCode `RedirectShopper` with action.type `redirect`, an intermediate redirect instruction rather than evidence of final payment status. See raw lines 349–383 and 692–706.
- The guide directs test-status checks to the test Customer Area Payment list and says live acceptance requires a request for Online banking Poland in the live Customer Area. See raw lines 301–305 and 708–712.

> [!warning] Source inconsistency
> The Advanced requirements call for iOS Components but its base-integration link has `integration=Drop-in` (raw line 315). Both flow snippets use `None` and a configuration object despite the page saying no added configuration is needed (raw lines 270–299, 320–346). Follow the linked base integration and verify the actual SDK type and setup before implementing; this snapshot alone does not resolve the inconsistency.

## Detail locators

- Sessions requirements and required shopperEmail: raw `## Sessions flow Component`, lines 25–46.
- Sessions request and example returnUrl/country/currency: raw `## Add additional parameters to your /sessions request`, lines 40–69.
- Configuration and Sessions initialization: raw `## Add additional configuration for Online banking Poland` and `## Initialize the Component for Online banking Poland`, lines 270–299.
- Advanced prerequisites and initialization: raw `## Advanced flow Component`, lines 307–346.
- Advanced fields, request example, and redirect response: raw `## Add additional parameters to your /payments request`, lines 349–383, and redirect response lines 692–706.
- Test/live instructions: raw `## Test and go live`, lines 301–305 and 708–712.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-poland]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/ios-component/2026-09-15|Online banking Poland iOS Component, captured 2026-09-15]]
