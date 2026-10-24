---
title: "Adyen DANA overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana"
raw_files:
  - "adyen/docs/payment-methods/dana/2026-09-15.md"
tags: [adyen, dana, indonesia, wallets, online-payments]
---

## Overview

This [[adyen]] overview describes DANA as an Indonesian digital wallet and summarizes its shopper redirect, country/currency matrix, amount floor and integration routes. See [[adyen-online-payments]]. It is a 2026-09-15 documentation snapshot, not evidence of current merchant enablement, a particular transaction result or settlement. See raw lines 15–91.

## Key takeaways

- The page says a shopper signs up for DANA with a mobile number and six-digit PIN and may fund the DANA account by bank transfer or cash deposit. In the described checkout journey the shopper selects DANA, is redirected to the DANA website, logs in with a mobile number, authenticates using the PIN, confirms, sees a result on DANA, and is redirected back to the merchant website/app. These are shopper/provider steps; this overview does not state that the redirect back alone proves final merchant-side authorization or settlement. See raw lines 23–33.
- The redirect page is valid for **five minutes by default** after the shopper is sent to DANA, then times out. This is the page lifetime, not a universal payment-finalization time or a retry guarantee. See raw line 35.
- The matrix labels DANA `Wallets` with `redirect` flow, country **ID** and currency **IDR**. It marks recurring, refunds, partial refunds and multiple partial refunds available; separate captures, partial captures, multiple partial captures and chargebacks unavailable in this snapshot. The recurring mark is a capability pointer, not a token/consent procedure; the refund marks are not evidence that a specific refund executed. See raw lines 37–39.
- DANA must be at least **300 IDR**; below that amount, the page says the method does **not appear** as available. The condition is about method presentation, not proof that an amount at or above the floor guarantees eligibility, approval or payment success. See raw line 41.
- The page routes to Web, iOS, Android, React Native, Flutter and API-only implementations, plus Pay by Link and in-person references. These are navigation, not child SDK/API version requirements, redirect/callback/webhook mechanics or current support confirmation. See raw lines 43–91.

## Detail locators

- **Wallet context and shopper redirect/PIN journey:** raw lines 23–33.
- **Default redirect page expiry:** raw line 35.
- **Country/currency and capability matrix:** raw lines 37–39.
- **300-IDR method-display floor:** raw line 41.
- **Channel and integration-child routes:** raw lines 43–91.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/dana/web/2026-09-15|DANA Web chooser]] — linked channel route; child behavior separate.
- [[raw/adyen/docs/payment-methods/dana/ios/2026-09-15|DANA iOS chooser]] — linked channel route; child behavior separate.
- [[raw/adyen/docs/payment-methods/dana/android/2026-09-15|DANA Android chooser]] — linked channel route; child behavior separate.
- [[raw/adyen/docs/payment-methods/dana/api-only/2026-09-15|DANA API-only guide]] — linked merchant-built-UI route; request and outcome details separate.

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/2026-09-15|DANA overview — captured 2026-09-15]]
