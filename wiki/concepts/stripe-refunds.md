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

The 2026-05-11 refund guide says a fully refunded credit-card charge cannot be disputed or charged back. The 2026-11-07 refund guide omits that sentence. The separately captured fraud-types guidance distinguishes fully refunded from partially refunded card payments, which can still be disputed for their full amount. See [[source-stripe-disputes-fraud-types]].

The November refund guide warns that a merchant's proactive bank-debit refund and an overlapping dispute initiated by the customer's bank can yield two credits. See the payment-method routes in [[source-stripe-refunds]].

## Reversal vs Refund

A refund issued shortly after the charge may appear as a **reversal**. The original charge disappears from the statement without a separate credit. Reversals usually incur lower network fees, so IC+ users might see a cost difference. Check `destination_details[card][type] = 'reversal'` in the API.

## Refund Reference Numbers (ARN/STAN/RRN)

Where supported, customers can give their bank a refund reference. The card ARN can take up to seven business days and is unavailable for reversals. Stripe attempts STAN/RRN when networks lack ARN support. Selected local payment methods have separate references. Check `destination_details[card][reference]` for card refunds.

## Failed Refunds

7 failure reasons: `charge_for_pending_refund_disputed`, `declined`, `expired_or_canceled_card`, `insufficient_funds`, `lost_or_stolen_card`, `merchant_request`, `unknown`. When a bank or issuer returns failed refund funds, Stripe credits them to the Stripe balance. The guides give an up-to-30-day estimate from the post date in failure handling and from the request in tracing. Webhook: `refund.failed`.

For `charge_for_pending_refund_disputed`, Stripe recommends accepting or challenging the dispute instead of refunding to avoid duplicate reimbursement.

## Cancel a Refund

- **Card refunds**: the Dashboard is the only supported channel. Only some card refunds qualify, during a short window before the refund reaches the customer. Processed charge reversals are ineligible.
- **Refunds awaiting bank details**: the API or Dashboard can cancel eligible refunds while `requires_action` and details remain uncollected. The November guide gives examples including Konbini, PromptPay, Boleto and bank transfers. See the state and retry workflow in [[source-stripe-refunds]].

## Cancel a PaymentIntent

Valid statuses: `requires_payment_method`, `requires_capture`, `requires_confirmation`, `requires_action`, `processing` (US Bank Account only). Cannot cancel after success.

## Connect

- Direct charges → connected account debited
- Destination / separate charges → platform debited (reverse transfers to recover from connected accounts)

## Key Events

`refund.created`, `refund.updated` (ARN added here), `refund.failed`, `charge.refunded`, `review.closed`.

## Sources

- [[source-stripe-refunds]] — full refund and cancel guide: mechanics, failed reasons, reversal, ARN, Connect, events
