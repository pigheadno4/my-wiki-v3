---
title: "Stripe Subscriptions"
type: concept
category: technology
tags: [stripe, subscriptions, recurring-payments, billing, checkout, customer-portal, webhooks, entitlements, flexible-billing]
---

## Stripe Subscriptions

Stripe's recurring billing product. Manages subscription lifecycle — creation, renewal, failure handling, cancellation — and integrates with Checkout, Invoicing, and the Customer Portal.

**Design decisions**: (1) Pricing model: flat rate, per-seat, tiered (volume or graduated), usage-based (fixed+overage / pay-as-you-go / credit burndown). (2) Checkout interface: Stripe-hosted, embedded, custom form, pricing table, one-click buttons (Express Checkout Element: Link/Apple Pay/Google Pay/PayPal/Klarna/Amazon Pay), payment link (not for usage-based), mobile app. (3) Billing timing: pay up front, free trial (PM collected), freemium (PM collected before trial ends).

**Billing object chain**: The 2026-11-07 Billing APIs overview says a `Subscription` generates an `Invoice` each cycle and describes `PaymentIntent` creation when an invoice has an amount due; automatically charged subscriptions use the subscription or customer default payment method. See [[source-stripe-billing-apis]].

> [!warning] Contradiction
> The same November snapshot's PaymentIntent table says invoices automatically create PaymentIntents without the amount-due condition; the May capture also uses broad wording. Treat this as unresolved documentation tension, not a universal runtime rule.

**Payment behavior**: `default_incomplete` (recommended; collect payment after creation), `allow_incomplete` (immediate attempt), `error_if_incomplete` (fails entirely on payment failure).

**23-hour first payment window**: customer must pay within 23h (on-session assumption); after 23h → `incomplete_expired`; create new subscription for returning customer.

**Async payment methods** (ACH etc.): skip `incomplete`, go directly to `active`; if payment fails later, invoice voided but subscription stays `active`.

**8 subscription statuses**: `trialing`, `active`, `incomplete` (awaiting initial payment or action), `incomplete_expired`, `past_due`, `canceled` (terminal in this overview), `unpaid`, `paused` (trial-end missing-method path in this overview). For reactivation from `past_due` or `unpaid`, the captured default uses the most recent non-voided invoice; an all-invoices setting requires all applicable outstanding invoices to be settled. `active` does not prove every invoice is paid. See [[source-stripe-subscriptions-overview]].

**11 core billing objects**: Account (v2, customer-configured) or Customer (v1), Product, Price, Subscription, Invoice, PaymentIntent, PaymentMethod, Feature, ProductFeature, Entitlement.

## Server SDK 23.0.0 Pause and Billing Contracts

The retained Endive SDK adds `stripe.subscriptions.pause(id, params)`, a POST to `/v1/subscriptions/{id}/pause`. Its comment describes a true paused status: no invoices and no new billing periods, resumable via the resume endpoint, but no attached schedule. This is distinct from `pause_collection`. Schedule-managed pauses instead have `pause_schedules` on create/update (only one entry supported), optional resume timing/settings, and operation statuses; omit an update to preserve it or pass an empty string to clear it.

Update/resume `billing_cycle_anchor` becomes an object with `type: 'now' | 'unchanged'`; invoice previews also permit a timestamp variant. Resume adds `payment_behavior` (direct endpoint default `resume_on_payment_attempt`; new schedule resume settings default `resume_on_payment_success`). Item `current_trial`, trial-end anchor settings and invoice/subscription `status_details` add typed lifecycle information. This is SDK contract evidence, not proof of universal Billing eligibility. Source: [[source-github-stripe-node]].

> [!warning] Contradiction
> The historical trial-only paused-status description above is not exhaustive for this SDK: the 23.0.0 generated status comment repeats it even though that same file implements explicit pause and exposes `pause_requested` reasons. Preserve the old guide/version evidence; consult the version-qualified endpoint and product prerequisites rather than treating that comment as a restriction. See [[stripe-node-sdk]] and [[source-github-stripe-node]].

## PHP 22.0.0 Pause and Anchor Contracts

PHP exposes `$stripe->subscriptions->pause($id, $params)`, POST `/v1/subscriptions/{id}/pause`, distinct from `pause_collection`. Its endpoint comment says paused subscriptions stop invoices/new periods and excludes subscriptions with attached schedules. `pause_schedules` on SubscriptionSchedule provides a separate schedule-managed surface. Update/resume `billing_cycle_anchor` now uses an array with `type`; invoice-preview anchors additionally allow `timestamp`. Resume adds `payment_behavior`; subscription items expose `current_trial`, and subscription/invoice responses add `status_details`. These are SDK contracts, not standalone product-eligibility guarantees. Source: [[source-github-stripe-php]].

> [!warning] Contradiction
> PHP22.0.0's `Subscription::$status` comment still says paused status is only entered after a trial ends without a payment method, but its service implements the new explicit pause endpoint. Preserve the earlier guide/version information and consult endpoint prerequisites; that comment is not an exhaustive rule. See [[source-github-stripe-php]].

## PHP 21.3.0 Cancellation Feedback

The PHP SDK adds `billing->feedbackOptions` create/list/retrieve/update/deactivate operations, portal cancellation `feedback_options`, and subscription cancellation/update `cancellation_details.feedback_option`. Deactivated feedback options cannot be used in portal configurations. These generated contracts extend custom cancellation reasons; they do not change the irreversible canceled-subscription boundary. Source: [[source-github-stripe-php]].

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

- **Billing-related updates** — can create prorations and generate invoices, depending on the change and settings: price, quantity, billing period, add/remove items.
- **Non-billing updates** — apply immediately with no prorations: metadata, payment methods, tax settings, discount-only changes.

**Discount-only changes**: updating coupons or promo codes alone doesn't create proration invoice items — new discount applies to next invoice. Exception: if combined with a proration-triggering update in the same API call (e.g. quantity change), Stripe calculates the proration using the **updated discount state**.

**Pending updates**: for changes that trigger a new invoice, use pending updates so the change only applies if the invoice is successfully paid.

### Changing price (upgrade / downgrade)

Two methods: (1) `stripe.subscriptions.update` with `items[].id` + new `price`; (2) `stripe.subscriptionItems.update` with new `price` (when no subscription-level changes needed).

**Pitfall**: omitting the item `id` when updating a subscription's price **adds** a new subscription item — both prices become active simultaneously.

**Quantity resets to 1** on price change — pass existing quantity explicitly to preserve it.

**Billing period on price change**: The separate [[source-stripe-subscriptions-change-price]] guide says a same-interval change keeps dates, a different interval resets the billing period, and adding a trial moves it to trial end. The November [[source-stripe-subscriptions-billing-mode-compare]] qualifies the interval statement by mode: classic can reset its anchor for an interval change, while flexible preserves the anchor for that change unless `billing_cycle_anchor` is explicitly reset or `trial_end` is updated.

**Zero-amount edge cases**: The price-change guide says zero-amount to non-zero generates an invoice and resets the period, while zero quantity to non-zero does neither. For the flexible free-to-paid scenario, the November comparison instead says charges remain pending until the next cycle unless `proration_behavior=always_invoice` or `billing_cycle_anchor=now` is used for immediate invoicing. Keep each source’s mode and scenario qualification.

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

- `subscription_data.billing_cycle_anchor` in Checkout subscription mode — Unix timestamp that aligns future billing-cycle dates. The first full invoice can precede a config-derived anchor; see [[source-stripe-subscriptions-billing-cycle]] (2026-05-12 lines 112–114; 2026-11-07 lines 83–85).
- Default `proration_behavior: 'create_prorations'` — prorated charge for initial period
- `proration_behavior: 'none'` — initial period is free; no $0 invoice; `payment_status = 'no_payment_required'`
- **Checkout limitations**: Checkout cannot combine a trial with a billing-cycle anchor, and its `proration_behavior=none` cannot be used with one-time prices. The Subscriptions API does document `trial_end` with an anchor; see [[source-stripe-subscriptions-billing-cycle]] (2026-05-12 lines 160–207; 2026-11-07 lines 115–149). The existing `amount_off` coupon restriction with `create_prorations` remains a separate Checkout limitation, not established by this billing-cycle guide.

## Limit Customers to One Subscription

- Detection: Stripe matches by `Customer` object (if in session) or **email address**
- Redirect to portal or your website — configured in Dashboard → Checkout and Payment Links settings
- Portal requires no-code portal + login link enabled; disabling login link re-enables multi-sub creation
- Active statuses that trigger redirect: `active`, `past_due`, `unpaid`, `paused`
- Works with Checkout (hosted + embedded) and Payment Links

## Free Trials

Stripe's May and November 2026 guides label the `trial_end`/`trial_period_days` free-trial period a legacy integration path and recommend separate Trial Offers for new integrations. Trial Offers have their own preview and flexible-billing constraints; Checkout's documented no-payment-method trial path here remains the legacy period path. [[source-stripe-subscriptions-free-trials]]

- `subscription_data.trial_period_days` or `subscription_data.trial_end` (Unix timestamp)
- Max 730 days; practical issues at longer trials: PM expiry, lower conversion
- **No PM in this Checkout Session**: `payment_method_collection: 'if_required'` makes payment-information collection optional; set `subscription_data.trial_settings.end_behavior.missing_payment_method` to `cancel` or `pause` for the documented Checkout end behavior. [[source-stripe-subscriptions-free-trials]]
- **End behavior**: `subscription_data.trial_settings.end_behavior.missing_payment_method: 'cancel'` or `'pause'`
  - Pause = no invoices and can remain paused indefinitely. A payment method may be added through the portal, but resume and payment of the resumption invoice are required before reactivation; the API can begin resume without a method attached. The 23-hour auto-void applies only if the invoice's PaymentIntent has no attached method and remains unconfirmed. [[source-stripe-subscriptions-free-trials]]
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
- [[source-stripe-billing-apis]] — Billing API objects overview (May and November 2026 captures): 11 objects, customer model variants, entitlements, and the qualified Invoice → PaymentIntent narrative/table conflict
- [[source-stripe-subscriptions-overview]] — Subscription lifecycle: 8 statuses, payment behavior options, 23h window, async PM behavior, payment status matrix
- [[source-stripe-checkout-subscriptions-quickstart]] — May and November 2026 hosted Checkout subscription quickstart: recurring Price lookup key, customer portal, webhook and active-status access check; dated variants and optional features in source
- [[source-stripe-subscriptions-design-integration]] — Design guide: 4 pricing models, 7 checkout interfaces, 3 billing timing models, integration matrix
- [[source-stripe-build-subscriptions]] — Full integration guide: 3 UI paths (hosted/embedded/Elements), billing_mode:flexible, provision access pattern, test payment methods
- [[source-stripe-recurring-pricing-models]] — Pricing models reference: flat rate, per-seat, tiered, usage-based
- [[source-stripe-flat-rate-pricing]] — Flat rate pricing implementation: Product + monthly/yearly Price + Subscription API pattern
- [[source-stripe-per-seat-pricing]] — Per-seat pricing: same API as flat rate but pass quantity (seats) in subscription items
- [[source-stripe-usage-based-pricing]] — Usage-based pricing: licensed vs metered usage_type, billing_scheme:tiered + meter, credit burndown via billing.creditGrants
- [[source-stripe-tiered-pricing]] — Tiered pricing: volume (qty × one tier rate) vs graduated (sum tiers), flat_amount per tier, quantity=0 edge case
- [[source-stripe-subscriptions-setup-intents]] — SetupIntents for zero-payment subs: auto-created, requires_action vs requires_payment_method, doesn't auto-cancel on subscription end
- [[source-stripe-subscriptions-migration]] — Migration overview: Zuora/Recurly/Chargebee → toolkit (no-code) or APIs; PAN import; 4-scenario decision matrix
- [[source-stripe-subscriptions-migration-toolkit]] — Billing migration toolkit (May and November 2026 captures): three CSV paths, scheduled-start and cancellation windows, collection validation, toolkit-specific proration default, and tax/sample contradictions

> [!warning] Contradiction
> The May toolkit capture said blank/omitted `proration_behavior` defaults to `create_prorations` and blank external-tax fields would follow the Billing integration after go-live. The November capture says this toolkit CSV defaults to `none` and blank tax fields do not enable future automatic tax. Its unchanged Basic example also says 20 USD in prose but puts 50 in the one-time amount field. See the dated [[source-stripe-subscriptions-migration-toolkit]]; do not treat sample rows as verified upload templates.
- [[source-stripe-subscriptions-migration-api]] — API migration: Subscription API permitted, Schedules recommended for future starts; default payment method for automatic collection, conditional legacy price_data, ID and mid-cycle mapping, sandbox test clocks

> [!warning] Contradiction
> The 2026-05-12 API migration capture lists a one-year legacy-price interval limit; the 2026-11-07 capture lists three years. They are dated documentation claims, not a live API validation. Both prose examples denote June 1, 2022 at 00:00 UTC, but their unchanged `start_date=1654066801` denotes 07:00:01 UTC. The intended sample time is unresolved. See [[source-stripe-subscriptions-migration-api]] and its preserved raw captures.
- [[source-stripe-subscriptions-webhooks]] — 22 subscription webhook events, invoice.created 72h risk, access expiration pattern, EventBridge/Event Grid routing
- [[source-stripe-subscriptions-billing-cycle]] — Billing-cycle guide (2026-05-12 and 2026-11-07): new-subscription config or timestamp, versioned reset-to-now behavior, private-preview flexible-mode timestamp reset, trial-as-anchor, and automatic reset cases
- [[source-stripe-subscriptions-trial-offers]] — Trial Offers API (preview): discounted/free/upgrade/item-level trials, flexible billing required, opt-in cancellation
- [[source-stripe-subscriptions-free-trials]] — Legacy trial_end/trial_period_days (May and November 2026): no-PM end choices, paid-invoice resume gate, conditional 23-hour void, billing-anchor example
- [[source-stripe-subscriptions-billing-mode]] — Flexible billing mode: migrate API, proration_discounts itemized/included, schedule inheritance, cannot revert to classic
- [[source-stripe-subscriptions-billing-mode-compare]] — Classic vs flexible billing comparison (May and November 2026 captures): prorations, usage, anchors, pending items, cancellations, trials, mixed intervals, and item limits; scenario-specific differences
- [[source-stripe-subscriptions-mixed-interval]] — Mixed interval subscriptions: item-level periods, interval alignment rules, cancellation, Checkout limitation
- [[source-stripe-subscriptions-coupons]] — Coupons/promotion codes: duration behaviors, stackable discounts, promo code restrictions, update rules
- [[source-stripe-subscriptions-modify]] — Modify subscriptions hub: billing-related vs non-billing update distinction, discount+proration mixed-call behavior, pending updates
- [[source-stripe-subscriptions-change-price]] — Change price (upgrade/downgrade): item-ID pitfall, quantity reset, billing period rules, zero-amount edge cases, usage meter notes
- [[source-stripe-subscriptions-prorations]] — Prorations: 6 triggers, exhaustive non-trigger list, classic vs flexible credit prorations, preview locking, unpaid invoice handling
- [[source-stripe-subscriptions-pending-updates]] — Pending updates: payment_behavior=pending_if_incomplete, 27 supported PMs, expiry logic, metered item edge cases, 3 webhook events
- [[source-stripe-subscriptions-cancel]] — Cancel subscriptions: immediate/period-end/custom-date/schedule methods, invoice item handling, dispute config, billing anchor behavior
- [[source-stripe-subscriptions-pause]] — True pause (flexible billing only): bill_for, 6 blocking conditions, resume invoice 23h window, 4 webhook events
- [[source-stripe-subscriptions-prebilling]] — May 2026 preview and November 2026 prebilling guides: `billing_schedules`, `bill_until`, licensed-item scope, updated API prerequisite and total-cycle limit, invoice timing by `proration_behavior`
- [[source-stripe-subscriptions-invoices]] — Subscription invoices: lifecycle, 4-level payment priority, draft window, void rules, metadata propagation
- [[source-stripe-subscriptions-ach-debit]] — ACH subscription: 10-day microdeposit window, default PM webhook required, trial SetupIntent flow, Checkout delayed notification events
- [[source-stripe-subscriptions-amazon-pay]] — May 2026 Amazon Pay subscription guide: SetupIntents, PaymentIntents and hosted Checkout paths; November 2026 capture is a variant index
- [[source-stripe-subscriptions-bacs-debit]] — Bacs subscription: Checkout-only, delayed notification, 9 test accounts, inline pricing, trials, tax rates, coupons
- [[source-stripe-subscriptions-bank-transfers]] — Bank transfer subscription: send_invoice+customer_balance required, days_until_due, cash balance auto-pay, Accounts v2 cash balance path
- [[source-stripe-subscriptions-becs-debit]] — AU BECS subscription guide (May/November 2026): SetupIntent and DDR, first-payment check, conditional insufficient-funds retry, mandate URL sharing
- [[source-stripe-subscriptions-cash-app-pay]] — Cash App Pay subscription guide: three detailed paths in the 2026-05-13 capture; 2026-11-07 base capture is a variant index. Direct API examples show QR/redirect authentication.
- [[source-stripe-subscriptions-klarna]] — Klarna subscription: Checkout (recommended) + Payment Element, 23 countries, email-based test approve/deny, BNPL options vary by country
- [[source-stripe-subscriptions-paypal]] — May 2026 PayPal subscription guide: Stripe-hosted Checkout + Direct API SetupIntent; billing agreement, update off_session guidance, mandate.updated on revoke; November 2026 index links variants only
- [[source-stripe-subscriptions-pix]] — Pix subscription: November variant index; May combined guide covers three mandate-based paths, cross-border tax-ID statement, setup versus payment outcomes and six sandbox email patterns
- [[source-stripe-subscriptions-revolut-pay]] — Revolut Pay subscription: May 2026 guide covers three paths; `usage=off_session` on SetupIntent creation and `off_session=true` on SetupIntents-path subscription creation; November capture is variant navigation only
- [[source-stripe-subscriptions-kr-card]] — South Korean card (kr_card) subscription: KRW-only, 3 paths, off_session+mandate_data required, local processor redirect
- [[source-stripe-subscriptions-kakao-pay]] — Kakao Pay subscription: identical to kr_card structure, kakao_pay PM type, KRW-only
- [[source-stripe-subscriptions-naver-pay]] — Naver Pay subscription: identical structure, naver_pay PM type, KRW-only
- [[source-stripe-subscriptions-acss-debit]] — Canadian PAD subscription guide (2026-05-13 and 2026-11-07): Checkout subscription-mode waitlist, conditional insufficient-funds retries, payment-confirmed fulfillment, default-PM webhook, 10-day microdeposit window
- [[source-stripe-subscriptions-sepa-debit]] — SEPA subscription: Checkout + Payment Element, delayed notification, 20+ country IBAN test tables
- [[source-stripe-subscriptions-stablecoins]] — Stablecoin subscription: May 2026 three-path guide with crypto method examples; Payment Intents uses a USDC price example, Checkout and Setup Intents use USD examples; MetaMask and Amoy are recommended sandbox tools; November capture is variant navigation only
- [[source-stripe-subscriptions-twint]] — dated May 2026 TWINT subscription examples for Checkout, Setup Intents and Subscriptions API; November 2026 variant index. Direct API examples include mandate_data and return_url, while the Checkout example does not; setup success and first-payment success are distinct.
- [[source-stripe-subscriptions-ideal]] — 2026-05-13 iDEAL→SEPA variants: hosted Checkout first payment or refunded 0.01 EUR trial collection; Direct API refunded setup collection, generated SEPA method, and off_session update guidance. 2026-11-07 capture is a variant index only.
- [[source-stripe-subscriptions-pause-payment]] — pause payment collection: 3 behaviors (void/keep_as_draft/mark_uncollectible), vs true pause, resumes_at, unpausing
- [[source-stripe-subscriptions-third-party]] — May 2026 guide for own-processor custom PaymentMethods/PaymentRecords and separate out-of-band invoices, including its 23-hour reporting window; November 2026 base capture is a variant index only
- [[source-stripe-billing-taxes-collect]] — collecting taxes on subscriptions: Stripe Tax (Elements without Intent, address validation) vs Tax Rates (cascade rules, dynamic Checkout)
- [[source-stripe-billing-customer-tax-ids]] — Customer Tax IDs: 130+ types, reverse charge flag, AU/EU/GB auto-validation, customer.tax_id.updated webhook
- [[source-stripe-billing-taxes-migration]] — migrating subscriptions to Stripe Tax: automated tooling, manual steps, tax_behavior immutability, schedule to avoid prorations
- [[source-stripe-subscriptions-schedules]] — subscription schedules: phases, dual proration settings, metadata merge rules, direct update auto-split, 10 use cases
- [[source-stripe-subscriptions-backdate]] — backdating: classic vs flexible line items, 3 usage patterns, coupon duration gotcha (counts from backdate, not API call)
- [[source-stripe-billing-analytics]] — billing analytics: MRR definition + 6 growth components, ARPU, LTV, cohort retention, configurable discount/subscriber settings, 3 CSV reports
- [[source-stripe-billing-benchmarks]] — benchmarking: k-NN peer matching, ≥5 subs access, 7 benchmarked metrics, percentile display
