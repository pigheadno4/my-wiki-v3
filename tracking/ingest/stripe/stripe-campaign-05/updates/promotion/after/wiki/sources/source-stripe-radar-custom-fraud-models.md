---
title: "Stripe — Custom Fraud Models"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/radar/custom-fraud-models
raw_files:
  - "stripe-radar-custom-fraud-models-2026-11-07.md"
  - "stripe-radar-custom-fraud-models-2026.md"
tags: [stripe, radar, custom-fraud-model, metadata, machine-learning, fraud-detection]
---

## Summary

The May 10 and November 7, 2026 guides describe [[stripe]] Radar custom fraud models as combining a merchant's structured payment metadata with Stripe's global fraud signals. The November guide also documents how to request preview access.

## Preview access

The November guide asks the merchant to enter an email to request access, and its documentation-side example uses the preview identifier `radar_custom_models_preview`. The May capture gives no registration path. Requesting access is separate from Stripe's onboarding assessment, training, and deployment. The captures leave approval, account and plan eligibility, general availability, and numerical volume thresholds unverified.

## Requirements and model workflow

1. The merchant sends structured business signals on payment objects. `PaymentIntent.metadata` is one standard API field the guides give as an example. The merchant must first supply the relevant metadata. The guides describe no additional action once those signals are sent.
2. Stripe evaluates whether transaction history is sufficient during onboarding and trains a business-specific model using merchant metadata and global fraud signals.
3. After deployment, a Radar risk score incorporating Stripe's global intelligence and the merchant's signals becomes available without further integration changes at that stage. The captures leave score selection and out-of-scope traffic behavior unspecified.
4. Stripe retrains the model as the product catalog, customer base, and fraud patterns change.

The guides describe potential benefits such as finding fraud that looks normal in global traffic, approving legitimate payments that appear riskier globally, and improving the tradeoff between false positives and missed fraud. The captures supply no performance measurement for a merchant.

## Examples of metadata

| Signal | Examples |
| --- | --- |
| User | Account age, verification status, VIP flag |
| Behavior | Session duration, time from login to checkout, interaction frequency |
| Product | Product category, item value tier, shipping method |
| Risk | Internal evaluations, usage-to-payment ratios |

These examples illustrate business-specific signals. Follow the separate [[source-stripe-payment-intents|Payment Intents metadata guidance]] for keeping sensitive data out of metadata.

## Related Pages

- [[stripe-radar]] — Radar concept and custom scores
- [[source-stripe-radar-optimize-risk-factors]] — separate guidance on risk factor data quality

## Raw Sources

- [[raw/stripe-radar-custom-fraud-models-2026-11-07|November 7, 2026 custom fraud models guide]]
- [[raw/stripe-radar-custom-fraud-models-2026|May 10, 2026 custom fraud models guide]] — verbatim overview
