---
title: "Metronome API: Create a Package"
type: source
date_ingested: 2026-09-13
canonical_url: "https://docs.metronome.com/api-reference/contracts/create-a-package"
original_format: webpage
raw_files:
  - "metronome/api-reference/contracts/create-a-package-2026-08-28.md"
tags: [metronome, api-reference, packages, contracts, aliases]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/packages/create` operation (`createPackage-v1`) for creating a reusable, customer-agnostic package of time-relative contract terms on top of a rate card. Packages are intended for consistent cohort pricing; the page directs negotiated custom terms to the more flexible contract-creation operation.

## Key takeaways

- Package dates are expressed relative to a future contract's start: `starting_at_offset` determines a generated start, `duration` determines an exclusive end from that start, and `date_offset` represents a point-in-time date. The documented relative-date units are days, weeks, months, and years.
- Aliases are human-readable substitutes for package IDs during contract provisioning. Reassigning an alias updates the original package's alias schedule, and the alias references the package to which it was most recently assigned.
- Packages cannot be edited after creation. Rate-card changes or direct edits to a provisioned contract are the documented alternatives, and an edited contract remains associated with the package used to provision it.
- If a package specifies billing-provider configuration, successful provisioning requires the customer to have exactly one matching billing-provider configuration.
- HTTP `200` returns the created package identifier at `data.id`.

## Material warnings and boundaries

> [!warning] Package definitions are immutable
> The operation creates a package that cannot later be edited. Use a new package/version, rate-card changes, or direct contract edits according to the intended scope; direct contract edits do not remove the original package association.

> [!warning] Alias reassignment changes routing
> Assigning an alias already in use updates the original package's alias schedule and makes the alias reference the most recently assigned package. Treat this as a consequential provisioning-route change.

> [!warning] Billing-provider matching can block provisioning
> When the package sets `billing_provider` and `delivery_method`, the customer must have one and only one matching billing-provider configuration for provisioning to succeed.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/v1/packages/create` -> `post` (`operationId: createPackage-v1`).
- **Package inputs:** `components.schemas.CreatePackagePayload` is the request schema and requires `name`; it routes rate-card selection, aliases, package duration, contract-term templates, billing and invoice settings, thresholds, spend trackers, and subscriptions to their dedicated nested schemas. The enclosing OpenAPI `requestBody` does not declare `required: true`, so this page does not establish omitted-body runtime behavior.
- **Relative dates and aliases:** `components.schemas.RelativeDate` defines relative values and units; `RelativeScheduleDurationInput`, `RelativeSchedulePointInTimeInput`, and the template schemas show where offsets and durations are applied. `components.schemas.PackageAlias` contains the alias name and its effective start/end timestamps.
- **Restrictions:** the introductory `### Usage guidelines` section records the consistent-terms use case, billing-provider match condition, alias reassignment effect, supported relative-time granularities, and package immutability. Nested conditional restrictions remain with their referenced component schemas.
- **Success:** `paths` -> `/v1/packages/create` -> `post` -> `responses` -> `200` requires top-level `data`, which references `components.schemas.Id`; the example places the UUID at `data.id`.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-packages-and-aliases]]
- Supporting concept: [[metronome-customers-and-contracts]]
- Package guide: [[source-metronome-guides-implement-metronome-core-concepts-packages-overview]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/create-a-package-2026-08-28|Create a package]] — complete collected documentation and embedded OpenAPI operation
