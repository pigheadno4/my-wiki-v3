---
title: "Stripe Terminal: Configure Cellular Network"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/fleet/cellular"
raw_files:
  - "stripe-terminal-cellular-config-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, cellular, s710]
---

## Summary

The 2026-05-01 [[stripe]] Terminal guide describes remote fleet cellular configuration for the Stripe Reader S710. Locations default to cellular disabled. The 2026-11-07 base capture indexes the Dashboard and API variants.

## Key Details

**Location and reader activation in May**. Enable cellular at a Location, then register the S710 to that Location to activate it. The fleet guide describes cellular fallback when WiFi is unavailable. The April and November 2026 S700/S710 setup captures list the Android-managed order for a cellular-enabled S710 as Ethernet, then WiFi, then cellular.

**Dashboard in May**. From the location details or Manage locations page, edit **Cellular** under local or inherited configuration, select **Enabled**, acknowledge the billing impact, and select **Done** and **Apply changes**.

**API in May**. Create or update a Configuration object with `cellular: { enabled: true }` for the Location.

**Billing in May**. Stripe charges an additional monthly cellular fee for each reader whose cellular service was enabled at any time during that calendar month.

## Related

- [[stripe-terminal-hardware-orders]] — Terminal fleet configurations and reader registration
- [[stripe-terminal]] — Terminal reader hardware and network architecture
- [[source-stripe-terminal-setup-reader-s700-s710]] — S700/S710 setup and Ethernet, WiFi and cellular priority

## Raw Sources

- [[raw/stripe-terminal-cellular-config-2025|Stripe Terminal cellular configuration guide captured 2026-05-01]]

## Related raw API references

- [[raw/stripe-terminal-fleet-cellular-2026-11-07|Stripe Terminal cellular configuration Dashboard and API index captured 2026-11-07]]
