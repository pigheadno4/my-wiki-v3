---
title: "Adyen Managed risk webhooks v1 overview"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/managed-risk-webhooks/latest/overview"
raw_files:
  - "adyen/api-explorer/managed-risk-webhooks/latest/overview/2026-09-15.md"
tags: [adyen, platforms, managed-risk, webhooks]
---

## Overview

This 2026-09-15 API Explorer snapshot catalogs Managed risk webhooks v1. Adyen says it sends these webhooks to customers using Adyen Managed Risk when it adjusts risk measures applied to their account holders' payouts based on risk level. The named measures are settlement delays, rolling reserves, and reserve waivers. This platform payout-risk family is distinct from payment fraud decisions and from a merchant account's reserve balance. [[adyen]] [[adyen-platforms]] [[adyen-webhooks]]

## Key takeaways

- The catalog lists eight POST event routes: `balancePlatform.managedRisk.balance.block.released`; `reserveWaiver.applied` and `.removed`; `rollingReserve.applied`, `.lifted`, and `.updated`; and `settlementDelay.lifted` and `.updated`, each with the shared `balancePlatform.managedRisk.` prefix.
- This overview supplies endpoint names and short summaries only. It does not give event payload schemas, resource IDs, receiver response requirements, timing, delivery behavior, or proof that a particular payout or funds movement occurred; consult each event's own reference for its contract.

## Detail locators

- Family purpose, customer scope and risk measures: raw lines 5–11.
- Eight POST event names and summaries: raw `## Endpoints` → `### General`, lines 13–25.

## Related

- [[adyen-platforms]] — modern platform and account-holder context.
- [[adyen-webhooks]] — general incoming webhook context.

## Raw Sources

- [[raw/adyen/api-explorer/managed-risk-webhooks/latest/overview/2026-09-15|Managed risk webhooks v1 overview (2026-09-15)]]
