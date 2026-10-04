---
title: "Braintree General Testing Reference (Node.js)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/testing/node"
raw_files:
  - "braintree/docs/reference/general/testing/node-2026-09-16.md"
tags: [braintree, node-js, sandbox, testing, transactions, disputes, fraud-tools]
---

## Overview

This collected Braintree Node.js general testing reference catalogs Sandbox-only values and routes for simulating gateway behavior across transactions, card verification, payment-method nonces, settlement status, disputes, 3D Secure, fraud tools, AVS/CVV, bank details and selected wallet flows. Its central retrieval value is the boundary between these simulations and Production: the environments, credentials and created configuration are separate, and the page does not establish live acceptance, merchant eligibility or successful real-money processing.

## Key takeaways

- The page uses specific Sandbox values to trigger simulated outcomes. Transaction authorization behavior is driven by the amount, while card-verification behavior is driven by the test card number or verification nonce. A listed valid card number does not by itself guarantee transaction success because amount and, when configured, AVS/CVV inputs can also affect the result.
- Static `payment_method_nonce` values are provided for server-side Sandbox testing, and the Node.js section exposes four `braintree.Test.Nonces` objects. The full card, alternative-payment-method, verification, CVV-only and 3D Secure fixture inventories remain at the raw locators below rather than being treated as Production capabilities.
- The settlement testing routes can move a transaction already in `submitted_for_settlement` to `settled` or `settlement_declined`. The displayed callback and Promise snippets are examples for this collected Node.js page, not proof of successful execution or a guarantee about other SDK variants.
- Sandbox disputes can be simulated, but Production dispute response and management depend on account setup and are not available to every account. The source also routes to Sandbox dispute-creation and outcome-simulation procedures; those fixtures do not prove Production dispute eligibility or behavior.
- Fraud testing is conditional. The pending-review fixture is described as available only for Fraud Protection Advanced; Risk Threshold rejection reasons require at least Node `2.24.0` on this page or appear as `Unrecognized`; the Sandbox fraud-product UI is illustrative rather than configurable for rejection testing; fraud-response fixtures can depend on enabled fraud, risk-threshold or AVS/CVV rules; and `fake-gateway-rejected-fraud-nonce` is marked deprecated.
- Purging Sandbox data is consequential: confirmation logs the user out, locks the account and blocks API operations until completion. The page says the purge does not affect regular merchant accounts, recurring-billing plans, webhooks or other account settings, and it cannot delete merchant accounts.

> [!warning] Sandbox simulation and destructive-action boundaries
> This 2026-09-16 snapshot documents simulated Sandbox outcomes, not current availability, account eligibility, Production acceptance, bank behavior or live execution. Sandbox objects, options and recurring-billing settings do not transfer to Production, credentials differ, and production dispute management is account-dependent. Purge Test Data temporarily locks the Sandbox account and blocks API operations until the purge finishes.

## Detail locators

- Sandbox purpose and Sandbox-versus-Production isolation, non-transfer and separate credentials: `# Testing`, lines 14-20.
- Amount-driven authorization and settlement-response fixtures: `## Transaction amounts`, lines 23-39.
- Card transaction-versus-verification control distinction, valid-card qualification and verification fixtures: `## Credit card numbers`, lines 42-143.
- Static server-side nonces, example sale calls, card and alternative-payment-method fixtures, verification/CVV-only fixtures, 3D Secure scenarios and Node.js nonce objects: `## Payment method nonces`, lines 146-334.
- Submitted-for-settlement status transitions and Node.js callback/Promise examples: `## Settlement status`, lines 336-401.
- Sandbox dispute availability qualification, dispute creation and simulated API/Control Panel outcomes: `## Disputes`, lines 404-515.
- External 3D Secure test-card route: `## 3D Secure`, lines 517-519.
- Fraud-product qualification, minimum SDK-version table, illustrative-UI limit, conditional nonces and deprecated nonce: `## Fraud tools`, lines 522-563.
- AVS/CVV rule-enablement condition and response tables: `## AVS and CVV/CID responses`, lines 566-609.
- Sandbox routing numbers and external IBAN-generator route: `## Bank routing numbers`, lines 612-623.
- Platform-specific PayPal One Touch testing routes: `## PayPal One Touch`, lines 626-628.
- Purge inventory, confirmation procedure, temporary lock/API outage and unaffected-setting limits: `## Purge sandbox data`, lines 631-656.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Supporting server integration concept: [[braintree-server-sdk]]
- Supporting fraud concept: [[braintree-fraud-tools]]
- Supporting authentication concept: [[braintree-3d-secure]]
- Related Sandbox/Production orientation: [[source-braintree-get-started-try-it-out]]
- Related card testing and go-live guide: [[source-braintree-credit-cards-testing-go-live-node]]

## Raw Sources

- [[raw/braintree/docs/reference/general/testing/node-2026-09-16|Braintree General Testing Reference for Node.js]] - complete collected reference covering Sandbox test fixtures, Node.js examples, simulated status and dispute routes, fraud qualifications, environment isolation and purge consequences
