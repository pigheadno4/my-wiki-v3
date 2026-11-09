---
title: "Stripe Radar"
type: concept
category: technology
tags: [stripe, radar, fraud, fraud-detection, rules-engine, risk, machine-learning, block-list, 3ds, connect]
---

## Overview

Stripe Radar is Stripe's real-time fraud protection system using AI/ML. Available in three tiers with no additional development time required for the base tier.

## Product Tiers

| Tier | Key capability |
| --- | --- |
| **Stripe Radar** | AI fraud detection built into every Stripe account |
| **Radar for Fraud Teams** | Custom rules engine, risk insights, trend analysis |
| **Radar for Platforms** | Adds account-level risk protection for Connect platforms |

## Pricing

Fee per evaluated transaction across all attempt types (successful, declined, blocked, flagged for review).

**Stripe Billing exception**: only billed for the first transaction of a recurring series — subsequent transactions are free.

Radar for Platforms adds a per-connected-account fee.

## Payment Methods Screened

Default protection (all users): all payment methods blocked at high risk. Custom risk settings (Fraud Teams/Platforms):

| Support level | Payment methods |
| --- | --- |
| Full | Cards (credit/debit/Apple Pay/Google Pay), ACH, SEPA |
| Private preview | ACSS, AU BECS, Bacs, NZ BECS, PayTo; BNPL (Affirm, Afterpay, Klarna); Cash App, PayPal; Stablecoin/crypto |

Use `:payment_method_type:` attribute to target specific PMs in rules. See [[source-stripe-radar-supported-payment-methods]].

**Not screened**: SetupIntents for non-card payment methods (unless enabled in settings).

## Rules (Custom + Built-in)

**4 actions**: Request 3DS, Allow (override everything — use minimally), Block, Review; Platforms also: Pause payouts.

**Built-in**: `if :risk_level: = 'highest'` (deprecated), `if :risk_level: = 'elevated'` (review); CVC/AVS rules (risk-score-based since Dec 2024). Platforms add `:account_risk_level:` rules.

**Rule syntax**: `{action} if {attribute} {operator} {value}`. Metadata: `::field::`. List membership: `:attr: in @list`. Max 200 transaction + 100 account rules. Backtests against last 6 months.

**3DS attributes**: `is_3d_secure` (recommended for block), `is_3d_secure_authenticated` (stricter), `has_liability_shift`. Exclude wallets: `not(:digital_wallet: = 'android_pay' and :has_cryptogram:)`.

**Radar Assistant**: LLM writes rules from natural language (training consent required). EU note: geo-blocking regulation prohibits blocking EU customers by location. See [[source-stripe-radar-rules]].

**Dispute resolution rules**: `Resolve dispute if {condition}` — auto-refunds matching disputes (requires dispute prevention signup). Dispute-specific attributes: `amount_in_xyz` (disputed amount), `is_fraudulent`, `card_brand` (visa/mc only), `network_reason_code` (Visa only). See [[source-stripe-radar-rules-disputes]].

**Rule reference details**: Missing attributes always return false (use `is_missing()` to check explicitly). Velocity attributes use bucket windows (hourly = 3900s/5min buckets). `amount_in_xyz` auto-converts currency. Metadata is case-sensitive; customer/destination/account scopes available (`::customer:field::`). Post-authorization attributes (CVC/AVS) may cause temporary auth hold. See [[source-stripe-radar-rules-reference]].

## Block/Allow Lists (Fraud Teams)

Reusable value collections used in Radar rules. Default lists cover Cards (BIN, country, fingerprint, IP, email, customer ID), ACH (fingerprint + shared), SEPA (fingerprint + shared). Cannot delete default lists.

**Custom list types**: String, Case-sensitive string, Card fingerprint, Card BIN, Customer ID, Email, IP address, Country, SEPA/ACH fingerprint. Up to 50,000 items. Default fingerprint allowlists: 30-day max lifespan. Custom lists can have indefinite expiration.

**Fraud report auto-populates block lists**: card fingerprint(s) + email from `receipt_email`/Customer.email/description fields. See [[source-stripe-radar-lists]].

## Risk Insights (Fraud Teams)

Explains why Radar scored a payment. Available for last 6 months only; not in sandbox. Shows: fraud factor numbers (multiplier vs Stripe average, e.g. 3.5x), top fraud factors, customer signals (name/email match, email auth rate on network), geography (billing/shipping/IP), and related payments (same IP/card — detect card testing and trial abuse). See [[source-stripe-radar-risk-insights]].

## Review Queue (Fraud Teams)

Manual review queue for elevated-risk payments. Most PMs supported except ACH/SEPA direct debit. Two views: list (quick scan) + detailed (risk insights + related payments by email/IP/card; `J`/`K` nav).

**Smart Refunds**: post-completion fraud recommendations — Very high (72% dispute chance) to Very low (15%).

**Auth-and-capture flow**: approving a review ≠ capturing — separate actions. Uncaptured payments show Cancel (not Refund). Auto-capture pattern: `capture_method: 'manual'` → check `paymentIntent.review` → if empty capture immediately; else wait for `review.closed` webhook with `reason === 'approved'`. See [[source-stripe-radar-reviews-auth-capture]].

**Actions**: Approve, Refund, or Refund+report fraud (adds email + card fingerprint to block lists). Disputed payment → review auto-closed. Webhooks: `review.opened`, `review.closed`. See [[source-stripe-radar-reviews]].

## Core Features

| Feature | What it does |
| --- | --- |
| AI fraud detection | Real-time risk scoring; risk controls auto-block elevated/high-risk payments |
| Custom rules engine | Business-specific rules; auto-responses to risk levels; dispute resolution rules |
| Risk insights | Per-payment risk factors; suspicious pattern detection across transactions |
| 3DS integration | Trigger 3D Secure for high-risk card transactions via rules |
| Block/allow lists | Manage by email, IP, card fingerprint, metadata, payment method |
| Real-time monitoring | View and respond to fraud activity as it happens |

## How Radar Blocking Appears

When Radar blocks a payment, `Charge.outcome.type = "blocked"` and `network_status = "not_sent_to_network"`. See [[stripe-declines]] for full `outcome` object reference.

## Radar and Dispute Prevention

Radar rules power the **Resolution** tool in dispute prevention (RDR/Ethoca rules). Radar for Fraud Teams includes win-likelihood scoring (1–5 dots) for incoming disputes. See [[disputes]] for dispute prevention integration.

## Risk Factor Impact

The more data you provide, the better Radar performs. Estimated improvements from each data type:

| Data | Model improvement |
| --- | --- |
| Advanced risk factors (device signals via Stripe.js / SDKs / Radar Sessions) | +36% |
| IP address | +12% |
| Customer email | +11% |
| Customer name | +3% |
| Billing address | +1% |

**Integration ranking** (best → worst): Payment Links / Checkout / Elements+customer → Direct API + Radar Sessions + customer → Direct API + client+customer → Direct API alone.

**Key practices**: include Stripe.js on every page; use Customer objects; enable Radar for SetupIntents in settings; update privacy policy to disclose Stripe's device data collection. See [[source-stripe-radar-optimize-risk-factors]].

## Radar for Platforms

Extends Radar to Connect platforms with connected account risk scoring (`highest` ≥90% loss probability, `elevated` 50-89%) and investigation tools.

**Connected account rules**: Raise review OR Pause payouts + review. **Transaction rules**: same as other tiers.

**Risk tab**: agent-generated indicators (suspicious network, location mismatch), risk metrics (disputes/refunds/declines time-series), risk history with notes.

**Actions**: reject (7 reason codes: fraud_card_casher, fraud_no_intent_to_fulfill, credit, etc. — hard to reverse), set reserves, pause payments/payouts, request identity verification (gov ID + selfie), dismiss review.

**Platform payment controls**: platform-only (overrides connected accounts) or shared (platform rules first). Permissions: Connect Risk Analyst role required.

**API signals (private preview)**: account fraud, account insolvency, fraudulent website — webhook-driven via Account Signals API. See [[source-stripe-radar-for-platforms]] and [[source-stripe-radar-account-risk-signals]].

## Fraud Insights (Fraud Teams)

Dashboard → Radar → Insights tab. Default filters: risk score >65 + >10 charges/card/hour. 3-month near-real-time view. Payment status filter: All/Successful/All fraud/Disputes/EFWs. Pivot chart by Day/Week/Month or attribute dimension (risk score stacks into 0-9, 10-19 ranges). Transaction list with drill-down. Actions: refund individual, enable risk controls, write rules. See [[source-stripe-radar-fraud-insights]].

## Fraud Alerts

Stripe auto-detects unusual patterns (e.g. risk score distribution shift) → email + Dashboard bell → alert investigation page with risk trend charts, elevated-risk payment list, and volume impact. Fraud Teams users also get Smart Refunds recommendations and targeted rule suggestions. Best practice: act quickly, look for common patterns (IP/billing address/card BIN). See [[source-stripe-radar-fraud-alerts]].

## Analytics Center

Dashboard → Radar Overview. Two views: new Analytics Center (default) and Legacy overview (toggle).

**New view**: Fraud/Disputes/Blocks rate charts with peer benchmark comparison; rule match breakdown (Blocked/3DS/Allow/Review details); monitoring program status tracking. Configurable: volume vs count, fraud arrival date, de-duplicate retries, include SetupIntents. 24-hour delay; defaults to prior 30 days.

**Legacy view**: Overview Chart (3DS→Screened→Disputed flow), benchmarks (block rate, fraud dispute rate, false positive estimate), fraudulent disputes chart with projected maximum (dashed line). Each chart has CSV download + View in Sigma. See [[source-stripe-radar-analytics]].

## Test Cards

| Risk level | Card number | PaymentMethod |
| --- | --- | --- |
| `highest` (rules apply) | `4000000000004954` | `pm_card_riskLevelHighest` |
| `highest` (always blocked) | `4100000000000019` | `pm_card_chargeDeclinedFraudulent` |
| `elevated` | `4000000000009235` | `pm_card_riskLevelElevated` |

Rule backtesting covers last 6 months of live mode payments; shows disputes/EFWs, refunds, blocked/succeeded counts + Overrides for allow rules. See [[source-stripe-radar-testing]].

## Risk Settings and Controls

**3 preset risk settings** (Dashboard → Risk controls): Maximize protection → Balance → Maximize revenue. Each tunes blocking thresholds across 4 risk controls. Selecting a risk setting disables the legacy `Block if :risk_level: = 'highest' default` rule (migration since March 1, 2026).

**4 risk controls**: Fraudulent dispute (backtest + custom threshold in Fraud Teams), Early fraud warning (Maximize protection only; recommended for VAMP), Adaptive 3DS (liability shift on auth; SCA overrides disable), Fraudulent non-card payments (auto-enabled).

**5 Radar scores**:

| Score | Rule attribute | Status |
| --- | --- | --- |
| Fraudulent dispute score (0–99, cards+ACH+SEPA) | `:fraudulent_dispute_score:` | Active |
| Early fraud warning score (0–99, cards only) | `:early_fraud_warning_score:` | Active |
| Bot score (0–99, Checkout only) | `:bot_score:` | Preview |
| Risk score (0–99) | `:risk_score:` | **Deprecated** |
| Overall risk level (max of above) | `:risk_level:` | Active |

Custom rules never overridden by risk settings. See [[source-stripe-radar-risk-settings]].

## Risk Levels and Scoring

Risk score range: 0–99 (Radar for Fraud Teams only). Default thresholds: ≥75 = high, ≥65 = elevated.

| `risk_level` | Default action | `outcome.type` |
| --- | --- | --- |
| `highest` | Blocked | `blocked` |
| `elevated` | Allowed; auto-queued for review (Fraud Teams) | `manual_review` |
| `normal` | Allowed | `authorized` |
| `not_assessed` | Allowed (non-card/ACH/SEPA, opted-out) | `authorized` |
| `unknown` | Allowed (evaluation error) | `authorized` |

**Radar object support**: Charges (no 3DS), PaymentIntents (all), SetupIntents (no review). Billing: only scores first recurring payment; evaluates rules for all.

**Feedback loop**: refund with `reason: 'fraudulent'` → adds email + card fingerprint to block lists; AI model learns from it.

**Network coverage**: 92% cards seen before, 82% SEPA, 71% ACH.

See [[source-stripe-radar-risk-evaluation]].

## Customer Evaluation API (Upfunnel Risk)

Risk signals at registration and login — **before any payment** is collected. Detects:

- `multi_accounting`: same actor registering multiple accounts (on `registration` events)
- `account_sharing`: same account used from multiple locations simultaneously (on `login` events)

Score 0–100, same `risk_level` bands as payment (`highest`/`elevated`/`normal`). Requires Radar Session as prerequisite. Report outcomes (`registration_success|failed`, `login_success|failed`) to improve model. **Must reuse same Customer ID at payment time** to connect lifecycle signals. Preview API (`Stripe-Version: 2026-03-04.preview`). See [[source-stripe-radar-customer-evaluation]].

## Radar for Issuing

IssuingAuthorizationEvaluation API: real-time fraud risk scoring for Stripe Issuing card authorizations before approving or declining. Works with physical and tokenized cards. Supports automated approval workflows for Issuing programs. See [[source-stripe-radar-issuing]].

## Multiprocessor (External Payment Evaluation)

Evaluate non-Stripe-processed payments with Radar at any point in the payment lifecycle. Signals: `fraudulent_payment` (default), `fraudulent_dispute` (preview, blocks), `early_fraud_warning` (preview). Prerequisites: tokenized PaymentMethod (card only) + Radar Session + customer email. API: `POST /v1/radar/payment_evaluations`. See [[source-stripe-radar-multiprocessor]].

## Bot Abuse Prevention

Bot score (0–99) assigned to **Stripe Checkout** payments only. High score = bot likely made payment (not fraud signal). Use for anti-scripting/anti-bot policies (e.g. limited-inventory). Access via Dashboard → payment → Risk scores, Sigma `radar_abuse_prevention_attributes.bot_score`, or custom Radar rule on `:bot_score:`. See [[source-stripe-radar-bot-abuse]].

## Pay-As-You-Go Abuse Evaluation

For usage-based / post-paid billing: detect intentional non-payment risk mid-billing cycle (background worker, not checkout). API: `POST /v1/radar/payment_evaluations` with `customer_presence=off_session`, `payment_type=recurring` + payment method + customer + invoice amount. No Radar Session needed. Read `signals.non_payment_abuse.risk_level` — ignore `fraudulent_payment` defaults. Fail-open (4xx/5xx doesn't affect billing). No outcome reporting required. See [[source-stripe-radar-payg-abuse]].

## Free Trial Abuse Prevention

Radar risk control that blocks high-risk trial starts before customers gain access. Predicts if subscription payment will fail when trial ends (common patterns: prepaid/virtual cards, repeated signups with same card).

Enable at Dashboard → Risk controls → Free trial abuse. Auto-detected with Checkout Sessions (subscription mode), `trial_period_days/end`, or 100% off coupons. Other integrations need metadata setup (contact Stripe). Monitor via `rule_decisions` table with `block_if_high_free_trial_abuse_risk`. See [[source-stripe-radar-free-trial-abuse]].

## Custom Fraud Models

Extends Radar's global model with business-specific metadata (e.g. account age, VIP status, session duration, product category, internal risk scores). Requires: structured metadata on PaymentIntent objects + sufficient payment volume. No integration changes after setup — new risk score replaces global one automatically. Model retrains as business evolves. See [[source-stripe-radar-custom-fraud-models]].

## Advanced Fraud Detection (Stripe.js / Mobile SDKs)

Two risk factor types: **device characteristics** (browser/screen/device — identifies anomalous environments) and **activity indicators** (mouse movement, time-on-page, copy-paste detection — bot vs human). Scoped to single session; page contents only collected if matching Stripe Elements fields. Include Stripe.js on **every page** for richest signals; hCaptcha also loaded per page.

Stripe prevents >$500M/month in fraud. Data never used for advertising.

**Disable** (increases fraud risk): `loadStripe.setLoadParameters({advancedFraudSignals: false})` (JS), `StripeAPI.setAdvancedFraudSignalsEnabled(false)` (iOS v19.1.1+), `Stripe.advancedFraudSignalsEnabled = false` (Android v14.4.0+). **Cannot disable**: Stripe Elements events or 3DS2 device info. See [[source-stripe-disputes-advanced-fraud-detection]].

## Radar Sessions

For direct API / third-party tokenization flows where Stripe.js isn't present. Captures IP, browser, device characteristics as a snapshot at checkout time.

- **Don't use** if using Payment Links, Checkout, Elements, or mobile SDKs (auto-captured)
- Client: `stripe.createRadarSession()` → send ID to server
- Server: attach via `radar_options: { session: id }` on PaymentMethod and/or PaymentIntent
- **On-session**: attach to both PaymentMethod + PaymentIntent (with `confirm: true`) for best results
- **Off-session**: attach to PaymentMethod creation only
- Mobile: iOS SDK ≥v21.6.0, Android ≥v16.9.0

See [[source-stripe-radar-sessions]].

## Sources

- [[source-stripe-radar-how-it-works]] — Radar overview: tiers, pricing, payment methods, features
- [[source-stripe-radar-optimize-risk-factors]] — Risk factor impact table, integration ranking, best practices
- [[source-stripe-radar-sessions]] — Radar Sessions: when to use, integration flow, on/off-session attachment strategy
- [[source-stripe-radar-risk-evaluation]] — Risk levels/scores, outcome fields, object support matrix, feedback loop, network coverage
- [[source-stripe-radar-custom-fraud-models]] — Custom fraud models: business metadata signals, requirements, how it works, high-impact metadata types
- [[source-stripe-disputes-advanced-fraud-detection]] — Advanced fraud detection: device+activity risk factors, Stripe.js on every page, hCaptcha, disable options
- [[source-stripe-radar-customer-evaluation]] — Customer Evaluation API: multi_accounting + account_sharing signals, score/risk levels, lifecycle flow
- [[source-stripe-radar-free-trial-abuse]] — Free trial abuse: blocks high-risk trial starts, auto-detected with Checkout Sessions, Sigma monitoring
- [[source-stripe-radar-payg-abuse]] — PAYG abuse: non_payment_abuse signal, fail-open Payment Evaluation API, mid-cycle background evaluation
- [[source-stripe-radar-bot-abuse]] — Bot score (0-99) for Checkout payments: anti-scripting policy enforcement, Sigma query, Radar rules
- [[source-stripe-radar-multiprocessor]] — Multiprocessor: evaluate non-Stripe payments, 3 signals (fraudulent_payment/dispute/EFW), card-only
- [[source-stripe-radar-issuing]] — Radar for Issuing: IssuingAuthorizationEvaluation API, pre-authorization fraud scoring, physical + tokenized cards
- [[source-stripe-radar-risk-settings]] — Risk settings (3 presets), 4 risk controls, 5 Radar scores, deprecation of risk_score
- [[source-stripe-radar-supported-payment-methods]] — PM coverage: cards+ACH+SEPA fully supported; BNPL/wallets/stablecoin preview; :payment_method_type: attribute
- [[source-stripe-radar-reviews]] — Review queue: Smart Refunds, actions, assignments, webhooks, best practices
- [[source-stripe-radar-risk-insights]] — Risk insights: fraud factor numbers, top factors, customer signals, related payments (6-month limit)
- [[source-stripe-radar-reviews-auth-capture]] — Auth-and-capture review: approve ≠ capture; Cancel vs Refund; review.closed webhook auto-capture pattern
- [[source-stripe-radar-lists]] — Lists: default (Cards/ACH/SEPA), 11 custom types, 50k limit, 30-day allowlist max, fraud report auto-population
- [[source-stripe-radar-rules]] — Rules: 4 actions, built-in rules, syntax, 3DS attributes, Radar Assistant, EU geo-blocking note
- [[source-stripe-radar-rules-reference]] — Rules reference: processing order, attribute types, operators, missing attributes, velocity buckets, metadata scopes
- [[source-stripe-radar-rules-supported-attributes]] — Supported attributes: 5 categories, risk/IP/email/distance/fingerprint/time/crypto (827 lines)
- [[source-stripe-radar-testing]] — Test cards (highest/elevated risk), rule backtesting framework, when to implement each rule type
- [[source-stripe-radar-rules-disputes]] — Dispute resolution rules: Resolve dispute action, dispute-specific attributes (is_fraudulent, network_reason_code)
- [[source-stripe-radar-analytics]] — Analytics Center: fraud/dispute/block rate charts, benchmarks, rule match breakdown, legacy overview
- [[source-stripe-radar-fraud-alerts]] — Fraud alerts: auto-detected attacks, email+bell notification, investigation page, Fraud Teams extra actions
- [[source-stripe-radar-fraud-insights]] — Fraud insights: Insights tab, default filters (risk>65+velocity), pivot chart, payment status filter, drill-down actions
- [[source-stripe-radar-for-platforms]] — Radar for Platforms: connected account risk scores, investigation tools, reject (7 codes), reserves, API signals
- [[source-stripe-radar-account-risk-signals]] — Account Signals API: 3 signal types (fraud/delinquency/website), webhook-driven, actions table
