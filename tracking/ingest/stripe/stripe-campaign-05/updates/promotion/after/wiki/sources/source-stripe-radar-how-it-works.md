---
title: "Stripe — How Radar Works"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/radar/how-radar-works"
raw_files:
  - "stripe-radar-how-radar-works-2026-11-07.md"
  - "stripe-radar-how-it-works-2026.md"
tags: [stripe, radar, fraud, fraud-detection, rules-engine, risk, block-list, allow-list, 3ds]
---

## Overview

The November 7, 2026 guide describes real-time Radar protection for transaction fraud, account risk and customer abuse. Radar screens supported payment attempts, including successful, declined, blocked and review-flagged attempts. Both overviews exclude non-card SetupIntents. The separate May Risk evaluations guide describes a settings option for SetupIntents when using card payments. See May lines 8–20 and November lines 9–13 and [[source-stripe-radar-risk-evaluation]].

The May 10, 2026 capture described base Stripe Radar, Radar for Fraud Teams for custom rules and deeper insights, and Radar for Platforms for transaction and account risk. It listed cards, card-backed wallets, ACH and SEPA Direct Debit, with additional payment method controls in preview. Its general feature list covered AI fraud detection, rules, risk insights, 3D Secure, block and allow lists, and real-time monitoring. November links supported methods and compares four named plans. The captures do not map the May labels to November plans or give an effective transition date. See May lines 8–36 and November lines 11–22.

## November plan matrices

| Scope | Included at the named plan and above |
| --- | --- |
| Transaction prevention, Lite | Essential card fraud prevention, card testing prevention and fraud alerts |
| Transaction prevention, Standard | Expanded fraud prevention, all-supported-method protection, fraud analytics, default rules and lists, and risk levels |
| Transaction prevention, Plus | Risk scores, custom rules and lists, rule backtesting, transaction manual reviews, risk preferences, Adaptive 3DS, Smart Refunds, Radar Assistant, advanced fraud analytics and agentic insights |
| Transaction prevention, Pro | Dynamic risk thresholds |
| Account prevention, Standard | AI fraud prevention, analytics, default rules and lists, account manual reviews, recommendations, fraudulent merchant signal, history and risk levels |
| Account prevention, Plus | Risk scores, custom rules and lists, backtesting, dynamic reserves, fraudulent website signal, Radar Assistant and agentic insights |
| Customer abuse, Pro | Free-trial, bot, multi-account, account-sharing and pay-as-you-go controls |

Stripe reports that businesses on Standard block 42% more fraud on average than those on Lite. This is the publisher's comparison for that metric. The supported-methods companion describes broad default protection for supported methods, excluding deprecated ones. It assigns default high-risk blocking controls to Standard and above, notes Stripe can still block payments on Lite, and conditions customization on the plan. The overview's transaction matrix separately marks the all-payment-methods feature unsupported on Lite. See November lines 15–76 and [[source-stripe-radar-supported-payment-methods]].

## Fees and screening

The November guide states that Standard, Plus and Pro charge when Radar screens an authorization or charge. Examples include one-off and recurring payments, invoices and subscription lifecycle events. Unscreened transactions incur no per-screen fee described here.

For Stripe Billing subscriptions, Radar screens and charges for the first payment and the first payment after any payment method change. The merchant can configure how many successful renewal cycles Radar screens before skipping later renewals. A skipped renewal incurs no Radar transaction screening fee. If the payment method changes, screening resumes on the next payment and the configured skip behavior resumes from that point. For a free trial, the first screen occurs when the customer is charged. The May overview described a Billing first-transaction-only fee exception. The separate May Risk evaluations guide says the fraud model scores only the initial Stripe Billing subscription payment and Radar evaluates rules for all payments. That scoring-versus-rules description is separate from the newer screening and fee schedule. See November lines 78–82 and May lines 8–10 and [[source-stripe-radar-risk-evaluation]].

For Connect, Stripe charges Radar account fees to the platform and applies the collecting account's rate to transaction fees. A platform collecting and transferring a payment can pass the fee to the connected account by reducing the transfer. The May overview described an additional connected-account fee for Radar for Platforms. Neither capture provides exact rates, default or maximum renewal settings, or individual plan entitlement. See November lines 83–84 and May lines 8–10.

## Related Pages

- [[stripe-radar]] — Risk evaluation, rules and plan-specific context
- [[stripe-declines]] — Radar blocking and Charge outcome
- [[stripe-3d-secure]] — Authentication and Radar rules
- [[source-stripe-radar-supported-payment-methods]] — Payment method coverage and plan-based default controls
- [[source-stripe-radar-risk-evaluation]] — Model scoring, rules and object support
- [[source-stripe-radar-for-platforms]] — Connect platform controls
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-radar-how-radar-works-2026-11-07|November 7, 2026 How Radar works]] — Full guide with plan matrices and fee documentation
- [[raw/stripe-radar-how-it-works-2026|May 10, 2026 How Radar works]] — Earlier full overview preserving May labels and fees
