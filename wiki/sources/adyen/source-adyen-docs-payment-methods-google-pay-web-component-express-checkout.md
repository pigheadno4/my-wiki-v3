---
title: "Adyen Google Pay Web Component express checkout"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/web-component/express-checkout"
raw_files:
  - "adyen/docs/payment-methods/google-pay/web-component/express-checkout/2026-09-15.md"
tags: [adyen, google-pay, web-components, express-checkout]
---

## Overview

This 2026-09-15 capture of Adyen's Google Pay express checkout Web Component guide (page metadata last modified 2025-11-06) describes a wallet checkout with shipping, total, and shopper-information callbacks. It applies only to an existing Web Components **Advanced flow** integration; the page explicitly excludes Android. The Google Pay setup steps and addition of the method in Adyen Customer Area precede the example. This is a historical integration guide, not evidence of current merchant eligibility or a successful payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The example sets Google Pay `SHIPPING_ADDRESS` and `SHIPPING_OPTION` callback intents, asks for a shipping address and option, supplies initial options and `transactionInfo`, then checks `isAvailable()` before mounting. For Web v6.0.0 or later, it says `isExpress: true` is required. Sample US/USD prices, shipping countries, and options illustrate configuration; they do not establish universal market support.
- `onPaymentDataChanged` illustrates address validation and recalculation on initialization, address changes, or shipping-option changes. The merchant must implement the example's `fetchNewShippingOptions` and `calculateNewTransactionInfo` logic. A wallet-side changed amount is **not** sent to Adyen automatically: validate the updated amount and pass it to `onSubmit` for the server's `/payments` request. The guide does not show that request, a response, or an authorization/capture/settlement result.
- The `onAuthorized` callback in the example obtains Google Pay shopper information before `onSubmit`; its name is not proof of Adyen payment authorization. Optional `emailRequired`, `billingAddressRequired`, and `billingAddressParameters` request extra shopper fields.
- Read the snippets with care: the broad example uses `shippingOptions` while the step-by-step section uses `shippingOptionParameters`; the shipping example spells the constructor `GooglePlay` instead of `GooglePay`; and the mount snippet calls `googlepay.isAvailable()` but mounts `googlePay`. These are source-level mismatches, not validated runnable code.

## Detail locators

- Requirements, Advanced-only and Android exclusion: raw lines 21–28.
- Broad HTML/JavaScript sample, callback intents, initial shipping options and amount, data callbacks, shopper callback, and availability check: raw lines 30–174.
- Callback and shipping configurations: raw lines 186–247. v6 express flag and initial total: raw lines 249–284. Optional email and billing address: raw lines 286–312.
- Merchant-owned recalculation and amount-validation handoff to `onSubmit`/`/payments`: raw lines 314–358. Shopper-information callback and mount: raw lines 360–392.

## Related

- [[adyen-online-payments]] — parent online-payment integration concept.
- [[source-adyen-docs-payment-methods-google-pay-web-component]] — base Web Component integration; its Sessions/default path does not override this page's Advanced-only express scope.

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/web-component/express-checkout/2026-09-15|Google Pay express checkout, captured 2026-09-15]]
