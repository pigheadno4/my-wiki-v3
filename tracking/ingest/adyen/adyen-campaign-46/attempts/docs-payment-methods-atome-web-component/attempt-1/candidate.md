---
title: "Adyen Atome Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/web-component"
raw_files:
  - "adyen/docs/payment-methods/atome/web-component/2026-09-15.md"
tags: [adyen, atome, web, components, redirect, online-payments]
---

## Overview

This captured [[adyen]] guide adds Atome to an existing Web Components integration. It separates Sessions flow and Advanced flow, specifies the Atome shopper and order data, initializes the `Atome` Component, and points to redirect, refund, and test/live steps. It is method-specific guidance alongside the main [[adyen-online-payments]] integration guides, not a standalone checkout recipe.

## Key takeaways

- **Flows and prerequisites:** Sessions requires an existing Sessions Web Components integration, Checkout API v68 or later, redirect handling (`action.type: redirect`), and Atome added in Customer Area. Advanced requires an existing Advanced Web Components integration, redirect handling, and the same method setup. Both import `Atome` from `@adyen/adyen-web` and instantiate `new Atome(checkout, ...).mount(...)` (raw lines 23–36, 734–741, 808–821, 854–889).
- **Request data and geography:** For Sessions `/sessions` and Advanced `/payments`, the tables mark shopper name, email, phone, billing address, line items, and country code required; Advanced additionally marks `paymentMethod.type: atome` required. `deliveryAddress` has an unmarked Required cell and is described as optional when billing and delivery addresses match. The stated country/currency pairs are Malaysia/MYR and Singapore/SGD. The examples use Singapore/SGD and a 1000-minor-unit total made from one 400 unit line and two 300 unit lines; examples do not establish a merchant's live eligibility (raw lines 40–52, 894–907; examples 54–112 and 909–976).
- **Component fields:** Sessions allows prefilling personal and billing details through `data`. The page says Atome forces `deliveryAddress` and `companyDetails` hidden in the Component; its table shows personal and billing fields editable and bank account hidden. That display rule is separate from the server request fields (raw lines 746–804).
- **Redirect, result, and refunds:** The Advanced example response is labeled successful but has `resultCode: RedirectShopper` and a redirect `action`; that is a redirect instruction, not evidence of a completed or authorised payment. Both flow requirements defer redirect handling to the main guide. For partial refunds, the guide says to supply the refund `amount` to `/payments/{paymentPspReference}/refunds`; its “Refunds and cancellations” heading supplies no separate cancellation procedure (raw lines 34–35, 826–832, 860–861, 1624–1646).
- **Test and live gates:** Testing requires an Atome sandbox shopper account requested through an Adyen contact, with separate accounts for multiple countries/regions. The guide lists QR test apps for MY and SG, Customer Area test status, and contacting Support to add Atome in the live Customer Area (raw lines 834–852, 1648–1666). This captured page does not demonstrate a real payment or live enablement.
- **Example caveats:** The Sessions curl sample has `-X POST` without a trailing line continuation before `-d`, a duplicate `countryCode` key, and an app custom-scheme `returnUrl` despite this being a Web guide. The Advanced curl sample also lacks the continuation before `-d`. The Sessions configuration-object snippet omits a closing brace. Treat those snippets as illustrative, not copy-ready (raw lines 58–78, 794–806, 913–919).

## Detail locators

- Page identity and Sessions requirements/request fields: pinned raw lines 15–52.
- Sessions request examples: pinned raw lines 54–731; import, configuration, refunds and test/live: lines 734–852.
- Advanced requirements/import/initialization/request table: pinned raw lines 854–907; request examples: lines 909–1622.
- Advanced redirect-action response, partial refund and test/live: pinned raw lines 1624–1666.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-atome]] — captured Atome method overview; this page gives the Web Component integration details.

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/web-component/2026-09-15|Atome Web Component, captured 2026-09-15]]
