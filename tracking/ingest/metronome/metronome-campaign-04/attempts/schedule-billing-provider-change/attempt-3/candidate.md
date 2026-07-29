---
title: "Schedule a billing provider change"
type: source
date_ingested: 2026-07-29
canonical_url: "https://docs.metronome.com/guides/customers-billing/manage-customers/schedule-billing-provider-change"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/manage-customers/schedule-billing-provider-change-2026-07-13.md"
tags: [metronome, billing-providers, contract-billing, marketplace-billing]
---

## Overview
Metronome documents how to change the billing-provider configuration on an existing contract without replacing the contract. The contract retains an ordered schedule of provider-configuration segments aligned to billing-period boundaries, allowing invoice delivery to move among Stripe, NetSuite, and AWS, Azure, or GCP marketplace providers subject to transition-specific timing constraints.

## Key takeaways
- A provider change is added through `add_billing_provider_configuration_update` on `POST v2/contracts/edit`; its `effective_at` is either `START_OF_CURRENT_PERIOD` or `START_OF_NEXT_PERIOD`.
- Stripe-to-Stripe, Stripe-to-NetSuite, and NetSuite-to-Stripe changes may start in the current or next period. Every transition to or from a marketplace, including marketplace-to-marketplace, is next-period only.
- A current-period correction can reroute a draft invoice, but it does not reroute an invoice already finalized and sent. Metronome states that every invoice is sent exactly once.
- Marketplace transitions require threshold billing to be removed before switching to the marketplace. Each contract is limited to 10 schedule segments unless the account team grants additional capacity.
- Existing consumers of `customer_billing_provider_configuration` remain compatible because that field continues to expose only the currently active configuration; the full history and future schedule is available separately.

## Supported transitions

| Transition | Start of current period | Start of next period |
| --- | --- | --- |
| Stripe → Stripe | Supported | Supported |
| Stripe → NetSuite | Supported | Supported |
| NetSuite → Stripe | Supported | Supported |
| Stripe → marketplace | Not supported | Supported |
| Marketplace → Stripe | Not supported | Supported |
| Marketplace → marketplace | Not supported | Supported |
| NetSuite → marketplace | Not supported | Supported |
| Marketplace → NetSuite | Not supported | Supported |

Here, marketplace covers AWS Marketplace, Azure Marketplace, and Google Cloud Marketplace.

## Scheduling prerequisites and request
The operation applies to an existing contract and identifies the customer, contract, and destination billing-provider configuration. The request uses `add_billing_provider_configuration_update` on `POST v2/contracts/edit` and chooses one of the two supported symbolic boundaries in `schedule.effective_at`.

Before a move to any marketplace provider, active threshold billing must be disabled. Marketplace-involved changes cannot use `START_OF_CURRENT_PERIOD`; they must begin at `START_OF_NEXT_PERIOD` because marketplace billing is metered from the beginning of a period.

## Effective timing and invoice routing
A contract's provider schedule is an ordered list of segments, each beginning at an `effective_at` timestamp on a billing-period boundary. `START_OF_CURRENT_PERIOD` resolves to the start of the current usage-invoice service period, while `START_OF_NEXT_PERIOD` resolves to the start of the following service period.

For a current-period Stripe configuration correction, the current draft invoice is routed to the new configuration. A finalized invoice already sent to Stripe remains with its original delivery, so the configuration update does not cause it to be sent again. For a next-period Stripe-to-marketplace transition, every invoice from the current period continues through the existing Stripe configuration and the marketplace configuration starts with the next period.

When moving to a marketplace, the existing provider completes the current period. When moving away from a marketplace, the marketplace continues billing through the end of that period.

> [!warning] Timing description requires clarification
> The overview selects the active configuration using the latest `effective_at` before an invoice's service-period end date (or its `issued~at` date when there is no service-period end), while the constraints section says each invoice maps by its service-period start date. The page does not reconcile those formulations for unusual service periods or invoices without a service-period end.

## Contract response and customer-facing effects
`POST v2/contracts/get` returns two different views. `customer_billing_provider_configuration` remains backward compatible and continues to return the currently active configuration, so integrations reading that field require no change. `billing_provider_configuration_schedule` returns all past, current, and future segments in order, with `effective_at` and `effective_until` boundaries.

The documented effects are on contract configuration and invoice routing; the page does not describe a change to the Metronome customer identity or creation of a replacement contract.

## Cross-system responsibility boundary
Metronome owns the contract schedule and uses it to choose where each invoice is delivered. The current provider remains responsible for the periods assigned to its segment, and marketplace metering cannot be transferred in the middle of a period.

The page does not document how destination configurations are created, how customer or account identifiers are provisioned or reconciled in Stripe, NetSuite, AWS, Azure, or GCP, or how operators verify that an external provider is ready before scheduling the change. Responsibility and sequencing for those external-system preparations therefore remain unspecified by this source.

## Limits, replacement, and open questions
- A contract may have at most 10 provider-configuration schedule segments. Additional capacity requires contacting the Metronome account team.
- A future scheduled change is not deleted directly in the documented flow. To cancel it, schedule a newer segment for the same period; the latest segment takes precedence.
- The page does not specify validation errors, retry or idempotency behavior for `contracts/edit`, how simultaneous edits are resolved, or whether a scheduled future segment can be inspected before acceptance beyond fetching the resulting schedule.
- The page does not explain what happens if the destination provider configuration becomes invalid after scheduling but before it takes effect.

## Related
- Company: [[wiki/companies/metronome|Metronome]]
- Concepts: [[wiki/concepts/metronome/metronome-customers-and-contracts|Metronome customers and contracts]], [[wiki/concepts/metronome/metronome-invoicing|Metronome invoicing]], [[wiki/concepts/metronome/metronome-integrations|Metronome integrations]]

## Raw Sources
- [[raw/metronome/guides/customers-billing/manage-customers/schedule-billing-provider-change-2026-07-13|Schedule a billing provider change — verbatim Metronome documentation]]
