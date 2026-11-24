---
title: "Stripe Terminal: Configurations Overview"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-configurations-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, locations, splash-screen, tipping]
---

## Summary

The Terminal Configuration object controls reader settings (splash screen, tipping, offline mode, etc.) in a two-level hierarchy: account-level (default) and location-level (override). Changes propagate within 10 minutes.

## Key Details

**Hierarchy**: account-level default → location-level override. Locations inherit the account default unless overridden. The account default cannot be applied directly to a location.

**Zone-level configurations**: private preview.

**Propagation time**: up to 10 minutes for changes to reach readers.

**API**:
- Retrieve account default: `configurations.list({ is_account_default: true })`
- Create config: `configurations.create({ bbpos_wisepos_e: { splashscreen: 'file_...' } })`
- Assign to location: `locations.update(locationId, { configuration_overrides: 'tmc_...' })`
- Update: `configurations.update(configId, { ... })`
- Delete: `configurations.del(configId)` — location reverts to account default within 10 min

**Dashboard**: manage via Manage locations page; create/edit/delete per location or account default.

## Raw Sources

- [[stripe-terminal-configurations-2025]] — verbatim webpage content (Dashboard flows + Node.js API samples)
