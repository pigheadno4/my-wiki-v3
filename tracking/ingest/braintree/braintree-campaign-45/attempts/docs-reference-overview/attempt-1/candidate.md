---
title: "Braintree Reference Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/overview"
raw_files:
  - "braintree/docs/reference/overview-2026-09-16.md"
tags: [braintree, api-reference, client-sdk, server-api, forward-api]
---

## Overview

This unversioned [[braintree]] webpage, captured 2026-09-16, is a directory for Braintree reference material. It separates client references from server-side request and response references, and also routes readers to Forward API and general reference material. It is a documentation map for [[braintree-payment-platform]], not an executable API contract or proof of current SDK support, merchant enablement, request success, payment execution, settlement, or funding.

## Key takeaways

- The Client References section links Android, iOS and iOS Drop-in, JavaScript v3 Hosted Fields and Drop-In UI, and a separate JavaScript v2 route. Those snapshot labels and links do not identify exact package versions or establish current platform or SDK support; the JavaScript v2 route must not be presented as current v3 behavior.
- Server-side API Requests are organized by resource type for integration customization or call-level understanding, while Server-side Response Objects are presented for response-handling customization or object-level details. The overview does not supply request schemas, methods, response fields, error behavior, SDK-language scope, or transaction lifecycle semantics.
- The page warns that integrations may be affected by upcoming certificate changes and directs readers to a best-practices guide. It does not state which SDKs, versions, environments, certificates, dates, or mitigation steps are affected; follow the linked guidance and current provider evidence before acting.
- Forward API is listed as a separate reference category, and its use is expressly subject to eligibility. This directory does not establish production approval, configuration, destination acceptance, or payment execution.
- The General category routes to best practices, validation errors, processor responses, sandbox test values, third-party plugins, and other material; use the detailed references for those routine specifics.

## Detail locators

- Reference-directory identity: `# Reference Overview`, raw lines 14-16.
- Client reference inventory and visible JavaScript v2/v3 labels: `## Client References`, raw lines 19-26.
- Certificate-change warning and linked best-practices route: `## Server-side API Requests`, raw lines 29-35.
- Server-side response-object purpose: `## Server-side Response Objects`, raw lines 38-40.
- Forward API eligibility qualification: `## Forward API`, raw lines 43-45.
- General reference categories: `## General`, raw lines 48-50.

## Related

- [[braintree]] - provider company and broader source catalog
- [[braintree-payment-platform]] - main provider-level product and interaction route
- [[braintree-server-sdk]] - server-side SDK boundary and package-qualified evidence
- [[braintree-web-sdk]] - browser SDK boundary and exact-version evidence
- [[braintree-forward-api]] - eligibility-qualified forwarding retrieval hub

## Related raw API references

- [[raw/braintree/docs/reference/client-reference/javascript/v2/best-practices-2026-09-16|Braintree JavaScript v2 best practices]] - linked navigation-only route; not read as factual evidence for this source
- [Braintree certificate best-practices route](https://developer.paypal.com/braintree/docs/reference/general/best-practices/ruby) - linked navigation-only route; not read as factual evidence for this source, and no pinned raw is claimed here

## Raw Sources

- [[raw/braintree/docs/reference/overview-2026-09-16|Braintree Reference Overview (captured 2026-09-16)]]