---
title: "Braintree Forward API Hyperwallet Integration"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/extend/forward-api/hyperwallet"
raw_files:
  - "braintree/docs/guides/extend/forward-api/hyperwallet-2026-09-16.md"
tags: [braintree, braintree-extend, forward-api, hyperwallet, bank-cards]
---

## Overview

This collected Braintree developer guide documents a Forward API destination integration for sending payment-method data to Hyperwallet's Bank Card Create and Bank Card Update API routes. It is a Braintree-hosted guide for configuring and testing forwarding, not Hyperwallet-owned API authority and not proof that a card was tokenized, a payout was initiated or completed, or a customer payment was executed.

The snapshot was collected on 2026-09-16. It preserves the guide's environment mapping, request examples, prerequisites and troubleshooting notes, but does not establish current production eligibility, account enablement, successful API execution or present Hyperwallet behavior.

## Key takeaways

- The guide says production Forward API use is subject to eligibility and directs readers to an Account Manager or Business Development. Collection of this page and sandbox access do not establish production approval.
- The documented environment mapping uses `hyperwallet_sandbox` for Braintree Sandbox to Hyperwallet Sandbox, and `hyperwallet_integration` for both Braintree Sandbox to Hyperwallet UAT and Braintree Production to Hyperwallet Production. The destination URL must also match the environment and configured URL pattern.
- Before the sandbox example, the page directs the reader to create a Hyperwallet sandbox account and user, obtain the returned user token, and use the Hyperwallet API username and API password from the credentials flow. The example separately authenticates to the Braintree sandbox forwarding endpoint with Braintree public/private keys and places the Hyperwallet username, password and card data under `sensitive_data`; these values are credentials or sensitive payment data, not reusable sample configuration.
- The create and update examples send a Braintree `payment_method_nonce` to the Forward API and target Hyperwallet REST v4 bank-card URLs with `POST` and `PUT`, respectively. These are example forwarding requests. They do not establish that Forward API creates a Braintree Vault token, runs a Hyperwallet payout, or executes a customer payment.
- Hyperwallet sandbox accepts only a limited set of card numbers according to the page. The examples therefore override the card number with a literal `sensitive_data.number`; for a normal request, the guide says to omit that attribute so the number comes from the nonce. The displayed numbers and CVV are test values only.
- For UAT, the page says to work with the onboarding helper for nonce-tokens representing vaulted debit cards that Forward API loads and sends to Hyperwallet. Its troubleshooting guidance also calls out the required trailing slash for bank-card collection URLs, the correct REST version, an environment-appropriate URL, and a non-US `transferMethodCountry` error condition.

> [!warning] Production eligibility is separate
> The collected page states that production Forward API use is subject to eligibility. Confirm current approval, configuration and environment alignment with Braintree before production use; a successful sandbox request would not establish production access.

> [!warning] Forwarding is not tokenization, payout or payment execution
> This guide uses a Braintree payment-method nonce as input to forwarding requests that create or update a Hyperwallet bank-card resource. It does not document creation of a new Braintree payment-method token, payout initiation or completion, customer-payment authorization or capture, settlement, or funding. Hyperwallet API behavior remains under Hyperwallet's own current authority.

> [!warning] Protect both credential sets and payment data
> The examples contain placeholders for Braintree keys, a merchant ID, a Hyperwallet user token, Hyperwallet API credentials, and sensitive card fields. Keep real values out of source, logs and evidence artifacts, and do not copy the literal sandbox test card values into production requests.

## Detail locators

- Production eligibility qualification and contact routes: `**AVAILABILITY**`, raw lines 17-18.
- Destination identity and Bank Card Create/Update scope: introduction below `# Hyperwallet Integration`, raw line 20.
- Braintree-to-Hyperwallet environment and config-name mapping: `## Naming & Environment Alignment`, raw lines 23-29.
- Sandbox-account, user-token and Hyperwallet API-credential prerequisites: `## Example`, raw lines 32-37.
- Sandbox create request, Braintree authentication, forwarding fields, destination URL and sensitive-data placement: `Example create request (sandbox)`, raw lines 39-67.
- Example Hyperwallet bank-card response body: `Response Body`, raw lines 68-94.
- Update-token prerequisite and example `PUT` forwarding request: `Example update request`, raw lines 95-120.
- Sandbox literal-number override, normal nonce-number behavior and test-value list: notes after the update example, raw lines 122-131.
- URL-regex failure, trailing-slash/version/environment guidance and country-related error: `## Common Issues`, raw lines 136-160.
- Hyperwallet test-value distinction and UAT onboarding-helper nonce-token prerequisite: final paragraph under `## Common Issues`, raw line 169.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]

## Related raw API references

- [[raw/braintree/docs/reference/forward-api/overview-2026-09-16|Braintree Forward API overview]] - linked navigation-only destination for the production-eligibility route and general Forward API reference; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/extend/forward-api/hyperwallet-2026-09-16|Braintree Forward API Hyperwallet integration guide]] - complete collected destination guide covering eligibility, environment mapping, sandbox prerequisites, create/update examples, nonce-versus-literal test-card handling, UAT onboarding and common issues
