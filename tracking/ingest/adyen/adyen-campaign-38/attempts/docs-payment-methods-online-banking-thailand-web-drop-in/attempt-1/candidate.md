---
title: "Adyen Online banking Thailand Web Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/web-drop-in/2026-09-15.md"
tags: [adyen, online-banking-thailand, web, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen guide describes method-specific additions for Online banking Thailand in existing Web Drop-in Sessions and Advanced integrations. It covers redirect prerequisites, optional Web import, Sessions issuer presentation and test/live steps. It does not prove current bank availability, merchant eligibility or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and method setup in Customer Area. The guide adds no Online banking Thailand fields to the base `/sessions` request. Advanced separately requires an existing Web Drop-in Advanced integration, redirect handling and Customer Area setup; the page adds no method-specific base `/payments` fields. The v68+ prerequisite appears under Sessions only.
- In either flow, `MolPayEBankingTH` can be imported individually from `@adyen/adyen-web` for tree-shaking; this import is optional. The Sessions section alone lists optional configuration: `issuer` to preselect a bank, `highlightedIssuers` to put banks first (added in Web v5.1.0), `showImage: false` to hide logos, and `placeholder` for dropdown text, overridden by custom translations. Its issuer-ID table lists Bangkok Bank, Krungsri Bank, Krung Thai Bank, Siam Commercial Bank and Kasikorn Bank. This table is a page snapshot, not a current bank-availability guarantee.
- The Sessions configuration sample is fenced as bash and calls `MolPayEBankingTH.Configuration()` with generic comments; treat it as illustrative rather than a verified executable Web snippet. The Advanced prerequisite hyperlink contains an encoded `{{getParameter('platform')}}` template instead of a resolved platform value; follow the explicit Advanced Web Drop-in requirement and the separately resolved redirect link, not that templated URL as proof of another flow.
- Testing uses an issuer ID available for the Component in the applicable country/region and checks status in the Adyen test Customer Area. Before live acceptance, the page requires a request in the live Customer Area. Redirect setup, issuer selection or test request does not establish authorization, capture or settlement; the page does not give a method-specific final-outcome procedure.

## Detail locators

- Sessions requirements, no-extra-fields `/sessions`, optional import: pinned raw lines 25–54.
- Sessions optional issuer display configuration, v5.1.0 qualification, example and issuer IDs: pinned raw lines 56–87.
- Sessions test/live instructions: pinned raw lines 89–97.
- Advanced requirements, templated prerequisite link, redirect handling, optional import and no-extra-fields `/payments`: pinned raw lines 99–127.
- Advanced test/live instructions: pinned raw lines 129–137.

## Related

- [[adyen-online-payments]] — Sessions, Advanced, Web Drop-in and redirect boundaries
- [[source-adyen-docs-payment-methods-online-banking-thailand]] — method overview, with its own regional and outcome scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/web-drop-in/2026-09-15|Online banking Thailand Web Drop-in guide, 2026-09-15]]
