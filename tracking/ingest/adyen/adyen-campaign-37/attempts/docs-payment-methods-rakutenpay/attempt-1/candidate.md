---
title: "Adyen Rakuten Pay overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/2026-09-15.md"
tags: [adyen, rakutenpay, japan, wallets, online-payments]
---

## Overview

This [[adyen]] overview identifies Rakuten Pay as a Japan digital wallet, describes a desktop/mobile website redirect and return, gives a JP/JPY wallet capability row, and links integration channels. See [[adyen-online-payments]]. The 2026-09-15 snapshot is not evidence of current merchant availability, successful authorization, capture or settlement.

## Key takeaways

- The page says desktop and mobile shoppers are redirected to the **Rakuten Pay website** and then back to the merchant page; it also says the method is available for **Ecommerce and IPP**. It does not define IPP or state that shopper return establishes payment finality. See raw line 19.
- The matrix labels the method **Wallets**, **Redirect**, **JP** and **JPY**. It marks recurring, refunds (including partial and multiple partial), separate captures, partial captures and chargebacks positively; **multiple partial captures** is marked unavailable. Most positive marks carry a **“See note”** qualifier, but this pinned overview contains no explanatory note, so their precise conditions are unresolved here. These marks are historical capability indicators, not proof of merchant enablement, transaction execution or a completed refund/chargeback. See raw lines 21–23 and full raw through line 80.
- The page offers navigation to **Web, iOS, Android, React Native, Flutter and API-only** guides, plus Pay by Link and in-person pages. These links do not supply child SDK/API versions, merchant prerequisites, authentication/return details or current support. See raw lines 25–73.
- The See also links point to general online payments, 3D Secure, capture and payment-method pages. A 3D Secure or capture link here does not state that those features are required for a specific Rakuten Pay transaction. See raw lines 75–80.

## Detail locators

- **Method identity, redirect/return and Ecommerce/IPP claim:** raw line 19.
- **JP/JPY capability matrix and unresolved “See note” markers:** raw lines 21–23.
- **Channel and API-only routes:** raw lines 25–73.
- **General See also links:** raw lines 75–80.

## Related

- [[adyen-online-payments]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/rakutenpay/web/2026-09-15|Rakuten Pay Web chooser]] — linked channel route; child behavior separate.
- [[raw/adyen/docs/payment-methods/rakutenpay/ios/2026-09-15|Rakuten Pay iOS chooser]] — linked channel route; child behavior separate.
- [[raw/adyen/docs/payment-methods/rakutenpay/android/2026-09-15|Rakuten Pay Android chooser]] — linked channel route; child behavior separate.
- [[raw/adyen/docs/payment-methods/rakutenpay/api-only/2026-09-15|Rakuten Pay API-only guide]] — linked merchant-built-UI route; request and outcome details separate.

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/2026-09-15|Rakuten Pay overview — captured 2026-09-15]]
