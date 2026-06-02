---
title: "Stripe — Account Risk Signals"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-account-risk-signals-2026.md"
  - "stripe-radar-fraudulent-merchant-signal-2026.md"
  - "stripe-radar-merchant-delinquency-signal-2026.md"
  - "stripe-radar-fraudulent-website-signal-2026.md"
tags: [stripe, radar, connect, platforms, account-signals, fraud, delinquency, website]
---

## Summary

Overview of the Account Signals API for Connect platforms: 3 webhook-driven signal types for connected account risk, triggering actions via Radar for Platforms.

## 3 Signal Types

| Signal | Detects | Method |
| --- | --- | --- |
| Fraudulent merchant | Misrepresentation, unauthorized transactions, first-party fraud | ML model (continuous) |
| Merchant delinquency risk | Financial distress → unfulfilled orders, disputes, negative balances | ML model (continuous) |
| Fraudulent website | Deceptive/policy-violating websites, fake storefronts | On-demand analysis |

Signal changes trigger webhook events to your endpoint.

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

**Risk levels**: `highest`, `elevated`, `normal`, `low`, `not_assessed` (same 5 levels as fraudulent merchant).

**16 indicators**: `account_balance`, `aov`, `charge_concentration`, `dispute_window`, `disputes`, `duplicates`, `exposure`, `firmographic`, `lifetime_metrics`, `payment_processing`, `payment_volume`, `payouts`, `refunds`, `related_accounts`, `tenure`, `transfers`.

**Webhook**: `v1.account_signals[delinquency].created` (note: v1 format, unlike fraudulent merchant's v2 format).

## Fraudulent Website Signal Detail

**Key difference from other signals**: on-demand (not continuous) — triggered via `POST /v2/core/account_evaluations`.

**Can evaluate before account exists**: pass `account_data.defaults.profile.business_url` instead of `account` ID.

**Asynchronous** — webhook: `v2.core.account_signals.fraudulent_website_ready`.

**Payload fields**: `risk_level` (`low`/`normal`/`elevated`/`highest`/`unknown`), `details` (LLM-generated plain text description), `evaluation_id`, `signal_id`, `evaluated_at`.

**No indicator table** — LLM generates a `details` text explanation instead. `unknown` returned when URL is invalid or unreachable.

## Raw Sources

- [[stripe-radar-account-risk-signals-2026]] — verbatim Account Signals API overview
- [[stripe-radar-fraudulent-merchant-signal-2026]] — verbatim fraudulent merchant signal detail (risk levels, 9 indicators, webhook)
- [[stripe-radar-merchant-delinquency-signal-2026]] — verbatim merchant delinquency risk signal detail (16 indicators, webhook)
- [[stripe-radar-fraudulent-website-signal-2026]] — verbatim fraudulent website signal detail (on-demand, LLM details, unknown risk level)
