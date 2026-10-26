---
title: "Bizum Web Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bizum/web-component"
raw_files:
  - "adyen/docs/payment-methods/bizum/web-component/2026-09-15.md"
tags: [adyen, bizum, web-components, redirect, online-payments]
---

## Overview

This 2026-09-15 Bizum guide adds the method to an existing Adyen Web Components integration, with separate Sessions and Advanced server-side instructions. It covers redirect setup, request additions, Component import/initialization, and test fixtures; it does not demonstrate a completed live payment or current merchant eligibility. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and flow:** both branches require an existing Web Components integration for their respective server-side flow, redirect handling with `action.type: redirect`, Bizum activation to obtain MID and Terminal ID, and adding Bizum in Customer Area. The Sessions branch alone explicitly states Checkout API v68 or later. (raw lines 23–38, 379–388)
- **Sessions:** add a unique alphanumeric `reference` of 4–125 characters to `/sessions`; import `Redirect` from `@adyen/adyen-web` and initialize the Bizum redirect Component. The page says no Bizum-specific configuration parameters are needed. Its test-environment `/sessions` examples use EUR, countryCode ES, and a custom-scheme return URL; example values do not establish general eligibility or a required return URL form. (raw lines 39–69, 334–362)
- **Advanced:** import and initialize the same `Redirect` Component; add the described unique `reference` to `/payments`. The test `/payments` examples set `paymentMethod.type` to `bizum` and show a web return URL. The documented response has a redirect action; its `RedirectShopper` JSON is an example of an intermediate handoff, not final authorization or settlement. (raw lines 390–445, 738–757)
- **Example and test limits:** both JavaScript initialization snippets render `type:bizum` as an unquoted identifier, so they should not be treated as copy-ready code without checking the SDK syntax. Test guidance names telephone number `700 000 000` and describes authorization for amounts less than 10 and refusal for amounts more than 15, without stating a unit or behavior for the interval. Check test payment status in the test Customer Area; the guide does not document a final webhook sequence. (raw lines 360–361, 367–377, 410–411, 759–772)

## Detail locators

- Sessions prerequisites, `reference` table and request example: raw lines 29–69. The table's rendered regular expression contains a trailing `)`; consult the linked Checkout API reference before relying on that expression.
- Sessions `Redirect` import, no added configuration, initialization: raw lines 334–362.
- Advanced prerequisites, `Redirect` import/initialization and `/payments` reference: raw lines 379–445.
- Advanced redirect response example: raw lines 738–757; test fixtures: raw lines 759–772.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bizum/web-component/2026-09-15|Bizum Web Component guide, 2026-09-15 snapshot]]
