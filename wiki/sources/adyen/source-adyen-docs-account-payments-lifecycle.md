---
title: "Adyen payments lifecycle statuses"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/payments-lifecycle"
raw_files:
  - "adyen/docs/account/payments-lifecycle/2026-09-15.md"
tags: [adyen, payment-lifecycle, customer-area, statuses, reconciliation]
---

## Overview

This Adyen account guide (2025-09-18 last-modified metadata; captured 2026-09-15) explains how a payment appears and changes status in Customer Area, then catalogs status meanings across offers, authorization, capture/settlement, refunds, disputes, online payouts, and stored value. It is a status interpretation and navigation reference, not a live transaction record or a guarantee of merchant payout or shopper receipt. Use [[adyen-online-payments]] for the integration route, [[adyen-payment-capture]] for capture-specific behavior, and [[adyen]] for provider context.

## Key takeaways

- Customer Area tracking applies to any Adyen payments integration; viewing payments requires `View Payments` or `View key payments data` role. Each payment entry is identified by PSP reference and merchant reference; subsequent statuses update that entry, and the **Payment lifecycle** journal lists each status. A status requiring action should be investigated until an appropriate final outcome is known. [Raw lines 19–49]
- An **offer** precedes completion/authorization for flows such as redirect; `Received` and `Open` are not authorization. `Authorised` means shopper authorization and financial-institution approval, with funds reserved. Capture is distinct; Adyen recommends waiting for capture before delivering goods/services, and authorization can expire if not captured in its payment-method-specific validity period. [Raw lines 69–117, 123–133, 198–210]
- `SentForSettle` awaits the institution's funds and is no longer cancellable. `Settled` means Adyen received funds and is final for a successful payment, **not** that Adyen paid the merchant. `SettleScheduled` is Sales day payout-specific and appears as `Settled` in reports; `SettledReversed` can later return to `Settled`, while `CaptureFailed` describes failed capture with a possible subsequent resolution attempt. [Raw lines 228–294, 354–377]
- Refund states differ: `SentForRefund` awaits confirmation; `Refunded` says the merchant account was debited and the financial institution intends to credit the shopper, which can still take up to 40 days. `RefundScheduled` appears as `Refunded` in reports, while `RefundedReversed`, `RefundFailed`, and `RefundScheduledUnconfirmed` have different money-movement meanings. [Raw lines 387–443, 505–577]
- Online **payout** statuses concern sending funds from the account to another receiver, not Adyen's ordinary merchant settlement payout. `ReceivedPayout` is request receipt, `PayoutAuthorised` precedes sending, `SentForPayout` awaits completion, and `PaidOut` means transfer to receiver. Sales day payout-specific `PaidOutScheduled` appears as `PaidOut` in reports. [Raw lines 663–727]

## Detail locators

- Customer Area roles, payment list, PSP/merchant-reference identity, journal: raw lines 23–49. Offer and authorization states, including final refusal/cancellation/error and expiry: raw lines 69–226.
- Capture and settlement statuses, conditional acquiring/installment/Sales day payout cases, and failure/reversal: raw lines 228–385. Refund statuses and shopper-receipt distinctions: raw lines 387–585.
- Dispute/chargeback statuses and balance movement: raw lines 587–661. Online payout statuses: raw lines 663–800. Stored-value load/unload statuses: raw lines 802–848.
- The page labels some states final within their own status flow, but that label does not collapse later merchant settlement, shopper credit, disputes, payout processing, or external-acquirer follow-up into one universal financial-finality claim. Report aliases such as `SettleScheduled` → `Settled`, `RefundScheduled` → `Refunded`, and `PaidOutScheduled` → `PaidOut` are context-specific, not proof that the underlying live payment completed another stage.

## Related

- [[adyen-online-payments]]
- [[adyen-payment-capture]]
- [[adyen]]
- [[source-adyen-docs-online-payments-build-your-integration-payment-result-codes]]

## Raw Sources

- [[raw/adyen/docs/account/payments-lifecycle/2026-09-15|Adyen payments lifecycle, 2026-09-15 snapshot]]
