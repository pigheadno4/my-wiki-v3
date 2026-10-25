---
title: "Adyen Bank Transfer via KCP overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/2026-09-15.md"
tags: [adyen, bank-transfer, kcp, korea, online-banking]
---

## Overview

This [[adyen]] **Bank Transfer via KCP** overview presents a **South Korea (KR), Korean won (KRW)** **Online Banking redirect** method, a historical merchant assurance/escrow statement, a named bank/securities list, a capability matrix and Web/iOS/Android/API-only child routes. It is a 2026-09-15 documentation snapshot. It does not establish current Korean law, a particular merchant's regulatory compliance, KCP enablement, completed fund transfer, delivery confirmation or payment outcome. [[adyen-online-payments]]

## Key takeaways

- **Historical merchant assurance claim:** The page says Korea-registered e-commerce merchants accepting online bank transfer must have **escrow or electronic surety assurance** for shopper protection, and describes shopper money as held by the bank until product delivery is confirmed. It says neither Adyen nor KCP can provide this service and directs obtaining it from a **local Korean bank**. This is the page's dated regulatory claim and provider-role allocation, not verified current legal advice or proof a merchant has obtained the assurance. See raw lines 23–25.
- **Method matrix:** The row labels **Online Banking**, **redirect**, **KR/KRW**. It marks refunds, partial refunds and multiple partial refunds available, while marking recurring, separate/partial/multiple partial captures and chargebacks unavailable. It says nothing about ordinary capture. Matrix marks are historical method-level claims, not completion of a specific refund or transfer. See raw lines 27–29.
- **Bank and integration navigation:** The “Available banks” section lists banks, cooperative/credit institutions and securities/investment names in the captured page; it should not be read as current participant eligibility. The integration chooser links Web, iOS, Android and API-only, with API-only labelled for a custom UI on website or mobile app. Child guides supply actual request, redirect and status conditions. See raw lines 31–96.
- **Link mismatch:** The page's “Read more” link labelled **Bank Transfer via KCP** points to an `adyen.com/payment-methods/korean-cards` URL. That link is not evidence this bank-transfer method is a card product. See raw line 21.

## Detail locators

- Scope, regulatory statement and provider roles: raw lines 15–25.
- KR/KRW matrix and capability marks: raw lines 27–29.
- Historical available-bank/securities list: raw lines 31–70.
- Channel/API-only routes and related navigation: raw lines 72–103.

## Related

- [[adyen-online-payments]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/2026-09-15|Adyen Bank Transfer via KCP snapshot]]
