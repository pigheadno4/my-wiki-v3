---
title: "Braintree GraphQL Brazil Billing Agreement Installments Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides/financing_options"
raw_files:
  - "braintree/graphql/integration_guides/financing_options-2026-09-16.md"
tags: [braintree, graphql, paypal, brazil, installments, financing]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes a Brazil Billing Agreement with Installments route for merchants domiciled in Brazil. The documented flow uses Braintree GraphQL to calculate PayPal financing options for a payment method and transaction context, then charge the PayPal account with a selected option. It is a documentation snapshot, not an exact GraphQL schema baseline, SDK implementation, current merchant or buyer eligibility decision, environment-availability statement, or proof of a successful charge, settlement or funding.

## Key takeaways

- The page limits the feature to merchants domiciled in Brazil. It describes a consumer entering Pay with PayPal, using the Hermes flow to set up a billing agreement and select or change a funding instrument, returning to the merchant checkout, and then selecting an installment option. Those steps describe the documented journey; they do not prove availability or completion for an individual account or buyer.
- The merchant server first calls `paypalFinancingOptions` through Braintree GraphQL. The guide says calculation requires a payment-method ID, transaction information, currency code and country code. Its displayed query selects `financingOptions`, a credit-product identifier and qualifying-option terms such as rates, term, interval, payments, discounts, total interest and total cost; the BRL/`BR` variables and returned values are examples, not universal constraints or guaranteed offers.
- To transact, the guide routes the payment-method ID, transaction information and a financing option to `chargePayPalAccount`. The displayed request supplies a selected financing option under `options`, and the response selects the transaction status plus the selected financing option from the PayPal transaction-details snapshot. The snippets are illustrative object and field shapes rather than proof of exact current-schema nullability or validation behavior.
- The page says a successful charge results in `SETTLING`, `SUBMITTED_FOR_SETTLEMENT` or `SETTLED`. These are alternative documented result states, not interchangeable lifecycle stages or evidence that the displayed example executed, settled or funded.
- This captured guide states that merchants integrate through the Braintree GraphQL API and that server SDK support is future work. Do not generalize the route to a language SDK, another payment method, another installment product, another merchant domicile, or undocumented Sandbox/Production parity.

## Material warnings

> [!warning] Eligibility and product scope
> This page is specifically about PayPal Billing Agreement with Installments for merchants domiciled in Brazil. It does not establish current account enablement, consumer eligibility, a guaranteed set of financing offers, or universal Braintree, PayPal, Brazil-card or buy-now-pay-later behavior.

> [!warning] Examples are not schema or execution proof
> The query, mutation, variables and responses are captured documentation examples. The page names no Sandbox or Production environment and no GraphQL schema version. Its BRL/`BR` values, financing-option fields and displayed `SETTLING` response must not be treated as exhaustive schema, current deployment evidence or proof that any charge, settlement or funding event occurred.

## Detail locators

- Brazil-domiciled merchant restriction, PayPal Billing Agreement identity, Braintree GraphQL route and future server-SDK wording: raw lines 14-18.
- Consumer checkout, Hermes billing-agreement and funding-instrument steps, merchant-server option lookup, return and installment selection: `## Consumer Experience`, raw lines 21-27.
- `paypalFinancingOptions` prerequisites and displayed selection set: `### 1. Calculate Financing Options`, raw lines 35-90.
- BRL/`BR` request example and displayed financing-option response fields: raw lines 93-161.
- `chargePayPalAccount` prerequisites, transaction selection and selected-financing-option snapshot fields: `### 2. Charge PayPal Account with Selected Financing Option`, raw lines 163-196.
- Displayed charge variables, example selected option and successful-state statement: raw lines 199-223.
- Example response with `SETTLING` and selected-financing-option snapshot: raw lines 225-251.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Related raw API references

The guide links to Pay with PayPal orientation and transaction-status definitions. Those targets were not read for this entry and are navigation only; they do not establish current product eligibility, exact GraphQL schema behavior, environment availability or successful execution.

## Raw Sources

- [[raw/braintree/graphql/integration_guides/financing_options-2026-09-16|Braintree GraphQL Brazil Billing Agreement with Installments guide]] - complete collected page covering the Brazil eligibility statement, consumer flow, financing-option calculation and selected-option charge examples
