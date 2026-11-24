---
title: "Stripe Radar"
type: concept
category: technology
tags: [stripe, radar, fraud, fraud-detection, rules-engine, risk, machine-learning, block-list, 3ds, connect]
---

## Overview

Stripe Radar evaluates transaction fraud, account risk and customer abuse in its November 2026 overview.

## Dated plan coverage

May 2026 describes Stripe Radar, Radar for Fraud Teams and Radar for Platforms. November lists Lite, Standard, Plus and Pro. All four list card fraud prevention, card testing prevention and alerts. Standard and above add expanded and all-supported-method protections, default rules/lists, analytics and risk levels, and account manual reviews. Plus and above add transaction scores and manual reviews, custom controls and advanced features. Pro adds dynamic transaction risk thresholds and customer abuse controls. See [[source-stripe-radar-how-it-works]] for the transaction, account and customer matrices. The captures give no May-to-November plan mapping.

## Pricing

The November overview charges Standard, Plus and Pro for screened authorizations and charges. For Stripe Billing it documents the first payment and the first payment after a method change, a configurable number of successful renewal cycles to screen, and no fee for skipped renewals. On a free trial the first screen is when the customer is charged. May described only a first-transaction fee exception for Billing. This fee wording is separate from the earlier model scoring and rules evaluation guidance.

For Connect, the November guide says Stripe charges the platform the Radar account fee. A screened transaction uses the collecting account's rate. A collecting platform can pass on fees by reducing its transfer. See [[source-stripe-radar-how-it-works]].

## Payment Methods Screened

May lists cards, card-backed wallets, ACH and SEPA Direct Debit, with other payment method controls in preview. November screens supported successful, declined, blocked and review-flagged attempts. Its all-payment-methods prevention row starts at Standard. The same-day supported-method guide describes broad default protection but scopes default high-risk controls to Standard and above and says Stripe may still block Lite payments. Custom settings depend on plan. Use `:payment_method_type:` to target a method within eligible rules. See [[source-stripe-radar-supported-payment-methods]].

Both Radar overviews exclude non-card SetupIntents. The separate May Risk evaluations guide describes enabling Radar for SetupIntents when using cards. See [[source-stripe-radar-risk-evaluation]].

## Rules (Custom + Built-in)

**4 actions**: Request 3DS, Allow (override everything — use minimally), Block, Review; Platforms also: Pause payouts.

**Built-in**: `if :risk_level: = 'highest'` (deprecated), `if :risk_level: = 'elevated'` (review); CVC/AVS rules (risk-score-based since Dec 2024). Platforms add `:account_risk_level:` rules.

**Rule syntax**: `{action} if {attribute} {operator} {value}`. Metadata: `::field::`. List membership: `:attr: in @list`. Max 200 transaction + 100 account rules. Backtests against last 6 months.

The April 2026 [[source-stripe-payment-intents#Descriptor and metadata boundaries|Payment Intents guide]] names Radar for Fraud Teams for custom metadata rules. Its November capture calls the product Radar Plus in equivalent guidance. The dated labels leave plan equivalence, eligibility, and any rename date unresolved.

**3DS attributes**: `is_3d_secure` (recommended for block), `is_3d_secure_authenticated` (stricter), `has_liability_shift`. Exclude wallets: `not(:digital_wallet: = 'android_pay' and :has_cryptogram:)`.

**Radar Assistant**: LLM writes rules from natural language (training consent required). EU note: geo-blocking regulation prohibits blocking EU customers by location. See [[source-stripe-radar-rules]].

**Dispute resolution rules**: `Resolve dispute if {condition}` — auto-refunds matching disputes (requires dispute prevention signup). Dispute-specific attributes: `amount_in_xyz` (disputed amount), `is_fraudulent`, `card_brand` (visa/mc only), `network_reason_code` (Visa only). See [[source-stripe-radar-rules-disputes]].

**Rule reference details**: Missing attributes always return false (use `is_missing()` to check explicitly). Velocity attributes use bucket windows (hourly = 3900s/5min buckets). `amount_in_xyz` auto-converts currency. Metadata is case-sensitive; customer/destination/account scopes available (`::customer:field::`). Post-authorization attributes (CVC/AVS) may cause temporary auth hold. See [[source-stripe-radar-rules-reference]].

## Block and allow lists

Radar rules can reference reusable lists for allow, block or review. Default lists cover Cards, ACH and SEPA. Merchants can change their items while Stripe keeps the default lists fixed. May named Radar for Fraud Teams for custom lists. The November plan matrix lists default lists on Standard, Plus and Pro and custom lists on Plus and Pro.

**Custom list types**. Both lists guides describe ten entries. Each list can hold up to 50,000 items. Default fingerprint allowlist entries last at most 30 days. Custom payment-method fingerprint lists can have longer or indefinite expiration when used in custom rules. See [[source-stripe-radar-lists]] for the dated API enum and expiration scope.

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

**Integration evidence**. May and November recommend Payment Links, Checkout and Elements with customer risk factors. The captured completeness columns are blank. The percentages above are Stripe’s model estimates for individual factors. See [[source-stripe-radar-optimize-risk-factors]] for the full dated integration rows and factor scopes.

**Key practices**. Stripe recommends including Stripe.js on every page and instructs merchants to always load it directly from Stripe’s hosted URL. Reuse Customer objects and disclose device collection. Stripe scans per Charge, including Charges generated across retries. Charge-free setup scans are off by default. Use the Radar settings opt-in to scan SetupIntents. See [[source-stripe-radar-optimize-risk-factors]] for the dated Dahlia and Endive script instructions and setting.

## Radar for Platforms

Extends Radar to Connect platforms with connected account risk scoring (`highest` ≥90% loss probability, `elevated` 50-89%) and investigation tools.

**Connected account rules**: Raise review OR Pause payouts + review. **Transaction rules**: same as other tiers.

**Risk tab**: agent-generated indicators (suspicious network, location mismatch), risk metrics (disputes/refunds/declines time-series), risk history with notes.

**Actions**: reject (7 reason codes: fraud_card_casher, fraud_no_intent_to_fulfill, credit, etc. — hard to reverse), set reserves, pause payments/payouts, request identity verification (gov ID + selfie), dismiss review.

**Platform payment controls**: platform-only (overrides connected accounts) or shared (platform rules first). Permissions: Connect Risk Analyst role required.

**Account Signals API.** The May 2026 overview links a dated preview and describes fraudulent merchant, merchant delinquency risk and on-demand fraudulent website evaluations. The November overview adds payment delinquency exposure, a conditional estimate of dispute and refund dollars at risk. It describes a 90-day lookup period after creation for signals and evaluations, omits older signals from lists, and illustrates notification, retrieval and a platform action decision.

The separate November merchant guide uses `2026-10-28.preview`, documents Radar Standard or higher and limits certain detail fields to Plus and Pro. It shows a thin readiness event followed by an API fetch. The website guide also documents thin events and retrieval. It allows sandbox testing on any Radar plan and specifies Plus or Pro and a 4,000-request monthly limit for live evaluation. See [[source-stripe-radar-account-risk-signals]] for each signal contract and [[source-stripe-radar-for-platforms]] for review and account actions.

## Fraud Insights

The May 2026 Insights guide names Radar for Fraud Teams for Dashboard access. November names Radar Plus. The separate November plan table lists agentic insights for Plus and Pro and transaction fraud alerts for all four listed plans. The dated material leaves plan equivalence and account entitlements unresolved.

The initial Insights view shows the prior three months in near real time, with successful payments, risk score strictly above 65, and more than 10 charges per card number per hour. Available statuses include all payments, successful payments, all fraud, disputes and early fraud warnings. Operators can change the date range and attributes, pivot by day, week, month or an attribute such as risk score, and drill into individual payments. Refunds and changes to risk controls or rules are merchant decisions.

The November guide adds analysis of payments that triggered a fraud alert. An alert can yield one or more patterns for inspection in Insights, where the operator can see transaction details, fraud volume and dispute counts and decide whether to change rules or risk settings. See [[source-stripe-radar-fraud-insights]] for the dated workflow and [[source-stripe-radar-fraud-alerts]] for separate alert notifications and investigation.

## Fraud Alerts

Stripe auto-detects unusual patterns (e.g. risk score distribution shift) → email + Dashboard bell → alert investigation page with risk trend charts, elevated-risk payment list, and volume impact. Fraud Teams users also get Smart Refunds recommendations and targeted rule suggestions. Best practice: act quickly, look for common patterns (IP/billing address/card BIN). See [[source-stripe-radar-fraud-alerts]].

## Analytics Center

**May 10, 2026 Radar Overview.** Radar Analytics center was the default, with a toggle to the Legacy overview. The newer view defaults to 30 days after a 24-hour delay. It offers count or volume, fraud arrival or payment date, retry deduplication and optional SetupIntent inclusion. Fraud, all disputes, blocks and rule actions have separate panels.

**Legacy overview.** The six-month default includes the 3DS, Radar screening and dispute sequence, privacy-gated benchmark comparisons, modeled dispute projections and manual reviews for Radar for Fraud Teams. Legacy block rate uses attempted payments, while the newer view's May formula uses successful payments. Charts offer CSV download. View in Sigma requires Sigma access. The November capture links both views. See [[source-stripe-radar-analytics]].

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

## Multiprocessor Payment Evaluation

The May 2026 guide describes non-Stripe processing with a tokenized card, Radar Session and customer email. The November guide documents evaluations for any processor, approval-gated input alternatives for non-Stripe processing and a preview example for same-payment evaluation reuse when processing on Stripe. Both describe `fraudulent_payment` as the default and give blocking language for `fraudulent_dispute`. The response provides a recommendation and separate scores. The business server separately transacts with a third-party processor. See [[source-stripe-radar-multiprocessor]] for the dated signal, PCI and billing conditions.

## Bot Abuse Prevention

Bot score (0–99) assigned to **Stripe Checkout** payments only. High score = bot likely made payment (not fraud signal). Use for anti-scripting/anti-bot policies (e.g. limited-inventory). Access via Dashboard → payment → Risk scores, Sigma `radar_abuse_prevention_attributes.bot_score`, or custom Radar rule on `:bot_score:`. See [[source-stripe-radar-bot-abuse]].

## Pay-As-You-Go Abuse Evaluation

For usage-based / post-paid billing: detect intentional non-payment risk mid-billing cycle (background worker, not checkout). API: `POST /v1/radar/payment_evaluations` with `customer_presence=off_session`, `payment_type=recurring` + payment method + customer + invoice amount. No Radar Session needed. Read `signals.non_payment_abuse.risk_level` — ignore `fraudulent_payment` defaults. Fail-open (4xx/5xx doesn't affect billing). No outcome reporting required. See [[source-stripe-radar-payg-abuse]].

## Free Trial Abuse Prevention

Radar risk control that blocks high-risk trial starts before customers gain access. Predicts if subscription payment will fail when trial ends (common patterns: prepaid/virtual cards, repeated signups with same card).

Enable at Dashboard → Risk controls → Free trial abuse. Auto-detected with Checkout Sessions (subscription mode), `trial_period_days/end`, or 100% off coupons. Other integrations need metadata setup (contact Stripe). Monitor via `rule_decisions` table with `block_if_high_free_trial_abuse_risk`. See [[source-stripe-radar-free-trial-abuse]].

## Custom Fraud Models

Custom models use structured merchant signals on payment objects, such as `PaymentIntent.metadata`, and enough transaction history for Stripe's onboarding review. In the May and November 2026 guides, Stripe trains with global and merchant signals. After deployment, a score combining those signals becomes available without another integration change, and Stripe retrains the model as patterns change. The November guide also documents an email-based preview request. See [[source-stripe-radar-custom-fraud-models]].

## Advanced Fraud Detection (Stripe.js / Mobile SDKs)

Two risk factor types: **device characteristics** (browser/screen/device — identifies anomalous environments) and **activity indicators** (mouse movement, time-on-page, copy-paste detection — bot vs human). Activity signals are scoped to one shopping session on one site or app; page contents are collected only for matching Stripe Elements input fields. Stripe recommends Stripe.js throughout shopping for richer signals; on each page where it loads, it **can** load hCaptcha. Contact Stripe Support to opt out of hCaptcha integration.

Stripe prevents >$500M/month in fraud. Data never used for advertising.

**Disable advanced signals on your own site/app** (increases fraud risk): for Stripe.js, set `advancedFraudSignals=false` in the script-tag query parameter **or** use the latest pure module with `loadStripe.setLoadParameters({ advancedFraudSignals: false })`; the November HTML example does not remove the older module option. iOS SDK v19.1.1+ uses `StripeAPI.setAdvancedFraudSignalsEnabled(false)`; Android SDK v14.4.0+ uses `Stripe.advancedFraudSignalsEnabled = false` before any SDK object is accessed or instantiated. This does not stop collection on Stripe domains, Stripe-managed Elements events, or basic 3DS2 device information sent to issuers. See [[source-stripe-disputes-advanced-fraud-detection]].

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

- [[source-stripe-radar-how-it-works]] — May Radar labels and November plan matrices, method screening, Billing renewals and Connect fee attribution
- [[source-stripe-radar-optimize-risk-factors]] — Stripe’s estimated model impact, three recommended integration rows with blank captured completeness cells, and dated hosted-script and charge-free setup guidance.
- [[source-stripe-radar-sessions]] — Radar Sessions: when to use, integration flow, on/off-session attachment strategy
- [[source-stripe-radar-risk-evaluation]] — Risk levels/scores, outcome fields, object support matrix, feedback loop, network coverage
- [[source-stripe-radar-custom-fraud-models]] — May and November custom-model guides on preview access, merchant metadata, volume assessment, and post-deployment scores
- [[source-stripe-disputes-advanced-fraud-detection]] — Advanced fraud detection: device+activity risk factors, Stripe.js on every page, hCaptcha, disable options
- [[source-stripe-radar-customer-evaluation]] — Customer Evaluation API: multi_accounting + account_sharing signals, score/risk levels, lifecycle flow
- [[source-stripe-radar-free-trial-abuse]] — Free trial abuse: blocks high-risk trial starts, auto-detected with Checkout Sessions, Sigma monitoring
- [[source-stripe-radar-payg-abuse]] — PAYG abuse: non_payment_abuse signal, fail-open Payment Evaluation API, mid-cycle background evaluation
- [[source-stripe-radar-bot-abuse]] — Bot score (0-99) for Checkout payments: anti-scripting policy enforcement, Sigma query, Radar rules
- [[source-stripe-radar-multiprocessor]] — May and November 2026 Payment Evaluation guides for external and Stripe processing, dated access and input scope, risk responses and evaluation reuse.
- [[source-stripe-radar-issuing]] — Radar for Issuing: IssuingAuthorizationEvaluation API, pre-authorization fraud scoring, physical + tokenized cards
- [[source-stripe-radar-risk-settings]] — Risk settings (3 presets), 4 risk controls, 5 Radar scores, deprecation of risk_score
- [[source-stripe-radar-supported-payment-methods]] — PM coverage: cards+ACH+SEPA fully supported; BNPL/wallets/stablecoin preview; :payment_method_type: attribute
- [[source-stripe-radar-reviews]] — Review queue: Smart Refunds, actions, assignments, webhooks, best practices
- [[source-stripe-radar-risk-insights]] — Risk insights: fraud factor numbers, top factors, customer signals, related payments (6-month limit)
- [[source-stripe-radar-reviews-auth-capture]] — Auth-and-capture review: approve ≠ capture; Cancel vs Refund; review.closed webhook auto-capture pattern
- [[source-stripe-radar-lists]] — May and November 2026 guides with default lists, ten custom entries in the guide, separate API enum, item expiry and card fraud-feedback effects.
- [[source-stripe-radar-rules]] — Rules: 4 actions, built-in rules, syntax, 3DS attributes, Radar Assistant, EU geo-blocking note
- [[source-stripe-radar-rules-reference]] — Rules reference: processing order, attribute types, operators, missing attributes, velocity buckets, metadata scopes
- [[source-stripe-radar-rules-supported-attributes]] — Supported attributes: 5 categories, risk/IP/email/distance/fingerprint/time/crypto (827 lines)
- [[source-stripe-radar-testing]] — Test cards (highest/elevated risk), rule backtesting framework, when to implement each rule type
- [[source-stripe-radar-rules-disputes]] — Dispute resolution rules: Resolve dispute action, dispute-specific attributes (is_fraudulent, network_reason_code)
- [[source-stripe-radar-analytics]] — May 2026 Radar Analytics center and legacy reporting, view-specific metrics, cohort benchmarks and Sigma access. November links the two views.
- [[source-stripe-radar-fraud-alerts]] — Fraud alerts: auto-detected attacks, email+bell notification, investigation page, Fraud Teams extra actions
- [[source-stripe-radar-fraud-insights]] covers the May and November 2026 Dashboard workflows, dated plan terms, initial filters and the November alert-triggered analysis.
- [[source-stripe-radar-for-platforms]] — Radar for Platforms: connected account risk scores, investigation tools, reject (7 codes), reserves, API signals
- [[source-stripe-radar-account-risk-signals]] — May and November 2026 Account Signals API overviews, four November signal routes, 90-day lookup and list scope, and separate guides to plan, event and retrieval behavior.
