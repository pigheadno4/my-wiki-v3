---
title: "Stripe Subscription Invoices"
type: concept
category: framework
tags: [stripe, billing, subscriptions, invoices, payment-collection, draft-invoice, metadata]
---

## Overview

Stripe generates one invoice per subscription billing period. This page covers the invoice lifecycle, payment collection priority, draft window operations, void behavior, and metadata propagation rules.

## Invoice lifecycle — new subscription

| collection_method | Finalization timing | Draft window? |
|---|---|---|
| `charge_automatically` | Immediately | No |
| `send_invoice` | ~1h after creation | Yes (~1h) |

- First invoice unpaid → invoice `open`, `auto_advance=false`, subscription `incomplete`
- Upgrade/downgrade also creates new invoice with `auto_advance=false`
- **`billing_mode=flexible` + metered-only items**: no invoice at creation — sub goes active immediately. Invoice only generated if backdated (prior usage) or pending items exist.

## Invoice lifecycle — renewals

1. Subscription renews → invoice created with `status=draft`
2. `invoice.created` webhook fires
3. ~1h draft window (editable, add items)
4. Finalized → payment attempted
5. Payment succeeds → `status=paid`

## Saved-default payment method fallback

For invoice collection, Stripe uses the first available saved default in this order; accepted payment method **types** are configured separately with `payment_settings.payment_method_types`:

| Priority | Saved default | API field |
|---|---|---|
| 1 | Invoice | `invoice.default_payment_method` |
| 2 | Subscription | `subscription.default_payment_method` |
| 3 | Customer or customer-configured Account | `customer.invoice_settings.default_payment_method` or `configuration.customer.billing.default_payment_method`, respectively |
| 4 | Legacy customer source | `customer.default_source` |

See [[source-stripe-subscriptions-invoices]] (2026-11-07 capture, lines 62–71) for the fallback and [[source-stripe-subscriptions-payment-methods-setting]] for accepted types.

## Working with the draft window

After `invoice.created`, you have ~1h to modify the draft:

```js
// Add item to specific draft invoice
stripe.invoiceItems.create({ invoice: draftInvoiceId, pricing: { price: priceId }, customer: customerId })

// Without invoice param → pending item (applied to NEXT period)
stripe.invoiceItems.create({ customer: customerId, pricing: { price: priceId } })
```

**Pause for review**: set `auto_advance=false` within one hour of `invoice.created` to prevent automatic payment attempts and invoice emailing while reviewing. Resume automatic collection with `auto_advance=true`. The cited invoice-guide passage does not expressly establish a finalization outcome; see [[source-stripe-subscriptions-invoices]] (2026-05-13 lines 234–242; 2026-11-07 lines 263–271).

**Max 250 invoice items** per invoice.

## Getting a draft window on `charge_automatically` subscriptions

Since the first invoice finalizes immediately, use one of:
- `trial_end` set a few seconds in future → $0 first invoice, then real invoice has ~1h draft
- Create via subscription schedule → initial status `active` with ~1h draft invoice

## Adding charges to invoices

| Method | When applied |
|---|---|
| `invoiceItems.create({ customer })` | Next invoice (pending) |
| `invoiceItems.create({ invoice: draftId })` | Specific draft invoice |
| `add_invoice_items` on `subscriptions.create` | First invoice only |
| `pending_invoice_item_interval` on subscription | Recurring one-off invoices on schedule |

## Voiding invoices

### First invoice void

| Subscription was | After void |
|---|---|
| `incomplete` | → `incomplete_expired` |
| `past_due` | → `active` |
| `active` | No change |

### Most recent non-first invoice void

Stripe walks invoices newest → oldest until a condition matches:
- `paid` or `uncollectible` found → subscription → `active`
- `charge_automatically` + dunning exhausted → `canceled`/`unpaid`/`past_due`
- `send_invoice` + past due date → `past_due`
- No match found → subscription → `active`

## Metadata propagation

| Location | Value |
|---|---|
| `invoice.subscription_details.metadata` | Contains subscription metadata from invoice creation, even if subscription metadata changes later; see [[source-stripe-subscriptions-invoices]] (2026-05-13 line 280; 2026-11-07 line 309) |
| Line items `parent.type=subscription_item_details` | **Most recent** subscription metadata at retrieval time |
| Line items `parent.type=invoice_item_details` | No subscription metadata |

Updating line item metadata directly does NOT preserve inherited subscription metadata — must set explicitly.

Subscription item metadata is not propagated to any other objects automatically.

## Per-subscription payment method settings

`payment_settings.payment_method_types` limits allowed **types**, not the identity of a saved default method. An explicit subscription list overrides Invoice default type configuration for that subscription and passes to its SetupIntent and invoices. With `send_invoice`, customers choose eligible types on the Hosted Invoice Page; with `charge_automatically`, Stripe attempts payment without first showing a selector. Eligibility also depends on account activation, currency, amount, country, collection method, and product support. [[source-stripe-subscriptions-payment-methods-setting]]

**Pitfall**: when an applicable default payment method exists, include its **type** in an explicit `payment_method_types` list; otherwise that default method cannot pay the subscription's invoices. This type allowance is separate from the priority of an individual saved method. [[source-stripe-subscriptions-payment-methods-setting]]

**`save_default_payment_method`**: when enabled, whatever PM the customer pays with becomes the new subscription default.

**Payment update links (May 2026 capture)**: the Dashboard guide described links for automatically billed `active`, `past_due`, or `trialing` subscriptions; card-only, one use, 30-day expiry. They update the associated subscription's method, not the customer's default. The November type-settings guide does not address link availability. [[source-stripe-subscriptions-payment-methods-setting]]

## payment_behavior options

| Value | Behavior |
|---|---|
| `allow_incomplete` | Immediately attempts payment on create; → `incomplete` if fails |
| `default_incomplete` | Always `incomplete` if invoice requires payment; confirm PaymentIntent separately |

Both: → `active` after first invoice paid. **23-hour rule**: first invoice unpaid after 23h → `incomplete_expired` (final, irreversible — voids open invoice, blocks future invoices).

## Failed payment status flows

- **`charge_automatically` recurring failure**: subscription → `past_due`; PaymentIntent → `requires_payment_method` or `requires_action`. After retries exhausted → `canceled` or `unpaid` per Dashboard settings.
- **`incomplete` restrictions**: can only update `metadata`, `save_default_payment_method`, `description` — no invoice-affecting changes.
- **`unpaid`**: future invoices still created but left as **drafts**. Can resend past_due invoice or leave closed.
- **Standalone invoice + `auto_advance=false`**: stays `open` indefinitely. With `auto_advance=true`: may → `uncollectible` after retries.

## Preview upcoming invoice

`stripe.invoices.createPreview()` — models changes (price swap, quantity, trial, coupon) before applying. Includes base price, pending items, discounts, customer credit balance.

## Sources

- [[source-stripe-subscriptions-invoices]] — Stripe docs: full subscription invoice guide (lifecycle, payment priority, draft window, void rules, metadata)
- [[source-stripe-billing-collection-method]] — Collection methods: charge_automatically vs send_invoice, payment_behavior options, 23h incomplete_expired rule, unpaid draft behavior
- [[source-stripe-subscriptions-payment-methods-setting]] — Allowed subscription payment method types and invoice eligibility (November 2026); save-default and payment update link details retained as May 2026 evidence
