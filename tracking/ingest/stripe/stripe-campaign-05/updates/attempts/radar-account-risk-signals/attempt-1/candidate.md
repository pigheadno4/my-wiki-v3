---
title: "Stripe — Account Risk Signals"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-22
original_format: webpage
raw_files:
  - "stripe-radar-account-risk-signals-2026-11-07.md"
  - "stripe-radar-account-risk-signals-2026.md"
  - "stripe-radar-fraudulent-merchant-signal-2026.md"
  - "stripe-radar-merchant-delinquency-signal-2026.md"
  - "stripe-radar-fraudulent-website-signal-2026.md"
tags: [stripe, radar, connect, platforms, account-signals, fraud, delinquency, website]
---

## Summary

The May 10 and November 7, 2026 captures of https://docs.stripe.com/radar/account-risk-signals describe programmatic risk signals for Connect platforms. Stripe evaluates connected-account activity and sends a webhook when a risk signal changes. The May guide lists three signal types. November adds payment delinquency exposure and illustrates the platform retrieving the signal and deciding how to respond.

## Signal types and retrieval

| Signal | Documented scope |
| --- | --- |
| Fraudulent merchant | Risk indicators such as misrepresentation, unauthorized transactions or first-party fraud. Stripe evaluates account activity. |
| Merchant delinquency risk | Financial distress associated with potential unfulfilled orders, disputes, refunds or negative balances. |
| Fraudulent website | On-demand evaluation for deceptive or policy-violating websites, including misleading claims or fake storefronts. |
| Payment delinquency exposure | Added to the November overview. Estimates dollars at risk from potential disputes and refunds if a connected account becomes delinquent. |

November says account signals and account evaluations can be retrieved for up to 90 days after creation. List requests omit account signals created more than 90 days ago. The overview states a retrieval and list boundary. The separate delinquency-risk guide's negative balance lasting more than 90 days describes the risk being assessed. [[raw/stripe-radar-merchant-delinquency-risk-2026-11-07|November delinquency risk detail, lines 8–13]]

## Notification and platform response

May links to the [Core event-types route for `2026-03-25.preview`](https://docs.stripe.com/api/v2/core/events/event-types.md?api-version=2026-03-25.preview). November links to the [Account Signals API with `api-version=preview`](https://docs.stripe.com/api/v2/signals/account-signals.md?api-version=preview). Its diagram shows connected-account payments or disputes feeding Stripe's models, a signal-ready webhook to the platform backend, retrieval by `GET /v2/signals/account_signals/{id}`, and the platform receiving signal level and indicators before deciding whether to review, pause or reject. The notification signals readiness. The separate child guides give the event and payload contract for each signal.

May's Radar for Platforms action table lists raising a review, pausing payouts, pausing payments, rejecting a confirmed fraudulent account, setting reserves and requesting identity verification. November replaces the table with a route to account fraud prevention. That guide retains the six options, qualifies request identity verification on use of Stripe Identity, directs platforms to Stripe Support to reverse rejection, and names Connect Risk Analyst, Administrator or Super Administrator for risk reviews. These are platform decisions. A signal is an input to that decision and leaves confirmed fraud and action execution unverified. [[source-stripe-radar-for-platforms|Radar for Platforms]] · [[raw/stripe-radar-account-fraud-prevention-2026-11-07|November account fraud prevention, lines 102–126, 140–154 and 162–166]]

## Separately captured November signal details

- **Fraudulent merchant.** The ready event is thin with an empty `data` object. Retrieve the signal using `related_object.id`. The detail guide lists the signal from Radar Standard upward and the returned 0–100 probability only on Plus and Pro. The earlier detailed capture below describes a payload with full details. [[raw/stripe-radar-fraudulent-merchant-2026-11-07|November fraudulent merchant detail, lines 9–24 and 43–51]]
- **Merchant delinquency risk.** The detail names `v2.signals.account_signal.merchant_delinquency_ready`, compared with the earlier v1 event below, and gives an early-access request. [[raw/stripe-radar-merchant-delinquency-risk-2026-11-07|November delinquency risk detail, lines 8–13 and 60–66]]
- **Fraudulent website.** On-demand evaluation uses `POST /v2/signals/account_evaluations`, compared with the earlier Core endpoint below. The individual ready event `v2.signals.account_signal.fraudulent_website_ready` and optional `v2.signals.account_evaluation.complete` for multiple signals are thin. Use `related_object.id` to retrieve the resource. The detail allows sandbox testing on any Radar plan and specifies Plus or Pro with 4,000 monthly requests for live use. [[raw/stripe-radar-fraudulent-website-2026-11-07|November fraudulent website detail, lines 9–26 and 63–73]]
- **Payment delinquency exposure.** The separate guide describes requesting early access and lists `v2.signals.account_signal.payment_delinquency_exposure_ready`. Its conditional monetary estimate is a separate signal from merchant delinquency risk. [[raw/stripe-radar-payment-delinquency-exposure-2026-11-07|November payment delinquency exposure, lines 7–13 and 55–61]]

The overview's diagram and these child guides leave account-specific entitlement and common delivery semantics across signal types unresolved.

## Related Pages

- [[stripe]]
- [[stripe-radar]] — concept page
- [[source-stripe-radar-for-platforms]] — full Radar for Platforms guide (actions, investigation, reject codes)

The three detailed summaries below describe their May 10, 2026 captures. The separately scoped November changes are above.

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

- [[raw/stripe-radar-account-risk-signals-2026-11-07|Account risk signals overview, captured 2026-11-07]] — full 36-line overview with the retrieval boundary and platform decision diagram.
- [[raw/stripe-radar-account-risk-signals-2026|Account risk signals overview, captured 2026-05-10]] — full 40-line overview with dated preview routing and action table
- [[raw/stripe-radar-fraudulent-merchant-signal-2026]] — verbatim fraudulent merchant signal detail (risk levels, 9 indicators, webhook)
- [[raw/stripe-radar-merchant-delinquency-signal-2026]] — verbatim merchant delinquency risk signal detail (16 indicators, webhook)
- [[raw/stripe-radar-fraudulent-website-signal-2026]] — verbatim fraudulent website signal detail (on-demand, LLM details, unknown risk level)
