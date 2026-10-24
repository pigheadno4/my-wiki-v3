---
title: "GCash Android Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/gcash/android-drop-in/2026-09-15.md"
tags: [adyen, gcash, android, drop-in, online-payments, recurring-payments]
---

## Overview

This [[adyen]] snapshot, captured 2026-09-15, adds GCash to an **existing Android Drop-in** integration. It separates Sessions and Advanced server-flow additions, a recurring-token route, and test/live guidance. The page is a method-specific add-on, not proof of current Philippines/PHP merchant eligibility, shopper-wallet access, successful authorization, capture, settlement, refund or token creation. See [[adyen-online-payments]] and raw lines 15–25.

## Key takeaways

- **Sessions Drop-in:** an existing Android Sessions Drop-in integration with **Checkout API v68 or later** and adding GCash in Customer Area are stated prerequisites. The page requires no additional GCash-specific `/sessions` parameters or configuration. Its Sessions table does not separately specify redirect handling; shared flow behavior is delegated to the main integration guide. See raw lines 25–46.
- **Advanced Drop-in:** an existing Android Advanced Drop-in integration, handling `action.type: redirect`, and adding GCash in Customer Area are stated prerequisites. The guide requires no additional method-specific configuration or **base** `/payments` parameters; recurring-token requests below do add fields. The Advanced section does not separately state the Sessions v68 minimum. See raw lines 298–318.
- For recurring transactions, initial token creation calls for `storePaymentMethod: true` and a unique `shopperReference` of **at least three characters** in `/payments`, plus a server that receives token lifecycle webhooks. The guide says `recurring.token.created` supplies `storedPaymentMethodId` **when the initial payment has settled**. This `/payments` wording also appears inside the Sessions section, so it should not be generalized into a claim that every Sessions integration calls `/payments` directly. Shopper-consent mechanics are not specified here. See raw lines 48–71 and 320–343.
- For later token payments, it specifies the received `paymentMethod.storedPaymentMethodId` (or `/listRecurringDetails` lookup), the same shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The request snippets use `gcash`, PHP and TEST as examples; an example token ID, payment request or return URL does not prove an authorized future charge. The Java sample uses `setStoredPaymentMethodId`, consistent with the stated field, but its amount differs from the cURL amount; sample amounts are illustrative. See raw lines 73–139 and 345–411.
- Under **Test and go live**, the guide says a successful **live** payment test needs a real mobile number registered to a GCash account, directs payment-test issues to Adyen Support, then says to check **test** payments in the test Customer Area. These live-versus-test statements are distinct and do not by themselves establish an equivalent sandbox outcome. A separate request in the live Customer Area is required before live GCash acceptance. No provider/account/financial test was performed for this record. See raw lines 286–296 and 558–566.

## Detail locators

- Sessions prerequisites, no additional request/configuration and recurring-token fields/webhook: raw lines 25–85.
- Sessions TEST recurring request examples: raw lines 87–283. The cURL example uses `/checkout/v68/payments` and PHP 1000, whereas Java uses PHP 15000 (lines 90–96, 123–125); neither is an eligibility or outcome contract.
- Sessions test/live guidance: raw lines 286–296.
- Advanced prerequisites, redirect and no-extra-base-field statements: raw lines 298–318.
- Advanced recurring conditions and example requests: raw lines 320–555.
- Repeated live-number, support, test-status and live-request wording: raw lines 558–566.

## Related

- [[adyen-online-payments]]
- [[adyen-android-sdk]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/android-drop-in/2026-09-15|GCash Android Drop-in guide — captured 2026-09-15]]
