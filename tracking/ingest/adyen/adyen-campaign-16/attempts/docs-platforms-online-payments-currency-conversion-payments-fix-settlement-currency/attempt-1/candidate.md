---
title: "Adyen Platforms: fix the cost of goods in the settlement currency"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/currency-conversion/payments/fix-settlement-currency"
raw_files:
  - "adyen/docs/platforms/online-payments/currency-conversion/payments/fix-settlement-currency/2026-09-15.md"
tags: [adyen, platforms, online-payments, currency-conversion, fx, split-payments]
---

## Overview

This dated Adyen Platforms guide describes a pilot currency-conversion flow for an online payment whose cost of goods is fixed in the platform user's settlement currency. The customer pays a calculated amount in the processing currency, which varies with the prevailing exchange rate and Adyen conversion markup. The guide's CZK 1000.00/PLN 201.74 values and Checkout v72 request are examples, not a current quote, account entitlement, or proof of payment or payout.

## Key takeaways

- Adyen labels currency conversion limited availability and pilot phase and says the process and documentation may change. Contact Adyen for piloting; do not infer general availability from the example (raw lines 19–20).
- Compute the customer-facing processing-currency amount from the fixed settlement-currency goods amount with either Foreign Exchange API `POST /rates/calculate` or the Exchange Rate Report. The FX API calculation uses `type=splitPayment`, settlement `sourceAmount` in minor units, processing `targetCurrency`, and `exchangeSide=buy`; its applied rate includes markup (raw lines 55–91). The report rate also includes markup, so do not add it again or assume reciprocal rates are interchangeable (raw lines 153–205).
- In the guide's payment flow, `amount` is the amount/currency the customer pays and `splits.amount` fixes the amount/currency for the user's settlement balance. For multiple splits their amounts must sum to the cost of goods in settlement currency. A `Remainder` split directs mismatches or miscalculations to its specified balance account; the guide recommends a `PaymentFee` split too (raw lines 216–228, 892). This routing is material to who bears an amount discrepancy; the page does not quantify broader FX risk or establish a default liable account.
- Prerequisites include online payments integration with checkout UI; Checkout API credentials; standard webhooks with transfer or transaction webhook subscription; account-holder `receivePayments`, `receiveFromPlatformPayments`, and `sendToTransferInstrument` capabilities; and merchant-account currency configuration. Foreign Exchange API credentials, Read FX rates role and support enablement apply when using `rates/calculate`; Exchange Rate Report access requires one of Merchant report, Merchant financial or Merchant admin roles (raw lines 26–45). These are documented setup conditions, not proof a particular account is configured.

## Detail locators

- Requirements, credentials, roles, webhooks, capabilities and merchant currency setup: raw lines 26–45.
- FX API request/response field table and illustrative CZK-to-PLN response: raw lines 62–151. The prose table says `exchangeSide=buy`, but the example response displays `sell` at line 136; verify behavior against the current API before relying on that response field.
- Exchange Rate Report configuration, calculation and non-reciprocal markup rates: raw lines 153–214.
- Payment endpoint choices (`/payments`, `/sessions`, captures), required conversion field table, Checkout v72 example and language-library examples: raw lines 216–870. The sample response at lines 871–890 is illustrative.
- Split booking and reconciliation locator: raw line 892.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-currencies-and-fx]]

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/currency-conversion/payments/fix-settlement-currency/2026-09-15|Pinned Adyen Docs snapshot, 2026-09-15]]
