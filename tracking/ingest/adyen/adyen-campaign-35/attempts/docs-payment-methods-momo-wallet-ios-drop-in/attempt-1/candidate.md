---
title: "Adyen MoMo iOS Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/ios-drop-in/2026-09-15.md"
tags: [adyen, momo, ios, drop-in, wallets, recurring-payments]
---

## Overview

This 2026-09-15 Adyen guide describes MoMo-specific additions to an existing iOS Drop-in integration, separately for Sessions and Advanced flow. It is an integration guide, not evidence of current merchant eligibility or a completed payment. See [[adyen]], [[adyen-ios-sdk]] and [[adyen-tokenization]].

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration, Checkout API v68 or later, and MoMo added in Customer Area. The page specifies no additional MoMo parameters for the base `/sessions` request and no extra MoMo configuration. These statements do not remove the main integration's requirements.
- Advanced requires an existing iOS Drop-in Advanced integration, MoMo added in Customer Area, and redirect handling for `action.type: redirect`. It specifies no additional MoMo parameters for the base `/payments` request or extra MoMo configuration. The merchant-owned Advanced payment and redirect flow remains in the main guide.
- For optional recurring payments in either flow, create a shopper token through `/payments` with `storePaymentMethod: true` and a unique `shopperReference`. After the initial payment settles, the `recurring.token.created` lifecycle webhook carries the `storedPaymentMethodId`; the server must receive that webhook. A later `/payments` request uses `paymentMethod.storedPaymentMethodId`, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel` selected as `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. Token creation, redirect handling and a request submission do not themselves prove authorization or settlement.
- The test instructions use MoMo's test app and scenario credentials, with payment status checked in the Adyen test Customer Area. Live MoMo acceptance requires a request in the live Customer Area. The sample amount is in VND; this page does not state a general country or currency eligibility rule.

## Detail locators

- Sessions prerequisites and base request/configuration: pinned raw lines 25–46.
- Sessions recurring creation and token-payment fields: pinned raw lines 50–85; examples at 87–284.
- Test and live prerequisites: pinned raw lines 286–297, repeated at 561–572.
- Advanced prerequisites, redirect handling and base request/configuration: pinned raw lines 299–321.
- Advanced recurring creation and token-payment fields: pinned raw lines 325–360; examples at 362–559.
- Example qualification: the Java examples use `setRecurringDetailReference` for the token field while the prose and JSON/curl examples use `storedPaymentMethodId` (lines 77, 99–100, 128–130, 352, 374–375, 403–405). Treat this as an SDK example representation, not proof that the fields are interchangeable across API payloads. The curl samples use Checkout test v68 and VND, not a general SDK-version or currency requirement.

## Related

- [[adyen-ios-sdk]] — native Drop-in and merchant/server integration boundary
- [[adyen-tokenization]] — stored-method and recurring-payment concepts
- [[adyen-online-payments]] — Sessions and Advanced payment flows

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/ios-drop-in/2026-09-15|MoMo iOS Drop-in guide, 2026-09-15]]
