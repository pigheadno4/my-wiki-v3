---
title: "Adyen Bank Transfer via KCP Android Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp/android-component"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/android-component/2026-09-15.md"
tags: [adyen, kcp, bank-transfer, android, components, south-korea]
---

## Overview

This [[adyen]] guide adds **Bank Transfer via KCP** to an existing Android Components integration, with separate Sessions and Advanced instructions. It is a method add-on to the main integration guides, not a standalone bank-transfer implementation. See [[adyen-online-payments]] and [[adyen-android-sdk]]. This captured 2026-09-15 page does not establish current account eligibility, successful bank authorization, settlement or refund.

## Key takeaways

- **Sessions** requires an existing Android Components Sessions flow, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and method addition in Customer Area. The page says no extra method-specific `/sessions` parameters or Component configuration. These statements do not waive the base integration's standard fields or redirect handling. See raw lines 25–42 and 67–71.
- **Advanced** requires an existing Android Components Advanced flow, handling an additional `redirect` action, and adding the method in Customer Area. It likewise says no extra KCP configuration or `/payments` parameters. The guide states no separate Checkout API minimum for Advanced. See raw lines 132–140, 165–175 and 228–232.
- Both flows use `InstantPaymentComponent` for method type **`kcp_banktransfer`**. The guide gives Compose and non-Compose examples: import `instant` and, for Compose, `components-compose`; Sessions obtains the method from `checkoutSession`, while Advanced selects it from `/paymentMethods` response. The Compose examples require a distinct key for a different screen/payment session and a new key when resetting the Component. Module versions remain `YOUR_VERSION` placeholders, not a stated Android SDK minimum. See raw lines 44–126 and 142–226.
- Under **Test and go live**, both flow sections say there are **no KCP bank-transfer testing credentials** because authorization uses a Public Identification Certificate, also called a “Digital Signature for individuals.” This does not establish that the method lacks a TEST environment, that a merchant may simulate a signature, or that a live transfer should be attempted. The page gives no actual live-onboarding step or final webhook/payment-result procedure. See raw lines 128–130 and 234–236.

## Detail locators

- **Sessions prerequisites, v68 gate, redirect action and request condition:** raw lines 25–42.
- **Sessions imports and InstantPaymentComponent examples:** raw lines 44–126.
- **Advanced prerequisites, import/configuration and Component examples:** raw lines 132–226.
- **Advanced request condition:** raw lines 228–232.
- **No KCP testing credentials/PIC explanation:** raw lines 128–130 and 234–236.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[source-adyen-docs-payment-methods-bank-transfer-kcp]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/android-component/2026-09-15|Bank Transfer via KCP Android Component guide — captured 2026-09-15]]
