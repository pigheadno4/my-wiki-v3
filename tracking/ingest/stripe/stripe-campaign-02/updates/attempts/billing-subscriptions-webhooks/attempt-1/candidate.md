---
title: "Stripe — Using Webhooks with Subscriptions"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/webhooks"
raw_files:
  - "stripe-billing-subscriptions-webhooks-2026-11-07.md"
  - "stripe-subscriptions-webhooks-2026.md"
tags: [stripe, subscriptions, webhooks, events, invoice, eventbridge, event-grid]
---

## Overview

Stripe's May 12 and November 7, 2026 captures explain subscription event handling, payment and status monitoring, access decisions, invoice finalization, and optional Amazon EventBridge or Azure Event Grid delivery. Most subscription activity is asynchronous, so the integration needs an event destination and must verify incoming Stripe events. See [[stripe]] and [[stripe-subscriptions]].

## Key takeaways

- The main subscription-event table names **26 distinct events in both captures**: 2 Customer/Account creation, 6 subscription lifecycle, 1 entitlement, 8 invoice, 2 PaymentIntent, and 7 subscription-schedule events. Use `customer.subscription.*` for subscription tracking whether customers are represented by Customer objects or Accounts v2. The November capture says Accounts v2 is GA for Connect users and public preview for other Stripe users; it does not establish account-specific eligibility.
- The November capture adds a **separate four-row risk/customer-data table**: `charge.refunded`, `charge.dispute.created`, `radar.early_fraud_warning.created`, and `customer.updated`. It directs production integrations that accept payments to handle the three risk events, and integrations storing Customer data locally or depending on Customer fields to handle `customer.updated`. For Accounts v2 customer representation, it names `v2.core.account[configuration.customer].updated` and `v2.core.account[identity].updated` for the distinct configuration and identity changes. Subscribe to the events the integration requires.
- For a risk event associated with a subscription, the November guide gives an **API-version-dependent lookup**, not an unconditional event-to-subscription mapping. On `2025-03-31.basil` or later, obtain a PaymentIntent ID from the event object or its Charge; list `paid` InvoicePayments filtered by `payment.type=payment_intent` and `payment.payment_intent`; paginate all results; retrieve each Invoice and require `parent.type=subscription_details` before reading `parent.subscription_details.subscription`. A null PaymentIntent, no matching paid InvoicePayments, or an Invoice with another parent type leaves that route unresolved. Earlier versions use the Charge's nullable `invoice`, then the Invoice's `subscription`. The captured guide supplies no universal fallback for an unresolved route.
- For the access-expiration pattern, the May capture advanced the timestamp after `invoice.paid`. The November capture adds a required check: retrieve the associated subscription and confirm `status=active` **before** extending access. One paid invoice can leave the subscription non-active under all-invoices status resolution. `invoice.upcoming` can precede an automatically charged renewal, but Stripe says it is not sent with `collection_method=send_invoice`.
- The November status table makes `past_due` and `unpaid` recovery depend on Dashboard status resolution. With most-recent-invoice resolution, settling the most recent non-voided invoice or marking it uncollectible can reactivate; with all-invoices resolution, settle all applicable outstanding invoices. `past_due` does not guarantee another retry. `active` does not prove every associated historical invoice is paid. Continue monitoring `customer.subscription.trial_will_end`, `past_due`, `canceled` and `unpaid` transitions; the guide suggests verifying a payment method before trial end, notifying on `past_due`, and revoking access on `canceled` or `unpaid`.

> [!warning] Contradiction
> The November capture repeats `invoice.payment_failed` with incompatible blanket PaymentIntent and subscription states: `requires_action` and first-invoice-only `incomplete` in its main table, `requires_payment_method` and unqualified `incomplete` in its payment-failure table, then `requires_action` and unqualified `incomplete` in its additional-action table. These rows do not establish one universal transition. Keep first-invoice and actual payment-state conditions when handling failures. Its invoice-finalization section also refers to an invoice `subscription` property without an API-version qualification, while its new post-Basil risk lookup specifies `parent.subscription_details.subscription`; use the version-qualified route above.

## Invoice finalization and delivery

An unsuccessful response to `invoice.created` can delay automatic finalization of **all invoices with automatic collection for up to 72 hours**, except invoices with a custom scheduled finalization time. Stripe includes account endpoints and connected platforms' endpoints in this response condition, but excludes organization endpoints; a successful organization-level response does not affect automatic finalization. Subscription updates that synchronously attempt payment, including initial invoices and some updates, do not incur this delay. The guide says Stripe waits one hour after a successful `invoice.created` response before attempting payment and otherwise attempts finalization and sending after 72 hours. In live mode it describes retries for up to three days, versus three retries over a few hours in a sandbox. These are captured guide statements, not a test of a particular endpoint.

`invoice.finalization_failed` prevents collection on an unfinalized invoice even while a subscription may remain active and the customer may retain access. Inspect `last_finalization_error`; for Stripe Tax, `automatic_tax.status=requires_location_inputs` calls for customer location details, while `failed` calls for retry later. Listen for the failure event and act on the failed invoice.

Stripe also documents AWS EventBridge and Azure Event Grid destinations. Test a webhook or destination with sandbox actions that trigger events, Stripe CLI, or Stripe for Visual Studio Code.

## Detail locators

- November 2026 main event table and Customer/Accounts v2 boundary: [[raw/stripe-billing-subscriptions-webhooks-2026-11-07|November guide]], lines 20–71; separate risk/customer-data table, lines 73–86.
- November risk-event subscription lookup: same raw, lines 120–142; access gate, lines 144–158; status table, lines 160–185.
- November automatic finalization, endpoint boundary, failure, and testing: same raw, lines 187–243.
- May 2026 main table, access pattern, status table, and finalization: [[raw/stripe-subscriptions-webhooks-2026|May guide]], lines 19–71, 106–189.

## Related

- [[stripe-subscriptions]] — subscription lifecycle and access context.

## Raw Sources

- [[raw/stripe-billing-subscriptions-webhooks-2026-11-07|Stripe subscription webhooks guide, 2026-11-07]]
- [[raw/stripe-subscriptions-webhooks-2026|Stripe subscription webhooks guide, 2026-05-12]]
