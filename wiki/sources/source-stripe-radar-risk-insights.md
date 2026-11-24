---
title: "Stripe — Radar Risk Insights"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/radar/reviews/risk-insights"
raw_files:
  - "stripe-radar-reviews-risk-insights-2026-11-07.md"
  - "stripe-radar-risk-insights-2026.md"
tags: [stripe, radar, risk-insights, fraud-factors, related-payments, fraud-teams]
---

## Summary

The May and November 2026 [[stripe]] guides describe how Radar evaluates hundreds of network and payment risk factors to assign a risk score and level and decide when to block a payment or mark it for review. Merchants can inspect those signals through **Show all insights** on a payment. Both guides state that Stripe retains Risk Insights data for up to six months and that the interface is unavailable for older transactions.

## Customer Signals

Risk Insights can show cardholder name and email correspondence, the Stripe network authorization rate associated with that email, and billing, shipping and IP locations. A low authorization rate might indicate suspicious behavior. Integration-provided details such as cardholder email, IP address and shipping address help Radar compute the data used in its assessment. See the [[source-stripe-radar-optimize-risk-factors|integration checklist]] for the data inputs.

## Fraud Factor Detail in the 2026-05-10 Guide

The May guide describes Risk Insights as available with Radar for Fraud Teams. Its section on fraud factor numbers and **Top Fraud Factors** describes data for charges made within the previous six months, with sandbox payments outside that feature’s scope.

- **Fraud factor numbers** compare the likelihood of fraud for charges with similar values for a factor against the Stripe average. A 3.5× factor means charges with similar values for that factor are 3.5 times as likely to be fraudulent as the Stripe average. May expects some factors above 1 for higher-risk payments and some below 1 for lower-risk payments. Hover details show the distribution of possible values, which can change over time.
- **Top Fraud Factors** highlights values commonly associated with fraud. Radar can identify a fraud pattern from multiple factors even if none looks suspicious individually.

November retains **Show all insights** and the six-month interface restriction. It omits the May plan label, fraud factor number and Top Fraud Factors explanations, and sandbox wording. Eligibility for those details under the newer plans and in sandboxes remains unresolved in these captures.

## Related Payments

Both dedicated Risk Insights captures describe other payments to the merchant’s own business that share the viewed payment’s customer ID, IP address, or card number. Many cards using one IP or multiple customers sharing a card can help investigate patterns such as card testing or trial abuse.

> **2026-11-07 documentation difference.** The dedicated Risk Insights guide lists customer ID, IP address, or card number. The same-day [[raw/stripe-radar-transaction-reviews-2026-11-07|Transaction Reviews guide]] (line 52) lists email address, IP address, or card number for its Related Payments link. The captures leave the reason for the identifier difference and the actual lookup behavior unresolved.

## Related Pages

- [[stripe-radar]] — Radar concept and Risk Insights
- [[source-stripe-radar-reviews]] — transaction review and payment detail views
- [[source-stripe-radar-optimize-risk-factors]] — integration checklist

## Raw Sources

- [[raw/stripe-radar-reviews-risk-insights-2026-11-07|Stripe Radar Risk Insights guide captured 2026-11-07]]
- [[raw/stripe-radar-risk-insights-2026|Stripe Radar Risk Insights guide captured 2026-05-10]] — includes the fraud-factor figures
