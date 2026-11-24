---
title: "Stripe Terminal: Manage Locations and Zones"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-locations-and-zones-2025.md"
tags: [stripe, stripe-terminal, locations, zones, fleet, connect, connection-token]
---

## Summary

Locations group readers by physical site and apply the correct regional configuration. Zones optionally provide hierarchical grouping of locations. Locations are required before any reader can accept payments.

## Key Details

**Locations**: required for all readers; group readers by physical site; address requirements vary by country (4 tiers). Cannot change a location's country after creation — create a new location and re-register readers.

**Address requirement tiers**:
- AU, CA, IT, JP, ES, US: `line1`, `city`, `state`, `postal_code`, `country`
- Most of EU + MY, NZ, NO: `line1`, `city`, `postal_code`, `country`
- BG, HR, CY, IE, MT, SG, SI: `line1`, `postal_code`, `country`
- GI: `line1`, `country`

**Zones**: optional hierarchical grouping; multiple locations per zone; nested zones supported; location can only belong to one zone. Zones cannot be created/modified via API — Dashboard only.

**Connection token scoping**: pass `location` to `connectionTokens.create` to restrict the token to smart readers at that location only. Has no effect on Bluetooth readers.

**Connect patterns**:
- Direct charges: create Location under connected account using `Stripe-Account` header
- Destination charges: Locations belong to platform; store connected account reference in Location `metadata`

## Raw Sources

- [[stripe-terminal-locations-and-zones-2025]] — verbatim webpage content (Dashboard flows + Node.js API samples)
