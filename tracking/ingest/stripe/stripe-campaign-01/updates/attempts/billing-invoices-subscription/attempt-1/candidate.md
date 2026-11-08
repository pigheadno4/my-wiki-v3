---
title: "Stripe Subscriptions — Subscription Invoices"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/invoices/subscription"
raw_files:
  - "stripe-billing-invoices-subscription-2026-11-07.md"
  - "stripe-subscriptions-invoices-2026.md"
tags: [stripe, billing, subscriptions, invoices, payment-collection, draft-invoice, metadata]
---

## Summary

Stripe's subscription-invoice guide covers first invoices, renewals, saved-default payment-method fallback, draft invoice changes, voiding, and metadata propagation. The 2026-11-07 capture adds preview-qualified finalized-invoice editing, customer-configured Account payment-method fallback, optional saving of a successful payment method, Dashboard payment-update links, and API-version-specific subscription expansion.

## Lifecycle — new subscription invoices

- `charge_automatically` → invoice finalized immediately; payment attempted immediately.
- `send_invoice` → invoice finalized about one hour after creation; emailed to the customer.
- Until payment succeeds, the first invoice is `open` with `auto_advance=false`, and the subscription is `incomplete`. If payment succeeds or no payment is required, the invoice becomes `paid` and the subscription becomes `active`.
- Upgrade/downgrade invoices can also be created with `auto_advance=false` from the outset.
- **`billing_mode=flexible` with metered-only items**: no invoice at creation, and the subscription becomes active immediately, except when backdated accrued usage or pending invoice items exist.
- Ordinarily, a finalized invoice cannot receive invoice items or other changes affecting the amount due; new customer invoice items apply to the next invoice.

### Finalized-invoice editing preview (2026-11-07)

The November page labels the ability to edit finalized subscription invoices **preview** and offers a registration example. It does not establish account eligibility or which revisions an enrolled account can make. The ordinary post-finalization amount restriction above remains the stated general rule. See new raw lines 30–42.

## Lifecycle — renewal invoices

1. Invoice created → status `draft` → `invoice.created` event fires.
2. About one hour of draft editing.
3. Stripe attempts finalization and payment with the saved default payment method.
4. If payment succeeds, invoice status becomes `paid`.

## Saved-default payment method fallback (2026-11-07)

When collecting an invoice payment, Stripe uses the first available saved method in this order:

| Priority | Saved default | API attribute |
|---|---|---|
| 1 | Invoice | `invoice.default_payment_method` |
| 2 | Subscription | `subscription.default_payment_method` |
| 3 | Customer or customer-configured Account | `customer.invoice_settings.default_payment_method` or `configuration.customer.billing.default_payment_method`, respectively |
| 4 | Legacy customer source | `customer.default_source` |

This fallback order differs from `payment_settings.payment_method_types`, which controls the payment method **types** a subscription's invoices can accept. A subscription can explicitly set `default_payment_method` or legacy `default_source`. See new raw lines 62–71; the May capture's third fallback listed the Customer field alone (old lines 51–58).

Set `payment_settings.save_default_payment_method=on_subscription` to save the method from a **successful subscription payment** as `subscription.default_payment_method`. It defaults to `off` and is separate from the Dashboard **Save customer payment information** setting. See new raw lines 73–77.

### Dashboard payment-update links (2026-11-07)

The Dashboard can generate a single-use payment-update link for a subscription with Billing set to `Auto`, not `Send`. It changes only that associated subscription's payment method, not the customer default. The subscription must be `active`, `past_due`, or `trialing`; the new method must be a card. Each link works once and expires after 30 days if unused. The Dashboard can deactivate a subscription's existing links. These are documented link constraints, not evidence of eligibility for any particular account. See new raw lines 79–98.

## Draft window usage

During the approximately one-hour draft period after `invoice.created`:
- Add items with an invoice item create request specifying `invoice` for that draft invoice.
- Omitting the `invoice` parameter makes the item pending for a future invoice instead.
- Up to 250 invoice items can be added to an invoice.

**Pause for review**: within one hour of `invoice.created`, set `auto_advance=false` to prevent automatic payment attempts and emailing while reviewing; resume automatic collection with `auto_advance=true` when ready. The cited passage does not separately establish whether finalization is prevented (old lines 234–242; new lines 263–271).

## First invoice edit window

| `collection_method` | Draft window? | Documented way to obtain a draft window |
|---|---|---|
| `send_invoice` | About one hour | Already present |
| `charge_automatically` | No; first invoice finalizes immediately | Set `trial_end` several seconds ahead, or create through a subscription schedule |

The `trial_end` example generates a zero-amount first invoice; a later nonzero invoice has an approximately one-hour draft period. The schedule example also yields a first invoice with a one-hour draft period. These are documented paths, not a guarantee of payment outcome. See new raw lines 164–185.

## Adding items to invoices

- **Future invoice**: create an invoice item for a customer; the item goes to the next invoice. The optional `subscription` parameter targets a specific subscription.
- **First invoice one-time charge**: use `add_invoice_items` on subscription creation.
- **Draft invoice**: create an invoice item with the `invoice` parameter to attach it to that invoice.
- **Recurring pending items**: `pending_invoice_item_interval` creates recurring one-off invoices for pending items.
- Pending invoice items can still cause invoicing and a billing attempt after subscription cancellation. They are not prorated on a subscription change.
- A manually generated one-off invoice does not automatically inherit subscription tax rates; add applicable tax rates explicitly.

The 2026-05-13 capture renders the invoice-item, invoice-create, and subscription-create examples in Node SDK form (old lines 88–115, 152–167, 181–204). The 2026-11-07 capture renders corresponding examples as curl (new lines 145–162, 199–208, 222–235). The format change does not establish SDK deprecation.

## Retrieve the full subscription from an invoice (2026-11-07)

Retrieving an invoice returns the Subscription ID by default. To expand the full Subscription object, use `expand[]=parent.subscription_details.subscription` on **API version 2025-03-31.basil or later**; on earlier API versions, use `expand[]=subscription`. See new raw lines 125–143.

## Voiding invoices

### Void first invoice

| Subscription status | Result after void |
|---|---|
| `incomplete` | `incomplete_expired` |
| `past_due` | `active` |
| `active` | No change |

### Void most recent invoice (non-first)

Stripe walks back through invoices from most recent to oldest:
- First `paid` or `uncollectible` invoice → subscription `active`.
- `charge_automatically` with dunning stopped after retry limits → `canceled`, `unpaid`, or `past_due` according to automatic collection settings.
- `send_invoice` past the due date → `past_due`.
- If none match → `active`.

See old raw lines 255–274 and new raw lines 284–303.

## Metadata propagation

| Location | Behavior |
|---|---|
| `invoice.subscription_details.metadata` | Contains subscription metadata from invoice creation, even if subscription metadata changes later |
| Invoice line items with `parent.type=subscription_item_details` | Reflect most recent subscription metadata when the invoice is retrieved |
| Invoice line items with `parent.type=invoice_item_details` | Do not carry subscription metadata |

Direct line-item metadata updates replace the line item's metadata declaration; inherited subscription metadata is not preserved implicitly. Subscription item metadata does not propagate automatically to other Stripe objects. See old raw lines 276–286 and new raw lines 305–315.

## Historical Accounts v2 note (2026-05-13)

The May capture instructs integrations using customer-configured Accounts to replace `Customer` and event references in its code examples with equivalent Accounts v2 API references (old line 8). The November capture omits that broader instruction but explicitly includes a customer-configured Account default-payment-method field in fallback position 3 (new line 68). Omission alone does not establish withdrawal of the May guidance; verify current Accounts v2 mappings with dedicated authority before applying them.

## Related pages

- [[stripe-subscriptions-invoices]] — concept route
- [[stripe-subscriptions]] — subscription concept
- [[stripe-subscriptions-prorations]] — proration behavior
- [[source-stripe-subscriptions-payment-methods-setting]] — accepted payment method types and payment-update-link context
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-invoices-subscription-2026-11-07|2026-11-07 Stripe subscription invoices capture]]
- [[raw/stripe-subscriptions-invoices-2026|2026-05-13 Stripe subscription invoices capture]]
