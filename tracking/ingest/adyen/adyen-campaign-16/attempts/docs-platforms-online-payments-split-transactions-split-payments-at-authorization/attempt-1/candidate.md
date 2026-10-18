---
title: "Adyen Platforms split online payments at authorization"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/split-transactions/split-payments-at-authorization"
raw_files:
  - "adyen/docs/platforms/online-payments/split-transactions/split-payments-at-authorization/2026-09-15.md"
tags: [adyen, platforms, online-payments, split-payments]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes **split instructions in an online payment authorization request** to allocate a user's sale amount, platform commission, transaction fees and any currency-conversion remainder across platform balance accounts. It is about specifying and tracking a split for payments processed on behalf of platform users; it does not determine the legal seller or merchant of record, prove a particular balance-account booking, capture, payout or bank receipt. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Prerequisites listed are an online-payments integration and checkout UI, Checkout and Transfers API credentials, a server accepting standard plus transfer or transaction webhooks, and account-holder capabilities **receivePayments**, **receiveFromPlatformPayments** and **sendToTransferInstrument**. If **receiveFromPlatformPayments** is not **valid**, funds cannot be allocated to that user's balance account and the page says the **full amount** is booked to the platform's liable balance account. This is a consequential fall-back, not proof the holder is verified or funds arrived.
- Add `splits` to POST `/payments` or `/sessions`. The guide lists a destination/charged **balanceAccountId** (a user's or the platform's liable account), type, amount and **store reference** for the normal store route. Its field table presents `store` among split-item fields while the example places `store` at the request top level; consult the linked Checkout API schema for exact placement rather than treating this page's layout as conclusive. `BalanceAccount` books the user's sale amount; `Commission` books platform commission to its liable account and need not specify `account`; `PaymentFee` can book total fees to a selected account. Unknown fees or an unspecified currency-conversion `Remainder` default to the liable account. `amount.currency` is specifically needed for conversion, `amount.value` is not needed for fees/remainder unknown at payment time, and `reference` is conditionally required for `BalanceAccount`. The `TopUp` type is **not supported in /sessions**.
- The guide's USD 80 example allocates USD 75 sale to a user balance account, USD 5 commission to the liable balance account, and fees via a separate `PaymentFee` item. This is an illustrative **test** request, not a prescribed fee/commission rate, current API-version guarantee or observed booking. Registered payment facilitators **without configured stores** must send additional sub-merchant data instead of assuming the ordinary store-reference path covers them.
- An `Authorised` payment response is not sufficient proof of correct split booking. The request validates split **format**, not destination balance-account existence or status. For a nonexistent balance account or one linked to a **closed** holder, the full transaction and fees are booked to the platform liable account; the guide points to later internal transfer for balance correction. Track each split using transfer-created/updated and transaction-created webhooks; their received, authorised, captured and booked stages are distinct. Fee deductions are outgoing relative to the user's account; sale and commission credits are incoming to their respective user/liable accounts in the examples.
- The page recommends a unique split **reference** for reconciliation; without one, split amounts aggregate in a report entry. If amounts are unknown at payment time, **capture-time** splits can be provided, and they **override authorization-time splits**. Adyen recommends payment-time splits because some methods do not support delayed capture and can otherwise book incorrectly; capture-time instructions are suggested only to change amounts such as partial captures or overcaptures. This page links automatic split configuration but states no precedence rule for that separate route.
- Additional links cover finer transaction-fee types, exchange-rate remainder, chargebacks and top-ups. A `Remainder` is a possible leftover after conversion, not a guaranteed gain or fee. Chargeback allocation and final fee/currency accounting belong to their linked guides; this source supplies navigation and the split-type orientation.

## Detail locators

- Scope, prerequisites, capability fall-back and split fields/types: pinned raw lines 15–58.
- Standard platform example, test environment/API versions and payment-facilitator exception: pinned raw lines 60–1410.
- Invalid/closed destination fall-back and per-split transfer/transaction webhook stages: pinned raw lines 1411–2399.
- Additional fee, remainder, chargeback/top-up routes and authorization-vs-capture precedence: pinned raw lines 2401–2444.

## Related

- [[adyen-platforms]] — provider concept for platform/user and liable balance-account context.
- [[source-adyen-docs-platforms-manage-stores]] — store reference/resource route, separate from successful split execution.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/split-transactions/split-payments-at-authorization/2026-09-15|Adyen split payments at authorization, captured 2026-09-15]]
