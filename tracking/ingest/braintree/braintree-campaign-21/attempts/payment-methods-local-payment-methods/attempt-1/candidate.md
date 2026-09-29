---
title: "Braintree Local Payment Methods"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/local-payment-methods"
raw_files:
  - "braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md"
tags: [braintree, local-payment-methods, regional-payments, payment-contexts, paypal]
---

## Overview

This collected Braintree guide describes Local Payment Methods as banks, wallets or other payment means that operate only in particular regions, using iDEAL in the Netherlands and Bancontact in Belgium as examples. It is a retrieval route for the page's merchant and customer availability, PayPal-account prerequisite, currency treatment, redirect-heavy checkout flow, Payment Context visibility and unsupported dispute, vaulting and recurring-transaction boundaries; the 2026-09-16 snapshot does not itself confirm current merchant or customer eligibility.

## Key takeaways

- The page says eligible merchants in Braintree-supported countries can offer Local Payment Methods only after adding PayPal to their Braintree integration. It says transactions are presented in euros, funds settle into the merchant's PayPal business account in its primary currency, and applicable conversion is added to the customer's payment amount.
- Customer availability depends on locality and the supported scheme for that country. The page says Custom UI lets the merchant control which methods appear based on the customer's country; method-by-method support remains in the linked developer documentation rather than this guide.
- Setup is scoped to creating, verifying and linking a valid PayPal business account in the Braintree Control Panel, followed by the client and server integrations described in the linked developer documentation.
- The page says disputes are currently unsupported for Local Payment Methods and directs customers to their bank. It separately says vaulting payment methods and creating recurring transactions are currently unsupported.
- Since most Local Payment Methods require redirecting the customer into the selected method's checkout flow, the page presents Payment Contexts as pre-transaction visibility into payment initiation, method type and customer progress. It says this feature is currently available as a search function in the Braintree gateway; the status table and troubleshooting examples remain at the raw locators below.

## Evidence boundaries

> [!warning] Method and locality scope
> Do not treat one listed regional example or a link to the method catalog as evidence that every Local Payment Method is available in every country. Determine customer availability from the exact method and country documentation, and retain the guide's eligible-merchant and PayPal-account qualifications.

> [!warning] Redirect and lifecycle scope
> The page says most, not all, Local Payment Methods require a redirect. Payment Contexts describe pre-transaction checkout progress and merchant attempts; they are visibility records, not by themselves proof that settlement or funding completed.

## Detail locators

- Local Payment Method identity and regional examples: `# Local Payment Methods`, line 16.
- Eligible-merchant, PayPal-integration, euro-presentment, primary-currency settlement and customer-conversion qualifications: `## Availability`, line 21.
- Locality-dependent schemes and Custom UI display control: `### Customer Availability`, line 26.
- PayPal business-account prerequisite and separate client/server integration route: `## Setup`, line 31.
- Processing fees and funding statements: `### Fees`, line 39, and `### Funding`, line 44.
- Unsupported dispute, vaulting and recurring-transaction boundaries: `### Disputes`, line 49, and `### Recurring transactions and vaulting support`, line 54.
- Redirect-qualified Payment Context purpose, captured context and current search surface: `## Payment Contexts`, lines 59-63; Control Panel search steps: lines 65-71.
- Payment Context creation, status meanings and scenario examples: `### Statuses`, lines 74-91.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Recurring-use boundary: [[recurring-payments]]
- Dispute-handling boundary: [[disputes]]

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16|Braintree Local Payment Methods guide]] - complete collected page covering regional scope, availability, PayPal setup, processing boundaries and Payment Context visibility
