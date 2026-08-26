---
title: "Metronome Guide: Create Packages"
type: source
date_ingested: 2026-08-26
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/implement-metronome/core-concepts/packages-overview.md"
raw_files:
  - "metronome/guides/implement-metronome/core-concepts/packages-overview-2026-07-13.md"
tags: [metronome, packages, aliases, contracts, rate-cards, pricing]
---

## Overview

This guide defines a package as a reusable, time-relative set of contract terms for provisioning cohorts with the same contract structure while maintaining one rate card. The package is created without a customer or customer billing configuration; a later contract-create call binds the selected package to a customer and absolute contract start.

## Query-critical facts

- Package creation requires connected usage events, a billable metric, a product, and a rate card. `/packages/create` can encode default duration and payment terms, billing provider, rate-card choice, commits, credits, subscriptions, threshold billing, scheduled charges, and rate overrides.
- Package terms use relative timing: `starting_at_offset` derives a term start from contract start, `duration` derives its exclusive end from that offset, and `date_offset` represents point-in-time terms without duration. Package aliases can replace generated IDs in contract provisioning.
- Customers are provisioned through `/contracts/create`. When a package is selected, Metronome currently accepts only `package_id` or `package_alias` plus `transition`; combining additional terms with package provisioning returns HTTP 400. The resulting contract retains an attached package ID visible in the app, data export, and API.
- Packages cannot be edited after creation. Pricing evolution uses a new package and an effective-dated alias schedule; unchanged alias-based provisioning selects the new package for new customers after its effective time. Existing contracts are not described as automatically rewritten: the guide instead directs operators to provision with a new package or edit an underlying contract.
- Package-term custom fields pass down to associated contracts. Package custom fields cannot be updated after being set, while the contract-level values created from them can be updated through `/customFields/setValues`; the listed supported package-term entities are commit, credit, scheduled charge, and subscription.

## Material boundaries

This guide is a workflow and example authority, not the complete schemas for package creation, contract creation, aliases, rates, terms, or custom fields. It does not define alias uniqueness or overlap resolution, selection behavior exactly at an effective-time boundary, package-create validation and errors, concurrent version rollout, rollback, propagation timing, or whether later rate-card changes alter already-provisioned contracts. The package examples do not establish accounting, tax, provider-delivery, payment-success, entitlement, or revenue-recognition outcomes.

## Raw-detail coverage map

Use the raw page for the complete UI sequence; both curl examples; all example amounts, dates, IDs, schedules, subscription and credit fields; the exact relative-time field examples; package listing and cohort-management endpoints; and the full package-term custom-field entity list. Dedicated API references remain authoritative for complete request, response, error, and concurrency contracts.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-packages-and-aliases]], [[metronome-customers-and-contracts]], [[metronome-products-and-rate-cards]]
- Secondary concept: [[metronome-custom-fields]]

## Raw Sources

- [[raw/metronome/guides/implement-metronome/core-concepts/packages-overview-2026-07-13|2026-07-13 snapshot - package definition, creation and provisioning flow, immutable versioning, alias rollout, and term custom fields]]
