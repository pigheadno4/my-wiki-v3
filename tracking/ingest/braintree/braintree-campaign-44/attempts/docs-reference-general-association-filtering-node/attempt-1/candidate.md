---
title: "Braintree Association Filtering (Node.js)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/association-filtering/node"
raw_files:
  - "braintree/docs/reference/general/association-filtering/node-2026-09-16.md"
tags: [braintree, node-js, association-filtering, customers, api-responses]
---

## Overview

This Braintree Node.js-routed reference explains limited-release association filtering: a supported API request can include a specific association filter ID so the response excludes configured associated data while retaining the excluded fields as empty arrays or null values.

## Key takeaways

- Association filtering was documented as a limited release for select merchants, with a contact route for questions.
- When a supported API request receives a specific filter ID, the response object excludes the fields named by that filter; those fields remain present as empty arrays or null values.
- Braintree says filtering unnecessary associated data could improve performance, with the possible improvement depending on how much data is associated with the object.
- The captured customer-filter table maps `f8124ed8` to excluding subscriptions and `353f78cc` to excluding addresses, custom fields, payment methods and subscriptions.
- The captured `Supported API requests` section lists no methods. A separate example shows `gateway.customer.find()` with `353f78cc` in callback and Promise forms, but the empty list is not reconstructed into a broader supported-method catalog.

> [!warning] Availability and captured-request boundary
> Treat the select-merchant limited release as a prerequisite. The pinned page does not provide the promised supported-request list, so use its displayed customer-find example only as an example and do not generalize support to other object methods.

## Detail locators

- Limited-release availability and contact route: `# Association Filtering > **AVAILABILITY**`, lines 17-18.
- Purpose of filtering associated data: `# Association Filtering`, lines 20-21.
- Filter-ID request condition and empty-array/null response behavior: `## How it works`, lines 24-26.
- Intended use and qualified performance statement: `## When to use association filtering`, lines 29-32.
- Empty captured request inventory: `## Supported API requests`, lines 33-35.
- Customer filter IDs and excluded association fields: `## Supported objects and filters`, lines 36-41.
- `gateway.customer.find()` callback and Promise examples using `353f78cc`: `## Example`, lines 44-57.
- Empty captured validation-error table: `## Validation errors`, lines 59-63.

## Scope and evidence boundary

This is a 2026-09-16 snapshot of an unversioned Braintree Node.js-routed website page: it identifies the Node server-SDK family and displayed examples, not an exact npm package or runtime version, environment-specific availability, present-day merchant enablement, measured latency gain, or successful API/payment execution.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/association-filtering/node-2026-09-16|Braintree Node.js association-filtering reference]] - complete collected page covering limited-release availability, filter behavior, customer filter IDs, examples and captured empty sections
