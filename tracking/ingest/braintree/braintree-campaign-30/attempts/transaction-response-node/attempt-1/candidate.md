---
title: "Braintree Transaction Response (Node.js)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/response/transaction/node"
raw_files:
  - "braintree/docs/reference/response/transaction/node-2026-09-16.md"
tags: [braintree, node-js, transactions, response-objects, processor-responses, risk-data]
---

## Overview

This collected Braintree Node.js response reference describes the Transaction record, including its current status, and routes readers through successful and unsuccessful result interpretation, processor and gateway response categories, risk data, status history, authorization-adjustment detail and network response codes. It is a response-retrieval reference, not proof that any specific payment was authorized, accepted by risk controls, submitted for settlement, settled or funded.

## Key takeaways

- The page identifies the Transaction object as a record containing transaction details and the current status. Its successful-result section associates success with an `authorized`, `settling`, or conditionally `submitted_for_settlement` status and shows how to inspect the payment-instrument type. Those states remain distinct; a successful result or an authorized status does not by itself establish settlement or funding.
- An unsuccessful result is grouped into three routes: validation preventing transaction creation, processor decline at authorization or settlement, and gateway rejection. The page exposes authorization-decline processor responses, settlement-decline processor settlement responses, and account-setting-based gateway-rejection reasons as separate diagnostic categories; one category must not be treated as evidence of another.
- Risk data is documented for credit-card verifications and transactions using compatible payment methods. The listed categories include fraud-service provider, risk identifier, device-data-captured flag and risk decision; the page additionally associates decision reasons with Fraud Protection and a risk score with Fraud Protection Advanced. These values provide scoring context and do not themselves establish processor authorization or settlement. The Java and .NET minimum-version note on the page is not a Node.js SDK requirement.
- Status history records transaction status changes with amount, status, UTC timestamp, transaction source and user categories. The exact status and source value inventories remain at the raw locator; listed history events document recorded states, not guaranteed transition order or completion of settlement.
- Network response code and text can be present on some transaction and verification objects as raw card-network responses. The page says they are supplemental and directs integrations to treat the processor response code as the source of truth.
- The settlement examples keep lifecycle actions conditional: a transaction submitted for settlement may be voided before it settles, while a settled transaction requires the separate refund route. Exact operation eligibility belongs to the linked request references rather than this response-object page.
- The page states that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. Because that external policy is not part of this source, this entry preserves the notice without interpreting which fields or records are limited.

## Detail locators

- Results-limitation notice and Transaction-record identity: `# Transaction`, lines 17-20.
- Successful result statuses and payment-instrument-type inspection: `## Result object > ### Successful result`, lines 28-49.
- Unsuccessful-result categories and validation route: `### Unsuccessful result` and `#### Validation errors`, lines 51-79.
- Authorization processor-decline fields and standardized-versus-additional processor response guidance: `#### Processor declined`, lines 80-109.
- Settlement processor-decline fields: `#### Processor settlement declined`, lines 111-129.
- Account-setting-based gateway-rejection status and reason: `#### Gateway rejection`, lines 131-146.
- Risk-data scope, product-specific additions, cross-language version note and decision-value inventory: `#### Risk data`, lines 148-180.
- Merchant-account currency example: `## Examples > ### Currencies`, lines 191-200.
- Settlement-result handling examples and settlement-decline route: `### Settlement status`, lines 202-254.
- Pre-settlement void versus post-settlement refund example: `### Voiding settlement`, lines 256-283.
- Explicit and possible automatic authorization adjustments plus adjustment-field table: `## Authorization adjustments`, lines 285-309.
- Status-history field categories, exact status/source inventories and callback/Promise examples: `## Status history details`, lines 312-367.
- Product-ID orientation: `## Product ID codes`, lines 369-371.
- Supplemental network-response qualification and exact card-network code tables: `## Network response codes`, lines 375-584.

## Evidence boundaries

> [!warning] Response state is not an end-to-end payment outcome
> Keep result success, processor authorization, gateway risk decisions, settlement submission, settlement completion and later funding separate. This snapshot documents returned response categories and examples; it does not establish current merchant eligibility, account configuration, field presence for every transaction, or successful execution of an individual payment.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- General Node.js result-wrapper semantics: [[source-braintree-result-objects-node]]
- Provider-level transaction lifecycle route: [[source-braintree-transaction-lifecycle]]
- Fraud product distinctions: [[braintree-fraud-protection]] and [[braintree-fraud-protection-advanced]]

## Raw Sources

- [[raw/braintree/docs/reference/response/transaction/node-2026-09-16|Braintree Transaction response reference - Node.js]] - complete collected page covering Transaction response identity, success and failure categories, processor and gateway diagnostics, risk data, settlement examples, authorization adjustments, status history and network response codes
