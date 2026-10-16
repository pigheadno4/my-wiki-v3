---
title: "Adyen partner Uplift enablement"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/partners/uplift-enablement"
raw_files:
  - "adyen/docs/partners/uplift-enablement/2026-09-15.md"
tags: [adyen, partners, uplift, checkout, risk, tokenization]
---

## Overview

This Adyen partner guide explains integration features and choices that let a partner's merchant customers use Uplift across five modules: Protect, Tokenize, Authenticate, Optimize, and Personalize. It assigns implementation work to the partner, Customer Area choices to merchants, and some routing or evaluation to Adyen. Enablement guidance and vendor performance descriptions do not establish a particular merchant's eligibility, configured entitlement, conversion lift, cost reduction, payment authorization, or settlement. [[adyen]] [[adyen-partners]] [[adyen-uplift]]

## Key takeaways

- General prerequisites include webhook processing, application information in all payment requests, and at least `shopperEmail`. The page recommends Web Drop-in or Components v6 with Sessions or Advanced flow and Checkout API v71 or later; Web API-only v71+ with encrypted or raw card data is supported with additional requirements. The linked Uplift requirements own the full required/recommended field list. Protect's later how-to calls for four fields at minimum, so do not flatten its module-specific data guidance into the general `shopperEmail` floor.
- **Protect** asks partners to support risk profiles, dispute handling, fraud data collection, quality fields, and optionally premium case-management review. The partner chooses whether risk settings are merchant-configurable or fixed, and whether dispute webhooks are processed centrally. Premium manual review and risk-based authentication have separate conditions; the guide's fraud and authorization benefit statements are goals, not measured outcomes.
- **Tokenize** requires tokenization request fields `shopperReference`, `storePaymentMethod`, `recurringProcessingModel`, and `shopperInteraction`. Network Tokenization is optional and needs Adyen-side configuration through a partner manager. Real Time Account Updater is optional and paid; it sends no webhooks, so partners read update information from the payment response when enabled. The guide does not equate enabling a token feature with shopper consent or a successful subsequent charge.
- **Authenticate** calls for native or redirect 3D Secure 2 (or both), handling the `threeDS2` action, and `browserInfo` for Advanced flow. Native versus redirect is a partner implementation choice. The page describes Dynamic 3DS2 with the 3DS2 implementation and premium Protect risk-based authentication as conditionally automatic; it does not prove an authentication or liability outcome for a transaction.
- **Optimize** separates optional Enhanced Scheme Data for qualifying US domestic card payments, Intelligent Payment Routing, Smart Payment Messaging, Auto Rescue, and method support. Enhanced data needs outcome webhooks; co-badged support has a Web v6.16.0 minimum and v6.18.1 recommendation. Routing is off by default, needs at least two routes, and merchants enable it in Customer Area; the US/Australia optimization setting has options. Auto Rescue is enabled per transaction or merchant account and requires processing retry-outcome webhooks. ERPS is opt-in, in maintenance mode, and can hurt authorization rates. None of these settings guarantees a lower fee or recovered payment.
- **Personalize** describes Sessions-flow automatic behavior; Advanced flow needs `shopperConversionId` on both `/payments` and `/paymentMethods` and the returned payment-method order preserved. Merchants manage checkout experiments in Customer Area. Dynamic ordering and experiment availability are product features, not proof of a merchant's conversion improvement.

## Detail locators

- Opening, `## Requirements`, and `## How it works`, lines 19–51: partner/merchant roles, five-module scope, integration recommendations and API-only conditions, webhook/application/shopper fields.
- `## Protect`, lines 53–75: risk/dispute/data roles, premium review and four-field module how-to.
- `## Tokenize`, lines 77–92: required token fields, Adyen network-token configuration, paid RTAU and response-not-webhook update path.
- `## Authenticate`, lines 94–111: 3DS2 modes, additional action, Advanced browser info, conditional premium authentication.
- `## Optimize`, lines 113–134: US enhanced-data outcome, co-badged version floor, routing/merchant choice, Auto Rescue webhooks and ERPS warning.
- `## Personalize`, lines 136–152: Sessions/Advanced split, shopper conversion identifier, ordering and Customer Area experiments.

## Related

- [[adyen-partners]] — broader partner integration route, pending campaign promotion.
- [[adyen-uplift]] — the five-module product concept.
- [[adyen-risk-management]] and [[adyen-tokenization]] — individual module domains.

## Raw Sources

- [[raw/adyen/docs/partners/uplift-enablement/2026-09-15|Adyen partner Uplift enablement, fetched 2026-09-15]]
