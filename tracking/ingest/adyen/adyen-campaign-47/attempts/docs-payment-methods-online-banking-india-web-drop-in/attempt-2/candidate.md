---
title: "Adyen Online Banking India Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-india/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-india/web-drop-in/2026-09-15.md"
tags: [adyen, online-banking-india, web, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds Online Banking India to an existing Web Drop-in integration, with separate Sessions and Advanced flow instructions. Its Advanced example uses method type `onlinebanking_IN`, INR and an issuer value. It does not establish current issuer availability, merchant eligibility, payment success or live operation. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow:** Requires an existing Web Sessions Drop-in integration, Checkout API v68 or later, redirect handling for `action.type=redirect`, and Online Banking India added in Customer Area. The page says no method-specific parameters are needed in `/sessions`, and no additional Online Banking India configuration is needed in Drop-in (pinned raw lines 23–58).
- **Advanced flow:** Requires an existing Web Advanced Drop-in integration, redirect handling and Online Banking India in Customer Area. The `/payments` table marks `paymentMethod.issuer` (shopper-selected issuing bank) and `browserInfo` required. Its example includes `paymentMethod.type=onlinebanking_IN`, INR, issuer CBI, returnUrl and browser details; these examples do not establish the current bank list (lines 68–128).
- The optional tree-shaking prose says to include `OnlineBankingIN` when importing individual payment methods, but the displayed import line is inconsistent and syntactically invalid; see warning below (lines 42–52). The guide provides no additional method-specific Drop-in configuration in either flow (lines 54–58, 80–84).
- For testing Netbanking in India, it points to the MyStore demo and selecting India. Before live Online Banking India acceptance, it says to submit a request in the live Customer Area (lines 60–66, 519–525). A demo route does not prove this merchant's integration or live status.
- **Method-level gate from the separate [[source-adyen-docs-payment-methods-online-banking-india|Online Banking India overview]]:** processing requires compliance with regulations in India, a local entity, and a local integration in India; the overview directs merchants to their account manager or Support for details (overview pinned raw line 25). These requirements are from the overview, not this Web Drop-in child guide. Child-guide Customer Area setup alone does not establish current eligibility.

> [!warning] Optional import and Advanced base link
> The optional import text names `OnlineBankingIN`, but the code line reads `import { AdyenCheckout, Dropin, Online Banking India } from '@adyen/adyen-web';` (raw lines 46–51), which is not valid JavaScript named-import syntax. The Advanced integration requirement URL contains an unresolved encoded `{{getParameter('platform')}}` template despite Web wording (line 76). Follow the appropriate Web base guide and verified package exports rather than copying those lines as a working recipe.

## Detail locators

- Sessions requirements, no-extra-parameters, optional import and configuration: pinned raw lines 23–58.
- Sessions test/live setup: lines 60–66.
- Advanced requirements, fields and request examples: lines 68–517.
- Advanced test/live setup: lines 519–525.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-online-banking-india]] — method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-india/web-drop-in/2026-09-15|Online Banking India Web Drop-in guide, captured 2026-09-15]]
