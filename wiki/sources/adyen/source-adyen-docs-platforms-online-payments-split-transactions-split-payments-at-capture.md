---
title: "Adyen Platforms split payments at capture"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/split-transactions/split-payments-at-capture"
raw_files:
  - "adyen/docs/platforms/online-payments/split-transactions/split-payments-at-capture/2026-09-15.md"
tags: [adyen, platforms, split-payments, capture, balance-accounts]
---

## Overview

This 2023-modified guide, captured 2026-09-15, describes setting or changing **Adyen for Platforms online-payment** split instructions when a separately captured authorization is captured. It routes from [[adyen-platforms]] and relates to the general [[adyen-payment-capture]] lifecycle. Split instructions at capture can override payment-request instructions; Adyen still recommends including payment-time splits where possible because some payment methods do not support delayed capture (raw lines 19–25, 39–45, 1674–1678).

## Key takeaways

- Prerequisites in this guide are Checkout API credentials, a server able to receive standard webhooks and subscribed transfer or transaction webhooks, manual capture enabled, and a payment method supporting separate captures (raw lines 27–45). Use the authorization `pspReference` as `paymentPspReference` in POST `/payments/{paymentPspReference}/captures`; the capture's own `pspReference` is different (lines 51–59, 593–644).
- If the capture amount differs from the authorization amount, capture-time splits are required; omission books all funds to the platform's liable balance account. `Surcharge` and `Tip` are unsupported for capture-time splitting (lines 47–49). The page recommends payment-time splits even if later updated, and says capture-time instructions override the initial set (lines 25, 43, 1678).
- Each split directs a part of the amount: `BalanceAccount` to a specified user balance account, `Commission` to the platform liable balance account, and fee types to selected accounts; `Remainder` concerns currency conversion and `TopUp` is separately qualified for `/sessions`. The field table makes `amount.currency` conditional for currency conversion and `reference` conditional for `BalanceAccount` (lines 61–72). The USD 80 sale/commission/fee allocation is an example, not a required fee policy (lines 74–122).
- A capture response with `status: received` only acknowledges the request; use the `CAPTURE` webhook for outcome, then transfer and transaction webhooks to track each split's status and booking (lines 593–666). Request validation checks split **format**, not destination balance-account validity. If the account is nonexistent or attached to a closed account holder, the full transaction **and fees** go to the platform liable balance account despite a successful transaction (lines 646–650).
- Split references support reconciliation; without them the split amounts aggregate into one entry in reporting (lines 1674–1678). Additional fee, FX remainder, chargeback and top-up routes are described at lines 1641–1672.

## Detail locators

- Capture split request parameters, examples and versioned test snippets: raw lines 51–591; curl uses Checkout test `v72`, while Java/PHP/.NET/Node/Go/Python/Ruby examples name their own library versions and note a live endpoint prefix where applicable.
- Receipt and failure/liable-account warning: lines 593–650.
- Per-split transfer/transaction webhook stages and example identifiers: lines 652–1640; sample `received`, `authorised`, `captured` and `booked` events are test payloads, not live financial proof.
- Extra fee, conversion, chargeback, top-up and reference guidance: lines 1641–1678.

## Evidence boundary

This is a capture-time Platforms split guide, not a Classic capture API guide or a claim about in-person splitting. The example account IDs, USD amounts, fee allocation and webhook events do not establish any real platform's merchant of record, legal ownership, split execution, booked funds, payout or bank receipt. It does not establish current payment-method support or account eligibility.

## Related

- [[adyen-platforms]] — platform balance-account and user context.
- [[adyen-payment-capture]] — general authorization/capture outcome boundary.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/split-transactions/split-payments-at-capture/2026-09-15|Pinned Adyen capture-time split guide, captured 2026-09-15]]
