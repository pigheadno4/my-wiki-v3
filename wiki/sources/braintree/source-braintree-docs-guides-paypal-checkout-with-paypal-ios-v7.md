---
title: "Braintree PayPal One-Time Payments for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/checkout-with-paypal/ios/v7"
raw_files:
  - "braintree/docs/guides/paypal/checkout-with-paypal/ios/v7-2026-09-16.md"
tags: [braintree, paypal, ios, one-time-payments, checkout, tokenization]
---

## Overview

This captured Braintree website guide is the iOS v7 route for PayPal One-time Payments. It describes constructing a `BTPayPalCheckoutRequest` with a required transaction amount and passing it to `BTPayPalClient.tokenize`; the completion can return a tokenized PayPal account with a payment-method nonce, an error, or buyer cancellation. The page's successful client branch exposes a nonce but does not show transaction creation, authorization, capture, settlement or funding.

This is a 2026-09-16 website snapshot for [[braintree]] and [[braintree-ios-sdk]]. It is not current package-qualified SDK or GitHub implementation evidence, a direct PayPal integration guide, merchant or buyer eligibility proof, or successful payment execution.

## Key takeaways

- The page presents PayPal One-time Payments as a checkout shortcut that can be placed at different points in the shopping journey. Its iOS example initializes `BTPayPalClient`, creates `BTPayPalCheckoutRequest` with an amount, and tokenizes the request; the sample amount, currency and returned account fields are examples rather than guarantees or a complete transaction procedure.
- The captured warning says Braintree Mobile SDK SSL certificates expire on March 30, 2026, directs iOS SDK 6.17.0 or newer for new certificates, and warns that traffic from app versions retaining older SDKs will fail after that date. This is a historical notice embedded in an iOS v7-routed page, not proof of current support or of the status of any exact SDK package.
- The Contact Module is stated as US-only in this snapshot. Contact visibility/editability, Shipping Module callbacks, line-item display, buyer-identifier prefilling, and the Pay Now versus Continue choices are optional or conditional customizations; use the raw locators below for their exact request details and conditions.
- The guide says Continue is for a final amount that will change after the payer returns to the merchant site and limits the return path to no more than one additional completion page. It contrasts this with Pay Now, where the payer completes on the PayPal review page before returning to the merchant site.
- The App Switch section says merchants need a redirect-flow integration that can switch to the PayPal app or redirect in the same browser tab. However, its implementation link targets an iOS v6 App Switch guide. That unread target is navigation only and does not establish iOS v7 App Switch API behavior, availability or package support.

## Evidence boundaries

> [!warning] Historical certificate notice
> Preserve the warning's stated March 30, 2026 date, iOS 6.17.0+ remediation and consequence for app versions retaining older certificates. Because this is a captured website notice, verify current official package and lifecycle guidance before an operational decision.

> [!warning] Tokenization is not transaction completion
> The client completion returns a tokenized PayPal account nonce, an error or cancellation. The page does not show a transaction call, so the client result does not prove authorization, capture, settlement or funding.

> [!warning] Platform and version scope
> This source is the exact website iOS v7 route. Do not import behavior from sibling Android or JavaScript guides, direct PayPal products, separately retained GitHub SDK evidence, or the linked but unread iOS v6 App Switch guide.

## Detail locators

- Product purpose and possible checkout-button placement: `# One-time Payments`, raw line 24.
- Historical mobile SSL-certificate expiry, stated iOS 6.17.0+ remediation and traffic-failure consequence: `# One-time Payments` IMPORTANT, raw lines 17-20.
- Required amount, `BTPayPalClient`, `BTPayPalCheckoutRequest`, tokenization completion and nonce/error/cancellation branches: `## Invoking the One-time Payments flow`, raw lines 27-69.
- Customization inventory: `## Customizing One-time Payments`, raw lines 71-82.
- Contact Module purpose, US-only qualification, visibility/editability choices and request example: `### Integrating Contact Module`, raw lines 84-131.
- Shipping Module buyer changes, merchant callback response and request example: `### Integrating Shipping Module`, raw lines 133-148.
- Line-item presentation surfaces and example: `### Integrating Pass Line-item Details`, raw lines 150-168.
- Buyer identifier prefilling and request example: `### Integrating Pass Buyer Identifier`, raw lines 170-187.
- Pay Now and Continue meanings, placement guidance and changing-final-amount condition: `### Integrating Pay Now or Continue`, raw lines 189-211.
- Redirect-flow description and iOS v6 implementation-guide link: `### Integrating App Switch`, raw lines 213-232.
- Optional shipping-address collection and separate server-side `Transaction.Sale` route: `## Shipping address`, raw lines 235-237.
- Snapshot country-support statement: `## Country support`, raw lines 240-242.
- Currency-presentment statement and separate server-side charging route: `## Currency presentment`, raw lines 245-249.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-ios-sdk]]
- Provider-level payment-method route: [[braintree-payment-methods]]
- PayPal method orientation: [[source-braintree-payment-methods-paypal-overview]]

## Related raw API references

The captured page points to request options, server-side shipping and currency guidance, and an iOS v6 App Switch integration guide. Those linked targets are navigation only here and were not used as behavioral evidence for this iOS v7 retrieval entry.

## Raw Sources

- [[raw/braintree/docs/guides/paypal/checkout-with-paypal/ios/v7-2026-09-16|Braintree PayPal One-Time Payments — iOS v7 (captured 2026-09-16)]]
