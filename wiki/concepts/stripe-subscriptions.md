---
title: "Stripe Subscriptions"
type: concept
category: technology
tags: [stripe, subscriptions, recurring-payments, billing, checkout, customer-portal, webhooks, entitlements, flexible-billing]
---

## Stripe Subscriptions

Stripe's recurring billing product. Manages subscription lifecycle — creation, renewal, failure handling, cancellation — and integrates with Checkout, Invoicing, and the Customer Portal.

**Design decisions**: (1) Pricing model: flat rate, per-seat, tiered (volume or graduated), usage-based (fixed+overage / pay-as-you-go / credit burndown). (2) Checkout interface: Stripe-hosted, embedded, custom form, pricing table, one-click buttons (Express Checkout Element: Link/Apple Pay/Google Pay/PayPal/Klarna/Amazon Pay), payment link (not for usage-based), mobile app. (3) Billing timing: pay up front, free trial (PM collected), freemium (PM collected before trial ends).

**Billing object chain**: `Subscription` → auto-generates `Invoice` each billing cycle → `Invoice` auto-creates `PaymentIntent` → `PaymentIntent` collects from stored `PaymentMethod`.

**Payment behavior**: `default_incomplete` (recommended; collect payment after creation), `allow_incomplete` (immediate attempt), `error_if_incomplete` (fails entirely on payment failure).

**23-hour first payment window**: customer must pay within 23h (on-session assumption); after 23h → `incomplete_expired`; create new subscription for returning customer.

**Async payment methods** (ACH etc.): skip `incomplete`, go directly to `active`; if payment fails later, invoice voided but subscription stays `active`.

**8 subscription statuses**: `trialing`, `active`, `incomplete` (awaiting first payment or 3DS), `incomplete_expired`, `past_due`, `canceled` (terminal), `unpaid`, `paused` (trial ended without PM + `missing_payment_method=pause`).

**11 core billing objects**: Account (v2, customer-configured) or Customer (v1), Product, Price, Subscription, Invoice, PaymentIntent, PaymentMethod, Feature, ProductFeature, Entitlement.

## Integration Paths

| Path | Best for |
| --- | --- |
| Checkout (`mode: 'subscription'`) | New signups; hosted or embedded UI |
| Payment Links | No-code recurring; no website needed |
| Subscriptions API directly | Custom checkout UI; programmatic control |
| Dashboard (no-code) | Manual setup for small volume |

## Checkout Integration

1. Create Product + recurring Price (`recurring: { interval: 'month' }`)
2. Create Checkout Session: `mode: 'subscription'`, `line_items: [{ price, quantity }]`
3. Optional: `subscription_data.billing_mode: { type: 'flexible' }` (requires API `2025-06-30.basil`)
4. On `checkout.session.completed`: save `customer.id` + `subscription.id`, provision access
5. On `invoice.paid`: renew access each billing period
6. On `invoice.payment_failed`: notify + redirect to Customer Portal

## Provisioning Pattern

Check `product.id` (not `price.id`) in subscription event handlers — decouples access from pricing:

```text
customer.subscription.created/updated/deleted
  └─ items[0].price.product → product_id
  └─ status → active | past_due | canceled | ...
```

Store: `{ product_id, subscription_id, subscription_status, customer_id }`

## Key Webhook Events

| Event | Action |
| --- | --- |
| `checkout.session.completed` | Initial provision |
| `invoice.paid` | Renew access |
| `invoice.payment_failed` | Notify + portal |
| `customer.subscription.created` | Grant access |
| `customer.subscription.updated` | Adjust access level |
| `customer.subscription.deleted` | Revoke access |

## Modifying Subscriptions

Existing subscriptions can be changed without cancel-and-recreate. Two categories of change:

- **Billing-related updates** — create prorations and can generate invoices: price, quantity, billing period, add/remove items.
- **Non-billing updates** — apply immediately with no prorations: metadata, payment methods, tax settings, discount-only changes.

**Discount-only changes**: updating coupons or promo codes alone doesn't create proration invoice items — new discount applies to next invoice. Exception: if combined with a proration-triggering update in the same API call (e.g. quantity change), Stripe calculates the proration using the **updated discount state**.

**Pending updates**: for changes that trigger a new invoice, use pending updates so the change only applies if the invoice is successfully paid.

### Changing price (upgrade / downgrade)

Two methods: (1) `stripe.subscriptions.update` with `items[].id` + new `price`; (2) `stripe.subscriptionItems.update` with new `price` (when no subscription-level changes needed).

**Pitfall**: omitting the item `id` when updating a subscription's price **adds** a new subscription item — both prices become active simultaneously.

**Quantity resets to 1** on price change — pass existing quantity explicitly to preserve it.

**Billing period on price change**: same `interval`+`interval_count` → dates unchanged; different intervals → resets to date of change; adding a trial also resets dates (to trial conclusion).

**Zero-amount edge cases**: zero-amount price → non-zero generates invoice + resets billing period. Zero-quantity → non-zero does NOT generate invoice or reset billing period.

## Flexible Billing Mode

`subscription_data.billing_mode: { type: 'flexible' }` — enhanced, more predictable billing behavior. Default is `'fixed'`. Requires API version `2025-06-30.basil` or later.

## Customer Portal

Stripe-hosted page for self-service subscription management:

- Payment method updates, cancellations, plan changes
- Create: `stripe.billingPortal.sessions.create({ customer/customer_account, return_url })`
- Configure in Dashboard (which actions to allow)
- Monitor: `customer.subscription.updated`, `customer.subscription.deleted`

## Subscription Statuses

`active` → `past_due` (payment failure) → `canceled` or `unpaid`. Also: `trialing`, `incomplete`, `incomplete_expired`, `paused`.

## Yearly Prices in Monthly Terms

Dashboard setting (Checkout and Payment Links settings → "per month") shows equivalent monthly rate below yearly total in Checkout, Payment Links, pricing tables, and buy buttons. With upsell: strikethrough shown if yearly has lower monthly equivalent. Not eligible when: recurring + one-time mix, non-annual intervals, free trials, billing cycle anchors, usage-based pricing.

## Subscription Upsells

Dashboard-only feature to offer longer-term plan upgrades (e.g., monthly → yearly) during Checkout:

- Configure on Price details page; immediately applies to eligible sessions
- **Price pair requirements**: same Product, currency, both recurring, matching tax_behavior/tiers/transform_quantity; non-metered only
- **Session eligibility**: subscription mode + exactly 1 recurring price
- Savings displayed as amount or percentage (1-billing-cycle basis)
- Always retrieve `line_items` after `checkout.session.completed` — they update to reflect the selected price
- Trial length unchanged; coupons apply to upsell price with duration counting from first application

## Billing Cycle Anchor

- `subscription_data.billing_cycle_anchor` — Unix timestamp; sets first full invoice date + all future dates
- Default `proration_behavior: 'create_prorations'` — prorated charge for initial period
- `proration_behavior: 'none'` — initial period is free; no $0 invoice; `payment_status = 'no_payment_required'`
- **Limitations**: trials + anchor mutually exclusive; `none` + one-time prices incompatible; `amount_off` coupons incompatible with `create_prorations`

## Limit Customers to One Subscription

- Detection: Stripe matches by `Customer` object (if in session) or **email address**
- Redirect to portal or your website — configured in Dashboard → Checkout and Payment Links settings
- Portal requires no-code portal + login link enabled; disabling login link re-enables multi-sub creation
- Active statuses that trigger redirect: `active`, `past_due`, `unpaid`, `paused`
- Works with Checkout (hosted + embedded) and Payment Links

## Free Trials

- `subscription_data.trial_period_days` or `subscription_data.trial_end` (Unix timestamp)
- Max 730 days; practical issues at longer trials: PM expiry, lower conversion
- **No PM at signup**: `payment_method_collection: 'if_required'`
- **End behavior**: `subscription_data.trial_settings.end_behavior.missing_payment_method: 'cancel'` or `'pause'`
  - Pause = no invoices, resumes on PM add via portal; can pause indefinitely
- **`customer.subscription.trial_will_end`** webhook → send reminder email + portal redirect
- Card network compliance requirements apply

## Extensions

- **Free trials**: `trial_period_days` on Price or `subscription_data.trial_settings`
- **Dynamic trial updates** (private preview): update `subscription_data.trial_period_days` or `subscription_data.trial_end` server-side via `runServerUpdate`; `trial_period_days` and `trial_end` are mutually exclusive; must use same field to remove as was used to set; see [[source-stripe-checkout-dynamic-trials]]
- **Discounts/coupons**: apply at checkout or via API
- **Usage-based billing**: metered prices; `usage_type: 'metered'` on Price
- **Pricing tiers**: `billing_scheme: 'tiered'` with `tiers` array
- **Prorations**: automatic on plan changes; configurable
- **Entitlements**: auto-created when subscription is created (one per Feature in the subscribed Product); use `customer.activeEntitlements` to gate features — don't re-query subscription/product/feature chain; listen to `entitlement.active_entitlement_summary.updated` to provision/deprovision
- **Multiple products**: multiple `line_items` per subscription session

## Plan Change

```js
await stripe.subscriptions.update(subscriptionId, {
  cancel_at_period_end: false,
  items: [{ id: currentItemId, price: newPriceId }],
});
// Triggers customer.subscription.updated
```

Use `stripe.invoices.createPreview({ customer, subscription, subscription_details: { items: [...] } })` to show customers the prorated amount before confirming.

## Cancellation

`stripe.subscriptions.del(subscriptionId)` → triggers `customer.subscription.deleted`.

> **Canceled subscriptions cannot be reactivated.** Collect new billing info and create a new subscription on the existing customer record.

## Customer Models

- **Customers v1**: `stripe.customers.create(...)` — `customer` param on session
- **Accounts v2** (recommended for Connect): `stripe.v2.core.accounts.create(...)` with `configuration.customer` — `customer_account` param on session; requires API version `2026-03-25.dahlia`

## Checkout Sessions Subscription Flow

Session: `mode: 'subscription'` + `ui_mode: 'elements'` + `customer` or `customer_account`. Client uses `checkout.createPaymentElement()` + `actions.confirm()`. `canConfirm` property gates the Pay button. Display `session.lineItems` and `session.total.total.amount`.

## Sources

- [[source-stripe-checkout-build-subscriptions]] — Full Checkout subscription integration: product/price setup, session creation, webhook provisioning, customer portal, flexible billing mode, test cards
- [[source-stripe-build-subscriptions-elements]] — End-to-end Elements subscriptions guide: entitlements, plan change, proration preview, cancel pattern, Accounts v2
- [[source-stripe-inapp-digital-goods-custom-checkout]] — iOS digital goods subscriptions (mobile context): default_incomplete + expand latest_invoice, invoice webhooks, Universal Links return, Apple Pay US+EEA
- [[source-stripe-inapp-digital-goods-customer-portal]] — iOS subscription management portal: billingPortal.sessions.create, customer.subscription.* webhooks, product catalog config, tax ID collection
- [[source-stripe-recurring-payments-overview]] — Stripe recurring payments overview: subscription creation via Dashboard/Payment Links/Checkout/Elements, flexible billing_mode, Accounts v2 customer_account, confirmation_secret expand
- [[source-stripe-billing-apis]] — Billing API objects overview: Subscription→Invoice→PaymentIntent chain, 11 objects, Entitlements model, Account v2 vs Customer v1
- [[source-stripe-subscriptions-overview]] — Subscription lifecycle: 8 statuses, payment behavior options, 23h window, async PM behavior, payment status matrix
- [[source-stripe-checkout-subscriptions-quickstart]] — Checkout subscription quickstart: lookup_key pattern, customer portal, 5 webhook events, trial/billing-anchor/auto-tax
- [[source-stripe-subscriptions-design-integration]] — Design guide: 4 pricing models, 7 checkout interfaces, 3 billing timing models, integration matrix
- [[source-stripe-build-subscriptions]] — Full integration guide: 3 UI paths (hosted/embedded/Elements), billing_mode:flexible, provision access pattern, test payment methods
- [[source-stripe-recurring-pricing-models]] — Pricing models reference: flat rate, per-seat, tiered, usage-based
- [[source-stripe-flat-rate-pricing]] — Flat rate pricing implementation: Product + monthly/yearly Price + Subscription API pattern
- [[source-stripe-per-seat-pricing]] — Per-seat pricing: same API as flat rate but pass quantity (seats) in subscription items
- [[source-stripe-usage-based-pricing]] — Usage-based pricing: licensed vs metered usage_type, billing_scheme:tiered + meter, credit burndown via billing.creditGrants
- [[source-stripe-tiered-pricing]] — Tiered pricing: volume (qty × one tier rate) vs graduated (sum tiers), flat_amount per tier, quantity=0 edge case
- [[source-stripe-subscriptions-setup-intents]] — SetupIntents for zero-payment subs: auto-created, requires_action vs requires_payment_method, doesn't auto-cancel on subscription end
- [[source-stripe-subscriptions-migration]] — Migration overview: Zuora/Recurly/Chargebee → toolkit (no-code) or APIs; PAN import; 4-scenario decision matrix
- [[source-stripe-subscriptions-migration-toolkit]] — Toolkit detail: 3 CSV types, 24h go-live buffer, 10h cancel window, timing advice, validation errors
- [[source-stripe-subscriptions-migration-api]] — API migration: Subscription Schedules (>30d future), legacy pricing via price_data, mid-cycle continuity, test clocks
- [[source-stripe-subscriptions-webhooks]] — 22 subscription webhook events, invoice.created 72h risk, access expiration pattern, EventBridge/Event Grid routing
- [[source-stripe-subscriptions-billing-cycle]] — Billing cycle anchor: billing_cycle_anchor_config (monthly/yearly), direct timestamp, reset to now, trial-as-anchor, auto-reset scenarios
- [[source-stripe-subscriptions-trial-offers]] — Trial Offers API (preview): discounted/free/upgrade/item-level trials, flexible billing required, opt-in cancellation
- [[source-stripe-subscriptions-free-trials]] — Legacy trial_end: trial_period_days, missing_payment_method (cancel/pause/create_invoice), resume flow, combine with billing anchor
- [[source-stripe-subscriptions-billing-mode]] — Flexible billing mode: migrate API, proration_discounts itemized/included, schedule inheritance, cannot revert to classic
- [[source-stripe-subscriptions-billing-mode-compare]] — Classic vs flexible: 12-row comparison (prorations, usage, cancellation, trials, mixed intervals)
- [[source-stripe-subscriptions-mixed-interval]] — Mixed interval subscriptions: item-level periods, interval alignment rules, cancellation, Checkout limitation
- [[source-stripe-subscriptions-coupons]] — Coupons/promotion codes: duration behaviors, stackable discounts, promo code restrictions, update rules
- [[source-stripe-subscriptions-modify]] — Modify subscriptions hub: billing-related vs non-billing update distinction, discount+proration mixed-call behavior, pending updates
- [[source-stripe-subscriptions-change-price]] — Change price (upgrade/downgrade): item-ID pitfall, quantity reset, billing period rules, zero-amount edge cases, usage meter notes
- [[source-stripe-subscriptions-prorations]] — Prorations: 6 triggers, exhaustive non-trigger list, classic vs flexible credit prorations, preview locking, unpaid invoice handling
- [[source-stripe-subscriptions-pending-updates]] — Pending updates: payment_behavior=pending_if_incomplete, 27 supported PMs, expiry logic, metered item edge cases, 3 webhook events
- [[source-stripe-subscriptions-cancel]] — Cancel subscriptions: immediate/period-end/custom-date/schedule methods, invoice item handling, dispute config, billing anchor behavior
- [[source-stripe-subscriptions-pause]] — True pause (flexible billing only): bill_for, 6 blocking conditions, resume invoice 23h window, 4 webhook events
- [[source-stripe-subscriptions-prebilling]] — Prebilling (public preview): bill_until, applies_to, 8 limitations, invoice timing via proration_behavior
- [[source-stripe-subscriptions-invoices]] — Subscription invoices: lifecycle, 4-level payment priority, draft window, void rules, metadata propagation
- [[source-stripe-subscriptions-ach-debit]] — ACH subscription: 10-day microdeposit window, default PM webhook required, trial SetupIntent flow, Checkout delayed notification events
- [[source-stripe-subscriptions-amazon-pay]] — Amazon Pay subscription: 3 integration paths (SetupIntents/PaymentIntents/Checkout), mandate_data required, off_session, redirect flow
- [[source-stripe-subscriptions-bacs-debit]] — Bacs subscription: Checkout-only, delayed notification, 9 test accounts, inline pricing, trials, tax rates, coupons
- [[source-stripe-subscriptions-bank-transfers]] — Bank transfer subscription: send_invoice+customer_balance required, days_until_due, cash balance auto-pay, Accounts v2 cash balance path
- [[source-stripe-subscriptions-becs-debit]] — BECS subscription (AU): SetupIntents + DDR mandate compliance, no-retry rule, mandatory mandate URL sharing
- [[source-stripe-subscriptions-cash-app-pay]] — Cash App Pay subscription: 3 paths (SetupIntents/Subscriptions API/Checkout), QR code + redirect auth, mandate_data required
- [[source-stripe-subscriptions-klarna]] — Klarna subscription: Checkout (recommended) + Payment Element, 23 countries, email-based test approve/deny, BNPL options vary by country
- [[source-stripe-subscriptions-paypal]] — PayPal subscription: Checkout + Direct API (SetupIntents), off_session=true required, billing agreement ID, mandate.updated on revoke
- [[source-stripe-subscriptions-pix]] — Pix subscription (Brazil/BRL): Pix Automático mandate, 3 paths, tax_id required, mandate_options.amount tip, 6 email test scenarios
- [[source-stripe-subscriptions-revolut-pay]] — Revolut Pay subscription: 3 paths (SetupIntents/Subscriptions API/Checkout), off_session required, mandate_data, redirect auth
- [[source-stripe-subscriptions-kr-card]] — South Korean card (kr_card) subscription: KRW-only, 3 paths, off_session+mandate_data required, local processor redirect
- [[source-stripe-subscriptions-kakao-pay]] — Kakao Pay subscription: identical to kr_card structure, kakao_pay PM type, KRW-only
- [[source-stripe-subscriptions-naver-pay]] — Naver Pay subscription: identical structure, naver_pay PM type, KRW-only
- [[source-stripe-subscriptions-acss-debit]] — Canadian PAD (acss_debit) subscription: Checkout NOT supported, no auto-retry, manual default PM webhook, 10-day microdeposit window
- [[source-stripe-subscriptions-sepa-debit]] — SEPA subscription: Checkout + Payment Element, delayed notification, 20+ country IBAN test tables
- [[source-stripe-subscriptions-stablecoins]] — Stablecoin subscription: 3 paths (Checkout/PaymentIntents/SetupIntents), crypto PM type, USDC native currency, testnet via MetaMask+Amoy
- [[source-stripe-subscriptions-twint]] — TWINT subscription: CHF only, 3 paths (Checkout/SetupIntents/Subscriptions API), mandate_data+return_url required, QR via redirect
- [[source-stripe-subscriptions-ideal]] — iDEAL→SEPA subscription: Checkout + Direct API, iDEAL captures IBAN then generates SEPA PM, off_session updates, 6 test patterns
- [[source-stripe-subscriptions-pause-payment]] — pause payment collection: 3 behaviors (void/keep_as_draft/mark_uncollectible), vs true pause, resumes_at, unpausing
- [[source-stripe-subscriptions-third-party]] — billing with 3rd party processors: custom PMs + payment records (recommended) vs out-of-band (legacy), 23h window, retry logic
- [[source-stripe-billing-taxes-collect]] — collecting taxes on subscriptions: Stripe Tax (Elements without Intent, address validation) vs Tax Rates (cascade rules, dynamic Checkout)
- [[source-stripe-billing-customer-tax-ids]] — Customer Tax IDs: 130+ types, reverse charge flag, AU/EU/GB auto-validation, customer.tax_id.updated webhook
- [[source-stripe-billing-taxes-migration]] — migrating subscriptions to Stripe Tax: automated tooling, manual steps, tax_behavior immutability, schedule to avoid prorations
- [[source-stripe-subscriptions-schedules]] — subscription schedules: phases, dual proration settings, metadata merge rules, direct update auto-split, 10 use cases
- [[source-stripe-subscriptions-backdate]] — backdating: classic vs flexible line items, 3 usage patterns, coupon duration gotcha (counts from backdate, not API call)
- [[source-stripe-billing-analytics]] — billing analytics: MRR definition + 6 growth components, ARPU, LTV, cohort retention, configurable discount/subscriber settings, 3 CSV reports
- [[source-stripe-billing-benchmarks]] — benchmarking: k-NN peer matching, ≥5 subs access, 7 benchmarked metrics, percentile display
