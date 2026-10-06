---
title: "Braintree JavaScript v2 braintree.setup Configuration"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/configuration"
raw_files:
  - "braintree/docs/reference/client-reference/javascript/v2/configuration-2026-09-16.md"
tags: [braintree, javascript-v2, client-sdk, configuration, tokenization]
---

## Overview

This collected [[braintree]] website snapshot is the JavaScript v2 client reference for configuring `braintree.setup(authorization, integrationType, options)`. It documents a historical Braintree.js client-configuration surface and callback handoff for [[braintree-web-sdk]]; it is not evidence of current SDK or browser support, current hosted behavior, merchant enablement, successful payment execution, or the behavior of a separately retained GitHub version.

## Key takeaways

- `braintree.setup` takes a client token or tokenization key as its authorization string, an integration type of `dropin` or `custom`, and an options object. This is a client-authorization input contract; the page does not document creation of the credential or a server API credential.
- Setup-level options are separate from the options specific to Drop-in and Custom. The common surface routes PayPal and fraud-data configuration and includes readiness, tokenization-success, and error callbacks; integration-specific fields and their conditions remain in the raw table.
- `onReady` receives an integration object. Its PayPal launch and close methods are unavailable in Drop-in, and `initAuthFlow` is Custom-only and must run synchronously from a user click or the browser will block the popup.
- When `onPaymentMethodReceived` is supplied, successful client-side tokenization invokes it with payment-method information, including a nonce intended for the merchant server. Braintree.js then neither inserts the hidden nonce field nor submits the form automatically, so sending data to the server becomes merchant-owned. This callback and nonce are not proof of transaction authorization, capture, settlement, or other payment completion.
- `paymentMethodNonceReceived` is deprecated in favor of `onPaymentMethodReceived`. The page also makes the Drop-in `container` and Custom `id` fields required for their respective integration types and notes that error types vary by integration.
- The returned details object varies by payment-method type. PayPal billing-address data is not available to all merchants and requires eligibility/enabling through PayPal Support; phone data is conditional on the corresponding PayPal business-account setting. These documented fields and inputs do not prove runtime availability for a merchant or buyer.

## Detail locators

- `Configuration for braintree.setup` lines 14-26 — method signature, client authorization input, supported integration-type strings, and options-object route.
- `Setup method options` lines 29-45 — common-option scope, PayPal and data-collector routes, CORS/CSP note, readiness integration object, teardown route, Custom-only PayPal methods, synchronous-click condition, and device data.
- `Setup method options` lines 46-59 — successful-tokenization callback and merchant-owned server handoff, returned nonce/type/details fields, deprecated callback, error shape, required Drop-in/Custom element IDs, Hosted Fields route, and default vaulted-method selection behavior.
- `onPaymentMethodReceived details object` lines 62-75 — payment-method-dependent details and credit-card display fields.
- `PayPal` lines 77-107 — returned billing, identity, phone and shipping fields; billing-address merchant eligibility; phone-setting condition; and further PayPal configuration navigation.

## Related

- [[braintree-web-sdk]] — provider concept for the browser SDK, client/server nonce boundary, and separately qualified website and exact-version evidence.
- [[source-braintree-docs-reference-client-reference-javascript-v2-best-practices]] — companion historical v2 setup, readiness, teardown and form-handling guidance.
- [[source-braintree-docs-reference-client-reference-javascript-v2-paypal]] — companion historical v2 PayPal options and callback reference.
- [[source-braintree-client-sdk-migration-javascript-v3]] — separately collected historical v2-to-v3 migration route; consult it rather than treating this page as current-support evidence.

## Raw Sources

- [[raw/braintree/docs/reference/client-reference/javascript/v2/configuration-2026-09-16|Braintree JavaScript v2 braintree.setup configuration snapshot (2026-09-16)]]
