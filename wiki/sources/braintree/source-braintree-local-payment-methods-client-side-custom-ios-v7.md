---
title: "Braintree Local Payment Methods Custom Client-Side Implementation for iOS v7"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/client-side-custom/ios/v7"
raw_files:
  - "braintree/docs/guides/local-payment-methods/client-side-custom/ios/v7-2026-09-16.md"
  - "braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md"
  - "braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16.md"
tags: [braintree, local-payment-methods, ios, swift, custom-ui, webhooks]
---

## Overview

This captured Braintree developer guide describes a custom Local Payment Methods client flow for iOS v7. The merchant selects a transaction-consistent merchant account, adds the Local Payment SDK modules, constructs a method-specific `BTLocalPaymentRequest`, and starts `BTLocalPaymentClient`, which the page says launches an `ASWebAuthenticationSession`. It is a platform/version-routed website snapshot for [[braintree]], [[braintree-payment-methods]] and [[braintree-ios-sdk]], not current SDK-package evidence or proof of merchant eligibility, buyer eligibility, payment authorization, completion, settlement or funding. Separate same-date article and Node server snapshots below supply supporting prerequisites and conflicts; they do not change this page's primary identity.

## Key takeaways

- The merchant account determines the PayPal credentials used for the transaction. The guide requires the same merchant account across other calls in that transaction lifecycle and says it cannot be switched between the start and finish of a Local Payment transaction.
- The supporting umbrella article separately limits Local Payment Methods to eligible merchants, requires PayPal to be added to the Braintree integration, and says a valid PayPal Business Account must be created, verified and linked in the Braintree Control Panel before completing the client and server integrations. These article-level prerequisites are not claims made by the primary iOS page.
- The page permits merchant-owned custom UI and gives an iDEAL button as its example. Its captured tables map named Local Payment Methods to `paymentType`, country and currency values, required request parameters and some minimum transaction amounts; those combinations are method-specific rather than evidence of uniform availability or timing.
- The client example initializes `BTLocalPaymentClient`, creates a `BTLocalPaymentRequest`, assigns a flow delegate and calls `start()`. A delegate callback allows preprocessing before invoking its supplied `start` closure. The example callback body is omitted, so this snapshot does not establish a nonce or any completed server-side transaction.
- The primary guide says Braintree webhooks must be implemented to accept Local Payment Methods. The same-date Node server guide calls the Payment Context GraphQL API an alternative to webhooks, but separately documents customer-return and no-return transaction paths, a three-hour auto-refund condition and `local_payment_reversed`. The snapshots do not resolve the scope of the stated alternative, and neither a notification nor a Payment Context is by itself proof of settlement or funding.
- The captured warning says older Braintree Mobile SDK certificates expire on March 30, 2026, directs iOS SDK 6.17.0 or newer for new certificates, and warns that traffic from app versions retaining older SDKs will fail after expiration. This historical warning appears on an iOS v7-routed page and does not establish the current support status of any exact SDK package.

## Evidence boundaries

> [!warning] Captured sample is not copy-ready
> The Swift snippet declares `let request = BTLocalPaymentRequest(...)` and assigns its delegate, but then calls `localPaymentClient.start(localPaymentRequest)` even though `localPaymentRequest` is not defined in the captured snippet. Do not copy this invocation unchanged or treat it as successful execution evidence. The omitted result body also cannot establish a returned nonce, authorization, completion, settlement or funding.

> [!warning] Unresolved same-date currency conflict
> The supporting umbrella article says Local Payment Method transactions are automatically presented to customers in euros, while the primary iOS method table supplies PLN for BLIK, SGD for grabpay, GBP for UK SOFORT, and EUR or PLN for P24. Do not harmonize these claims or infer which is current; use the exact method-specific implementation row and verify applicable current product authority.

> [!warning] Webhook and Payment Context GraphQL tension
> The primary page states that webhooks must be implemented, while the supporting Node page calls the Payment Context GraphQL API an alternative to webhooks. The Node page also separately describes both client-returned and webhook-returned nonce routes, a three-hour auto-refund and `local_payment_reversed`; do not infer that GraphQL replaces every completed or reversed webhook responsibility.

> [!warning] Lifecycle and environment scope
> Client initiation, the omitted result callback and server notifications are distinct from authorization, completion, settlement, funding and reversal outcomes. The page does not classify every listed method as instant or non-instant, and its placeholder client authorization plus captured examples do not prove sandbox or production execution.

> [!warning] Shipping-data scope
> `shippingAddressRequired` is conditional on shipping physical goods. The guide says `true` prompts for shipping details, while the default `false` prompts for basic customer information; data already collected can instead be passed in the request. These prompt descriptions are not payment-result guarantees.

## Detail locators

- Historical mobile SDK certificate-expiration notice and stated traffic consequence: primary iOS raw, `# Client-Side Implementation`, lines 17-20.
- Merchant-account selection, credential role and no-switch lifecycle condition: primary iOS raw, `### Determine which merchant account to use`, lines 28-30.
- CocoaPods, Swift Package Manager and Carthage module lists: primary iOS raw, `### Get the SDK`, lines 33-53.
- Custom UI purpose and per-method `paymentType`, country and currency table: primary iOS raw, `### Invoke payment flow`, lines 56-73.
- `paymentTypeCountryCode` fallback rule: primary iOS raw, `### Invoke payment flow`, line 74.
- Required-parameter and minimum-limit table: primary iOS raw, `### Invoke payment flow`, lines 76-88.
- Client initialization, request construction, the `request` versus undefined `localPaymentRequest` mismatch, omitted result body and delegate callback: primary iOS raw, `### Invoke payment flow`, lines 90-138, especially lines 116-129.
- Webhook requirement: primary iOS raw, `### Invoke payment flow`, lines 140-141.
- Conditional shipping-address collection and default basic-information behavior: primary iOS raw, `### Shipping addresses`, lines 146-150.
- Eligible-merchant and PayPal-integration prerequisite plus euro-presentment statement: supporting umbrella article raw, `## Availability`, lines 19-21; valid PayPal Business Account setup: `## Setup`, lines 29-31.
- Customer-return/no-return paths, three-hour auto-refund and reversal webhook: supporting Node raw, `## Local Payment Method webhooks`, lines 21-31; two nonce routes: `## Creating transactions`, lines 54-59.
- Payment Context update and GraphQL-alternative wording: supporting Node raw, `## Payment Contexts`, lines 124-130.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Native SDK route: [[braintree-ios-sdk]]
- Umbrella article prerequisites and lifecycle owner: [[source-braintree-payment-methods-local-payment-methods]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/client-side-custom/ios/v7-2026-09-16|Braintree Local Payment Methods Custom Client-Side Implementation — iOS v7 (captured 2026-09-16)]] — primary platform/version guide.
- [[raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16|Braintree Local Payment Methods article (captured 2026-09-16)]] — fully read supporting authority for eligibility, PayPal setup and the conflicting umbrella currency statement.
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Braintree Local Payment Methods Server-Side Implementation — Node.js (captured 2026-09-16)]] — fully read supporting authority for return/no-return handling, nonce routes, auto-refund, reversal notification and the Payment Context GraphQL tension.
