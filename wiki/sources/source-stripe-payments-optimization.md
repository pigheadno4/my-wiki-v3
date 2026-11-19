---
title: "Stripe Docs — Payments optimization"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/analytics/optimization
original_format: webpage
raw_files:
  - "stripe-payments-analytics-optimization-2026-11-07.md"
  - "stripe-payments-optimization-2025.md"
tags: [stripe, authorization-boost, adaptive-acceptance, card-account-updater, network-tokens, ic-plus, payment-optimization, cnp]
---

## Summary

The Optimization Dashboard reports **estimated** effects of Authorization Boost features on card-not-present (CNP) payment attempts: recovered payment volume and count, success-rate increase, and network cost savings. The May 8 and November 7, 2026 captures describe the same behavior. Stripe says these estimates do not guarantee outcomes. This page does not establish that a feature is enabled for a particular merchant, that any individual payment would otherwise have failed, or that displayed savings were realized in the account's fees.

## Three Authorization Boost features

| Feature | Documented recovery mechanism | Conditional network cost mechanism |
| --- | --- | --- |
| Adaptive Acceptance | AI reformats requests before authorization or after decline and selectively reattempts; in the US an eligible debit transaction might be retried on a PINless network after a Visa/Mastercard decline. | For IC+ businesses, excessive-retry prevention, decline prevention, and Data Only 3DS may avoid network or scheme fees. |
| Card account updater | Major card-network updater services retrieve changed saved-card PAN or expiry; a later successful payment can use updated information. | None listed. |
| Network tokens | Network-issued credentials substitute for card numbers and can stay current after underlying card data changes. | For eligible interchange pricing and markets, tokens can qualify for lower interchange or avoid outdated-credential scheme penalties. |

The guide explicitly describes AI for Adaptive Acceptance. It describes separate network updater and token mechanisms for the other two; calling all three “AI-driven” overstates the evidence.

## Attribution and estimate boundaries

For each optimized payment, Stripe estimates the likelihood that the optimization caused an approval that otherwise would not have happened. If multiple features touch one payment, it attributes the benefit to the feature most likely responsible. The guide's example is 100 payments × 50 USD × 20% estimated causal likelihood = 1,000 USD estimated recovered volume; it is an illustration, not observed incremental revenue.

Cost savings for IC+ businesses are modeled from interchange and scheme-fee rules and counterfactual network costs. Stripe explicitly says it does **not** reconcile those estimates directly with the fees applied to the account. The Dashboard shows cost-saving estimates only for domestic payments in the US and Canada, though savings may occur elsewhere. It omits possible network-token-use fees such as Visa's VDCU fee, which can reduce net benefit. Adaptive Acceptance and network tokens are the named cost-savings drivers; card account updater has no cost-savings row.

## Dashboard report and chart

Date-range and weekly/monthly aggregation filters apply to charts, metrics, and tables. The per-feature report shows estimated recovered volume, recovered payments, success-rate increase, and cost savings; `Show summary` provides an aggregate view. The download lists payments where optimization features were applied for acceptance-rate benefits and Stripe's estimated contribution likelihood. Its presence is not proof of an actual counterfactual outcome.

The guide says cost savings appear in the Dashboard when the business has at least 100 USD equivalent in estimated savings across Adaptive Acceptance and network tokens over the last 12 months. This display threshold is distinct from the domestic US/Canada scope of cost-estimate display and from merchant eligibility.

The payment-success-rate chart is for **CNP payments only**. It shows the raw attempt rate, which counts repeat attempts for the same purchase, rather than the deduplicated rate based on final purchase outcomes. Its dotted blue line is an **estimated** rate without optimizations, not a measured control group.

## Capture and asset provenance

The two 136-line captures differ in local versus remote image references, italics, heading whitespace, and Markdown table layout. The May capture's downloaded assets, `raw/assets/stripe-authorization-boost.png` and `raw/assets/stripe-payment-success-rate.png`, are historical capture artifacts. The November capture references CDN image URLs; that presentation change supplies no evidence of a changed chart or feature rollout.

## Related

- Company: [[stripe]]
- Concept: [[stripe-authorization-boost]]
- Related source: [[source-stripe-authorization-boost-ab-test]], [[source-stripe-payments-recommendations]]

## Raw Sources

- [[raw/stripe-payments-analytics-optimization-2026-11-07|November 7, 2026 optimization guide]] — full page with CDN image references.
- [[raw/stripe-payments-optimization-2025|May 8, 2026 optimization guide]] — full page with downloaded local image references.
