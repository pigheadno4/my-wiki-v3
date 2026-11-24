---
title: "Stripe — Account Risk Signals"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-22
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

## Signal types and retrieval

| Signal | Detects | Method |
| --- | --- | --- |
| Fraudulent merchant | Misrepresentation, unauthorized transactions, first-party fraud | ML model (continuous) |
| Merchant delinquency risk | Financial distress → unfulfilled orders, disputes, negative balances | ML model (continuous) |
| Fraudulent website | Deceptive/policy-violating websites, fake storefronts | On-demand analysis |

Signal changes trigger webhook events to your endpoint.

## Notification and platform response

Raise review, pause payouts, pause payments, reject account, set reserves, request identity verification — all via Radar for Platforms.

## Related Pages

- [[stripe]]
- [[stripe-radar]] — concept page
- [[source-stripe-radar-for-platforms]] — Radar for Platforms actions and investigation
- [November Account Fraud Prevention actions](../../raw/stripe-radar-account-fraud-prevention-2026-11-07.md#L113) — the action route linked from the November merchant signal guide
- [[stripe]] — Stripe company page

The three detailed summaries below describe their May 10, 2026 captures. The separately scoped November changes are above.

## Fraudulent merchant signal

### November 7, 2026 guide

Stripe automatically evaluates the signal for new or existing connected accounts. Radar Standard and higher include the signal. Plus and Pro can receive the 0–100 `probability` score and `additional_details.indicators`. Both details are absent if the risk level is `unknown`.

| Risk level | November meaning |
| --- | --- |
| `highest` | Approximately 90% probability that the account is fraudulent |
| `elevated` | Approximately 50% probability that the account is fraudulent |
| `normal` | Low probability of fraud |
| `unknown` | Stripe could not determine a risk level |

These are fraudulent-merchant signal probabilities. General Radar account scoring separately estimates platform financial loss from fraud or insolvency. Use the signal as evidence for review and decide on any account action separately.

November’s indicators each carry an `impact` (`decrease`, `neutral`, `slight_increase` or `strong_increase`) and an `explanation`. The dated table uses `geolocation`, includes `other` for a type the API version does not support, and omits May’s `web_presence` row. See the November **Indicators** table for the exact vocabulary.

#### Event and retrieval

Stripe sends `v2.signals.account_signal.fraudulent_merchant_ready` when it creates a signal. The November event is thin with `data: {}`. Use `related_object.id` to fetch that signal. The dated fetch and list samples use `Stripe-Version: 2026-10-28.preview` with `/v2/signals/account_signals`. Fetch appends the signal ID. List filters with `account_details[account]` and the requested type, with `type[0]=fraudulent_merchant` in the example. It returns only the latest signal per requested type. Signals can be retrieved for up to 90 days after creation. List results omit older signals.

Both response examples nest `risk_level`, `probability` and `additional_details.indicators` under `fraudulent_merchant`. The example serializes the score as the JSON string `"53.75"`. The guide describes the 0–100 score range. The example gives the wire representation for that sample.

#### Sandbox

To simulate a signal, the November guide adds a suffix to the connected account’s `business_profile.name`. Stripe creates a signal and sends the same readiness webhook. The supplied fixtures cover `normal`, `elevated` and `highest`, with one suffix active per account, in a sandbox only. See the dated **Test in a sandbox** section for the exact fixture values.

### May 10, 2026 guide

May listed `highest` (approximately 90%), `elevated` (approximately 50%), `normal`, `low` and `not_assessed`. It said each signal returned `risk_level` and a 0–100 `probability`, and described the same readiness event as carrying `risk_level`, `probability` and `indicators`. The May indicator table listed `bank_account`, `business_information_and_account_activity`, `disputes`, `failures`, `geo_location`, `other_related_accounts`, `other_transaction_activity`, `owner_email` and `web_presence`. The paired captures leave any mapping between May’s omitted levels and November’s `unknown` unresolved.

## Merchant Delinquency Risk Signal Detail

**Risk levels**: `highest`, `elevated`, `normal`, `low`, `not_assessed` (same 5 levels as fraudulent merchant).

### November 7, 2026 delinquency guide

- Use the linked [Account Signals API](https://docs.stripe.com/api/v2/signals/account-signals.md?api-version=2026-07-29.preview) reference to retrieve the latest assessment. Listen for `v2.signals.account_signal.merchant_delinquency_ready` when a delinquency signal has been evaluated. This guide specifies notification timing and separate latest-result retrieval. It leaves the event body, retrieval parameters and retention period unspecified.
- Risk levels listed are `highest`, `elevated`, `normal` and `low`. On Radar Plus and Pro the signal also includes a `probability` score from 0 to 100. The separate fraudulent-merchant result list includes `unknown` and omits `low`, and its guide describes a thin-event contract specific to that signal.
- The November delinquency table lists 15 indicators: `account_balance`, `aov`, `charge_concentration`, `dispute_window`, `disputes`, `exposure`, `firmographic`, `lifetime_metrics`, `payment_processing`, `payment_volume`, `payouts`, `refunds`, `related_accounts`, `tenure` and `transfers`. The table retains `related_accounts` and omits May's `duplicates` row. November also omits `not_assessed` from the displayed risk levels. Field deprecation or equivalence to the separate merchant signal is unverified.

The readiness notification reports when evaluation has occurred. The platform can separately choose an appropriate account action using the [Account Fraud Prevention action guide](https://docs.stripe.com/radar/account-fraud-prevention.md#take-action), such as raising a review, pausing payments or setting reserves. See November raw lines 7–25, 27–58 and 60–66, and the separate action guide at lines 113–126.

### May 10, 2026 delinquency guide

May describes broader financial distress that might lead to unrecoverable negative balances from disputes, refunds or failed payouts. The guide links its `2026-03-25.preview` core event reference for latest-result retrieval, and describes `v1.account_signals[delinquency].created` when evaluated. It lists `highest`, `elevated`, `normal`, `low` and `not_assessed`. May includes 16 indicators, adding `duplicates` to the 15 listed above alongside the separate `related_accounts` row. The previous action route led to Radar for Platforms and Account Risk Signals. See May raw lines 6–24 and 26–55.

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

- [[stripe-radar-account-risk-signals-2026]] — verbatim Account Signals API overview
- [[stripe-radar-fraudulent-merchant-signal-2026]] — verbatim fraudulent merchant signal detail (risk levels, 9 indicators, webhook)
- [[stripe-radar-merchant-delinquency-signal-2026]] — verbatim merchant delinquency risk signal detail (16 indicators, webhook)
- [[stripe-radar-fraudulent-website-signal-2026]] — verbatim fraudulent website signal detail (on-demand, LLM details, unknown risk level)
