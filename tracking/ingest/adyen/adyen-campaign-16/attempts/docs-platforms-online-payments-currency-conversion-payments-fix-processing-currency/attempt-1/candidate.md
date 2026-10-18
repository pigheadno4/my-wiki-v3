---
title: "Adyen Platforms FX payments: fix the processing-currency amount"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/currency-conversion/payments/fix-processing-currency"
raw_files:
  - "adyen/docs/platforms/online-payments/currency-conversion/payments/fix-processing-currency/2026-09-15.md"
tags: [adyen, platforms, online-payments, currency-conversion, foreign-exchange]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes a pilot online-payment conversion path when the goods price is fixed in the customer's processing currency. The customer pays that fixed amount; the user's settlement-currency receipt varies with the exchange rate and Adyen conversion markup. The platform calculates a settlement amount with the Foreign Exchange API and supplies both currencies in a Checkout payment or capture request. The page describes a request path, not current account eligibility, actual booking, a guaranteed rate, or merchant-of-record identity. See [[adyen]], [[adyen-platforms]] and [[adyen-currencies-and-fx]].

## Key takeaways

- **Limited availability:** The raw page says currency conversion is in pilot, with processes and documentation subject to change; contact Adyen about piloting. Prerequisites include an online-payments integration and checkout UI; separate Checkout API and Balance Platform Foreign Exchange API credentials; the FX credential's **Read FX rates role**; standard webhooks plus transfer or transaction webhooks; account-holder capabilities `receivePayments`, `receiveFromPlatformPayments`, and `sendToTransferInstrument`; and Support enablement of the FX API and required merchant-account currencies. Listed prerequisites do not show that any particular account currently has them.
- **Calculate the variable user amount:** Send `POST /rates/calculate` with an `exchangeCalculations` item: `type=splitPayment`, `sourceAmount` containing the fixed processing currency and value in minor units, `targetCurrency` as the user's settlement currency, and `exchangeSide=sell`. The response's `targetAmount.value` is the calculated user amount in settlement currency, and `appliedExchangeRate` includes Adyen's markup. Keep customer charge and user receipt distinct; the rate example is illustrative, not a current quote.
- **Submit both currencies:** The guide names Checkout `POST /payments`, `POST /sessions`, or `POST /payments/{paymentPspReference}/captures`. Put the customer-paid processing amount and currency in top-level `amount`, and the calculated settlement amount and currency in `splits.amount`. For multiple splits, the page says the sum of settlement-currency split amounts must equal the calculated goods amount. It recommends explicit `Remainder` and `PaymentFee` split items.
- **Remainder and booking risk:** The guide says mismatches or miscalculations are booked to the balance account specified in the `Remainder` split and can be reconciled per transaction in the Balance Platform Accounting Report. Its statement that supplied splits are guaranteed assumes valid split destinations; the separate [[source-adyen-docs-platforms-online-payments-split-transactions-split-payments-at-authorization]] guide warns that a nonexistent balance account or one tied to a closed holder can instead cause the full transaction and fees to book to the platform's liable balance account. Verify actual outcomes through the relevant records and webhooks.
- **Example and version boundary:** The FX calculator example fixes PLN 200.00 and shows a CZK result. The subsequent Checkout field table cites PLN 200.00/CZK 1015.31, while the test `/v72/payments` and SDK examples use PLN 201.74/CZK 1000.00. Treat these as distinct illustrative numbers, not one arithmetically consistent live transaction. The response sample says `Authorised`; it alone does not prove final user credit or reconciliation. The page's code samples are versioned (Java 33.0.0, PHP 24.0.0, .NET 27.0.0, Node 23.3.0, Go 16.3.0, Python 13.3.0, Ruby 10.1.1) and mostly target test Checkout; the FX curl example names a live Balance Platform endpoint.

## Detail locators

- Pilot and fixed-processing versus variable-settlement premise: raw lines 15–24. Requirements, credential identities, role, webhooks, capabilities and Support setup: lines 26–42. Flow: lines 44–50.
- `/rates/calculate` request fields and response semantics: lines 52–83; illustrative PLN/CZK rate calculation: lines 87–142.
- Checkout endpoints, amount/split fields, split-sum and remainder rule: lines 144–156; test v72 curl and versioned SDK examples: lines 158–797; illustrative `Authorised` response and accounting-report pointer: lines 799–820.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform user and balance-account context.
- [[adyen-currencies-and-fx]] — provider FX and currency context.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-settlement-currency]] — opposite fixed-settlement-amount path; compare its separately pinned source.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-refunds-your-user]] — separate FX refund path.
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-payments-at-authorization]] — general split destination, liable-account fallback and webhook context.

## Related raw API references

- The raw page links to the Foreign Exchange API rate calculator, Checkout payment/session/capture endpoints, and Balance Platform Accounting Report. Consult those references independently for current schemas and operating conditions.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/currency-conversion/payments/fix-processing-currency/2026-09-15|Adyen Docs: Fix the cost of goods in the processing currency (2026-09-15 snapshot; pilot)]]
