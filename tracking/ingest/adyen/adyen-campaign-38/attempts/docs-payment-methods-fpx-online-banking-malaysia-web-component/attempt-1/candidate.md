---
title: "Adyen FPX Online Banking Malaysia Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/web-component"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/web-component/2026-09-15.md"
tags: [adyen, fpx, malaysia, web, components, online-banking]
---

## Overview

This 2026-09-15 guide adds FPX Online Banking Malaysia to an **existing Web Components** integration. It gives separate Sessions and Advanced additions, including the `MolPayEBankingMY` import/Component and redirect handling. It is method-specific guidance rather than a complete main integration or evidence of a completed bank payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites:** Use an existing Sessions-flow Web Components integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and add the method in Customer Area. The page says no extra parameters are needed for the `/sessions` request. (raw lines 25–42)
- **Sessions Component:** Import and initialize `MolPayEBankingMY`. Optional configuration lists `issuer` to preselect a bank, `highlightedIssuers` to raise banks in the dropdown (added in Web v5.1.0), `showImage: false` to hide bank logos, and `placeholder` text overridden by custom translation configuration. The example uses `fpx_abb`; consult the full issuer-ID table, rather than treating the example as the only bank. (raw lines 44–107)
- **Advanced prerequisites and request:** The Advanced section requires an existing Advanced-flow Web Components integration, redirect handling and method addition in Customer Area. It also imports and initializes `MolPayEBankingMY`, and says no additional `/payments` parameters are needed. The Advanced requirements table does not state a Checkout API minimum; the v68 minimum appears in the Sessions table. (raw lines 127–169)
- **Testing versus live:** The page directs test payments with an available issuer ID and test status inspection in Customer Area. Before live acceptance, it says to submit a request in the live Customer Area. Neither instruction is proof of merchant approval, successful authorization or settlement. (raw lines 119–125, 171–177)

## Detail locators

- Sessions prerequisites, no extra session parameters and import: raw lines 25–54.
- Sessions optional Component configuration, example, bank issuer IDs and initialization: raw lines 56–117.
- Advanced prerequisites, import/initialization and no extra payment parameters: raw lines 127–169.
- Test and live-request instructions, repeated by flow: raw lines 119–125 and 171–177.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/web-component/2026-09-15|Adyen FPX Malaysia Web Component, 2026-09-15 snapshot]]
