---
title: "Adyen Marketplace-path sales-day fund settlement"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/settle-funds"
raw_files:
  - "adyen/docs/marketplaces/settle-funds/2026-09-15.md"
tags: [adyen, marketplaces, platforms, settlement, balance-accounts, payouts]
---

## Overview

This Marketplace-path guide explains when payment funds become available in user and platform balance accounts. Adyen describes processing user transactions through a merchant account, splitting the funds and settling them into the corresponding balance accounts. Sales-day batches use captured funds and net adjustments; balance-account settlement is separate from a subsequent payout to a bank. See [[adyen]] and [[adyen-platforms]] for provider and modern balance-platform context. The page is a dated timing model, not evidence of a particular capture, settled balance or bank receipt.

## Key takeaways

- The normal sales-day model batches funds captured during a 24-hour sales day, by default 00:00–23:59 in the balance account's local time zone. A later sales-day closing time can be configured. The batches settle after the sales day according to settlement-delay days, independently of when schemes or payment methods transfer their funds to Adyen. The page's Monday-to-Wednesday two-business-day example is illustrative, not a promise for every account or holiday.
- Settlement is net: transaction costs, refunds, chargebacks, settlement reversals and other adjustments such as balance transfers reduce the user's sales amount. Adjustments enter as they occur, so a current batch can contain items related to a different sales day. Do not equate a capture amount with an eventual available balance or payout amount.
- The default delay is contractual and varies by region and payment method. Managed payouts use an Adyen-optimized delay aligned with the contractual estimated arrival time; custom payouts can override the default waiting period with a custom delay before funds become available to scheduled or on-demand requests. The examples depend on sales-day cutoff, business days and bank holidays. Adyen says it settles available funds on working days, excluding bank holidays. The example table contains timing shorthand and one final five-day row without a time zone; use contract and account-specific settings rather than deriving a universal timestamp.
- Pass-through settlement is deprecated and unavailable for new integrations **except** listed payment methods/variants: Afterpay, `alipay_sg_pos`, Clearpay, `maestro_USA`, and PayPal. Their funds follow the payment-method schedule rather than sales-day closing time. This exception does not reinstate pass-through for other methods.
- If Adyen has not received funds within 30 days after capture, it subtracts them from the current settlement batch as a settlement reversal. A balance credit or earlier batch estimate therefore does not prove the funds will remain available, or that a later bank payout succeeds.

## Detail locators

- Merchant-account-to-split-balance path and pass-through deprecation/method exceptions: raw lines 15–31. Sales-day definition, captured batch and net calculation: lines 33–59.
- Contractual delay, managed versus custom treatment, business-day and holiday examples: lines 61–93. Thirty-day reversal: lines 95–97. Closing-time and custom-delay child routes: lines 99–107.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — modern balance-platform and Marketplace model.
- [[source-adyen-docs-platforms-settle-funds]] — separately pinned Platforms-path settlement guide.
- [[source-adyen-docs-platforms-settle-funds-pass-through-settlement]] — separate deprecated method-schedule model.
- [[source-adyen-docs-platforms-settle-funds-configure-closing-time]] — balance-account closing-time configuration.

## Related raw API references

- The raw page links to Marketplace payment flow, managed/custom payout and observed-bank-holiday references; current account settings and holiday dates need their own authority.

## Raw Sources

- [[raw/adyen/docs/marketplaces/settle-funds/2026-09-15|Adyen Docs: Settle funds (2026-09-15 snapshot)]]
