---
title: "Adyen KakaoPay Web Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/kakaopay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/kakaopay/web-drop-in/2026-09-15.md"
tags: [adyen, kakaopay, web-drop-in, wallets, recurring-payments]
---

## Overview

This [[adyen]] guide specifies KakaoPay-specific additions to an **existing Web Drop-in** integration, split between Sessions and Advanced flows. It is not a standalone Web integration recipe; the linked main integration guides supply base setup and redirect handling. See [[adyen-online-payments]] and [[adyen-tokenization]]. The September 2026 page and examples do not prove current enablement, live payment acceptance or actual token/payment settlement. See raw lines 15–48 and 308–336.

## Requirements and one-time flow

- **Sessions:** Existing Sessions Web Drop-in; Checkout API **v68 or later**; redirect handling for `action.type: redirect`; and KakaoPay added in Customer Area. The page says no KakaoPay-specific parameters are needed when creating a **base payment session**. Optionally import `Redirect` with Adyen Web for tree shaking. See raw lines 25–53.
- **Advanced:** Existing Advanced Web Drop-in, redirect handling and KakaoPay added in Customer Area. It says no extra KakaoPay-specific parameters are needed for the **base `/payments` request**, and likewise shows optional `Redirect` import. The integration-type URL at raw line 316 contains an unresolved encoded platform template; use the stated Web Drop-in context and the Web-scoped Advanced redirect/import step links at raw lines 317 and 324 instead of treating that prerequisite URL as a reliable route. This section does **not** restate the Sessions section's v68 minimum, so do not silently generalize that table row to Advanced. See raw lines 308–336.
- The “no additional parameters” statements apply to the one-time base request only. The same guide subsequently requires extra `/payments` fields for token creation and token-funded recurring charges in **both** flow sections. The Sessions section moves to `/payments` for tokenization even though the base Sessions section discusses `/sessions`; keep those request contexts distinct. See raw lines 40–42, 65–95, 334–377.

## Recurring and outcome boundary

- For token creation, the guide says include `storePaymentMethod: true` and merchant-unique `shopperReference` in `/payments`. This triggers a Kakao account login and confirmation of the recurring transaction by the shopper. The merchant server must receive recurring token lifecycle events; **after the payment has settled**, `recurring.token.created` carries `shopperReference`, initial payment `pspReference` as `eventId`, and `storedPaymentMethodId`. Consent/login, a submitted request or an initial response is not itself evidence that settlement or token creation occurred. See raw lines 58–81 and 340–363.
- For a subsequent payment, use `paymentMethod.storedPaymentMethodId` from that webhook (or the stated `/listRecurringDetails` alternative), the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The example request chooses `Subscription` and `KRW`; it is an illustration, not proof every amount, currency or model is enabled or that a payment succeeded. See raw lines 83–116 and 365–399.
- The samples show Checkout test `v68/payments`, API-key placeholders and language-library TEST configurations (with LIVE comments), plus examples of idempotency-key use in Node/Python/Ruby. These are example scopes, not a live transaction, a blanket environment switch or proof that all snippets use the same current client version. See raw lines 97–294 and 379–576.
- The guide says successful **live** payment testing needs a real mobile number registered to a KakaoPay account; test payment status is checked in the test Customer Area; and accepting live payments first requires a KakaoPay request in the live Customer Area. Those are distinct test/live prerequisites and status checks, not evidence that a request was approved or a payment completed. See raw lines 296–306 and 578–588.

## Detail locators

- **Sessions prerequisites and no-extra-base-session parameters:** raw lines 25–53.
- **Sessions token creation, settlement webhook and subsequent-token request:** raw lines 56–95.
- **Advanced prerequisites and no-extra-base-payment parameters:** raw lines 308–336.
- **Advanced repeated token flow:** raw lines 338–377.
- **Representative request snippets and environments:** raw lines 97–294 and 379–576.
- **Test/live qualifications:** raw lines 296–306 and 578–588.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/kakaopay/2026-09-15|KakaoPay overview]] — method scope and linked channels; distinct from this Web Drop-in procedure.

## Raw Sources

- [[raw/adyen/docs/payment-methods/kakaopay/web-drop-in/2026-09-15|KakaoPay Web Drop-in — captured 2026-09-15]]
