---
title: "Adyen EPS API-only integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/api-only"
raw_files:
  - "adyen/docs/payment-methods/eps/api-only/2026-09-15.md"
tags: [adyen, eps, api-only, austria, redirect, issuer, recurring]
---

## Overview

This 2026-09-15 EPS API-only add-on covers the method-specific steps for an existing Adyen Web API-only integration: present a bank list, pass an issuer ID, request AT/EUR availability and initiate an EPS bank redirect. Its recurring section describes a later SEPA Direct Debit token path, not repeat EPS redirects. The base integration guide owns general redirect handling; this page does not prove current bank coverage, merchant enablement, a completed payment or live recurring eligibility. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-eps|the EPS overview]].

## Key takeaways

- Prerequisites are an existing API-only integration that handles `action.type=redirect` and EPS added in Customer Area. The shopper chooses EPS and a bank, is redirected to the bank site to enter bank details, then returns to the merchant site. Show available banks in the payment form and send the selected bank's issuer ID to the server. The document gives separate test/live issuer lists and says issuer data can also come from `/paymentMethods`.
- To surface EPS in `/paymentMethods`, the guide specifies `countryCode=AT`, `amount.currency=EUR` and the payment amount. The response example places `type=eps` and an `issuers` array in the payment-method object. For `/payments`, add `paymentMethod.type=eps`, the selected `paymentMethod.issuer` and a `returnUrl` of at most 1024 characters. The general `/payments` fields and redirect completion are delegated to the linked base guide.
- Do not blindly copy issuer examples: the live list assigns Dolomitenbank ID `b42dd796-8bda-4893-acc2-ddfae9c9cdb7`, while the example `/paymentMethods` response assigns it `d5d5b133-1c0d-4c08-b2be-3c9b116dc326`. The `/payments` prose says issuer value, then gives 'Dolomitenbank' as an example even though that is a bank name rather than either listed ID. Use the chosen environment's returned issuer ID; the captured examples conflict and do not establish present bank availability.
- Recurring is described through SEPA Direct Debit: request a shopper token with `storePaymentMethod=true` and a unique `shopperReference` of at least three characters. The page strongly recommends explicit shopper permission for future SEPA payments and clear schedule/amount communication. Only after the first payment settles does it say a `recurring.token.created` webhook supplies `storedPaymentMethodId`; configure the recurring-token lifecycle webhook. Future `/payments` prose calls for `paymentMethod.storedPaymentMethodId`, the same `shopperReference`, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`.
- The recurring examples use `paymentMethod.type=sepadirectdebit` and mostly `recurringDetailReference`, contradicting the prose's `storedPaymentMethodId` field; they must not be copied as authoritative request shape without reconciling this difference. The `/paymentMethods` curl example also lacks a shell continuation after `-X POST` before `-d`, and its JSON response example contains a comment. The NodeJS availability examples instantiate `Config` and `EnvironmentEnum` without importing them. These sample defects do not alter the stated AT/EUR, issuer and token-flow concepts.
- Check EPS test statuses in the test Customer Area. Before accepting live EPS, submit an EPS request in live Customer Area. The sample Checkout v72 URLs and library-version labels are examples, not declared minimums or proof of live setup.

## Detail locators

- Scope, prerequisites and bank redirect: pinned raw lines 15–35. Form issuer choice and separate test/live bank IDs: lines 37–84. AT/EUR `/paymentMethods` inputs and curl example: lines 86–114. Response issuer example: lines 363–383. The Dolomitenbank table/response ID mismatch is lines 65 and 375–376.
- `/payments` method-specific fields and `returnUrl` maximum: pinned raw lines 385–391. The prose's bank-name-as-issuer example is line 390. General redirect handling is linked from line 28, not specified as a new response workflow here.
- SEPA recurring scope, permission and token creation: pinned raw lines 393–416. Future payment prose fields: lines 418–430. Divergent `recurringDetailReference` examples start at lines 432–453 and continue through line 733; compare prose line 422. Curl line-break defect: lines 101–106. NodeJS undeclared configuration symbols: lines 221–231 and 335–346. Test/live Customer Area gates: lines 736–740.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-eps]] — method overview and capability marks

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/api-only/2026-09-15|EPS API-only guide, captured 2026-09-15]]
