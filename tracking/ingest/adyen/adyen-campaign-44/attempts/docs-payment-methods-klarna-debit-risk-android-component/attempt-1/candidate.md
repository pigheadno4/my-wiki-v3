---
title: "Adyen Klarna Debit Risk Android Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna-debit-risk/android-component"
raw_files:
  - "adyen/docs/payment-methods/klarna-debit-risk/android-component/2026-09-15.md"
tags: [adyen, klarna-debit-risk, android, components, sepa-direct-debit]
---

## Overview

This 2026-09-15 Adyen guide adds Klarna Debit Risk to an existing Android Components integration. It has separate Sessions and Advanced flow instructions for a redirect action, and a conditional recurring route that first stores SEPA details using a Klarna Debit Risk payment and then charges the token as SEPA Direct Debit. It is distinct from Klarna financing methods. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions needs an existing Android Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and Klarna Debit Risk added in Customer Area. Advanced needs an existing Android Components Advanced integration, handling for the additional redirect action, and the same method setup. The page says no ordinary extra `/sessions` or Advanced `/payments` parameters and no Klarna Debit Risk-specific component configuration.
- For either flow, import the Android `instant` module, adding `components-compose` when using Jetpack Compose. Create `InstantPaymentComponent` for method type `directEbanking`; Sessions obtains the method from `checkoutSession`, while Advanced selects it from the `/paymentMethods` response. Both flows show Compose and view-based mounts; the Compose key must vary when resetting the component or using a different screen/session.
- Recurring is through **SEPA Direct Debit**, not a repeat Klarna Debit Risk checkout. The guide recommends explicit shopper permission and clear schedule/amount disclosure because of SEPA chargeback risk. For token creation, its `/payments` field table marks `paymentMethod.type: directEbanking`, `returnUrl`, `countryCode`, `recurringProcessingModel`, `shopperInteraction`, `shopperReference`, and `storePaymentMethod` as required. It says the online shopper interaction is `Ecommerce`, shopper reference must be unique, at least three characters, case-sensitive and free of PII, and `storePaymentMethod` is true for initial storage. A `recurring.token.created` webhook supplies the `storedPaymentMethodId`.
- Use the stored token only for shopper-absent `Subscription` or `UnscheduledCardOnFile` payments. Those later examples send `paymentMethod.type: sepadirectdebit`, the stored ID, `shopperReference`, `shopperInteraction: ContAuth`, and the selected recurring model. The guide discourages SEPA `CardOnFile` due to chargeback risk, recommending shopper-present individual Klarna Debit Risk authorization instead.
- **Source example conflict:** both token-creation field tables mark `countryCode` required and describe online `shopperInteraction` as `Ecommerce`, but their shown token-creation requests omit `countryCode` and send `ContAuth`. The curl/Node/Ruby/Python examples also use string forms of `storePaymentMethod` while typed examples use booleans. Do not copy the sample as proof those discrepancies are accepted by the API; reconcile with the chosen Checkout API version and base tokenization guide.
- Test with Klarna sample data before live acceptance. The page separately says to enable Klarna Debit Risk on the live merchant account. TEST samples and a listed method do not prove live eligibility, authorization, settlement, or SEPA debit outcome.

## Detail locators

- Sessions requirements, no-extra-field claim, imports, `InstantPaymentComponent` and `directEbanking`: raw lines 25–127.
- Sessions recurring guidance, token field table and request examples: raw lines 128–510. Tokenized subscription and unscheduled examples: raw lines 511–1128.
- Advanced requirements, imports, mounting, no-extra-field claim: raw lines 1137–1237. Advanced recurring section repeats the field and sample tension: raw lines 1239–1621; token payment examples: raw lines 1622–2239.
- Test and live enablement: raw lines 1129–1135 and 2240–2246. Curl payment examples use Checkout API v72 TEST; individual library snippets identify their own versions.

## Related

- [[adyen-online-payments]] — provider integration context.
- [[adyen-tokenization]] — general token lifecycle context; this source supplies the method-specific route.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna-debit-risk/android-component/2026-09-15|Klarna Debit Risk Android Component, captured 2026-09-15]]
