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

This operational guide describes subscription price changes, free-trial structures, add-ons, transitions, and cancellation through Metronome rate cards and customer contracts. It provides lifecycle guidance rather than the complete schema for contract creation or editing.

## Key takeaways

- Changing a subscription rate on its rate card flows to inheriting contracts at the next billing period; a contract-level overwrite retains that contract's overwritten price.
- A trial shorter than a billing cycle uses two consecutive subscriptions and a $0 override on the first; a full-cycle trial uses one time-bounded $0 override before list-rate billing resumes in the next period.
- A subscription has one rate per billing period, allowing scheduled rate-card changes without interrupting mid-cycle customers.
- Add-ons use the `add_subscription` edit-contract action. The guide says the relevant rate's `entitlement` must be `true`; this is the guide's terminology, not authoritative request-field spelling.
- Metronome recommends renewal transitions for upgrades and downgrades. It limits proration to upgrades, while a downgrade takes effect at the next billing period.

## Lifecycle operations

For an upgrade or downgrade, the guide recommends a contract transition with `transition.type` set to `renewal`. It describes the transition as ending the first subscription and starting the second in one API call, automatically handling proration, keeping original and new package rates separately auditable, and handling credit rollover for credit-based subscription models. The guide bounds proration to upgrade motions such as increasing quantity or adding a subscription mid-period; decreasing quantity takes effect at the next billing period.

A cancellation can end the contract or only the subscription by moving the respective end date through the linked edit-contract endpoint. Metronome recommends ending the contract for most cancellations; if the customer later restarts, it recommends creating a new contract so the contract remains the source of truth for the active plan. Ending a hybrid subscription also requires ending its recurring credit separately. After the latest service period is finalized, changing a contract end date does not update the subscription end date; an in-advance subscription needs a new subscription for future active service periods.

## Documentation boundaries

> [!warning] Endpoint-link inconsistency
> The upgrade/downgrade section calls its route the "create contract endpoint" but links to the edit-contract path. This guide does not establish the authoritative endpoint or full payload shape for `transition.type=renewal`; use dedicated current contract API references for implementation.

> [!info] Entitlement terminology
> This guide says the subscription-rate `entitlement` must be `true` for an add-on. Existing Metronome rate-card context documents `entitled`; no dedicated schema source reviewed here reconciles those spellings, so this guide does not establish an authoritative request field.

The guide does not define trial date-boundary semantics, the edit-contract request schema, entitlement defaults, contract-transition validation, cancellation effects on invoices, or concurrency and retry behavior.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-subscriptions]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]], [[metronome-credits-and-commits]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]]
- Legacy mutation context: [[source-metronome-api-reference-contracts-amend-a-contract]] — retiring amendment endpoint, not the edit-contract endpoint linked by this guide

## Raw Sources

- [[raw/metronome/guides/pricing-packaging/subscription/manage-subscription-lifecycle-2026-07-13|2026-07-13 snapshot — subscription pricing, trials, transitions, and cancellation]]
