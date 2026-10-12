---
title: "Adyen Webhooks"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/webhooks"
raw_files:
  - "adyen/docs/development-resources/webhooks/2026-09-15.md"
tags: [adyen, webhooks, asynchronous-events, state-management]
---

## Overview

This Adyen documentation overview introduces webhooks as event-driven HTTP POST messages from an Adyen service to a merchant-defined endpoint. It explains their role in asynchronous processing, internal resource-state updates, and automatic notification of external events, then routes configuration, security, handling, event-type, and troubleshooting details to dedicated documentation.

## Key takeaways

- A receiver needs to accept a webhook with a `2xx` HTTP status, store the message, and process its contents.
- A configured webhook subscription avoids continuous API polling and supports processes whose resource status can change seconds, minutes, hours, or days later.
- For asynchronous payment flows, the page uses iDEAL as an example where completion confirmation can take time; it says a webhook can carry the final outcome when available. Its separate authorized-payment-to-paid-order example illustrates a possible merchant backend action, not proof that any payment completed or that every authorization is final.
- Webhook messages can contain a resource snapshot for updating merchant-held state. The page qualifies its connected-resource example to Adyen for Platforms account holders, balance accounts, capabilities, and balances.
- For events not caused directly by a merchant API request, the page identifies webhooks as the automatic notification path. Its examples remain product- and flow-qualified: Adyen for Platforms onboarding verification, shopper-initiated chargebacks, report availability, and Adyen Issuing relayed authorisation.

> [!warning] Evidence boundary
> This unversioned documentation snapshot is an overview and navigation source. It does not establish event-specific payloads, delivery ordering or retries, security mechanics, account eligibility, successful endpoint operation, successful payment execution, or GitHub/SDK implementation behavior; use the dedicated linked documentation and applicable product authority for those claims.

## Detail locators

- Webhook identity and receiver actions: `# Webhooks`, paragraph beginning "A webhook is a lightweight mechanism".
- Subscription, polling, and long-running-process purpose: `# Webhooks`, paragraphs beginning "When you configure a subscription" and "Webhooks are great".
- Payment-flow qualification and illustrative backend action: `### Handling asynchronous flows`.
- Resource-snapshot state management and Adyen for Platforms example: `### State management`.
- External-event scope and product-qualified examples: `### Reacting to external events`.
- Dedicated configuration, security, handling, event-type, and troubleshooting routes: `## Next steps`.

## Related

- Company: [[adyen]]
- Concept: [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/development-resources/webhooks/configure-and-manage/2026-09-15|Configure and manage webhooks]]
- [[raw/adyen/docs/development-resources/webhooks/secure-webhooks/2026-09-15|Secure your webhooks]]
- [[raw/adyen/docs/development-resources/webhooks/handle-webhook-events/2026-09-15|Handle webhook events]]
- [[raw/adyen/docs/development-resources/webhooks/webhook-types/2026-09-15|Webhook structure and types]]
- [[raw/adyen/docs/development-resources/webhooks/troubleshoot/2026-09-15|Troubleshoot webhooks]]

## Raw Sources

- [[raw/adyen/docs/development-resources/webhooks/2026-09-15|Adyen webhooks overview]] — complete collected overview of purpose, receiver actions, asynchronous flows, resource-state updates, external-event examples, and next-step routes
