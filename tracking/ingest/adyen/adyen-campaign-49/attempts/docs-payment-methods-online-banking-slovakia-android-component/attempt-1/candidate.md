---
title: "Adyen Online banking Slovakia Android Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/android-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/android-component/2026-09-15.md"
tags: [adyen, online-banking-slovakia, android, component, redirect, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds Online banking Slovakia to an existing Android Components integration, with separate Sessions and Advanced server-side flows. It covers the bank-selection Component, redirect handling, the Advanced issuer field, and test/live setup. It is a method-specific supplement to [[adyen-online-payments]], not a complete base integration or evidence of payment success. [[adyen]]

## Key takeaways

- **Sessions prerequisites and request:** Start with an existing Android Components Sessions flow, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and Online banking Slovakia added in Customer Area. The page says no extra method-specific `/sessions` parameters are needed. Import `onlineBankingSKComponent`; add `components-compose` if using Jetpack Compose. The optional `setSubmitButtonVisible` configuration controls button visibility. [Raw: lines 23–84]
- **Sessions Component:** Use `OnlineBankingSKComponent` with `PaymentMethodTypes.ONLINE_BANKING_SK` from the checkout session. The Compose example supplies a unique component key for each screen/payment session or reset, whereas the non-Compose example attaches the Component to a view. Those are distinct UI patterns, not server-side request fields. [Raw: lines 86–139]
- **Advanced prerequisites and Component:** Start with an existing Android Components Advanced flow that handles redirect and has the method added in Customer Area. Its Checkout API row literally reads “v or later” with no number; do not infer an Advanced minimum from that row or carry over the Sessions v68 minimum. The Advanced Component examples select `ONLINE_BANKING_SK` from the `/paymentMethods` response, with Compose/non-Compose variants and the same optional submit-button setting. [Raw: lines 151–260]
- **Advanced server request:** The method-specific `/payments` table marks `paymentMethod.issuer` required as the issuing bank selected by the shopper. The examples use `paymentMethod.type: onlineBanking_SK`, `issuer: cs`, EUR 1000 minor units and an HTTPS `returnUrl`; these are examples, not proof that `cs` is the only issuer or that every EUR request succeeds. The page does not provide a final result sequence beyond the redirect prerequisite. [Raw: lines 263–295]
- **Example and environment caveats:** The request samples cover curl and Java v27.0.0, PHP v19.0.0, .NET v17.0.0, Node v18.0.0, Go v10.4.0, Python v12.5.1 and Ruby v9.5.1. The Go sample labels its library v10.4.0 but imports `.../v9/src/...`; treat the version/import mismatch as an unresolved sample conflict. The examples target test and say live use additionally needs `liveEndpointUrlPrefix`. They are illustrations, not executed calls. [Raw: lines 275–584]
- **Test/live:** The guide says to test with real payment details and small amounts, check test-payment status in test Customer Area, and add the method in Customer Area to accept live payments. This is provider guidance, not an instruction here to conduct payments or a claim that a live account is enabled. [Raw: lines 142–148, 585–591]

> [!WARNING] Incomplete Advanced version row
> The Advanced requirements table says “Checkout API v or later” (raw line 157) without a version number. Only the Sessions table clearly states v68 or later (raw line 32). Verify the applicable base guide/API contract before relying on an Advanced version threshold.

## Detail locators

- Sessions requirements, module/configuration and Component variants: pinned raw lines 23–139.
- Advanced requirements, module/configuration and Component variants: pinned raw lines 151–260.
- Required issuer and sample request/library variants: pinned raw lines 263–584.
- Test/live instructions: pinned raw lines 142–148 and 585–591.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-online-banking-slovakia]] — approved overview for SK/EUR redirect journey and method-level capabilities, distinct from this Android guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/android-component/2026-09-15|Online banking Slovakia Android Component guide, captured 2026-09-15]]
