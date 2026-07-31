---
title: "Let customers manage spend and usage"
type: source
date_ingested: 2026-07-31
canonical_url: "https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/customer-controls"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/optimize-customer-experience/customer-controls-2026-07-13.md"
tags: [metronome, customer-controls, alerts, spend-limits, commit-balances, invoice-totals]
---

## Overview

This guide shows how a merchant can let end users configure spend, commit-balance, and invoice-total thresholds in the merchant's own product. Metronome evaluates the associated alerts and sends signals through webhooks or exposes their status through alert APIs; the merchant remains responsible for the customer-facing interface, communication, and any service-access decision.

## Key takeaways

- Soft and hard spend limits use the same `spend_threshold_reached` alert type in the examples. Their names, threshold values, and downstream actions distinguish them; the page does not document a native soft-versus-hard enforcement mode.
- Metronome evaluates billing-period spend and moves the alert to `in_alarm` when its threshold is reached. A webhook can then drive a customer notification or an application-owned access block.
- A spend threshold measures usage-based spend before credit and commit drawdown, while an invoice-total threshold measures the post-drawdown usage-invoice amount. Neither signal establishes invoice finalization, collection, or payment success.
- `group_values` can scope spend thresholds to one dimension value or evaluate any value for a key. The key must exist as a group key on the underlying billable metrics, and Metronome reprices the selected usage subset as if it were a presentation group.
- A customer can have spend-threshold notifications for three distinct keys. When one key has more than 5,000 values for that customer, the guide directs the merchant to contact a Metronome representative; it does not state a hard value limit.
- `low_remaining_commit_balance_reached` can signal that a commit is nearing depletion. Customer outreach, sales follow-up, and access cutoff remain merchant-owned actions.

## Merchant interface and enforcement boundary

The end user sets limits in the merchant's application, and the shown interface is an example rather than a documented Metronome-hosted customer dashboard component. The merchant creates one alert for each limit, stores the returned alert IDs, and uses those IDs to distinguish actions later. The example's soft and hard alerts differ by name and threshold but share `spend_threshold_reached`; no separate severity field or automatic hard-limit policy is shown.

When an alert enters `in_alarm`, Metronome sends a notification to a configured webhook. The application can notify the customer for a soft limit or disable service access for a hard limit. Although the guide describes hard limits as preventing further usage, its implementation steps make the access block an application action. It does not define an entitlement mutation, automatic request denial, a maximum overshoot, or ordering between threshold evaluation, webhook delivery, and subsequent usage.

For changed limits, the guide tells the merchant to archive the old notification before creating a replacement with the new threshold. It does not define an in-place threshold update, atomic replacement, behavior during the gap, or whether archived alert IDs remain queryable.

## Spend thresholds, denomination, and retrieval

The create examples send `alert_type`, `credit_type_id`, `name`, `threshold`, and `customer_id` to `/v1/alerts/create`. For the documented USD credit type, threshold values are cents, so `10000` represents $100. Other supported currencies use whole units, and spend alerts can also use custom pricing units defined on the Metronome app's Offering page. The page does not provide a complete currency table, precision rules, conversion behavior, or the complete create-alert schema.

Webhook payloads include basic identifiers such as notification type, customer ID, and alert ID. The merchant should verify that the alert and customer IDs match its stored association before acting. The page also permits polling one threshold notification with `/customer-alerts/get` or listing all customer threshold notifications with `/customer-alerts/list`, for example during login. Exact delivery retries, deduplication, signature verification, and broader state semantics belong to the dedicated notification and webhook sources. This page's real-time phrasing does not define a standalone end-to-end latency guarantee.

## Dimension-scoped spend limits

A `group_values` entry with both `key` and `value` targets a specific dimension value, such as one `user_id`. Supplying a key without a value evaluates any value for that dimension; the example says the webhook identifies which `organization_id` breached the threshold. The page does not define how multiple `group_values` entries combine, empty or null values, missing values, or whether one alert can mix exact and any-value selectors.

The group key must be present on billable metrics associated with the customer's contract. Spend from a product whose underlying metric lacks that key does not contribute. For a scoped threshold, Metronome recomputes the invoice as though the selected key were a presentation group key, applying tiering, quantity rounding, or a `MAX` aggregation to the selected subset. This is a threshold calculation rule, not a claim that the contract's actual invoice presentation is changed.

Metronome permits spend-threshold notifications for three keys per customer and blocks use of a fourth key. For a key with more than 5,000 values for one customer, the guide requests representative consultation rather than stating that the configuration is rejected. This threshold-specific rule is distinct from the separate billable-metric guidance that warns of possible API latency as group-key cardinality approaches 1,000 values.

The displayed `/v1/customer-alerts/get` body is not valid JSON because it omits a comma after `alert_id`; use the dedicated API reference rather than copying the example literally.

## Commit-balance and invoice-total controls

The commit example creates `low_remaining_commit_balance_reached` with a credit type, threshold, and customer. The resulting signal can support customer messaging, sales outreach, or an application-owned cutoff when the balance reaches zero. The page does not define which customer- or contract-level commits contribute, priority or applicability effects, treatment of expired balances, or whether credits are included. It also does not automatically prevent usage or renegotiate a contract.

`spend_threshold_reached` uses usage-based spend before credit and commit drawdown. By contrast, `invoice_total_reached` evaluates the amount after drawdown; the example narrows it to usage invoices with `invoice_types_filter: ["USAGE"]`. The page does not define draft-versus-finalized evaluation, taxes, adjustments, scheduled charges, payment collection, paid or failed status, repeated alarm behavior, or how later invoice changes affect the alert.

## Documentation cautions

The invoice-total curl example contains a credential-looking bearer literal rather than the `<TOKEN>` placeholder used elsewhere. It should not be copied or treated as a usable credential; use a separately provisioned secret.

This guide supplies application patterns, not a complete customer-controls product or enforcement contract. It does not document a hosted end-user dashboard, authentication or authorization for editing limits, alert creation idempotency, notification ordering, access re-enablement, failure recovery, race handling, service-denial guarantees, invoice lifecycle state, or payment outcome.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-alerts-and-notifications]], [[metronome-webhooks]], [[metronome-billable-metrics]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/optimize-customer-experience/customer-controls-2026-07-13|2026-07-13 snapshot — merchant-configured spend, commit-balance, and invoice-total controls]]
