---
title: "Metronome Amend a Contract API"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/amend-a-contract"
raw_files:
  - "metronome/api-reference/contracts/amend-a-contract-2026-07-13.md"
tags: [metronome, api, contracts, amendments, commits, pricing-overrides]
---

## Overview
This API reference documents the bearer-authenticated `POST /v1/contracts/amend` operation and its nested amendment schema. Metronome marks amendments for replacement by Contract editing: new clients are directed to `editContract`, and this endpoint will become unavailable after Contract editing is enabled.

## Key takeaways
- The request requires UUIDs for `customer_id` and `contract_id` plus `starting_at`, whose date-time is the inclusive start of the amendment.
- An amendment can carry commits, credits, pricing overrides, scheduled charges, contract custom fields, and configuration-gated discounts, professional services, reseller royalties, and commercial-system fields.
- Nested objects impose conditional requirements and selector exclusions: schedules distinguish inclusive starts from exclusive ends, commit and credit applicability specifiers cannot be combined with their direct product selectors, and override type determines its required rate, multiplier, priority, or tiers.
- A successful response contains `data.id`; the example repeats the submitted contract ID, but the schema does not independently define the identifier's semantics. The endpoint also documents a `400` message error and a shared `404` not-found error.

## Amendment scope and lifecycle
At the top level, `starting_at` is the only documented amendment timing control and is inclusive. The page does not define whether omitted optional fields preserve existing values, whether submitted arrays append to or replace existing collections, how backdated amendments interact with invoice state, or whether the mutation is atomic across its nested collections. Those behaviors should not be inferred from this schema.

Several top-level fields are explicitly dependent on the client's configuration, including NetSuite and Salesforce identifiers, total contract value, discounts, professional services, and reseller royalties. The schema exposes these fields but does not define the configurations that enable them.

## Commits and credits
A commit requires `type` and `product_id`; accepted type spellings cover prepaid and postpaid variants. Its `access_schedule` description calls that schedule required, although `access_schedule` is not included in the OpenAPI object's `required` array. For postpaid commits, the description permits one access item, requires its amount to match the invoice-schedule total, and says the true-up invoice schedule also has one item. For prepaid commits, an omitted invoice schedule produces a complimentary commit with no invoice. The legacy `amount` field is deprecated in favor of access and invoice schedules.

Commit and credit rollover fractions must be between zero and one, and lower numeric priorities apply first. If direct product IDs, product tags, or specifiers are absent, a commit applies to all products; credit descriptions state the analogous all-product default for absent IDs and tags. Specifiers use any-match semantics across the list and cannot be combined with direct product-ID or tag selectors. Commits can provide a temporary ID for commit-specific overrides, hierarchy child-access configuration, and configuration-gated spend-tracker attributes that are immutable after creation.

## Overrides and rate validation
Each override requires an inclusive RFC 3339 `starting_at`; optional `ending_before` is exclusive. Supported override types are overwrite, multiplier, and tiered. Overwrites take precedence over multiplier and tiered overrides. A multiplier must be nonnegative; an overwrite needs `overwrite_rate`; a tiered override needs at least one tier and a positive priority. Under the documented EXPLICIT scheme, overwrites are first and tiered and multiplier overrides then use lowest-priority-value-first ordering.

An override can target a product ID or product tags, or use `override_specifiers`, but these selector forms cannot be combined. Commit-specific overrides default `is_commit_specific` to false; when enabled, specifiers can identify commits or recurring commits, and `target` defaults to `LIST_RATE`. The rate schema constrains flat prices to nonnegative values and percentage prices to the zero-to-one range. A configured minimum is limited to percentage or tiered-percentage rates and prevents commit-specific overrides from applying to that rate or applied override. Some rate types and exclusion fields are client- or feature-gated.

## Schedules and other nested objects
Duration schedules require `schedule_items`; each item requires an amount, an inclusive start, and an exclusive end. Point-in-time schedules say callers must provide either `schedule_items` or `recurring_schedule`. A point item requires a timestamp and accepts either `amount` or the `unit_price` and `quantity` pair. Recurring schedules require inclusive start, exclusive end, frequency, and amount distribution, and describe the same amount-versus-unit-price-and-quantity choice. The OpenAPI `required` arrays do not encode every one of those prose-level either/or rules, so implementations need to retain the documented conditional validation rather than relying only on required-field lists.

Discounts and scheduled charges require a product and point-in-time schedule. Professional services require product, unit price, quantity, and maximum term amount; unit price is multiplied by quantity. Reseller royalties require a reseller type and describe a requirement for at least one product-ID or product-tag selector. Setting their nullable `ending_before` to null removes an existing end timestamp, and provider-specific nested options cover AWS and GCP identifiers.

## Documented boundaries
The page lists HTTP `200`, `400`, and `404` responses but does not document conflict, idempotency, retry, concurrency, finalized-invoice, or partial-failure behavior for amendments. It also does not reconcile prose-level conditional requirements with every OpenAPI `required` array. Because the endpoint is being retired, new integrations should follow the linked Contract editing migration guidance rather than treating this legacy mutation schema as the current lifecycle authority.

## Related
- Companies: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-products-and-rate-cards]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-contracts-get-contract-edit-history]], [[source-metronome-api-reference-credits-and-commits-edit-a-commit]]

## Raw Sources
- [[raw/metronome/api-reference/contracts/amend-a-contract-2026-07-13|2026-07-13 snapshot — legacy contract amendment endpoint and nested mutation schema]]
