---
title: "TWINT Android Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/android-component"
raw_files:
  - "adyen/docs/payment-methods/twint/android-component/2026-09-15.md"
tags: [adyen, twint, android, components, online-payments, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds **TWINT** to an existing Android Components integration, with separate Sessions and Advanced server-side branches. It describes the `TwintComponent`, optional method configuration, and recurring-token paths. The Advanced branch requires handling `redirect` or `sdk` additional actions; the page does not itself demonstrate a successful payment or settlement. [[adyen]] [[adyen-android-sdk]] [[adyen-online-payments]]

## Key takeaways

- **Sessions** requires an existing Android Components Sessions integration, **Checkout API v68 or later**, and TWINT added in Customer Area. Its ordinary `/sessions` creation adds no TWINT-specific parameters. The page imports the `twint` module (plus `components-compose` for Compose) and creates `TwintComponent` from the Session payment method for Compose or Views. See raw lines 25–64 and 92–145.
- **Advanced** requires an existing Android Components Advanced integration, TWINT in Customer Area, and additional-action handling for `action.type: redirect` **or** `sdk`. Its ordinary `/payments` request adds no TWINT-specific parameters. The Advanced requirements table does not state the Sessions v68 minimum. Its Component examples obtain TWINT from the `/paymentMethods` response. See raw lines 194–225 and 253–314.
- Both branches show optional Component settings for submit-button visibility, action-handling method, and a storage-choice field. The table gives `setShowStorePaymentField` a **true** default; the later Advanced recurring section says setting it to **false** removes that UI option. Displaying a storage field is not itself shopper consent or token creation. See raw lines 66–90, 227–251 and 414–423.
- The repeated recurring guidance says to create a token with `storePaymentMethod: true` and a shopper-unique `shopperReference` of at least three characters in `/payments`. Once details have been stored, `recurring.token.created` carries the initial payment's reference and `storedPaymentMethodId`; the merchant server must receive the token lifecycle webhook. Later token `/payments` requests use stored ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. These fields belong to tokenization requests, so they do not contradict the ordinary no-extra-parameters statements. [[adyen-tokenization]] See raw lines 147–186, 316–355 and 363–384.
- A further stored-method display subsection says **Sessions** can request stored methods using `storedPaymentMethodMode` and `shopperReference` in `/sessions`, then pass a supported TWINT `StoredPaymentMethod` to `TwintComponent`. It spells the field exactly `storedPaymentMethodMode`; verify this against the `/sessions` API schema before implementation rather than silently correcting or assuming validity. **Advanced** says to carry the shopper's `data.storePaymentMethod` choice to `/payments`, include shopper reference in `/paymentMethods`, and pass the returned supported stored method to the Component. The page also mentions Drop-in in these subsections, though this source's main scope is Android Components. See raw lines 386–437.
- TEST guidance is a Customer Area status check. Before live TWINT acceptance, the page says to submit a TWINT request in the **live** Customer Area. No explicit TWINT test-case values, authorization result sequence, capture or settlement proof are given here. See raw lines 188–192 and 357–361.

## Detail locators

- Sessions prerequisites, ordinary request, modules, configuration and Component launch: raw lines 25–145.
- Advanced prerequisites, actions, modules, configuration, launch and ordinary request: raw lines 194–314.
- Initial token creation, lifecycle webhook and ContAuth token request (repeated): raw lines 147–186 and 316–355.
- Later Sessions/Advanced stored-method display instructions: raw lines 363–437.
- Test status and live request gate: raw lines 188–192 and 357–361.

## Related

- [[adyen-android-sdk]] — Android Components integration architecture.
- [[adyen-online-payments]] — online payment-method context.
- [[adyen-tokenization]] — token creation and reuse context.
- [[source-adyen-docs-payment-methods-twint]] — TWINT method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/android-component/2026-09-15|TWINT Android Component, captured 2026-09-15]]
