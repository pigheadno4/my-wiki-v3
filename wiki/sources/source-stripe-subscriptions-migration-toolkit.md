---
title: "Stripe — Billing Migration Toolkit"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit"
raw_files:
  - "stripe-billing-subscriptions-import-subscriptions-toolkit-2026-11-07.md"
  - "stripe-subscriptions-migration-toolkit-2026.md"
tags: [stripe, subscriptions, migration, billing-toolkit, csv, subscription-schedule, pan-import]
---

## Overview

Stripe's Dashboard Billing migration toolkit imports subscription data from a third-party, home-grown, or another Stripe account through CSV and creates scheduled Stripe subscriptions. The page describes preparation, validation, migration timing, and repair paths; an uploaded or scheduled subscription does not prove a payment was collected. See [[stripe]] and [[stripe-subscriptions]].

Set up a Stripe Billing integration before migration. A payments-data import from the prior processor is required only when moving from another processor, not for Stripe-to-Stripe migration. For a third-party or home-grown system, create the new Stripe subscriptions before canceling the old ones, then cancel old subscriptions before their next charge; schedule close billing dates after the last old-system charge. These are the page's timing instructions, not evidence that any migration has run.

## CSV route and defaults

| Template | Recurring-price representation |
| --- | --- |
| Basic | Destination Stripe `customer`, future `start_date`, recurring `price`, and optional quantity/settings |
| Multi-price items | Destination `customer`, future `start_date`, and `items.x.price` with optional quantities |
| Ad-hoc pricing | Destination `customer`, future `start_date`, and recurring `adhoc_items.x` amount, product, interval, and currency |

Choose the template that matches the recurring pricing route; the full specification lists the fields at November raw lines 476–506. The toolkit requires `start_date` at least 24 hours after CSV upload, or at least 1 hour in a sandbox. A past `backdate_start_date` requires `proration_behavior=none`. The worked January 2024 timestamps and the renewal example's "charge immediately" wording do not waive the future upload-time buffer.

> [!warning] Contradiction
> The 2026-05-12 toolkit page says omitted `proration_behavior` defaults to `create_prorations` (May lines 52, 77, 111, 449). The 2026-11-07 same-URL page says an omitted column or blank value defaults to `none` (November lines 57, 89, 127, 497). Use the November toolkit-specific wording for this CSV route; do not apply it to the separate Subscription Schedule API's top-level or per-phase defaults. The November past-due-cycle example explicitly sets `create_prorations` for a prorated invoice and possible dunning if unpaid (lines 377–383).

The optional `add_invoice_items.0.amount`, `.product`, and `.currency` fields add a **one-time extra** in major currency units. They are separate from recurring `adhoc_items`. Omit or leave all three blank for a recurring-only import; copying the recurring amount into the one-time field requests a second charge. The November 9.99 + 9.99 = 19.98 illustration is before taxes, discounts, or credits (lines 504–510).

> [!warning] Contradiction
> Both captures' Basic add-on example says the extra fee is **20 USD** in prose (May line 255; November line 316), but the `add_invoice_items.0.amount` CSV row contains **50** (May line 260; November line 320). The November field definition makes that a one-time amount in major units. Reconcile the intended amount and valid template before reusing the row; it is not a verified 20 USD upload example. Some other sample rows are also column-misaligned, so use the full specification and current template for exact headers.

For Stripe-to-Stripe migration, the Customer, Price, and any Coupon or Tax IDs must belong to the destination account. The older source summary wrote `metadata.source`; the November full specification writes `metadata_source` while template prose also uses `metadata.source`. The exact accepted CSV header is unresolved in these captures; do not silently normalize it in an upload template. See November lines 431–442, 474, and 491.

## Payment source and collection

The November Advanced setting **Allow subscriptions without a default payment source** is unchecked by default. This blocks `charge_automatically` rows whose customer lacks a default source. `send_invoice` rows are exempt from that check and require customer email and `days_until_due`; an emailed invoice or an active subscription status does not establish payment. If the setting is checked, rows without a default source can import, but their invoices will fail to collect at billing time unless a default is set before the first billing date. This scoped validation qualifies the broad "all customers" wording in the CSV prerequisites table. See November lines 153–163, 465–467, 498, and 502.

On a missing-source error, download the error file, inspect `processing_error`, set a default for each affected customer, and upload the revised CSV. An already attached method can be made the default; the page gives Dashboard steps and an API update using `invoice_settings[default_payment_method]`. For data from another processor, the PAN import may need to finish first. See November lines 238–286.

## Tax and other constraints

> [!warning] Contradiction
> The May 2026 external-tax example said blank `automatic_tax` and `default_tax_rate` fields would automatically follow the configured Billing tax integration after go-live (May lines 362–366). The November 2026 toolkit guidance says blanks **do not enable automatic tax for future invoices**. For a configured third-party tax app, it says set `automatic_tax=true` on the migrated subscription; installing or selecting the app alone is insufficient (November lines 412–416, 493). This is documented toolkit guidance, not an observed tax calculation.

Stripe Tax's automatic calculation path requires customer location data, and `default_tax_rate` is incompatible with `automatic_tax`. The toolkit supports one coupon per subscription. With a future anchor and `proration_behavior=none`, updating the schedule or subscription can unset the coupon and requires reapplying it. See November lines 59, 420, 460–474, and 499.

## Timing, review, and limits

The CSV upload limit is 120 MB. The toolkit validates the file, then presents a summary to review before **Start migration**. It creates Subscription Schedules and retains a 24-hour pre-live buffer, reduced to 1 hour in a sandbox. A scheduled subscription cannot be edited in the toolkit or canceled by a customer in the portal; the page routes edits to the schedule API or Dashboard. The toolkit's **Cancel migration** action is available for 10 hours after scheduling; afterward use the schedule cancel endpoint or cancel individual subscriptions in the Dashboard. Monitor invoices, payment methods, charge dates, and amounts after go-live. See November lines 147–202 and 220–225.

Validation errors include invalid dates, too-early `start_date`, missing required fields, tax/price incompatibility, and missing default payment source for `charge_automatically`. Correct the `processing_error` rows and re-upload. The guide's sample rows and status descriptions are not receipts for a successful charge, tax calculation, or account eligibility.

## Related

- [[stripe-subscriptions]] — subscription concept and toolkit route
- [[stripe-subscriptions-schedules]] — schedule behavior and distinct API proration defaults
- [[source-stripe-subscriptions-migration]] — migration overview

## Raw Sources

- [[raw/stripe-billing-subscriptions-import-subscriptions-toolkit-2026-11-07|Billing migration toolkit, captured 2026-11-07]]
- [[raw/stripe-subscriptions-migration-toolkit-2026|Billing migration toolkit, captured 2026-05-12]]
