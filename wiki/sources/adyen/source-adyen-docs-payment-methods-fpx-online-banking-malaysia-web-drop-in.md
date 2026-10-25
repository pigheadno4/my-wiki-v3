---
title: "Adyen FPX Online Banking Malaysia Web Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/web-drop-in/2026-09-15.md"
tags: [adyen, fpx, online-banking-malaysia, web, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen guide gives FPX Online Banking Malaysia additions to an existing Web Drop-in integration, separately for Sessions and Advanced flow. It covers redirect prerequisites, optional individual Web import and test/live steps; the main integration guides own the rest of the payment flow. This snapshot does not prove current issuer or merchant availability, or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and FPX Online Banking Malaysia added in Customer Area. It specifies no extra FPX fields for the base `/sessions` request. Advanced requires an existing Web Drop-in Advanced integration, redirect handling and Customer Area setup; it specifies no extra method fields for the base `/payments` request. The page states the v68+ prerequisite in its Sessions section only.
- For either flow, `MolPayEBankingMY` may be imported individually from `@adyen/adyen-web` to support tree shaking. The import is optional and is not a method-specific Web SDK minimum.
- The Advanced integration-type hyperlink contains an encoded, unresolved `{{getParameter('platform')}}` value, while its redirect link explicitly targets Advanced Web Drop-in. Use the explicit Advanced requirement and resolved flow-specific guidance; the templated URL does not establish another platform or flow.
- For testing, the page says to use an issuer ID available for the Online banking Malaysia Component in the respective country/region and inspect test-payment status in the Adyen test Customer Area. It provides no issuer-ID list or currency in this child guide. Live acceptance requires a separate request in the live Customer Area. Redirect setup, issuer selection and request submission do not prove authorization, capture or settlement; this page has no method-specific final-outcome procedure.

## Detail locators

- Sessions requirements and base `/sessions` statement: pinned raw lines 25–42.
- Sessions optional import and test/live steps: pinned raw lines 44–64.
- Advanced requirements, including templated prerequisite URL and redirect handling: pinned raw lines 66–76.
- Advanced optional import, base `/payments` statement and test/live steps: pinned raw lines 78–104.

## Related

- [[adyen-online-payments]] — Web Drop-in, Sessions/Advanced and redirect boundaries
- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia]] — method overview with its own country, currency and outcome scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/web-drop-in/2026-09-15|FPX Online Banking Malaysia Web Drop-in guide, 2026-09-15]]
