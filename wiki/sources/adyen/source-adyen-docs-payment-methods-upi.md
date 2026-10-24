---
title: "UPI"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/upi"
raw_files:
  - "adyen/docs/payment-methods/upi/2026-09-15.md"
tags: [adyen, upi, india, online-payments, payment-methods]
---

## Overview

This 2026-09-15 Adyen UPI overview describes India UPI payment options, a merchant entity/integration prerequisite, a historical UPI Collect transition notice and links to channel-specific guides. It does not specify UPI AutoPay mandate creation or recurring charge execution; its recurring capability mark has an unresolved “See note” qualification on this page. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The page says that processing UPI requires complying with its linked India regulations guide and having a **local entity and local integration in India**; it directs merchants to their account manager or Adyen Support for more information. This is the provider's historical prerequisite statement, not a current legal assessment or proof of onboarding/approval. (raw line 19)
- It recounts an **NPCI notice in November 2025** about a plan to deprecate **UPI Collect** in favor of Intent and QR. Adyen says it will no longer offer Collect for **new merchant integrations** and updated Drop-in/Components at **v6.30.0**. Existing custom Checkout API/UI users of Collect are **strongly recommended** to start offering Intent and/or QR and migrate; that recommendation is distinct from a dated hard shutdown for all existing merchants. (raw lines 21–24)
- The options described are **Intent**, redirecting a shopper to their UPI app on mobile; **QR**, showing a code scanned with the app; and **Collect**, asking for a virtual payment address before the shopper completes payment in the app. The page's table instead labels the overall payment flow **await**, with **IN/INR** and **Direct debit**; do not flatten these option-specific shopper actions into one universal redirect or result behavior. (raw lines 26–36)
- The matrix marks recurring with a check and **“See note”**, but the captured page has no corresponding note or AutoPay/mandate instructions. It marks refunds, partial and multiple partial refunds and chargebacks with checks, while separate, partial and multiple partial captures are X-marked. These marks are historical capability indicators, not independent proof of current eligibility, mandate consent, refund state or payment/capture/settlement outcome. (raw lines 34–36)
- The chooser links Web, iOS, Android, React Native, Flutter and API-only guides, plus Pay by Link. It does not give those child guides' SDK/API versions, deep-link/return handling, TEST/LIVE process or final status procedure. (raw lines 38–80)

## Detail locators

- India entity/integration and regulatory-support pointer: raw line 19.
- November 2025 Collect notice, new-integration restriction, v6.30.0 update and existing-custom recommendation: raw lines 21–24.
- Intent/QR/Collect shopper descriptions and IN/INR capability matrix: raw lines 26–36.
- Channel and API-only/Pay by Link navigation: raw lines 38–80.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/upi/2026-09-15|Adyen UPI overview, 2026-09-15 snapshot]]
