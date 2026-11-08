---
title: "Stripe Subscriptions — Subscription Invoices"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-invoices-2026.md"
tags: [stripe, billing, subscriptions, invoices, payment-collection, draft-invoice, metadata]
---

## Summary

Comprehensive guide to how Stripe generates and manages subscription invoices across the subscription lifecycle: new subscription, renewals, payment collection priority, draft window usage, voiding, and metadata propagation.

## Lifecycle — new subscription invoices

- `charge_automatically` → invoice finalized immediately; payment attempted immediately
- `send_invoice` → invoice finalized ~1h after creation; emailed to customer
- First invoice unpaid → invoice `open`, `auto_advance=false`, subscription `incomplete`
- Upgrade/downgrade invoices also get `auto_advance=false` from the outset
- **`billing_mode=flexible` + metered-only**: no invoice at subscription creation — sub becomes active immediately. Invoice generated only if backdated (accrued usage) or pending items exist.

## Lifecycle — renewal invoices

1. Invoice created → status `draft` → `invoice.created` event fires
2. ~1h draft window (editable)
3. Finalized → payment attempted
4. If paid → status `paid`

## Payment method priority (4 levels)

| Priority | Source | API attribute |
|---|---|---|
| 1 | Invoice default PM | `invoice.default_payment_method` |
| 2 | Subscription default PM | `subscription.default_payment_method` |
| 3 | Customer invoice default PM | `customer.invoice_settings.default_payment_method` |
| 4 | (Legacy) Customer default source | `customer.default_source` |

## Draft window usage

During the ~1h draft period after `invoice.created`:
- Add items with `stripe.invoiceItems.create({ invoice: draftInvoiceId, ... })`
- Omitting `invoice` param → pending items (applied to next period instead)
- Max 250 invoice items per invoice

**Pausing for review**: set `auto_advance=false` within 1h of `invoice.created`. Resume with `auto_advance=true` when ready.

## First invoice edit window

| collection_method | Draft window? | Workaround to get draft window |
|---|---|---|
| `send_invoice` | Yes (~1h) | N/A |
| `charge_automatically` | No (finalized immediately) | Use `trial_end` a few seconds in future, or create via subscription schedule |

`trial_end` workaround: generates $0 first invoice, then non-zero invoice has ~1h draft window.

## Adding items to invoices

- **Future invoice**: `stripe.invoiceItems.create({ customer, pricing })` — adds to next invoice (no `invoice` param)
- **First invoice one-time charge**: `add_invoice_items` on `subscriptions.create`
- **Draft invoice**: `stripe.invoiceItems.create({ invoice: draftId, ... })` — attached to that specific invoice
- **Recurring pending items**: `pending_invoice_item_interval` on subscription — Stripe creates one-off invoices on schedule

## Voiding invoices

### Void first invoice

| Subscription status | Result after void |
|---|---|
| `incomplete` | → `incomplete_expired` |
| `past_due` | → `active` |
| `active` | No change |

### Void most recent invoice (non-first)

Stripe walks back through invoices from most recent to oldest:
- First `paid` or `uncollectible` invoice → subscription → `active`
- `charge_automatically` + dunning exhausted → `canceled`/`unpaid`/`past_due` (per auto-collection settings)
- `send_invoice` + past due date → `past_due`
- If none match → subscription → `active`

## Metadata propagation

| Location | Behavior |
|---|---|
| `invoice.subscription_details.metadata` | Snapshot of subscription metadata **at invoice creation time** |
| Invoice line items with `parent.type=subscription_item_details` | Reflects **most recent** subscription metadata at retrieval time (may differ from creation) |
| Invoice line items with `parent.type=invoice_item_details` | Does NOT carry subscription metadata |

Directly updating line item `metadata` via invoice line update endpoint does NOT preserve inherited subscription metadata — must be set explicitly.

Subscription item metadata is NOT propagated automatically to any other Stripe objects.

## Related pages

- [[stripe-subscriptions-invoices]] — concept page
- [[stripe-subscriptions]] — concept page
- [[stripe-subscriptions-prorations]] — proration behavior
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-invoices-2026]] — verbatim Stripe docs webpage
