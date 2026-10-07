---
title: "Braintree JavaScript v2 Credit Cards Client Reference"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/credit-cards"
raw_files:
  - "braintree/docs/reference/client-reference/javascript/v2/credit-cards-2026-09-16.md"
tags: [braintree, credit-cards, javascript-v2, client-reference, tokenization, 3d-secure]
---

## Overview

This collected [[braintree]] website snapshot is the JavaScript v2 client reference for lower-level credit-card tokenization and limited 3D Secure UI options. It documents browser-side nonce creation and UI callbacks for [[braintree-web-sdk]]; it does not establish current SDK support or deprecation status, PCI certification, server-side transaction processing, authorization, settlement, or a successful payment.

## Key takeaways

- For custom form behavior such as merchant-owned submit callbacks or validation, the page recommends creating a Braintree client and calling `client.tokenizeCard(...)`; its example sends the resulting nonce to the merchant server. The example is a client handoff pattern, not evidence that a server processed a transaction.
- The page states that payment fields cannot be hosted on the merchant checkout page for eligibility for the easiest PCI compliance level, SAQ A, and points to Hosted Fields as the hosted approach. This is page-specific integration framing, not a PCI certification or general compliance determination.
- Payment-method nonces are stated to expire after three hours. A nonce may still be created when inputs are empty or invalid, while a failed `tokenizeCard` call that returns no nonce yields the string `Unable to tokenize card.`; the page says gateway unreachability is one possible cause.
- Drop-in and Hosted Fields are described as handling validation and card-type detection, but a custom credit-card integration must perform client-side validation and present suitable UI. Routine tokenization fields and the sample values remain in the raw snapshot.
- The 3D Secure section documents `useDefaultLoader`, `onLookupComplete`, and `onUserClose`. `onLookupComplete` occurs after a successful lookup and before the authorization modal, while `onUserClose` follows a user-initiated modal close; neither callback is payment-success evidence.
- The page is explicitly scoped to JavaScript v2 but does not state that version's current support or deprecation status. Consult separately retained lifecycle or migration evidence before making a current-SDK recommendation.

## Detail locators

- `Credit card direct tokenization` lines 17-21: SAQ A field-hosting statement and Hosted Fields navigation.
- `Tokenize card` lines 24-41: lower-level client tokenization example, merchant-server nonce handoff comment and three-hour nonce lifetime.
- `Options` lines 44-74: tokenization option example, nonce creation despite input-validation issues and no-nonce error behavior.
- `Client-side validation` lines 77-85: Drop-in/Hosted Fields validation comparison and custom-integration responsibility.
- `3D Secure UI options` lines 88-106: `verify3DS` example and loader, lookup-complete and user-close callback semantics.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/client-reference/javascript/v2/credit-cards-2026-09-16|Braintree JavaScript v2 Credit Cards client-reference snapshot (2026-09-16)]]
