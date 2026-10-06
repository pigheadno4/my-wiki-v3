---
title: "Braintree GraphQL Credit Card Integration Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides/credit_cards"
raw_files:
  - "braintree/graphql/integration_guides/credit_cards-2026-09-16.md"
tags: [braintree, graphql, credit-cards, transactions, verification, vault, tokenization]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide routes GraphQL credit-card operations for charging, verification, Vault storage, billing-address updates, authorization, detached refunds and direct card tokenization. It documents operation purposes and example selections, not a language-SDK implementation or an exact GraphQL schema baseline, and it does not establish current deployment, account enablement, card eligibility, successful authorization, settlement, funding or refund completion.

## Key takeaways

- `chargePaymentMethod` is presented as the simplest route: it accepts an amount and a client-relayed single-use payment method and immediately submits the transaction for settlement. For additional inputs such as billing address, tokenized CVV or 3D Secure authentication, the guide routes to `chargeCreditCard`. Both examples select a transaction object; their displayed `SUBMITTED_FOR_SETTLEMENT` status is example output, not execution evidence or proof of settlement or funding.
- `verifyCreditCard` runs verification on a credit card already stored in the Vault and returns a verification object. The guide says the gateway normally uses a $0 or $1 authorization and automatically voids it, with a different authorization amount available through options. That authorization and automatic void are consequential card-network actions, not a purchase. When Premium Fraud Management Tools are used, the page strongly recommends sending device data on every verification. Processor-declined and gateway-rejected results expose different reason routes.
- `vaultCreditCard` combines verification and subsequent Vault storage: the page says the resulting multi-use payment method is saved only if verification succeeds, and the payload returns separate payment-method and verification objects. `updateCreditCardBillingAddress` targets an existing multi-use card and verifies the card and new address before setting the replacement billing address. These operations can persist or modify Vault data; their displayed `VERIFIED` responses are examples rather than guarantees.
- `authorizeCreditCard` creates an authorization without submitting for settlement and returns transaction details. The page directs the merchant to inspect transaction status and later call `captureTransaction`; authorization and capture are separate actions, and the page does not establish capture success or final settlement.
- `refundCreditCard` is the detached-credit route and returns a refund object. Detached credits are disabled by default and generally violate card-association rules; the page says temporary enablement must be requested by the authorized signer on the Braintree gateway account. The displayed `SUBMITTED_FOR_SETTLEMENT` refund is not proof that a refund settled or reached the cardholder.
- `tokenizeCreditCard` accepts raw credit-card fields and returns a single-use payment method. The guide restricts this mutation to PCI SAQ-D integrations and explicitly says not to use it when compliance status is uncertain. The resulting single-use method can be passed to charge or authorization mutations; tokenization itself is not authorization, verification, Vault storage or payment success.

> [!warning] Scope, account and environment boundaries
> This website snapshot does not identify an SDK package/version or an API schema version, and its code blocks are illustrative selection and response shapes. The captured page does not name Sandbox or Production, so do not infer environment availability or parity. Detached-credit enablement is account-controlled, while card, processor, fraud-tool, merchant-account and regional eligibility require separate authority.

## Detail locators

- Simple immediate-settlement-submission route, amount and single-use payment-method input, example transaction selection and displayed response: `## Creating simple transactions`, raw lines 17-67.
- Advanced `chargeCreditCard` purpose, additional-input examples, transaction fields and displayed response: `## Creating advanced transactions`, raw lines 70-147.
- Stored-card verification purpose, Control Panel recommendation, default/custom authorization amount, automatic void and request/response examples: `### Card verification`, raw lines 149-223.
- Premium Fraud Management Tools device-data recommendation, result-object placement, decline/rejection statuses and reason routes: raw lines 224-247.
- Verify-and-Vault success condition, separate payment-method and verification objects, examples and unsuccessful-result meanings: `### Verify and Vault`, raw lines 250-322.
- Existing multi-use-card billing-address mutation, pre-update verification and example payload: `### Update Billing Address`, raw lines 325-386.
- Separate authorization purpose, transaction object/status inspection, later `captureTransaction` requirement and examples: `### Authorize`, raw lines 388-435.
- Detached-credit association warning, `refundCreditCard` request/refund object, displayed status and authorized-signer temporary-enablement prerequisite: `### Creating a Detached Refund`, raw lines 437-496.
- PCI SAQ-D-only raw-card tokenization restriction, `tokenizeCreditCard` input/payment-method output and downstream single-use-method routes: `### Tokenization`, raw lines 497-560.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Single-use terminology and lifecycle route: [[source-braintree-payment-method-nonces]]
- Provider transaction-lifecycle route: [[source-braintree-transaction-lifecycle]]

## Related raw API references

The guide links to GraphQL reference entries for its mutations, inputs, payload objects and rejection fields, plus separate collection, Vault, transaction-lifecycle, Control Panel and fraud guidance. Those targets were not read for this entry and are navigation only; they do not establish exact schema equivalence, account enablement, environment availability or successful execution.

## Raw Sources

- [[raw/braintree/graphql/integration_guides/credit_cards-2026-09-16|Braintree GraphQL Credit Card integration guide]] - complete collected page covering charge, verification, Vault, billing-address update, authorization, detached-refund and PCI-qualified tokenization operations
