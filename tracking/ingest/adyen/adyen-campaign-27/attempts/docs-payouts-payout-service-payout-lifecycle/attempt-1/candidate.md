---
title: "Adyen Payout Service payout lifecycle"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/payout-lifecycle"
raw_files:
  - "adyen/docs/payouts/payout-service/payout-lifecycle/2026-09-15.md"
tags: [adyen, payouts, payout-service, transfers, webhooks, lifecycle]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service guide separates accounting events for a transfer out of a balance account from later tracking of delivery to a counterparty bank account or card. A received request, reserved amount, and booked debit are different states; booking alone does not prove the beneficiary received funds. The guide covers regular and optionally reviewed payout flows, later internal screening, bank/card-specific tracking, and returns. This Transfers API lifecycle is distinct from the legacy Online Payout API described in [[adyen-payouts]].

## Key takeaways

- In the regular flow, a valid request yields a `balancePlatform.transfer.created` webhook with `status: received`; invalid parameters can produce only an API error, without a webhook. Sufficient funds lead to reservation and `authorised`; insufficient funds lead to `refused`. Booking deducts funds and creates a transaction, with `transfer.updated: booked` and `transaction.created`. See raw lines 27–44.
- An **optional** `review` object on `POST /transfers` adds team approval: initial `received`/`pending`, then approved `authorised`, customer cancellation, or cancellation after 30 days without action (`approvalExpired`). Approved payouts then proceed to booking/debit. This is a Payout Service request option, not an inherited legacy staged-review requirement. See raw lines 48–63.
- After booking, a tracking webhook can report `pending` for Adyen manual screening. Failed internal review freezes funds and prevents external payout; the bank also screens incoming funds. Card-network `accepted` means accepted for processing, not cardholder receipt, and card-scheme checks can later yield `refused`. See raw lines 65–103.
- For instant bank payouts in the guide's SEPA/UK/US scope, `credited` follows counterparty-bank acceptance, while a failed instant connection or bad payout data requires a later retry or correction and retry. For non-instant bank payouts, `estimatedArrivalTime` is an estimate that can be revised if a batch is delayed, not credit confirmation. See raw lines 105–132.
- The return section says non-instant payouts may be **returned** after counterparty-bank screening: `transfer.updated: returned` carries a reason and `transaction.created` credits the source balance account. Its “cannot fail” wording belongs to that post-dispatch bank-return distinction; it must not erase the earlier request rejection, insufficient-funds refusal, or internal-review failure paths. See raw lines 31–39, 89–99 and 136–149.

## Detail locators

- **Regular accounting flow and webhook split:** raw lines 23–44.
- **Optional team approval, cancellation and 30-day expiry:** raw lines 48–63.
- **Post-booking tracking and internal review:** raw lines 65–103.
- **Instant credit/failure versus non-instant ETA/batching:** raw lines 105–132.
- **Bank return and balance-account credit:** raw lines 136–149.

## Related

- [[adyen-payouts]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/payout-lifecycle/2026-09-15|Adyen Payout Service payout lifecycle — collected 2026-09-15]]
