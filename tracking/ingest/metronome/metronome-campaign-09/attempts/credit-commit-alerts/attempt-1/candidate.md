---
title: "Metronome Credit and Commit Threshold Notifications"
type: source
date_ingested: 2026-08-01
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/alerts"
raw_files:
  - "metronome/guides/pricing-packaging/apply-credits-and-commits/alerts-2026-07-13.md"
tags: [metronome, credits, commits, threshold-notifications, entitlements, upsell]
---

## Overview

This guide describes threshold notifications on Metronome credit and commit balances. It presents access, renewal, and upsell use cases; names supported balance dimensions; and gives a UI workflow for narrowing a zero-balance credit alert with a custom field.

## Key takeaways

- Metronome supports notifications based on remaining credit or commit balance, percent remaining, and days remaining.
- These notifications can inform entitlement workflows when prepaid customers cannot use the product after exhausting balance, or sales workflows when a commitment is nearly exhausted. The page does not say that the notification itself blocks product access, changes an entitlement, or renegotiates a commitment.
- Custom fields can narrow a notification to a subset of credits or commits. The worked example selects credits with `credit_type: free_trial`, uses the **Contract credit balance** notification type, and sets its threshold to `$0` for selected customers.

## Threshold dimensions and use cases

The guide identifies three notification dimensions for credits and commits: remaining balance, percent remaining, and days remaining. A prepaid PayGo example says a customer that cannot pay in arrears should be cut off after its credit or commit balance reaches zero. A separate annual-commit example uses early 90% consumption as a signal for renewal or upsell discussions.

These examples establish notification use cases, not an end-to-end enforcement or sales automation contract. The page does not specify whether Metronome automatically denies product requests, mutates entitlement state, contacts a customer, opens a sales workflow, or performs a renewal or upsell. It also does not define evaluation cadence, delivery channel, latency, retries, ordering, repeated-trigger behavior, or recovery after balance increases.

## Custom-field filtering workflow

The UI example first adds a `credit_type` custom field to credit entities and assigns values such as `free_trial`. The user then creates a notification, chooses **Contract credit balance**, enters a `$0` threshold, applies an advanced filter where `credit_type` equals `free_trial`, and selects the customers in scope.

The example does not define API request or response fields, supported operators, case sensitivity, missing-field behavior, multiple-filter semantics, or whether the selected balance aggregates multiple matching credits. The page likewise does not define the denominator or rounding for percent remaining, the date basis or time zone for days remaining, or whether the available dimensions behave identically for credits and commits.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-alerts-and-notifications]], [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-customers-billing-manage-customers-manage-product-access]], [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]], [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/apply-credits-and-commits/alerts-2026-07-13|2026-07-13 snapshot — credit and commit threshold dimensions, use cases, and custom-field filtering]]
