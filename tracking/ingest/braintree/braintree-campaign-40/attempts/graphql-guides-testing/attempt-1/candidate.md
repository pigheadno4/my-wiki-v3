---
title: "Braintree GraphQL: Testing in Sandbox"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/testing"
raw_files:
  - "braintree/graphql/guides/testing-2026-09-16.md"
tags: [braintree, graphql, sandbox, testing, payment-methods, settlement]
---

## Overview

This collected [[braintree|Braintree]] website guide describes Sandbox test data and GraphQL actions for testing single-use and vaulted payment methods, transaction-status outcomes and settlement-state transitions. It is a Sandbox testing guide, not evidence of live execution, production behavior, merchant enablement, SDK support or the exact commit-qualified GraphQL schema.

## Key takeaways

- Sandbox test single-use payment methods act as payment-method IDs but are not consumed. The page says they may be passed as `paymentMethodId` to `chargePaymentMethod` and other payment-method queries or mutations. To exercise a vaulted path, it directs the reader to vault a test single-use method with `vaultPaymentMethod`, then charge the returned payment-method ID.
- Transaction-status simulation uses designated test amounts on `TransactionInput` when charging a payment method. Card-verification test values have a different purpose—initial payment-method validation—and the page explicitly says they do not force `chargePaymentMethod` transactions into different states.
- In Sandbox, `sandboxSettleTransaction` can force a transaction from `SUBMITTED_FOR_SETTLEMENT` to `SETTLED`, or to `SETTLEMENT_DECLINED` depending on the selected test amount. The method is Sandbox-only: production must follow normal settlement processing, and calling it there produces an error.
- The shown PayPal vault, declined-card charge and settlement payloads are examples. Their displayed IDs, amount and response states are synthetic fixtures, not credentials, reusable live payment data, or proof that any request ran or settled. This page does not specify general HTTP request construction or authorization credentials; use the separately collected API-call guide for that prerequisite.

## Detail locators

- `Test Payment Methods` — non-consuming Sandbox single-use methods, their use as `paymentMethodId`, the test vault-then-charge sequence, and an example PayPal vault mutation.
- `Testing Different Transaction Statuses` — transaction-amount status simulation, the separation from card-verification values, and an illustrative `2046.00` / `PROCESSOR_DECLINED` charge response.
- `Forcing Settlement of Transactions` — the Sandbox settlement transition, amount-dependent `SETTLED` versus `SETTLEMENT_DECLINED` outcome, production prohibition, and example `sandboxSettleTransaction` input/response.

## Related

- [[braintree-payment-platform]]
- [[braintree-payment-methods]]
- [[source-braintree-graphql-guides-making-api-calls]] — environment endpoints, credentials, version header and request/response handling; distinct prerequisites not established by this testing page.

## Raw Sources

- [[raw/braintree/graphql/guides/testing-2026-09-16|Braintree GraphQL Testing (fetched 2026-09-16)]]
