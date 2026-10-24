---
title: "Adyen DANA iOS Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/ios-component"
raw_files:
  - "adyen/docs/payment-methods/dana/ios-component/2026-09-15.md"
tags: [adyen, dana, ios, components, recurring-payments]
---

## Overview

This [[adyen]] page gives DANA-specific additions to an **existing iOS Components** integration in separate Sessions and Advanced flows. It uses `InstantPaymentComponent` for the initial payment and describes later recurring token payments. It is not a standalone iOS integration or proof of current DANA enablement, a completed payment or a stored token. See [[adyen-online-payments]] and [[adyen-tokenization]]. See raw lines 15–23, 25–110 and 320–402.

## Base flow and Component

- **Sessions:** Requires an existing Sessions iOS Components integration, Checkout API **v68 or later**, redirect handling for `action.type: redirect`, and DANA added in Customer Area. The ordinary `/sessions` call and DANA Component need no extra method-specific parameters/configuration. The Swift example checks for `.other("dana")`, creates `InstantPaymentComponent`, sets the **session** as delegate and calls `initiatePayment()`. These method-specific omissions do not remove the main flow's base setup or redirect handling. See raw lines 25–69.
- **Advanced:** Requires an existing Advanced iOS Components integration, redirect handling for `action.type: redirect`, and DANA added in Customer Area. The integration-type URL at raw line 328 points to `integration=Drop-in` despite saying **Components**; the redirect and payment step links are Components-scoped. Use the stated Components context and verify the correct main guide rather than relying on that inconsistent prerequisite URL. No additional DANA configuration or ordinary `/payments` parameters are specified. The Swift example checks `.other("dana")`, sets **self** as delegate and initiates the payment. The Advanced table does not repeat the Sessions v68 minimum. See raw lines 320–363.
- The no-extra-fields claims apply to **ordinary initial** `/sessions` or `/payments` calls. Both recurring sections explicitly add token-creation and later-token fields to `/payments`; the Sessions recurring subsection also uses `/payments`, distinct from its base `/sessions` request. See raw lines 38–48, 72–110, 359–402.

## Recurring and outcome boundary

- The page says DANA supports recurring transactions. To create a token, include `storePaymentMethod: true` and a unique `shopperReference` in `/payments`; the merchant server must receive Recurring tokens lifecycle webhooks. **After the payment has settled**, `recurring.token.created` provides the shopper reference, initial payment `pspReference` as `eventId`, and `storedPaymentMethodId`. Request submission, shopper redirect/return or Component initiation does not establish settlement or token issuance. See raw lines 72–95 and 365–388.
- A later token payment includes `paymentMethod.storedPaymentMethodId` from that webhook (or the stated `/listRecurringDetails` lookup), the same `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The sample chooses `Subscription` and `IDR`; it does not prove an actual payment or universal model eligibility. See raw lines 97–132 and 390–425.
- The samples use a Checkout **test** `v68/payments` endpoint and TEST client environments. Node/Python/Ruby snippets label particular API-library versions and show idempotency-key examples. These are illustrative server calls and version labels, not an iOS SDK minimum, a live environment switch or completed payment evidence. See raw lines 111–308 and 404–601.
- The page repeats that testing successful **live** DANA payments requires a real mobile number registered with a DANA account, checking **test** payments uses the test Customer Area, and accepting **live** DANA payments first requires a DANA request in the live Customer Area. This mixed live/test wording distinguishes prerequisites and status lookups; a submitted request is not approval, and this guide does not give a final authorization webhook contract for the initial redirect payment. See raw lines 310–318 and 603–611.

## Detail locators

- **Sessions prerequisites, no extra base fields, Component/delegate:** raw lines 25–69.
- **Sessions token creation and settled-payment webhook:** raw lines 72–95.
- **Advanced prerequisites, anomalous Drop-in URL, base request/Component:** raw lines 320–363.
- **Advanced repeated recurring fields and webhook:** raw lines 365–402.
- **Representative test requests/library labels:** raw lines 111–308 and 404–601.
- **Testing/live account and Customer Area conditions:** raw lines 310–318 and 603–611.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/dana/2026-09-15|DANA overview]] — ID/IDR, redirect lifetime and amount floor; separate from this iOS Component add-on.

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/ios-component/2026-09-15|DANA iOS Component — captured 2026-09-15]]
