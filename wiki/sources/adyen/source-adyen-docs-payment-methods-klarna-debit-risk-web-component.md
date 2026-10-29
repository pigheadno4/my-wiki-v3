---
title: "Adyen Klarna Debit Risk Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna-debit-risk/web-component"
raw_files:
  - "adyen/docs/payment-methods/klarna-debit-risk/web-component/2026-09-15.md"
tags: [adyen, klarna-debit-risk, web-components, redirect, sepa-direct-debit, recurring]
---

## Overview

This 2026-09-15 Adyen Docs page adds Klarna Debit Risk to an existing Web Components Sessions or Advanced integration. The one-time method uses a redirect Component; its recurring path first stores details during a Debit Risk payment and then processes token payments as **SEPA Direct Debit**, a distinct payment method. This guide supplies add-on steps, not the complete base integration or proof of merchant enablement or payment outcome. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Web Components Sessions flow, Checkout API v68+, redirect handling (`action.type: redirect`) and Klarna Debit Risk added in Customer Area. Advanced requires its corresponding Web Components flow, redirect handling and Customer Area setup. The guide adds no ordinary `/sessions` or `/payments` request parameters and no Debit Risk configuration parameters; import `Redirect` and initialize its Component for `directEbanking`. The printed JavaScript uses unquoted `directEbanking` in the `type` property, although API examples use the string `"directEbanking"`; verify the value before copying the snippet.
- Recurring uses SEPA Direct Debit rather than a recurring Klarna Debit Risk payment. The guide strongly recommends explicit shopper permission and transparency about schedule and amount to reduce chargebacks. For the initial `/payments` token request, its table calls for `paymentMethod.type: directEbanking`, `returnUrl`, `countryCode`, `recurringProcessingModel`, `shopperInteraction`, a non-PII `shopperReference` of at least three case-sensitive characters, and `storePaymentMethod: true`. Email, phone and locale are optional in this table. The table warns against SEPA Direct Debit CardOnFile because of chargeback risk and recommends individual Debit Risk authorization for shopper-present flows.
- A `recurring.token.created` webhook provides the `storedPaymentMethodId`. Use that token only when the shopper is absent, for `Subscription` or `UnscheduledCardOnFile`. Subsequent `/payments` requests use `paymentMethod.type: sepadirectdebit`, `storedPaymentMethodId`, the same shopper reference, `shopperInteraction: ContAuth` and the relevant recurring model. The page's examples are TEST requests in EUR and do not establish production success.
- The token-creation parameter table describes online `shopperInteraction` as `Ecommerce`, but its initial-token code examples set `ContAuth`. The page does not resolve this conflict; do not copy the sample as an authoritative value for a shopper-present initial authorization. The Component initialization snippet also lacks quotes around `directEbanking`, unlike the API type examples.
- Before accepting live payments, the guide says to test with Klarna test data, inspect test payments in Customer Area, and enable Klarna Debit Risk on the live merchant account. This is a prerequisite checklist, not evidence that a live account has been enabled.

## Detail locators

- Sessions requirements, ordinary request/configuration non-additions, import and Component snippet: pinned raw lines 25–72. Advanced equivalents: lines 1083–1121.
- Recurring purpose, permission recommendation, initial-token table and examples: lines 74–455 and 1123–1504. The table says `Ecommerce` at lines 102/1151, while token-creation samples use `ContAuth` at lines 128/1166–1180 and language variants.
- Token-created webhook and shopper-absent constraint: lines 455–463 and 1504–1512. Subscription and unscheduled SEPA payment samples: lines 465–1073 and 1514–2122.
- Test and live enablement: lines 1075–1081 and 2124–2130.

## Related

- [[adyen-online-payments]] — provider payment integration concept
- [[source-adyen-docs-payment-methods-klarna-debit-risk]] — method overview and non-settlement risk

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna-debit-risk/web-component/2026-09-15|Klarna Debit Risk Web Component guide, captured 2026-09-15]]
