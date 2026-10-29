---
title: "Online banking Poland Android Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/android-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/android-component/2026-09-15.md"
tags: [adyen, online-banking-poland, android, component, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Poland to an existing Android Components integration** using Sessions or Advanced server-side flow. It covers required shopper email, the `OnlineBankingPLComponent`, redirect action, and test/live setup. A redirect action is not proof of completed payment. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-online-banking-poland]] for Przelewy24 branding and the PL/PLN capability matrix.

## Key takeaways

- **Sessions flow** requires an existing Android Components Sessions integration, Checkout API **v68 or later**, redirect handling, and Online banking Poland added in Customer Area (raw lines 25–36). Its `/sessions` addition is required `shopperEmail`, with a **50-character maximum** (raw lines 38–46). The curl example uses a test endpoint, PL/PLN and an Android-style return URL; these are sample values (raw lines 48–69).
- Android module examples add `com.adyen.checkout:onlinebankingpl:YOUR_VERSION`; Compose also adds `components-compose`. The guide uses `OnlineBankingPLComponent` and `PaymentMethodTypes.ONLINE_BANKING_PL` to launch either Compose or non-Compose UI (raw lines 270–291, 315–368). The optional `setSubmitButtonVisible` defaults to **true**; setting false hides the submit button (raw lines 293–313). The shown configuration block has an unlabeled nested brace and placeholder `value`, so it is not a complete runnable Kotlin sample.
- **Advanced flow** requires an existing Android Components Advanced integration, handling `action.type: redirect`, and Customer Area setup (raw lines 376–384). It repeats the module/UI and optional submit-button setup, sourcing the payment-method object from `/paymentMethods` in the examples (raw lines 386–486). The Advanced requirements table specifies **no Checkout API minimum**, so do not import the Sessions v68 minimum as an Advanced requirement from this page.
- Advanced `/payments` requires `shopperEmail` (maximum 50 characters). It lists `paymentMethod.issuer` as the selected bank's issuer ID **without a required mark** (raw lines 488–497). Examples send `type: onlineBanking_PL`, `issuer: 141`, PLN and a return URL; those are sample values, not an exhaustive issuer list or proof that issuer is mandatory for every request (raw lines 499–523, 653–686).
- The Advanced response includes `action.type: redirect`; its JSON example has `resultCode: RedirectShopper` and a GET redirect URL (raw lines 831–845). Check test payment status in test Customer Area **Payments > Payment list**; live acceptance requires a method request in live Customer Area (raw lines 370–374, 847–851). Neither redirect presentation nor test status lookup establishes successful live payment.

> [!warning] Illustrative sample syntax
> The Sessions and Advanced curl examples omit a shell continuation after `-X POST` before `-d` (raw lines 53–69, 503–523). Some SDK snippets refer to undeclared request/config objects, and the Kotlin configuration blocks contain an unlabeled nested brace (raw lines 73–169, 252–268, 303–313, 419–429). Consult the actual SDK/base integration contract rather than copying these fragments as complete code.

## Detail locators

- Sessions prerequisites, email field and sample request: raw `## Sessions flow Component`, lines 25–69.
- Sessions SDK snippets, Android module, configuration and launch: raw lines 71–368.
- Sessions test/live gate: raw lines 370–374.
- Advanced prerequisites and Component setup: raw `## Advanced flow Component`, lines 376–486.
- Advanced email/issuer fields, examples and redirect response: raw lines 488–845.
- Advanced test/live gate: raw lines 847–851.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-poland]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/android-component/2026-09-15|Online banking Poland Android Component, captured 2026-09-15]]
