---
title: "Alipay+ API-only integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay-plus/api-only"
raw_files:
  - "adyen/docs/payment-methods/alipay-plus/api-only/2026-09-15.md"
tags: [adyen, alipay-plus, wallets, api-only, redirect, online-payments]
---

## Overview

This 2026-09-15 Alipay+ guide is a method-specific add-on to an existing Adyen Advanced API-only integration. It describes the generic Alipay+ payment-method request, wallet selection after redirect, return/details handling and wallet-specific outcome identifiers. Its country/currency lists and examples are a historical documentation snapshot, not proof that every listed wallet is available to a given merchant or that a payment completed. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and discovery:** The merchant needs an existing API-only integration that handles a `redirect` action and has Alipay+ added in Customer Area. The merchant-built form lists Alipay+ without extra shopper fields. For `/paymentMethods`, the guide lists allowed `countryCode` and `amount.currency` values; its SG/SGD example response shows generic `alipay_plus`. These lists and the sample `/v72` TEST endpoint do not establish current wallet-by-wallet eligibility or a general API version minimum. (raw lines 23–52, 54–72, 264–275)
- **Request and channel:** Initial `/payments` requests use `paymentMethod.type: alipay_plus`; a wallet must not be preselected through that field. `channel` is documented as required with Web, iOS or Android context, and `browserInfo` is required for Web. The guide says channel and browser user agent affect wallet entry points; iOS/Android in-app contexts use a hosted redirect page that may deep-link or app-switch if supported, with no native SDK integration. A wrong channel can yield an incompatible redirect experience. (raw lines 277–284, 286–322, 461–492)
- **Redirect and wallet resolution:** An example `/payments` response is `RedirectShopper` with a GET `redirect` action, an intermediate shopper action. After authentication and return, a `redirectResult` is used in `/payments/details`; the example response is `Authorised` and resolves to `alipay_plus_gcash`. The guide says the wallet-specific `paymentMethod` also appears in the later AUTHORISATION webhook. The wallet table maps names to variants; a generic Alipay+ request does not make their capabilities identical. (raw lines 324–459)
- **Material source conflicts:** The redirect section says “Adyen then sends” `/payments/details` with `redirectResult`, while implementation notes say the frontend must call that endpoint; the exact caller responsibility is unresolved here and should be checked against the main API-only guide. The details example includes `paymentData` said to come from the original `/payments` response, but the shown redirect response omits it. The `/payments/details` example resolves to GCash, while the following AUTHORISATION webhook sample names Alipay China despite narrative wording about the actual wallet; do not join those samples as one verified transaction. (raw lines 328–347, 351–402, 404–459, 465–467)
- **Limits and environment conflict:** `storePaymentMethod: true` is stated to fail validation; this guide does not support Alipay+ tokenization. It states no Alipay+ TEST environment and recommends live penny tests, with a separate live Customer Area request before accepting live payments. Its `checkout-test` examples and sample successful TEST-looking result cannot prove a usable Alipay+ TEST path, live availability, capture or settlement. No financial operation was performed. (raw lines 59–72, 288–347, 380–437, 468–469, 494–504)

## Detail locators

- Existing Advanced API-only, redirect and Customer Area requirements: raw lines 23–43.
- Discovery country/currency table, request example and generic method type: raw lines 45–72, 264–275.
- `/payments` channel/browserInfo fields and redirect response: raw lines 277–349.
- Return, details and webhook examples; wallet-specific variants: raw lines 351–459.
- Implementation cautions, platform contexts and TEST/LIVE boundary: raw lines 461–504.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay-plus/api-only/2026-09-15|Adyen Alipay+ API-only guide, 2026-09-15 snapshot]]
