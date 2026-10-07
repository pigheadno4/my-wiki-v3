---
title: "Braintree Package Tracking Client-Side Configuration"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/package-tracking/client-side"
raw_files:
  - "braintree/docs/guides/package-tracking/client-side-2026-09-16.md"
tags: [braintree, package-tracking, paypal, client-sdk, line-items]
---

## Overview

This collected Braintree package-tracking client-side guide provides JavaScript, Swift and Kotlin examples for placing PayPal order line-item metadata into the client integration used to create user approval. Its consequential handoff rule says line-item information may be omitted from the server integration only when it was already submitted through the Client SDK integration and has not changed.

This is a 2026-09-16 unversioned website snapshot. It does not identify exact client-SDK package versions, mobile OS or language runtime versions, a server SDK, or an execution environment; the page also says its code is incomplete. It is therefore not current-support, end-to-end order, user-approval, server-acceptance, package-tracking, fulfillment or payment-outcome proof.

## Key takeaways

- The JavaScript example selects PayPal funding and calls `paypalCheckoutInstance.createPayment()` with checkout flow, amount, currency, capture intent, shipping-address settings and a line item. The line item illustrates UPC code/type, product URL and image URL in addition to quantity, amount, name and debit kind; exact example values and matching comments remain at the raw locator.
- The Swift example creates `BTPayPalCheckoutRequest` and `BTPayPalLineItem` values, then assigns an image URL. The Kotlin example creates `PayPalCheckoutRequest` and `PayPalLineItem` values and assigns the item list to the request; it illustrates image and UPC fields. These platform snippets do not establish identical field coverage or compatibility across SDKs.
- The permission to omit server-side line items is conditional on the Client SDK integration having already submitted them with no changes. The page does not say that all client data, changed line items, product/order state, or the later package-tracking request may be omitted.

> [!warning] Treat the snippets as scoped examples
> The page expressly says the displayed code is not the entire integration. Preserve the PayPal, client-side, user-approval and line-item scope; use the linked package-tracking overview and server-side guide for their separate lifecycle stages rather than treating these snippets as the tracking submission itself.

## Detail locators

- Client-integration purpose and use with a server integration for creating user approval: raw line 16.
- Unchanged-line-item condition for omitting line items from the server integration, plus the incomplete-integration warning and JavaScript v3 guide route: raw lines 17-18.
- JavaScript PayPal checkout request and line-item fields: `### javascript`, raw lines 21-45.
- Swift request, line item and image URL example: `### swift`, raw lines 47-52.
- Kotlin request, line item, image/UPC fields and request assignment: `### kotlin`, raw lines 54-72.
- Next-page navigation to a server-side Java route: raw line 73; this label is navigation, not behavioral evidence for that unread target.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Package-tracking lifecycle, eligibility and SDK-prerequisite context: [[source-braintree-docs-guides-package-tracking-overview]]
- Separate Node.js server-side example route: [[source-braintree-docs-guides-package-tracking-server-side-node]]

## Raw Sources

- [[raw/braintree/docs/guides/package-tracking/client-side-2026-09-16|Braintree package-tracking client-side configuration]] - complete collected snapshot of the client-side line-item examples and conditional client/server handoff note
