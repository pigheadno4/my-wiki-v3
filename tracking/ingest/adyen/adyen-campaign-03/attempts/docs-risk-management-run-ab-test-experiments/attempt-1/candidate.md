---
title: "Adyen Risk Profile A/B Experiments"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/run-ab-test-experiments"
raw_files:
  - "adyen/docs/risk-management/run-ab-test-experiments/2026-09-15.md"
tags: [adyen, protect, risk-management, risk-profiles, experiments, live-payments]
---

## Overview

This Adyen Protect guide explains how a Risk admin compares a merchant account's current base risk profile with a variant profile by randomly assigning a selected share of **live** transactions to the two profiles. These experiments process real payments; they are not test simulations. The guide covers setup, traffic split, stop conditions, results, and transaction lookup.

## Key takeaways

- The guide requires an online-payments integration, enabled risk management and premium features, a Customer Area **Risk admin** role, and at least two configured risk profiles. It says only one risk experiment can run at a time and only one can be active per merchant account. Dynamic 3D Secure rules linked to risk checks in the variant profile do **not** trigger during the experiment.
- In live Customer Area, the user selects a merchant account and variant profile and chooses a traffic percentage. Included transactions are split evenly between the base and variant profiles; the page's 20% example assigns 10% of all transactions to each. Payments explicitly assigned a risk profile in the request are excluded. The experiment continues until stopped, but edits to either profile's risk configuration or disabling premium features also stop it.
- Running-experiment results refresh every 15 minutes. The guide provides transaction, issuer-refusal, authorization, risk-block, and Notification of Fraud measures, with deeper chargeback/dispute and refusal information in details. Adyen recommends at least one month before relying on fraud and chargeback rates. Stopping the experiment leaves a separate decision about which profile to assign to the merchant account for future transactions; no automatic winner rollout is stated.

## Detail locators

- Opening and `## Requirements` (raw lines 15–35): live-transaction boundary, premium/role/profile prerequisites, concurrent-experiment limits, and variant-profile Dynamic 3DS limitation.
- `## Start risk experiment` (raw lines 37–63): base/variant identity, merchant account, traffic percentage and even split, stop triggers, and explicitly assigned-profile exclusion.
- `## View experiment results` (raw lines 65–84): running/completed views, 15-minute updates, comparison metrics, and details.
- `## Stop risk experiment` and `## View experiment transactions` (raw lines 86–108): stop action, one-month recommendation, future profile assignment choice, and reference-based transaction search.

## Related

- Company: [[adyen]]
- Concept: [[adyen-risk-management]]

## Raw Sources

- [[raw/adyen/docs/risk-management/run-ab-test-experiments/2026-09-15|2026-09-15 Adyen live risk-profile experiment guide]]
