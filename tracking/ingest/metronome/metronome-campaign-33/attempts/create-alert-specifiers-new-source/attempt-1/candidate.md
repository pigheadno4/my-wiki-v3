---
title: "Metronome Guide: Create Alert Specifiers"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/set-up-notifications/create-alert-specifiers"
raw_files:
  - "metronome/guides/customers-billing/set-up-notifications/create-alert-specifiers-2026-08-28.md"
tags: [metronome, alerts, notifications, credits, commits, custom-fields]
---

## Overview

Metronome alert specifiers segment evaluation of `low_remaining_contract_credit_and_commit_balance_reached` by custom fields on commits and credits. Without specifiers, the alert evaluates one combined balance of all active commits and credits for a customer; specifiers can include matching balances, exclude matching balances, or evaluate a separate group for each value of one custom-field key. This guide configures evaluation scope and notification signals—it does not document a balance mutation, invoice operation, or automatic merchant response.

## Query-critical facts

- `alert_specifiers` applies here to `low_remaining_contract_credit_and_commit_balance_reached`. Within one specifier, explicit inclusion key-value conditions are ANDed; separate specifiers are ORed. Omitting `custom_field_filters` includes all commits and credits, after which any matching exclusion condition removes a balance even if it met the inclusion conditions. Exclusion entries are ORed and must target entities already within that same specifier's inclusion scope.
- The filters depend on custom fields set on commits or credits. Setting or updating an applicable custom-field value triggers reevaluation of a balance alert using `alert_specifiers`; this is an evaluation trigger, not a documented change to the credit or commit balance itself. [[source-metronome-api-reference-custom-fields]] remains the current authority for broad custom-field entity scope and persistence, while [[source-metronome-api-reference-alerts-create-a-threshold-notification]] remains the exact create-operation and nested-schema authority.
- A key without a value creates per-value evaluation. This mode requires exactly one specifier with one group key and cannot group by multiple keys. The guide permits up to three per-key balance alerts for one customer and up to 1,000 unique values for each group key; configurations above 1,000 values are routed to the Metronome support portal rather than assigned a documented higher limit.
- When a grouped value crosses the threshold, Metronome sends a webhook whose returned `alert_specifiers` identifies that key-value pair. The first value to cross also produces an additional alert-level webhook whose filter omits the value. The guide does not define ordering, atomicity, duplicate suppression, evaluation-to-delivery latency, or whether the two deliveries arrive together. [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]] is the authority for ordinary threshold cadence and state, and [[source-metronome-guides-platform-configuration-setup-webhooks]] is the authority for HTTP delivery, retries, deduplication, and verification.
- The worked include pattern filters `ContractCredit` by `promo_code: may_the_fourth` at a `$0` threshold. The worked exclude pattern leaves the base set otherwise inclusive, removes `ContractCreditOrCommit` balances tagged `is_product_specific: true`, and shows numeric `threshold: 10000`; the page does not state that example's currency, pricing unit, or minor-unit interpretation, so `10000` must not be converted into a money amount by inference.
- `POST /v1/customer-alerts/get` can retrieve the current status for a specified key-value pair and the example returns `in_alarm`; the dedicated [[source-metronome-api-reference-alerts-get-a-threshold-notification]] controls locator, response, freshness, and current-state semantics. A return from `IN_ALARM` to `OK` can produce `low_remaining_contract_credit_and_commit_balance_resolved`, but this guide requires support enablement and does not define its delivery timing or recovery behavior.

## Material boundaries and documentation tensions

Alert configuration, evaluation, and delivery are separate authorities. Creating the alert stores configuration; setting or updating a matching custom field triggers reevaluation; a threshold crossing can create webhook signals; none of those statements proves synchronous evaluation, successful delivery, balance or ledger mutation, invoice creation or recalculation, payment or collection, or downstream customer action. [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]] assigns customer communication, service cutoff, restoration, and other product responses to the merchant application.

> [!warning] Field-name tension
> The note comparing alert specifiers with the top-level filter names `alert_specifiers[].custom_field_filter` in the singular, while the guide's definitions and every request or webhook example use `custom_field_filters` in the plural. Use the current create-operation schema rather than silently treating the singular spelling as an accepted request field.

> [!warning] Entity-label tension
> The grouped create example uses `ContractCreditorCommit`, while later grouped webhook examples use `ContractCreditOrCommit`. The guide does not reconcile those labels or establish that both are accepted enum values; verify the current create schema before copying the request.

The page does not define case sensitivity, missing-key treatment for explicit inclusion or exclusion, duplicate conditions, overlap when one balance matches multiple specifiers, grouping behavior for objects without the key, state transitions for newly created or retagged groups, concurrent update ordering, historical replay, status-read freshness, or endpoint-specific create failures. It also does not say that alert evaluation mutates balances or ledgers, changes contracts, recalculates or finalizes invoices, delivers invoices, collects payment, or enforces access.

## Raw-detail coverage map

- **Configuration and matching:** complete include, exclude, multi-specifier OR, within-filter AND, same-specifier exclusion-scope, and single-key grouping rules.
- **Worked requests:** the `$0` tagged-promotion request, per-promotion grouped request, and general-credit exclusion request with literal `threshold: 10000` and their exact entity labels.
- **Notification examples:** grouped key-value payload, additional first-crossing alert-level payload, status lookup request and `in_alarm` response, and support-enabled resolved-event name.
- **Limits and tensions:** three per-key alerts per customer, 1,000-value group-key guidance, support route above that cardinality, singular-versus-plural filter spelling, and `ContractCreditorCommit` versus `ContractCreditOrCommit`.
- **Authority boundaries:** use the dedicated custom-field source for broad persistence, the threshold-create and get sources for API contracts, notification guidance for evaluation state and cadence, webhook guidance for transport, and customer-controls guidance for merchant-owned action.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-alerts-and-notifications]], [[metronome-credits-and-commits]], [[metronome-custom-fields]], [[metronome-webhooks]]
- Related sources: [[source-metronome-api-reference-alerts-create-a-threshold-notification]], [[source-metronome-api-reference-alerts-get-a-threshold-notification]], [[source-metronome-api-reference-custom-fields]], [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]], [[source-metronome-guides-platform-configuration-setup-webhooks]], [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-alerts]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/set-up-notifications/create-alert-specifiers-2026-08-28|2026-08-28 snapshot - complete alert-specifier matching, grouping, webhook, status, limit, and worked-example guide]]
