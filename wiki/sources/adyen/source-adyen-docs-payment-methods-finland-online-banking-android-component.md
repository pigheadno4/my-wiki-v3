---
title: "Adyen Online banking Finland Android Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/android-component"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/android-component/2026-09-15.md"
tags: [adyen, finland-online-banking, android, components, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Finland** to an existing Android Components integration. It covers Sessions and Advanced redirect flows, required shopper email, `InstantPaymentComponent` setup, and Paytrail test guidance. It is a method-specific add-on, not a complete Android integration or evidence of current merchant enablement. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-finland-online-banking]] for the separate FI/EUR method overview.

## Key takeaways

- **Sessions:** start with an existing Android Components Sessions flow, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and Online banking Finland added in Customer Area. The `/sessions` addition marks `shopperEmail` required. The TEST v71 request uses FI/EUR and a custom-scheme `returnUrl`; its `s.hopper@@example.com` email is visibly malformed and must not be copied as a validated shopper address. See raw lines 25–69.
- For Sessions, import the `instant` Android module (plus `components-compose` when using Jetpack Compose), with no extra method configuration. The example selects `ebanking_FI` from the checkout session and creates `InstantPaymentComponent`; the Compose example uses a unique key per Component/screen/session reset. These are UI setup examples, not proof that a bank redirect completed. See raw lines 342–425.
- **Advanced:** start with an existing Android Components Advanced flow, handle the redirect action, and add the method in Customer Area. Import the same modules and initialize `InstantPaymentComponent` using an `ebanking_FI` method from the `/paymentMethods` response; no extra method configuration is specified. The v68 API minimum is stated only in the Sessions requirements table on this page. See raw lines 432–527.
- The Advanced `/payments` table marks `paymentMethod.type: ebanking_FI` and `shopperEmail` required. `paymentMethod.issuer` is not generally marked required, but its description explicitly says it is **required for the Issuer redirect flow**; `returnUrl` is unmarked and described as the post-payment return URL with maximum length 1024 characters. The TEST v72 payment examples omit `paymentMethod` despite the required type row and use an HTTPS `returnUrl` in an Android guide. Treat them as incomplete examples; obtain the actual selected method/issuer and app return handling from the appropriate base flow. The example response's `RedirectShopper`/`redirect` is an additional action, not final payment status. See raw lines 528–561 and 826–840.
- Before live acceptance, the guide says to test with Paytrail's test environment/sample data. It says **testing multiple partial refunds is currently not available**. The separate method overview's matrix marks multiple partial refunds available (and its refund check points to a missing note); keep this test-environment limitation distinct from the overview capability mark and do not infer that a test can verify it. See raw lines 426–430 and 842–846, plus [[source-adyen-docs-payment-methods-finland-online-banking]].

## Detail locators

- Sessions prerequisites, required email and TEST request examples: raw lines 25–340.
- Sessions module/Component setup and test note: raw lines 342–430.
- Advanced prerequisites and module/Component setup: raw lines 432–527.
- Advanced request-field table and abbreviated TEST examples: raw lines 528–824.
- Redirect response and repeated Paytrail test limitation: raw lines 826–846.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/android-component/2026-09-15|Fully read Online banking Finland Android Component raw]]
