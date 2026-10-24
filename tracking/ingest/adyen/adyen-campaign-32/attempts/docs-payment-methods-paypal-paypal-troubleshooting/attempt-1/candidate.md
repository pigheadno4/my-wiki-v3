---
title: "Adyen PayPal Web troubleshooting"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/paypal-troubleshooting"
raw_files:
  - "adyen/docs/payment-methods/paypal/paypal-troubleshooting/2026-09-15.md"
tags: [adyen, paypal, web, troubleshooting, online-payments]
---

## Overview

This [[adyen]] troubleshooting page, modified and captured 2026-09-15, applies to **Web Drop-in and Web Components integrations using Checkout `/payments`**. It maps a loading overlay, a stuck processing state, custom PayPal button failure and three console-error classes to checks. See [[adyen-online-payments]]. Its symptoms and checks are diagnostic guidance, not evidence that a transaction was authorized, captured or settled. See raw lines 15–21 and 23–96.

## Key takeaways

- If the PayPal overlay spins after the shopper clicks PayPal, the page says the window opens during `onSubmit` but needs the full `response.action` from the server's `/payments` response passed to Drop-in or Component. Browser console silence does not rule out initialization or action-handoff problems. This identifies a client/server handoff to inspect, not a guaranteed repair. See raw lines 23–31.
- If the shopper finishes in PayPal and the UI remains on “Processing Payment,” the page associates that symptom with no `/payments/details` request. For PayPal `action.type: sdk`, configure `onAdditionalDetails` to submit its `state.data` to `/payments/details`. The observed processing message is not payment completion; neither the request nor an API response alone proves the final outcome. See raw lines 33–41.
- A single custom button cannot submit PayPal in this Web integration by hiding its own button with `showPayButton: false`. The page says the PayPal smart button calls the PayPal library to obtain shopper PayPal account information and must remain on the page. This is a method-specific UI constraint, not a statement that the shopper has a valid funding source. See raw lines 43–51.
- The guide recommends testing with browser console open and says that when a console error appears, **the transaction remains an open offer**. For the USD/EUR mismatch error, `amount.currency` must be set in client initialization and `paymentMethodsConfiguration.amount.currency` should match the actual `/payments` currency. The example is labeled `json` but contains ellipses and unquoted keys, so it is illustrative rather than valid JSON. See raw lines 53–76.
- The capture-versus-authorize **intent mismatch** is between payment-method configuration and the PayPal SDK. For **Web Drop-in v3.13.0 or earlier** specifically, the guide says to pass `intent` dynamically from payment-method configuration, avoid an overriding wrong `paypalConfiguration.intent`, and check `paymentMethodsResponse.paypalConfiguration.intent` against the authorization type configured on the merchant account. This is a request/SDK intent diagnostic, not proof that a capture occurred. See raw lines 78–86.
- The merchant-ID console error points to a wrong PayPal Merchant ID in payment-method settings; the page says to compare that setting and contact Adyen Support to verify the account configuration. It does not verify the account or grant permissions itself. This page gives no billing-agreement, recurring-token, funding-source eligibility or actual capture/refund procedure; use the separate PayPal integration guides for those topics. See raw lines 88–100.

## Detail locators

- **Scope, overlay action handoff and missing details request:** raw lines 15–41.
- **Required PayPal smart-button behavior and console-error status boundary:** raw lines 43–55.
- **Currency mismatch and illustrative amount snippet:** raw lines 57–76.
- **Legacy Drop-in intent/merchant configuration and PayPal Merchant ID check:** raw lines 78–96.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypal]]
- [[source-adyen-docs-payment-methods-paypal-web-drop-in]]
- [[source-adyen-docs-payment-methods-paypal-web-component]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/paypal-troubleshooting/2026-09-15|PayPal troubleshooting — captured 2026-09-15]]
