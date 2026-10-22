---
title: "Pay out to bank accounts | Adyen Payout Service"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/2026-09-15.md"
tags: [adyen, payouts, payout-service, bank-accounts, transfers]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] **Payout Service** guide describes Transfers API payouts **from your balance account to a third-party bank account**, such as a freelancer's or provider's account. It is a route, priority, cut-off and statement-text reference, not an executed payout or bank-receipt record. See [[adyen-payouts]] for the payout-family route and [[adyen-financial-products]] for the product-family context. Keep this Transfers API path separate from the legacy Online Payout API. [Raw: lines 11, 15–19]

## Key takeaways

- The guide says third-party payouts are in local currencies, with stated exceptions for EUR in SEPA locations outside the eurozone and USD in Canada. The **same captured page** separately lists a Hong Kong USD wire row and EUR/GBP/USD cross-border routes, so its “two exceptions” sentence is not a complete eligibility rule. Use the country, currency, priority and bank-format tables together and verify a route for the specific counterparty. This snapshot does not prove current availability. [Raw: lines 21–67, 85–93]
- The country tables distinguish regular, instant, fast, wire and cross-border support; cross-border routes additionally specify bank-account identification and account-owner address requirements. Higher priority carries higher fees, and intermediary banks may delay a cross-border payout or leave the beneficiary with less than the instructed amount. The prose calls instant available in Australia, while the Australia support table lists only regular, fast and wire; do not resolve that conflict as current support. [Raw: lines 30–83]
- Adyen recommends calculating transfer routes when building the integration, first paying a location/counterparty, or investigating repeated failures. Route selection depends on priority, currency and counterparty location. Cut-off times, local timezone, settlement delay and minimum/maximum amount vary by table row; after-cut-off processing can shift to a later business day. The SEPA and US examples contain broken/missing words and the US lead-in describes next-day timing while its first example says same-day receipt, so use the row-level table as dated evidence rather than treating illustrative arrival times as a guarantee. [Raw: lines 85–162]
- A supplied statement description is passed to the recipient bank, but most banks, not all, display it. Accepted input length is generally up to 140 characters; visible length and allowed characters vary by country, currency and priority. Some table rows explicitly show **zero bank-statement visibility** even when Adyen accepts a description or beneficiary reference, including PLN regular and SGD wire. [Raw: lines 164–174, 221–228, 336–345]
- Adyen screens each balance-platform transfer for regulatory and risk purposes and recommends including more counterparty information to reduce manual-review and processing-delay risk. The linked child guides own route calculation, the actual payout request and movement webhooks; this page alone does not establish booking, settlement, bank acceptance or beneficiary receipt. [Raw: lines 347–363]

## Detail locators

- Purpose and third-party balance-account-to-bank direction: raw lines 15–19.
- Supported location/currency/priority/format tables and cross-border requirements: raw lines 21–67.
- Priority fees, intermediary-bank risk and route calculation: raw lines 69–93.
- Cut-offs, timezone, settlement delay and amount bands: raw lines 95–162.
- Statement-text acceptance versus visibility matrix: raw lines 164–345.
- Screening and child-guide routes: raw lines 347–363.

## Related

- [[adyen-payouts]] — payout-family route, including legacy API distinction
- [[adyen-financial-products]] — Payout Service product-family context
- [[source-adyen-docs-payouts-payout-service-payout-lifecycle]] — separate request, booking, tracking and return states
- [[source-adyen-docs-payouts-payout-service-getting-paid-transfer-routes]] — route calculation for an actual payout candidate
- [[source-adyen-docs-payouts-payout-service-getting-paid-transfer-statement]] — statement-text matrix in the getting-paid guide

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/2026-09-15|Pinned Payout Service bank-payout guide]]
