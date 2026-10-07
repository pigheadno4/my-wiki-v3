---
title: "Braintree Hipercard and Hiper Testing"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/hipercard-and-hiper/testing"
raw_files:
  - "braintree/docs/guides/hipercard-and-hiper/testing-2026-09-16.md"
tags: [braintree, hipercard, hiper, sandbox, testing, cards]
---

## Overview

This captured unversioned [[braintree|Braintree]] webpage is a Sandbox test-card fixture reference for Hipercard and Hiper. It says both methods are in limited release for select merchants and directs readers to request access. The snapshot does not establish current support or merchant enablement, identify a client or server SDK/version, provide GitHub implementation or history evidence, apply the fixtures to Production, or prove payment execution. [[braintree-payment-methods]]

## Key takeaways

- When testing the integration in the Sandbox environment, the page provides one Hipercard credit-card fixture and one Hiper credit-card fixture.
- The exact test values remain in the verified raw locator rather than being copied into this retrieval page.

> [!warning] Environment and access boundary
> Use these values only as the captured Sandbox fixtures under the page's limited-release/select-merchant condition. They are not Production card data, current availability or account-enablement proof, and a test input alone is not evidence of a successful payment.

## Detail locators

- **Limited-release/select-merchant condition and access-request route:** `AVAILABILITY`, raw lines 17-18.
- **Hipercard and Hiper Sandbox credit-card test values:** `## Test card numbers`, raw lines 21-27.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Brazil-path accepted-method scope: [[source-braintree-articles-br-transactions-accepted-payment-methods]]
- General card-testing route: [[source-braintree-credit-cards-testing-go-live-node]]

## Raw Sources

- [[raw/braintree/docs/guides/hipercard-and-hiper/testing-2026-09-16|Braintree Hipercard and Hiper Testing (2026-09-16 snapshot)]]
