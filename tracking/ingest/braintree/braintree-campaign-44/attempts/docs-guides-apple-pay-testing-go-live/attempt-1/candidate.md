---
title: "Braintree Apple Pay Testing and Go Live"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/apple-pay/testing-go-live"
raw_files:
  - "braintree/docs/guides/apple-pay/testing-go-live-2026-09-16.md"
tags: [braintree, apple-pay, testing, sandbox, production]
---

## Overview

This 2026-09-16 snapshot of an unversioned [[braintree]] guide covers testing and go-live checks for [[braintree-apple-pay]] across device, web, sandbox, development troubleshooting, and production contexts. It is not exact-version SDK evidence and does not by itself prove current eligibility, environment configuration, or payment execution.

## Key takeaways

- To test the entire Apple Pay flow, the page requires an Apple Pay-capable device; for web testing, it names Safari or Chrome.
- In Braintree's sandbox, Apple Pay Sandbox test cards require the device to be signed into an iCloud sandbox tester account. The returned payment-method nonce contains dummy "Jane Doe" data even after successful decryption, while separate test amounts and test nonces can simulate server behavior.
- In production, the page says Braintree decrypts payment data using an Apple Pay certificate stored on its servers and says the device account number (DPAN) should match between Wallet and the Braintree Control Panel. During development, it identifies certificate mismatch as a likely cause of tokenization failure and routes certificate identification to the token `publicKeyHash` field, with separate iOS and web token objects.
- The go-live checklist tells the merchant to run a few real transactions covering all supported card types. It notes that Apple Pay requires coordination among acquiring banks, issuing banks, and card networks, and directs the merchant to email Braintree if live transactions are declined.

> [!warning] Live transaction boundary
> The real-transaction step is captured provider guidance, not authorization to initiate payments. Its result is merchant-, environment-, card-, device-, and time-dependent, and this source does not establish a transaction budget or successful processing.

## Detail locators

- Full-flow device condition and Safari/Chrome web-testing statement: raw line 16.
- Sandbox cards, iCloud sandbox tester account, dummy nonce data, and server-behavior simulation routes: raw line 18.
- Production certificate custody and Wallet/Control Panel DPAN expectation: raw line 20.
- Development certificate-mismatch diagnosis and platform-specific `publicKeyHash` token routes: raw line 22.
- Real-transaction go-live check and decline-coordination note: `## Go live`, raw lines 23–27.

## Related

- [[braintree]]
- [[braintree-apple-pay]]

## Raw Sources

- [[raw/braintree/docs/guides/apple-pay/testing-go-live-2026-09-16|Braintree Apple Pay Testing and Go Live (2026-09-16 snapshot)]]
