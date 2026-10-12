---
title: "Adyen API Authentication Types"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/api-authentication"
raw_files:
  - "adyen/docs/development-resources/api-authentication/2026-09-15.md"
tags: [adyen, api-authentication, api-key, basic-authentication]
---

## Overview

This unversioned [[adyen]] documentation snapshot explains the two authentication mechanisms it lists for requests to Adyen APIs: API-key authentication and HTTP Basic authentication. It distinguishes library-managed authentication from the headers that a direct API caller must construct.

## Key takeaways

- Every request to Adyen APIs must be authenticated. The page lists API-key authentication and Basic authentication as the available types.
- When an Adyen API library is used, the integration supplies the credential for its selected authentication type and the library handles authentication. A direct API caller must instead apply the documented authentication header itself.
- API-key authentication sends the API key in the `x-API-key` HTTP request header. The page routes API-key generation to the Customer Area credential workflow.
- Basic authentication sends a username and password through the `Authorization` request header. Its credential value is the base64-encoded `username:password` combination; the page routes generation of that username and password to the Customer Area credential workflow.

> [!warning] Evidence boundary
> This short snapshot documents request-header mechanics and navigation to credential generation. It does not establish credential roles or account scope, secret-storage and rotation controls, current account eligibility, correct deployment, successful authentication or endpoint authorization, API availability, or payment execution. The displayed requests are examples, not proof of a successful call.

## Detail locators

- Authentication requirement, listed types, and library-versus-direct-call responsibility: lines 19-24.
- API-key header name and example request: `## API key authentication`, lines 26-39.
- Basic-authentication header, credential encoding, and example request: `## Basic authentication`, lines 41-60.
- Credential-generation route: `## Next steps`, lines 62-66.

## Related

- Company: [[adyen]]
- Concept: [[adyen-api-access]]

## Related raw API references

- [[raw/adyen/docs/development-resources/api-credentials/2026-09-15|API credentials]]

## Raw Sources

- [[raw/adyen/docs/development-resources/api-authentication/2026-09-15|Adyen API authentication types (2026-09-15)]] — complete collected page for API-key and Basic request-header authentication and the library-versus-direct-call boundary
