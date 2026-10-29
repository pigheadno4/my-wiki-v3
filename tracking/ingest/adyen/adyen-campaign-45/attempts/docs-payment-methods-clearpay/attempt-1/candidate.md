---
title: "Adyen Clearpay payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/clearpay"
raw_files:
  - "adyen/docs/payment-methods/clearpay/2026-09-15.md"
tags: [adyen, clearpay, buy-now-pay-later, redirect, chargebacks]
---

## Overview

This Adyen Docs overview, captured 2026-09-15, presents Clearpay as a buy now, pay later service in the United Kingdom. It describes a four-installment shopper purchase, Clearpay risk checks before approval, and Clearpay taking full fraud risk and paying the merchant up front **if those checks succeed**. Its matrix scopes the listed method to GB/GBP and a redirect flow. This snapshot does not establish current merchant eligibility, a specific shopper's approval, guaranteed settlement, or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The feature matrix marks recurring unavailable; refunds, partial and multiple partial refunds, separate captures, partial and multiple partial captures, and chargebacks available. These are page-level method indicators, not an account entitlement or implementation procedure (pinned raw lines 27–29).
- Regional names are distinct: this page calls the service Cash App Afterpay or $Afterpay in the US and Afterpay in Australia, Canada and New Zealand. Its own GB/GBP Clearpay row should not be extended to those regional products (line 31).
- Shoppers may initiate chargebacks directly with Clearpay up to 120 days after payment, cancellation, or expected receipt. The merchant has 13 days to defend or accept a dispute; no response or acceptance loses the dispute and debits the account. If defended, Clearpay has 30 days to decide (lines 33–37).
- Integration navigation covers Web, iOS, Android, React Native, Flutter, API only, and Pay by Link. The platform guides and API-only route own implementation details (lines 39–81).

## Detail locators

- Four-installment model, conditional risk/merchant-payment statement and GB/GBP feature matrix: pinned raw lines 23–29.
- Regional branding: line 31. Chargeback timings and consequence: lines 33–37.
- Platform and API-only integration routes: lines 39–81; general related links: lines 83–88.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-clearpay-web]] — Web integration route
- [[source-adyen-docs-payment-methods-clearpay-ios]] — iOS integration route
- [[source-adyen-docs-payment-methods-clearpay-android]] — Android integration route
- [[source-adyen-docs-payment-methods-clearpay-api-only]] — merchant-built UI route

## Raw Sources

- [[raw/adyen/docs/payment-methods/clearpay/2026-09-15|Clearpay overview, captured 2026-09-15]]
