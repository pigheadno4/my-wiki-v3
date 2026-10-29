---
title: "Adyen Online banking Poland Web Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/web-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/web-component/2026-09-15.md"
tags: [adyen, online-banking-poland, web, component, redirect, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds Online banking Poland to an existing Web Components integration. It separates Sessions and Advanced server-side flows, specifies method-specific email and issuer fields, imports/mounts `OnlineBankingPL`, and shows an Advanced redirect action. It is a supplement to [[adyen-online-payments]], not a complete return/finality recipe or evidence of payment success. [[adyen]]

## Key takeaways

- **Sessions prerequisites and request:** Start with an existing Web Components Sessions integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and Online banking Poland added in Customer Area. Its method-specific `/sessions` table requires `shopperEmail` of **50 characters or fewer**. The PLN amount 1000, PL country and app-scheme `returnUrl` shown in the sample are example values, not a Web return-URL prescription or current eligibility proof. [Raw: lines 25–68]
- **Sessions Component:** Import `OnlineBankingPL` from `@adyen/adyen-web`, initialize it with the checkout instance and mount it. The page says no additional Online banking Poland configuration parameters are needed in this Sessions flow. This is method-specific; the base integration still supplies checkout/session configuration. [Raw: lines 271–302]
- **Advanced prerequisites and request:** Start with an existing Web Components Advanced integration that handles `action.type: redirect` and has the method added in Customer Area. Import and mount `OnlineBankingPL`. The `/payments` table requires `shopperEmail` of **50 characters or fewer** but leaves `paymentMethod.issuer` unmarked as required, describing it as the selected bank's ID. Examples include `type: onlineBanking_PL`, issuer `141`, PLN amount and HTTPS `returnUrl`; these do not make issuer universally required or list all banks. This section states no Advanced Checkout API minimum. [Raw: lines 310–382]
- **Redirect and outcome boundary:** The sample Advanced response has `resultCode: RedirectShopper` and `action.type: redirect` with a GET `action.url`. This is an intermediate redirect, not an authorized payment. The page does not explain the returned `redirectResult`, `/payments/details`, or webhook finality; use the base integration or separately approved API-only guide for those steps, with attribution. [Raw: lines 689–705]
- **Sample and live caveats:** Both curl examples place `-X POST` on a line without continuation before `-d`; several Sessions language examples call `createCheckoutSessionRequest` without constructing it, and Node samples use `Config`/`EnvironmentEnum` without shown imports. Treat these as illustrations, not runnable commands. The page says to check test payments in test Customer Area and submit a request for Online banking Poland in live Customer Area before live acceptance. The library-version labels and `liveEndpointUrlPrefix` comments in examples are scoped to those samples, not a declared API minimum or completed live setup. [Raw: lines 50–268, 303–308, 363–689, 706–711]

> [!WARNING] Preserve field requiredness and redirect finality
> `shopperEmail` is required in both method-specific tables, but Advanced `paymentMethod.issuer` is unmarked (raw lines 46, 356–357). An example issuer does not override that table. `RedirectShopper` is not the final payment result (raw lines 691–704).

## Detail locators

- Sessions requirements, required email and sample session requests: pinned raw lines 25–268.
- Sessions import, no-extra-configuration and mount: pinned raw lines 271–302.
- Advanced requirements, import/mount and method-specific payment fields: pinned raw lines 310–357.
- Advanced examples and redirect action: pinned raw lines 359–705.
- Test/live gate: pinned raw lines 303–308 and 706–711.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-online-banking-poland]] — approved P24/PL/PLN method overview and redirect capability context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/web-component/2026-09-15|Online banking Poland Web Component guide, captured 2026-09-15]]
