---
title: "Let customers manage spend and usage"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/customer-controls"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/optimize-customer-experience/customer-controls-2026-08-28.md"
  - "metronome/guides/customers-billing/optimize-customer-experience/customer-controls-2026-07-13.md"
tags: [metronome, customer-controls, alerts, spend-limits, commit-balances, invoice-totals]
---

## Overview

This guide shows how a merchant can expose spend, commit-balance, and invoice-total controls in its own product. It defines a principal-actor flow in which an end user chooses limits, the merchant application creates and tracks threshold notifications, Metronome evaluates billing conditions and sends webhook signals, and the merchant application decides how to notify the customer or control service access.

## Query-critical facts

- For spend limits, an end user sets the threshold in the merchant application, that application creates a `spend_threshold_reached` notification, Metronome evaluates billing-period spend and moves the notification to `in_alarm`, and Metronome sends the configured application webhook a signal that can be used for customer communication or an optional access block.
- The merchant application is responsible for matching the webhook's alert ID and customer ID to its stored association and for deciding whether the signal represents its soft or hard limit. Customer messaging and disabling access are application actions; the guide does not document a Metronome entitlement mutation or automatic request denial. When a limit changes, the workflow archives the previous notification before creating a replacement.
- A dimension-scoped spend threshold uses a `group_values` key that must be a group key on billable metrics associated with the customer's contract. Products whose underlying metric lacks that key do not contribute. Metronome recomputes the selected subset as though the key were a presentation group key, so tiering, quantity rounding, and `MAX` metric behavior apply to the subset.
- A customer can have spend-threshold notifications for three distinct keys and is prevented from adding one with a fourth key. For a key with more than 5,000 values for that customer, the current guide routes configuration discussion through the Metronome support portal rather than documenting a hard maximum.
- `low_remaining_commit_balance_reached` provides a signal for customer or sales outreach and can trigger a merchant-owned cutoff when a commit balance reaches zero. `spend_threshold_reached` evaluates usage-based spend before credit and commit drawdown, while `invoice_total_reached` evaluates after drawdown and can be restricted to usage invoices.

## Material boundaries

- The guide's hard-limit language does not establish native access enforcement: its explicit workflow assigns service blocking to the merchant application after webhook receipt. It does not define automatic denial, maximum overshoot, ordering between evaluation, delivery, and later usage, or access restoration.
- Archiving an old notification and creating a replacement is not documented as atomic, and the guide does not define behavior during the replacement gap or in-place threshold updates.
- The post-drawdown invoice-total signal does not establish invoice finalization, delivery, collection, payment success, settlement, or how later invoice changes affect the alert. The commit-balance example likewise does not define which balances aggregate into the signal or automatically renegotiate a contract.

## Raw-detail coverage map

Use the raw page for the complete spend-alert create examples; currency and custom-pricing-unit denomination note; current **Developer - Notifications - Webhooks** configuration route; webhook payload-handling walkthrough; archive and polling examples; exact-value and any-value `group_values` requests; the malformed customer-alert lookup JSON; subset-repricing explanation; three-key and high-cardinality support guidance; commit-balance request; invoice-total request and usage-invoice filter; and the credential-looking bearer literal that should not be copied. Dedicated notification, webhook, alert API, billable-metric, credit/commit, and invoice sources remain authoritative for their complete schemas, delivery contracts, lifecycle semantics, and downstream outcomes.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-alerts-and-notifications]], [[metronome-billable-metrics]], [[metronome-credits-and-commits]], [[metronome-invoicing]]
- Supporting concepts: [[metronome-webhooks]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/optimize-customer-experience/customer-controls-2026-08-28|2026-08-28 snapshot - customer-set thresholds, merchant-owned actions, dimension controls, and current support routes]]
- [[raw/metronome/guides/customers-billing/optimize-customer-experience/customer-controls-2026-07-13|2026-07-13 snapshot - prior webhook UI and representative-contact wording]]
