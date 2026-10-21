---
title: "Adyen Marketplace: Split online payments at authorization"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/split-transactions/split-payments-at-authorization"
raw_files:
  - "adyen/docs/marketplaces/split-transactions/split-payments-at-authorization/2026-09-15.md"
tags: [adyen, marketplaces, platforms, online-payments, splits]
---

## Overview

This Marketplace-path online-payments guide (last modified 2023-02-16; captured 2026-09-15) describes putting transaction-specific split instructions in an authorization request when the marketplace processes a customer payment on behalf of a user. The stated booking targets are the user's balance account for a sale, the marketplace's liable balance account for commission and defaults, and selected balance accounts for fees or currency-conversion remainder. Authorization instructions, balance-account booking, later settlement and payout are separate events. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Prerequisites include an online payments integration and checkout UI, Checkout and Transfers API credentials, standard webhook handling plus Transfer or Transaction webhook subscriptions, and account-holder `receiveFromPlatformPayments` in a **valid** state. If that capability is not valid, the guide says funds cannot be allocated to that user's balance account and the full amount is booked to the marketplace liable balance account. See raw lines 21–33.
- Add a `splits` array to Checkout POST `/payments` or `/sessions`. `BalanceAccount` names a user/liable balance-account ID and needs a split `reference`; `Commission` books to the liable balance account without an `account`; `Remainder` defaults there unless directed elsewhere. Unspecified transaction fees book to liable, while a `PaymentFee` split can assign fees to a chosen account. `TopUp` is excluded from `/sessions`. The split table gives conditional currency/value rules, so read the exact row before constructing a payload. See raw lines 36–55 and 1671–1702.
- The illustrative Checkout v72 TEST request is USD 80.00 total, with USD 75.00 `BalanceAccount` sale to a user balance account and USD 5.00 `Commission` to liable; `PaymentFee` has no advance amount because fees are not known at payment time. The sample `resultCode=Authorised` and PSP/merchant references are authorization evidence, not proof that split legs were credited, settled, paid out, or received by a bank. Other language examples include different values, notably a NodeJS EUR 400.00 example, so do not treat every snippet as one matching transaction. See raw lines 57–113, 340–396 and 665–679.
- **Destination fallback:** The request validates split format but not named balance accounts. An absent balance account or one linked to a closed account holder can cause the whole transaction and fees to book to the marketplace liable balance account even if the payment succeeds. The page points to a later internal transfer to correct balances; it does not show one executed. See raw lines 681–685.
- Track each split item separately through Transfer `created/received`, `updated/authorised`, `updated/captured`, and Transaction `created/booked` webhooks. The examples label sale as incoming to user, fee as outgoing from user and commission as incoming to liable. Sample payloads are not a single consistent ledger trace: the fee webhook uses a second user balance account although the authorization example assigns `PaymentFee` to the first; the commission booked transaction shows a negative amount and a user balance-account ID despite the incoming liable-credit prose. Check live event IDs, direction and balances rather than copying those example identities. See raw lines 687–703, 707–1022, 1023–1338 and 1339–1669.
- References for split items support reconciliation; without them, the guide says split amounts aggregate into one entry. Capture-time split instructions override authorization-time instructions. The page recommends authorization-time instructions because some payment methods do not support delayed capture and booking may otherwise be wrong; reserve capture-time changes for amount updates such as partial captures or overcaptures. See raw lines 1704–1708.

## Detail locators

- Prerequisites, valid capability and liable fallback: raw lines 21–33.
- Split fields, types, account ownership and example request/response: raw lines 36–679.
- Invalid/closed destination behavior: raw lines 681–685.
- Per-split Transfer/Transaction webhook lifecycle and example discrepancies: raw lines 687–1669.
- Additional fees, remainder, top-up and reference/capture precedence: raw lines 1671–1708.

## Related

- [[adyen-platforms]] — main concept for Marketplace online splits.
- [[adyen-automatic-split-configuration]] — separate store-profile route; transaction-specific instructions take precedence there.
- [[adyen-platform-internal-transfers]] — later balance-correction route.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/marketplaces/split-transactions/split-payments-at-authorization/2026-09-15|Split payments at authorization, captured 2026-09-15]]
