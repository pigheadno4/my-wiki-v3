---
title: "Adyen Checkout Settings"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/checkout-settings"
raw_files:
  - "adyen/docs/online-payments/checkout-settings/2026-09-15.md"
tags: [adyen, online-payments, checkout-settings, payment-method-ordering, uplift]
---

## Overview

This Adyen guide describes Customer Area checkout settings for a merchant account: manually adding, removing, or ordering payment methods by shopper country or region; dynamically ordering methods toward a selected cost or conversion goal; linking a shopper across one checkout session; and reviewing checkout analytics. The settings require an online-payments integration using the Checkout API and either the Merchant admin or Change payment methods Customer Area role.

This is a documentation snapshot, not proof that Dynamic ordering is enabled for a merchant, that an integration meets Personalize requirements, or that a specific optimization outcome will occur.

## Key takeaways

- Manual Payment methods settings are configured per country or region and apply when the checkout session's shopper country code matches that configuration. Within one merchant account, manual and dynamic ordering are alternatives; enabling Dynamic ordering makes the manual order for that account stop applying.
- Dynamic ordering selects payment-method order using the chosen cost or conversion strategy plus current and historical transaction insights. It is available only when the integration meets the Personalize module requirements, does not work alongside manual ordering, and has limited impact when transaction-level `allowedPaymentMethods` or `blockedPaymentMethods` filters are used.
- Web Drop-in with the Sessions flow supports Dynamic ordering without additional configuration because `shopperConversionId` is included automatically. Other integration types must include that field. In the Advanced flow, generate one unique ID per checkout session, send the same ID in `/paymentMethods` and `/payments`, and do not regenerate it before checkout completion.
- The Tokenization checkout setting is marked for removal. In this guide it applies only to payment links created through the Customer Area, for which Adyen directs merchants to Pay by Link settings instead.
- Checkout analytics can be reviewed in **Analytics** > **Checkout analytics**, including overview, shopper insights, Dynamic ordering, completion-rate, and validation-error views.

## Detail locators

- `## Requirements` (raw lines 21–32) — Checkout API integration, recommended Web Drop-in v6+ Sessions route, required Customer Area roles, Personalize eligibility, and ordering/filter limitations.
- `## Checkout settings` and `## Payment methods` (raw lines 34–60) — merchant-account scope, manual-versus-dynamic choice, country/region configuration, shopper-country matching, experiments, and the effect of enabling Dynamic ordering.
- `## Dynamic ordering` (raw lines 62–83) — optimization inputs, dashboard/experiment routes, integration qualification, and Customer Area activation steps.
- `## Link a shopper to a checkout session` (raw lines 85–103) — session boundary, conversion tracking, automatic Sessions handling, and the Advanced-flow `shopperConversionId` lifecycle.
- `## Tokenization` (raw lines 105–109) — planned removal and Pay by Link replacement route.
- `## Checkout dashboard` (raw lines 111–127) — dashboard purpose, navigation, and available views.

## Related

- Company: [[adyen]]
- Concept: [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/checkout-settings/2026-09-15|Adyen checkout settings (2026-09-15 snapshot)]]
