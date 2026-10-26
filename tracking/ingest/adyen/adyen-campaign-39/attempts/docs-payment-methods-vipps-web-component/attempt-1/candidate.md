---
title: "Adyen Vipps Web Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/web-component"
raw_files:
  - "adyen/docs/payment-methods/vipps/web-component/2026-09-15.md"
tags: [adyen, vipps, web, components, online-payments]
---

## Overview

Adyen's 2026-09-15 Vipps Web Component page describes additions to an existing Web Components integration for Sessions and Advanced server-side flows. It delegates general integration steps to the main flow guides. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For Sessions, the page calls for an existing Web Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and Vipps added in Customer Area. It lists `shopperStatement` (falling back to `reference` for the Vipps app description) and `amount.value` in minor units; it states a Vipps minimum of 100 minor units, or 1.00 NOK. The table's Required cells are blank, so this page alone does not establish those fields as additional mandatory properties. It says no Vipps-specific Component configuration is needed.
- For Advanced, the page calls for an existing Web Components Advanced integration, redirect handling, and Vipps added in Customer Area. Its `/payments` table lists entries with blank Required cells for `paymentMethod.telephoneNumber` to prefill the Vipps-hosted page, `shopperStatement` with the same fallback, `channel` (for example Web, iOS, Android), and `amount.value` with the same 100 minor-unit minimum. The example uses NOK, `type: vipps`, and `channel: Web`; the response example is `RedirectShopper` with `action.type: redirect`, an intermediate action rather than authorization or settlement evidence.
- Both flows import `Vipps` from `@adyen/adyen-web` and initialize its Component with a checkout instance. The page's Sessions example uses Checkout API v71 and its Advanced example v72; these examples do not replace the explicit Sessions v68-or-later minimum. The Sessions example's app-scheme `returnUrl` and `countryCode: NO` are example values, not stated universal Web requirements or a full country-eligibility rule.
- For TEST-environment Vipps testing, the page sends the merchant to the Vipps test app, then instructs them to add Vipps to a test merchant account, create a Vipps payment request, and have the shopper check the app notification and authorize. For live payments it requires a separate request in live Customer Area, then describes low-amount payments and checking the server's `AUTHORISATION` webhook and payment list for status. The app authorization step and redirect response do not by themselves prove an Adyen authorization outcome.

## Detail locators

- Sessions requirements, `/sessions` parameter table and v71 example: raw lines 25-68.
- Sessions import, Component initialization and configuration: raw lines 70-102.
- Sessions test-app setup, test flow, live request and status checks: raw lines 104-130.
- Advanced requirements, import and initialization: raw lines 132-168.
- Advanced `/payments` parameter table, v72 example and redirect response: raw lines 170-222.
- Repeated Advanced TEST/live setup and status checks: raw lines 224-250.

## Related

- [[adyen-webhooks]] — status-event context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/web-component/2026-09-15|Vipps Web Component (2026-09-15 snapshot)]]
