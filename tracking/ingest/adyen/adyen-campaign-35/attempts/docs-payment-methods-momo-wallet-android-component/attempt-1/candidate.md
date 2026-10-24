---
title: "Adyen MoMo Android Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/android-component"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/android-component/2026-09-15.md"
tags: [adyen, momo, android, components, wallets, tokenization]
---

## Overview

This [[adyen]] MoMo Android Components add-on, captured 2026-09-15, gives method-specific steps for **existing** Sessions or Advanced Android Components integrations. It uses `InstantPaymentComponent` with MoMo method type `momo_wallet`, requires redirect handling, and documents a separate recurring-token route. See [[adyen-online-payments]] and [[adyen-tokenization]]. This is a historical guide, not evidence that a particular merchant has MoMo enabled, that a test or live payment succeeded, or that the examples are a complete integration. See raw lines 15–23, 25–77 and 377–420.

## Key takeaways

- **Sessions:** Start with an existing Sessions Android Components integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and MoMo added in Customer Area. The base `/sessions` request needs no MoMo-specific parameters; the page shows `instant` and, for Compose, `components-compose` imports, then `InstantPaymentComponent` creation for `momo_wallet`. It gives no concrete Android SDK version in place of `YOUR_VERSION`. See raw lines 25–77 and 79–126.
- **Advanced:** Start with an existing Advanced Android Components integration, additional-action redirect handling, and Customer Area method setup. The base `/payments` request needs no additional MoMo-specific fields. The page again uses `InstantPaymentComponent` with `momo_wallet`; its Compose and View examples derive the method from `/paymentMethods`. The no-extra-fields statement concerns the ordinary payment add-on, not the separate recurring-token requests. See raw lines 377–477.
- **Recurring:** The guide states MoMo supports recurring transactions. For token creation, its `/payments` request adds `storePaymentMethod: true` and a unique `shopperReference`; it says `recurring.token.created` arrives **when the payment has been settled**, carrying `storedPaymentMethodId`, and calls for a server that receives token-lifecycle webhooks. A later token payment uses that stored ID, the same shopper reference, `shopperInteraction: ContAuth`, and a `recurringProcessingModel` selected for fixed-interval `Subscription` or nonfixed `UnscheduledCardOnFile`. A token request or initial redirect does not itself establish settlement or token creation. See raw lines 128–165 and 479–516.
- **Example qualification:** Most later-payment examples use `storedPaymentMethodId`, but the Java examples instead call `setRecurringDetailReference` (raw lines 208–211 and 559–562). Treat that as an unresolved example/API-mapping discrepancy, not a verified substitute. The example amounts in VND and TEST endpoint/library snippets are illustrative; this page does not enumerate merchant-country eligibility or establish live account configuration. See raw lines 167–365 and 518–715.
- **Testing and live:** The test instructions use the MoMo test app and scenario-specific test credentials, and direct checking test-payment status in Customer Area. Accepting live MoMo payments requires a request in the live Customer Area. A downloaded app, selected scenario or live request is not a verified payment outcome or approval. See raw lines 366–375 and 717–726.

## Detail locators

- Sessions prerequisites, base request and component setup: raw lines 25–126.
- Sessions recurring-token fields, webhook and examples: raw lines 128–365.
- Advanced prerequisites, component and base request: raw lines 377–477.
- Advanced recurring-token fields and examples: raw lines 479–715.
- Test app, credentials, status check and live request: raw lines 366–375 and 717–726.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-android-sdk]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/android-component/2026-09-15|MoMo Android Component — captured 2026-09-15]]
