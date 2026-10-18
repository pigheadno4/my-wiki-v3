---
title: "Adyen for Platforms split chargeback booking"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks"
raw_files:
  - "adyen/docs/platforms/online-payments/split-transactions/split-chargebacks/2026-09-15.md"
tags: [adyen, platforms, online-payments, split-transactions, chargebacks]
---

## Overview

This 2023-modified, 2026-09-15-captured Adyen for Platforms guide configures where an online-payment chargeback’s disputed amount and chargeback fees are booked across platform balance accounts. Its scope is a dispute/chargeback after an issuer dispute begins, including reversals and second chargebacks; it is distinct from the original payment split, a capture, or a refund. The booking choice does not by itself establish contractual liability, merchant of record, a successful defense, or completed movement of funds. See [[adyen-platforms]].

## Key takeaways

- For a platform already processing online payments, the guide states no special chargeback-handling prerequisite. Initially, Adyen debits the entire disputed amount from the platform’s liable balance account; a successful defense or customer repayment credits it back as a chargeback reversal, while an unsuccessful defense can lead to a second chargeback debit. The platform can accept a chargeback or seek defense material from its user.
- Three booking choices are documented for a potential chargeback: all to the platform liable balance account, all to one specified balance account, or allocation using the original payment’s `splits` ratio. The ratio behavior uses relative proportions, not original amounts; the disputed amount and currency need not equal the original payment. One-account behavior requires `targetAccount`. Optional `costAllocationAccount` routes chargeback fees, which otherwise default to the liable balance account.
- Support configures the balance-platform default; a payment-level `platformChargebackLogic` overrides that default, and logic on a capture request overrides the payment request. The page shows `/payments`, `/sessions` and `/payments/{paymentPspReference}/captures` as configuration routes. `behavior` accepts `deductFromLiableAccount`, `deductFromOneBalanceAccount`, or `deductAccordingToSplitRatio`. These are prospective booking instructions for chargeback events, not a reallocation of the original sale.
- The Checkout request validates split-instruction format, not referenced balance-account existence or account-holder status. A successful request can still book the full transaction and fees to the platform liable balance account when a target does not exist or its account holder is closed. The guide points to an internal funds transfer to correct balances, but does not authorize a blind transfer or prove that a particular correction succeeded.
- The guide calls for `CHARGEBACK` notifications and separate balance-platform transfer/transaction webhooks for each split item. Its example progression separates outgoing transfer `received`, `authorised`, later `chargeback` with `transactionId`, and a `balancePlatform.transaction.created` with `booked`; a notification or accepted request alone is not a booked movement. Example `platformPaymentType` values distinguish disputed balance-account amount, payment fee and commission; precise fields remain in the pinned webhook examples and Balance Platform Accounting Report route.
- The illustrative split-ratio calculation mixes USD and EUR labels for the same USD 88 dispute, and a fee webhook example has inconsistent balance figures/status labeling. Treat those example values as illustrative, not an authoritative currency conversion, fee rule or observed ledger. Test API/SDK snippets are version-labeled and use test credentials; they do not establish current live compatibility.

## Detail locators

- Dispute, liable-account default, reversal and second-chargeback lifecycle: pinned raw lines 15–35.
- Three behaviors, default/payment/capture precedence, fields and webhook notice: pinned raw lines 37–68.
- Invalid/closed target fallback and correction route: pinned raw lines 70–74.
- Liable-account request examples: pinned raw lines 80–766; one-account behavior, default fee account and examples: lines 767–1474.
- Split-ratio rule, mixed-currency example and test request examples: pinned raw lines 1475–2188.
- Transfer/transaction webhook progression, split-item grain, disputed-amount/fee/commission examples and report link: pinned raw lines 2189–3160.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/split-transactions/split-chargebacks/2026-09-15|Platforms split-chargebacks snapshot (2026-09-15)]]
