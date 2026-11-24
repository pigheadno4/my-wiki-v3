---
title: "Stripe — Account Risk Signals"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-22
original_format: webpage
raw_files:
  - "stripe-radar-fraudulent-website-2026-11-07.md"
  - "stripe-radar-account-risk-signals-2026.md"
  - "stripe-radar-fraudulent-merchant-signal-2026.md"
  - "stripe-radar-merchant-delinquency-signal-2026.md"
  - "stripe-radar-fraudulent-website-signal-2026.md"
tags: [stripe, radar, connect, platforms, account-signals, fraud, delinquency, website]
---

## Summary

[[stripe|Stripe]] Account Signals provides risk intelligence for Connect platforms across fraudulent merchant, merchant delinquency, and fraudulent website signals. Website evaluation is on demand, including for a prospective business.

## 3 Signal Types

| Signal | Detects | Method |
| --- | --- | --- |
| Fraudulent merchant | Misrepresentation, unauthorized transactions, first-party fraud | ML model (continuous) |
| Merchant delinquency risk | Financial distress → unfulfilled orders, disputes, negative balances | ML model (continuous) |
| Fraudulent website | Deceptive/policy-violating websites, fake storefronts | On-demand analysis |

The May account-risk overview describes continuous evaluation with signal-change notifications. It separately labels the website signal on demand. The November website guide below describes website evaluation readiness events for that route.

## Actions

Available Radar actions for existing connected accounts include raising a review, pausing payouts or payments, rejecting the account, setting reserves, and requesting identity verification when eligible. The website evaluation provides a result for the platform to assess.

## Related Pages

- [[stripe-radar]] — concept page
- [[source-stripe-radar-for-platforms]] — full Radar for Platforms guide (actions, investigation, reject codes)

## Fraudulent Merchant Signal Detail

**Risk levels**: `highest` (~90%), `elevated` (~50%), `normal`, `low`, `not_assessed`. Returns `risk_level` + `probability` (0–100).

**9 indicators**: `bank_account`, `business_information_and_account_activity`, `disputes`, `failures`, `geo_location`, `other_related_accounts`, `other_transaction_activity`, `owner_email`, `web_presence`.

**Webhook**: `v2.signals.account_signal.fraudulent_merchant_ready` — payload includes `risk_level`, `probability`, `indicators`.

## Merchant Delinquency Risk Signal Detail

**Risk levels**: `highest`, `elevated`, `normal`, `low`, `not_assessed` (same 5 levels as fraudulent merchant).

**16 indicators**: `account_balance`, `aov`, `charge_concentration`, `dispute_window`, `disputes`, `duplicates`, `exposure`, `firmographic`, `lifetime_metrics`, `payment_processing`, `payment_volume`, `payouts`, `refunds`, `related_accounts`, `tenure`, `transfers`.

**Webhook**: `v1.account_signals[delinquency].created` (note: v1 format, unlike fraudulent merchant's v2 format).

## Fraudulent Website Signal Detail

The May 10 and November 7, 2026 guides at [the fraudulent website signal URL](https://docs.stripe.com/radar/fraudulent-website) describe an on-demand asynchronous evaluation for an existing connected account or a prospective business. An invalid or unreachable website yields `unknown` and an explanation. Risk values are `low`, `normal`, `elevated`, `highest` and `unknown`. The results include an LLM-generated `details` description.

### November 7, 2026 website guide

- **Access.** Sandbox testing is available with any Radar plan. Live use requires Radar Plus or Pro and is limited to 4,000 requests per month. These are website-specific conditions, distinct from the preview API version used in the samples.
- **Request.** The samples use `POST /v2/signals/account_evaluations` and Stripe API version `2026-10-28.preview`. Request `fraudulent_website` in `requested_signals`. Use `account_details.account` for an existing account. For an evaluation before account creation, use `account_details.data.defaults.profile.business_url`. The business URL is the only required business-data field for that entity-less evaluation. Stripe documents optional additional fields for a more informed assessment.
- **Readiness and retrieval.** Listen for `v2.signals.account_signal.fraudulent_website_ready` when the individual website signal is ready. When multiple signals were requested, Stripe sends `v2.signals.account_evaluation.complete` after all requested results are ready. Both events are thin and their `data` is always `{}`. Use `related_object.id` to fetch the corresponding object. Both object types are retrievable for up to 90 days after creation.
- **Result shape.** The fetched `v2.signals.account_signal` example has its own `id` and `created`, an `account_evaluation` reference, and the `fraudulent_website.risk_level` and `fraudulent_website.details` result. The full `v2.signals.account_evaluation` example has its own evaluation ID, requested and pending signals, and `evaluated_signals.fraudulent_website` with the signal reference, `evaluated_at`, risk level, and details.
- **Sandbox.** Reserved test URLs produce deterministic results without a real crawl. Other URLs in sandbox receive the standard `normal` mock response. The guide shows updating an existing account's business URL using Accounts v1 or v2, or supplying it directly for an entity-less sandbox evaluation. Live mode performs a real evaluation.

See November raw lines 9–59 for access and request samples, lines 61–130 for webhook and result retrieval, including aggregate retrieval at lines 95–121, and lines 132–210 for sandbox tests. The guide links to [[raw/stripe-radar-account-fraud-prevention-2026-11-07|Account Fraud Prevention]] for separate platform actions on existing connected accounts. The evaluation itself returns risk intelligence, including for a prospective business. Platform operators choose any applicable action on an existing connected account through the documented tools.

### May 10, 2026 website guide

The earlier example used `POST /v2/core/account_evaluations` with API version `2026-03-25.preview`, `signals`, and either top-level `account` or `account_data.defaults.profile.business_url`. It described the `v2.core.account_signals.fraudulent_website_ready` event as carrying `risk_level`, `details`, `evaluation_id`, `signal_id` and `evaluated_at`. See May raw lines 10–64. The captures describe these contracts on their respective dates. Interoperability between the samples is unverified.

## Raw Sources

- [[raw/stripe-radar-fraudulent-website-2026-11-07]] — November 7, 2026 full fraudulent website signal guide with request, thin events, retrieval and sandbox tests
- [[stripe-radar-account-risk-signals-2026]] — verbatim Account Signals API overview
- [[stripe-radar-fraudulent-merchant-signal-2026]] — verbatim fraudulent merchant signal detail (risk levels, 9 indicators, webhook)
- [[stripe-radar-merchant-delinquency-signal-2026]] — verbatim merchant delinquency risk signal detail (16 indicators, webhook)
- [[raw/stripe-radar-fraudulent-website-signal-2026]] — May 10, 2026 fraudulent website signal guide and earlier preview contract
