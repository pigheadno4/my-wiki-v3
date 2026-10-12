---
title: "Adyen API Security"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/security/api-security"
raw_files:
  - "adyen/docs/development-resources/security/api-security/2026-09-15.md"
tags: [adyen, api-security, authentication, rate-limiting, throttling]
---

## Overview

This Adyen guidance page summarizes API-security practices for all Adyen integration types. It focuses on authentication and on rate limiting and throttling, while routing detailed Adyen authentication, credential, partner OAuth, client-side authentication, and TLS topics to dedicated documentation.

## Key takeaways

- The page is guidance only, not a complete security checklist or definitive advice. Its stated integration scope is all Adyen integrations.
- For APIs an integration owns, the page presents API keys, OAuth 2.0, and multifactor authentication as approaches to consider. API keys must be protected, rotated, and kept out of client-side code; MFA is framed as something an application can encourage or require, especially for sensitive data.
- For requests to Adyen APIs, the page routes merchants to API credentials created in the Customer Area and supplied through the relevant HTTP request header. It separately describes partner OAuth as delegated access to specific merchant-account resources after the merchant authorizes the request, using the resulting token for requests on that merchant's behalf.
- Rate limiting and throttling are presented as protections against misuse including denial-of-service attacks, brute-force attacks, and scraping. The page recommends considering distributed counters across API gateways and traffic- and behavior-sensitive throttling, but gives no numeric limits or provider-runtime guarantees.
- The page also says to transmit data over HTTPS with the correct TLS configuration and to conduct security audits and penetration tests, addressing discovered issues immediately.

> [!warning] Evidence boundary
> This unversioned snapshot is general security guidance, not a complete security standard or proof that an integration is secure. It does not establish Adyen's numeric rate limits or throttling behavior, current account or OAuth eligibility, successful authentication or authorization, correct credential or TLS deployment, API availability, or payment execution. Follow the dedicated linked documentation and current security requirements for implementation details.

## Detail locators

- Guidance-only disclaimer and focus areas: lines 19-24 under `# API security`.
- Applicability to all Adyen integrations: `## Requirements`.
- API-key, OAuth 2.0, and MFA considerations for an integration's own APIs: `## API authentication`, lines 40-46.
- Adyen API credential and partner OAuth routes: `## API authentication`, lines 48-52.
- Purpose of rate limiting and throttling: `## Rate limiting and throttling`, lines 54-56.
- Distributed rate limiting and dynamic throttling considerations: `## Rate limiting and throttling`, lines 58-62.
- HTTPS/TLS and audit/testing guidance: `## Rate limiting and throttling`, lines 64-66.
- Authentication and client-side-authentication next steps: `## See also`.

## Related

- Company: [[adyen]]
- Concept: [[adyen-api-access]]

## Related raw API references

- [[raw/adyen/docs/development-resources/api-authentication/2026-09-15|API authentication types]]
- [[raw/adyen/docs/development-resources/api-credentials/2026-09-15|API credentials]]
- [[raw/adyen/docs/partners/oauth/2026-09-15|OAuth for partners]]
- [[raw/adyen/docs/development-resources/client-side-authentication/2026-09-15|Client-side authentication]]
- [[raw/adyen/docs/development-resources/security/sensitive-data/tls/2026-09-15|Transport Layer Security configuration]]

## Raw Sources

- [[raw/adyen/docs/development-resources/security/api-security/2026-09-15|Adyen API security]] — complete collected guidance for authentication, rate limiting and throttling, HTTPS/TLS, and security testing
