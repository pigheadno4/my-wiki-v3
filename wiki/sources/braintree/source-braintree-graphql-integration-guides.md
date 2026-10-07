---
title: "Braintree GraphQL Integration Guides Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides"
raw_files:
  - "braintree/graphql/integration_guides-2026-09-16.md"
tags: [braintree, graphql, integration-guides, api-schema, sandbox]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree|Braintree]] website page explains how to use the GraphQL integration-guide collection: each available guide is intended to give feature-specific implementation context and an end-to-end path. It is an orientation and navigation page, not an inventory proving that every API feature has a guide, or evidence of current feature availability, merchant eligibility, enablement, exact deployed schema, SDK/runtime behavior, request execution, or payment outcomes.

## Key takeaways

- Availability is guide-specific. The page directs readers to check the top of each guide because a feature can be limited by merchant, region, or use case; this dated snapshot does not establish present eligibility or enablement.
- The guides are intended to explain feature implementation end to end, but their examples deliberately omit fields that are irrelevant to the illustrated use case. Use the linked schema reference for the available-field inventory rather than treating an example as an exhaustive or exact deployed schema.
- The linked API Explorer can browse the schema and execute GraphQL requests in a Sandbox environment from the browser. That route is navigation, not proof of credentials, account access, production behavior, successful execution, or payment results.
- A missing guide is ambiguous: the page says either the feature is absent from the API or its guide has not yet been written. It directs readers to the schema reference and changelog, then to support if the schema also lacks the relevant feature; if the feature is present, it points to SDK documentation plus the schema reference for the relevant calls. Those linked targets were not read for this entry and govern their own current details.

> [!warning] Snapshot and example boundaries
> Confirm each guide's stated availability and the current schema before implementation. Do not infer present merchant, region, use-case or production eligibility from inclusion in this collected guide section, or infer complete fields, deployed behavior, successful requests, payments, settlement or funding from its pared-down examples or Sandbox Explorer route.

## Detail locators

- Guide-section purpose and incomplete guide coverage: opening paragraph, raw line 16.
- Per-guide merchant, region and use-case availability check: `AVAILABILITY`, raw lines 19–20.
- End-to-end intent, pared-down examples and schema-reference route for available fields: `## How to use these guides`, raw lines 23–25.
- Browser-based API Explorer and explicit Sandbox execution environment: `## How to use these guides`, raw line 27.
- Missing-guide ambiguity and schema, changelog, support and SDK-documentation decision route: `## If you don't see the guide you're looking for`, raw lines 30–36.

## Related

- [[braintree-payment-platform]]
- [[braintree]]
- [[source-braintree-graphql-guides]] — separate Braintree GraphQL landing and basic-orientation source.

## Related raw API references

- Braintree GraphQL schema reference (`/braintree/graphql/reference`) — linked navigation only; not read as evidence for this entry.
- Braintree GraphQL API Explorer (`/braintree/graphql/explorer`) — linked navigation only; the overview identifies its Sandbox environment, but this entry does not establish access or execution.
- Braintree GraphQL API changelog (`https://github.com/braintree/graphql-api/blob/master/CHANGELOG.md`) — linked navigation only; not exact-commit evidence here.
- Braintree SDK guides (`/braintree/docs/guides/overview/`) and support (`/braintree/help/`) — linked fallback routes only; not read as behavior, eligibility or support-outcome evidence.

## Raw Sources

- [[raw/braintree/graphql/integration_guides-2026-09-16|Braintree GraphQL Integration Guides Overview (fetched 2026-09-16)]]
