---
title: "Stripe Checkout: Build a Subscriptions Integration"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-build-subscriptions-2025.md"
  - "stripe-checkout-free-trials-2025.md"
  - "stripe-checkout-limit-subscriptions-2025.md"
  - "stripe-checkout-billing-cycle-2025.md"
  - "stripe-checkout-upsells-2025.md"
  - "stripe-checkout-yearly-price-display-2025.md"
tags: [stripe, checkout, subscriptions, recurring-payments, billing, customer-portal, webhooks, entitlements, flexible-billing, free-trials, limit-subscriptions, billing-cycle, prorations, upsells, yearly-pricing, monthly-display]
---

## Summary

End-to-end guide for building a subscription integration with Stripe Checkout. Covers product/price catalog setup, Checkout Session creation in subscription mode, webhook-based provisioning, customer portal setup, and the embedded page variant. Both hosted and embedded modes documented.

## Key Takeaways

- **Session**: `mode: 'subscription'` + recurring Price ID; works for both hosted and embedded modes
- **Flexible billing mode**: `subscription_data.billing_mode: { type: 'flexible' }` — enhanced behavior; requires API version `2025-06-30.basil`
- **Webhook provisioning**: `checkout.session.completed` → provision; `invoice.paid` → renew access; `invoice.payment_failed` → notify + redirect to portal
- **Provision by product not price**: check `product.id` on subscription events — allows price changes without breaking access logic
- **Store**: `product.id`, `subscription.id`, `subscription.status`, `customer.id` (or `customer_account.id`)
- **Customer portal**: `stripe.billingPortal.sessions.create({ customer, return_url })`; configure in Dashboard; monitor `customer.subscription.created/updated/deleted`
- **Embedded mode**: `ui_mode: 'embedded_page'` + `return_url` with `{CHECKOUT_SESSION_ID}` template; session-status endpoint for return page handling
- **lookup_keys**: alternative to price IDs when creating sessions

## Minimum Webhook Events

| Event | Action |
| --- | --- |
| `checkout.session.completed` | Provision subscription; save `customer.id` + `subscription.id` |
| `invoice.paid` | Continue provisioning each billing period |
| `invoice.payment_failed` | Notify customer; redirect to portal for payment method update |
| `customer.subscription.created` | Grant access based on product |
| `customer.subscription.updated` | Update access level |
| `customer.subscription.deleted` | Revoke access |

## Integration Steps (Hosted)

1. Create products + recurring prices via Dashboard or API
2. Create Checkout Session: `mode: 'subscription'`, `line_items: [{ price, quantity }]`, `success_url` with `{CHECKOUT_SESSION_ID}`
3. On `checkout.session.completed`: save `customer.id`, provision access
4. On `invoice.paid`: continue access each billing period
5. On `invoice.payment_failed`: notify + portal redirect
6. Customer portal: `billingPortal.sessions.create({ customer, return_url })`

## Integration Steps (Embedded)

1. Same products + prices setup
2. Create session: add `ui_mode: 'embedded_page'`, `return_url` with `{CHECKOUT_SESSION_ID}`
3. Mount via `stripe.createEmbeddedCheckoutPage({ fetchClientSecret })` or `EmbeddedCheckoutProvider`
4. Return page: GET `/session-status?session_id=...` → handle `complete` (success) or `open` (remount)
5. Same webhook provisioning as hosted

## Flexible Billing Mode

`subscription_data.billing_mode: { type: 'flexible' }` enables enhanced billing behavior. Requires Stripe API version `2025-06-30.basil` or later. Standard `type: 'fixed'` is the default.

## Customer Portal

- Configure in Dashboard: payment method updates, cancellation, upgrade/downgrade
- Create session server-side: `stripe.billingPortal.sessions.create({ customer/customer_account, return_url })`
- Monitor portal-triggered events: `customer.subscription.updated`, `customer.subscription.deleted`

## Access Provisioning Pattern

Check `product.id` (not `price.id`) when determining access — this decouples access control from pricing changes:

```js
// In customer.subscription.updated handler:
const productId = subscription.items.data[0].price.product;
// Grant access based on productId, not priceId
```

Store in your DB: `{ product_id, subscription_id, subscription_status, customer_id }`

## Test Cards

| Scenario | Card |
| --- | --- |
| Success (no auth) | `4242 4242 4242 4242` |
| Requires 3DS auth | `4000 0025 0000 3155` |
| Declined (insufficient funds) | `4000 0000 0000 9995` |
| BECS success | Account `900123456`, BSB `000000` |
| SEPA success | `AT321904300235473204` |

## Extensions

- Taxes: `automatic_tax: { enabled: true }`
- Discounts/coupons, free trials, prorations
- Usage-based billing, pricing tiers
- Entitlements for feature gating
- Multiple products per subscription

## Yearly Prices in Monthly Terms

- **Dashboard setting**: Checkout and Payment Links settings → pricing display "per month"
- Shows equivalent monthly rate below yearly total; if yearly is a upsell with lower monthly equivalent, strikethrough shown
- Applies to: Checkout, Payment Links, pricing tables, buy buttons
- **Restrictions**: not eligible when recurring + one-time mix, non-annual intervals, free trials, billing cycle anchors, or usage-based pricing

## Subscription Upsells

- **Dashboard-only setup**: Price details page → Upsells section → select target price; immediately applies to eligible sessions
- **Price pair requirements**: same Product, same currency, both `recurring`, matching `tax_behavior`/tier `up_to`/`transform_quantity`; non-metered only
- **Session eligibility**: subscription mode + exactly one recurring price + valid upsell config
- **Savings display**: 1-billing-cycle savings (e.g., $1000/yr vs $100/mo → saves $200); shown as amount or percentage
- **Fulfillment**: always retrieve `line_items` via API after `checkout.session.completed` — updates to selected upsell price
- **Trial**: trial length unchanged when upsell selected
- **Coupons**: applied coupon also applies to upsell price; `duration` counts from first application

## Billing Cycle Anchor

- `subscription_data.billing_cycle_anchor` — Unix timestamp; must be future before next natural billing date
- Determines first full invoice date and all future billing dates
- **Example**: monthly sub created May 15, anchor = June 1 → prorated charge May 15, then always June 1
- **Default** `proration_behavior: 'create_prorations'` — customer charged prorated amount for initial period
- **`proration_behavior: 'none'`** — initial period to anchor is free; no $0 invoice generated; line_items + total_details = 0; `payment_status = 'no_payment_required'`
- **Limitations**:
  - Trials + anchor are mutually exclusive
  - `proration_behavior: 'none'` + one-time prices: incompatible
  - `amount_off` coupons incompatible with default `create_prorations`

## Limit Customers to One Subscription

- **Detection**: Stripe matches existing subscriber by `Customer` object (if passed in session) or email address
- **Redirect destination**: customer portal or your website — configured in Dashboard → Checkout and Payment Links settings
- **Customer portal**: requires no-code portal activated with login link enabled; disabling login link re-enables multiple subscription creation
- **Website redirect**: custom URL with optional `{CHECKOUT_SESSION_ID}` and `{CUSTOMER_EMAIL}` template vars
- **Active statuses that trigger redirect**: `active`, `past_due`, `unpaid`, `paused`
- Works with both Checkout (hosted + embedded) and Payment Links

## Free Trials

- **Params**: `subscription_data.trial_period_days` (int) or `subscription_data.trial_end` (Unix timestamp)
- **Max**: 730 days (2 years); practical risks at longer trials: PM expiry + lower conversion
- **No PM required**: `payment_method_collection: 'if_required'` — skip payment collection during trial sign-up
- **End behavior** when no PM at trial end: `subscription_data.trial_settings.end_behavior.missing_payment_method`
  - `'cancel'` — subscription ends immediately; new subscription needed to re-subscribe
  - `'pause'` — no invoices generated; resumes when PM added via portal; pauses indefinitely
- **Trial reminder emails**: Dashboard → Subscriptions and emails → "Manage free trial messaging"; not sent in sandbox
- **`customer.subscription.trial_will_end`** webhook — trigger your own reminder email + portal redirect
- Card network compliance requirements apply for trials

## Related Pages

- [[stripe-subscriptions]] — Stripe Subscriptions concept page
- [[stripe-checkout]] — Stripe Checkout concept page
- [[recurring-payments]] — Generic recurring payments concept

## Raw Sources

- [[stripe-checkout-build-subscriptions-2025]] — Full subscription integration: product/price setup, Checkout Session (hosted + embedded), webhook provisioning, customer portal, flexible billing mode, test cards
- [[stripe-checkout-free-trials-2025]] — Free trials: trial_period_days/trial_end params, no-PM option, cancel vs pause end behavior, trial_will_end webhook, reminder emails, compliance requirements
- [[stripe-checkout-limit-subscriptions-2025]] — Limit to one subscription: email/Customer detection, portal vs website redirect, 4 active statuses, login link dependency (3 CDN images)
- [[stripe-checkout-billing-cycle-2025]] — Billing cycle anchor: billing_cycle_anchor param, proration_behavior (create_prorations vs none), payment_status=no_payment_required, limitations (no trials, no one-time prices, no amount_off coupons)
- [[stripe-checkout-upsells-2025]] — Subscription upsells: Dashboard-only setup, price pair requirements, session eligibility, savings display, fulfillment, trial + coupon behavior (3 GIFs)
- [[stripe-checkout-yearly-price-display-2025]] — Yearly prices in monthly terms: Dashboard setting, per-month display in Checkout/Payment Links/pricing tables/buy buttons, restrictions (3 CDN images)
