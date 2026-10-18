---
title: "Adyen Platforms in-person transaction fees"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/transaction-fees"
raw_files:
  - "adyen/docs/platforms/in-person-payments/transaction-fees/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, transaction-fees]
---

## Overview

This 2023-02-10-modified Adyen for Platforms page, captured 2026-09-15, explains how a platform can allocate **in-person payment-related transaction fees** across a user's and its own liable balance accounts using Terminal API split instructions. The fee amounts are calculated after the payment request, so split types describe booking destinations rather than known fee values at payment time. This source does not decide the legal seller or merchant of record, establish a current fee schedule, prove a particular booking, or show payout or bank receipt. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- For a platform already processing payments, the page lists no **additional** preparations. Payment-related **Interchange, Scheme Fees, Adyen Markup and Adyen Commission** can be assigned to a user balance account through split instructions; absent such instructions, these fees default to the platform's **liable balance account**. **Processing costs**, including those for refused/cancelled payments, other aggregated costs such as 3DS enrollment, and tiered-pricing discounts cannot be allocated to individual payment requests under this guide. A provider fee named **AdyenCommission** is distinct from the platform's own **Commission** sale split.
- Split types form a hierarchy: `PaymentFee` aggregates all transaction fees; `AcquiringFees` aggregates interchange and scheme fees; `AdyenFees` aggregates Adyen commission and markup. Individual types override the corresponding aggregate portion, and aggregate types override that portion of `PaymentFee`. A more granular fee item moves only its own component to the specified account; the remaining components follow the aggregate instruction. If **no fee-type booking instruction** is sent in the payment or capture request, Adyen adds a `PaymentFee` split to the liable account. The page recommends explicit fee instructions even when allocating to liable, to aid reconciliation.
- The illustrative Terminal API request encodes `split.api`, item count, total amount/currency and per-item types/accounts/references in `SaleToAcquirerData` as **ampersand-separated key-value pairs** or **Base64-encoded JSON**. Its example uses `split.totalAmount=8000` and `split.currencyCode=USD` while `AmountsReq.RequestedAmount` is **80.00 USD**; preserve those field-specific representations and consult the Terminal API schema before building requests. The example assigns a USD 75 sale and USD 5 platform commission separately from fee splits; these amounts and a V400m test payload are illustrative, not standard rates or live execution.
- The example assigns `AcquiringFees` to the user balance account and `AdyenFees` to the liable account in its request. The later Adyen-fees introduction says **user** account, whereas its transfer prose/payload say **liable**, and its `transaction.created` sample names a **user** balance account with a different transfer ID/reference. The acquiring-fee captured-transfer payload also names a different balance-account ID from its received/booked examples. The fee webhook samples are in **EUR** while the payment request is **USD**, without a conversion explanation. Do not derive a clean account/sign/currency reconciliation rule from these examples; use actual transaction and accounting evidence for an account-specific answer.
- Fee movement has separate `transfer.created` **received**, `transfer.updated` **authorised/captured**, and `transaction.created` **booked** stages per split item; a Terminal `PaymentResponse` **Success** alone is not a booked-fee or final payout record. The Balance Platform Accounting Report shows aggregated `PaymentFee`, `AcquiringFees` and `AdyenFees` rows with an Amount column, while four Platform Payment columns show granular interchange, scheme fee, markup and Adyen commission. Report rows and sample webhook times are records/examples, not bank settlement proof.
- This page supplies no separate partial-capture algorithm or current country/role eligibility table. Linked fee-reconciliation guidance is a next-step route; do not import its behavior without reading it.

## Detail locators

- Scope, default liable allocation, non-pass-through costs and fee-type precedence: pinned raw lines 15–89.
- USD 80 example and Terminal API `SaleToAcquirerData` formatting: pinned raw lines 91–249.
- Per-split fee transfer/transaction webhook stages and contradictory sample accounts/currency: pinned raw lines 250–887.
- Accounting Report aggregate/granular fields and default `PaymentFee` row: pinned raw lines 888–898.

## Related

- [[adyen-platforms]] — provider concept for platform and user balance-account context.
- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-payments-at-authorization]] — separate Terminal API sale/commission split guide.

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/transaction-fees/2026-09-15|Adyen in-person transaction fees, captured 2026-09-15]]
