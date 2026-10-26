---
title: "Swish Android Component | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/swish/android-component"
raw_files:
  - "adyen/docs/payment-methods/swish/android-component/2026-09-15.md"
tags: [adyen, swish, android, components, qr, wallet]
---

## Overview

This [[adyen]] guide gives Swish-specific additions to an existing Android Components checkout, separately for Sessions and Advanced server-side flows. It uses `InstantPaymentComponent` for `swish`; the Advanced prerequisites call for additional-action handling with `action.type: qr`. This dated source is an integration guide, not proof of current merchant eligibility, payment authorization, capture or settlement. See [[adyen-online-payments]] and the separate [[source-adyen-docs-payment-methods-swish|Swish overview]] for method and regional context.

## Key takeaways

- **Sessions:** Requires an existing Android Components Sessions integration, Checkout API v68 or later and Swish added in Customer Area. It says no extra Swish parameters are needed for `/sessions`. The configuration table lists `setSubmitButtonVisible` with a blank Required cell as a visibility option; it does not make that setting mandatory. See raw lines 25–41 and 66–86.
- **Advanced:** Requires an existing Android Components Advanced integration, handling an additional `qr` action and adding Swish in Customer Area. It says no extra Swish-specific `/payments` parameters are needed. The same optional-looking submit-button visibility setting appears. The page states no Advanced Checkout API minimum. See raw lines 151–159, 184–204 and 263–267.
- **Android setup:** Both flow sections import `com.adyen.checkout:instant:YOUR_VERSION`; Compose adds `components-compose:YOUR_VERSION`. They select `swish` from the Session or `/paymentMethods` response, then use `InstantPaymentComponent`. Compose wraps it with `AdyenComponent` and a key that changes for a different screen/session or reset; View examples attach it to a view. `YOUR_VERSION` is a placeholder, not a pinned SDK requirement. See raw lines 43–64, 88–140, 161–181 and 206–260.
- **TEST and live gates:** The page says a Swish TEST payment is authorised within 15 seconds and documents Merchant Swish Simulator refusal scenarios through an error code in `shopperStatement` (example `FF08`). It directs merchants to check the TEST Payment list. Accepting live Swish requires a separate request in the live Customer Area. These documented test expectations and simulator inputs are not proof that an actual payment was authorized or that a live merchant is enabled. See raw lines 143–149 and 269–275.

> [!warning] Action type differs across Swish guides
> This Android Components page states `action.type: qr` for Advanced action handling (raw line 158). The separately retained [[source-adyen-docs-payment-methods-swish-api-only|Swish API-only guide]] notes an example response with `action.type: qrCode`. The pages do not reconcile the values; use the actual response and version-qualified base-flow guidance rather than silently equating them. The configuration snippets here also contain placeholders and a nested brace structure, so they are illustrative rather than executable code as printed. See raw lines 76–86 and 194–204.

## Detail locators

- Sessions requirements, import/configuration and Compose/View creation: raw lines 25–140.
- Advanced QR-action requirement, import/configuration, Component creation and no-extra-payment-parameters note: raw lines 151–267.
- TEST authorization claim, refusal simulator and live-request gate: raw lines 143–149 and 269–275. This method page supplies no country/currency matrix or complete QR/webhook lifecycle.

## Related

- [[adyen-android-sdk]] — separately versioned native Components architecture; this page pins no SDK release.
- [[source-adyen-docs-payment-methods-swish-api-only]] — separate Web API-only QR/app handoff and webhook outcome guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/swish/android-component/2026-09-15|Swish Android Component, 2026-09-15 snapshot]]
