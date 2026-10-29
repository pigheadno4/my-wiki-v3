---
title: "Adyen EPS Web Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/web-component"
raw_files:
  - "adyen/docs/payment-methods/eps/web-component/2026-09-15.md"
tags: [adyen, eps, web, components, redirect, recurring]
---

## Overview

This 2026-09-15 EPS Web Component guide adds EPS-specific steps to an existing Adyen Web Components integration in either Sessions or Advanced flow. It covers redirect readiness, importing and mounting `EPS`, bank-issuer presentation, and later recurring payments through SEPA Direct Debit. It is a method add-on, not a complete checkout integration or proof of current bank availability, merchant enablement or payment success. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-eps|the EPS overview]].

## Key takeaways

- Sessions requires an existing Web Components Sessions integration, Checkout API v68 or later, redirect handling for `action.type=redirect`, and EPS added in Customer Area. No EPS-specific `/sessions` request parameters are required. Import `EPS` from `@adyen/adyen-web`, configure it and mount `new EPS(checkout, …)`. The page describes optional `issuer` preselection, `highlightedIssuers` (added in Adyen Web v5.1.0), and dropdown `placeholder`; no bank is preselected by default. The configuration sample's `d5d5b133-1c0d-4c08-b2be-3c9b116dc326` issuer is absent from this page's test and live lists, so do not treat it as a verified selectable issuer. The sample also shows a single string for plural `highlightedIssuers`; consult the linked integration/API guidance for actual accepted shape rather than inferring it from this example.
- Advanced requires an existing Advanced Web Components integration, redirect handling and EPS added in Customer Area. It likewise imports and mounts `EPS`; no EPS-specific `/payments` fields are prescribed for the ordinary payment request. General payment request construction and redirect completion belong to the linked base integration guide. The Advanced section does not repeat the Sessions configuration table, so this capture alone does not establish Advanced configuration details.
- The captured issuer lists differ between test and live: test lists PSA Bank Group; live lists Austrian banks. The lists are snapshot data, not evidence of present issuer availability or live entitlement. Check test statuses in test Customer Area; accepting live EPS requires submitting an EPS request in live Customer Area.
- For future payments, the guide says EPS recurring transactions use SEPA Direct Debit, not a repeated EPS redirect. It strongly recommends explicit shopper permission and transparency about schedule and amount. Token creation uses `storePaymentMethod=true` and a unique `shopperReference` of at least three characters in `/payments`; after the first payment settles, a `recurring.token.created` webhook supplies `storedPaymentMethodId`. Configure the token lifecycle webhook. Later `/payments` requests use `paymentMethod.storedPaymentMethodId`, the same `shopperReference`, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`. This is a separate server-side recurring request path even when the first Web Component checkout uses Sessions.

## Detail locators

- Page scope and Sessions prerequisites: pinned raw lines 15–36; no additional `/sessions` fields: lines 39–42; import, configuration and mounting: lines 45–90. The sample issuer and `highlightedIssuers` values are at lines 63–75. Sessions test/live issuer lists: lines 92–134.
- Sessions recurring permission, token creation, settlement webhook and later stored-token fields: pinned raw lines 136–173. Sessions test/live Customer Area gates: lines 175–179.
- Advanced prerequisites, import and mounting: pinned raw lines 181–218; its test/live bank lists: lines 220–260; no extra ordinary `/payments` fields: lines 261–263. Advanced recurring and live gates repeat at lines 265–310.

## Related

- [[adyen-online-payments]] — primary provider integration route
- [[adyen-tokenization]] — stored-method and recurring concepts
- [[source-adyen-docs-payment-methods-eps-api-only]] — API-only issuer request details and separate example conflicts
- [[source-adyen-docs-payment-methods-eps]] — EPS method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/web-component/2026-09-15|EPS Web Component guide, captured 2026-09-15]]
