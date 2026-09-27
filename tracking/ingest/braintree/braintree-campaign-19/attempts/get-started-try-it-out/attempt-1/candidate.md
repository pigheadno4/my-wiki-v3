---
title: "Braintree Try It Out: Sandbox and Production Boundaries"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/try-it-out"
raw_files:
  - "braintree/articles/get-started/try-it-out-2026-09-16.md"
tags: [braintree, sandbox, production, testing, control-panel]
---

## Overview

This collected Braintree article recommends testing early and often and introduces the Sandbox as a test environment that is almost identical to Production. Its retrieval value is the boundary between simulated Sandbox activity and live Production behavior: it identifies important environment differences, country-qualified Sandbox behavior, non-transfer of data and settings, and separate credentials.

The page links to detailed users-and-roles, testing-values, gateway-credentials and production-integration guides. Those links are navigation routes, not authority from this page for the linked procedures or their current support.

## Key takeaways

- Within Sandbox, the page says users and roles can be created, transactions can be run with test credit-card numbers, and the gateway can be explored with Sandbox testing values through the Sandbox Control Panel or API. The linked pages own the detailed values and procedures.
- Sandbox and Production are not interchangeable. The comparison table distinguishes test payment methods from real ones, test-value-triggered processor responses and webhooks from bank responses and actual gateway events, Sandbox's lack of dedicated hardware from Production's dedicated resources, and broader Sandbox purge/delete capabilities from Production's manual-deletion and no-transaction-deletion boundary. It also documents account-qualified Production settings and disputes.
- Sandbox cannot withstand high transaction volumes. Sandbox location defaults from the country used to access the Braintree homepage unless changed before signup, and Sandbox processing options, currencies and features can vary by country.
- A Sandbox account is not linked to a Production account: created objects, processing options and recurring-billing settings do not transfer, and login information, merchant ID and API keys differ. The final section only links developers to a separate production-integration guide when they are ready to accept real payments; this page does not supply the go-live procedure.

> [!warning] Simulation is not Production proof
> The page calls Sandbox "almost identical" to Production while documenting material differences. Sandbox transactions, test values, webhooks, dispute simulations, settings and currency tests do not establish live-payment acceptance, Production configuration, bank processing, event delivery or current product eligibility. The 2026-09-16 collection date also does not establish current behavior.

## Detail locators

- Recommendation to test early and often: `# Try It Out`, line 16.
- Sandbox purpose, Control Panel/API use and linked testing routes: `## The Braintree sandbox`, lines 19-23.
- Login, payment-method, processor-response, capacity, deletion, webhook, processing-option, dispute, location and recurring-billing contrasts: `## Sandbox versus production`, comparison table, lines 26-41.
- Country default and country-qualified Sandbox options, currencies and features: `## Sandbox versus production`, line 43.
- Non-linkage, non-transfer and separate credentials: `## Sandbox versus production > IMPORTANT`, lines 46-47.
- Sandbox currency-test setup: `## Testing currencies`, lines 52-69.
- Simulation-versus-Production dispute qualification: closing paragraph under `## Testing currencies`, line 71.
- Production integration is delegated to a linked guide: `## Switching from sandbox to production`, lines 74-76.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree managing users and roles article]] - unread navigation-only destination linked for user and role procedures; not used as factual evidence here
- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Braintree important gateway credentials article]] - unread navigation-only destination linked for merchant-ID and API-key details; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/get-started/try-it-out-2026-09-16|Braintree Try It Out article]] - complete collected article covering Sandbox purpose, Sandbox-versus-Production distinctions, environment isolation, currency testing and the separate production-integration route
