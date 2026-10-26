---
title: "Adyen TWINT Web Component guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/web-component"
raw_files:
  - "adyen/docs/payment-methods/twint/web-component/2026-09-15.md"
tags: [adyen, twint, web, components, sessions, advanced, capture, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds TWINT to an existing Web Components integration, with separate Sessions and Advanced server-side instructions. It covers redirect prerequisites, `Twint` import/initialization, recurring-token use, and a later capture section. It does not give a concrete TWINT `/payments` response, redirect return or final payment webhook sequence; follow the main flow authority for those steps. This snapshot does not prove merchant enablement, token creation, capture or payment success. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Sessions:** requires an existing Web Components Sessions integration, **Checkout API v68 or later**, `action.type: redirect` handling and TWINT added in Customer Area. It states no TWINT-specific `/sessions` parameters or Component configuration. The page imports `Twint` from `@adyen/adyen-web` and constructs `new Twint(checkout, {...}).mount('#twint-container')`; the snippet's configuration-object comment should not override the explicit no-additional-configuration statement. (raw lines 25–76)
- **Advanced:** separately requires existing Web Components Advanced, redirect handling and Customer Area addition. It also imports/initializes `Twint` and says no TWINT-specific `/payments` parameters. This section does **not** state a Checkout API minimum or a separate no-extra-configuration rule; do not carry the Sessions-only v68/configuration wording across unqualified. (raw lines 125–167)
- **Recurring:** both flow sections require token creation and reuse. Initial `/payments` adds `storePaymentMethod: true` and a shopper-unique `shopperReference` of at least three characters. Once details are stored, `recurring.token.created` supplies `storedPaymentMethodId`, initial payment `pspReference` as `eventId`, and shopper reference; the merchant server must receive lifecycle webhooks. Future `/payments` requests use the stored ID, same shopper reference, `ContAuth`, and `Subscription` or `UnscheduledCardOnFile`. The page repeats this token route after its capture section; it does not show a successful token issuance or later payment. (raw lines 78–117, 169–208, 245–282)
- **Capture:** the later section says TWINT is captured automatically by default with Capture Delay **Immediate** or **1–7 days**. If the setting is **Manual**, authorization expires after **7 days**, so capture must occur before then. TWINT allows a partial capture but not multiple partial captures; any unclaimed remainder is automatically cancelled. Capture prose names `modificationAmount` while the JSON example uses `amount` and `reference`; verify the endpoint contract instead of treating the example as a consistent field list. The page does not tie this section to one flow explicitly. (raw lines 216–243)
- **Environment:** both flow sections direct TEST status checks to Customer Area and require a separate TWINT request in the **live** Customer Area before live acceptance. These instructions are not evidence of test success or live activation. (raw lines 119–123, 210–214)

## Detail locators

- Sessions requirements, no-extra-fields/config, Web import and Component: pinned raw lines 25–76.
- Advanced prerequisites, Web import/Component and `/payments` field statement: pinned raw lines 125–167.
- Repeated token lifecycle and ContAuth models: pinned raw lines 78–117, 169–208 and 245–282.
- Capture setting, seven-day expiry, partial-capture remainder and prose/example mismatch: pinned raw lines 216–243.
- TEST checks and LIVE request gates: pinned raw lines 119–123 and 210–214.

## Related

- [[adyen-online-payments]] — main provider payment/action context
- [[adyen-tokenization]] — provider stored-method lifecycle
- [[source-adyen-docs-payment-methods-twint]] — TWINT method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/web-component/2026-09-15|TWINT Web Component guide, 2026-09-15]]
