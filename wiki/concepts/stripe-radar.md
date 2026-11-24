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

**Transaction actions**. Custom rules depend on plan. Where supported, Request 3DS asks the issuer to authenticate for Checkout, Payment Intents and Setup Intents. The issuer might decline to perform 3DS. Radar continues to Allow, Block and Review whether or not the 3DS rule matches. Stripe also handles issuer-required 3DS and regulatory SCA when needed. Contact Stripe to create Allow rules. An Allow match skips later Radar Block and Review rules. The issuer can still decline. A Review match preserves normal payment processing and sends only successful payments to the queue. Platforms can review accounts or pause payouts and raise a review. See [[source-stripe-radar-rules]] and [[source-stripe-radar-rules-reference]].

**Built-in rules**. The legacy default `Block if :risk_level: = 'highest'` rule is being retired as accounts migrate to risk settings. The guides describe elevated-risk review and legacy or risk-score-based CVC and AVS Dashboard rules, with the latter change dated December 2024. The May account rules list `account_risk_level`. The November Rules guide lists `account_fraud_risk_level` for the two account-level risk predicates without assigning actions. The [[source-stripe-radar-rules-supported-attributes|November attributes reference]] separately lists `account_fraud_risk_level` and `account_fraud_risk_score` for account rules and `account_risk_level` for private-preview Treasury transaction rules.

**Rule syntax**: `{action} if {attribute} {operator} {value}`. Metadata: `::field::`. List membership: `:attr: in @list`. Max 200 transaction + 100 account rules. The Radar rules guide documents a six-month simulation of charges in its Review rules section. The separate testing guide describes historical live-mode payments without giving a duration.

**Traffic allocation**. November documents staged rollout or rollback for custom transaction rules. 100% is the default. At 0% shadow, Radar evaluates and reports outcomes without enforcing the action. Retries for the same transaction stay in the same bucket. See [[source-stripe-radar-rules#Traffic Allocation|the rules guide]] for card grouping.

The April 2026 [[source-stripe-payment-intents#Descriptor and metadata boundaries|Payment Intents guide]] names Radar for Fraud Teams for custom metadata rules. Its November capture calls the product Radar Plus in equivalent guidance. The dated labels leave plan equivalence, eligibility, and any rename date unresolved.

**3DS attributes**. `is_3d_secure` is generally recommended for Block and `is_3d_secure_authenticated` requires full authentication. `has_liability_shift` reflects Stripe's expected liability shift. The risk-based Block example excludes off-session payments, Apple Pay, and Google Pay when it has a cryptogram. See [[source-stripe-radar-rules#Key 3DS Attributes|the dated rules examples]].

**Radar Assistant** drafts transaction rules from natural language. Using it constitutes agreement that Stripe can log and use chat entries to train and improve it. Users can write rules manually. The guide says EU businesses might be affected by the Geo-blocking Regulation and its limits on blocking payments from customers based in EU member states. See [[source-stripe-radar-rules]].

**Dispute resolution rules** automatically refund incoming disputes that match any configured `Resolve dispute if {condition}` rule. The May 2026 guide names Stripe Radar or Radar for Fraud Teams with dispute-prevention signup. The November guide requires plan support for dispute prevention, and the separate November prevention preview directs merchants to sign up in Dispute settings. See [[source-stripe-radar-rules-disputes]] for the dated eligibility wording, disputed-amount units, Connect account precedence and conflicting USD 10 example.

**Rule reference details.** Comparisons with missing attributes return false, including under `NOT`. Absent Boolean attributes evaluate to false. Use `is_missing()` to check explicitly. Velocity uses buckets, with an hourly upper bound of 3,900 seconds in five-minute buckets. `amount_in_xyz` auto-converts currency. Metadata is case-sensitive when used as a string and can use customer, destination or account scopes. Radar evaluates rules using post-authorization attributes such as AVS/CVC after rules without those attributes. A customer can see a temporary authorization even if Radar ultimately blocks the charge. See [[source-stripe-radar-rules-reference]].

## Block and allow lists

Radar rules can reference reusable lists for allow, block or review. Default lists cover Cards, ACH and SEPA. Merchants can change their items while Stripe keeps the default lists fixed. May named Radar for Fraud Teams for custom lists. The November plan matrix lists default lists on Standard, Plus and Pro and custom lists on Plus and Pro.

**Custom list types**. Both lists guides describe ten entries. Each list can hold up to 50,000 items. Default fingerprint allowlist entries last at most 30 days. Custom payment-method fingerprint lists can have longer or indefinite expiration when used in custom rules. See [[source-stripe-radar-lists]] for the dated API enum and expiration scope.

**Fraud report auto-populates block lists**: card fingerprint(s) + email from `receipt_email`/Customer.email/description fields. See [[source-stripe-radar-lists]].

## Risk Insights

The May and November 2026 guides describe payment-level risk signals, **Show all insights**, and up to six months of data and interface access. The May guide names Fraud Teams and documents fraud factor multipliers, Top Fraud Factors, and a sandbox restriction in its fraud-factor section. November omits those details. See [[source-stripe-radar-risk-insights]] for the dated scope, customer and geography signals, and the comparison method.

The dedicated guides describe Related Payments by customer ID, IP address, or card number. The separate [[raw/stripe-radar-transaction-reviews-2026-11-07|November Transaction Reviews capture]] describes email address, IP address, or card number. The difference between the documented identifiers remains unresolved. The [[source-stripe-radar-reviews|May Transaction Reviews summary]] provides the earlier review workflow.

## Review Queue (Fraud Teams)

Manual review queue for elevated-risk payments. Most PMs supported except ACH/SEPA direct debit. Two views: list (quick scan) + detailed (risk insights + related payments by email/IP/card; `J`/`K` nav).

**Smart Refunds**: post-completion fraud recommendations — Very high (72% dispute chance) to Very low (15%).

**Auth-and-capture flow**. Review approval and payment capture are separate. Cancel releases the uncaptured authorization without creating a Refund. The November 7, 2026 Workflows template runs after review closure and separately captures only when the review was approved and the payment still awaits capture. The Dashboard and API routes remain available in both dated guides. See [[source-stripe-radar-reviews-auth-capture]].

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

**Connected account rules.** A platform with a supporting Radar plan can raise a connected account for review or raise a review and pause payouts while under review. The May 2026 reference names Radar for Platforms. November also documents separate private-preview Treasury Block and Review actions for inbound transfers and received credits. See [[source-stripe-radar-rules-reference]].

**Risk tab**: agent-generated indicators (suspicious network, location mismatch), risk metrics (disputes/refunds/declines time-series), risk history with notes.

**Actions**: reject (7 reason codes: fraud_card_casher, fraud_no_intent_to_fulfill, credit, etc. — hard to reverse), set reserves, pause payments/payouts, request identity verification (gov ID + selfie), dismiss review.

**Platform payment controls for direct charges.** The November 2026 risk-settings guide documents connected-account-only, platform-only, and shared management where the connected account is merchant of record and is controlled solely by the platform. Platform-only overrides connected-account rules. Shared management evaluates one rule set starting with platform rules, while action ordering lets an allow rule from either side override the other side’s block. For specified Lite or platform-only situations the platform can grant view-only access to outcomes. See [[source-stripe-radar-risk-settings]]. The separate [[source-stripe-radar-for-platforms]] guide describes permissions for risk reviews.

The [[source-stripe-radar-for-platforms|2026-05-10 Radar for Platforms guide]] says platform rules run first and have priority when both parties' rules match, yet gives an example where a connected-account rule can still block or review after a platform allow. The 2026-11-07 risk-settings guide describes a single rule set and explicitly lets an allow from either party override the other's block, with platform rules evaluated first. The guides leave live shared-rule precedence unresolved.

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

## Sandbox Tests and Rule Backtesting

The May and November guides document sandbox card fixtures for rule-dependent highest risk, always-blocked highest risk and elevated risk. The elevated fixture specifies the risk level. November adds test cards for the Payment Evaluation API’s `fraudulent_payment` signal and direct-debit test inputs that simulate Radar blocks for SEPA and ACH. See [[source-stripe-radar-testing]] for fixtures and [[source-stripe-radar-multiprocessor]] for Payment Evaluation API access and test-key scope.

Rule testing searches historical live-mode payments and summarizes matching counts and volume. Allow Overrides represent previously Radar-blocked payments that would be allowed under the proposed rule. The separately captured November [[source-stripe-radar-rules|rules guide]] documents a six-month simulation in its Review rules section.

## Risk Settings and Controls

The 2026-11-07 risk-settings guide describes three presets and a plan-qualified custom Fraudulent dispute threshold with backtesting. A threshold that matches no preset displays Manual mode. First enabling a risk setting disables the default classic high-risk block rule permanently. Existing custom rules continue to apply. The 2026-05-10 guide dates the transition for existing Radar for Fraud Teams users to March 1, 2026.

November adds Fraudulent card payments on Standard and above and card-only dynamic thresholds that temporarily tighten blocking and revert when detected fraud pressure ends. The separate November plan matrix lists dynamic thresholds on Pro and risk preferences, transaction scores, custom rules and Adaptive 3DS on Plus and Pro. Early fraud warning extends from the May Maximize protection-only statement to November’s Balanced and Maximize protection. Non-card control scope follows the dated supported-method guide. See [[source-stripe-radar-risk-settings]].

The [[raw/stripe-radar-risk-settings-2026-11-07|November 7, 2026 Risk Settings capture]] says the Dashboard overall risk level takes the maximum of the fraudulent dispute, early fraud warning and classic risk scores that contributed to the payment decision. The Dashboard displays Normal, Elevated or Highest. The `:risk_level:` rules attribute reflects classic risk alone. Classic `:risk_score:` remains usable in eligible custom rules after the default block rule is disabled. November also introduces the separate card-only fraudulent payment score. The November Supported Attributes guide lists the card-only 0–99 `:bot_score:` rule attribute with Radar Pro. See **Bot Abuse Prevention** below for the dated integration scope.

## Risk Levels and Scoring

The May 2026 [[source-stripe-radar-risk-evaluation|risk evaluations guide]] describes a 0–99 classic score with Radar for Fraud Teams and default thresholds of 65 or above for elevated and 75 or above for high. November Risk Settings also describes the classic model as 0–99. Both dated [[source-stripe-radar-rules-supported-attributes|Supported Attributes captures]] list a 0–100 classic rule attribute, with default thresholds of at least 65 for elevated and at least 75 for highest that can be adjusted. Whether the model emits 100 remains unresolved. See [[source-stripe-radar-risk-settings]] for the November plan scope, Dashboard overall risk level and retirement of the default classic high-risk block rule.

| `Charge.outcome.risk_level` in the May 2026 examples | May guide action or illustrated outcome | `Charge.outcome.type` |
| --- | --- | --- |
| `highest` | Blocked by default in the May 10, 2026 Risk evaluations example. The legacy rule applies while enabled. See [[source-stripe-radar-risk-settings]] for accounts using risk settings. | `blocked` when blocked |
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

The [[source-stripe-radar-bot-abuse|May 10, 2026 Bot Abuse guide]] describes a 0–99 score for Stripe Checkout, with Dashboard payment Risk scores, custom rules and Sigma access via `radar_abuse_prevention_attributes.bot_score`. The [[raw/stripe-radar-bot-abuse-2026-11-07|November 7, 2026 Bot Abuse capture]] documents the 0–99 Radar Pro bot score and the bot risk control for Stripe Checkout, Custom Checkout, Radar Sessions and Web Elements. November [[source-stripe-radar-rules-supported-attributes|Supported Attributes]] scopes the `:bot_score:` rule predicate to cards. A high score indicates likely bot activity and does not establish fraud or malice. Stripe advises using the score for anti-scripting or anti-bot policies rather than as a standalone fraud signal. The November guide describes viewing the score in the Dashboard, writing custom rules and using the bot risk control.

## Pay-As-You-Go Abuse Evaluation

For post-paid and usage-based billing, the merchant server estimates non-payment abuse risk outside checkout. The May 2026 guide uses Payment Evaluation. The November guide uses Billing Evaluation in preview and describes evaluation as usage accrues and before invoice finalization. Both use `signals.non_payment_abuse.risk_level` and describe a fail-open request. See [[source-stripe-radar-payg-abuse]] for the dated contracts, and [[source-stripe-radar-free-trial-abuse]] for the card-save stage before there is accrued usage.

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

A Radar Session supplies a snapshot of IP, browser and device details for self-tokenized cards, third-party tokenization or server-side card submission where the signals are missing. Preferred Stripe integrations already send enough information for this path.

- **Client.** Create the session late in checkout or when saving card details using Stripe.js, iOS SDK 21.6.0 or later, or Android SDK 16.9.0 or later. Send the session ID to the server. The client example typically continues checkout if session creation fails.
- **Server.** Attach via `radar_options.session`. For on-session payments, Stripe recommends sending the session on PaymentMethod creation and PaymentIntent creation or confirmation. PaymentIntent Create with a session requires `confirm=true`. The separate Confirm endpoint accepts the session for an existing Intent.
- **Off-session.** Attach the session when creating the PaymentMethod so its associated signals can be used for later charges.

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
- [[source-stripe-radar-payg-abuse]] — May 2026 Payment Evaluation and November 2026 Billing Evaluation preview guidance for post-paid non-payment abuse, with lifecycle, response and sandbox qualifiers.
- [[source-stripe-radar-bot-abuse]] — May 10, 2026 Bot Abuse guide on Checkout scoring, anti-bot policies, Sigma and rules. The [[raw/stripe-radar-bot-abuse-2026-11-07|November 2026 capture]] gives the Radar Pro and integration scope.
- [[source-stripe-radar-multiprocessor]] — May and November 2026 Payment Evaluation guides for external and Stripe processing, dated access and input scope, risk responses and evaluation reuse.
- [[source-stripe-radar-issuing]] — Radar for Issuing: IssuingAuthorizationEvaluation API, pre-authorization fraud scoring, physical + tokenized cards
- [[source-stripe-radar-risk-settings]] — May and November 2026 Risk Settings guides to plan-qualified controls, separate classic and Dashboard risk signals, and direct-charge settings.
- [[source-stripe-radar-supported-payment-methods]] — May method-level coverage and preview opt-in, November default and plan-dependent settings, and the dated Bacs rule example and supported-value discrepancy.
- [[source-stripe-radar-reviews]] — Review queue: Smart Refunds, actions, assignments, webhooks, best practices
- [[source-stripe-radar-risk-insights]] — May and November 2026 payment-level insights, six-month interface access, dated fraud-factor scope and Related Payments identifier wording.
- [[source-stripe-radar-reviews-auth-capture]] — May and November 2026 review of uncaptured payments, Dashboard and API capture, and the November Workflows template
- [[source-stripe-radar-lists]] — May and November 2026 guides with default lists, ten custom entries in the guide, separate API enum, item expiry and card fraud-feedback effects.
- [[source-stripe-radar-rules]] — Rules: 4 actions, built-in rules, syntax, 3DS attributes, Radar Assistant, EU geo-blocking note
- [[source-stripe-radar-rules-reference]] — May and November 2026 technical references for payment, Connect account and private-preview Treasury actions, operators, missingness, metadata and velocity.
- [[source-stripe-radar-rules-supported-attributes]] — May and November 2026 reference for rule attributes, including classic and recommended scores, payment-method and wallet predicates, and Connect account and Treasury rule scopes.
- [[source-stripe-radar-testing]] — May and November 2026 sandbox and historical-live rule testing guides, including the November Payment Evaluation, SEPA and ACH cases.
- [[source-stripe-radar-rules-disputes]] — Dispute resolution rules with dated plan and enrollment guidance, automatic refunds on a match, dispute-specific attributes and the USD 10 example conflict
- [[source-stripe-radar-analytics]] — May 2026 Radar Analytics center and legacy reporting, view-specific metrics, cohort benchmarks and Sigma access. November links the two views.
- [[source-stripe-radar-fraud-alerts]] — Fraud alerts: auto-detected attacks, email+bell notification, investigation page, Fraud Teams extra actions
- [[source-stripe-radar-fraud-insights]] covers the May and November 2026 Dashboard workflows, dated plan terms, initial filters and the November alert-triggered analysis.
- [[source-stripe-radar-for-platforms]] — Radar for Platforms: connected account risk scores, investigation tools, reject (7 codes), reserves, API signals
- [[source-stripe-radar-account-risk-signals]] — May and November 2026 Account Signals API overviews, four November signal routes, 90-day lookup and list scope, and separate guides to plan, event and retrieval behavior.
