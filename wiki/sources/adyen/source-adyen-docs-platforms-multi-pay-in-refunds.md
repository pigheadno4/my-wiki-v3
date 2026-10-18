---
title: "Refund third-party multi pay-in payments through Adyen for Platforms"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/multi-pay-in/refunds"
raw_files:
  - "adyen/docs/platforms/multi-pay-in/refunds/2026-09-15.md"
tags: [adyen, platforms, multi-pay-in, refunds, split-payments]
---

## Overview

This 2026-09-15 Adyen for Platforms guide covers refunds of payments processed by a third-party pay-in provider but settled in platform users' balance accounts. The platform initiates an Adyen Checkout API refund to deduct amounts from platform/user balances and return funds to its multi pay-in account. The pay-in partner, through a separately arranged process, is responsible for sending the refund amount to the user's customer. An Adyen request, balance-account deduction or multi pay-in credit is not proof that the partner returned money to that customer.

## Key takeaways

- Before initiating at Adyen, have a refund process in the pay-in partner's system. Use the original payment PSP reference in POST `/payments/{paymentPspReference}/refunds`. The request requires an `amount` and `merchantAccount`; the refund value equals the captured amount or is less for a partial refund, and its top-level currency matches the payment authorization currency. A merchant refund reference is optional for reconciliation. The refund-request outcome arrives asynchronously in a `REFUND` webhook; do not treat request submission as final success.
- A `splits` array can allocate deductions across a user's balance account and the platform's liable balance account. For partial refunds, the page strongly recommends explicit split instructions. Split-item fields include destination `account`, `amount.value`, `type` and a `reference` conditionally required for `BalanceAccount`; split `amount.currency` is conditionally required when that portion is refunded in a currency different from the original payment. Listed types include `BalanceAccount`, `Commission`, Adyen fee variants and `Remainder`; by default all fees are deducted from the platform's liable balance account. The table marks split `account` required, while the page's `Commission` request example omits it, so this snapshot does not resolve that field's per-type requirement.
- Omitting refund splits to reuse the original ratio is described for a full refund equal to the original payment amount when the *authorization* contained split instructions. The refund follows authorization splits, not capture splits. If the authorization had no split instructions, the full refund amount is debited from the platform's liable balance account. Do not generalize this no-split route to partial refunds.
- The API validates split-instruction format, not whether referenced balance accounts exist or can receive the debit. An apparently successful transaction can therefore debit an unintended account; if an account is nonexistent or its holder is closed, the full transaction and fees book to the liable balance account. The guide points to internal transfers for correction, which is a separate action.
- Use the `REFUND` webhook for the refund-request outcome and transfer/transaction webhooks for fund movements. The examples distinguish outgoing user-balance and liable-commission refund transfers, and an incoming internal transfer to the multi pay-in account. They show `received`, `authorised`, `refunded` or `booked` statuses, with transaction-created events for balance postings. Status on one leg is not proof of another leg or of the pay-in partner's customer refund. The JSON payloads, USD values, identifiers and library-version/test-environment calls are illustrative. Some example identity/amount fields differ across tabs; use these examples as locators, not an account-specific ledger.

## Detail locators

- Opening paragraphs and `## Refund a payment`: third-party processor versus Adyen/partner duties, original PSP reference, amount/currency and merchant-account fields, asynchronous `REFUND` outcome.
- `### Tab: Refund with split instructions (recommended)`: split field matrix, fee/commission types and example API v72/test requests in several library versions.
- `### Tab: Use split instructions from payment authorization`: full-refund conditions, authorization-versus-capture rule and liable fallback.
- `### Troubleshooting`: format-only validation, invalid balance-account fallback and separate internal correction.
- `## Track fund movements` and its three tabs: outgoing user/liable deductions, incoming multi pay-in credit, transfer and transaction webhook status examples.

## Related

- [[adyen-platforms]] — platform model and source route.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/multi-pay-in/refunds/2026-09-15|Adyen refund third-party payments guide (fetched 2026-09-15)]]
