---
title: "Adyen Alipay+ overview"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay-plus"
raw_files:
  - "adyen/docs/payment-methods/alipay-plus/2026-09-15.md"
tags: [adyen, alipay-plus, wallets, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen overview presents Alipay+ as a cross-border digital-payment network connecting merchants to multiple local wallets through one integration. It describes a “wallet of wallets” analogy, where underlying wallets are likened to issuers, and lists online browser and mobile-app flows. This network description does not establish identical wallet eligibility or capabilities for each merchant. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page names 11 included wallets: Alipay, AlipayHK, DANA, Kakao Pay, K Plus, NAVER Pay, Touch 'n Go eWallet, Toss, TrueMoney, GCash, and Rabbit LINE Pay. Its summary table labels the payment type “Wallets,” flow “redirect,” countries “International,” and currencies “Multiple”; it does not give wallet-by-wallet country or currency eligibility.
- In the summary table, recurring, separate captures, partial captures, multiple partial captures, and chargebacks carry `x` marks. Refunds, partial refunds, and multiple partial refunds carry checkmarks. These are dated, overview-level marks; the table does not state ordinary-capture behavior, individual-wallet differences, merchant enablement, or a completed financial operation.
- An onboarding request goes to all wallets for separate review under each wallet's own risk requirements. The page describes an *expected* SLA for all wallets to be onboarded within one month, not an approval guarantee. TrueMoney has an additional form completed by Adyen Support and submitted to Alipay+ on the merchant's behalf.
- Navigation links lead to Web, iOS, Android, and Pay by Link routes. Their presence is not implementation guidance or proof of current channel availability.

## Detail locators

- Network definition, “wallet of wallets” analogy, and 11-wallet claim: pinned raw lines 23–27; summary capability table: lines 29–31.
- Wallet list: lines 33–47; onboarding and TrueMoney exception: lines 49–53.
- Channel navigation and “See also” links: lines 55–86.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay-plus/2026-09-15|Alipay+ overview, 2026-09-15]]
