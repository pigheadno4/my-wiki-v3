---
title: "Braintree Premium Fraud Management Tools Server-Side Implementation (Node.js)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/server-side/node"
raw_files:
  - "braintree/docs/guides/premium-fraud-management-tools/server-side/node-2026-09-16.md"
tags: [braintree, premium-fraud-management, node-js, device-data, risk-data]
---

## Overview

This captured Node.js server-side guide explains how a merchant backend supplies client-collected device data to Braintree requests, optionally skips Premium Fraud Management Tools checks for an individual transaction or verification, supplies transaction custom fields used by Fraud Protection Advanced filters, and reads risk data returned for credit-card verifications and compatible-payment-method transactions. It is a dated documentation snapshot, not proof of current account enablement, product eligibility, payment execution or SDK support.

## Key takeaways

- The captured availability table recommends the latest SDK and identifies Node SDK 2.24.0 as the minimum for all features described as available on this page. That is a page-scoped historical requirement, not a claim that 2.24.0 is currently supported or sufficient for present-day enablement.
- The server passes collected device data when creating a customer, payment method or transaction. The guide strongly recommends device data when a customer adds a credit card to the Vault or initiates a transaction; for verification requests, it says device data enables preliminary fraud checks in addition to any enabled AVS, CVV and risk-threshold checks. The Node examples are implementation examples, not successful-execution guarantees.
- For PayPal transactions using the Vault flow, the page separately calls including device data critical for reducing decline rates and routes details to a PayPal guide. This does not make that PayPal concern interchangeable with card-fraud scoring.
- Setting `skipAdvancedFraudChecking` skips Premium Fraud Management Tools checks for a specific transaction. The page also documents the option for specific verification calls through payment-method create/update and customer create/update. Skipping a fraud check does not establish authorization, approval, capture, settlement or funding.
- Fraud Protection Advanced custom fields must be passed in payment transaction details before they can be created in the tool and used in filter conditions. This page does not establish current Advanced eligibility, account configuration or filter behavior beyond that prerequisite.
- Returned risk data can include the fraud service provider, risk identifier, device-data-captured flag and risk decision. The page says Fraud Protection data includes decision reasons and Fraud Protection Advanced data additionally includes a risk score; those named products and their response fields must remain distinct. The listed risk-decision values are `Not Evaluated`, `Approve`, `Review` and `Decline`, but this page does not define the gateway or processor action for each value. A risk decision, including `Review`, is not itself processor authorization, capture or settlement.

## Detail locators

- SDK availability and the captured Node minimum: `**AVAILABILITY**`, lines 17-24.
- Request placement and callback/Promise examples for transactions and payment-method verification: `## Using device data`, lines 29-92.
- Recommended events, verification rationale and the separate PayPal Vault warning: `### When to pass device data`, lines 94-108.
- Transaction and verification bypass option plus Node examples: `### Skipping Premium Fraud Management Tools`, lines 111-172.
- Fraud Protection Advanced custom-field purpose and transaction-input prerequisite: `## Custom fields`, lines 174-178.
- Response-field inventory, product-qualified additions, Node property examples and decision values: `## Response handling`, lines 181-201.

## Related

- Company: [[braintree]]
- Named product concept: [[braintree-fraud-protection]]
- Named product concept: [[braintree-fraud-protection-advanced]]
- Server integration boundary: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/guides/premium-fraud-management-tools/server-side/node-2026-09-16|Braintree Premium Fraud Management Tools server-side implementation for Node.js]] — complete captured guide covering SDK availability, device-data forwarding, per-request skipping, custom fields and risk response handling
