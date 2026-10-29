---
title: "Cash App Pay API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/api-only"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/api-only/2026-09-15.md"
tags: [adyen, cash-app-pay, api-only, redirect, tokenization, online-payments]
---

## Overview

This 2026-09-15-captured Cash App Pay guide adds the **Cash App Pay** wallet to an existing API-only integration using merchant-built payment UI. It covers method discovery, redirect payment and result handling, and optional tokenized recurring or card-on-file payments. This is distinct from Cash App Afterpay. The snapshot does not prove current merchant eligibility, live enablement, shopper authorization or settlement. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Prerequisites and discovery:** The page requires an existing API-only integration, enables recurring-token lifecycle webhooks, and calls for Support to add Cash App Pay; it explicitly says an API-only merchant cannot add the method in Customer Area themselves. It also instructs enabling **Payment > Recurring details** additional data. If using /paymentMethods to display choices, the guide specifies US country, USD currency, minor-unit amount and channel Web/iOS/Android; the returned method type is `cashapp`. These are captured request conditions, not current account eligibility (raw lines 21–45).
- **One-time redirect:** The server-side /payments instruction specifies `paymentMethod.type: cashapp`, `paymentMethod.subtype: redirect`, and channel Web/iOS/Android. The illustrated response is `RedirectShopper` with a redirect action. Send the shopper to the returned `action.url`; after return, send URL-decoded `redirectResult` in /payments/details. The iOS SFSafariViewController and Android Chrome Custom Tabs advice, plus default-browser advice for mobile, are recommendations rather than universal requirements (raw lines 47–74, 374–429).
- **Result and capture:** The guide says /payments/details `resultCode` is used for shopper display and that an asynchronous webhook also conveys outcome. `Received` means the final result is not yet known and an AUTHORISATION webhook follows; `Authorised` is documented as successful but requires a separate capture if the merchant uses manual capture. Cancelled, Error and Refused have distinct shopper actions; Error/Refused point to refusalReason. Neither a redirect nor Received proves completed payment (raw lines 431–443).
- **Tokenized future payments:** The page describes future recurring and card-on-file use after an initial Cash App Pay token-creating transaction. It recommends explicit shopper permission; with permission to save details, the guide says future payments can bypass shopper approval. For token creation, the examples use `storePaymentMethod`, `shopperReference`, `shopperInteraction: Ecommerce` and `recurringProcessingModel: Subscription`. To obtain the shopper's $cashtag, enable **Token information for digital wallets**, then read `cashapp.cashtag`, shopperReference and storedPaymentMethodId from /payments/details additionalData; the `recurring.token.created` webhook carries token references but **not** the $cashtag. In later tokenized payments, `paymentMethod.cashtag` is optional and recommended for recognition, while the stored token and other tokenization parameters come from the linked tokenization guide. When Cash App Pay details are deleted, `recurring.token.disabled` signals the token should be removed to avoid later failed attempts (raw lines 445–455, 459–480, 813–857, 859–883, 1223–1243).
- **Test and live:** The page directs testing in Adyen's test environment with Cash App Pay sandbox magic values and checking test payments in Customer Area. Its go-live sentence says to add Cash App Pay in live Customer Area; read that with the API-only Support requirement rather than inferring self-service setup. No test example proves live acceptance (raw lines 21–30, 1245–1249).

> [!warning] Contradiction and captured example limits
> The separate [[source-adyen-docs-payment-methods-cash-app-pay|Cash App Pay method overview]] labels its capability-table payment flow **Direct** (separate pinned overview raw line 27), while this API-only child explicitly specifies a redirect subtype/action (this raw lines 49–53, 374–388); the method-level table does not replace this integration's returned action. The initial /payments sample uses v52 and /payments/details uses v72, so the examples do not establish a minimum Checkout API version (lines 58, 407). The initial-token curl renders `storePaymentMethod` as the string "true" while library examples use a boolean, and the later-token curl omits a comma after `returnUrl` (lines 475, 511, 645, 798, 880–882). Use the flow guidance and API schema rather than treating those snippets as paste-ready requests.

## Detail locators

- Requirements, conditional /paymentMethods discovery, and first payment request: pinned raw lines 21–74.
- Redirect, /payments/details and result-code actions: pinned raw lines 374–443.
- Initial token creation, permission, $cashtag retrieval and later token usage: pinned raw lines 445–857 and 859–1221.
- Token-disabled webhook and test/live instructions: pinned raw lines 1223–1249.
- Separate method-level Direct classification: `raw/adyen/docs/payment-methods/cash-app-pay/2026-09-15.md` line 27; the child raw_files field names only this API-only page.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/api-only/2026-09-15|Cash App Pay API-only guide, captured 2026-09-15]]
