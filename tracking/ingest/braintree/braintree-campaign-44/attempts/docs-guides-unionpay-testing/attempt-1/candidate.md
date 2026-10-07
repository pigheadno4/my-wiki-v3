---
title: "Braintree UnionPay Testing"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/unionpay/testing"
raw_files:
  - "braintree/docs/guides/unionpay/testing-2026-09-16.md"
tags: [braintree, unionpay, sandbox, testing, verification]
---

## Overview

This captured unversioned [[braintree|Braintree]] webpage is a Sandbox test-fixture reference for the dedicated UnionPay integration: it maps test card numbers to card and negative-test scenarios, then gives special field values for verification or enrollment API error cases. Its opening notice says that integration is deprecated because UnionPay can now be processed as a credit card through Discover. The snapshot does not establish that these dedicated-flow fixtures apply to the replacement credit-card path, Production, a particular client or server SDK, current merchant enablement, or an executed payment. [[braintree-payment-methods]]

## Key takeaways

- The card-number table is explicitly for testing UnionPay in the Sandbox environment. It includes debit and credit fixtures, unsupported and not-activated-online cases, a no-SMS-verification case, variable-length card numbers, and one row whose description is captured as `does not support separate****calls`; the malformed phrase is retained as a locator rather than interpreted.
- Additional error cases use special field values during verification or enrollment API calls: `smsCode` value `999999` represents an incorrect customer-entered SMS code, while an `expirationYear` or `expirationDate` before 2010 represents an expired card. These are documented simulation inputs, not a general transaction-response contract.

> [!warning] Deprecated integration boundary
> The page redirects readers from the deprecated dedicated UnionPay integration to credit-card processing through Discover, but does not say that the listed UnionPay Sandbox fixtures apply to that replacement route.

## Detail locators

- **Deprecation and Discover credit-card redirect:** `AVAILABILITY`, raw lines 17-18.
- **Sandbox card fixtures and their documented scenarios:** `## Test card numbers`, raw lines 21-36.
- **Verification and enrollment error triggers:** `## Testing other error cases`, raw lines 39-46.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- UnionPay product and processing scope: [[source-braintree-payment-methods-unionpay]]
- General card-testing route: [[source-braintree-credit-cards-testing-go-live-node]]

## Raw Sources

- [[raw/braintree/docs/guides/unionpay/testing-2026-09-16|Braintree UnionPay Testing (2026-09-16 snapshot)]]
