---
title: "Braintree GraphQL Account Onboarding"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides/account_onboarding"
raw_files:
  - "braintree/graphql/integration_guides/account_onboarding-2026-09-16.md"
tags: [braintree, graphql, account-onboarding, partners, underwriting, merchant-accounts]
---

## Overview

This collected [[braintree|Braintree]] website guide describes a GraphQL account-onboarding route for a partner business with many billers, franchisees, or sub-merchants to submit account applications for underwriting through `createBusinessAccount`. It is limited to select merchants and requires prior Partner application completion plus PayPal Account Manager setup. It is a website integration guide, not a language-SDK contract or exact-commit GraphQL schema, and its mutation and response examples do not prove account eligibility, underwriting approval, payment processing, payout execution, or production availability.

## Key takeaways

- The page says the account onboarding API is available only to select merchants. Before use, the partner must have completed the initial Partners application process, been set up by a PayPal Account Manager, obtained Braintree Control Panel login credentials, and worked with that Account Manager to configure the required features. The snapshot does not identify an environment, so the credential and setup statement must not be generalized into sandbox or production enablement.
- The intended actor is a business onboarding billers, franchisees, or sub-merchants. The API submits their information for underwriting. Only after a biller is approved does the page say the business can process payments in that biller's name and create payout calls; submission or an `accountRequest.id` is therefore not approval or downstream execution evidence.
- The guide describes `createBusinessAccount` as accepting account settings plus nested `business` and `financialInstruments` inputs. `business` represents the biller's legal entity and identifies stakeholder and optional point-of-contact roles; `financialInstruments` represents the merchant account's payout method.
- The displayed mutation, variables, response, and validation errors are examples. Field values and input paths remain raw locators; this page does not establish a complete/current schema, language-SDK support, or a successful application outcome.

## Evidence boundaries

> [!warning] Application status is not approval
> The example response returns an `accountRequest.id`, while the opening description makes later payment processing and payout calls conditional on biller approval. Do not treat the example response, request ID, or absence of displayed errors as underwriting approval, account activation, payment acceptance, or payout success.

> [!warning] Eligibility, credentials, and environment remain qualified
> This snapshot says access is limited to select merchants and depends on Partner application and PayPal Account Manager setup with Braintree Control Panel login credentials. It does not specify sandbox versus production or prove that any account is enabled for the operation. Use [[source-braintree-graphql-guides-making-api-calls]] for the separately collected general GraphQL request and credential route.

## Detail locators

- Select-merchant availability and the partner use case for billers, franchisees, or sub-merchants: opening paragraphs, raw lines 16-18.
- Partner application, PayPal Account Manager setup, Control Panel credentials, and feature configuration: `## Requirements`, raw lines 21-23.
- `createBusinessAccount` purpose and the account, legal-entity, stakeholder, point-of-contact, and payout-method input roles: `## Creating an Application`, raw lines 26-36.
- Mutation shape: `### Mutation`, raw lines 38-48; full variable example: `### Variables`, raw lines 51-209.
- Example `accountRequest.id` response: `### Response`, raw lines 211-225.
- Example validation errors and input paths: `## Error Samples`, raw lines 227-305.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- General GraphQL request and credential route: [[source-braintree-graphql-guides-making-api-calls]]
- Separate commit-qualified schema authority: [[source-github-graphql-api]]

## Raw Sources

- [[raw/braintree/graphql/integration_guides/account_onboarding-2026-09-16|Braintree GraphQL account onboarding guide]] - fully read 2026-09-16 website snapshot covering select-merchant availability, partner setup, the account-application mutation, examples, and validation-error samples
