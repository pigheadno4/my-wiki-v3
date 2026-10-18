---
title: "Adyen Platforms FX refunds: book the remainder to the user"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/currency-conversion/refunds/your-user"
raw_files:
  - "adyen/docs/platforms/online-payments/currency-conversion/refunds/your-user/2026-09-15.md"
tags: [adyen, platforms, online-payments, refunds, foreign-exchange]
---

## Overview

This 2026-09-15 Adyen Platforms page describes a limited-availability pilot for currency-converted online-payment refunds where the platform chooses to book the FX remainder to its user's balance account. The shopper's refund is fixed in the processing currency originally paid, while the user's debit is in the settlement currency and may differ from the amount originally credited. This is an allocation and request guide, not evidence of current pilot access, an executed refund, shopper receipt or merchant-of-record identity. See [[adyen]], [[adyen-platforms]] and [[adyen-currencies-and-fx]].

## Key takeaways

- The page says currency conversion is in pilot and processes or documentation may change; contact Adyen about participation. Its scenario has the customer pay in processing currency (illustratively PLN) and the user's balance account credited in settlement currency (illustratively CZK). Booking the remainder to the user keeps the shopper-side refund at the original processing-currency amount, while the user bears the changed settlement-currency debit. The page's amounts and rate are examples, not a live quotation or guaranteed rate.
- Prerequisites are an Adyen online-payments integration with checkout UI, Checkout API credentials, standard/transfer/transaction webhook handling, account-holder capabilities `receivePayments`, `receiveFromPlatformPayments` and `sendToTransferInstrument`, Support configuration of required merchant-account currencies, and a captured payment before initiating a refund. Option 2 additionally needs the Balance Platform Foreign Exchange API credential, **Read FX rates role**, and Support enablement of the FX API for the merchant account. Listed capability requirements do not prove an account holder has them enabled.
- Option 1 reuses original payment values in the Checkout refund: `amount` holds the processing currency and original customer-paid value, while `splits.amount` holds the original settlement-currency value. Add a `Remainder` split specifying the user's balance account without a remainder amount. The guide says Adyen then books any conversion remainder to that account. The example uses PLN 201.74 at the top level and CZK 1000.00 in the user split; these are separate currency amounts, not interchangeable units.
- Option 2 first calls `POST /rates/calculate` with `type=splitRefund`, processing-currency `sourceAmount` in minor units, settlement `targetCurrency`, and `exchangeSide=sell`. The returned settlement-currency `targetAmount.value` is the proposed user refund debit; `appliedExchangeRate` includes Adyen's Markup. Then send a Checkout refund with the original processing-currency amount and adjusted settlement-currency split amount. For multiple splits, their settlement-currency sum should equal that adjusted amount; the guide recommends a `Remainder` split to assign any mismatch or miscalculation to the specified balance account. The rate response is calculation guidance, not proof that the eventual refund settled at the example rate.
- The guide's statement that the supplied splits are guaranteed must be read with its setup and account conditions; the separate [[source-adyen-docs-platforms-online-payments-split-transactions-split-refunds]] guide warns that Checkout validates split format rather than balance-account existence and may book an invalid or closed-holder target to the platform's liable balance. The page does not give a distinct partial-refund procedure or state that every payment method supports partial refunds. It shows test Checkout v72 and versioned SDK examples; `status: received` in its example response is not final refund or shopper-receipt proof.

## Detail locators

- Pilot warning, remainder example and processing-versus-settlement effects: raw lines 15–37. Requirements, distinct API credentials/role, capabilities, currency enablement and captured-payment condition: lines 39–57. Common flow: lines 59–67.
- Option 1 original amounts and explicit no-amount `Remainder` split: lines 69–76; test request/SDK examples and response: lines 80–545. Option 2 FX calculation request and response fields: lines 546–581; illustrative calculation/rate: lines 585–643; Checkout fields, split-sum and mismatch routing: lines 645–661; test request/SDK examples and `received` response: lines 665–1129.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform user and balance-account context.
- [[adyen-currencies-and-fx]] — provider FX and amount-unit context.
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-refunds]] — refund split-booking and invalid-account fallback; distinct from this FX pilot procedure.

## Related raw API references

- The raw page links to the Foreign Exchange API rate calculator, Checkout refund endpoint and Balance Platform Accounting Report. Consult those independently for current API schema, availability and reconciliation semantics.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/currency-conversion/refunds/your-user/2026-09-15|Adyen Docs: Book the remainder to your user (2026-09-15 snapshot; limited availability)]]
