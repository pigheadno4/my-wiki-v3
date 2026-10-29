---
title: "Adyen Online banking Finland Web Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/web-component"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/web-component/2026-09-15.md"
tags: [adyen, finland-online-banking, web, components, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Finland** to an existing Web Components integration. It describes Sessions and Advanced redirect flows, required shopper email, the `Redirect` Component, and Paytrail test guidance. It is a method-specific add-on, not a full Web integration or evidence of live merchant enablement. See [[adyen]], [[adyen-online-payments]], and the separate method overview [[source-adyen-docs-payment-methods-finland-online-banking]].

## Key takeaways

- **Sessions:** use an existing Web Components Sessions flow with Checkout API v68 or later, redirect handling for `action.type: redirect`, and Online banking Finland added in Customer Area. The `/sessions` addition marks `shopperEmail` required. The TEST v71 sample uses FI/EUR but shows an app-scheme `returnUrl` in this Web guide, malformed `s.hopper@@example.com`, and a curl command without a continuation after `-X POST`. Treat those values as illustrative, not a working Web request. See raw lines 25–69.
- Import `Redirect` from `@adyen/adyen-web`; no extra method configuration is specified. The Sessions example mounts `new Redirect(checkout, { type:ebanking_FI })`, with `ebanking_FI` unquoted in the displayed JavaScript. Use the applicable base integration to determine a valid method type/configuration rather than copying this snippet literally. See raw lines 342–370.
- **Advanced:** use an existing Web Components Advanced flow with redirect handling and method setup in Customer Area. Import and mount `Redirect` again; the same unquoted `type:ebanking_FI` appears. The v68 API minimum is stated in this page's Sessions requirements, not its Advanced requirements. See raw lines 378–410.
- The Advanced `/payments` table marks `paymentMethod.type: ebanking_FI` and `shopperEmail` required. It says `paymentMethod.issuer` is relevant and required **for the Issuer redirect flow**; `returnUrl` is described as the post-payment URL, maximum 1024 characters, but is not marked required in this table. The TEST v72 examples omit `paymentMethod` despite that required type row, repeat the malformed email, and the curl example lacks a continuation after `-X POST`. The sample response returns `RedirectShopper` with a `redirect` action, which is a redirect step rather than final payment confirmation. See raw lines 412–445 and 710–724.
- Before live acceptance, the guide directs testing with Paytrail's test environment and sample data. It says **testing multiple partial refunds is currently not available**. The separate method overview marks multiple partial refunds available in its capability matrix while its refund note is absent in the captured raw; retain this test limitation and capability tension rather than treating the matrix as a successful test. See raw lines 372–376 and 726–730, plus [[source-adyen-docs-payment-methods-finland-online-banking]].

## Detail locators

- Sessions prerequisites, email field and multilingual TEST request examples: raw lines 25–340.
- Sessions `Redirect` import, setup and Paytrail test note: raw lines 342–376.
- Advanced prerequisites, `Redirect` setup and request table: raw lines 378–423.
- Advanced TEST request examples and redirect response: raw lines 425–724.
- Repeated Paytrail test limitation: raw lines 726–730.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/web-component/2026-09-15|Fully read Online banking Finland Web Component raw]]
