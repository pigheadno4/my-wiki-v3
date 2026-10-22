---
title: "Adyen Standard Web Drop-in checkout customization"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/drop-in/customize-checkout"
raw_files:
  - "adyen/docs/standard/integration/drop-in/customize-checkout/2026-09-15.md"
tags: [adyen, online-payments, standard-integration, web-drop-in, localization]
---

## Overview

This 2026-09-15 [[adyen]] **Standard Web Drop-in** guide describes customizing checkout payment-method order, language/localization, text direction and styling within [[adyen-online-payments]]. It is a configuration guide, not evidence that a payment method is enabled for a merchant or that a change has been applied in a live checkout (raw lines 15–28, 50–52, 157–169).

## Key takeaways

- **Ordering choice:** Dynamic payment-method ordering is enabled by default and Adyen highly recommends it. Customer Area settings can prioritize cost or conversion for all or selected countries/regions. Manually selecting methods by country is available, but the page says it disables dynamic ordering and does not recommend it (raw lines 24–48).
- **Locale resolution and overrides:** Drop-in uses the global `AdyenCheckout` `locale`; if absent it uses the session `shopperLocale`; an unmatched locale falls back to `en-US`. A `translations` object plus matching `locale` in global configuration can replace included text or define a custom locale. Missing keys in the custom-locale example fall back to `en-US` values (raw lines 54–155). Localization changes affect UI text, not payment-method or merchant eligibility.
- **Direction and styling boundaries:** Text direction stays left-to-right unless the checkout container's parent has an HTML `dir` attribute; merely setting an RTL locale is insufficient. CSS custom properties and an override stylesheet imported after Adyen CSS can style elements outside an iframe; the page does not promise styling of iframe contents (raw lines 157–188).
- **Example mismatch:** The custom-locale code constructs `globalConfiguration` but calls `AdyenCheckout(configuration)` in the same snippet (raw lines 147–155). Treat that as an unresolved variable-name mismatch in the example, not a tested working invocation.

## Detail locators

- Dynamic default, cost/conversion controls and manual-ordering tradeoff: raw lines 24–48.
- Included-language, global/session locale precedence and en-US fallback: raw lines 50–63.
- Translation overrides and custom-locale parameters/examples: raw lines 65–155.
- Separate right-to-left direction and outside-iframe CSS styling: raw lines 157–188.

## Evidence boundary

This guide documents configuration surfaces for the Standard Drop-in UI. The source does not itself specify a Web SDK version or prove that any particular translation key, CSS override, payment method, or ordering goal is effective in a merchant's deployment. Follow the parent integration's own version and setup requirements; validate the source's variable-name mismatch before copying the example.

## Related

- [[adyen-online-payments]] — online-payment and Drop-in route.
- [[source-adyen-docs-standard-integration-drop-in]] — parent Sessions/Web Drop-in setup.
- [[source-adyen-docs-standard-integration-drop-in-best-practices]] — separate embedding and production setup guidance.

## Raw Sources

- [[raw/adyen/docs/standard/integration/drop-in/customize-checkout/2026-09-15|Pinned Standard Drop-in customization guide, captured 2026-09-15]]
