---
title: "Braintree Payment Orchestration Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/orchestration/overview"
raw_files:
  - "braintree/docs/guides/orchestration/overview-2026-09-16.md"
tags: [braintree, paypal-orchestration, payment-processing, processor-connections, transaction-routing]
---

## Overview

This collected Braintree overview defines PayPal Payment Orchestration as a layer through which merchants can connect to multiple payment service providers (PSPs), acquirers and value-added services by using a single integration to route and manage transactions. It says merchants can retain their existing Braintree integration without changing client-side tokenization or SDK code.

The page was collected on 2026-09-16. It is a Braintree-hosted product overview, not independent authority for the listed destination providers and not proof of current connector availability or merchant eligibility, successful payment execution, settlement or funding.

## Key takeaways

- The documented identity is a Braintree-facing orchestration layer for connecting multiple PSPs, acquirers and value-added services through one integration. The page describes authorization performance, redundancy, geographical expansion and ecosystem-management benefits, but those product statements are not guarantees for a particular merchant, transaction, market or connector.
- Merchants can use an existing Braintree integration without client-side tokenization or SDK-code changes. Connector activation is through the merchant's Braintree account; the page directs merchants to an AM or TAM to identify connectors appropriate for their markets, with a separate onboarding-support route when no dedicated AM or TAM is available.
- All transaction operations named by the overview—authorization, capture, void and refund—must go through Braintree. The page warns that calling a connector directly causes reconciliation errors and synchronization issues.
- The connector section is a snapshot inventory and navigation route. Its provider descriptions and brief capability notes do not replace the connector-specific guides or independent destination-provider authority; use those sources for market, instrument, 3DS, token, refund, dispute and lifecycle qualifications.

> [!warning] Keep orchestration operations on Braintree
> For the documented orchestration route, perform authorization, capture, void and refund through Braintree. Do not call the connector directly for those operations.

> [!warning] Do not infer Forward API behavior
> This overview defines Payment Orchestration and its Braintree-owned transaction-operation boundary. It does not state that Orchestration uses [[braintree-forward-api]], and it does not import Forward API eligibility, request-transformation, security or destination-example constraints.

> [!warning] Preserve snapshot and destination boundaries
> The available connectors and their summarized capabilities are statements in this 2026-09-16 Braintree snapshot. They do not establish current availability, account or market eligibility, enablement, successful execution, settlement, funding or destination-wide behavior.

## Detail locators

- Orchestration identity, single-integration purpose and existing-Braintree client-side continuity: introduction below `# Payment Orchestration Overview`, raw lines 14-18.
- Claimed scale, authorization, local-network, redundancy, recovery and lock-in benefits: benefit list, raw lines 20-28.
- Mandatory Braintree route for authorization, capture, void and refund, plus direct-connector reconciliation and synchronization warning: important notice, raw line 30.
- Snapshot connector inventory, destination summaries, capability notes and connector-guide routes: `## Available connectors`, raw lines 33-75.
- AM/TAM connector-selection route and alternate onboarding contact: `## Next steps`, raw lines 78-82.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-orchestration]]
- Distinct outbound request-construction route: [[braintree-forward-api]]

## Raw Sources

- [[raw/braintree/docs/guides/orchestration/overview-2026-09-16|Braintree Payment Orchestration overview]] - complete collected overview covering product identity, claimed benefits, the Braintree-owned transaction-operation boundary, connector navigation and onboarding route
