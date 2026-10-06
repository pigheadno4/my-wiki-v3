---
title: "Braintree In-Person Technical Overview"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/about/technical-overview"
raw_files:
  - "braintree/in-person/about/technical-overview-2026-09-16.md"
tags: [braintree, in-person, graphql, card-reader, architecture]
---

## Overview

This collected, unversioned [[braintree|Braintree]] website page is a high-level architecture and capability overview for Braintree In-Person. It describes In-Person as additional Braintree GraphQL objects and mutations and outlines an application-mediated flow from a merchant to physical locations, paired readers, charge-request contexts, status polling, and a returned transaction object after reader interaction. It is not an exact-version GraphQL schema, SDK or GitHub implementation record, current hardware or account-eligibility statement, merchant deployment design, reader-online proof, or evidence that a payment was authorized, captured, settled, funded, or otherwise succeeded.

## Key takeaways

- The page places the API caller in the merchant's role: the caller creates `InStoreLocation` objects representing physical locations that contain readers and retains each generated location ID for later changes. It then pairs one or more `InStoreReader` objects to a location and retains the generated reader ID for reader initialization. These are described relationships and responsibilities, not proof that a particular merchant, location, or reader has been created or paired.
- A charge request creates an `InStoreContext` by supplying the checkout total and target reader ID. The application retains the returned context ID and checks context status on an interval while the customer interacts with the reader; the page says a `Transaction` object is returned when that interaction finishes. A context ID, polling response, customer completion, or returned object must not be treated by this overview alone as proof of authorization, capture, settlement, funding, or success.
- The hardware section says Verifone manufactures the terminal hardware while Braintree develops most of the device functionality and software. Its captured table labels P400, E285, and M400 as available and describes Ethernet/WiFi and power characteristics, but that table is snapshot documentation, not current model availability, provisioning, network reachability, firmware, security posture, or merchant compatibility evidence.
- The page states that Sandbox and Production readers behave the same but are not interchangeable: special test cards work on Sandbox readers, and test cards do not work on Production readers. This environment boundary is consequential; Sandbox setup or test-card behavior cannot establish Production reader readiness or a live payment result.
- The functionality table routes to separate guides for sale, authorization, refunds, vaulting, line-item display, custom prompts, non-PCI gift/PLCC magstripe-data collection, PayPal/Venmo QR payments, and offline processing. These are high-level capability labels with linked navigation, not exact-schema, SDK-parity, enablement, eligibility, security-compliance, lifecycle, or successful-execution guarantees; verify each linked guide and applicable account/environment conditions separately.

## Detail locators

- `## Intro to Braintree GraphQL` (raw lines 19-23) — GraphQL learning routes and the statement that In-Person adds GraphQL objects and mutations whose integration uses the detailed Braintree GraphQL guides.
- `## Understanding the In-Person GraphQL Object Relationships` (raw lines 26-34) — merchant/caller responsibility, location creation, reader pairing, retained generated IDs, context creation from amount and reader ID, interval status checks, customer interaction, and returned `Transaction` object.
- `## What Card Reader models are supported?` (raw lines 37-47) — Verifone/Braintree hardware-software responsibility statement; Sandbox-versus-Production interchangeability and test-card warning; and the snapshot P400, E285, and M400 power/network table.
- `## High-Level Functionality Summary` (raw lines 50-61) — capability labels, short descriptions, and links to the separate sale, authorization, refund, vaulting, display, prompt, card-data, QR-payment, and offline-processing guides.
- Final navigation (raw line 63) — separate Solution Architecture and Solution Coverage pages; linked navigation only, not evidence used for this entry.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- Braintree GraphQL guides and the Merchant, InStoreLocation, InStoreReader, InStoreContext, Transaction, `createInStoreLocation`, `pairInStoreReader`, and `requestChargeFromInStoreReader` references — linked navigation only; their current schemas, required fields, errors, permissions, and runtime behavior were not read as evidence for this entry.
- The linked setup, ready-for-launch, hardware FAQ, hardware-model, transaction, refund, vaulting, display, custom-prompt, card-data, QR-payment, offline-processing, Solution Architecture, and Solution Coverage pages — navigation only unless represented by a separately reviewed source page.

## Raw Sources

- [[raw/braintree/in-person/about/technical-overview-2026-09-16|Braintree In-Person Technical Overview (fetched 2026-09-16)]]
