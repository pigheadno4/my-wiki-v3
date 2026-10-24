---
title: "PayPal Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/web-component"
raw_files:
  - "adyen/docs/payment-methods/paypal/web-component/2026-09-15.md"
tags: [adyen, paypal, web-components, wallets, tokenization]
---

## Overview

This 2019-modified, 2026-09-15-captured [[adyen]] guide adds PayPal Smart Payment Buttons to an **existing Web Components** integration, through [[adyen-online-payments]]. It states availability from Components **v3.7.0**, requires the existing Components integration and PayPal setup steps, and splits instructions by `/sessions` and `/payments`. These are documented integration paths and examples, not proof that a merchant or shopper has live PayPal access or that a payment completed.

## Key takeaways

- The page calls `/sessions` the default for Components **v5.0.0+**, and `/payments` the route for an additional use case. It shows TEST Checkout examples at `/v71/sessions` and `/v72/payments`, while language-library examples have their own listed versions; those snippets are illustrative, not a single version-independent request contract. The request tables leave `lineItems` unmarked as required. A `/payments` example identifies PayPal with `paymentMethod.type: "paypal"` and `subtype: "sdk"`. See raw locators for fields and samples.
- `additionalData.paypalPairingId` is conditional on a customer-initiated transaction using Fraudnet with the same pairing ID sent to Fraudnet and Adyen. `additionalData.paypalRisk` concerns marketplaces and merchants in certain verticals, with PayPal/its account manager determining applicable fields; the page says to encode them as a stringified `additional_data` array. The common marketplace field table is expressly illustrative, not universally required. For HUF, PayPal expects rounded transaction and line-item amounts to match; Adyen-side rounding can leave a discrepancy that PayPal rejects.
- On the client, the `/sessions` tab says no extra PayPal configuration is needed, and uses `new PayPal(checkout)` on **v6+** versus `checkout.create('paypal')` on **v5 and earlier**. The `/payments` tab lists amount, country code, submission/action callbacks, PayPal merchant ID and intent; its table names `onAdditionalAction` and `configuration.merchantId/intent`, while its example uses `onAdditionalDetails` and top-level `merchantId/intent`. Follow the exact version/flow guide for implementation; the snapshot does not reconcile these differences. The sample rejects absent `resultCode` or unexpected errors and resolves even an unsuccessful result. The page also calls for a `same-origin-allow-popups` cross-origin opener policy to allow PayPal popups.
- Optional settings cover CSP nonce (from v5.2.0), button style, shipping/user-input callbacks, PayPal Credit/Pay Later buttons and Venmo visibility. The page dates per-payment `intent` choices to **v5.34.0+**: capture, authorize, subscription and tokenize. It lists Pay Later country/local-currency scope and cross-border limits and says Venmo appears by default when both merchant and shopper are in the US. These UI options do not establish PayPal funding or shopper eligibility.
- An API `resultCode` can drive a provisional shopper message, but the page says to wait for webhooks for the **final payment outcome**, particularly when risk rules run after authorisation. `AUTHORISATION` success/failure is its listed completion signal; `OFFER_CLOSED` for a timeout requires enabling that non-default event. Optional PayPal details in standard webhooks require the listed additional setting. Neither button rendering nor an `Authorised` synchronous result alone proves capture or settlement.
- For recurring use, the page **strongly recommends** explicit shopper permission. Direct merchants without indirect settlement need PayPal Vault permissions; marketplaces or indirect-settlement arrangements are directed to Adyen Support. Cross-account token sharing needs account configuration. Zero-value token creation requires **v5.3.0+** for `/sessions`; for `/payments`, use `intent: "tokenize"` at **v5.34.0+** or a global amount object at **v5.3.0+**, otherwise the page says no token is created. Zero-value requests require `shopperEmail` and `amount.value: 0`; it says not to include `shopperEmail` for non-zero-value requests. Obtain the shopper reference/token from `recurring.token.created`, rather than assuming a request response produced a usable token.
- Before capture, the guide points to cancellation; after capture, refund. For an immediately captured partial refund, it calls for refund `lineItems` and says a mismatch with amount causes Adyen to add a dummy item. For later capture, `capturePspReference` is required **when later capture, multiple partial captures enabled, and more than one partial capture all apply**; it must be the capture reference, not the payment reference, and omission can cause failure. The immediately captured section's line-item wording mixes “items the shopper should pay for” with “only ... items that you are refunding”; preserve that ambiguity rather than guessing an accounting rule from the example. A refund response with `status: received` is not proof of final refund.
- Seller Protection discussion is limited to **physical goods** and asks program participants for delivery address, shopper name and line items, with a test-payment eligibility check. The testing section uses PayPal business/personal sandbox roles; live setup separately requires a live PayPal business account and configured live environment. It states live PayPal availability also depends on a logged-in shopper with a valid funding method.

## Detail locators

- [[raw/adyen/docs/payment-methods/paypal/web-component/2026-09-15|Pinned raw]], lines 15–48: identity, Components/version/setup prerequisites, `/sessions` default and conditional risk fields; lines 516–568: `/payments` tab and PayPal subtype example.
- Same raw, lines 50–513 and 528–1039: TEST curl and versioned language-library examples; Python `paypalRisk` strings at lines 412 and 927 and the PHP `/payments` example at lines 684–690 need independent scrutiny before use.
- Same raw, lines 1041–1119: HUF rounding, conditional marketplace/vertical risk fields and stringified formatting; lines 1121–1255: DOM/component version split and `/payments` table/example mismatch.
- Same raw, lines 1257–1373: optional settings, Pay Later/Venmo scope and versioned intent; lines 1375–1412: resultCode versus final webhook outcome and optional webhook details.
- Same raw, lines 1414–1485: recurring permission, Vault/marketplace setup, zero-value version/configuration gates and token webhook; lines 1487–1607: capture-sensitive cancel/refund paths and partial-refund example; lines 1609–1643: Seller Protection and sandbox/live boundaries.

## Related
- [[adyen-tokenization]] — generic tokenization context; this page's PayPal and version conditions govern here.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/web-component/2026-09-15|PayPal Component]]
