---
title: "Braintree Venmo Client-Side Implementation (Android v5)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/venmo/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/venmo/client-side/android/v5-2026-09-16.md"
tags: [braintree, venmo, android, client-sdk, tokenization]
---

## Overview

This collected Braintree Android v5 client-side guide covers two Venmo integration shapes: SDK-managed Payment Buttons and a custom request/launcher/return/tokenization flow. Both produce a Venmo payment-method nonce for a separate merchant-server path; setup, launch, callback handling or nonce creation is not proof of a transaction, authorization, settlement or funding.

The page requires the merchant to satisfy the linked Venmo eligibility guidance and enable Venmo in the Braintree Sandbox before testing or going live. Those instructions are snapshot-scoped prerequisites, not evidence of current availability, production approval, merchant enablement or buyer eligibility.

## Key takeaways

- The Payment Buttons module is described as launching Venmo authentication and tokenizing the result. In the XML/Fragment example, the merchant stores a started pending request and calls `handleReturnToApp` after control returns; the Compose button instead handles that return call inside the SDK. Examples use a tokenization key or client token, app-link return URL and deep-link fallback scheme, but do not establish current package compatibility or a completed payment.
- In the custom flow, the client creates a payment-authorization request, launches it, persists the resulting pending request, handles the returned intent, and tokenizes a successful authorization result. Success returns a nonce for server processing; failure and cancellation are separate callback results. The launcher is initialized in `onCreate`, while return handling differs for `singleTop` and other Activity launch modes.
- Every `VenmoRequest` must identify `MULTI_USE` or `SINGLE_USE`. That choice changes the customer-facing consent language and connected-business behavior. `SINGLE_USE` does not permit vaulting: Vault creation attempts return a validation error, and transaction vault flags do not vault the nonce even though the page says the transaction is processed normally.
- Custom integrations must present order summaries before and after purchase with the page's specified fields. The page warns that noncompliance can interrupt Venmo service and separately routes merchants to Venmo brand guidelines.
- The page assigns device-data collection to the client before each transaction and sends the nonce plus device data to the merchant server, which supplies it when creating the Venmo transaction. It advises collecting close to transaction creation to help reduce declines; this is not transaction, fraud-decision or settlement proof.

> [!warning] Historical certificate notice
> This 2026-09-16 snapshot says Braintree Mobile SDK certificates were set to expire on March 30, 2026, directs Android users to version 4.45.0+ or 5.0.0+, and warns that traffic from retained older app versions would fail. The stated date had already passed when the page was collected. Treat this as historical page evidence, not confirmation of current certificate state, one current dependency version, or actual traffic failure.

> [!warning] Purchase, Vault and profile boundaries
> For multiple onboarded Venmo apps under one gateway, the custom integration passes the applicable `profile_id` in both the client flow and server-side transaction creation. In a purchase context, `totalAmount` is required and shown on the paysheet; it may be omitted for vault-only tokenization. These request/setup conditions do not establish that a profile is enabled, consent was obtained, a nonce was accepted by the server, or any transaction succeeded.

## Detail locators

- Historical mobile-certificate date, Android upgrade floors and stated traffic consequence: `# Client-Side Implementation > IMPORTANT`, raw line 18.
- Payment Buttons choices, SDK-managed role and eligibility/Sandbox prerequisite: `## Choose an integration method` through `#### Get Buttons Module`, raw lines 23-40.
- XML/Fragment button initialization, pending-request launch callback and return-result handling: `#### Get Buttons Module`, raw lines 42-115.
- Compose button's SDK-managed return handling and tokenize callback: `#### Get Buttons Module > Jetpack Compose`, raw lines 138-173.
- Custom-integration order-summary fields, interruption warning and brand route: `Custom integration`, raw lines 174-203.
- Custom module dependency examples and request/launcher/return/tokenization sequence: `#### Get the SDK` through `#### Invoking the Venmo flow`, raw lines 208-335.
- `MULTI_USE` versus `SINGLE_USE` consent, connected-business and vaulting consequences: `#### Payment method usage`, raw lines 343-365.
- Multiple-profile client/server `profile_id` duties: `### Multiple profiles`, raw lines 387-395.
- Per-transaction device-data collection and server handoff: `## Collect device data`, raw lines 400-422.
- Address flags, Enriched Customer Data prerequisite and nonce-return fields: `## Shipping and Billing Address collection`, raw lines 427-493.
- Purchase-context amount requirement, optional line items and displayed validations: `## Amounts and Line Items`, raw lines 495-560.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-android-sdk]]
- Venmo availability and merchant setup boundary: [[source-braintree-payment-methods-venmo]]

## Related raw API references

- [[raw/braintree/docs/guides/venmo/server-side/node-2026-09-16|Braintree Venmo server-side Node.js guide]] - linked next-page family navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/venmo/client-side/android/v5-2026-09-16|Braintree Venmo client-side implementation (Android v5)]] - complete collected snapshot for Payment Buttons, custom launch/return/tokenization, usage-scoped consent and vaulting, compliance, device-data and request-field conditions
