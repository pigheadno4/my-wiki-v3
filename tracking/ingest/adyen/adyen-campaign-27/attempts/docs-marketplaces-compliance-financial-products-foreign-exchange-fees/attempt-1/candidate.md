---
title: "Adyen Marketplace financial-product FX fee disclosure examples"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/compliance-financial-products/foreign-exchange-fees"
raw_files:
  - "adyen/docs/marketplaces/compliance-financial-products/foreign-exchange-fees/2026-09-15.md"
tags: [adyen, marketplaces, financial-products, fx, pricing, compliance]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] financial-products compliance-guideline page describes how FX rate and additional fees should be presented for a user transaction involving currency conversion. It says it is not legal advice. Its GBP/USD variable, fixed and third-party-fee tables are presentation examples, not a current tariff, executable quote or proof of funds delivered. See [[adyen-financial-products]] and [[adyen-currencies-and-fx]].

## Key takeaways

- **Disclosure scope:** The page says the user should clearly see the FX rate and additional fees at transaction time and in statements covering the relevant period. It says the examples are based on UK Financial Conduct Authority guidance but applies its guidance to marketplaces in all regions. This is Adyen's dated provider instruction, not a determination of current law or product eligibility in each region. See pinned raw lines 19–23 and 101.
- **Fee illustrations:** The variable example shows £100 paid, 3%/£3 fee, £97 converted at 1.30 GBP/USD and $126.10 received. Fixed-fee examples show fee, payer/converted value, rate and recipient amount; the page says the Adyen exchange rate includes a 3% markup in those examples. None of the values establishes a live rate or charged fee. See pinned raw lines 25–72.
- **Example discrepancy:** The first Fixed Fee table lists 1 GBP to 1.26 USD and a £0 fixed fee, but also £3 total fees added and the recipient as £126.10. The currency and arithmetic do not reconcile with the stated rate and amount, so do not use this row to calculate a quote. The additional fixed-fee examples also use differing `You convert`/`You pay` arrangements; retain their labels rather than blending them into one rule. See pinned raw lines 38–66.
- **Intermediary-fee distinction:** The third-party-fee examples contrast an upfront `Pay all fees?` amount, described by the page as protecting the intended recipient amount, with a route where third-party fees are deducted from the recipient amount. Intermediary banks may deduct charges. These examples do not establish the actual fees charged by a given bank or the beneficiary's final receipt. See pinned raw lines 74–99.

## Detail locators

- Nonlegal-advice scope, FX rate/fee presentation and examples notice: pinned raw lines 15–23.
- Variable and fixed GBP/USD examples, markup statement and inconsistent first fixed table: pinned raw lines 25–72.
- Third-party/intermediary fee examples and provider's all-region wording: pinned raw lines 74–101.

## Related

- [[adyen-financial-products]] — reciprocal financial-product compliance concept.
- [[adyen-currencies-and-fx]] — broader FX context; this source is about presentation examples.
- [[source-adyen-docs-platforms-compliance-financial-products-foreign-exchange-fees]] — same dated guidance under the Platforms path.

## Raw Sources

- [[raw/adyen/docs/marketplaces/compliance-financial-products/foreign-exchange-fees/2026-09-15|Marketplace FX fee presentation guidance, captured 2026-09-15]]
