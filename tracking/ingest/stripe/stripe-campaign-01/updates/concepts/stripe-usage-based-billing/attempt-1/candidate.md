---
title: "Usage-Based Billing (Stripe)"
type: concept
category: technology
tags: [stripe, billing, usage-based, meters, subscriptions, pricing, invoicing]
---

## Definition

Stripe's usage-based billing lets you charge customers based on actual product consumption — API calls, data processed, seats used, etc. This page details the **basic Billing Meters API** path (billing v2), distinct from the legacy `aggregate_usage` metered price approach. In the 2026-11-07 guide, Stripe recommends Metronome for new usage-based integrations unless maintaining an existing Billing Meters integration; that recommendation is not Meter API deprecation or forced migration.

> [!warning] Contradiction
> The earlier “current approach” wording reflected the Meter-based guide, while the November guide now recommends Metronome for new integrations. The capture does not establish account-specific Metronome eligibility or removal of Billing Meters.

## Ingestion Methods

Three ways to send meter events to Stripe:

- **API** — `stripe.billing.meterEvents.create(...)` (real-time or batched)
- **Dashboard** — manual input (one event at a time) or CSV file upload (max 5 MB). CSV fields: `timestamp` (`yyyy-MM-dd`, ISO with TZ, or Epoch), `event_name`, `payload_stripe_customer_id` (`cus_xxxx` or `acct_xxxx`), `payload_value` (column name mirrors `value_settings` key). Errors → downloadable error file with per-record reasons.
- **Amazon S3** — bulk ingestion via S3 connector (CSV, JSON, JSON Lines; max 1 GB/file). Configure via Stripe Dashboard → Data management → Connectors with an IAM role + trust policy. Polls every 5 minutes; initial sync covers last 90 days. Rate limits: 1 file per 10 seconds or 1M records; max 50 files/10 GB per poll; 10,000 events/second processing. Two-tier error handling: format errors → `data_management.import_set.failed/succeeded` (snapshot); data errors → same thin events as API.

Must configure the meter before recording usage. Events process asynchronously — summaries and upcoming invoices may lag.

For LLM token billing, Stripe's retained `@stripe/token-meter@0.1.0` implementation sends Billing v2 meter events with customer, token count, provider/model, and input/output token type. Its fire-and-forget path catches and logs delivery errors without interrupting model generation. Production use therefore needs independent monitoring, reconciliation, and replay/recovery controls to avoid silent usage undercount. See [[source-github-ai]].

## Lifecycle

1. **Ingestion** — send meter events (usage data) to Stripe
2. **Product catalog** — create usage-based prices linked to meters
3. **Billing** — subscribe customers to prices; Stripe generates invoices at end of billing period
4. **Monitoring** — threshold alerts + usage analytics

## Core Objects

**Meter** — defines what to track and how to aggregate it. Configuration:

| Attribute | Description |
| --- | --- |
| Event name | Unique per meter; must match `event_name` in meter events |
| Event ingestion | **Raw** (default): all events are standalone, multiple events per timestamp all count. **Pre-aggregated**: only the most recently received event within each hourly/daily window is kept (UTC boundaries). |
| Aggregation formula | `sum` / `count` / `last` |
| Payload key overrides | `value_settings.event_payload_key` (default: `value`), `customer_mapping.event_payload_key` (default: `stripe_customer_id`) |

After creation, only `display_name` can be changed — all other configuration is immutable.

API: `stripe.billing.meters.create({ display_name, event_name, default_aggregation: { formula }, customer_mapping: { event_payload_key: 'stripe_customer_id', type: 'by_id' }, value_settings: { event_payload_key: 'value' } })`

**Meter event** — a single unit of reported usage. Fields:

- Event name (must match meter config)
- Customer identifier
- Numerical usage value (sent as a **string** in the payload; decimals supported)
- Optional: timestamp (defaults to now), `identifier` for idempotency (auto-generated if omitted), segmentation dimensions

Timestamp constraints: within the past **35 calendar days** and no more than **5 minutes in the future** (clock drift allowance).

Rate limits (v1 endpoint, live mode): **1,000 calls/second** standard; **100 ops/second** for Connect platforms using `Stripe-Account` header. Mitigate by pre-aggregating before sending, or use API v2 high-throughput.

**API v2 — Meter Event Streams**: up to **10,000 events/second** (live only; contact sales for up to 200,000/s). Uses 15-minute stateless auth sessions: `client.v2.billing.meterEventSession.create()` → token → `client.v2.billing.meterEventStream.create({ events: [...] })`. Stream events are not logged in Workbench Logs.

API: `stripe.billing.meterEvents.create({ event_name, payload: { stripe_customer_id, value } })`

**Meter event summary** — retrieve a customer's aggregated usage for any custom time range. Updates asynchronously as events are processed.

API: `stripe.billing.meters.listEventSummaries(METER_ID, { customer, start_time, end_time })` — Unix timestamps

**Meter event adjustment** — cancel an incorrectly recorded event within 24 hours of sending it. Must specify the event's `identifier`. Cancellations do not update finalized invoices. Negative quantities are also supported to offset incorrect usage (aggregate clamped to 0 if negative).

API: `stripe.billing.meterEventAdjustments.create({ type: 'cancel', event_name, cancel: { identifier } })`

**Price** — references a meter via `recurring.meter`; combined with `billing_scheme`, `transform_quantity`, and `unit_amount` to produce the charge. Can be mixed with flat recurring prices in a single subscription.

API: `recurring: { usage_type: 'metered', interval: 'month', meter: METER_ID }`

**Subscription** — links a customer to one or more prices; drives the billing cycle and invoice generation.

- `billing_mode=flexible`: no first invoice for metered items (recommended)
- `billing_mode=classic`: zero-value line item for metered items on first invoice

## Pricing Models

| Model | Description | API |
| --- | --- | --- |
| **Pay as you go** | Pure consumption billing | Meter API (v2) |
| **Flat fee + overages** | Flat base rate + arrears usage charges | This captured `usage-based-v1` guide uses `/v1/billing/meters`, `recurring.meter`, and `/v1/billing/meter_events`; the URL name alone does not establish a legacy `aggregate_usage` flow. See [[source-stripe-usage-based-billing-flat-fee-overages]]. |
| **Credit-based** | Pre-purchase credits drawn down by usage | Meter API (v2) |

> [!info] The captured flat fee and overages example uses two prices on one subscription: (1) a graduated metered price tied to a Billing Meter, with the first 1,000 units included, and (2) a $100 monthly licensed price. The May Node example uses `Decimal.from()`; the November curl example uses numeric form values, so `Decimal.from()` is not a general requirement. The guide's first-invoice caveat about metered lines should not erase the separate upfront licensed charge. See [[source-stripe-usage-based-billing-flat-fee-overages]].

> [!warning] Contradiction
> The May and November guide prose says 0.04 USD per hundred units, but the Dashboard tier says 0.04 USD per unit and the API tier has `unit_amount_decimal=4` in USD. Confirm the intended basis before implementing the sample rate; the captures contain no executed invoice result.

## Credit Grants

The matched Billing Credits guide describes prepaid or promotional Credit Grants that can apply to eligible metered-price subscription items at invoice finalization. Its 2026-05-05 capture carried a Public preview banner; the 2026-11-07 capture omits it, which does not establish general availability or account eligibility. Advanced UBB (private preview) burns in real time under separately sourced guidance.

**Use cases in the Billing Credits guide**: paid or free credits for memberships, pay-as-you-go plans, subscriptions, or specific merchant products and services. **Prohibited**: gift cards, stored value outside those approved merchant offerings, third-party payments, and digital-wallet linking.

**Credit grant states**:

| State | Description |
| --- | --- |
| Pending | `available_balance` not yet usable |
| Granted | Eligible based on `effective_at`; effective immediately if omitted, as the captured guide states |
| Depleted | Balance fully used |
| Expired | Reached `expires_at` or manually expired |
| Voided | Never applied to any invoice; can't be applied to future invoices |

> [!warning] Contradiction
> Both captures say `effective_at` must occur in the future and also say omitting it makes the grant effective immediately (new line 48; old line 40). This source does not establish a universal future-only validation rule.

**Eligibility** — grant applies to invoice if all 4 true: (1) invoice `period_end` ≥ grant `effective_at`; (2) invoice `period_end` < grant `expires_at` (if set); (3) grant has available balance at finalization; (4) currencies match. Cannot apply to one-off invoices, setup fee items, licensed-price items, or legacy Usage Records items.

**Application**: after discounts, before taxes and `invoice_credit_balance`. Credits apply only at finalization — preview/draft balances may change. No finalization order guarantee across subscriptions.

**Priority when multiple grants match**: (1) priority number, (2) earlier `expires_at`, (3) `promotional` before `paid`, (4) earlier `effective_at`, (5) earlier `created`.

**Ledger vs available balance**: the grant is backed by an immutable, append-only ledger of transactions, while its **ledger balance changes** as credits and debits are recorded. Available balance is the usable amount after expired credits or unrecorded transactions. The **100 unused-grants-per-customer** cap uses ledger balance, not available balance: a pending grant or a non-expired, non-voided grant with positive ledger balance counts, even if available balance is zero. A grant stops counting when a finalized invoice's credit application depletes ledger balance to zero, or the grant expires or is voided; invoice finalization alone does not suffice.

**Void & credit note**: voiding an invoice reinstates credits (immediately expired if grant past expiry). Credit notes do NOT reinstate credits — must create a new grant.

**Credit Grant API**: `stripe.billing.creditGrants.create({ customer, name, applicability_config: { scope: { price_type: 'metered' } }, category: 'paid', amount: { type: 'monetary', monetary: { value: 1000, currency: 'usd' } } })` — `value` in cents. To scope to a single price: pass `applicability_config.scope.billable_items[0].id`.

**Credit balance summary**: `stripe.billing.creditBalanceSummary.retrieve({ customer, filter: { type: 'applicability_scope', applicability_scope: { price_type: 'metered' } } })`

**Credit balance transactions**: `stripe.billing.creditBalanceTransactions.list({ customer, credit_grant })`

**Funding flow**: create invoice → add invoice item → finalize → `invoice.paid` webhook → grant credits.

## Subscription Management

**Transform quantity** — divide reported usage before pricing: `transform_quantity: { divide_by: 60, round: 'up' }`. Not compatible with tiered pricing.

**Mid-cycle price updates:**

- `billing_mode=flexible`: creates invoice item for prior metered usage immediately; `proration_behavior='none'` skips billing the removed price.
- `billing_mode=classic`: only usage after the update is billed at new price; pre-update usage lost unless re-reported or `billing_cycle_anchor=now` reset. Threshold invoices at old price still charged but don't offset end-of-period usage.

**Backdated subscriptions**: record usage first, then create subscription with `backdate_start_date` (Unix timestamp). Flexible: appears on first invoice. Classic: appears on next cycle invoice.

**Cancellation**: no proration supported. Canceled subscriptions cannot be reactivated — create new subscription. `cancel_at_period_end=true` reversible before period end. Final invoice includes all metered usage from last period.

## Monitoring and Alerts

The November 7, 2026 usage-alert guide invites requests for Usage Analytics API preview and early access to spend and credit balance alerts. Those invitations do not establish account access or describe those alerts' API behavior. See [[source-stripe-usage-based-billing-alerts-setup]] and https://docs.stripe.com/billing/subscriptions/usage-based/alerts.

Two mechanisms:

- **Usage alerts** — notify when a customer meets the configured meter usage threshold (the example uses `gte=100`). Evaluation happens on usage reported **after** alert creation and includes prior reported usage; creation alone is not described as an immediate trigger. Max **25 per meter+customer**; alerts don't work with test clocks. Use cases: email users, deprovision access, upsell sales team. See [[source-stripe-usage-based-billing-alerts-setup]].
- **Billing thresholds** — trigger an invoice when a customer reaches a spend amount.

**Alert API example**: `stripe.billing.alerts.create({ title, alert_type: 'usage_threshold', usage_threshold: { filters: [{ type: 'customer', customer }], meter, gte: 100, recurrence: 'one_time' } })`. This is a **customer-filtered** example; the captured API examples do not establish the all-customer request shape. `One-time per-customer` fires once when the customer meets the configured threshold and does not retrigger for later usage. Webhook event: `billing.alert.triggered`. The Dashboard separately defaults to **Any customer** and offers **Specific customer**. See [[source-stripe-usage-based-billing-alerts-setup]].

**Billing thresholds — API**:

- Monetary (subscription): `billing_thresholds[amount_gte]=10000` (smallest currency unit, min 50); `reset_billing_cycle_anchor=true` to reset cycle at threshold. Dashboard supported.
- Usage (subscription item): `billing_thresholds[usage_gte]=2000`. **API only** — Dashboard not supported.

Tiers are maintained across threshold invoices (reset only at period end, unless `reset_billing_cycle_anchor=true`). Volume tiers + thresholds can produce negative line items when tier boundary is crossed after a threshold invoice — excess credit goes to customer balance.

**Billing threshold constraints**: not on trial subscriptions; not evaluated in last 24h before subscription ends; monetary threshold must exceed sum of flat rates; monetary threshold excludes taxes but includes discounts and billing credits; one monetary threshold per subscription, one usage threshold per subscription item; per-package tiered pricing unsupported; invoiced amount may slightly exceed threshold; threshold invoices don't include grace period usage.

## Invoice Finalization Grace Period

Default: **1 hour**. Configurable up to **72 hours (3 days)** via Dashboard → Invoice settings. Stripe advises against setting the grace period longer than the service period; for daily service, it says not to use a grace period of 24 hours or more.

**Subscription-cycle invoices** and **subscription-schedule phase-transition invoices that modify metered items** can include usage reported during the finalization grace period. Other invoices, including **threshold invoices**, use usage recorded before invoice creation.

> [!warning] Contradiction
> The May capture and former summary named only cycling versus threshold invoices. The November guide adds qualifying phase transitions and warns that a mid-cycle subscription-item price change skips finalization recomputation: grace-period usage then appears on neither current nor subsequent invoices in classic or flexible subscriptions using billing meters. See [[source-stripe-usage-based-billing-configure-grace-period]].

Rules allow per-group overrides with conditions: "Invoice is from a subscription cycle", "Has a metered price", or both. When multiple rules match, the most conservative (longest) grace period wins. The first invoice of a subscription using `charge_automatically` finalizes immediately regardless of these rules; the captures do not extend this statement to first `send_invoice` invoices.

For ordinary eligible draft-invoice processing, usage timestamps must fall within that invoice's service period; a timestamp after draft creation routes usage to the next invoice. This does not override the November exceptions: usage reported beyond grace may appear in meter summaries but not the finalized or next invoice, and a mid-cycle subscription-item price change can omit grace-period usage from both current and subsequent invoices.

## Meter Event Error Handling

Stripe processes meter events asynchronously and emits **thin events** when errors occur:

| Event | Trigger |
| --- | --- |
| `v1.billing.meter.error_report_triggered` | Meter has invalid usage events |
| `v1.billing.meter.no_meter_found` | Events reference a missing/invalid meter ID |

Subscribe via Workbench event destination with **Thin** payload style. Fetch full details with `client.v2.core.events.retrieve(id)` → `event.fetchRelatedObject()`.

Error codes (`reason.error_types.code`): `meter_event_customer_not_found`, `meter_event_no_customer_defined`, `meter_event_dimension_count_too_high`, `archived_meter`, `timestamp_too_far_in_past`, `timestamp_in_future`, `meter_event_value_not_found`, `meter_event_invalid_value`, `no_meter`.

## Sources

- [[source-stripe-usage-based-billing-how-it-works]] — dated basic Billing Meters lifecycle and six definitions, with Stripe's 2026-11-07 Metronome recommendation for new integrations and asynchronous summary qualification
- [[source-stripe-usage-based-billing-use-cases]] — three pricing model index: pay-as-you-go, flat fee + overages (v1 only), credit-based
- [[source-stripe-usage-based-billing-payg]] — pay-as-you-go end-to-end: meter + price + customer + subscription + meter events + preview invoice + event summaries
- [[source-stripe-usage-based-billing-flat-fee-overages]] — captured flat fee + overages example: Meter API, graduated metered and licensed prices, scoped Accounts v2/Customers v1 routes, contradictory rate wording, and qualified invoice timing
- [[source-stripe-usage-based-billing-credits]] — credit-based pricing: credit grants, burn timing, balance summary/transactions, funding flow, meter dimensions
- [[source-stripe-usage-based-billing-recording-usage]] — ingestion methods index: API, Dashboard CSV, Amazon S3; async processing note
- [[source-stripe-usage-based-billing-meters-configure]] — meter config attributes table, Raw vs Pre-aggregated ingestion modes, immutability rule, Meter Event Adjustment API
- [[source-stripe-usage-based-billing-recording-usage-api]] — API ingestion deep-dive: rate limits, API v2 high-throughput streams, timestamp constraints, idempotency, async error events + 9 error codes
- [[source-stripe-usage-based-billing-recording-usage-dashboard]] — Dashboard ingestion: manual input + CSV upload (5 MB limit, field schema, error file workflow)
- [[source-stripe-usage-based-billing-recording-usage-s3]] — Amazon S3 ingestion: connector setup, polling behavior, rate limits, two-tier error handling
- [[source-stripe-usage-based-billing-configure-grace-period]] — May and November 2026 invoice-finalization guide: 1h default, up to 72h rules, eligible cycle/phase invoices, timestamp and price-change limits
- [[source-stripe-usage-based-billing-credits-overview]] — Billing Credits overview: May 2026 Public preview label; November 2026 capture adds a rendered relationship diagram and preserves eligibility, priority, ledger-balance cap, and void/Credit Note rules without proving GA
- [[source-stripe-usage-based-billing-credits-setup]] — billing credits setup guide: create grant (+ billable_items price-level scoping), apply to invoices, retrieve balance, list transactions, funding flow
- [[source-stripe-usage-based-billing-monitor-usage-alerts]] — monitoring hub: usage alerts (25/meter+customer, retroactive eval) vs billing thresholds (invoice trigger), 8 threshold constraints
- [[source-stripe-usage-based-billing-alerts-setup]] — usage alert setup: create API, one-time per-customer type, billing.alert.triggered webhook, test clock limitation
- [[source-stripe-usage-based-billing-thresholds-setup]] — billing thresholds setup: monetary + usage APIs, reset_billing_cycle_anchor, tiers across invoices, volume tiers negative line item edge case
- [[source-stripe-usage-based-billing-manage-setup]] — UBB management: transform_quantity, mid-cycle price updates (flexible vs classic), backdated subscriptions, cancellation behavior
- [[source-github-ai]] — exact-SHA implementation evidence for Stripe LLM token metering, event payloads, and fire-and-forget delivery risk
