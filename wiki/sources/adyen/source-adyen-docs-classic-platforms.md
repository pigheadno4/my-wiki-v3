---
title: "Adyen Classic Platforms integration overview"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms"
raw_files:
  - "adyen/docs/classic-platforms/2026-09-15.md"
tags: [adyen, classic-platforms, marketplaces, sub-merchants]
---

## Overview

This 2023-modified, 2026-09-15-captured page is for **Classic Adyen for Platforms** integrations. It directs teams just starting an implementation to a separate **new integration guide**. In the Classic model described here, a platform onboards sellers, service providers or contractors as sub-merchants/account holders, accepts customer payments on their behalf, can split and transfer funds, pay sub-merchants out, and use reports for reconciliation. This page is a product/workflow overview; it does not define the newer balance-platform API/resource model.

## Key takeaways

- The platform can split each acquired payment among one or more sub-merchants, deduct costs such as commissions or payment fees, and hold funds until payout. It can move funds between the platform's and sub-merchants' accounts, then control or automate sub-merchant payout timing and amount. See raw lines 23–35 and 112–140.
- Onboarding describes business, non-profit and individual sub-merchants, with Adyen-run or platform-combined verification and staggered or upfront approaches. The page's immediate-payment-after-signup statement is an overview claim, not proof that a particular account holder passed verification or may process live payments. See raw lines 96–110.
- The supported-country list is a **dated snapshot** at raw lines 41–92. For point-of-sale processing, the country must also appear on the separate POS supported-country list (raw line 94). Neither list establishes current eligibility.
- Reports are proposed for receivables, transactional ledgers and fees (raw lines 142–152); the page supplies no completed payment, payout or reconciliation evidence.

## Detail locators

- Classic-versus-new integration route and high-level sub-merchant payment flow: [[raw/adyen/docs/classic-platforms/2026-09-15|raw lines 15–39]].
- Dated country list and POS condition: [[raw/adyen/docs/classic-platforms/2026-09-15|raw lines 41–94]].
- Onboarding, split payments, funds transfers, payouts and reports: [[raw/adyen/docs/classic-platforms/2026-09-15|raw lines 96–152]].

## Related

- [[adyen-classic-platforms]] — dedicated Classic integration concept.
- [[adyen-platforms]] — newer Adyen for Platforms model; its API/resource guidance is separate.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/2026-09-15|Classic integration (captured 2026-09-15)]]
