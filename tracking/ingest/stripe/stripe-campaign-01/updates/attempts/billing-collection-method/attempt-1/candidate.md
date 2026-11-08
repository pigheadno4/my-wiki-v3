---
title: "Stripe Billing — Collection Methods"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/collection-method"
raw_files:
  - "stripe-billing-collection-method-2026-11-07.md"
  - "stripe-billing-collection-method-2026.md"
tags: [stripe, billing, invoices, subscriptions, collection-method, payment-behavior, dunning]
---

## Overview

Stripe's Billing collection-method guide describes `charge_automatically` and `send_invoice` for invoices and subscriptions. The Dashboard can set the preference when creating either product; the Invoicing and Subscriptions APIs expose `collection_method`. The 2026-11-07 capture documents the same behavior as the 2026-05-13 capture; no substantive product change is evidenced by this comparison.

## Two collection methods

| Value | Guide's behavior |
| --- | --- |
| `charge_automatically` | Attempts to charge the customer's default payment method for an invoice or each subscription billing-period invoice. |
| `send_invoice` | Sends or generates an invoice for manual payment, with an adjustable payment window; the hosted invoice page and email reminders can facilitate payment. |

Some methods, including bank transfers, only support `send_invoice` and cannot be charged automatically. Changing a subscription's `collection_method` affects only subsequently created subscription invoices.

## Free trial with `charge_automatically`

The guide permits creating a free trial without collecting a payment method while setting `collection_method=charge_automatically`. The customer can add payment details through the Customer portal during the trial. After the trial, Stripe charges the customer's default payment method; if no payment method was added, configured subscription behavior can instead pause or cancel the subscription.

## `send_invoice` due dates

A manual-payment invoice can have a configured due date and up to three reminders, from 10 days before to 60 days after that date. For a past-due subscription invoice, settings allow an action at 30, 60, or 90 days: cancel, mark unpaid, or leave past due. The selected action determines later status and invoice handling; see the dated raw table.

## Subscription creation and first payment

| `payment_behavior` | Guide's stated condition and result |
| --- | --- |
| `allow_incomplete` | With `collection_method=charge_automatically`, immediately attempts payment; an unsuccessful initial attempt marks the subscription `incomplete`. |
| `default_incomplete` | If the first invoice requires payment, initializes as `incomplete`; confirm the resulting PaymentIntent in a separate request to attempt payment. |

For either behavior, payment of the first invoice makes the subscription `active`. A subscription requiring no payment at creation, such as a trial, is immediately `active`. If the first invoice remains unpaid after 23 hours, `incomplete_expired` is final and irreversible: the open invoice is voided and future invoices are prevented.

## Failed payment status flows

### Recurring automatic charges

A failed recurring payment or one requiring customer authentication sets the subscription to `past_due`, with the PaymentIntent at `requires_payment_method` or `requires_action`. The guide recommends listening for `customer.subscription.updated` and collecting a different payment method or customer action as appropriate. After successful payment, the subscription is `active` and invoice `paid`.

If an automatically charged renewal payment fails, the subscription becomes `past_due`. After retries are exhausted, Stripe **might** mark it `canceled` or `unpaid`, depending on subscription settings. This is a possible later outcome, not an inevitable transition.

### Incomplete subscription restrictions

While a subscription is `incomplete`, only attributes whose updates do not create an invoice or invoice item can be changed. The guide gives `metadata`, `save_default_payment_method`, and `description` as examples, not an exhaustive allowlist.

### Manual-payment subscriptions and unpaid status

With `send_invoice`, the subscription becomes `past_due` if its invoice remains unpaid by the due date. After an extended deadline, Stripe might mark it `canceled` or `unpaid`, depending on settings. An `unpaid` subscription still produces future invoices as drafts; the guide describes resending past-due and draft invoices to collect payment or leaving them closed and unpaid.

### Standalone invoice failures

| Condition | Guide's stated outcome |
| --- | --- |
| Standalone invoice with `charge_automatically`, auto-advancement disabled, and failed initial attempt | Remains `open`; while auto-advancement is disabled, Stripe does not automatically close, retry, or transition it. |
| Invoice with auto-advancement enabled | Stripe might mark it `uncollectible` after retry exhaustion, depending on invoice-status settings. |
| `send_invoice` invoice unpaid past due date | Becomes `past_due`; after an extended deadline, it may be left past due or changed to `uncollectible` or `void`. |

## Enterprise clients and wire transfers

The guide describes tracking and reconciliation advantages of manual methods such as wire transfers for high-volume enterprise clients. It calls wire transfer a commonly preferred method for this type of client and says `send_invoice` can generate well-documented invoices payable by wire transfer. It does not make a universal enterprise recommendation or guarantee an audit trail.

## Detail locators

The 2026-11-07 capture covers invoice and subscription method settings (lines 9–36), manual due dates and actions (38–48), first-payment behavior (54–60), recurring and incomplete-subscription outcomes (62–90), standalone invoice outcomes (92–98), and enterprise wire transfers (100–102). The 2026-05-13 capture preserves the corresponding historical text at lines 8–35, 37–47, 53–59, 61–89, 91–97, and 99–101. These captures do not establish current account-specific payment-method eligibility, Dashboard settings, or a successful payment, invoice delivery, finalization, or settlement.

## Related

- [[stripe-subscriptions-invoices]] — subscription invoice lifecycle and payment priority
- [[stripe-subscriptions]] — subscription concept and related sources
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-collection-method-2026-11-07|Stripe Billing collection-method guide, captured 2026-11-07]]
- [[raw/stripe-billing-collection-method-2026|Stripe Billing collection-method guide, captured 2026-05-13]]
