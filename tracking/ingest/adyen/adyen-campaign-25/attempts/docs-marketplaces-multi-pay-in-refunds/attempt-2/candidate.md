---
title: "Refund third-party multi pay-in payments in Adyen Marketplaces"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/multi-pay-in/refunds"
raw_files:
  - "adyen/docs/marketplaces/multi-pay-in/refunds/2026-09-15.md"
tags: [adyen, marketplaces, platforms, multi-pay-in, refunds, split-payments]
---

## Overview

This 2026-09-15 Marketplace-path guide covers refunds of payments processed by a third-party pay-in provider but settled into a marketplace user's Adyen balance account. The marketplace initiates a Checkout API refund that deducts funds from user and/or platform balance accounts and returns funds to the multi pay-in account. The pay-in partner is separately responsible for sending the money to the user's customer; the page says to establish that partner-side process before initiating at Adyen. An Adyen refund request or booked balance movement does not prove the customer received the refund. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Use the original payment PSP reference from the API response or authorization/transfer webhooks in POST `/payments/{paymentPspReference}/refunds`. The request specifies `amount` and `merchantAccount`; `amount.value` equals the captured amount for a full refund or is less for a partial one, while `amount.currency` matches the authorization currency. The outcome arrives asynchronously through a `REFUND` webhook. See raw lines 23-39 and 779.
- Refund `splits` can specify deductions from user or platform balance accounts. The field table marks `account`, `amount.value` and `type` Required for each split item, with `reference` required for `BalanceAccount`; it also covers commission, Adyen-fee and remainder types and conditional split `amount.currency` for a different deduction currency. However, the TEST curl example's `Commission` split omits `account`, while its `BalanceAccount` split includes `account` and `reference`. The table/example conflict is unresolved; do not treat the example as proof of the table's per-item requiredness or as a validated request. The guide strongly recommends explicit splits for partial refunds. See raw lines 39, 43-60 and 67-96.
- The no-`splits` example is framed for a **full** refund equal to the original payment amount when the authorization included split instructions: it reuses the authorization ratio, **not** capture instructions. If authorization had no splits, the full amount is debited from the marketplace's liable balance account. Do not generalize that example to partial refunds. See raw lines 501-511.
- The API validates split format but **not** the named balance accounts. A nonexistent balance account or one whose account holder is closed causes the full transaction and fees to book to the marketplace's liable balance account, even when the transaction appears successful. Correcting balances requires a separate internal transfer. See raw lines 781-785.
- Track the `REFUND` request outcome separately from transfer and transaction webhooks. The examples depict outgoing refund deductions from the user's account and the platform's liable commission account, followed by an incoming `internalTransfer` credit to the multi pay-in account; `received` and `authorised` are intermediate statuses, while `refunded`/`booked` and transaction-created events document the respective balance postings. No such leg proves the pay-in partner refunded the customer. See raw lines 787-813, 969-971, 1100-1118, 1412-1424 and 1666-1702.
- API v72 and library snippets use TEST examples. Their amounts and identities are illustrative and inconsistent across sections: the request example refunds USD 8,000 minor units (raw lines 67-96), while the later user-deduction and multi pay-in webhook examples show USD 39,600 and 40,000 (raw lines 833-835 and 1444-1446); the booked incoming-transfer section repeats a `received` description (raw lines 1569-1572). Do not join those samples as one reconciled ledger or infer a live outcome.

## Detail locators

- Opening and `## Refund a payment`, raw lines 15-41: third-party versus Adyen/partner roles, original PSP reference, required request fields, captured-amount and authorization-currency constraints.
- `### Tab: Refund with split instructions (recommended)`, raw lines 43-499: split field matrix, fee/commission types and TEST API v72/library examples.
- `### Tab: Use split instructions from payment authorization`, raw lines 501-778: full-refund conditions, authorization-versus-capture ratio and liable-account fallback.
- `### Troubleshooting`, raw lines 781-785: format-only validation, invalid destination fallback and separate internal correction.
- `## Track fund movements`, raw lines 787-1702: three example legs, transfer and transaction webhook statuses, and differing example values/identities.

## Related

- [[adyen-platforms]] — Marketplace route within the current Adyen for Platforms model.
- [[source-adyen-docs-platforms-multi-pay-in-refunds]] — separately pinned Platforms-path refund guide; its own raw controls its claims and locators.
- [[adyen-platform-internal-transfers]] — separate balance-account correction path, not automatic refund completion.

## Raw Sources

- [[raw/adyen/docs/marketplaces/multi-pay-in/refunds/2026-09-15|Adyen Marketplace multi pay-in refunds guide, captured 2026-09-15]]
