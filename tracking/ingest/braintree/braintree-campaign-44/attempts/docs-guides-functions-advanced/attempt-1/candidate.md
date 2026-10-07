---
title: "Braintree Functions Advanced Topics"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/functions/advanced"
raw_files:
  - "braintree/docs/guides/functions/advanced-2026-09-16.md"
tags: [braintree, functions, runtime-context, environment-variables, javascript]
---

## Overview

This captured [[braintree|Braintree]] advanced-topics webpage is a documentation preview for the Braintree Functions runtime context: generated-configuration environment variables and the JavaScript argument supplied when a Function is invoked. It does not identify a client/server SDK or exact Functions runtime/package version, and the preview examples establish neither current availability nor deployed execution.

## Key takeaways

- The page says custom environment variables can be provided in the generated `config.yml`. Its YAML example places `HTTP_TIMEOUT` at the general level and gives `PAYMENT_URL` different values under `sandbox` and `production`; this is an illustrative configuration, not a complete configuration schema.
- A Function is described as receiving one JavaScript `context` object containing trigger-specific event data and structured Braintree metadata. The illustrated object uses `eventData` and `__metadata__`.
- The captured metadata table limits `environment` to `sandbox` or `production` and describes `invocationId` as identifying a Braintree Function execution and `requestId` as identifying the request that caused it, with both UUIDs intended for debugging and tracing.
- A separate JSON example uses `data` and `__meta.braintreeEnvironment` rather than the preceding `eventData` and `__metadata__.environment` names. The page does not explain their relationship, so the examples should not be treated as one normalized schema.

## Detail locators

- **Preview availability:** `AVAILABILITY`, raw lines 17–18.
- **Generated configuration and environment-qualified values:** `Runtime Context` > `Environment Variables`, raw lines 21–36.
- **Single JavaScript context argument and illustrated shape:** `Secrets` > `contextArgument`, raw lines 38–57.
- **Event-data route and metadata meanings:** `eventData`, raw lines 59–66.
- **Separate JSON example with alternate names:** `Examples` > `JSON`, raw lines 69–81.

## Related

- [[braintree]]
- [[braintree-payment-platform]] — main provider concept route for the collected Braintree Functions documentation previews.
- [[source-braintree-docs-guides-functions-cli-reference]] — separate preview reference for CLI operations and environment-qualified deployment.

## Raw Sources

- [[raw/braintree/docs/guides/functions/advanced-2026-09-16|Braintree Functions Advanced Topics (2026-09-16 snapshot)]]
