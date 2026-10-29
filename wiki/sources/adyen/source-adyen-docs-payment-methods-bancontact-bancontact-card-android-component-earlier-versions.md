---
title: "Bancontact card Android Component v4.x.x integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, bancontact, card, android, components, earlier-versions, 3d-secure, tokenization]
---

## Overview

This 2026-09-15 guide is for **Bancontact card Android Component v4.x.x**, with an existing **Advanced-flow Android Components** integration. It covers `BcmcComponent`, encrypted card-data handoff to the merchant server, mandatory 3D Secure redirect, `/payments/details`, WIP-gated recurring tokens and TEST/live setup. It is version-scoped historical integration evidence, not proof of current Android SDK behavior, WIP eligibility, live acceptance or payment success. [[adyen]] [[adyen-online-payments]] [[adyen-android-sdk]]

## Key takeaways

- **Card-only scope:** Bancontact card has no CVC, though a co-badged card may show one; **3D Secure is mandatory** and separate captures are unsupported. The Component collects sensitive card information without sending it through the merchant server, and this guide requires Redirect Component handling for 3DS. Its requirement is **Advanced-flow Android Components** plus Bancontact card addition in Customer Area, although several handling/See-also links point to Sessions guides. Use the matching version/flow, not the linked label alone. See raw lines 15–35 and 944–948.
- **Show and submit:** request `/paymentMethods` for `countryCode=BE`, `amount.currency=EUR`, select method `type=bcmc`, add the `com.adyen.checkout:bcmc` module, configure `BcmcConfiguration` with a client key, and attach `BcmcComponent`. The prose conditions sending Component data on both valid state **and** the shopper proceeding to pay, but the observer sample calls `sendPayment` as soon as `isValid` is true without an explicit shopper-action guard. Do not copy that observer as a submit handler; send `paymentComponentState.data` to the server for `/payments` only on the shopper's pay action. The `<latest-version>` dependency placeholder is not a stated v4 patch version. See raw lines 36–102.
- **Server/redirect:** the prose calls for Component payment data, Android channel and an app return URL obtained through `RedirectComponent.getReturnUrl(context)` (it writes `returnURL`). But `/payments` curl and language samples show a web `returnUrl`, `paymentMethod.type=scheme` despite earlier `bcmc` selection, and the curl has a literal hint-wrapped `paymentMethod` key. Treat these as unresolved prose/sample differences, not a copy-ready Bancontact request or safe card-data recipe. The examples are TEST endpoints using v68 `/payments`, not a universal minimum. See raw lines 102–135 and 137–441.
- **Authentication/outcome:** `/payments` may return `RedirectShopper` with `action.type=redirect`; use the Redirect Component for 3DS, then send its `actionComponentData.details` to server-side `/payments/details`. Its sample uses a v72 TEST endpoint and `Authorised` response. Present the synchronous `resultCode`, but the guide also says payment outcome arrives asynchronously by webhook. Possible result codes here are `Authorised`, `Cancelled`, `Error` and `Refused`. A sample `Authorised` is not live-payment proof. See raw lines 442–509.
- **Recurring is WIP-gated:** the guide recommends explicit shopper permission, says **Bancontact Wallet Initiated Program (WIP)** requires signup and not all companies qualify, and says amount limits apply. Under its WIP description, the first transaction involves SCA/consent; later transactions do not require SCA, while the issuer remains liable (the page says no liability shift). To create a token add `storePaymentMethod=true` and a shopper reference; after settlement receive `recurring.token.created` via the lifecycle webhook. Later `/payments` uses stored ID, same shopper reference, `ContAuth` and `Subscription` or `UnscheduledCardOnFile`. Contact Support to configure recurring TEST. Do not infer general Bancontact recurring from tokenization text alone. See raw lines 511–568. [[adyen-tokenization]]
- **TEST/live:** the co-badged BCMC/Visa test card may route to Bancontact **or Visa depending on payment-method setup**. `holderName=DECLINED` is a test refusal trigger. For live, add Bancontact card in live Customer Area. The setup prose earlier requests a **client key**, but final live step says **Client Encryption Public Key**; preserve this credential-label conflict and verify the applicable v4 setup before implementation. See raw lines 57–68 and 907–942.

## Detail locators

- v4 scope, card/CVC/3DS/capture, Advanced requirement and Sessions-link tension: raw lines 15–35.
- BE/EUR `bcmc` selection, module, client key and Component lifecycle: raw lines 36–102.
- Server handoff, channel/return URL and inconsistent `scheme`/hint examples: raw lines 102–441.
- Redirect, `/payments/details`, synchronous result and async webhook: raw lines 442–509.
- WIP eligibility, amount/SCA/liability, token webhook and reuse: raw lines 511–906.
- Co-badged TEST routing, refusal and live credential-label conflict: raw lines 907–942.

## Related

- [[adyen-online-payments]] — Bancontact card online route.
- [[adyen-android-sdk]] — version-scoped Android Component setup.
- [[adyen-tokenization]] — WIP-gated recurring token path.
- [[source-adyen-docs-payment-methods-bancontact]] — card/mobile overview and WIP footnote.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/android-component/earlier-versions/2026-09-15|Bancontact card Android Component v4.x.x, captured 2026-09-15]]
