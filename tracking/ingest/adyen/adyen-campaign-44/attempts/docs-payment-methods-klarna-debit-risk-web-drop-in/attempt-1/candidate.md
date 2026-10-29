---
title: "Adyen Klarna Debit Risk Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna-debit-risk/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/klarna-debit-risk/web-drop-in/2026-09-15.md"
tags: [adyen, klarna-debit-risk, web-drop-in, redirect, sepa-direct-debit, tokenization]
---

## Overview

This [[adyen]] guide describes method-specific additions for Klarna Debit Risk in an existing Web Drop-in integration. It separates Sessions and Advanced server-side flows and provides a recurring route through SEPA Direct Debit tokens. Klarna Debit Risk is distinct from Klarna Pay Now: the related [[source-adyen-docs-payment-methods-klarna-debit-risk]] overview describes non-guaranteed online-banking settlement and possible chargeback after an `AUTHORISATION` webhook. Use [[adyen-online-payments]] for the surrounding integration context. This guide alone does not prove enabled merchant access or payment settlement.

## Key takeaways

- **Sessions and Advanced setup:** Sessions requires an existing Web Drop-in Sessions flow, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and Klarna Debit Risk added in Customer Area (raw lines 25–36). Its ordinary `/sessions` request needs no method-specific additional parameters (raw lines 38–42). Advanced requires an existing Web Drop-in Advanced flow, redirect handling and Customer Area setup; its ordinary `/payments` request likewise needs no method-specific additions (raw lines 1066–1094). Optional tree-shaken import includes `Redirect` (raw lines 44–54, 1078–1088). These statements concern the ordinary Drop-in payment, not the separate token-creation request.
- **SEPA token route:** Both sections describe creating a token from a Klarna Debit Risk payment, then using that token for later **SEPA Direct Debit** transactions (raw lines 58–73, 1098–1113). They strongly recommend explicit shopper permission and clear schedule/amount disclosure to reduce chargeback risk (raw lines 65, 1105). Token creation's request table marks `paymentMethod.type: directEbanking`, `returnUrl`, `countryCode`, `recurringProcessingModel`, `shopperInteraction`, `shopperReference` and `storePaymentMethod: true`; `shopperReference` must have at least three characters and no PII (raw lines 73–87, 1113–1127). The `recurring.token.created` webhook carries `storedPaymentMethodId` (raw lines 437, 1477).
- **Token-use boundary:** This page says to use tokenized payments only without a present shopper, for `Subscription` or `UnscheduledCardOnFile`; the later payment is processed as `sepadirectdebit`, with the stored method ID, shopper reference and `ContAuth` shown in examples (raw lines 439–450, 777–807, 1479–1490, 1817–1847). The table also lists `CardOnFile` as a model while advising against SEPA Direct Debit for that flow because of chargebacks and favoring a shopper-authorized Klarna Debit Risk payment (raw lines 83, 1123). Do not infer a reusable Klarna wallet credential or guaranteed settlement.
- **Prose/example tensions:** The token-creation table labels online `shopperInteraction` as `Ecommerce` and marks `countryCode` required, but the adjacent subscription token examples use `ContAuth` and omit `countryCode` (raw lines 79–87 versus 89–112; repeated at 1119–1127 versus 1129–1152). The prose also says no extra token parameters while its table enumerates standard tokenization fields (raw lines 69–87). Follow the table and the main tokenization guide for the chosen operation; do not treat the example alone as a validated schema.
- **Test and live:** The guide calls for test-environment/sample-data validation and a distinct live merchant-account enablement step (raw lines 1056–1064, 2096–2104). TEST endpoints and versioned library examples are reference material, not live-payment or funds-arrival evidence.

## Detail locators

- Sessions flow requirements, ordinary request and optional import: pinned raw lines 25–54.
- Sessions token creation table, examples and webhook: pinned raw lines 58–437.
- Sessions token use and test/live guidance: pinned raw lines 439–1064.
- Advanced flow requirements, ordinary request and optional import: pinned raw lines 1066–1094.
- Advanced token creation, token use and test/live guidance: pinned raw lines 1098–2104.

## Related

- [[adyen-online-payments]] — provider checkout context.
- [[adyen-tokenization]] — token lifecycle context.
- [[source-adyen-docs-payment-methods-klarna-debit-risk]] — method identity, EUR/country scope, non-guaranteed settlement and chargeback warning.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna-debit-risk/web-drop-in/2026-09-15|Klarna Debit Risk Web Drop-in guide, captured 2026-09-15]]
