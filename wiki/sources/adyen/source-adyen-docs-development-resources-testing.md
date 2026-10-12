---
title: "Testing your online payments integration"
type: source
date_ingested: 2026-10-11
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/testing"
raw_files:
  - "adyen/docs/development-resources/testing/2026-09-15.md"
tags: [adyen, testing, online-payments, webhooks]
---

## Overview

This [[adyen]] documentation page is a testing hub for troubleshooting an online-payments integration before it goes live. It frames testing across the client-side application, server-side integration, and webhook server, and routes narrower guides through [[adyen-payment-testing]].

## Key takeaways

- Adyen recommends testing the full client-side and server-side integration in the test environment before accepting live payments.
- The documented prerequisites are test API and client keys, a test Customer Area configured with the functionality intended for go-live, a built online-payments integration, and a webhook server able to receive test webhooks.
- The guide says to use test credentials for the transaction types the integration handles, test every payment method that will be offered, and test each method with every `countryCode` for shopper countries or regions the integration will accept.
- Its card example is explicitly illustrative: submit a test card from the client-side test environment, then check that the server makes the corresponding request and the webhook server receives the corresponding webhook. It is not a guarantee of a particular result.
- The hub routes to focused testing documentation for payments and modifications, tokenization, risk features, 3D Secure 2 authentication, and result codes. Those child pages provide navigation here; their detailed behavior is not established by this source.

> [!warning] Snapshot and test-evidence boundary
> This dated documentation snapshot describes recommended testing and test-environment setup. It does not prove current production availability, merchant or payment-method eligibility, successful live authorization or settlement, or that any particular test completed successfully.

## Detail locators

- `## Requirements`, lines 21–26 — test keys, test Customer Area configuration, integration build, and webhook-server setup.
- `## Test your integration`, lines 28–32 — transaction, payment-method, and accepted-country coverage plus the client/server/webhook example.
- `## Test your integration`, lines 34–62 — navigation cards for payments and modifications, tokenization, risk features, 3D Secure 2 authentication, and result codes.
- `## See also`, lines 64–66 — test cards and credentials route.

## Related

- Company: [[adyen]]
- Concept: [[adyen-payment-testing]]

## Related raw API references

Navigation only; these child snapshots were not read as behavioral evidence for this entry.

- [[raw/adyen/docs/development-resources/testing/payments-and-modifications/2026-09-15|Payments and modifications testing]]
- [[raw/adyen/docs/development-resources/testing/tokenization/2026-09-15|Tokenization testing]]
- [[raw/adyen/docs/development-resources/testing/risk-features/2026-09-15|Risk-features testing]]
- [[raw/adyen/docs/development-resources/testing/3d-secure-2-authentication/2026-09-15|3D Secure 2 authentication testing]]
- [[raw/adyen/docs/development-resources/testing/result-codes/2026-09-15|Result-code testing]]

## Raw Sources

- [[raw/adyen/docs/development-resources/testing/2026-09-15|2026-09-15 snapshot — Testing your online payments integration]]
