---
title: "Braintree Server SDK Migration Guide (Node.js)"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/server-sdk-migration-guide/node"
raw_files:
  - "braintree/docs/reference/general/server-sdk-migration-guide/node-2026-09-16.md"
tags: [braintree, node-js, server-sdk, migration, sdk-versioning]
---

## Overview

This collected Braintree guide is a historical migration route for Node integrations moving from Server SDK version 2.24.0 or below to major version 3. It identifies the main runtime, gateway-initialization, search-result and exception changes; it is not a universal current upgrade requirement, and the page says a new integration starting on the latest SDK can skip this guide.

## Key takeaways

- Starting with Node SDK 3.0.0, the documented targets are Node 10+ and npm CLI 6+. These are v3 migration-era targets, not evidence of current runtime support.
- The prior gateway-setup function is rendered as `functionconnect()` in the collected page. The guide says it was deprecated in SDK 2.15.0 and removed in 3.0.0, and replaces it with construction of a `braintree.BraintreeGateway` instance.
- The `CreditCardGateway` `expired` and `expiringBetween` methods previously returned arrays of credit-card IDs because of a bug. The guide says the updated methods return either an iterable response or a stream containing full credit-card result objects.
- The migration guide says Down For Maintenance exceptions were renamed Service Unavailable exceptions and that additional timeout exceptions were added to clarify whether the source is the client request or gateway response.

## Detail locators

- Node applicability threshold and skip condition for new latest-SDK integrations: `# Server SDK Migration Guide > **AVAILABILITY**`, lines 17-26.
- Semantic-versioning purpose and the separate changelog route: `## Overview`, lines 29-33.
- Node 10+ and npm CLI 6+ targets for SDK 3.0.0: `## SDK major version 3 > ### Node versions`, lines 39-41.
- Deprecated and removed gateway-setup function plus replacement constructor example: `## SDK major version 3 > ### Creating a gateway instance`, lines 42-53.
- `expired` and `expiringBetween` result-shape correction: `## SDK major version 3 > ### Search methods for expiring credit cards updated`, lines 55-57.
- Renamed availability exception and additional timeout categories: `## SDK major version 3 > ### Exceptions`, lines 60-66.

## Evidence limitations

> [!warning] Historical migration scope
> This page describes the transition from Node SDK 2.24.0 or below to major version 3. It does not establish the currently supported SDK major version, Node runtime, npm version, deprecation deadline or upgrade path from later releases. Use current package and lifecycle authorities for present-day planning. The collected rendering also concatenates the legacy gateway function name with surrounding prose, so this source preserves that limitation instead of treating the page as clean API-signature evidence.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/server-sdk-migration-guide/node-2026-09-16|Braintree Node.js Server SDK Migration Guide]] - complete collected guide for the version-2.24.0-and-below to major-version-3 migration scope
