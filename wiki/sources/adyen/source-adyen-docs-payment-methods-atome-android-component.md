---
title: "Adyen Atome Android Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/android-component"
raw_files:
  - "adyen/docs/payment-methods/atome/android-component/2026-09-15.md"
tags: [adyen, atome, android, component, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds Atome to an existing Android Components integration using either Sessions or Advanced server-side flow. It gives Atome-specific additions and links to the main integration guides for shared steps. The page does not establish current account availability, a completed payment, or live enablement. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** Requires an existing Android Sessions Components integration, Checkout API v68 or later, redirect handling for `action.type=redirect`, and Atome added in Customer Area. The `/sessions` table marks shopper name, email, phone, billing address, line items and `countryCode` required; delivery address is optional when it is the same as billing. It specifies MY with MYR and SG with SGD (pinned raw lines 25–52).
- **Advanced flow:** Requires an existing Android Advanced Components integration, handling the additional redirect action, and Atome in Customer Area. Its `/payments` table marks `paymentMethod.type=atome`, the same shopper/contact/billing/line-item fields, and countryCode required, with the same MY/MYR and SG/SGD pairs; delivery address has the same conditional optionality (lines 846–957). The guide states Checkout API v68+ in the Sessions requirements, without repeating that requirement in the Advanced table.
- Both flows import `com.adyen.checkout:instant`; Jetpack Compose also imports `components-compose`. They use `InstantPaymentComponent` for Atome and say no Atome-specific configuration parameters are needed. Sessions gets the method from `checkoutSession.getPaymentMethod("atome")`; Advanced selects type `atome` from `/paymentMethods`. Compose examples use a unique Component key for a different screen or session (lines 732–813, 856–940).
- The guide describes partial refund by specifying `amount` in `/payments/{paymentPspReference}/refunds`. The test flow needs an Atome sandbox shopper account requested through an Adyen contact; use a different test account per country/region if testing multiple. It lists QR-code test apps for MY and SG. Live Atome setup requires contacting Support to add Atome in the live Customer Area (lines 816–844, 1688–1716).

> [!warning] Redirect is not final success
> The Advanced section calls its sample a “response for a successful payment,” but its actual `resultCode` is `RedirectShopper` with a redirect action (raw lines 1674–1685). That response directs the next shopper action and does not itself show final authorization or settlement. Use the linked main flow for subsequent result handling.

> [!warning] Sessions curl example
> The Sessions curl block repeats `countryCode` with the same SG value and places `-X POST` on a line before `-d` without a continuation (raw lines 55–78). Treat the table as the field requirements and the block as illustrative rather than a ready-to-run shell command.

## Detail locators

- Sessions requirements and required fields: pinned raw lines 25–52; example requests: lines 54–730.
- Sessions imports, launch and Atome configuration: lines 732–813; partial refund and test/live steps: lines 816–844.
- Advanced requirements, imports and Component launch: lines 846–940; required `/payments` fields and language examples: lines 942–1672.
- Advanced redirect response, partial refund and test/live steps: lines 1674–1716.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-atome]] — Atome method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/android-component/2026-09-15|Atome Android Component guide, captured 2026-09-15]]
