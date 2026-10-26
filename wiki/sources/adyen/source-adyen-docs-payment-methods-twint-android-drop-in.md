---
title: "Adyen TWINT Android Drop-in guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/twint/android-drop-in/2026-09-15.md"
tags: [adyen, twint, android, drop-in, sessions, advanced, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds TWINT to an existing Android Drop-in integration in Sessions or Advanced server-side flow. Sessions specifies Checkout API v68 or later; Advanced requires handling an additional `redirect` or `sdk` action. It gives method configuration, token creation/reuse and stored-method display guidance. It does not show a complete initial payment response, shopper handoff or final outcome; this snapshot does not prove current merchant enablement or a completed payment. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-twint]].

## Key takeaways

- Both flows require an existing Android Drop-in integration and TWINT added in Customer Area. The Sessions requirement explicitly says Checkout API v68+, while the Advanced requirement states action handling for `redirect` or `sdk` without a version minimum here. For an ordinary TWINT session, no extra `/sessions` parameters are prescribed; for an ordinary Advanced `/payments`, the page says no extra parameters. These statements do not negate the later conditional fields for token creation or reuse.
- The TWINT configuration object offers `setSubmitButtonVisible`, `setActionHandlingMethod` and `setShowStorePaymentField`; the store-field option defaults to `true` according to the table. The page does not mark these parameters required. Showing a store option is not itself shopper consent, token creation or entitlement to charge later.
- For token creation, the page instructs `/payments` with `storePaymentMethod: true` and a unique `shopperReference` of at least three characters. Once details are stored, the `recurring.token.created` webhook carries `shopperReference`, initial-payment `pspReference` as `eventId`, and `storedPaymentMethodId`; the server must be able to receive the Recurring tokens life cycle webhook. For direct future `/payments`, it lists stored method ID, same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. It also cites `/listRecurringDetails` as a way to obtain the stored ID. This is a token path, not proof a token or future payment succeeded.
- A later repeated recurring section discusses showing stored TWINT methods in Sessions or Advanced UI. Sessions text literally says `storedPaymentMethodMode` and `shopperReference` in `/sessions`, then passes the response to Drop-in; the field spelling should be verified against the API authority before implementation. Advanced text uses `PaymentComponentState.data.storePaymentMethod`, `/payments` `storePaymentMethod`/`shopperReference`, and `/paymentMethods` `shopperReference` for the stored list. It says to set `setShowStorePaymentField: false` to remove the storage option. Both tabs also include `TwintComponent` construction examples even though this is a Drop-in guide; those snippets are Components alternatives, not additional Drop-in requirements. Do not conflate UI stored-method selection with shopper-absent `ContAuth` token payments.
- The page says to check test-payment status in Customer Area and submit a request for TWINT in the live Customer Area before accepting live payments. Market/currency and capture details belong to the TWINT overview and other authority, not this Android add-on; no actual test/live outcome is shown.

## Detail locators

- Sessions prerequisite, v68+, Customer Area setup and normal `/sessions` additions: pinned raw lines 25–40.
- Optional TWINT configuration fields and default store-field visibility: pinned raw lines 42–66.
- First token create/reuse path and test/live steps: pinned raw lines 68–115.
- Advanced prerequisite, redirect/sdk action, configuration and ordinary `/payments` additions: pinned raw lines 117–157.
- Repeated token path: pinned raw lines 159–204; later stored-method UI tabs, literal Sessions field and Components snippets: lines 206–280.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[adyen-tokenization]] — provider token lifecycle and stored-method scope
- [[source-adyen-docs-payment-methods-twint]] — method overview and CH/CHF/capture context

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/android-drop-in/2026-09-15|TWINT Android Drop-in guide, 2026-09-15]]
