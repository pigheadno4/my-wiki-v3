---
title: "Adyen Standard Drop-in optional configuration"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/drop-in/optional-drop-in-configuration"
raw_files:
  - "adyen/docs/standard/integration/drop-in/optional-drop-in-configuration/2026-09-15.md"
tags: [adyen, online-payments, standard-integration, web-drop-in, configuration]
---

## Overview

This 2026-09-15 [[adyen]] guide describes optional client-side configuration for a **Standard Web Drop-in** integration under [[adyen-online-payments]]. It distinguishes settings on the per-payment-session `AdyenCheckout` object from settings on the shopper-facing `Dropin` instance. UI configuration and callbacks do not establish a payment outcome.

## Key takeaways

- For a smaller bundle, individual payment-method imports can be used; every method subsequently added must also be imported. **If** individual methods are imported, the Drop-in configuration must include `paymentMethodComponents` listing those imported methods. The code example later lists `Ideal` in that array without importing it in the earlier import snippet, so the snippets are illustrative and should be aligned before use. See raw lines 21–38 and 97–107.
- `AdyenCheckout` represents one payment session. Its optional `secondaryAmount` shows an additional currency on the Pay button, with the merchant doing the conversion and supplying the amount in minor units; this is display configuration, not an Adyen FX quote. `donation` is another optional configuration object. See raw lines 40–53.
- `beforeSubmit` can add shopper details to the payment request. The guide says to continue with `actions.resolve()` regardless of result code, including an unsuccessful payment; use `actions.reject()` only for a failed server-side Adyen API request or network issue. It also lists action-display and form-change event handlers. See raw lines 55–65.
- At the `Dropin` instance, method-specific `paymentMethodsConfiguration` overrides the global setting on `AdyenCheckout`. Stored/regular method display and initial opening, automatic selection, iframe redirect, wallet prominence, final animation and radio buttons have optional controls and documented defaults or applicability. `redirectFromTopWhenInIframe` sets top-level redirects when enabled, while the guide recommends avoiding an iframe. See raw lines 67–87.
- Enabling `showRemovePaymentMethodButton` requires implementing `onDisableStoredPaymentMethod`; when a shopper removes a stored method, the handler must DELETE that `storedPaymentMethodId` and then call `resolve()` or `reject()` according to the DELETE response. Showing the button alone does not perform or prove deletion. See raw lines 80–81 and 89–95.

## Detail locators

- **Individual imports and conditional component array:** raw lines 21–38, 73–75, 97–107.
- **Per-session `AdyenCheckout` amount/donation configuration and callbacks:** raw lines 40–65.
- **Drop-in display settings, defaults, precedence and iframe guidance:** raw lines 67–87.
- **Stored-method deletion callback:** raw lines 89–95.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-standard-integration-drop-in]]

## Raw Sources

- [[raw/adyen/docs/standard/integration/drop-in/optional-drop-in-configuration/2026-09-15|Adyen Standard Drop-in optional configuration — collected 2026-09-15]]
