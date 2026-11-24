---
title: "Stripe — Account Risk Signals"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-22
original_format: webpage
raw_files:
  - "stripe-radar-merchant-delinquency-risk-2026-11-07.md"
  - "stripe-radar-account-risk-signals-2026.md"
  - "stripe-radar-fraudulent-merchant-signal-2026.md"
  - "stripe-radar-merchant-delinquency-signal-2026.md"
  - "stripe-radar-fraudulent-website-signal-2026.md"
tags: [stripe, radar, connect, platforms, account-signals, fraud, delinquency, website]
---

## Summary

[[stripe|Stripe]] Account Signals provides risk intelligence for Connect platforms. A signal's readiness and a platform operator's choice to take action are separate. The November delinquency guide specifies the risk of carrying a negative balance for more than 90 days.

## 3 Signal Types

| Signal | Detects | Method |
| --- | --- | --- |
| Fraudulent merchant | Misrepresentation, unauthorized transactions, first-party fraud | ML model (continuous) |
| Merchant delinquency risk | May describes financial distress. November specifies risk of carrying a negative balance for more than 90 days. | Risk assessment for a connected account |
| Fraudulent website | Deceptive/policy-violating websites, fake storefronts | On-demand analysis |

The May account-risk overview describes continuous evaluation with signal-change notifications. It separately labels the website signal on demand. The November delinquency guide below describes a readiness event after evaluation. Choose any platform action separately.

## Actions

Raise review, pause payouts, pause payments, reject account, set reserves, request identity verification — all via Radar for Platforms.

## Related Pages

- [[stripe-radar]] — concept page
- [[source-stripe-radar-for-platforms]] — full Radar for Platforms guide (actions, investigation, reject codes)

## Fraudulent Merchant Signal Detail

**Risk levels**: `highest` (~90%), `elevated` (~50%), `normal`, `low`, `not_assessed`. Returns `risk_level` + `probability` (0–100).

**9 indicators**: `bank_account`, `business_information_and_account_activity`, `disputes`, `failures`, `geo_location`, `other_related_accounts`, `other_transaction_activity`, `owner_email`, `web_presence`.

**Webhook**: `v2.signals.account_signal.fraudulent_merchant_ready` — payload includes `risk_level`, `probability`, `indicators`.

## Merchant Delinquency Risk Signal Detail

The May 10 and November 7, 2026 captures at [Merchant delinquency risk](https://docs.stripe.com/radar/merchant-delinquency-risk) describe a Connect platform retrieving Stripe's latest delinquency evaluation, with a risk level and indicators for the connected account. The November guide defines the prediction as risk of carrying a negative balance for more than 90 days. It gives disputes, refunds and failed payouts as examples of events that can contribute to unrecoverable balances. The 90 days is a prediction horizon. The guide describes an email request for early access. Individual access and whether an account is currently delinquent remain separate.

### November 7, 2026 delinquency guide

- Use the linked [Account Signals API](https://docs.stripe.com/api/v2/signals/account-signals.md?api-version=2026-07-29.preview) reference to retrieve the latest assessment. Listen for `v2.signals.account_signal.merchant_delinquency_ready` when a delinquency signal has been evaluated. This guide specifies notification timing and separate latest-result retrieval. It leaves the event body, retrieval parameters and retention period unspecified.
- Risk levels listed are `highest`, `elevated`, `normal` and `low`. On Radar Plus and Pro the signal also includes a `probability` score from 0 to 100. The separate fraudulent-merchant result list includes `unknown` and omits `low`, and its guide describes a thin-event contract specific to that signal.
- The November delinquency table lists 15 indicators: `account_balance`, `aov`, `charge_concentration`, `dispute_window`, `disputes`, `exposure`, `firmographic`, `lifetime_metrics`, `payment_processing`, `payment_volume`, `payouts`, `refunds`, `related_accounts`, `tenure` and `transfers`. The table retains `related_accounts` and omits May's `duplicates` row. November also omits `not_assessed` from the displayed risk levels. Field deprecation or equivalence to the separate merchant signal is unverified.

The readiness notification reports when evaluation has occurred. The platform can separately choose an appropriate account action using the [Account Fraud Prevention action guide](https://docs.stripe.com/radar/account-fraud-prevention.md#take-action), such as raising a review, pausing payments or setting reserves. See November raw lines 7–25, 27–58 and 60–66, and the separate action guide at lines 113–126.

### May 10, 2026 delinquency guide

May describes broader financial distress that might lead to unrecoverable negative balances from disputes, refunds or failed payouts. The guide links its `2026-03-25.preview` core event reference for latest-result retrieval, and describes `v1.account_signals[delinquency].created` when evaluated. It lists `highest`, `elevated`, `normal`, `low` and `not_assessed`. May includes 16 indicators, adding `duplicates` to the 15 listed above alongside the separate `related_accounts` row. The previous action route led to Radar for Platforms and Account Risk Signals. See May raw lines 6–24 and 26–55.

## Fraudulent Website Signal Detail

**Key difference from other signals**: on-demand (not continuous) — triggered via `POST /v2/core/account_evaluations`.

**Can evaluate before account exists**: pass `account_data.defaults.profile.business_url` instead of `account` ID.

**Asynchronous** — webhook: `v2.core.account_signals.fraudulent_website_ready`.

**Payload fields**: `risk_level` (`low`/`normal`/`elevated`/`highest`/`unknown`), `details` (LLM-generated plain text description), `evaluation_id`, `signal_id`, `evaluated_at`.

**No indicator table** — LLM generates a `details` text explanation instead. `unknown` returned when URL is invalid or unreachable.

## Raw Sources

- [[raw/stripe-radar-merchant-delinquency-risk-2026-11-07]] — November 7, 2026 full merchant delinquency risk guide
- [[stripe-radar-account-risk-signals-2026]] — verbatim Account Signals API overview
- [[stripe-radar-fraudulent-merchant-signal-2026]] — verbatim fraudulent merchant signal detail (risk levels, 9 indicators, webhook)
- [[raw/stripe-radar-merchant-delinquency-signal-2026]] — May 10, 2026 merchant delinquency risk guide with 16 indicators and the v1 readiness event
- [[stripe-radar-fraudulent-website-signal-2026]] — verbatim fraudulent website signal detail (on-demand, LLM details, unknown risk level)
