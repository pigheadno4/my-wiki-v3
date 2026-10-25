---
title: "PayCo Android Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payco/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/payco/android-drop-in/2026-09-15.md"
tags: [adyen, payco, android, drop-in, online-payments]
---

## Overview

This 2026-09-15 guide describes adding PayCo to an existing Adyen Android Drop-in integration, split between Sessions and Advanced server-side flows. It states method-specific setup and testing assistance rather than an observed transaction result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions path:** requires an existing Android Drop-in Sessions integration, Checkout API v68 or later and PayCo added in Customer Area. The page says no PayCo-specific `/sessions` parameters or Drop-in configuration. Unlike its Advanced requirement, the Sessions requirement does not itself list redirect action handling; the method-specific page provides no Sessions action-handling or outcome procedure. (raw lines 25–46)
- **Advanced path:** requires an existing Android Drop-in Advanced integration, redirect handling (`action.type: redirect`) and PayCo added in Customer Area. It says no additional PayCo-specific Drop-in configuration or `/payments` parameters; it does not state an Advanced Checkout API or Android SDK version minimum. (raw lines 56–76)
- **Testing and evidence limit:** both sections say there are no PayCo-specific test credentials and direct testing-assistance questions to Adyen Support. This does not mean the TEST environment is absent. The page gives no live-enable procedure, request examples, shopper return, webhook status sequence, or proof of authorization, capture or settlement. (raw lines 48–54, 78–82)

## Detail locators

- Sessions prerequisite and no extra method parameters/configuration: raw lines 29–46.
- Advanced redirect prerequisite and no extra method parameters/configuration: raw lines 58–76.
- No specific PayCo test credentials and Support route: raw lines 48–54, 78–82.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payco/android-drop-in/2026-09-15|Adyen PayCo Android Drop-in guide, 2026-09-15 snapshot]]
