---
title: "Braintree SEPA Direct Debit Client-Side Implementation (JavaScript v3)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/sepa-direct-debit/client-side/javascript/v3"
raw_files:
  - "braintree/docs/guides/sepa-direct-debit/client-side/javascript/v3-2026-09-16.md"
tags: [braintree, sepa, direct-debit, javascript, client-sdk, tokenization]
---

## Overview

This 2026-09-16 Braintree website snapshot is the JavaScript v3 client-side implementation guide for SEPA Direct Debit. It covers creation of the SEPA component, customer bank-data collection and client tokenization into a nonce for a separate server-side path. It also documents an optional redirect flow that returns to the merchant page and can expose a successful tokenization payload. Component setup, a return to the page or a nonce is not proof of a debit, transaction success, settlement or funding.

The page limits SEPA Direct Debit to eligible merchants using a custom client-side integration, names Android v4.13+, iOS v5.11+ and JavaScript v3 SDK availability, excludes Drop-in and directs qualifying merchants to request account enablement for Sandbox or Production. These are snapshot-scoped statements and prerequisites, not evidence of current availability, merchant eligibility or account enablement.

## Key takeaways

- The client initializes the Braintree JavaScript v3 SDK and SEPA component with client authorization and a merchant ID. The merchant then collects the customer's bank and customer information and invokes `tokenize` from a customer action such as a button click. The returned nonce belongs to the subsequent server-side path; exact example fields and callback/Promise forms remain in the raw locators.
- The redirect flow is documented as available starting with Braintree JS SDK 3.110.0. Instead of opening the existing popup flow, it sends the user away on the current page when `redirectUrl` is passed to `braintree.sepa.create`; the page says that URL should be the same merchant page that initiated the redirect so the SDK can finish tokenization after return.
- Before using the redirect flow, the merchant must register every intended redirect domain with PayPal through the Braintree Control Panel in both Sandbox and Production. The page defines domain-name formatting rules and separate environment-specific registration steps; registration is configuration, not proof that a redirect, tokenization or payment succeeded.
- A successful redirect tokenization makes a nonce available on `sepaInstance.tokenizePayload`; the page also lists `ibanLastFour`, `customerId` and `mandateType` in that payload. Its query-parameter convention distinguishes `success=true` from a cancellation carrying `cancel=1` and `error_code=USER_DECLINED`, but those page-return signals are not evidence of a completed debit or final payment outcome.
- The redirect flow does not work with a tokenization key because of its reduced authorization. This is narrower than the page's ordinary initialization route, which allows either a tokenization key or a server-generated client token; integrations that require a tokenization key are directed to a Braintree representative.

> [!warning] Redirect authorization and environment boundary
> Do not generalize the ordinary client-authorization options to the redirect flow. The captured page specifically excludes tokenization keys from redirect use and separately requires redirect-domain registration in both Sandbox and Production.

> [!warning] Snapshot, SDK and execution boundary
> This is JavaScript v3 website guidance collected on 2026-09-16, including a redirect-flow floor of SDK 3.110.0. It is not current package-support evidence, exact commit-qualified SDK behavior, merchant enablement, buyer or bank-account eligibility, mandate acceptance, server processing, debit success, settlement or funding proof.

## Detail locators

- Eligible-merchant, custom-integration, platform/version, Drop-in exclusion and account-enablement statements: `# Client-Side Implementation > AVAILABILITY`, raw lines 17-20.
- JavaScript v3 setup and SEPA component assets: `## Installation`, raw lines 25-38.
- Client-authorization and SEPA-component initialization examples: `## Initialization`, raw lines 40-86.
- Redirect-flow SDK floor, popup rationale and current-page redirect description: `## Redirect Flow > AVAILABILITY`, raw lines 88-96.
- Dual-environment redirect-domain registration requirement and domain rules: `### Domain Registration`, raw lines 99-117; Control Panel steps continue at raw lines 120-177.
- `redirectUrl` same-page condition and callback/Promise examples: `### Code examples for redirect flow`, raw lines 182-240.
- Returned `tokenizePayload` values, redirect query parameters and tokenization-key limitation: raw lines 241-251.
- Required bank/customer inputs and optional billing address: `## Collect information`, raw lines 254-269.
- Customer-action tokenization role and reference route: `## Tokenize`, raw lines 272-276; callback/Promise and billing-address examples continue at raw lines 279-463.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- SEPA lifecycle and mandate overview: [[source-braintree-docs-guides-sepa-direct-debit-overview]]

## Raw Sources

- [[raw/braintree/docs/guides/sepa-direct-debit/client-side/javascript/v3-2026-09-16|Braintree SEPA Direct Debit client-side implementation for JavaScript v3]] - complete collected page covering SEPA component setup, redirect configuration, customer-data collection and client tokenization
