---
title: "Transaction fees | Adyen for Platforms"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/transaction-fees"
raw_files:
  - "adyen/docs/platforms/online-payments/transaction-fees/2026-09-15.md"
tags: [adyen, platforms, transaction-fees, split-payments, reconciliation]
---

## Overview

This 2023-last-modified [[adyen]] for Platforms guide, captured 2026-09-15, explains how to allocate transaction fees that Adyen calculates after receiving a payment request. Despite the URL's online-payments path, it says the guidance applies to both online and in-person payments. The default destination is the platform's liable balance account; eligible payment-related fees can instead be booked to a user's balance account through fee-type split instructions. This is fee-booking guidance, not a determination of legal seller, merchant of record, final settlement or bank receipt. [[adyen-platforms]]

## Fee scope and booking

- The guide says a platform that already processes payments has no additional requirements for this feature. Individual fee types are `Interchange`, `SchemeFee`, `AdyenMarkup` and `AdyenCommission`. `AcquiringFees` aggregates interchange plus scheme fees, `AdyenFees` aggregates markup plus commission, and `PaymentFee` aggregates all transaction fees. Adyen Commission is associated with blended rates and Markup with Interchange++ pricing in the table; do not assume both apply to every payment.
- Processing costs, including those on refused or cancelled payments, and other aggregated costs such as 3DS enrollment cannot be allocated to individual payments in the payment request. Tiered-pricing discounts also cannot be allocated to individual payments. Thus the page's fee-split types do not represent every possible cost or a universal invoice amount.
- Fee split instructions can be sent in a payment or capture request; the worked flow names Checkout `/payments` or `/sessions` with fee items in `splits`. The field table marks `account`, `type` and unique `reference` required and `description` optional. Fees are unknown at payment time, so the examples route fee types to balance accounts rather than asserting a precomputed fee amount. If no transaction-fee split is supplied, Adyen automatically inserts `PaymentFee` and books all transaction fees to the platform's liable balance account; the page recommends specifying even liable-account fee splits for reconciliation.
- Granular fee-type booking overrides the corresponding portion of an aggregate. For example, `AdyenMarkup` directed to liable balance overrides that part of a user-directed `PaymentFee`; interchange, scheme fee and Adyen commission remain on the user's balance in the example. The table at raw lines 63–71 gives the full `PaymentFee`/`AcquiringFees`/`AdyenFees` hierarchy and individual overrides. These destinations concern balance-account booking, not who legally owns the sale or who receives a payout.

## Event and report evidence

- The example response returns `resultCode: Authorised` with `merchantReference`; that is authorization evidence, not proof that fee transfers were captured or booked. The guide routes tracking through `balancePlatform.transfer.created`, `balancePlatform.transfer.updated` and `balancePlatform.transaction.created` for each split item. Its test webhook examples progress through `received`, `authorised`, `captured` with a `transactionId`, and a transaction marked `booked`. A received or authorised transfer is not a booked debit; sample booked balance-account data does not prove payout or bank credit.
- The Balance Platform Accounting Report has separate rows and Amount values for aggregate `PaymentFee`, `AcquiringFees` and `AdyenFees`, while its four Platform Payment columns show Interchange, Scheme Fee, Markup and Commission at granular level. The automatically added liable-account `PaymentFee` also appears in the report. Match request reference, transfer and booked transaction/report records at the correct grain.
- **Pinned-source contradictions:** raw line 1141 says the example's `AdyenFees` debit is from the user's balance, whereas raw lines 99–104, 1147 and 1301 and the sample liable-account payload say it is from the platform's liable balance. The worked prose at line 99 says EUR 80 while the versioned payment sample and authorization response show USD 80; later webhook examples show EUR. The field table at line 113 describes `account` as a user's balance account even though the illustrated `AdyenFees` item targets the liable account. The illustrated fee webhooks also conflict: the `AcquiringFees` captured transfer names balance account `BA...02` after `BA...01` in its received transfer and booked transaction (raw lines 855–857, 1008–1011, 1127–1129); the `AdyenFees` booked transaction names user `BA...01` after liable balance in its transfer (1163–1166, 1317–1320, 1436–1439), uses a different transfer ID from the preceding transfer (1385–1387, 1416–1417), and reuses the `AcquiringFees` booked transaction ID (1100–1103, 1409–1413). Treat these payloads as inconsistent illustrations, not a normative join or destination map; reconcile actual per-split events and reports, verify the actual request/schema and account destination, and do not infer payout or bank receipt.
- This page does not define partial-refund or chargeback fee reversal allocation. Those cases require their own flow-specific sources. The page's historical snapshot and illustrative test payloads do not establish current account eligibility, actual fee rate, completed booking or a financial outcome.

## Detail locators

- **Scope, default and requirements:** raw lines 15–25.
- **Assignable and excluded costs; fee taxonomy and aggregate-over-atomic precedence:** raw lines 27–95.
- **`/payments`/`/sessions` field table, split example and currency discrepancy:** raw lines 97–782.
- **Authorization response and per-split transfer/transaction tracking:** raw lines 782–1446; contradictory Adyen-fee destination at lines 1141 and 1147.
- **Balance Platform Accounting Report grain and omitted-split default:** raw lines 1448–1454.

## Related

- [[adyen-platforms]]
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-refunds]] — separate refund allocation
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-chargebacks]] — separate chargeback allocation

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/transaction-fees/2026-09-15|Adyen Platforms transaction-fee guide — collected 2026-09-15]]
