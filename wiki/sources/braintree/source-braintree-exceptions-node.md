---
title: "Braintree Exceptions (Node.js)"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/general/exceptions/node"
raw_files:
  - "braintree/docs/reference/general/exceptions/node-2026-09-16.md"
tags: [braintree, node-js, server-sdk, exceptions, timeouts]
---

## Overview

This Braintree Node.js reference shows callback and Promise patterns for handling server-SDK exceptions and separates credential, authorization, webhook, lookup, server, client-library, request-volume, version, timeout and availability categories. Its timeout distinctions are important for recovery decisions because a custom SDK timeout does not establish that the gateway operation failed.

## Key takeaways

- Node.js integrations can inspect an exception in either a callback error branch or a Promise `catch`; the examples expose `type`, `name` and `message`. The page says its exception list tracks the latest server SDKs and sends older-version integrations to the migration guide, so names and handling remain SDK-version scoped.
- Authentication errors mean the API keys are incorrect. Authorization errors instead cover a key whose owning user role cannot perform the attempted action, and can also result from malformed submitted data. Exact classes and category explanations are located under the corresponding error headings.
- A not-found exception applies when the record being operated on cannot be found, but an invalid reference or association is documented as a validation error instead. Server, unexpected-client-library, unsafe-request-volume, unsupported-library-version and service-unavailable categories have separate headings and should not be collapsed into one outcome or recovery rule.
- The documented timeout categories identify different boundaries: a custom server-SDK timeout, Braintree timing out while delivering a response, or Braintree timing out while waiting for the complete request from the merchant server. Only the search-call gateway-timeout passage suggests an action—breaking a large search into smaller batches.

## Detail locators

- Callback and Promise handling, exposed exception properties and older-SDK route: `# Exceptions > ## Handling exceptions`, lines 23-57.
- Credential, role/malformed-data, webhook, lookup and validation distinctions: `## Authentication Error` through `## Not Found Error`, lines 60-96.
- Server, client-library, volume-limit and unsupported-library-version categories: `## Server Error` through `## Upgrade Required Error`, lines 99-124.
- Custom-limit, gateway-delivery and incomplete-request timeout categories: `## Timeouts`, lines 127-148.
- Downstream availability category: `## Service Unavailable Error`, lines 151-155.

## Evidence limitations

> [!warning] Timeout is not transaction-outcome or retry evidence
> A custom server-SDK timeout can occur even when the request later succeeds within Braintree's stated 60-second gateway timeout. The page does not provide a general safe-retry rule, establish the outcome of a timed-out mutation, or say that every gateway, request or service-availability exception is retryable. Determine operation state and recovery through the applicable operation-specific authority before repeating a request.

> [!note] Operational issue route
> Braintree says some exceptions may indicate a known API issue and recommends its status page's Braintree Product and API sections for current issues or scheduled maintenance. This collected page does not itself establish current service status.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-server-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/general/exceptions/node-2026-09-16|Braintree Exceptions (Node.js)]] - complete collected page covering Node.js handling patterns, exception categories and timeout boundaries
