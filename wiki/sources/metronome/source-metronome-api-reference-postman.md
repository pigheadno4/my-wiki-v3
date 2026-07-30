---
title: "Use Postman with Metronome"
type: source
date_ingested: 2026-07-30
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/postman"
raw_files:
  - "metronome/api-reference/postman-2026-07-13.md"
tags: [metronome, postman, openapi, api-authentication, customers]
---

## Overview

This setup guide shows how to explore the Metronome API in Postman without writing code. It covers importing Metronome's OpenAPI specification, configuring collection-level bearer-token authorization, and issuing an illustrative Create customer request.

## Key takeaways

- The documented prerequisites are a free Postman account, a Metronome account requested through Metronome, and a Metronome API token.
- Metronome directs users to import `https://api.metronome.com/v1/docs/openapi` as a Postman Link and set the import's Folder organization to Tags. The guide says this specification is always up to date, but provides no version or snapshot identifier.
- The imported collection uses Bearer Token authentication. The guide recommends a `{{api_token}}` Postman variable whose value is scoped to the `Metronome` collection.
- Before testing Create customer, the request must use the `{{api_token}}` bearer-token variable. The shown body and response are an example only; this guide does not define the endpoint's complete request or response contract.

## Setup flow

### Prerequisites

Before starting, create a free Postman account, request a Metronome account, and generate a Metronome API token. The page does not state how long that token remains valid, which permissions it has, or how it is rotated or revoked.

### Import the API collection

In Postman, use **File** > **Import**, choose **Link**, and enter Metronome's OpenAPI specification URL. In the next pane, open advanced settings and set **Folder organization** to **Tags**. The documentation describes the specification as always current; it does not provide a pinned version, revision identifier, or reproducible import snapshot.

A Postman collection groups requests in folders. The page notes that a collection can be forked for version control and collaboration, but it does not supply a Metronome-maintained collection export or describe change-management practices for a fork.

### Configure authorization

Select the imported collection's top-level **Metronome** folder and set its authorization type to **Bearer Token**. The guide recommends entering `{{api_token}}`, adding the variable when Postman reports it unresolved, assigning the Metronome API token as its value, and selecting **Collection: Metronome** scope.

The page then instructs the user to open **Customers** > **POST Create customer**, set that request's authorization type to **Bearer Token**, and confirm its Token field is `{{api_token}}` before saving. It does not say whether collection-level authorization alone should be inherited by every imported request.

### Illustrative request

The test request uses a JSON body containing `"name": "Example-Customer"`. The displayed response contains `data.id`, `data.external_id`, and `data.name`; because the page supplies no schema, these fields and values should not be treated as a complete API specification.

## Documented boundaries

- This page is a Postman configuration guide, not the authorization or customer-creation API reference. It does not document token permissions, expiration, storage controls, revocation, request errors, response status codes, or retry behavior.
- The claim that the OpenAPI specification is always up to date does not establish a versioning or compatibility policy.
- No security warning about exposing a token in a Postman variable is stated in this source; any token-storage policy must come from separate Metronome or Postman documentation.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-integrations]], [[metronome-customers-and-contracts]]
- Related sources: [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-customers-create-a-customer]]

## Raw Sources

- [[raw/metronome/api-reference/postman-2026-07-13|2026-07-13 snapshot — Postman OpenAPI import, collection authorization, and Create customer test]]
