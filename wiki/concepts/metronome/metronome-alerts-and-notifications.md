---
title: "Metronome Alerts and Notifications"
type: concept
category: technology
tags: [metronome, alerts, notifications, credits, trials]
---

## Definition

Metronome alerts evaluate a configured billing condition and produce a notification that merchant systems can use as an action signal. Alert-definition semantics are separate from the HTTP delivery, retry, deduplication, and signature-verification mechanics in [[metronome-webhooks]].

## Trial credit-balance example

A customer-scoped Contract credit-balance alert with a `$0` threshold can signal that a capped trial credit has been exhausted or expired. The guide's notification type is `alerts.low_remaining_contract_credit_and_commit_balance_reached`, with example fields including `customer_id`, `alert_id`, `threshold`, `alert_name`, `credit_type_id`, `remaining_balance`, and `triggered_by`.

The merchant owns any email, access restriction, or feature re-enablement that follows the notification. The source does not establish whether the threshold isolates the trial credit or aggregates other contract balances, how `triggered_by` classifies expiration or simultaneous triggers, or whether “real-time” implies a specific latency.

## Sources

- [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]] — customer-scoped trial alert, threshold, payload fields, and merchant-action boundary

## Related

- [[metronome-webhooks]]
- [[metronome-credits-and-commits]]
- [[metronome-customers-and-contracts]]
- [[metronome-usage-based-billing]]
