---
title: "Cash App Pay Android Component v4.x.x (earlier versions)"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, cash-app-pay, android, component, earlier-versions, recurring]
---

## Overview

This 2026-09-15-captured Adyen page describes a **Cash App Pay Android Component v4.x.x** add-on for an existing integration, with an Advanced-flow requirement of **Android Components 4.12.0 or later**. It covers app redirect/return, server payment requests, asynchronous results, tokenized future payments, and test/live setup. It is historical version-specific guidance, not evidence of a current SDK choice, merchant enablement, or completed payment. See [[adyen]] and [[adyen-online-payments]]. Cash App Pay here is distinct from Cash App Afterpay.

## Key takeaways

- **Flow and setup:** The requirements specify an existing **Advanced** Android Components integration, minimum Component version **4.12.0**, the Recurring tokens life cycle events webhook, Cash App Pay in Customer Area, and **Recurring details** under Developer > Additional data. The introduction also links a **Sessions** base guide, while the requirement and payment steps use Advanced; follow the explicit Advanced requirement for this captured page. The title says v4.x.x, but dependency and some base links point to `latest`; pin a compatible version rather than reading those links as proof that current releases share this older flow (raw lines 14–37).
- **Component and return:** The client configuration sets `CashAppPayComponent.getReturnUrl(context)`, and the handling Activity needs an `IntentFilter` for the app return. The page uses the `cashapp` payment-method object, attaches the Component view, submits from a Cash App Pay button, and passes valid Component state to the server when the shopper proceeds. The server's `/payments` request sets `paymentMethod.type: cashapp` and the Component return URL. The USD/v72 TEST request is illustrative, not a live outcome or a Checkout API minimum (raw lines 39–162).
- **Outcome boundary:** The page mentions `resultCode` on the `/payments` response, but its result section directs use of `/payments/details` and says a webhook also carries the outcome. `Received` means the final result is unknown and calls for an **AUTHORISATION** webhook; `Authorised` is successful, with manual capture still needed when configured. `Cancelled`, `Error`, and `Refused` have separate handling. Do not treat the app return, valid Component state, or `Received` as final authorization (raw lines 158–176).
- **Tokenization:** The page says recurring and card-on-file tokenization can support later payments without another shopper approval when the shopper permits storage, and strongly recommends explicit permission and transparency about recurring schedule/amount. The Component can expose a save-details toggle or hide it with automatic storage; pass the resulting `storePaymentMethod` and `shopperReference` in the token-creation `/payments` request. With **Token information for digital wallets** enabled, `/payments/details` additionalData includes the $cashtag, shopper reference and stored payment method ID; `recurring.token.created` has the latter references but **not** the $cashtag. For later token payments, the guide uses `storedPaymentMethodId`, optional `cashtag`, and a sample `ContAuth`/`CardOnFile` request. A `recurring.token.disabled` webhook after shopper deletion calls for removing the stored token to avoid future failed payments (raw lines 74–81, 178–250, 252–277, 600–633).
- **Example and test limits:** The source's optional-setting table spells `setStorePaymentMethod`, while later prose says `setstorePaymentMethod`; the `/payments/details` JSON example spells `merchantRreference`. Treat those as source inconsistencies, not new API/property names. The initial payment example is a curl command inside a JSON fence, and the tokenized examples use TEST v68 while the initial example uses TEST v72; these are examples, not a version compatibility proof. The page points to Cash App Pay sandbox magic values, test Customer Area status, and adding the method in live Customer Area before live acceptance (raw lines 80–81, 137–156, 186–234, 254–597, 635–645).

## Detail locators

- Version, flow and account/webhook prerequisites: pinned raw lines 14–37.
- Configuration, IntentFilter, Component state and one-off payment: pinned raw lines 39–162.
- Result-code and webhook finality: pinned raw lines 164–176.
- Consent, storage, cashtag and token retrieval: pinned raw lines 178–235.
- Later token payment and token-disabled webhook: pinned raw lines 237–633.
- TEST/live instructions: pinned raw lines 635–645.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/android-component/earlier-versions/2026-09-15|Cash App Pay Android Component earlier-versions guide, captured 2026-09-15]]
