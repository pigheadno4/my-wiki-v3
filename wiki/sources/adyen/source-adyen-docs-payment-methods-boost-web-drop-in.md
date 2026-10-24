---
title: "Boost Wallet Web Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boost/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/boost/web-drop-in/2026-09-15.md"
tags: [adyen, boost, wallet, web, drop-in, online-payments]
---

## Overview

This 2026-09-15 guide describes adding Boost Wallet to an existing Adyen Web Drop-in integration. It gives separate Sessions and Advanced server-side flow requirements, redirect handling, and an optional `Redirect` import. It does not document an observed transaction result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, redirect handling (`action.type: redirect`), and Boost Wallet added in Customer Area. The page says no Boost-specific `/sessions` parameters are needed. It calls importing individual methods for tree shaking optional; if used, its example imports `Redirect` with `AdyenCheckout` and `Dropin`. (raw lines 25–54)
- **Advanced flow:** requires an existing Web Drop-in Advanced integration, redirect handling and Boost Customer Area setup. Its optional tree-shaking import likewise includes `Redirect`; it says no additional Boost `/payments` parameters are needed. The base integration link at the requirement row contains a URL-encoded template expression in the `platform` parameter rather than a resolved platform value, while the section heading and other links specify Web Drop-in. This is a source-link defect, not evidence about another platform. The page does not state an Advanced Checkout API minimum. (raw lines 62–90)
- **Environment and outcome boundary:** both sections state there is no Boost Wallet test environment and describe penny tests in LIVE. This historical guidance is not authorization to transact, proof of current merchant availability, or proof of authorization, capture or settlement. The page stops at setup, request-parameter and redirect guidance. (raw lines 56–60, 92–96)

## Detail locators

- Sessions Web Drop-in, v68+, redirect and Customer Area prerequisites: raw lines 29–36.
- Sessions no-extra-parameters and optional `Redirect` import: raw lines 38–54.
- Advanced Web Drop-in requirement and unresolved platform template URL: raw lines 66–72.
- Advanced optional import and no extra `/payments` parameters: raw lines 74–90.
- No Boost TEST environment: raw lines 56–60, 92–96.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boost/web-drop-in/2026-09-15|Adyen Boost Wallet Web Drop-in guide, 2026-09-15 snapshot]]
