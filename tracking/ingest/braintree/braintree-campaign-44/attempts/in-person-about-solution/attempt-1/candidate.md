---
title: "Braintree In-Person Solution Architecture"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/about/solution"
raw_files:
  - "braintree/in-person/about/solution-2026-09-16.md"
tags: [braintree, in-person, architecture, card-reader]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree|Braintree]] webpage is a solution-architecture overview for [[braintree-in-person]]. It describes cloud-based reader configurations that avoid direct communication between POS hardware and the reader, illustrates several POS-to-reader topologies, and presents Braintree's intended payment-method abstraction and omnichannel relationship.

## Key takeaways

- The page says any device capable of a web-based API call can initialize and create a transaction on the reader; removing direct POS-hardware-to-reader communication is presented as enabling platform-independent integrated POS configurations.
- Its topology examples include a dedicated reader for each POS, multiple fixed or mobile POS devices sharing a reader, and multiple readers connected through a single POS design. These are architecture examples, not prescribed or proven deployments.
- Braintree states that In-Person aims to provide one integration across in-store and online channels, with a consistent interaction flow through `PaymentMethod` and `Transaction` objects. The page further says future payment methods can be rolled out through the Braintree Control Panel without changing the POS integration.
- The page positions the In-Person reader solution as one channel of a broader enterprise offering and points to Braintree card-not-present and Vault solutions for cross-channel capabilities.

## Scope

This snapshot is an unversioned product architecture overview: it is not exact API-schema or SDK/version authority, does not establish current product, merchant-account, hardware, payment-method, or environment availability, and does not prove that a described configuration was deployed or that any transaction was authorized, captured, settled, or funded.

## Detail locators

- `# Solution Architecture` (raw lines 14-16) — page identity and cloud-based reader-configuration purpose.
- `## In-Store Reader Configurations` (raw lines 19-21) — web-API initiation and the direct POS-to-reader communication boundary.
- `### Traditional Fixed POS 1:1 Configuration Example` through `### Dual-lane Checkout Example` (raw lines 24-38) — dedicated, shared-reader, mobile-POS, and many-readers-to-one-POS examples.
- `## Payment Method Abstraction` (raw lines 39-43) — unified integration goal, shared object flow, and the stated Control Panel rollout model.
- `## Omnichannel Capabilities` (raw lines 48-50) — In-Person's relationship to Braintree card-not-present and Vault offerings.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]
- Adjacent architecture route: [[source-braintree-in-person-about-technical-overview|Braintree In-Person Technical Overview]]

## Raw Sources

- [[raw/braintree/in-person/about/solution-2026-09-16|Braintree In-Person Solution Architecture (fetched 2026-09-16)]]
