---
title: "Adyen Online banking Thailand iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/ios-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/ios-component/2026-09-15.md"
tags: [adyen, online-banking, thailand, ios, components]
---

## Overview

This 2026-09-15 Adyen guide adds **Online banking Thailand** to an existing iOS Components integration. It splits the method additions between Sessions and Advanced server-side flows, with an `InstantPaymentComponent` and redirect handling. The guide is not the full iOS integration and does not establish a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites:** The Sessions section requires an existing iOS Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and Customer Area method addition. It says no extra `/sessions` parameters or method configuration parameters are needed. (raw lines 25–48)
- **Sessions Component:** Its Swift sample looks up `.other("molpay_ebanking_TH")`, returns if unsupported, creates `InstantPaymentComponent`, assigns the session as delegate and calls `initiatePayment()`. This is sample integration logic, not proof that a shopper completed bank authorization. (raw lines 50–70)
- **Advanced prerequisites and Component:** The Advanced section labels the required integration as iOS Components, but its integration-type link has `integration=Drop-in`; the redirect-handling link uses `integration=Components`. Preserve that link mismatch when following the base guide. It requires redirect handling and Customer Area method addition, says no extra method configuration or `/payments` parameters are needed, and shows the same method lookup with a Component delegate. No Checkout API minimum is stated in the Advanced requirements table. (raw lines 80–123)
- **Testing and live request:** Both flow sections direct test payments with an issuer ID available for the respective country/region, test-status inspection in Customer Area, and a separate request in the live Customer Area before accepting live payments. This page does not enumerate the issuer IDs or prove live approval, final authorization or settlement. (raw lines 72–78, 125–131)

## Detail locators

- Sessions prerequisites and parameter/configuration absence: raw lines 25–48.
- Sessions `InstantPaymentComponent` example: raw lines 50–70.
- Advanced prerequisite-link mismatch and redirect/setup requirements: raw lines 80–90.
- Advanced configuration, Component and request additions: raw lines 92–123.
- Test and live-request directions: raw lines 72–78 and 125–131.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/ios-component/2026-09-15|Adyen Thailand online-banking iOS Component, 2026-09-15 snapshot]]
