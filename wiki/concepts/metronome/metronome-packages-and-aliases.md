---
title: "Metronome Packages and Aliases"
type: concept
category: technology
tags: [metronome, packages, aliases, pricing, grandfathering]
---

## Definition

Metronome packages apply consistently defined pricing to selected customer cohorts, while effective-dated aliases let provisioning choose the applicable package without hard-coding its generated ID.

A package is a customer-agnostic, time-relative template of contract terms layered on one rate card. It can standardize billing terms, commits, credits, subscriptions, thresholds, scheduled charges, and rate overrides across a cohort. Packages cannot be edited after creation; operators version them by creating a new package and scheduling the same alias, so new alias-based provisioning resolves to the new version while existing contracts require separate provisioning or contract editing. [[source-metronome-guides-implement-metronome-core-concepts-packages-overview]]

## Cohort pricing

### Package-association discovery

Bearer-authenticated `POST /v1/packages/listContractsOnPackage` discovers customer and contract UUIDs associated with one required package UUID. Optional mutually exclusive `starting_at` and `covering_date` filters select contracts starting on or after a timestamp or active at one timestamp, while `include_archived` defaults false. HTTP `200` requires top-level `data` and exposes optional nullable sibling `next_page`; each projection requires customer, contract, and start identities but does not return package identity, alias or version, contract terms, rate card, or migration outcome. The page defines no closed interval, default ordering, total count, cursor lifetime, stable snapshot, concurrent-change behavior, or read-after-mutation visibility. Its migration example makes this list only the discovery step before separately ending contracts and provisioning replacements; it does not establish mutation atomicity, rollback, propagation, or reconciliation. [[source-metronome-api-reference-contracts-list-contracts-associated-with-a-package]]


In the documented grandfathering workflow, a product is added to the shared rate card with `entitled: false`, a package override entitles it for new customers, and new contracts select that package by alias while existing customers retain their contracted pricing.

Package rates layer on top of rate-card changes and inherit most such changes; an overwrite override is the stated exception. The guide does not enumerate what `most` excludes beyond overwrite overrides or define precedence for other overlapping package, rate-card, and contract changes.

## Effective-dated alias transition

Creating a second package under the same alias with a later `starting_at` makes unchanged provisioning calls resolve to the newer package from that date, while the original package receives an alias schedule ending at the transition.

This describes future provisioning, not mutation of already-provisioned contracts. Alias uniqueness, overlap handling, exact boundary lookup, timezone semantics, reuse after removal, resolved-package retention, and transition failures are undocumented.

## Sources

- [[source-metronome-api-reference-contracts-list-contracts-associated-with-a-package]] - package-scoped contract and customer association discovery, mutually exclusive time filters, archive visibility, pagination, and migration-authority boundaries


- [[source-metronome-guides-pricing-packaging-billing-model-guides-token-billing]] - illustrative credit-allocation package layered on a managed AI rate card and package-based customer contract provisioning

- [[source-metronome-guides-get-started-api-quickstart]] — core-object orientation that identifies packages as reusable rate-card and contract detail bundles while the direct first-invoice sequence provisions without one

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-make-a-pricing-change]] — package-based cohort grandfathering, rate-card inheritance boundary, and effective-dated alias transition

## Related

- [[metronome-products-and-rate-cards]]
- [[metronome-customers-and-contracts]]
