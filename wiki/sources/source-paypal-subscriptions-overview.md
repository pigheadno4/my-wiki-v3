---
title: "PayPal Subscriptions (Overview)"
type: source
date_ingested: 2026-04-15
original_format: webpage
raw_files:
  - "paypal-subscriptions-overview.md"
  - "paypal-subscriptions-integrate.md"
  - "paypal-subscriptions-customize.md"
  - "paypal-subscriptions-pricing-plans.md"
  - "paypal-subscriptions-billing-cycles.md"
  - "paypal-subscriptions-pause-resume.md"
  - "paypal-subscriptions-revise.md"
  - "paypal-subscriptions-change-quantity.md"
  - "paypal-subscriptions-future-date.md"
  - "paypal-subscriptions-trial-period.md"
  - "paypal-subscriptions-setup-fee.md"
  - "paypal-subscriptions-payment-failure.md"
  - "paypal-subscriptions-multiple-buttons.md"
  - "paypal-subscriptions-update-pricing.md"
  - "paypal-subscriptions-sell-social.md"
  - "paypal-subscriptions-test-golive.md"
  - "paypal-subscriptions-webhooks.md"
tags: [paypal, subscriptions, recurring-payments, billing, plans, products, js-sdk]
---

## Overview

Overview page for PayPal's Subscriptions product — how to bill customers at regular intervals using the Subscriptions REST APIs or the PayPal business account dashboard.

Source URL: <https://developer.paypal.com/docs/subscriptions/>

Last updated: 2025-05-09

## Key Takeaways

### Two integration paths

| Path | Best for |
| --- | --- |
| **Subscriptions REST APIs** | Merchants with their own product UI who want to customize the integration |
| **PayPal business account dashboard** | Merchants who don't need API integration — manage subscriptions through the PayPal dashboard |

### How it works (6 steps)

1. Create a **product** to represent goods or services
2. Create a **plan** to represent payment cycles
3. Use the **JavaScript SDK** to render the PayPal button, which starts the subscription process
4. The buyer agrees and subscribes
5. The button calls the **Subscriptions API** to create the subscription
6. The buyer sees the subscription confirmation

### Billing flexibility

- Fixed amount at regular intervals
- Variable amount based on number of users subscribed
- Volume-based or tier-based pricing
- Free or discounted trials
- Plan upgrade/downgrade support
- Automated payment recovery for failed payments

### Billing cycles

5 options: Day, Week, Month, Year, Custom (via `interval_count` + `interval_unit`).

- **Finite**: `total_cycles: N` — subscription ends after N cycles
- **Infinite**: `total_cycles: 0` — subscription continues until cancelled

## Integration (3-step flow)

1. **Create product** — `POST /v1/catalogs/products` (Catalog Products API); returns `PROD-*` ID
2. **Create plan** — `POST /v1/billing/plans` (Subscriptions API); returns `P-*` plan ID
3. **Add JS SDK button** — `vault=true&intent=subscription` in script tag; `createSubscription` + `onApprove` callbacks

### Plan request example features

- 1-month free trial → 12-month fixed-price ($10/month)
- $10 setup fee; `setup_fee_failure_action: CONTINUE`
- `auto_bill_outstanding: true`; `payment_failure_threshold: 3`
- 10% non-inclusive tax

### Key constraints

- **One currency per plan** — create separate plans for different currencies
- **JS SDK incompatibility**: `onShippingChange`, `onShippingAddressChange`, `onShippingOptionsChange` are **not compatible** with Subscriptions
- Webhooks available: `Subscriptions webhook events` for subscription lifecycle actions

### Test flow

1. Buyer selects PayPal button → logs in with sandbox personal account → Agree & Subscribe
2. Verify subscription in buyer's autopay list: `sandbox.paypal.com/myaccount/autopay/connect/`
3. Verify in merchant account: `sandbox.paypal.com/billing/subscriptions`

## Customization Capabilities (12 total)

| Capability | Description |
| --- | --- |
| Pricing plans | Fixed, quantity/seat-based, volume-based, tiered — see detail below |
| Billing cycles | Frequency + fixed period or open-ended |
| Pause or resume | Soft-cancel (`/suspend`) to reduce churn; resume (`/activate`); balances still recoverable during pause |
| Upgrade or downgrade | `/revise` endpoint; PayPal requires re-consent via HATEOAS URL; card payments do not; new price effective next cycle; no auto-proration |
| Change quantity | Same `/revise` endpoint + `quantity` field; same re-consent rules as plan change; new price next cycle; no auto-proration |
| Future start date | `start_time` on Create Subscription; setup fees charged immediately; start date updatable while still in future |
| Trial period | Up to 2 trial periods per plan; `tenure_type: "TRIAL"` billing cycles ordered by `sequence`; can be $0 or discounted |
| Setup fee | `payment_preferences.setup_fee` on Create Plan; charged before subscription begins; one-time only |
| Payment failure recovery | Retry every 5 days, max 2× per cycle; failed amount → outstanding balance; suspend at threshold; capture via `/capture` with `OUTSTANDING_BALANCE` |
| Multiple buttons | Load SDK once; unique container div per plan (use plan ID as container ID); separate `Buttons().render()` call per plan |
| Update plan pricing | `/update-pricing-schemes` on plan; 10-day notice to existing subscribers; grace period if next cycle within 10 days; supports volume/tiered pricing |
| Sell on social media | No-code: generate link from dashboard; Facebook/Instagram/Twitter/email/SMS; links valid 6 months |

## Pricing Models Detail

| Model | Key field | How price is calculated |
| --- | --- | --- |
| **Fixed** | `fixed_price` | Flat rate per billing cycle |
| **Quantity** | `quantity_supported: true` | Fixed unit price × subscriber-chosen quantity |
| **Volume** | `pricing_model: "VOLUME"` + `quantity_supported: true` | Entire quantity charged at the single tier rate the total quantity falls into |
| **Tiered** | `pricing_model: "TIERED"` + `quantity_supported: true` | Quantity split across tiers; each portion charged at its tier rate |

**Volume vs Tiered — worked example** (14 licenses, tiers: 1-5 @ $15, 6-10 @ $14, 11-15 @ $13):

- Volume: 14 × $13 = **$182** (all units at tier 3 rate)
- Tiered: 5×$15 + 5×$14 + 4×$13 = **$197** (units split across tiers)

**Last tier** has no `ending_quantity` — open-ended "and beyond" pattern.

> [!info] Source typo
> Tiered plan sample has `"starting_quantity": 11"` (missing opening quote) — preserved verbatim in raw file.

## Webhooks (17 events)

| Category | Events |
| --- | --- |
| Product (2) | `CATALOG.PRODUCT.CREATED`, `CATALOG.PRODUCT.UPDATED` |
| Plan (5) | `BILLING.PLAN.CREATED`, `BILLING.PLAN.UPDATED`, `BILLING.PLAN.ACTIVATED`, `BILLING.PLAN.PRICING-CHANGE.ACTIVATED`, `BILLING.PLAN.DEACTIVATED` |
| Payment (3) | `PAYMENT.SALE.COMPLETED`, `PAYMENT.SALE.REFUNDED`, `PAYMENT.SALE.REVERSED` |
| Subscription (7) | `BILLING.SUBSCRIPTION.CREATED`, `BILLING.SUBSCRIPTION.ACTIVATED`, `BILLING.SUBSCRIPTION.UPDATED`, `BILLING.SUBSCRIPTION.EXPIRED`, `BILLING.SUBSCRIPTION.CANCELLED`, `BILLING.SUBSCRIPTION.SUSPENDED`, `BILLING.SUBSCRIPTION.PAYMENT.FAILED` |

## Testing & Go Live

### Simulation methods

Two ways to trigger error simulations:

- **JSON pointer**: pass error code as field value in request body (e.g. `plan_id: "ERRSUB033"`)
- **Path parameter**: embed error code in URI (e.g. `/subscriptions/ERRSUB068/activate`)

### API error types

| HTTP | Error name | Meaning |
| --- | --- | --- |
| 400 | INVALID_REQUEST | Malformed/schema violation |
| 401 | AUTHENTICATION_FAILURE | Bad credentials |
| 403 | NOT_AUTHORIZED | Insufficient permissions |
| 404 | RESOURCE_NOT_FOUND | ID not found |
| 422 | UNPROCESSABLE_ENTITY | Business validation failure |
| 500 | INTERNAL_SERVER_ERROR | Server error — retry |

### Go live

Swap `api-m.sandbox.paypal.com` → `api-m.paypal.com` + sandbox credentials → live credentials.

## Raw Sources

- [[paypal-subscriptions-overview]] — verbatim webpage content with 6-step flow diagram, two integration path options
- [[paypal-subscriptions-integrate]] — full integration guide: create product + plan curl examples with JSON responses, JS SDK button code, test flow steps, See Also links
- [[paypal-subscriptions-customize]] — customization catalog: 12 capabilities table (pricing plans, billing cycles, pause/resume, upgrade/downgrade, quantity change, future date, trial, setup fee, payment failure recovery, multiple buttons, pricing updates, social media)
- [[paypal-subscriptions-pricing-plans]] — 4 pricing models with curl examples, volume vs tiered distinction, source typo in tiered sample (`starting_quantity: 11"`)
- [[paypal-subscriptions-billing-cycles]] — billing cycle options (Day/Week/Month/Year/Custom), finite vs infinite plans (`total_cycles: N` vs `total_cycles: 0`)
- [[paypal-subscriptions-pause-resume]] — pause (`/suspend`) as soft-cancel to reduce churn; resume (`/activate`); outstanding balances still recoverable during pause
- [[paypal-subscriptions-revise]] — upgrade/downgrade via `/revise` + new `plan_id`; PayPal needs re-consent (HATEOAS URL); card payments skip re-consent; new price next cycle; no auto-proration
- [[paypal-subscriptions-change-quantity]] — quantity change via same `/revise` endpoint + `quantity` field; same re-consent/billing rules; URL uses `/v1/subscriptions/` (no `billing/` prefix — possible doc inconsistency)
- [[paypal-subscriptions-future-date]] — `start_time` on Create Subscription (UTC); setup fees charged immediately at sign-up; start date updatable while still in future
- [[paypal-subscriptions-trial-period]] — up to 2 trial periods per plan; `tenure_type: "TRIAL"`; free ($0) or discounted; code blocks rendered as line-numbered strings (docs platform artifact)
- [[paypal-subscriptions-setup-fee]] — `payment_preferences.setup_fee` on Create Plan; charged before subscription begins; `payment_preferencesobject` link text typo in source
- [[paypal-subscriptions-payment-failure]] — retry every 5 days, max 2× per cycle; outstanding balance accumulates; suspend at `payment_failure_threshold`; capture via `/capture` + `OUTSTANDING_BALANCE`; partial capture supported
- [[paypal-subscriptions-multiple-buttons]] — load SDK once; unique container div per plan (tip: use plan ID as ID); separate `Buttons().render()` per plan; full 2-plan HTML example
- [[paypal-subscriptions-update-pricing]] — `/update-pricing-schemes` on plan; 10-day subscriber notice; grace period if next cycle within 10 days; `billing_cycle_sequence` targets specific cycles; supports volume/tiered
- [[paypal-subscriptions-sell-social]] — no-code subscription link from dashboard; Facebook/Instagram/Twitter/email/SMS; links valid 6 months; no website required
- [[paypal-subscriptions-test-golive]] — two simulation methods (JSON pointer + path param); 40+ ERRSUB/ERRCAT codes for Product/Plan/Subscription ops; 6 API error types; go-live URL swap; unclosed JSON quote in source
- [[paypal-subscriptions-webhooks]] — 17 webhook events: 2 product, 5 plan (incl. PRICING-CHANGE.ACTIVATED), 3 payment (COMPLETED/REFUNDED/REVERSED), 7 subscription lifecycle

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[recurring-payments]] — recurring payments concept; subscriptions are a primary use case
- [[paypal-vault]] — vault underlies subscription payment method storage
