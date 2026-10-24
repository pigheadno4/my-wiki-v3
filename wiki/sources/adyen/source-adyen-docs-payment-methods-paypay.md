---
title: "Adyen PayPay payment-method overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay"
raw_files:
  - "adyen/docs/payment-methods/paypay/2026-09-15.md"
tags: [adyen, paypay, japan, wallet, redirect]
---

## Overview

This [[adyen]] PayPay overview identifies PayPay as a Japan digital wallet and presents its online-payments flow as **redirect**, with **JP** and **JPY** in the capability table. It is a 2026-09-15 documentation snapshot, not proof of current merchant enablement, PayPay account eligibility or a completed payment. [[adyen-online-payments]]

## Key takeaways

- The table labels the method **Wallets / Redirect / JP / JPY**. It marks recurring, refunds, partial refunds, multiple partial refunds, separate captures and partial captures with checkmarks, while marking multiple partial captures and chargebacks with x symbols. Recurring, multiple partial refunds, separate captures, partial captures and chargebacks have “See note” markers, yet this pinned raw contains no corresponding note text. Treat those marks as overview-level, qualified claims, not an implementation contract or evidence of capture/refund/chargeback outcome. See raw lines 23–27.
- The online integration chooser links **Web**, **iOS**, **Android**, **React Native**, **Flutter** and **API only** guides. The API-only link describes a merchant-built UI for a website or iOS/Android app; these descriptions do not supply child-guide setup, API versions, server return handling or webhook semantics. See raw lines 29–65.
- Separate links point to **Pay by Link** and **in-person PayPay** support, outside the page's online redirect table. The page also links general Online payments, 3D Secure, Capture and Payment methods references. These links establish navigation only. See raw lines 67–84.

## Detail locators

- PayPay identity and capability matrix: raw lines 15–27.
- Channel and API-only guide links: raw lines 29–65.
- Pay by Link, in-person and general references: raw lines 67–84.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/2026-09-15|Adyen PayPay overview snapshot]]
