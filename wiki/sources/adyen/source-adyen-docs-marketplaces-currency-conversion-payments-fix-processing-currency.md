---
title: "Adyen Marketplaces FX payments: fix the processing-currency amount"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/currency-conversion/payments/fix-processing-currency"
raw_files:
  - "adyen/docs/marketplaces/currency-conversion/payments/fix-processing-currency/2026-09-15.md"
tags: [adyen, marketplaces, platforms, online-payments, currency-conversion, foreign-exchange]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Marketplace guide describes a **limited-availability pilot** in [[adyen-currencies-and-fx]]: fix the goods price in the customer's processing currency, calculate the user's variable settlement-currency amount using the Foreign Exchange API, then submit both amounts in Checkout payment or capture splits. The user settlement amount depends on the prevailing rate and Adyen markup. This is a documented request path, not proof of present account eligibility, capture, settlement, actual booking, payout or bank receipt.

## Key takeaways

- The page calls currency conversion a pilot whose processes and documentation may change. It requires an Adyen online-payments integration and checkout UI, separate Checkout API and Balance Platform Foreign Exchange API credentials, the FX **Read FX rates role**, standard webhooks plus Transfer or Transaction webhook subscription, and account-holder capabilities `receivePayments`, `receiveFromPlatformPayments` and `sendToTransferInstrument`. Support must enable the FX API and required merchant-account currencies. These are stated gates, not proof that an account has them. See raw lines 19–42.
- For the fixed customer-paid processing amount, call `POST /rates/calculate` with an `exchangeCalculations` item: `type=splitPayment`, `sourceAmount` containing processing currency and amount, settlement `targetCurrency`, and `exchangeSide=sell`. The response describes `targetAmount` as the user's settlement-currency amount and `appliedExchangeRate` as including Adyen markup. The rate example uses PLN 200.00 and CZK; it is illustrative, not a current quote. See raw lines 44–142.
- The guide names Checkout `POST /payments`, `POST /sessions` and `POST /payments/{paymentPspReference}/captures`. Put the customer-paid processing amount/currency in top-level `amount` and calculated settlement amount/currency in `splits.amount`. For multiple splits, the guide says their total must equal the settlement-currency goods amount; it recommends explicit `Remainder` and `PaymentFee` items. A mismatch or miscalculation goes to the account named in the `Remainder` split, with per-transaction reconciliation in the Balance Platform Accounting Report. See raw lines 144–156 and 820.
- The page says supplied splits are guaranteed, but the separate split-at-authorization guide says an invalid or closed-holder balance-account destination can book the full payment and fees to the platform liable account. Thus the guarantee in this page is not evidence of credit to an arbitrary split destination; check actual split and booking records. The sample Checkout response is only `Authorised`, not proof of capture or settlement. See this raw line 820 and [[source-adyen-docs-platforms-online-payments-split-transactions-split-payments-at-authorization]] (its raw lines 35 and 1413).
- Preserve example discrepancies: the FX field table calls `targetAmount.value` minor units, while the response JSON displays `"1015.31"` and prose says CZK 1015.31; the Checkout field table shows `101531`. The earlier example fixes PLN 200.00 and CZK 1015.31, whereas the versioned test Checkout request uses PLN 201.74 and CZK 1000.00. Verify units and actual request values rather than stitching examples into one transaction. The FX curl names a live Balance Platform endpoint, while Checkout curl uses test `/v72/payments`; SDK versions and TEST environments are examples. See raw lines 69–83, 89–142, 152–156, 160–214 and 216–797.

## Detail locators

- Pilot, fixed processing versus variable settlement premise, credentials, roles, webhook and capability gates: raw lines 19–42.
- FX calculation fields, markup and PLN/CZK response example: raw lines 44–142.
- Checkout endpoint choices, amount and split semantics: raw lines 144–156.
- Test Checkout v72 curl, SDK variants and sample `Authorised` response: raw lines 158–818.
- Remainder booking and accounting report pointer: raw line 820.

## Related

- [[adyen]] — provider profile.
- [[adyen-currencies-and-fx]] — canonical currency and FX concept.
- [[adyen-platforms]] — platform user and balance-account context.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-processing-currency]] — separate Platforms URL with equivalent fixed-processing route.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-settlement-currency]] — opposite fixed-settlement-amount path.
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-payments-at-authorization]] — split-destination validation and liable-account fallback boundary.

## Related raw API references

- The pinned page links to Foreign Exchange API `/rates/calculate`, Checkout payment/session/capture endpoints and the Balance Platform Accounting Report; consult their versioned references independently for current schemas.

## Raw Sources

- [[raw/adyen/docs/marketplaces/currency-conversion/payments/fix-processing-currency/2026-09-15|Marketplace fixed-processing-currency FX payment guide — pinned 2026-09-15 snapshot]]
