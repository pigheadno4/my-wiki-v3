---
title: "Braintree GraphQL Customers Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/customers"
raw_files:
  - "braintree/graphql/guides/customers-2026-09-16.md"
tags: [braintree, graphql, customers, vault, payment-methods]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes the GraphQL `Customer` object as a record for storing and organizing one or more payment methods. It demonstrates server-side GraphQL operations to create, update, delete, search and retrieve customers. This is a website/API documentation snapshot, not a language-SDK implementation or exact-schema baseline, and it does not establish current deployment, merchant eligibility, payment-method availability or successful payment execution.

## Key takeaways

- `createCustomer` has no required customer fields according to the guide, so the demonstrated operation can create either a populated customer or a blank customer whose fields are added later. The displayed fields and response are examples rather than a complete or guaranteed schema.
- Custom fields can hold additional customer data, but the guide says they must first be configured in the Control Panel before they can be used through the API.
- `updateCustomer` requires `customerId`. The page demonstrates a company-name change; that example does not establish every supported update field.
- `deleteCustomer` requires `customerId` and breaks the association between the customer and any transactions. A customer with existing payment methods will not be deleted; the guide directs the caller to delete those payment methods from the Vault first. A missing customer ID produces the documented `NOT_FOUND` error.
- Customers can be searched by characteristics through the search query, or retrieved by global ID through the node query. The shown company filter, selected fields and response records are examples; use the linked GraphQL reference or an exact schema source for the complete contract.

> [!warning] Consequential and evidence boundaries
> Customer deletion is consequential: it breaks transaction associations, and existing payment methods must be removed from the Vault before the customer can be deleted. The page does not state the downstream effects of deleting those payment methods; consult the dedicated payment-method lifecycle authority before acting. The guide's example operations and responses are not proof that an account is enabled or that an individual mutation succeeded.

## Detail locators

- Customer-object purpose, multiple-payment-method relationship and operation inventory: `# Customers`, lines 14-16.
- Create behavior, optional customer fields and blank-customer route: `## Create`, lines 19-26, and `### Blank customer`, lines 78-80.
- Custom-field purpose and Control Panel prerequisite: `### Use custom fields`, lines 126-128.
- Update operation and required customer ID: `## Update`, lines 192-194; the mutation, variables and response example continue through line 243.
- Deletion action, required customer ID, broken transaction association, existing-payment-method blocker and prior Vault-deletion instruction: `## Delete`, lines 245-249. The mutation example and missing-customer `NOT_FOUND` behavior continue through line 282.
- Characteristic search and its displayed query/response shape: `## Search`, lines 285-363. Global-ID node lookup and its displayed selection/response are at lines 364-399.
- Customer-error-code navigation: `## Errors`, lines 401-403.
- Exact commit-qualified GraphQL fields, nullability and constraints are separately retained in `raw/github/braintree/graphql-api/snapshots/2026-08-11-3a89f42/files/schema.graphql` via [[source-github-graphql-api]]; they must not be inferred from these website examples.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]
- Payment-method object and lifecycle: [[source-braintree-graphql-guides-payment-methods]]
- Exact commit-qualified schema: [[source-github-graphql-api]]

## Raw Sources

- [[raw/braintree/graphql/guides/customers-2026-09-16|Braintree GraphQL Customers guide]] - complete collected website page for GraphQL customer creation, update, deletion, search and lookup examples
