---
title: "Braintree GraphQL Google Pay Integration Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides/google_pay"
raw_files:
  - "braintree/graphql/integration_guides/google_pay-2026-09-16.md"
tags: [braintree, graphql, google-pay, paypal, transactions, vaulting]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes creating GraphQL transactions from Google Pay payment methods and the bounded Vault routes for Google Pay cards. It distinguishes card-funded Google Pay transactions from PayPal-through-Google-Pay transactions and records response fields that identify their Google Pay origin. This is a website integration guide, not a client-SDK implementation or exact GraphQL schema baseline, and it does not establish current merchant or customer eligibility, environment availability, authorization success, settlement or funding.

## Key takeaways

- The page describes Google Pay as supporting in-app and web purchases for customers with supported Android devices, using cards or PayPal accounts stored in a Google account as well as payment methods stored in Google Pay. Compatibility and availability are delegated to a linked support article, which was not read for this entry.
- For a Google Pay card, the guide uses `chargePaymentMethod` with `amount` and `paymentMethodId`. Its example response exposes `paymentMethodSnapshot.origin.type` as `GOOGLE_PAY` and selects `GooglePayOriginDetails.googleTransactionId` and `bin`. The displayed transaction status is example output, not proof that a charge, authorization, settlement or funding event occurred. The page also permits device data under `riskData` for additional fraud-analysis information.
- PayPal through Google Pay remains a PayPal transaction rather than becoming a Google Pay transaction. The guide uses the same `chargePaymentMethod` mutation, identifies a Google Pay origin on the PayPal payment method and shows `facilitatorDetails.oauthApplication.name` as `Google`. The merchant account used for the transaction must accept PayPal transactions, and the guide routes settlement rules and options to the ordinary PayPal transaction path.
- For certain account setups, the page recommends collecting and passing billing-address information when storing a payment method or creating a transaction; it says at least a postal code can improve the likelihood of authorization and directs merchants to contact Braintree about their setup. This conditional recommendation is not a guarantee of authorization.
- Google Pay cards may be stored in the Vault only for supported use cases. If eligible, the page gives `vaultPaymentMethod` and `vaultPaymentMethodAfterTransacting` on `chargePaymentMethod` as the two routes. PayPal accounts from Google Pay cannot be vaulted, so the post-transaction vaulting option is unsupported for those transactions.

> [!warning] Scope, eligibility and execution boundaries
> The captured page does not identify a client SDK, package version, exact GraphQL schema version or Sandbox-versus-Production environment. Its mutations, variables and responses are examples rather than runtime proof. Compatibility, merchant enablement, PayPal acceptance, card-vault eligibility and account-specific billing-address guidance require the linked or account-specific authority; do not infer them from a successful-looking example response.

## Detail locators

- Google Pay purpose, in-app/web surface and cards-or-PayPal-account description: `# Google Pay`, raw lines 14-18.
- Google Pay card treatment, `chargePaymentMethod` inputs, selection set, variables and example response: `### Using Credit Cards`, raw lines 24-93.
- Google Pay origin fields and optional `riskData` device-data route: raw line 94.
- PayPal-versus-Google-Pay transaction identity, mutation, Google Pay origin and Google facilitator details: `### Using PayPal with Google Pay`, raw lines 97-160.
- PayPal acceptance prerequisite, settlement-route equivalence and conditional billing-address recommendation: raw lines 161-163.
- Card-vault eligibility boundary, unsupported PayPal-account vaulting and the two card-storage routes: `## Vaulting Google Pay`, raw lines 164-174.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Dedicated merchant/customer eligibility, fraud-tool, vaulting and production-approval route: [[source-braintree-payment-methods-google-pay]]
- GraphQL payment-method identity and lifecycle route: [[source-braintree-graphql-guides-payment-methods]]

## Related raw API references

The guide links to GraphQL reference entries for `chargePaymentMethod`, `riskData` and `vaultPaymentMethod`, plus separate Google Pay availability, PayPal settlement and transaction guides. Those targets were not read for this entry and are navigation only; they do not establish exact schema equivalence, current account enablement, environment availability or successful execution.

## Raw Sources

- [[raw/braintree/graphql/integration_guides/google_pay-2026-09-16|Braintree GraphQL Google Pay integration guide]] - complete collected page covering card-funded and PayPal-funded charge examples, origin fields, account and billing qualifications, and Vault restrictions
