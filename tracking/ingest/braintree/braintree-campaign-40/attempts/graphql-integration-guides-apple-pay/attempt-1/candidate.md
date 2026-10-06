---
title: "Braintree GraphQL Apple Pay Integration Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides/apple_pay"
raw_files:
  - "braintree/graphql/integration_guides/apple_pay-2026-09-16.md"
tags: [braintree, graphql, apple-pay, digital-wallets, web-payments, vaulting]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide explains how its documented GraphQL route processes Apple Pay payments. It covers environment-matched test accounts, Apple Pay web-domain registration, the handoff of an authorized single-use payment-method ID to a server-side `chargePaymentMethod` call, and qualified Vault routes. It is separate from any exact-version client SDK implementation and from the commit-qualified GraphQL schema history; it does not establish current merchant or device eligibility, account enablement, deployment, successful authorization, transaction settlement or funding.

## Key takeaways

- Testing requires an iCloud account corresponding to the target environment: the guide specifies an iTunes Connect sandbox tester account for sandbox and a production iCloud account for production. This is an account prerequisite stated by the captured guide, not proof that a particular account, device or merchant is eligible.
- For Apple Pay on the web, every planned domain must be registered with Apple through the Braintree Control Panel. The guide says not to register through the Apple Developer Portal and says a merchant-generated Payment Processing Certificate is unnecessary for this web route because Braintree uses its shared certificate. Sandbox and production domains are registered separately, and the fully qualified domain must match exactly, including `www` where applicable.
- Production registration additionally requires hosting Braintree's domain-association file at `/.well-known/apple-developer-merchantid-domain-association`. The page says Apple's retrieval must avoid 3xx redirects, use HTTPS 1.1, return the file as a binary object with `Content-Type: application/octet-stream`, and remain reachable outside a firewall. These are captured setup requirements, not domain-verification or deployment proof.
- After the customer successfully authorizes payment, the client receives a single-use payment-method ID and sends it to the merchant server, where the guide passes it to `chargePaymentMethod`. The page also directs the merchant to collect client device data and include it in `riskData`. The displayed mutation, variables and `SUBMITTED_FOR_SETTLEMENT` response are examples, not proof that authorization, submission, settlement or funding occurred.
- The amount in the client-side Apple Pay request should reflect the amount authorized and submitted for settlement, although the page says transactions can still process if the amount changes during fulfillment. For billing address, tokenized CVV, 3D Secure authentication or other fraud-tool options, the guide routes to `chargeCreditCard` instead of `chargePaymentMethod`.
- Apple Pay cards can be saved in the Vault only for supported use cases. The page routes supported integrations either to `vaultPaymentMethod` or to the `vaultPaymentMethodAfterTransacting` input on `chargePaymentMethod`; the linked support and GraphQL reference pages remain separate authority for eligibility and exact schema behavior.

> [!warning] Scope and evidence boundary
> This website snapshot does not identify a client SDK package/version or an exact GraphQL schema revision. Its operation and response blocks are illustrative documentation, while environment, merchant-account, Apple Pay, domain and Vault eligibility depend on separate account and platform authority. Do not treat the examples or this collected page as deployment, live availability, successful payment, settlement or reusable-token proof.

## Detail locators

- Apple Pay identity and stated GraphQL-guide purpose: raw lines 14-18.
- Sandbox versus production iCloud-account prerequisite: `### iCloud account setup`, raw lines 24-26.
- Optional website icon recommendation: `### Specify an Icon`, raw lines 29-31.
- Web-domain registration requirement, Control Panel ownership, Apple Developer Portal exclusion and shared-certificate boundary: `### Domain registration`, raw lines 34-38.
- Sandbox Control Panel registration steps and exact fully qualified domain-name requirement: `#### Sandbox Environment`, raw lines 41-57.
- Production Control Panel registration, domain-association file location and verification-serving constraints: `#### Production Environment`, raw lines 62-87.
- Successful customer authorization, single-use payment-method handoff, server-side `chargePaymentMethod` action and device-data route: `## Creating transactions`, raw lines 90-95.
- Mutation selection, variables and displayed example response including Apple Pay origin details: raw lines 96-186.
- Amount-consistency guidance and `chargeCreditCard` route for additional billing, CVV, 3D Secure or fraud inputs: raw lines 187-189.
- Supported-use-case Vault qualification and `vaultPaymentMethod` or `vaultPaymentMethodAfterTransacting` routes: `## Vaulting Apple Pay cards`, raw lines 190-196.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-apple-pay]]
- Provider payment-method lifecycle route: [[braintree-payment-methods]]
- Commit-qualified GraphQL contract: [[source-github-graphql-api]]

## Related raw API references

The page links to GraphQL reference entries for `chargePaymentMethod`, `chargeCreditCard`, `riskData`, `vaultPaymentMethod` and `vaultPaymentMethodAfterTransacting`, plus Apple, Control Panel, fraud-device-data, credit-card and Apple Pay support guidance. Those linked targets were not read for this entry and are navigation only; they do not establish exact schema equivalence, SDK behavior, account enablement, domain verification, Vault eligibility or successful execution.

## Raw Sources

- [[raw/braintree/graphql/integration_guides/apple_pay-2026-09-16|Braintree GraphQL Apple Pay integration guide]] - complete collected page covering environment account setup, web-domain registration, single-use payment-method charging and qualified Vault routes