---
title: "Braintree Local Payment Methods Custom Client-Side Implementation for iOS v7"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/client-side-custom/ios/v7"
raw_files:
  - "braintree/docs/guides/local-payment-methods/client-side-custom/ios/v7-2026-09-16.md"
tags: [braintree, local-payment-methods, ios, swift, custom-ui, webhooks]
---

## Overview

This captured Braintree developer guide describes a custom Local Payment Methods client flow for iOS v7. The merchant selects a transaction-consistent merchant account, adds the Local Payment SDK modules, constructs a method-specific `BTLocalPaymentRequest`, and starts `BTLocalPaymentClient`, which the page says launches an `ASWebAuthenticationSession`. It is a platform/version-routed website snapshot for [[braintree]], [[braintree-payment-methods]] and [[braintree-ios-sdk]], not current SDK-package evidence or proof of merchant eligibility, buyer eligibility, payment authorization, completion, settlement or funding.

## Key takeaways

- The merchant account determines the PayPal credentials used for the transaction. The guide requires the same merchant account across other calls in that transaction lifecycle and says it cannot be switched between the start and finish of a Local Payment transaction.
- The page permits merchant-owned custom UI and gives an iDEAL button as its example. Its captured tables map named Local Payment Methods to `paymentType`, country and currency values, required request parameters and some minimum transaction amounts; those combinations are method-specific rather than evidence of uniform availability or timing.
- The client example initializes `BTLocalPaymentClient`, creates a `BTLocalPaymentRequest`, assigns a flow delegate and calls `start()`. A delegate callback allows preprocessing before invoking its supplied `start` closure. The example callback body is omitted, so this snapshot does not establish a nonce or any completed server-side transaction.
- The guide says Braintree webhooks must be implemented to accept Local Payment Methods. A webhook is a server-side notification prerequisite; receiving one is not by itself proof of settlement or funding. The linked server-side guide remains separate evidence.
- The captured warning says older Braintree Mobile SDK certificates expire on March 30, 2026, directs iOS SDK 6.17.0 or newer for new certificates, and warns that traffic from app versions retaining older SDKs will fail after expiration. This historical warning appears on an iOS v7-routed page and does not establish the current support status of any exact SDK package.

## Evidence boundaries

> [!warning] Lifecycle and environment scope
> Client initiation, the omitted result callback and webhook notifications are distinct from authorization, completion, settlement, funding and reversal outcomes. The page does not classify every listed method as instant or non-instant, and its placeholder client authorization plus captured examples do not prove sandbox or production execution.

> [!warning] Shipping-data scope
> `shippingAddressRequired` is conditional on shipping physical goods. The guide says `true` prompts for shipping details, while the default `false` prompts for basic customer information; data already collected can instead be passed in the request. These prompt descriptions are not payment-result guarantees.

## Detail locators

- Historical mobile SDK certificate-expiration notice and stated traffic consequence: `# Client-Side Implementation`, lines 17-20.
- Merchant-account selection, credential role and no-switch lifecycle condition: `### Determine which merchant account to use`, lines 28-30.
- CocoaPods, Swift Package Manager and Carthage module lists: `### Get the SDK`, lines 33-53.
- Custom UI purpose and per-method `paymentType`, country and currency table: `### Invoke payment flow`, lines 56-73.
- `paymentTypeCountryCode` fallback rule: `### Invoke payment flow`, line 74.
- Required-parameter and minimum-limit table: `### Invoke payment flow`, lines 76-88.
- `BTLocalPaymentClient`, `BTLocalPaymentRequest`, request fields, delegate and `ASWebAuthenticationSession` example: `### Invoke payment flow`, lines 90-138.
- Webhook prerequisite and separate server-side route: `### Invoke payment flow`, lines 140-141.
- Conditional shipping-address collection and default basic-information behavior: `### Shipping addresses`, lines 146-150.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Native SDK route: [[braintree-ios-sdk]]
- Existing article owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Braintree Local Payment Methods Server-Side Implementation — Node.js (captured 2026-09-16)]] — the client page links to server-side processing and webhook documentation; this target is navigation only here and was not used as behavioral evidence.

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/client-side-custom/ios/v7-2026-09-16|Braintree Local Payment Methods Custom Client-Side Implementation — iOS v7 (captured 2026-09-16)]]
