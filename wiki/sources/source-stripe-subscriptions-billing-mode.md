---
title: "Stripe — Flexible Billing Mode for Subscriptions"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/billing-mode"
raw_files:
  - "stripe-billing-subscriptions-billing-mode-2026-11-07.md"
  - "stripe-subscriptions-billing-mode-2026.md"
tags: [stripe, subscriptions, flexible-billing, billing-mode, proration-discounts, api-version]
---

## Overview

Stripe's subscription billing mode guide documents the `classic` and `flexible` modes, their version-dependent defaults, creation and migration routes, and proration discount display. The 2026-11-07 capture expands the post-migration and subscription-schedule guidance. The 2026-05-13 capture remains historical evidence for the already documented default and prospective-migration rules. [[stripe-subscriptions]] is the central concept; [[stripe]] is the company route.

## Key facts

- Flexible is recommended for new Billing users, but not required. Classic remains for backward compatibility. A subscription cannot be migrated from flexible back to classic.
- When an API request omits `billing_mode`, the guide documents `flexible` for `2025-08-27.preview` and later preview versions, or `2025-09-30.clover` GA and later GA versions; all other API versions default to `classic`. Upgrading to the cited GA version changes the default for new subscriptions, so integrations that need classic must set it explicitly.
- Dashboard creation or classic-to-flexible updating is described as possible regardless of the integration API version; full modification in the API requires `2025-06-30.basil` or later. The Dashboard default setting governs new Dashboard-created subscriptions and Dashboard-generated Payment Links and Pricing Tables, not API-created subscriptions or migrations. API-version default logic separately governs subscriptions from API-created Payment Links and Pricing Tables. The guide's general basil prerequisite should be read with this Dashboard/full-API distinction.
- Flexible billing can be selected on subscription creation or through the `/v1/subscriptions/{id}/migrate` API for an existing classic subscription. The May Node and November curl examples are dated examples, not evidence of a performed migration. The guide also points to Checkout Sessions, Subscription Schedules, and Quotes as creation routes.
- Migration changes behavior only for new activity. Pre-migration resources, including pending proration invoice items, are not recalculated. The November guide adds that credit prorations use the original debited amount, usage-based billing uses the price effective when usage was reported, and the billing cycle anchor is never automatically reset.
- For a subscription with an active schedule, the November guide directs migration through the migrate API; the Dashboard does not support this case, and API migration updates the schedule's `billing_mode` automatically. An unstarted schedule with no active subscription cannot be migrated; cancel and recreate it with `billing_mode` set to `flexible`. When creating a schedule with `from_subscription`, omit `billing_mode` if the subscription already has one: the schedule inherits it, and specifying it produces an error.
- For flexible subscriptions, `proration_discounts=itemized` (recommended) displays gross proration amounts and discount amounts; `included` preserves the older net-amount, zero-discount-amount display. Setting itemized requires API version `2025-06-30.basil` or later and a create or migrate route.

## Detail locators

- Two modes, recommendation, nonmandatory adoption, and one-way migration: November raw lines 9–24; May raw lines 8–23.
- Dashboard versus API version authority and defaults: November lines 28–69; May lines 27–68. For Dashboard creation, the November editor places Billing mode under **Billing and payment collection** (lines 41–46); for Dashboard migration, under **Advanced settings** (lines 520–523). The May UI steps differ (lines 40–45 and 498–501).
- Dated creation request and response examples: November lines 71–510 (curl); May lines 70–488 (Node). The illustrated subscription remains incomplete, its invoice open, and its PaymentIntent requires confirmation (November lines 431, 447, 498); the example proves no successful payment.
- Migration route, prospective effect, and expanded consequences: November lines 512–570; May lines 490–536. Both captures describe the prospective/no-recalculation boundary. Both also say `billing_mode.updated_at` in migration prose while labeling the response example `billing_mode_details.updated_at` (November lines 529 and 541–549; May lines 507 and 525–535). That inconsistency does not establish a response-field contract.
- Active and unstarted schedule cases, plus inheritance and `from_subscription` error: November lines 572–578; May line 540 covers the inheritance/error case only.
- Itemized versus included proration discount display and API floor: November lines 580–603; May lines 542–578.

## Related

- [[stripe-subscriptions]] — central subscriptions concept
- [[source-stripe-subscriptions-billing-mode-compare]] — mode comparison
- [[source-stripe-subscriptions-mixed-interval]] — mixed intervals
- [[stripe]] — company

## Raw Sources

- [[raw/stripe-billing-subscriptions-billing-mode-2026-11-07|Stripe billing mode guide, captured 2026-11-07]] — complete guide, 1023 lines
- [[raw/stripe-subscriptions-billing-mode-2026|Stripe billing mode guide, captured 2026-05-13]] — prior complete guide, 966 lines
