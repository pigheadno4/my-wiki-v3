---
title: "Alipay+ iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay-plus/ios-component"
raw_files:
  - "adyen/docs/payment-methods/alipay-plus/ios-component/2026-09-15.md"
tags: [adyen, alipay-plus, ios, components, redirect, wallets]
---

## Overview

This 2026-09-15 Adyen guide adds Alipay+ to an existing iOS Components integration, with separate Sessions and Advanced flow instructions. The page uses Adyen's `InstantPaymentComponent` for the generic `alipay_plus` method and requires the existing integration to handle a redirect action. It is an integration add-on, not proof of current wallet-level eligibility, live enablement or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The existing iOS Components Sessions flow must use Checkout API v68 or later, handle `action.type: redirect`, and have Alipay+ added in Customer Area. The page says no extra `/sessions` or Alipay+ configuration parameters are needed. The Swift example checks for `.other("alipay_plus")` in session payment methods, sets the session as delegate and calls `initiatePayment()`. Component initialization does not by itself prove a final payment result. (raw lines 25–69)
- **Advanced:** The existing iOS Components Advanced flow must handle the redirect and have the method added in Customer Area. The page says no extra Alipay+ configuration or `/payments` parameters are needed. The example checks for `.other("alipay_plus")`, sets the Component's delegate to `self` and calls `initiatePayment()`. This section states no Checkout API or iOS SDK version minimum. (raw lines 84–127)
- **Source link mismatch:** The Advanced requirement calls for an “iOS Components integration” but its linked base URL has `integration=Drop-in`; the redirect and payment-request links use `integration=Components`. Treat the base-guide link as inconsistent rather than evidence that Advanced Drop-in and Components are interchangeable. (raw lines 90–94, 123–127)
- **Environment and setup ambiguity:** Both flow sections state that Alipay+ has no test environment and recommend live penny tests; neither shows an observed transaction. Both require adding **Alipay+** in Customer Area, but their live acceptance instruction says to submit a request for **Alipay** in the live Customer Area. This name mismatch is unresolved; the live request remains a separate documented prerequisite. No wallet/card/account operation was performed. (raw lines 33–36, 72–82, 92–94, 129–139)
- **Scope:** The page does not describe wallet selection, wallet-specific `paymentMethod` values, webhook finality, tokenization, recurring, capture or settlement. These cannot be inferred from the generic Component example or redirect requirement; the Alipay+ overview and API-only guide are separate authorities. (raw lines 15–139)

## Detail locators

- Sessions requirements, no extra request/configuration and Swift Component example: raw lines 25–69.
- Sessions TEST/live and naming mismatch: raw lines 72–82.
- Advanced requirements, mismatch in base link, Component setup and request additions: raw lines 84–127.
- Advanced TEST/live and naming mismatch: raw lines 129–139.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipay-plus]]
- [[source-adyen-docs-payment-methods-alipay-plus-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay-plus/ios-component/2026-09-15|Adyen Alipay+ iOS Component guide, 2026-09-15 snapshot]]
