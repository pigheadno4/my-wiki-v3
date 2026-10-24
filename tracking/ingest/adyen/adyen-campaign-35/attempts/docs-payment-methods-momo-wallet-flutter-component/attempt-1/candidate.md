---
title: "Adyen MoMo Flutter Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/flutter-component/2026-09-15.md"
tags: [adyen, momo, flutter, components, wallets, tokenization]
---

## Overview

This [[adyen]] MoMo Flutter Components add-on, captured 2026-09-15, describes MoMo-specific requirements for **existing** Sessions or Advanced Flutter Components integrations and a separate recurring-token path. See [[adyen-online-payments]] and [[adyen-tokenization]]. It is not a standalone Flutter Component implementation, merchant-enablement proof, or a verified payment outcome. See raw lines 15–23, 25–46 and 297–319.

## Key takeaways

- **Sessions:** The prose calls for an existing Sessions Flutter Components integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and MoMo added in Customer Area. The base `/sessions` request needs no extra MoMo parameters, and the guide says no additional MoMo Component configuration is needed. The requirement-row link labeled Flutter Components points instead to an **Advanced Drop-in** URL; its label and destination conflict, so use the flow-specific prose and verify the base guide. See raw lines 25–46.
- **Advanced:** The prose calls for an existing Advanced Flutter Components integration, redirect handling and Customer Area method setup. It says the ordinary `/payments` request and Component configuration need no additional MoMo-specific parameters. Its integration-type requirement row also links to an Advanced Drop-in URL rather than Components. This page provides no Flutter Component launch snippet or complete redirect-result procedure. See raw lines 297–319.
- **Recurring:** The guide states MoMo supports recurring transactions. Token creation adds `storePaymentMethod: true` and a shopper-unique `shopperReference` to `/payments`. The `recurring.token.created` webhook, carrying `storedPaymentMethodId`, is described as arriving **when the initial payment has settled**, and the server must receive token-lifecycle events. Later `/payments` calls use that stored ID, the matching shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed schedules or `UnscheduledCardOnFile` for nonfixed schedules. The ordinary-payment no-extra-fields statements do not override these recurring fields. See raw lines 48–85 and 321–358.
- **Example qualification:** The Java examples call `setRecurringDetailReference` while the prose and other request examples use `paymentMethod.storedPaymentMethodId`; the page does not reconcile those field mappings. TEST endpoint snippets and VND amounts illustrate server requests, not actual Flutter runtime behavior, payment status, eligibility or live configuration. See raw lines 77–283 and 350–556, especially 128–130 and 401–404.
- **Testing and live:** The test instructions use MoMo's test app and scenario-specific credentials, and say to check test-payment status in Customer Area. Before live acceptance, a MoMo request must be submitted through live Customer Area. Neither a test app login nor a live request proves enablement or transaction success. See raw lines 286–295 and 559–568.

## Detail locators

- Sessions requirements and ordinary request/configuration: raw lines 25–46.
- Sessions token creation, webhook and later-payment fields: raw lines 48–85; examples at 87–283.
- Advanced requirements, ordinary request/configuration: raw lines 297–319.
- Advanced token creation, webhook and later-payment fields: raw lines 321–358; examples at 360–556.
- TEST and live gates: raw lines 286–295 and 559–568.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/flutter-component/2026-09-15|MoMo Flutter Component — captured 2026-09-15]]
