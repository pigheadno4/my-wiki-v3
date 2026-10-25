---
title: "Bank Transfer via KCP Web Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/web-drop-in/2026-09-15.md"
tags: [adyen, kcp, bank-transfer, web, drop-in, online-payments]
---

## Overview

This 2026-09-15 guide describes adding Bank Transfer via KCP to an existing Adyen Web Drop-in integration, with separate Sessions and Advanced server-side paths. It covers redirect setup and a testing-credential limitation, not an observed bank-transfer authorization or settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions flow:** requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, redirect handling (`action.type: redirect`) and Bank Transfer via KCP added in Customer Area. The page says no additional method-specific `/sessions` parameters are needed. Importing `Redirect` with `AdyenCheckout` and `Dropin` is optional for tree shaking, not an unconditional import requirement. (raw lines 25–54)
- **Advanced flow:** requires an existing Web Drop-in Advanced integration, redirect handling and the method added in Customer Area. It also offers optional `Redirect` import and says no extra method-specific `/payments` parameters. The Advanced base-integration URL contains an unresolved encoded `platform` template, while its heading and other links indicate Web Drop-in; this link defect does not change the stated integration type. No Advanced Checkout API minimum appears here. (raw lines 62–90)
- **Testing distinction:** both flow sections say there are no KCP bank-transfer testing credentials because authorization uses a Public Identification Certificate, also described as a digital signature for individuals. This does not establish that a TEST environment is unavailable, that a certificate was supplied or used, or that a payment succeeded. The page gives no full shopper return, webhook, live-enable, capture or settlement procedure. (raw lines 56–60, 92–96)
- **Scope:** the method-specific guide does not state a country/currency row or merchant entity requirement; those cannot be inferred from this page alone. (raw lines 15–96)

## Detail locators

- Sessions prerequisites and no extra session parameters: raw lines 29–42.
- Optional `Redirect` tree-shaking import: raw lines 44–54, 74–84.
- Advanced prerequisites and unresolved platform URL: raw lines 66–72.
- No extra payment parameters and certificate-related test limitation: raw lines 86–96.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/web-drop-in/2026-09-15|Adyen KCP bank-transfer Web Drop-in guide, 2026-09-15 snapshot]]
