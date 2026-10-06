---
title: "Braintree GraphQL Connections and Pagination Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/guides/connections"
raw_files:
  - "braintree/graphql/guides/connections-2026-09-16.md"
tags: [braintree, graphql, connections, pagination, relay, cursors]
---

## Overview

This collected [[braintree|Braintree]] website guide describes the connection shape and cursor-pagination pattern used by the Braintree GraphQL API. It presents collections as edges containing nodes and opaque cursors, accompanied by page information, and shows `first`, `after`, and `hasNextPage` in subset and continuation queries. The page states that Braintree's implementation adheres to the Relay specification; this 2026-09-16 snapshot is not independent proof of current specification conformity, exact schema support, SDK behavior, deployment availability, account eligibility or successful API execution.

## Key takeaways

- The guide uses connections where a result collection can be unbounded, including search results and collections attached to customers or payment methods. It says each pageable object type has a corresponding `*Connection` type, but the displayed `genericConnection` is an explanatory shape rather than an exact field contract for every object.
- A page is the connection's `edges` list. Each edge contains a `node` for the returned object and an opaque `cursor` marking that edge's place in the larger result set; `pageInfo.hasNextPage` indicates whether more edges exist beyond the current page.
- A caller that only needs a subset can omit the optional pagination fields. The simple transaction-search query and response are illustrative examples and do not establish a universal default page size, response validity for a current schema version, or result ordering for other connections.
- `first` requests a bounded number of items, `after` starts after a supplied cursor, and the two can be combined to request the next bounded slice. Criteria and ordering are available only for some connections, so the guide does not establish those arguments for every connection field.
- To continue the shown transaction search, the guide performs another search using a cursor from the prior page and checks `hasNextPage`. Its statement that `hasNextPage: false` leaves the oldest matching object last is tied to that transaction-search example and must not be generalized into a sorting guarantee for every connection.

> [!warning] Website guide and example boundary
> The page's generic GraphQL and JSON snippets explain connection mechanics; they do not identify an SDK package/version or an exact GraphQL schema version. Confirm concrete fields, argument support, ordering and environment/account availability against the applicable current schema and operation authority. A returned page or cursor is retrieval data, not payment, settlement or funding evidence.

## Detail locators

- Relay-adherence statement, connection definition and examples of unbounded collections: introduction, raw lines 14-20.
- Generic `*Connection` structure; `edges`, `node`, opaque `cursor` and `pageInfo.hasNextPage` meanings: `## The Contents of a Connection`, raw lines 23-78.
- Subset query with optional pagination fields omitted and illustrative transaction-search response: `## Simple Use`, raw lines 81-129.
- `first` slicing, `after` cursor continuation, combined arguments and the some-connections-only criteria/order qualification: `## Complex Connections`, raw lines 131-176.
- Complete transaction-search pagination example, cursor reuse, continuation behavior and `hasNextPage` stopping condition: `### Pagination`, raw lines 179-246.
- External GraphQL and Relay learning links: `### More on Relay`, raw lines 249-257.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Separate commit-qualified schema authority: [[source-github-graphql-api]]

## Related raw API references

The guide links to separate Braintree search and node-query guides and to external GraphQL and Relay resources. Those targets were not read for this entry and are navigation only; they do not establish exact schema equivalence, current ordering, cursor portability, SDK support or deployment availability.

## Raw Sources

- [[raw/braintree/graphql/guides/connections-2026-09-16|Braintree GraphQL Connections and Pagination]] - fully read 2026-09-16 website snapshot covering Relay-style connections, edge/node/cursor structure, `pageInfo`, slicing and cursor continuation
