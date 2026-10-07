---
title: "Braintree Payment Request Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/payment-request/overview"
raw_files:
  - "braintree/docs/guides/payment-request/overview-2026-09-16.md"
tags: [braintree, payment-request, javascript, browser, google-pay]
---

## Overview

Braintree-hosted overview of the browser Payment Request API and Braintree's JavaScript v3 Payment Request component. It describes a browser-provided payment-selection window for supported browsers, positions the component as an alternative or addition to Hosted Fields, and provides a snapshot browser/payment-method matrix. This fetched page does not document merchant-server transaction creation or environment behavior, and its dated statements do not establish current browser support, merchant enablement, exact SDK-package behavior, successful payment execution, or PCI certification. See [[braintree]] and [[braintree-web-sdk]].

## Key takeaways

- The page states that the Payment Request API is available through Braintree's JavaScript v3 SDK. It describes the underlying API as a W3C standard candidate that lets customers using supported browsers open a browser-provided window and select a saved payment method or enter a new one instead of completing a checkout form.
- Braintree's Payment Request component is presented as an alternative or addition to Hosted Fields. The page says card details are captured and tokenized within a Braintree iframe and are not exposed to the merchant website; its PCI-scope statement is source guidance, not independent compliance validation.
- The snapshot matrix lists credit cards for Desktop Chrome v61+ and Desktop Microsoft Edge build 14992+, and credit cards plus Google Pay for Android Chrome v61+. Treat those entries as the captured page's compatibility claims, not a current support guarantee.
- Merchants who want Google Pay without using Payment Request for ordinary card payments are directed to the separate Google Pay guide for a standalone button.

## Detail locators

- `AVAILABILITY` and the opening overview paragraph (raw lines 16–19): JavaScript v3 scope, supported-browser experience, browser-owned selection window, relationship to Hosted Fields, iframe tokenization, and the page's PCI-scope statement.
- `Supported browsers and payment methods` (raw lines 22–30): snapshot browser/version and payment-method matrix.
- `NOTE` (raw lines 32–33): standalone Google Pay button route when Payment Request is not wanted for regular card payments.

## Related

- [[braintree-web-sdk]] — modular browser SDK and version-qualified Payment Request route
- [[braintree]] — provider capsule and source catalog
- [[source-braintree-docs-guides-payment-request-setup-and-integration-javascript-v3]] — separate setup, tokenization, and merchant-server nonce-handoff guide

## Raw Sources

- [[raw/braintree/docs/guides/payment-request/overview-2026-09-16|Braintree Payment Request Overview (fetched 2026-09-16)]]
