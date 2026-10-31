---
title: "Adyen Forward API webhook v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Forward-API-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/Forward-API-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, webhooks, forward-api, payment-requests]
---

## Overview

This 2026-09-15 API Explorer snapshot identifies the Forward API webhook family as v1. The Forward API sends payment requests to third-party services on the merchant's behalf, and Adyen uses webhooks to notify the merchant about their result. The overview lists one `POST forwardApi.notification` event route, summarized as “Forward API request completed.”

## Key takeaways

- This is a catalog and purpose statement. The overview does not define the `forwardApi.notification` payload, event type value, resource or request reference, required or conditional field, example, response body, acknowledgement code, decision state, or failure outcome. Use the child event reference for those details.
- “Request completed” is the endpoint summary; the overview does not say a third-party service accepted the request, an authorization succeeded, funds were captured or settled, or a payment reached final state.
- The captured `latest` path is labeled v1 here. The 2026-09-15 snapshot does not establish current version, delivery order, retries, deduplication, or signature-verification behavior.

## Detail locators

- **Title and purpose, raw lines 5–9** — Forward API webhook v1, third-party payment-request forwarding, and Adyen result notifications.
- **Endpoints → General, raw lines 11–16** — single listed `POST forwardApi.notification` route and “Forward API request completed” summary.

## Related

- [[adyen]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/api-explorer/Forward-API-webhooks/latest/post/forwardApi.notification/2026-09-15|forwardApi.notification event reference]] — linked for navigation; its payload and response were not read for this overview entry.

## Raw Sources

- [[raw/adyen/api-explorer/Forward-API-webhooks/latest/overview/2026-09-15|Adyen API Explorer — Forward API webhooks v1 overview (2026-09-15)]]
