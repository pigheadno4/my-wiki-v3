---
title: "Metronome Manage Subscription Lifecycle"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/pricing-packaging/subscription/manage-subscription-lifecycle"
raw_files:
  - "metronome/guides/pricing-packaging/subscription/manage-subscription-lifecycle-2026-07-13.md"
tags: [metronome, subscriptions, pricing, free-trials, contract-transitions, cancellation]
---

## Overview

This operational guide describes how Metronome manages subscription price changes, trials, add-ons, transitions, and cancellation through rate cards and customer contracts. It supplies lifecycle guidance, not the complete request schema for contract creation or editing.

## Key takeaways

- Changing a subscription rate on its rate card flows to inheriting contracts at the next billing period; a contract-level overwrite keeps that contract on its overwritten price.
- A trial shorter than a billing cycle uses two subscriptions and a $0 override on the first; a full-cycle trial uses one time-bounded $0 override, then returns to the rate-card list rate in the next period.
- A subscription can have only one rate per billing period, so scheduled card changes do not interrupt customers mid-cycle.
- Add-ons use the `add_subscription` edit-contract action and require the relevant subscription rate to be entitled.
- Metronome recommends renewal transitions for upgrades and downgrades; it says only upgrades are prorated, while a downgrade takes effect at the next billing period.

## Lifecycle operations

For an upgrade or downgrade, the guide recommends a contract transition with `transition.type` set to `renewal`. It describes the transition as ending the first subscription and starting the second in one API call, automatically handling proration, preserving a clean audit separation between package rates, and handling credit rollover for credit-based subscription models. The guide limits proration to upgrade motions such as increasing quantity or adding a subscription mid-period; decreasing quantity takes effect at the next billing period.

A cancellation can end the contract or only the subscription by moving the relevant end date through the edit-contract endpoint. Metronome recommends ending the contract for most cancellations and creating a new contract if the customer later restarts. Ending only a hybrid subscription also requires ending its recurring credit separately. If the most recent service period is finalized, extending or removing a contract end date does not automatically extend the subscription; an in-advance subscription then needs a new subscription through `EditContract` for future active service periods.

## Documentation boundary

> [!warning] Endpoint-link inconsistency
> The upgrade/downgrade section calls its route the "create contract endpoint" but links to the edit-contract path. This guide does not establish the authoritative endpoint or full payload shape for `transition.type=renewal`; use the dedicated contract API references for implementation.

The guide does not define trial date-boundary semantics, the edit-contract request schema, entitlement defaults, contract-transition validation, cancellation effects on invoices, or concurrency and retry behavior.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-contracts-amend-a-contract]], [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]]

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/manage-subscription-lifecycle-2026-07-13|2026-07-13 snapshot — subscription pricing, trials, transitions, and cancellation]]
