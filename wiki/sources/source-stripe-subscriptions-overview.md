---
title: "Stripe — How Subscriptions Work"
type: source
date_ingested: 2026-11-08
canonical_url: https://docs.stripe.com/billing/subscriptions/overview
original_format: webpage
raw_files:
  - "stripe-billing-subscriptions-overview-2026-11-07.md"
  - "stripe-subscriptions-overview-2026.md"
tags: [stripe, subscriptions, billing, invoice, payment-intent, statuses, lifecycle, entitlements]
---

## Summary

Stripe subscription lifecycle guide covering creation, initial and recurring invoices, eight statuses, payment recovery, status resolution, cancellation and access provisioning. The 2026-11-07 capture distinguishes automatic collection from invoicing, makes activation depend on the configured governing invoices, and separates initial payment recovery from recurring retries.

## Collection Method and Initial State

For an immediate payment with `collection_method=charge_automatically`, the first invoice is `open` and the subscription is `incomplete` for a 23-hour payment window. After nonpayment, it becomes `incomplete_expired`, the invoice is void, and a returning customer needs a new subscription. The initial billing period starts when Stripe creates the first invoice; delayed payment does not move that start. By contrast, `send_invoice` without a trial can start `active` while the first invoice is unpaid. A trial starts `trialing`; this capture describes transition to `active` when the trial ends and payment succeeds, and its status table says product access can safely be provisioned during `trialing`. These are the captured guide's descriptions, not a universal state guarantee for every collection method or configuration. Delayed-confirmation payment methods may follow a different initial status path.

The 2026-05-12 capture describes `default_incomplete` for collecting and confirming a required first payment after creation, `allow_incomplete` as attempting collection immediately and becoming incomplete on failure, and `error_if_incomplete` as failing creation on payment failure. These are dated payment-behavior descriptions. The 2026-11-07 overview says collection and failure defaults depend on payment method and `payment_behavior` can override the default; its omission of those names is no evidence of deprecation or of a universal default.

## Status Resolution and Payment Outcomes

The eight status labels are `trialing`, `active`, `incomplete`, `incomplete_expired`, `past_due`, `canceled`, `unpaid`, and `paused`. The status table explicitly permits provisioning during `trialing`; the paid initial-payment recovery gate below applies to `incomplete` recovery, not trial access. Failed-payment settings determine whether later failure leaves a subscription `past_due` or moves it to `unpaid` or `canceled`; `unpaid` continues invoice generation without payment attempts. The overview's `paused` trial-end row describes a missing default payment method with `trial_settings.end_behavior.missing_payment_method=pause`; consult version-specific pause evidence for other pause paths. Checkout sessions with an `incomplete` subscription cannot update that subscription or invoice until session completion; expiring the session is another documented path.

Subscription settings determine which invoices govern reactivation. **Most recent invoice** is the captured default: the most recent non-voided invoice must be paid or manually marked uncollectible; other outstanding invoices need not block `active`. **All invoices** requires settlement of all applicable outstanding invoices, so paying a new invoice can leave an existing subscription `past_due` or `unpaid`. An applicable invoice is finalized, due and unsettled within the previous 37 months. Payment, voiding or manually marking uncollectible settles it; a Stripe-uncollectible invoice with reason `max_payment_attempts` or `payment_not_received` remains outstanding, while `user_forgiven` does not block activation. Changing the setting waits until the next status evaluation and does not change retry timing or final actions. `active` does not prove every invoice is paid.

| Payment outcome | PaymentIntent | Invoice | Subscription |
| --- | --- | --- | --- |
| Successful initial or later payment | `succeeded` | `paid` | An initial payment can activate its subscription when the required first invoice settles; for an existing `past_due` or `unpaid` subscription, `active` depends on all invoices governing its status being settled |
| Initial card error | `requires_payment_method` | `open` | `incomplete` |
| Initial authentication needed | `requires_action` | `open` | `incomplete` |

Delayed-confirmation methods such as ACH can bypass `incomplete` and become `active` while the PaymentIntent is still `processing`. A later failure can void the invoice while the subscription remains `active`. This is a possible path, not a universal async outcome or final payment guarantee.

## Recovery, Authentication and Access

For an initial card failure while `incomplete`, handle `invoice.payment_failed`, verify the webhook signature, collect a new payment method, confirm the open invoice's PaymentIntent, and update the subscription default payment method for future invoices. Listen for `invoice.paid` and confirm that the subscription is `active` before provisioning. Smart Retries and custom retry rules do **not** retry that initial payment while `incomplete`; the integration must collect it. For later recurring failures, monitor `invoice.payment_failed` and subscription status, notify the customer, and configure Smart Retries or custom rules and the final failed-payment outcome. `past_due` alone does not guarantee another retry.

For authentication, the 2026-11-07 capture directs the client to `stripe.handleNextAction` with the PaymentIntent client secret, then to monitor `invoice.paid` and confirm subscription `active` or active entitlements before provisioning. The 2026-05-12 capture used a Stripe.js `stripe.ConfirmCardPayment` example; this comparison does not prove SDK-wide removal or exclusivity. The newer overview says active entitlements for subscribed product features are created when a subscription becomes `active`; for paid initial-payment recovery, confirm active status or active entitlements before provisioning. Its status table separately says a `trialing` subscription can safely receive product access. Subscription creation, Checkout completion, or an isolated webhook name does not alone establish paid activation or final settlement.

## Earlier First-Invoice Constraints

The 2026-05-12 capture says a `send_invoice` first invoice can be edited for one hour before finalization and sending; a `charge_automatically` first invoice is finalized and charged immediately; and a schedule's first invoice is always open and cannot be edited. These constraints are retained as dated May evidence. Their omission from the November overview does not establish that they stopped applying; verify against a dedicated current invoice or schedule guide before operational use.

> [!warning] Contradiction
> The May overview says subscription creation creates active entitlements and presents invoice payment as an unconditional move to `active`; the November overview ties active entitlements to activation and conditions reactivation on the configured governing invoices. The older generic Smart Retry advice also must not be applied to an initial `incomplete` payment: the November overview expressly excludes automatic retries there. Use the newer lifecycle distinctions for this captured overview while retaining the May statements as dated historical evidence.

## Related Pages

- [[stripe]] — company page
- [[stripe-subscriptions]] — concept page

## Raw Sources

- [[raw/stripe-billing-subscriptions-overview-2026-11-07]] — 2026-11-07 lifecycle and status-resolution capture (186 lines)
- [[raw/stripe-subscriptions-overview-2026]] — 2026-05-12 lifecycle guide with payment-behavior and first-invoice examples (180 lines)
