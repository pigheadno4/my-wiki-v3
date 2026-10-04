---
title: "Braintree Local Payment Methods Custom Client-Side Implementation (Android v5)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/client-side-custom/android/v5"
raw_files:
  - "braintree/docs/guides/local-payment-methods/client-side-custom/android/v5-2026-09-16.md"
tags: [braintree, local-payment-methods, android, android-v5, custom-ui, tokenization]
---

## Overview

This [[braintree]] website-guide snapshot, collected 2026-09-16 and routed as Android v5, documents the custom client-side half of a Local Payment Methods integration. A merchant application can present its own method UI, create and launch a payment-authorization request, preserve the pending request across the external flow, handle the return to the app and tokenize a successful authorization result into a local-payment result whose success case exposes a nonce. The guide then routes the integration to a separate server-side page and requires Local Payment Method webhooks.

The client request, external-flow return and nonce are integration transitions, not proof that a payment completed, settled or funded. This page also does not classify a selected method as instant or non-instant. Follow [[braintree-payment-methods]] for the provider payment-method boundary and [[braintree-android-sdk]] for the platform context.

## Key takeaways

- Before adding Local Payment Methods, the app must declare a URL scheme in its Android manifest for browser-switch return handling. The example initializes `LocalPaymentLauncher` during `onCreate()`, handles the app return according to activity launch mode, and retains a started pending request for the later return.
- The merchant account selected at the start determines the PayPal credentials and must match the account used by other transaction-lifecycle calls. The page says it cannot be switched between the start and finish of the local-payment transaction.
- The success branch tokenizes `LocalPaymentAuthResult.Success` and handles a `LocalPaymentResult`; the displayed result branches are success with a nonce, failure and cancellation. This is client-side tokenization evidence only. The linked server-side implementation and the required webhook handling remain separate responsibilities.
- The payment-method, country, currency, required-parameter, transaction-limit and shipping-address tables/examples are retained as raw locators. They are snapshot documentation, not proof of uniform merchant eligibility, buyer eligibility, present availability, runtime validation or payment completion.

> [!warning] Historical mobile-certificate notice
> The captured page says the Braintree Mobile iOS and Android SDK certificates were due to expire on March 30, 2026, advises Android SDK `4.45.0+` or `5.0.0+`, and warns that all customer traffic for affected app versions would fail if those versions were neither decommissioned nor force-upgraded by that date. Because the snapshot was collected after the stated deadline, this is historical page evidence, not confirmation of current certificate state, current SDK support or compatibility for a particular app.

> [!warning] Conflicting dependency examples
> Under the same `Get the SDK` section, the Kotlin example shows `com.braintreepayments.api:local-payment:5.8.0` while the Groovy example shows `5.2.0`. Preserve both as captured examples; this page does not resolve the difference or establish either as the current package baseline.

> [!warning] Client/server and outcome boundary
> Starting the authorization flow, returning to the app, tokenizing a successful authorization result and receiving a nonce are not payment-completion, settlement or funding evidence. This page requires webhooks and points to a separate server-side implementation, but does not itself document instant-versus-non-instant completion semantics.

## Detail locators

- Dated mobile-certificate expiry, Android version floors and stated total-traffic consequence: `# Client-Side Implementation > **IMPORTANT**`, raw lines 17-20.
- Android manifest URL-scheme prerequisite: `## Setup`, raw line 27.
- Kotlin and Groovy local-payment dependency examples with different captured versions: `### Get the SDK`, raw lines 30-49.
- Merchant-account credential selection, lifecycle consistency and no-switch condition: `### Determine which merchant account to use`, raw lines 51-53.
- Local-method identifiers, country/currency combinations and `paymentTypeCountryCode` fallback: `### Invoke payment flow`, raw lines 56-74.
- Required-parameter and transaction-limit table: `### Invoke payment flow`, raw lines 76-88.
- Launcher/client initialization, return handling, pending-request use, tokenization, launch and result branches: `### Kotlin`, raw lines 91-207.
- Required webhook route: `### Kotlin > **IMPORTANT**`, raw lines 211-212.
- Shipping-address prompting and pre-collected-details behavior: `### Shipping addresses`, raw lines 217-221.
- Next-page server-side navigation: raw line 223.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Platform context: [[braintree-android-sdk]]
- Article owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

- [[raw/braintree/docs/guides/client-sdk/setup/android/v5-2026-09-16|Braintree Android v5 client SDK setup]] - linked URL-scheme and browser-switch setup navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Braintree Local Payment Methods server-side implementation for Node.js]] - exact collected server-side next-page route; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Braintree Local Payment Method webhooks for Node.js]] - exact collected webhook-detail route; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/client-side-custom/android/v5-2026-09-16|Braintree Local Payment Methods custom client-side implementation (Android v5)]] - fully read pinned website snapshot covering custom UI initiation, return handling, tokenization, merchant-account consistency, webhook dependency and historical SDK warnings
