---
title: "Adyen Legal Entity Management API v4 overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/overview"
raw_files:
  - "adyen/api-explorer/legalentity/latest/overview/2026-09-15.md"
tags: [adyen, legal-entity-management, api-reference, verification]
---

## Overview

This 2026-09-15 API Explorer overview identifies Legal Entity Management API **v4** as an API for managing legal entities containing information required for verification. It lists routes for legal entities, business lines, verification documents, transfer instruments, onboarding links/themes, Terms of Service, PCI questionnaires, tax electronic-delivery consent and periodic data review. The route catalog is navigation, not the individual endpoint contracts or evidence of verified status.

## Key takeaways

- Each request must use an API key in `X-API-Key`. The page directs platform/marketplace integrations to Customer Area key generation and Issuing integrations to Balance Platform Customer Area; it specifies a separate live key and live base URL. These statements do not establish a named role or actual credential access.
- The captured version suffix is `/lem/v4`; test base is `https://kyc-test.adyen.com/lem/v4` and the stated live base is `https://kyc-live.adyen.com/lem/v4`. The URL's `latest` segment does not prove v4 remains the current version after capture. Existing [[source-adyen-docs-platforms-manage-legal-entities|Platforms legal-entity guidance]] covers v3, so version-specific behavior must remain with its own source.
- The page states dated rate limits of 700 requests per five seconds in live, 200 per five seconds in test, and five failed requests per ten seconds. It says excess requests are blocked until the time frame ends; it gives no per-route exception or response contract here.
- The listed POST/PATCH/DELETE/GET route summaries do not establish required request fields, response statuses, deletion consequences, verification approval, consent completion, PCI compliance, onboarding completion, propagation timing or money movement.

## Detail locators

- `Authentication`, `Versioning`, `Rate limits`, `Going live` → key header, version suffix, snapshot limits and environment-specific key/base guidance.
- `## Servers` and `## Endpoints` → test base and v4 route catalog; consult each endpoint's own reference for its contract.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — platform verification and account context.
- [[adyen-issuing]] — separately mentioned key-generation context.
- [[adyen-api-access]] — general API credential context.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/overview/2026-09-15|2026-09-15 captured API Explorer overview]]
