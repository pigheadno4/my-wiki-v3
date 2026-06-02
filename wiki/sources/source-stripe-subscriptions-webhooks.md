---
title: "Stripe — Using Webhooks with Subscriptions"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-webhooks-2026.md"
tags: [stripe, subscriptions, webhooks, events, invoice, eventbridge, event-grid]
---

## Summary

Complete subscription webhook event reference (22 events). Covers status tracking patterns, the critical `invoice.created` 72-hour delay risk, active subscription access expiration pattern, and EventBridge/Event Grid routing.

## 22 Subscription Webhook Events

**Customer/Account**: `v2.core.account.created`, `customer.created`

**Subscription lifecycle**: `customer.subscription.created/deleted/paused/resumed/trial_will_end/updated`

**Entitlements**: `entitlements.active_entitlement_summary.updated`

**Invoice**: `invoice.created/finalized/finalization_failed/paid/payment_action_required/payment_failed/upcoming/updated`

**PaymentIntent**: `payment_intent.created/succeeded`

**Subscription Schedule**: `subscription_schedule.aborted/canceled/completed/created/expiring/released/updated`

**Note**: use `customer.subscription.*` events regardless of Accounts v2 or Customer v1.

## Critical: `invoice.created` 72-Hour Risk

If Stripe fails to receive success response to `invoice.created` → delays finalizing all auto-collection invoices **up to 72 hours**.

## Active Subscription Access Pattern

Store access expiration timestamp. On `invoice.paid` → extend timestamp. For auto-charge: first receive `invoice.upcoming` (a few days before renewal) for adding extra items.

## Status Transition Actions

- `trial_will_end` (3 days before) → verify payment method, optionally notify customer
- `past_due` → notify customer directly, prompt PM update
- `canceled`/`unpaid` → revoke access

## EventBridge / Event Grid

Can route Stripe events directly to AWS EventBridge or Azure Event Grid instead of webhook endpoint.

## Related Pages

- [[stripe-subscriptions]] — concept page

## Raw Sources

- [[stripe-subscriptions-webhooks-2026]] — verbatim subscription webhooks guide (201 lines)
