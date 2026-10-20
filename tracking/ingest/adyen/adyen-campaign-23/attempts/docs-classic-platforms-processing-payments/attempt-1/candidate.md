---
title: "Adyen Classic Platforms: Processing split payments"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/processing-payments"
raw_files:
  - "adyen/docs/classic-platforms/processing-payments/2026-09-15.md"
tags: [adyen, classic-platforms, split-payments, capture, refunds]
---

## Overview

This page is explicitly for **classic Adyen for Platforms** integrations (last modified 2021-08-26; captured 2026-09-15), and sends new implementations to a different guide. It describes splitting shopper payment, capture and refund amounts between Classic platform accounts, including the platform's liable account. In its example, the shopper's USD 400 payment allocates USD 300 to the seller account holder's account and USD 100 to the platform liable account as commission. The Classic destination is an `accountCode`, not a modern balance-account ID. These instructions and examples do not prove an actual authorization, capture, credit, payout or bank receipt. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Split instructions can be supplied at payment, capture or refund, up to 1,000 items for a transfer; stores can also use split configuration for automatic payment splits. In the `splits` array, `account` identifies the destination Classic `accountCode`; `MarketPlace` sends to another platform account, while types such as `Commission` or `VAT` go to the liable account. A `reference` is API-required for `MarketPlace` and recommended for other types for reconciliation. If no split instructions are in effect, payment and associated fees are booked to the liable account. See raw lines 19-49.
- Frontend validation checks split format, **not** whether a destination account exists or its holder is open. If the account is nonexistent or its account holder is `Closed`, Adyen says the full transaction amount goes to the liable account regardless of the requested split; a `PAYMENT_FAILURE` notification reports the failed split, with a separate fund-transfer route for correcting balances. See raw lines 75-81.
- Payment-request splits use POST `/payments`. Capture splits can override them, but only for methods supporting separate captures; iDEAL is named as an unsupported example. If a capture request has no split, the authorization split is used, **except partial captures**, which require split instructions or all funds go to the liable account. See raw lines 83-89 and 140-148.
- `SentForSettle` appears as `PENDING_CREDIT` in the account; the page says `CREDITED` and payout availability follow when Adyen receives payment funds. Neither state alone establishes external bank receipt. See raw lines 134-138.
- For a refund with explicit splits, use only accounts in the original split and the same split references; the page recommends explicit refund splits for partial or multiple partial refunds. A refund without splits uses the **authorization** split, not a later capture split, and its prose limits omission to a full authorized-amount refund with original authorization splits and desired original debits. Without original authorization splits the full refund debit defaults to the liable balance account. The following no-split sample uses `value: 599` after an original USD 10 (`value: 1000`) example, conflicting with the prose's equal-amount condition; do not treat that sample as proof a partial no-split refund preserves allocation. See raw lines 185-200, 218-240 and 283-309.
- The platform is assigned dispute-management responsibility. Chargebacks normally deduct according to the original split, but if a chargeback reversal amount differs from the payment amount, the page says deduction is entirely from the liable account. A separate support configuration can route chargebacks to that liable account. See raw lines 312-320.

## Detail locators

- **Scope and split fields**, raw lines 15-73: Classic-only qualification, shopper-to-seller/liable flow, payment-method note, 1,000-item ceiling, account/type/reference fields and USD 400 illustration.
- **Validation and payment**, raw lines 75-138: invalid/closed-account fallback, notification, `/payments` sample and `SentForSettle` to account-credit states.
- **Capture**, raw lines 140-183: separate-capture restriction, override/fallback and partial-capture instruction requirement.
- **Refund**, raw lines 185-310: explicit split account/reference rules, authorization fallback and inconsistent no-split sample.
- **Disputes**, raw lines 312-320: platform responsibility, default chargeback split and liable-account exceptions.

## Related

- [[adyen-classic-platforms]] — Classic platform account and split model.
- [[adyen-platforms]] — separate current Adyen for Platforms model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/processing-payments/2026-09-15|Adyen Classic Platforms online split-payment guide, captured 2026-09-15]]
