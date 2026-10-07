---
title: "Braintree Apple Pay Client-Side Implementation for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/apple-pay/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/apple-pay/client-side/ios/v7-2026-09-16.md"
tags: [braintree, apple-pay, ios, client-sdk, payment-method-nonce]
---

## Overview

This captured Braintree website guide documents a custom client-side Apple Pay integration for the Braintree iOS v7 SDK. After the Apple Pay certificate and Merchant ID are configured, the app coordinates PassKit and Braintree configuration, presents a `PKPaymentRequest`, tokenizes the authorized `PKPayment` with the Braintree SDK, and sends the returned payment method nonce to its server for transaction processing. This is versioned implementation guidance and a dated website snapshot, not evidence of current certificate status, merchant eligibility, or a successful payment. See [[braintree]] and [[braintree-apple-pay]].

## Key takeaways

- The iOS v7 path is a custom UI integration. The page says iOS v7 is not supported through Drop-in and points Drop-in users to the v5 implementation guide; it separately records Drop-in deprecation on July 14, 2025 and unsupported status beginning July 14, 2026.
- The app initializes Braintree client authorization, checks device/payment-network availability before showing Apple Pay, and creates a `PKPaymentRequest` either through `BTApplePayClient.paymentRequest` or manually. A manually created request must remain synchronized with gateway settings.
- The client-side authorization is not the terminal payment result: the app tokenizes `PKPayment` into a payment method nonce, sends that nonce to its server, and reports Apple Pay success or failure based on the server-side `Transaction.sale` result.
- For recurring payments, the page recommends MPANs over device-bound DPANs, says MPAN support is available only on iOS 16+, and calls MPAN support a Visa recurring-payments requirement. It also warns that networks without MPAN support may still return DPANs.
- The page carries a critical certificate notice: older Braintree Mobile SDK certificates were stated to expire on March 30, 2026, with iOS SDK 7.0.0+ named as the upgrade path and complete customer-traffic failure stated for app versions left on the older certificates. Because the raw was fetched on September 16, 2026 while the notice still describes that date prospectively, treat it as captured page wording rather than verified current certificate state.

## Detail locators

- **SDK and Drop-in boundary:** raw lines 32–69 (`Get the SDK`) list the custom Apple Pay module/framework options and the dated Drop-in lifecycle and v7-support notices.
- **Client initialization and division of responsibility:** raw lines 74–94 (`Initialization` and `PassKit integration and payment tokenization`) cover client authorization, nonce return, PassKit integration, and the merchant's responsibility for coordinating request and gateway configuration.
- **Availability and payment-request configuration:** raw lines 97–196 cover the Apple Pay button, device/network availability check, request construction, field recommendations, and synchronization with server environment and merchant configuration.
- **Recurring-payment token qualification:** raw lines 199–258 (`Recurring Payments (Transition to MPANs)`) preserve the iOS 16+, Visa, network-support, and DPAN-fallback conditions and locate the recurring, automatic-reload, and deferred request examples.
- **Presentation, tokenization, and server-result handoff:** raw lines 261–324 cover presenting the authorization controller, tokenizing the authorized payment, sending the nonce server-side, reflecting the `Transaction.sale` result, and dismissing the Apple Pay sheet.

## Related

- [[braintree]]
- [[braintree-apple-pay]]

## Raw Sources

- [[raw/braintree/docs/guides/apple-pay/client-side/ios/v7-2026-09-16|Braintree Apple Pay client-side iOS v7 guide (captured 2026-09-16)]]
