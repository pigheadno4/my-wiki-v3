---
title: "PayNow React Native Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paynow/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/paynow/react-native-component/2026-09-15.md"
tags: [adyen, paynow, react-native, components, qr-code, online-payments]
---

## Overview

This 2026-09-15 PayNow React Native Components guide covers only the Advanced server-side flow: it explicitly says React Native Components do not support Sessions flow. It identifies QR-code action handling and live setup, not a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Flow boundary:** the Sessions tab says React Native Components do not support Sessions. The Advanced tab requires an existing React Native Components Advanced integration, handling an additional `action.type: qrCode`, and PayNow added in Customer Area. The Advanced integration requirement's link uses `integration=Drop-in` despite the Components label and the Components links for action handling and payments; this remains an unresolved source-link mismatch. The page gives no SDK or Checkout API minimum. (raw lines 23–41)
- **Method additions:** the Advanced section says PayNow requires no extra Component configuration and no extra parameters on `/payments`. It does not show Component initialization, QR rendering, a QR expiry setting, a shopper return path or a final callback/webhook sequence; the linked general integration guide supplies the broader flow. (raw lines 43–53)
- **Live/test warning:** before live acceptance, the page requires contacting Adyen Support to add PayNow to the live Customer Area. It describes penny testing there with a real banking app and status lookup in the live Customer Area, while recommending against test Customer Area payments because test-environment bank transfers cannot be reversed and funds are deducted. This historical guidance does not authorize a real payment or prove current availability, authorization, capture or settlement. (raw lines 55–63)

## Detail locators

- Sessions unsupported and Advanced prerequisites/link mismatch: raw lines 25–41.
- No additional Advanced configuration or `/payments` fields: raw lines 43–53.
- Live Support gate, status route and consequential test warning: raw lines 55–63.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paynow/react-native-component/2026-09-15|Adyen PayNow React Native Component guide, 2026-09-15 snapshot]]
