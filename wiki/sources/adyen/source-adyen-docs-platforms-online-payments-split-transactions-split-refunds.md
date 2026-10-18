---
title: "Adyen for Platforms split refunds"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/split-transactions/split-refunds"
raw_files:
  - "adyen/docs/platforms/online-payments/split-transactions/split-refunds/2026-09-15.md"
tags: [adyen, platforms, online-payments, refunds, split-booking]
---

## Overview

This 2026-09-15 Adyen for Platforms page explains how a platform can send split instructions with a Checkout API refund request to allocate refund debits among its user and platform balance accounts. It describes who bears those debits in balance-platform bookkeeping; it does not identify the merchant of record or prove that a shopper received funds. See [[adyen]] and [[adyen-platforms]] for provider and platform context.

## Key takeaways

- Use the original payment PSP reference in `POST /payments/{paymentPspReference}/refunds`. The body requires `amount` and `merchantAccount`; the refund value is at most the captured amount and its currency must match the payment authorization. A request-level `reference` is optional. Checkout API credentials and a server prepared for standard, transfer and transaction webhooks are prerequisites. The refund request outcome arrives asynchronously in a `REFUND` webhook, so request acceptance is not final refund success.
- Refund split instructions can select user or platform balance accounts for deductions, but deductions are limited to balance accounts credited by the payment. The limitations section also says to use the same `pspReference` values as the original split. Some payment methods do not support partial or multiple partial refunds. `splits` is labelled recommended, not universally required; Adyen strongly recommends always specifying it for partial refunds.
- For a full refund without `splits`, when the original authorization contained splits, Adyen uses the authorization split ratio, not any capture split. If the authorization had no split instructions, the whole refund is debited from the platform's liable balance account. The no-splits example explicitly assumes a full amount, authorization splits and a wish to preserve the original split. Do not extrapolate this fallback to an unspecified partial-refund allocation.
- For explicit splits, the table lists `account` (user or platform balance-account ID), `amount.value`, and `type` as required for each split item; `reference` is conditionally required for `BalanceAccount`. Its listed types distinguish a balance-account refund debit, platform commission debit from the liable balance, Adyen markup/commission or aggregated fees, and currency-conversion remainder. Fees default to the platform's liable balance account. The top-level refund currency matches authorization, while split-item `amount.currency` is conditionally required if a different deduction currency is requested; the linked currency-conversion guide owns detailed FX behavior. The displayed Commission request example omits `account` despite the table's blanket required label, so the example does not resolve every type's field requirements.
- Split-format validation does not validate the named balance accounts. Even a successful transaction may be booked elsewhere: if a specified balance account does not exist or its account holder is closed, Adyen says the full transaction and fees book to the platform's liable balance account. The page points to an internal transfer as a possible balance correction; it is a separate action, not an automatic reversal.
- Track each refund split through balance-platform transfer and transaction webhooks. The examples distinguish outgoing refund amount, transaction-fee and platform-commission items using `platformPaymentType`, original payment PSP reference and refund modification PSP reference. Example transfer statuses progress `received` → `authorised` → `refunded` with a transaction ID, then a `booked` transaction event; the JSON examples are `environment: test` and illustrative USD values, not live or account-specific proof. This page concerns refunds after captured payments, not authorization/capture splitting or chargebacks.

## Detail locators

- Purpose, credentials, webhook prerequisites and refund limitations: raw lines 15–33. Checkout refund path, amount/currency and merchant-account fields, partial-split recommendation: lines 35–51. Explicit split fields/types and fee defaults: lines 53–70; test Checkout v72 and versioned SDK examples: lines 72–510.
- No-splits authorization-versus-capture rule and liable fallback: lines 511–523; request examples: lines 525–788. Asynchronous `REFUND` outcome, account validation fallback and possible correction: lines 789–795. Tracking webhook types and per-split sequencing: lines 797–811. Refund amount, fee and commission example payloads: lines 813–1767.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — Platforms user, balance and liable-account context.
- [[adyen-refunds]] — general online-payment refund context; distinct from Platforms split booking.

## Related raw API references

- The raw page links to Checkout refund, payment-method support, internal fund transfers, transaction fees, and refund currency conversion. Read those routes separately for operation-specific eligibility, reversal and FX semantics.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/split-transactions/split-refunds/2026-09-15|Adyen Docs: Split refunds (2026-09-15 snapshot)]]
