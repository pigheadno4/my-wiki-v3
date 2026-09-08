---
title: "Metronome Guide: Threshold Notifications"
type: source
date_ingested: 2026-09-08
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/set-up-notifications/threshold-notifications"
raw_files:
  - "metronome/guides/customers-billing/set-up-notifications/threshold-notifications-2026-07-13.md"
tags: [metronome, alerts, notifications, usage-based-billing]
---

## Overview

This guide compares Metronome threshold notifications for commit and credit balances, billing-period spend or usage, and invoice totals. It also routes readers to the notification-type catalog, webhook payload examples, UI and API setup, and evaluation triggers.

## Key takeaways

- Commit and credit notifications monitor remaining balances at customer or contract level. The guide explicitly excludes individual seat-scoped credits from those calculations; its separate seat-balance type uses `seat_filter` to scope a seat-based subscription and can optionally narrow to one seat.
- Spend thresholds evaluate usage-based spend before commit and credit drawdown, and exclude commit purchases. Billable-metric usage thresholds compare current-billing-period usage, while invoice thresholds evaluate each active invoice separately after credits, commits, and other adjustments, in the specified currency.
- Notifications can be configured in the UI or through `POST /v1/alerts/create`. The guide says usage ingestion and specified metadata changes trigger evaluation, and that notifications are sent to configured webhooks within minutes after the condition is met.

> [!warning] Action boundary
> The guide presents customer messages and upgrade workflows as possible uses of threshold signals. It documents webhook notification, not automatic spend enforcement, product upgrades, customer access changes, or other merchant action.

## Detail navigation

- `Threshold notification types` contains the alert-type identifiers, aggregation rules, custom-field and grouping filters, pricing-unit cautions, and the current-billing-period definition.
- `Webhook payload examples` shows example property placement for balance, spend, commit, usage, and invoice-total events; treat the shown values as examples, not guarantees for every alert type.
- `Creating and managing threshold notifications` gives the UI steps plus the `/v1/alerts/create` and `/v1/customer-alerts/get` routes, and cautions against scraping the status endpoint in place of webhook consumption.
- `Threshold notification evaluation triggers` names usage ingestion and customer metadata changes as evaluation triggers and gives the guide's source-scoped delivery timing statement.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-alerts-and-notifications]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/set-up-notifications/threshold-notifications-2026-07-13|Threshold notifications (2026-07-13)]] — complete guide with category definitions, alert-type details, payload examples, setup routes, and evaluation triggers
