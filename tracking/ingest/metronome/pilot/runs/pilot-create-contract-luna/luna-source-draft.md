---
title: "Create a contract"
type: source
date_ingested: 2026-07-14
canonical_url: "https://docs.metronome.com/api-reference/contracts/create-a-contract"
original_format: webpage
raw_files:
  - "metronome/api-reference/contracts/create-a-contract-2026-07-13.md"
tags: [metronome, contracts, usage-based-billing, credits, commits, subscriptions, threshold-billing]
---

## Overview

This page documents the POST /v1/contracts/create operation for creating a contract. The request requires customer_id and starting_at and can configure packages, rate cards, usage schedules, credits and commits, overrides, scheduled charges, subscriptions, billing configurations, spend trackers, thresholds, and customer hierarchy settings. A successful response returns the created contract in a data envelope, while 400 and 404 responses are documented.

## Key takeaways

- Contracts combine customer products, pricing, discounts, access duration, and billing configuration for PLG and Enterprise use cases.
- The request supports prepaid or postpaid commits, credits, recurring allotments, rollover settings, product- or usage-targeted applicability, and pricing overrides.
- Subscriptions require a subscription rate, collection schedule, and proration configuration; they can use quantity-only or seat-based quantity management.
- Contracts can use usage filters for concurrent contracts, can be edited through editContract with edit history retained, and can configure threshold billing and prepaid-balance thresholds.

## Details

### Endpoint and request

- The API operation is POST /v1/contracts/create with operationId createContract-v1.
- The JSON request body uses CreateContractPayload, whose required fields are customer_id and starting_at.
- The endpoint documents 200 success, 400 bad-request, and 404 not-found responses.

### Contract terms and usage schedules

- starting_at is the inclusive contract start time and ending_before is the exclusive contract end time.
- Usage statement schedules support monthly, quarterly, annual, and weekly frequencies; if no day is supplied, the schedule defaults to the first day of the month.
- A custom billing anchor date can align future usage statements to a chosen cadence, and invoice_generation_starting_at can defer automatic usage-invoice generation for historical invoice imports.

### Pricing and contract components

- A contract can reference a rate card by rate_card_id or rate_card_alias; rate-card product and price changes can propagate to associated contracts.
- Time-bounded overrides can target products, product tags, or usage specifiers and support overwrite, multiplier, and tiered pricing behaviors.
- Scheduled charges support one-time, recurring, or custom charges on specific dates, separate from usage billing or commitments.

### Commits and credits

- Commits support PREPAID and POSTPAID types with access and invoice schedules; prepaid commits can omit an invoice schedule to create a complimentary commit.
- Credits provide spending allowances and can be scoped by product IDs, product tags, or usage specifiers.
- Recurring commits and credits support recurrence frequency, commit duration, proration, and optional subscription configuration.
- rollover_fraction controls how much unused commit or credit balance rolls over, with values constrained between 0 and 1.

### Subscriptions

- Subscription inputs require subscription_rate, collection_schedule, and proration.
- Subscription rates specify a billing frequency and product ID that must match an existing subscription rate on the rate card.
- Quantity management defaults to QUANTITY_ONLY; SEAT_BASED subscriptions use seat identifiers and require seat_config.
- Subscription billing cycles can be anchored to a date and placed on scheduled invoices or usage invoices.

### Thresholds, providers, and hierarchy

- spend_threshold_configuration can initiate a threshold charge when usage reaches a configured amount.
- prepaid_balance_threshold_configuration can recharge a prepaid balance when it falls to a configured threshold and can use a custom credit type.
- Billing provider configuration can be selected by configuration ID or by provider and delivery method.
- Hierarchy configuration can define parent or child contracts, invoice consolidation behavior, and whether the parent or child pays invoice charges.

### Lifecycle and routing

- Created contracts can be edited through editContract, with edits retained in the audit log and exposed through getEditHistory.
- Customers may have multiple concurrent contracts, and usage_filter routes usage to the appropriate contract.
- uniqueness_key prevents duplicate contract creation; reusing a previously used key causes the request to fail with a 409 error.

## Change history

- 2026-07-14: Luna pilot draft from the assigned raw snapshot.

## Related

- Company: [[metronome]]
- Concepts: coordinator concept audit required before promotion.

## Raw Sources

- [[raw/metronome/api-reference/contracts/create-a-contract-2026-07-13|2026-07-13 snapshot]]
