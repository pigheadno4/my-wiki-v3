---
title: "Libraries | Adyen Docs"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/libraries"
raw_files:
  - "adyen/docs/development-resources/libraries/2026-09-15.md"
tags: [adyen, api-libraries, server-side, checkout-api, terminal-api, testing]
---

## Overview

This Adyen documentation page is a merchant-facing directory for server-side API libraries in Java, PHP, C#, Node.js, Go, Python, and Ruby. It explains optional library use, managed-package installation, generated request models, built-in HTTP transport, and sample TEST-environment `/payments` requests. It also separates Terminal API library choices for cloud and local communications. The 2026-09-15 snapshot carries a 2023-05-19 `last_modified` value; language requirements and code samples here should not be treated as verified current package-version contracts.

## Key takeaways

- A library is optional. The page says libraries provide API-version coverage, generated request models, and an HTTP client. The merchant still configures the client, credentials, environment, merchant account, payment request and any request options in the language-specific example.
- For Terminal API cloud communications, the page lists C#, Go, Java, Node, PHP and Ruby wrappers. For local communications, it lists C#, Java and Node, saying these also protect local communications. This is a documented integration choice, not evidence that every library supports the same Terminal API transport.
- Each language tab gives requirements, package or download routes and a sample payment request. These are TEST examples using placeholder API keys, merchant accounts and test card details; they do not establish a successful payment or production eligibility. The prose repeatedly introduces a EUR 10 / minor-unit 1000 example, but some snippets use USD 1000 and the PHP request sets amount value 1500. Check the actual sample before copying an amount or currency.
- Idempotency keys appear in several sample requests and are marked optional in the Node.js example. The sample is not an assertion that every payment call has the same idempotency requirement. Use the dedicated API idempotency documentation for the request contract.

## Detail locators

- `## How it works` — optional library role, generated models, Terminal API cloud/local choices and built-in HTTP client.
- `## Available libraries` / `### Tab: Java`, `### Tab: PHP`, `### Tab: C#`, `### Tab: NodeJS`, `### Tab: Go`, `### Tab: Python`, `### Tab: Ruby` — language-specific requirements, installation, sample TEST calls and example integrations.
- `## Next steps` — API integration, payment methods, webhooks and modification navigation.

## Related

- Company: [[adyen]]
- Generation and release provenance: [[adyen-sdk-automation]]
- Version-qualified library baselines: [[adyen-node-api-library]], [[adyen-php-api-library]]
- Related request contract: [[adyen-api-idempotency]]

## Raw Sources

- [[raw/adyen/docs/development-resources/libraries/2026-09-15|2026-09-15 snapshot — Adyen server-side libraries directory]]
