---
title: "Metronome Customers and Contracts"
type: concept
category: technology
tags: [metronome, customers, contracts, invoicing]
---

## Definition

Metronome customers are the billing entities to which usage is attributed. Contracts represent the commercial terms a customer has agreed to pay, generally starting from a rate card with optional negotiated discounts or commitments layered on top.

## Customer matching

An ingest alias associates an application-defined identifier with a Metronome customer. The SDK guide recommends this pattern when usage starts before the customer exists in Metronome: send the application's customer-table ID in events, then register it as an alias when provisioning the customer.

## Contract and invoice behavior

- A basic contract can apply predefined list prices from a rate card.
- Contract-level terms can add negotiated discounts or commitments.
- The contract `starting_at` time determines the billing periods for which invoices are generated.
- Current-period usage appears on a draft invoice, and the guide says its line items update seconds after Metronome receives usage data.

This introductory source does not define the full contract schema, amendment lifecycle, or invoice-state machine; those require dedicated contract and invoicing references.

## Contract creation API

`POST /v1/contracts/create` requires only `customer_id` and `starting_at` at the top level. Optional structures can apply a rate card or package, commits and credits, overrides, scheduled charges, subscriptions, usage routing, thresholds, provider configuration, and hierarchy behavior.

Important creation constraints include:

- `starting_at` is inclusive and `ending_before` is exclusive.
- `package_id` invokes a restricted package-provisioning mode in which only the documented small field subset is accepted; `package_alias` is mutually exclusive with `package_id`.
- Subscription quantity requirements depend on `quantity_management_mode`: quantity-only needs `initial_quantity`, while seat-based needs `seat_config`.
- `uniqueness_key` can prevent duplicate creation; its schema says reuse fails with HTTP 409.
- The scheduled-charge consolidation setting cannot be changed after the contract is created.

## Contract edit history

`POST /v2/contracts/getEditHistory` returns the recorded edit history for one customer contract. Metronome describes this as a full history spanning changes made in the UI, through `editContract`, and through other contract-changing endpoints. Each `ContractEdit` can identify when an edit occurred and group the additions, updates, archives, and removals it contained, including changes to pricing overrides, discounts, charges, commits, credits, subscriptions, usage filters, contract dates, and threshold configuration.

The targeted `POST /v2/contracts/commits/edit` operation is narrower than a general contract edit: it identifies one existing customer- or contract-level commit and changes that commit's fields, schedules, applicability, invoicing contract, rate type, priority, or hierarchy access.

## Edits and transitions

The enterprise guide distinguishes two lifecycle operations. An edit adds terms without starting a new contract. A transition starts a new contract, preserves its relationship to the original, and can apply renewal logic such as rolling over unused commitments or credits.

For recurring-grant upgrades, a renewal at the next period removes future old-contract charges and creates a finalized scheduled invoice plus a new draft usage invoice. A mid-period renewal prorates the first grant and finalizes old-contract usage through the transition date. A backdated renewal moves open-period usage to the replacement contract and uses a one-time adjustment before forward recurrence begins.

## Stripe Dashboard contract management

The Metronome Stripe App embeds customer and contract management in the Stripe Dashboard. It lists Stripe customers linked through Metronome billing-provider configurations and can automatically create a corresponding Metronome customer when contract creation starts. Its four-step wizard configures invoice terms, rate-card pricing and overrides, subscription quantities and product entitlement, credit schedules, and confirmation. The resulting contract uses the Stripe customer's existing billing-provider configuration for invoice delivery.

## Metronome dashboard provisioning

The Metronome dashboard quickstart creates a customer, optionally assigns ingest aliases, and then creates a contract with a rate card and start and end dates. The contract can also select a billing provider and include customer-specific prepaid commits or overrides.

## Sources

- [[source-metronome-guides-get-started-developer-sdks]] — customer aliases, basic contract provisioning, and introductory invoice behavior
- [[source-metronome-api-reference-contracts-create-a-contract]] — create endpoint, request families, conditional requirements, and response boundary
- [[source-metronome-api-reference-contracts-get-contract-edit-history]] — cross-channel contract change history and response structure
- [[source-metronome-guides-get-started-stripe-marketplace-app]] — Stripe Dashboard customer and contract management workflow
- [[source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit]] — enterprise provisioning, edits, transitions, and renewal rollover
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — dashboard customer and contract provisioning
- [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-create-a-pre-paid-commit]] — recurring grants, renewal transitions, and upgrade timing
- [[source-metronome-api-reference-credits-and-commits-edit-a-commit]] — targeted commit edit boundary

## Related

- [[metronome-event-ingestion]]
- [[metronome-products-and-rate-cards]]
- [[metronome-invoicing]]
- [[metronome-integrations]]
- [[metronome-credits-and-commits]]
