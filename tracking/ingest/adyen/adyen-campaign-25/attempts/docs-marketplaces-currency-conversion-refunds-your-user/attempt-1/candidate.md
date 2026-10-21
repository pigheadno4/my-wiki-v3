---
title: "Book an FX refund remainder to a marketplace user"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/currency-conversion/refunds/your-user"
raw_files:
  - "adyen/docs/marketplaces/currency-conversion/refunds/your-user/2026-09-15.md"
tags: [adyen, marketplaces, currency-conversion, refunds]
---

## Overview

This pinned Marketplace guide describes refunding a captured, currency-converted online payment while booking the exchange-rate remainder to the **user's balance account**. The customer paid in the processing currency; the user received the payment in the settlement currency. On refund, the customer's processing-currency amount stays fixed, while the user's settlement-currency debit can differ from the original credit. This is a **limited-availability pilot** in the captured page, whose processes may change; current availability needs confirmation with Adyen. See [[adyen]] and [[adyen-currencies-and-fx]].

## Key takeaways

- The example customer paid **PLN 201.74**, while the user sold goods for and received **CZK 1000.00**. A refund can leave a currency-conversion remainder. Booking it to the user means crediting the customer the original PLN amount and debiting the user for the original settlement amount plus the remainder; the guide gives a **CZK 32.31** additional user debit in its adjusted-amount example (raw lines 24–37, 585–643).
- Prerequisites include an online payments integration and Checkout UI, Checkout API credentials, standard webhooks plus transfer or transaction webhooks, the listed account-holder capabilities, configured merchant currencies, and a **captured** payment before refund. Option 2 also needs Foreign Exchange API credentials, **Read FX rates role**, and Support enablement for the merchant account (raw lines 39–57).
- **Option 1:** POST `/payments/{paymentPspReference}/refunds` using the original processing-currency `amount` and original settlement-currency `splits.amount`. Add a `Remainder` split directed to the user's balance account, without specifying the remainder amount. In the example those are PLN 201.74 and CZK 1000.00 respectively (raw lines 69–76, 80–117).
- **Option 2:** Ask the Foreign Exchange API `/rates/calculate` for `splitRefund` with source processing-currency refund amount, settlement target currency, and `exchangeSide: sell`. Use its `targetAmount` as the adjusted settlement-currency `splits.amount` in the Checkout refund, and route any mismatch with a `Remainder` split to the user's balance account. The example's adjusted user debit is **CZK 1032.31** for the fixed **PLN 201.74** customer credit (raw lines 546–661).
- The guide says split amounts are guaranteed and mismatches or miscalculations go to the named `Remainder` balance account; it points to the Balance Platform Accounting Report for reconciliation (raw line 661). The example Checkout response has `status: received`; receipt of a refund request is not evidence of completed customer credit, final booking, settlement, or payout (raw lines 510–544, 1095–1129).
- The sample `/rates/calculate` curl has a missing comma between `sourceAmount.currency` and `value` (raw lines 607–611). Treat it as an illustrative example, not a copyable JSON request. Other language samples are TEST examples, while that FX curl uses a live endpoint (raw lines 86–117, 599–617); choose the actual authorized environment and current API contract before implementation.

## Detail locators

- Pilot warning, money direction, requirements, and two options: raw lines 15–76.
- Original-amount refund request and `received` response: raw lines 80–544.
- Rate calculation parameters, adjusted amount, refund splits and `received` response: raw lines 546–1129.

## Related

- [[adyen]]
- [[adyen-currencies-and-fx]]
- [[adyen-platforms]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/currency-conversion/refunds/your-user/2026-09-15|Pinned FX refund guide]]
