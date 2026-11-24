---
title: "Stripe Refunds"
type: concept
category: technology
tags: [stripe, refunds, cancel, arn, reversal, failed-refund, connect, paymentintent]
---

## Overview

Refunds return funds to the original payment method. Processing fees are not returned. Refunds use the available Stripe balance (not pending); insufficient balance causes card refunds to go pending and other PM refunds to fail.

## Cancel vs Refund

| | Cancel | Refund |
| --- | --- | --- |
| When | Before completion | After success |
| Cost | Free | Processing fees not returned |
| How | Cancel PaymentIntent | Create Refund object |

**Disputes impossible** on fully refunded credit card charges.

## Reversal vs Refund

Refunds issued shortly after the original charge may appear as **reversals** — original charge drops off statement, no separate credit issued. IC+ users pay lower network fees on reversals. Check `destination_details[card][type] = 'reversal'` via API.

## Refund Reference Numbers (ARN/STAN/RRN)

Banking tracing identifiers — provide to customer if refund isn't visible. Available up to 7 business days after initiating. Not available for reversals. Check `destination_details[card][reference]` via API.

## Failed Refunds

7 failure reasons: `charge_for_pending_refund_disputed`, `declined`, `expired_or_canceled_card`, `insufficient_funds`, `lost_or_stolen_card`, `merchant_request`, `unknown`. Failed refund returns to Stripe balance (up to 30 days). Webhook: `refund.failed`.

**Important**: if `charge_for_pending_refund_disputed`, accept/challenge dispute instead — refunding would double-reimburse the customer.

## Cancel a Refund

- **Card refunds**: Dashboard only, brief window
- **Bank transfer refunds awaiting banking info**: API or Dashboard

## Cancel a PaymentIntent

Valid statuses: `requires_payment_method`, `requires_capture`, `requires_confirmation`, `requires_action`, `processing` (US Bank Account only). Cannot cancel after success.

## Connect

- Direct charges → connected account debited
- Destination / separate charges → platform debited (reverse transfers to recover from connected accounts)

## Key Events

`refund.created`, `refund.updated` (ARN added here), `refund.failed`, `charge.refunded`, `review.closed`.

## Sources

- [[source-stripe-refunds]] — full refund and cancel guide: mechanics, failed reasons, reversal, ARN, Connect, events
