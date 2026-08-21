---
title: "Metronome Packages and Aliases"
type: concept
category: technology
tags: [metronome, packages, aliases, pricing, grandfathering]
---

## Definition

Metronome packages apply consistently defined pricing to selected customer cohorts, while effective-dated aliases let provisioning choose the applicable package without hard-coding its generated ID.

## Cohort pricing

In the documented grandfathering workflow, a product is added to the shared rate card with `entitled: false`, a package override entitles it for new customers, and new contracts select that package by alias while existing customers retain their contracted pricing.

Package rates layer on top of rate-card changes and inherit most such changes; an overwrite override is the stated exception. The guide does not enumerate what `most` excludes beyond overwrite overrides or define precedence for other overlapping package, rate-card, and contract changes.

## Effective-dated alias transition

Creating a second package under the same alias with a later `starting_at` makes unchanged provisioning calls resolve to the newer package from that date, while the original package receives an alias schedule ending at the transition.

This describes future provisioning, not mutation of already-provisioned contracts. Alias uniqueness, overlap handling, exact boundary lookup, timezone semantics, reuse after removal, resolved-package retention, and transition failures are undocumented.

## Sources

- [[source-metronome-guides-pricing-packaging-make-pricing-changes-make-a-pricing-change]] — package-based cohort grandfathering, rate-card inheritance boundary, and effective-dated alias transition

## Related

- [[metronome-products-and-rate-cards]]
- [[metronome-customers-and-contracts]]
