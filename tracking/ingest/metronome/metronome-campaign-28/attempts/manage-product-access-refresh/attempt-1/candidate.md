---
title: "Metronome Manage Product Access"
type: source
date_ingested: 2026-08-29
original_format: webpage
canonical_url: "https://docs.metronome.com/guides/customers-billing/manage-customers/manage-product-access"
raw_files:
  - "metronome/guides/customers-billing/manage-customers/manage-product-access-2026-08-28.md"
  - "metronome/guides/customers-billing/manage-customers/manage-product-access-2026-07-13.md"
tags: [metronome, product-access, entitlements, contracts, notifications]
---

## Overview

This short Metronome navigation guide frames product access as a relationship among customer contracts, entitlement status, usage and payment signals, and entitlement-change notifications. It routes implementation questions to dedicated guides for provisioning, contract lifecycle transitions, trials, and notifications rather than defining those mechanisms itself.

## Query-critical facts

- Metronome says contract terms define customer access across packaging models and that entitlement status is tracked in real time based on usage and payment, with alerts for entitlement changes.
- Provisioning a customer and assigning a contract are presented as the basis for encoding entitlements in Metronome.
- Contract lifecycle management is the route for reflecting entitlement changes in renewal, upsell, and upgrade scenarios.
- Trials are presented as temporary-access models commonly used in product-led growth, while notifications are presented as communication about entitlement-state changes.

## Material boundaries

- This page is a navigation overview. It does not define entitlement fields, packaging configuration, status-evaluation mechanics or latency, contract-transition semantics, trial configuration, notification delivery, or error and recovery behavior. Follow the dedicated guides before implementation.
- The page does not establish that Metronome enforces access inside the merchant product. Its real-time wording has no latency, ordering, freshness, or consistency contract, and its alerting claim does not define notification transport or delivery guarantees.

## Raw-detail coverage map

Use the raw snapshot for the exact product-access framing; the customer-provisioning and contract-assignment route; renewal, upsell, and upgrade lifecycle examples; the PLG trial description; the notification route; all four documentation links; and the product-access illustration metadata. The linked dedicated guides remain the authority for their implementation details.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-alerts-and-notifications]], [[metronome-usage-based-billing]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]], [[source-metronome-guides-pricing-packaging-billing-model-guides-create-a-trial]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/manage-customers/manage-product-access-2026-08-28|2026-08-28 snapshot - product-access framing and navigation routes]]
- [[raw/metronome/guides/customers-billing/manage-customers/manage-product-access-2026-07-13|2026-07-13 snapshot - prior product-access navigation overview]]
