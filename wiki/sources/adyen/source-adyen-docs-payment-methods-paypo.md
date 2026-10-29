---
title: "PayPo payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo"
raw_files:
  - "adyen/docs/payment-methods/paypo/2026-09-15.md"
tags: [adyen, paypo, buy-now-pay-later, poland]
---

## Overview

This PayPo payment-method overview, last modified and captured 2026-09-15, describes a Polish buy now, pay later method, its overview capability matrix, and integration chooser. It is a dated documentation snapshot, not evidence of current availability, merchant-account enablement, shopper approval, or a successful live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page says shoppers can pay within **30 days** or split a payment into up to **6 installments**. Its “most popular” and “over a million active users” language is a dated source claim, not a current market measurement (raw line 23).
- The overview matrix identifies a **Buy Now Pay Later**, **redirect** flow for **PL/PLN**. It marks recurring and chargebacks with crosses; refunds, partial refunds, multiple partial refunds, and **separate captures** with checks; and partial captures and multiple partial captures with crosses. These are the page's capability marks, not a promise of merchant eligibility or a completed operation. In particular, a check for separate captures does not imply partial-capture support (raw lines 25–27).
- The chooser routes pre-built UI solutions for Web, iOS, Android, React Native, and Flutter, plus an API-only route for merchants building their own website, iOS, or Android UI. These are navigation choices; this overview does not supply a complete integration recipe (raw lines 29–65).
- The “See also” 3D Secure link is general navigation and does not establish a PayPo-specific 3D Secure capability (raw lines 67–72).

## Detail locators

- Method description and shopper timing: raw `# PayPo` lines 15–23.
- Geography, currency, redirect flow, and lifecycle capability marks: raw lines 25–27.
- Platform/UI integration chooser: raw `## How do you want to integrate?` lines 29–65.
- General “See also” navigation: raw lines 67–72.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/2026-09-15|PayPo method overview, captured 2026-09-15]]
