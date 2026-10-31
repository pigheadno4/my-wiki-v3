---
title: "Adyen Authorization webhooks v4 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/relayed-authorisation-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/relayed-authorisation-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, issuing, webhooks, authorisation]
---

## Overview

This 2026-09-15 snapshot is the Adyen Authorization webhooks v4 overview. It says Adyen sends webhooks about transaction authorization events and lists one general POST endpoint, `balancePlatform.authorisation.relayed`, summarized as “Relayed authorization requested.” The overview is a catalog route, not the detailed relayed request/response contract.

## Key takeaways

- The listed endpoint signals a relayed authorization request. The overview does not define its request payload, payment-instrument or transaction identifiers, response body, decision values, response deadline, fallback outcome, or the effect of an HTTP acknowledgement. Consult the endpoint reference for those rules before implementing a decision flow.
- The page does not state delivery order, retries, deduplication, signatures, capture, settlement, or bank receipt. Its `latest` URL is a captured snapshot label; the page heading names version v4.

## Detail locators

- Product/family heading and purpose: raw lines 5–7. Endpoint catalog and route summary: raw lines 9–14.

## Related

- [[adyen]] — provider overview.
- [[adyen-issuing]] — Issuing authorization context.
- [[adyen-webhooks]] — webhook family context.

## Related raw API references

- `balancePlatform.authorisation.relayed` endpoint reference — route named by this overview; payload and decision contract require a separate read.

## Raw Sources

- [[raw/adyen/api-explorer/relayed-authorisation-webhooks/latest/overview/2026-09-15|Authorization webhooks v4 overview (2026-09-15)]]
