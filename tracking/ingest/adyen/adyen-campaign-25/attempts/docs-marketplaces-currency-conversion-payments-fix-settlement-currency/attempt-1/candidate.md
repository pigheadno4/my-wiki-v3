---
title: "Adyen Marketplaces: Fixed settlement-currency cost of goods"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/currency-conversion/payments/fix-settlement-currency"
raw_files:
  - "adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15.md"
tags: [adyen, marketplaces, platforms, currency-conversion, online-payments]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Marketplaces guide describes a **limited-availability pilot** for an online payment whose goods cost is fixed in the user's **settlement currency**. The customer's amount in the **processing currency** is calculated from the exchange rate including Adyen's conversion markup; the illustrative fixed **CZK 1000.00** settlement amount corresponds to **PLN 201.74** customer payment in the example. This snapshot is not evidence of current availability, a live FX quote, completed payment, booked split or bank payout. [[adyen-currencies-and-fx]] [[adyen-platforms]]

## Setup and calculation routes

- The page requires an online payments integration with checkout UI, Checkout API credentials, a server accepting standard webhooks and subscription to any of Transfer or Transaction webhooks, account-holder `receivePayments`, `receiveFromPlatformPayments` and `sendToTransferInstrument` capabilities, and merchant-account configuration of the required currencies. For the **Foreign Exchange API `/rates/calculate` route only**, it additionally lists an FX credential, **Read FX rates** role and Support enablement. The **Exchange Rate Report route** requires one of Merchant report, Merchant financial or Merchant admin Customer Area roles. These are documented prerequisites, not account entitlement proof. See [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15|raw lines 19–45]].
- The FX API path sets `type=splitPayment`, `sourceAmount` to the fixed **settlement** currency/value in minor units, `targetCurrency` to the customer's **processing** currency, and `exchangeSide=buy`. The response table says `targetAmount` is the processing-currency charge and the applied rate includes markup. In the CZK→PLN illustration, the request asks to buy but the sample response says `exchangeSide=sell`; the curl sample also omits a comma between `sourceAmount.currency` and `value`. Do not use that sample as a verified executable request/response pair or infer the actual API's side behavior from it. See [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15|raw lines 62–151]].
- The alternate Exchange Rate Report path configures **Exchange rate (platform Settlement)** and calculates processing cost as fixed settlement cost × the settlement-to-processing rate. Reported rates already include markup and reciprocal directions are not interchangeable; the CZK 1000 × 0.20174 = PLN 201.74 calculation is illustrative, not a guaranteed rate for a later payment. See [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15|raw lines 153–214]].

## Payment splits and outcome boundary

- The guide names Checkout POST `/payments`, `/sessions` or `/payments/{paymentPspReference}/captures` routes. Its conversion field table makes `amount.value/currency` the customer's processing-currency amount and `splits.amount.value/currency` the user's fixed settlement-currency goods amount. For multiple splits, their settlement-currency values must sum to the goods cost; mismatches/miscalculations go to the balance account named in a `Remainder` split. It recommends `Remainder` and transaction-fee split items; the example names **the same illustrated balance account** for `BalanceAccount`, `Remainder` and `PaymentFee`, which is an example allocation, not a default liable-account rule. See [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15|raw lines 216–228, 230–291]].
- The Checkout v72 test sample submits **PLN 20174** in `amount` and **CZK 100000** in the BalanceAccount split. Its illustrative response shows `resultCode=Authorised`. The closing prose says splits are guaranteed and payment is booked according to the array, with remainder discrepancies reconcilable in the Balance Platform Accounting Report; that prose does not turn the example authorization response into independently observed booking, settlement, payout or beneficiary receipt. See [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15|raw lines 230–291, 871–892]].

## Detail locators

- Pilot notice, fixed-settlement model and conditional credential/capability setup: [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15|raw lines 15–54]].
- FX API calculation and inconsistent example; Exchange Rate Report formula: [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15|raw lines 55–214]].
- Payment/capture route, split fields, Checkout v72 and dated SDK samples, illustrative authorization/reconciliation: [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15|raw lines 216–892]].

## Related

- [[adyen-currencies-and-fx]] — main currency and FX concept.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-settlement-currency]] — related Platforms-path guide.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-settlement-currency/2026-09-15|Marketplace fixed settlement-currency goods amount (captured 2026-09-15)]]
