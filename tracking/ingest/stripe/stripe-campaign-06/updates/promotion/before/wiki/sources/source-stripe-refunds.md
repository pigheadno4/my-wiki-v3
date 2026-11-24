---
title: "Stripe — Refund and Cancel Payments"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-refunds-2026.md"
tags: [stripe, refunds, cancel, paymentintent, arn, reversal, connect, webhooks, failed-refunds]
---

## Summary

Complete refund and cancellation guide: mechanics, failed refund handling, reversal vs refund, ARN tracing, Connect behavior, and key webhooks.

## Key Rules

- **Cancel** (before completion): free
- **Refund** (after success): processing fees NOT returned
- **Balance source**: available balance only (not pending); insufficient → card refunds go pending, other PM refunds fail
- **Destination**: refund only to original payment method; can't redirect to different card/bank
- **Disputes**: impossible on fully refunded credit card charges

## Reversal vs Refund

Refunds issued shortly after original charge may appear as **reversals** (original charge drops off statement, no separate credit). IC+ users pay lower network fees on reversals. Verify via `destination_details[card][type] = 'reversal'` (API) or Timeline in Dashboard.

## Refund Reference Numbers

ARN (Acquirer Reference Number), STAN (System Trace Audit Number), or RRN (Retrieval Reference Number). Available up to 7 business days after initiating. Not available for reversals. Access via `destination_details[card][reference]` + `reference_type` in API or Timeline in Dashboard.

## Failed Refunds (7 Reasons)

| Reason | Description |
| --- | --- |
| `charge_for_pending_refund_disputed` | Customer disputed while refund pending — accept/challenge dispute instead |
| `declined` | Declined by financial partners |
| `expired_or_canceled_card` | Card canceled or expired |
| `insufficient_funds` | Pending refund expired before funds available |
| `lost_or_stolen_card` | Card lost or stolen |
| `merchant_request` | Business requested failure |
| `unknown` | Unknown reason |

Failed refund → Stripe adds amount back to your balance (up to 30 days). Webhook: `refund.failed`.

## Cancel a Refund

- **Card refunds**: Dashboard only, brief window before processing
- **Bank transfer refunds awaiting banking info**: API or Dashboard

Canceled refunds transition to `canceled` status with `failure_reason` + `failure_balance_transaction`.

## Cancel a PaymentIntent

Valid statuses: `requires_payment_method`, `requires_capture`, `requires_confirmation`, `requires_action`, `processing` (US Bank Account only). Cannot cancel after success.

## Connect Behavior

| Charge type | Debited from |
| --- | --- |
| Direct charges | Connected account |
| Destination / separate charges | Platform (must reverse transfers to recover from connected accounts) |

## Key Webhooks

`refund.created`, `refund.updated` (ARN added here), `refund.failed`, `charge.refunded`, `review.closed`.

## Related Pages

- [[stripe-refunds]] — concept page
- [[disputes]] — disputes impossible on fully refunded credit card charges
- [[source-stripe-receipts]] — refund receipts

## Raw Sources

- [[stripe-refunds-2026]] — verbatim refunds and cancel guide (295 lines)
