---
title: "Braintree Amex Express Checkout Testing and Go Live"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/amex-express-checkout/testing-go-live"
raw_files:
  - "braintree/docs/guides/amex-express-checkout/testing-go-live-2026-09-16.md"
tags: [braintree, amex-express-checkout, sandbox-testing, go-live, javascript]
---

## Overview

This 2026-09-16 unversioned Braintree website snapshot is a testing-and-go-live guide for the legacy Amex Express Checkout product: it gives Sandbox fixtures and a JavaScript `amex:init` environment switch for moving from `qa` to `production`. The page also says Amex Express Checkout was replaced by Visa Secure Remote Commerce (SRC), so the retained actions are historical product instructions rather than evidence of current Amex Express Checkout or SRC availability, exact SDK/runtime behavior, Production enablement, or successful payment processing.

## Key takeaways

- For Sandbox testing, the page says American Express sends card details to Braintree for secure server-side storage and instructs the merchant to set the JavaScript `env` parameter on `amex:init` to `qa`; the listed test-account values remain in the raw source.
- As an alternative Sandbox fixture, the page provides the test nonce `fake-amex-express-checkout-nonce`. A fixture or Sandbox transaction is not Production evidence.
- Its go-live checklist says to change the same `env` parameter from `qa` to `production` and, if possible, test with a real American Express account. The page supplies no exact Amex Express Checkout SDK/package version, account-enablement step, acceptance criterion, transaction result, settlement result, or funding result.

## Availability and migration warning

> [!warning] Unresolved product-status and successor conflict
> This page says Amex Express Checkout was replaced by SRC while still presenting legacy Sandbox and go-live steps. A related overview in the same 2026-09-16 capture also calls Amex Express Checkout currently available under qualified merchant/cardmember conditions, and the retained SRC authority says Click to Pay/SRC would no longer be supported effective January 20, 2026 even though that authority also describes SRC as a current limited release. Preserve these statements without treating the legacy `qa`-to-`production` action as a currently executable migration or availability guarantee. See [[source-braintree-docs-guides-amex-express-checkout-overview]] and [[source-braintree-payment-methods-secure-remote-commerce]].

The replacement notice further limits SRC to eligible merchants, says its API is subject to change, names Android v2, iOS v4 and JavaScript v3 as the Client SDK generations in which SRC was introduced, and directs merchants to request access. Those SRC version labels do not version the legacy Amex Express Checkout JavaScript instructions on this page.

## Detail locators

- Amex Express Checkout replacement direction, SRC limited-release eligibility, API-change warning, Client SDK generation labels and access request: opening `AVAILABILITY`, raw lines 17-18.
- Sandbox card-handling description, test-account route and `amex:init` `env=qa` instruction: `## Sandbox Testing`, raw lines 21-30.
- Sandbox test nonce: raw lines 32-33.
- Go-live environment switch and qualified real-account test instruction: `## Go live`, raw lines 34-38.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Legacy product overview and same-snapshot availability tension: [[source-braintree-docs-guides-amex-express-checkout-overview]]
- Separate SRC support-status authority: [[source-braintree-payment-methods-secure-remote-commerce]]

## Raw Sources

- [[raw/braintree/docs/guides/amex-express-checkout/testing-go-live-2026-09-16|Braintree Amex Express Checkout Testing and Go Live — fetched 2026-09-16]]
