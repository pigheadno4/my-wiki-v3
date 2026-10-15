---
title: "Classic API refund | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/modify-payments/refund"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15.md"
tags: [adyen, classic-api, online-payments, refunds, webhooks]
---

## Overview

This 2026-09-15 Adyen Docs snapshot describes Classic Payment API refunds after capture, through Customer Area, referenced `/refund`, or approval-limited unreferenced `/refundWithData`. Adyen marks this endpoint inactive and unsupported for new integrations, directing new builds and existing-integration migration toward Checkout API. See [[adyen]], [[adyen-online-payments]], and [[adyen-refunds]].

## Key takeaways

- A referenced `/refund` uses the original payment `pspReference` as `originalReference`, plus merchant account and a `modificationAmount` no greater than the captured amount. Its response has a distinct refund-request `pspReference` and `[refund-received]`; that response is receipt of the request, not final return of funds. The guide permits multiple partial refunds for supported methods while their sum remains within the captured amount.
- Adyen later sends a `REFUND` webhook with the refund-request PSP reference and a success flag. A false result has a reason; a true result usually leads to successful refund but may still be followed by scheme rejection and `REFUND_FAILED`. Some methods can instead reverse a refund, reported as `REFUNDED_REVERSED`, with funds back in the merchant account.
- A refund is for an already captured payment; the guide directs uncaptured payments to cancellation. Failure reasons include insufficient remaining payment balance after refunds or chargebacks, insufficient merchant funds, uncaptured transactions, and payment-method expiration.
- Where the original payment PSP reference is unavailable, the Classic `/refundWithData` route is limited by default and requires contacting Adyen Support for enablement. The page gives bank-account, raw-card, and recurring-contract variants; raw card data requires PCI Level 1 or 2 compliance. It explicitly routes customer payouts to Adyen's payout solution instead.
- `/refundWithData` returns a request reference and a `Received` result in examples, then reports validation outcome asynchronously through `REFUND_WITH_DATA`. In that webhook, `originalReference` identifies the unreferenced refund request because the original payment reference is unknown, while `pspReference` is generated when the refund was captured. A successful validation still allows later scheme rejection or reversal. This is historical Classic behavior, not a Checkout API schema or proof of current eligibility.

## Detail locators

- Inactive lifecycle, Checkout migration, and Customer Area route: lines 19–30.
- Captured-payment condition and referenced request fields: lines 32–43; distinct refund response reference: lines 59–67.
- `REFUND` webhook and success/false meanings: lines 70–81.
- Method-qualified partial and multiple refunds: `Partial refund`, lines 133–141.
- Failure reasons and later scheme rejection/`REFUND_FAILED`: lines 143–182; reversal/`REFUNDED_REVERSED`: lines 184–191.
- Unreferenced refund purpose, payout distinction, restricted enablement, and target variants: lines 227–239; raw-card PCI condition: lines 277–279; recurring contract identifiers: lines 311–317.
- `REFUND_WITH_DATA` request/reference distinction and asynchronous outcome: lines 349–365.

## Related

- [[adyen-refunds]] — provider refund lifecycle.
- [[adyen-online-payments]] — Classic and Checkout integration routes.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15|Classic refund (2026-09-15)]]
