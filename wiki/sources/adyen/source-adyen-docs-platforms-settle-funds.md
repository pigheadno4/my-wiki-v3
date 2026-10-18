---
title: "Adyen Platforms sales-day fund settlement"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/settle-funds"
raw_files:
  - "adyen/docs/platforms/settle-funds/2026-09-15.md"
tags: [adyen, platforms, settlement, balance-accounts, payouts]
---

## Overview

This 2026-09-15 Adyen for Platforms page describes when processed user transactions become settled balance-account funds. Adyen routes payment proceeds through a merchant account, applies the configured split between user and platform balance accounts, groups captures by sales day, and settles net batches after a settlement delay. Settlement makes funds available on balance accounts for a later managed or custom payout path; it is a different event from initiating a bank transfer or receiving funds at a beneficiary bank.

## Key takeaways

- The sales-day model groups funds captured within a 24-hour sales day into related settlement batches and settles them after that day ends. By default, the sales day uses the balance account's local timezone, midnight to the following 23:59; the closing time can be configured later for businesses closing after midnight. Settlement timing is described as independent of when schemes or payment methods transfer funds to Adyen.
- Net settlement deducts transaction costs, refunds, chargebacks, settlement reversals and other adjustments such as balance transfers from user sales. Adjustments are included when they occur, so the current settlement batch can contain an adjustment related to an earlier sales day. Do not treat a settlement batch as gross sales or as a one-to-one payment receipt.
- The default settlement delay is set by contract and varies by region and payment method. Managed payouts optimize that delay against the contract's estimated time of arrival. Custom payouts can override the default with a business-day delay that governs when a batch becomes available for scheduled or on-demand payout requests. Adyen says it settles available funds on working days excluding bank holidays; the dated tables illustrate time, closing-time, and holiday effects, not a guaranteed bank receipt.
- The pass-through settlement model is deprecated for new integrations, with stated exceptions for Affirm and `maestro_USA`; those variants settle on their payment-method schedule rather than the sales-day close. This page does not establish eligibility for those exceptions. If Adyen has not received a captured payment's funds within 30 days, it subtracts them from the current settlement batch as a reversed settlement. This is a consequential reduction of the available batch, distinct from a shopper refund.
- The page does not show transaction-specific settlement webhooks, payout booking, bank transfer status, legal ownership, or beneficiary bank credit. Follow the linked closing-time and custom-delay guides for configuration and the payout/transfer sources for later stages.

## Detail locators

- `# Settle funds` and `## Requirements`: merchant-to-balance-account framing and deprecated pass-through exceptions.
- `## Sales day settlement` and `## How fund settlement works`: local sales-day boundary, capture batching, delay, and net settlement.
- `## Settlement calculation`: deductions and cross-sales-day adjustments.
- `## Settlement delay`: contract default, managed ETA versus custom override, business days/holidays and illustrative tables.
- `## Settlement reversal`: 30-day non-receipt subtraction from current batch.

## Related

- [[adyen-platforms]] — main Platforms concept and source route.
- [[source-adyen-docs-platforms-custom-payouts]] — later custom bank-transfer request path.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/settle-funds/2026-09-15|Adyen settle funds (fetched 2026-09-15)]]
