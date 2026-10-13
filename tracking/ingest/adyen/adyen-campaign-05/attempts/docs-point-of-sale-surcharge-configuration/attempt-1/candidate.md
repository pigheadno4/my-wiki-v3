---
title: "Configuration-based POS surcharge | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/surcharge/configuration"
raw_files:
  - "adyen/docs/point-of-sale/surcharge/configuration/2026-09-15.md"
tags: [adyen, point-of-sale, surcharge, terminal-settings, management-api]
---

## Overview

This Adyen guide documents configuration-based surcharging for in-person payments: a merchant configures rules at company, merchant-account, store, or terminal level through Management API terminal settings, and an eligible payment terminal or Tap to Pay Mobile SDK calculates a surcharge from the presented card. It is distinct from the online API-only surcharge pilot and from per-payment dynamic surcharge. This 2026-09-15 webpage snapshot describes setup and behavior, not current legal permission, merchant enablement, or successful payment execution.

## Key takeaways

- Supported solution types in the page are Terminal API integrations with payment terminals or Tap to Pay Mobile solutions, plus standalone terminals. The page excludes SFO1 terminals and NYC1 mobile card readers. For payment terminals, the guide names software gates: v1.108 for maximum surcharge, v1.112 to distinguish commercial/consumer cards, v1.115 to exclude tips, and v1.117 for MOTO/MKE surcharging. These are feature gates in the snapshot, not proof of current firmware or account activation.
- Management API configuration requires an API credential/key with **Management API—Terminal settings read** and **Management API—Terminal settings read and write** roles. GET and PATCH `/terminalSettings` operate at company, merchant, store, or individual terminal scope. Live terminal-settings Management API calls have rate limits. Adyen recommends Standard webhooks carrying the surcharge amount in AUTHORISATION events; this guide's `TotalFeesAmount` payment-response field reports a surcharge amount, not a final settlement outcome.
- Rules select brand, currency, optional funding source, issuer country and commercial-card condition; `configurations` are ordered, and the first matching condition executes without checking later rules. A currency entry requires `currencyCode` and percentage and/or fixed amount; `amount` and `maxAmount` use minor units. The commercial-card check does not work on Mobile solutions or on payment terminals while internet is down, so rules relying on that distinction need particular care.
- Configuration can combine fixed amount and percentage, set a cap, and choose whether to exclude gratuities. The surcharge confirmation screen appears depending on configuration and solution; Mobile/Tap to Pay does not show it, and skipping it requires another form of disclosure under the guide. Tap to Pay surcharging needs Adyen Support to enable single tap; on mobile, only that single-tap flow is available. The page directs merchants to account for applicable compliance requirements; it does not establish current law or scheme permission for a proposed rule.
- Starting with terminal software v1.117, configured surcharge also applies to MOTO and MKE. If a merchant already surcharges those flows separately, this can charge twice; the guide offers an Adyen feature opt-out at company, merchant, store or terminal level through an Adyen account manager or technical contact. Confirm the existing setup before applying a configuration.

## Detail locators

- `Requirements` — integration and hardware scope, terminal software gates, credential roles, webhooks, live API rate limits, Tap to Pay display/single-tap conditions.
- `How it works` — ordinary payment request, card-based calculation, conditional customer confirmation or alternative disclosure, and response `TotalFeesAmount`.
- `Configure surcharges` — fee dimensions, fixed/percentage/cap and gratuity options, GET/PATCH scope, ordered first-match `configurations`, required brand/currency fields, minor-unit amounts, issuer country, and commercial-card offline/mobile limitation.
- `Opting out for MOTO and MKE` — v1.117 inclusion, double-surcharge risk and scope of opt-out.
- `If you need help` — Adyen Support route when the merchant cannot configure Management API directly.

## Related

- Company: [[adyen]]
- Concept: [[adyen-surcharging]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/surcharge/configuration/2026-09-15|2026-09-15 Adyen POS surcharge configuration guide]]
