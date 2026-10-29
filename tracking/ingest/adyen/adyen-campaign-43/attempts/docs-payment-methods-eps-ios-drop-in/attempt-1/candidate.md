---
title: "EPS iOS Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/eps/ios-drop-in/2026-09-15.md"
tags: [adyen, eps, ios, drop-in, redirect, sepa-direct-debit, tokenization]
---

## Overview

This 2026-09-15-captured guide gives the EPS-specific additions to an **existing iOS Drop-in** integration. It separates Sessions and Advanced server-side flows. It does not present a standalone checkout or final payment-result procedure, and its setup directions do not prove merchant approval or a completed payment (raw lines 15–25, 97–119).

## Key takeaways

- **Sessions flow:** The page requires an existing iOS Drop-in Sessions integration using **Checkout API v68 or later** and EPS added in Customer Area. It says there are no EPS-specific parameters to add when creating `/sessions` and no extra EPS Drop-in configuration. The Sessions requirement table does not separately spell out redirect handling; use the linked base integration guide for the host flow rather than importing the Advanced-specific checklist into this section (raw lines 25–46).
- **Advanced flow:** The page requires an existing iOS Drop-in Advanced integration, EPS added in Customer Area and existing handling for `action.type: redirect`. It says no EPS-specific Drop-in configuration or extra `/payments` parameters are needed. Unlike Sessions, this section does not state a Checkout API minimum (raw lines 97–119). Redirect handling is a prerequisite, not a final authorization or settlement result.
- Both sections say EPS recurring transactions run **through SEPA Direct Debit**. They strongly recommend explicit shopper permission and disclosure of payment schedule and charged amount to reduce chargeback risk. For the token path, the guide instructs a `/payments` request with `storePaymentMethod: true` and a shopper reference of at least three characters; **after settlement**, `recurring.token.created` supplies `storedPaymentMethodId`, and the server must accept token lifecycle events. Future `/payments` use the token and same shopper reference with `ContAuth` plus `Subscription` or `UnscheduledCardOnFile` (raw lines 48–87, 121–160). The Sessions section also names `/payments` for this recurring token step; do not silently rewrite it to `/sessions` (raw lines 57–66).
- Test EPS payment status can be checked in test Customer Area. Before accepting **live** EPS payments, submit an EPS request in live Customer Area. These are distinct test/live instructions and do not evidence a successful authorization, settlement, recurring charge or approved live account (raw lines 89–95, 162–168).

## Detail locators

- EPS iOS Drop-in scope and Sessions requirements/no-extra-settings: raw lines 15–46.
- Sessions SEPA recurring-token route: raw lines 48–87.
- Advanced requirements, redirect and no-extra-settings: raw lines 97–119.
- Advanced SEPA recurring-token route: raw lines 121–160.
- Test payment lookup and live EPS request: raw lines 89–95, 162–168.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-eps|EPS overview]]
- [[source-adyen-docs-payment-methods-sepa-direct-debit|SEPA Direct Debit overview]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/ios-drop-in/2026-09-15|EPS iOS Drop-in, fetched 2026-09-15]]
