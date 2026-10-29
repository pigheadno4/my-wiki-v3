---
title: "Adyen Online banking Slovakia Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/web-drop-in/2026-09-15.md"
tags: [adyen, online-banking-slovakia, web, drop-in, redirect, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds Online banking Slovakia to an existing Web Drop-in integration. It separates Sessions and Advanced server-side flows, redirect handling, the Advanced issuer field, and test/live setup. It is a method-specific supplement to [[adyen-online-payments]], not a complete base integration or proof of payment execution. [[adyen]]

## Key takeaways

- **Sessions flow:** Start with an existing Web Drop-in Sessions integration using Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and the method added in Customer Area. The page says there are no extra method-specific `/sessions` parameters or Drop-in configuration. It describes importing `OnlineBankingSK` individually as optional tree shaking, not a required import. [Raw: lines 23–59]
- **Advanced flow:** Start with an existing Web Drop-in Advanced integration that handles `action.type: redirect` and has the method added in Customer Area. The method-specific `/payments` table requires `paymentMethod.issuer`, the bank selected by the shopper; the examples use `paymentMethod.type: onlineBanking_SK`, issuer `cs`, EUR amount 1000 minor units and an HTTPS `returnUrl`. Those are sample values, not a list of all issuers or a successful result. This page states no Advanced Checkout API minimum or final redirect outcome. [Raw: lines 73–129]
- **Broken import and navigation examples:** Both optional-import snippets show `import { AdyenCheckout, Dropin, Online banking Slovakia } from '@adyen/adyen-web';` despite prose naming `OnlineBankingSK`; the spaced text is not a valid JavaScript named import. The Advanced integration requirement URL contains an unresolved encoded template in its `platform` query, while other Advanced links name Web. Treat those lines as captured documentation defects rather than a copy-ready import or a different platform requirement. [Raw: lines 46–51, 78, 86–91]
- **Server sample scope:** The page provides test-environment curl and Java v27.0.0, PHP v19.0.0, .NET v17.0.0, Node v18.0.0, Go v10.4.0, Python v12.5.1 and Ruby v9.5.1 request examples. They repeatedly say live use also needs `liveEndpointUrlPrefix`; the Go snippet labels v10.4.0 but imports `.../v9/src/...`, an unresolved version/import mismatch. These examples do not show an executed payment. [Raw: lines 112–420]
- **Test/live:** The guide says to test with real payment details and small amounts, check test payment status in test Customer Area, and add Online banking Slovakia in Customer Area for live acceptance. This is captured provider guidance, not evidence that an account is enabled or a payment was made. [Raw: lines 62–69, 424–430]

> [!WARNING] Do not copy the optional import snippet literally
> The prose says `OnlineBankingSK`, but the JavaScript snippets use the spaced words `Online banking Slovakia` inside a named import (raw lines 46–51, 86–91). Resolve the import against the actual Adyen Web package/version before implementation; the page's example is internally inconsistent.

## Detail locators

- Sessions prerequisites, no-extra-parameter/configuration statements and import: pinned raw lines 23–59.
- Advanced prerequisites, import and required issuer: pinned raw lines 73–108.
- Test request and language-library examples, including Go mismatch: pinned raw lines 112–420.
- Test/live guidance: pinned raw lines 62–69 and 424–430.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-online-banking-slovakia]] — approved method overview for SK/EUR redirect journey and method-level capabilities, separate from this Web guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/web-drop-in/2026-09-15|Online banking Slovakia Web Drop-in guide, captured 2026-09-15]]
