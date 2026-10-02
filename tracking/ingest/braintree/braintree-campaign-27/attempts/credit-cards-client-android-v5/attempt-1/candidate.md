---
title: "Braintree Credit Cards: Android v5 Standard Client-Side Implementation"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/credit-cards/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/credit-cards/client-side/android/v5-2026-09-16.md"
tags: [braintree, android-sdk, credit-cards, card-fields, tokenization, payment-method-nonce]
---

## Overview

This Android v5 [[braintree]] website-guide snapshot, collected 2026-09-16, documents the standard client-side Card Fields integration. The component collects and tokenizes card number, expiration date and CVV data; the merchant app supplies the surrounding checkout UI and pay button, then sends the returned payment-method nonce to its server to complete the transaction.

## Key takeaways

- Card Fields provides the three card fields with formatting, validation, brand detection and tokenization. The merchant app remains responsible for non-card fields such as name or billing address and for its own pay button.
- The guide requires base Braintree Android SDK setup and a tokenization key or client token. Its `ui-components` dependency requires Braintree Android SDK 5.29.0 or higher, and Card Fields is initialized with that authorization before accepting card input. The page's recommendation to use the latest SDK is historical snapshot guidance, not evidence of the current release.
- The app listens for form-validity changes, enables its own pay button, registers a result callback and calls `submit()`. A successful result contains a nonce for server-side transaction creation; tokenization or nonce receipt alone does not prove authorization, settlement or funding.
- The page directs merchants to test in sandbox before going live. This retained documentation snapshot records the instruction only; no app build, sandbox submission, transaction or production-readiness test was performed.

## Evidence limitations

This version-qualified website snapshot does not establish current Android SDK support, dependency availability, merchant enablement, buyer or card eligibility, or parity with the separately retained exact-SHA GitHub baseline. Its examples and verification prompts are documentation, not evidence that an integration or payment was executed successfully.

## Detail locators

- Card Fields purpose, managed fields, validation and nonce-to-server outcome: `# Standard Client-Side Implementation`, line 16.
- Base SDK, client-authorization and merchant-owned UI prerequisites: `## Before you begin`, lines 23-28.
- `ui-components` dependency and Android SDK 5.29.0-or-higher qualification: `## Add the Card Fields dependency`, lines 31-49.
- Authorization passed to `initialize`: `## Initialize Card Fields`, lines 76-98.
- Form-validity listener and merchant-owned pay-button behavior: `## Enable your pay button when the form is valid`, lines 101-114.
- Success/failure callback and nonce handoff: `## Handle the tokenization result`, lines 117-137.
- Merchant button calling `submit()`: `## Trigger submission from your pay button`, lines 140-151.
- Optional supplemental cardholder name and postal-code example: `## Optional: Add supplemental card data`, lines 154-168.
- Sandbox-before-live instruction: `## Test your integration`, lines 171-173.

## Related

- Company: [[braintree]]
- Android SDK concept: [[braintree-android-sdk]]
- Payment-method concept: [[braintree-payment-methods]]
- Platform distinction: [[source-braintree-credit-cards-client-javascript-v3]]

## Related raw API references

- [[raw/braintree/docs/guides/client-sdk/setup/android/v5-2026-09-16|Braintree Android v5 client SDK setup]] - prerequisite navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/authorization/overview-2026-09-16|Braintree client authorization overview]] - authorization navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/credit-cards/server-side/node-2026-09-16|Braintree Node server-side credit-card guide]] - server-side navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/credit-cards/testing-go-live/node-2026-09-16|Braintree Node credit-card testing and go-live guide]] - testing navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/credit-cards/client-side/android/v5-2026-09-16|Braintree Android v5 standard client-side credit-card implementation]] - fully read pinned website snapshot covering Card Fields responsibilities, prerequisites, tokenization and nonce handoff
