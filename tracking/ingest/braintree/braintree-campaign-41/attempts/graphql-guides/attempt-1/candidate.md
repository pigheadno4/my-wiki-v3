---
title: "Braintree GraphQL Get Started Guide"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides"
raw_files:
  - "braintree/graphql/guides-2026-09-16.md"
tags: [braintree, graphql, guides, schema, relay]
---

## Overview

This collected, unversioned [[braintree|Braintree]] website page is the landing and basic-orientation guide for Braintree GraphQL. It routes readers by experience and intent to introductory GraphQL material, Braintree Payment API concepts, request examples, the API Explorer, and a schema-repository changelog; it also introduces queries, mutations, schema introspection, and Braintree's stated Relay compatibility. The routes are navigation, not evidence for unread guide behavior, current API or schema scope, an exact GitHub commit, merchant eligibility, request execution, or payment outcomes.

## Key takeaways

- The landing page supports either top-to-bottom reading or intent-based navigation. Its named paths distinguish basic GraphQL orientation, an ideas-first Payments API guide, concrete API-call examples, interactive exploration, and the separate schema-repository changelog.
- The basic introduction describes queries as data-fetching requests and mutations as change-making requests; both can accept inputs. Its `ping` query, response, and named-operation snippets are teaching examples, not exact Braintree schema, authorization, environment, or runtime evidence.
- The page says the GraphQL schema defines the available types, queries, mutations, inputs, payloads, and return shapes, and that introspection can inspect schema information. Its statement that the schema is always up-to-date is captured provider guidance; this dated website snapshot does not itself establish the current schema, current deployment scope, or parity with a separately retained repository snapshot.
- The API Explorer is presented as a place to inspect the Braintree API schema and try queries and mutations. That route does not prove account access, credentials, successful execution, or payment behavior.
- The page states that the Braintree GraphQL API implements the Relay specification and describes that compatibility as primarily relevant to object lookup and search. This is an unversioned landing-page statement, not an exact field, pagination, SDK-version, or deployment guarantee.

## Detail locators

- `## If you`, lines 21-28 — intent-based routes to About GraphQL, API Concepts, Making API Calls, API Explorer, and the GitHub Schema Repo.
- `## About GraphQL`, lines 31-35 — newcomer learning recommendation and the separate Payments API and API-call routes.
- `### Queries and Mutations`, lines 41-76 — query-versus-mutation orientation, inputs, `ping` request/response examples, and arbitrary operation-name labels.
- `### Schema and Types`, lines 79-101 — schema/type purpose, introspection, the illustrative `__schema` query, validation guidance, and the page's schema-currency statement.
- `### The API Explorer`, lines 104-106 — schema-inspection and query/mutation trial route.
- `## Relay`, lines 109-111 — stated Relay compatibility and the lookup/search relevance boundary.

## Related

- [[braintree-payment-platform]]
- [[braintree]]

## Related raw API references

- [[source-braintree-graphql-guides-concepts]] — landing-page navigation to the ideas-first Payments API concepts guide; that separate source and raw govern its behavior claims.
- [[source-braintree-graphql-guides-making-api-calls]] — landing-page navigation to concrete request examples; that separate source and raw govern request requirements and behavior.
- [[source-braintree-graphql-guides-connections]] — separately retained detail for Relay-style connections and pagination; the landing page alone does not establish those shapes.
- [[source-github-graphql-api]] — separately retained schema-repository evidence; the landing page's repository link does not establish its exact commit or current scope.

## Raw Sources

- [[raw/braintree/graphql/guides-2026-09-16|Braintree GraphQL Get Started guide (fetched 2026-09-16)]]
