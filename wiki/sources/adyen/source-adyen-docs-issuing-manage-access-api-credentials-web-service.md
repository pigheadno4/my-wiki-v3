---
title: "Adyen balance-platform API credentials"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-access/api-credentials-web-service"
raw_files:
  - "adyen/docs/issuing/manage-access/api-credentials-web-service/2026-09-15.md"
tags: [adyen, issuing, platforms, api-credentials, balance-platform]
---

## Overview

This 2026-09-15-captured Adyen guide explains balance-platform web-service and Legal Entity Management (LEM) API credentials: creating, rotating, permissioning and deactivating them in Customer Area. **Scope caveat:** although filed under the Issuing path, its Requirements table specifies an **Adyen for Platforms** integration and Balance platform admin Customer Area role. Treat it as the page's stated procedure, not proof that every Issuing account can use the same controls. [[adyen]] [[adyen-issuing]]

## Key takeaways

- A credential has a username, API key and permissions/roles. Balance-platform setup creates default credentials. Web-service users authenticate Configuration, Transfers, Session Authentication for Platform Experience, and conditionally Capital API requests; LEM users authenticate Legal Entity Management and Session Authentication for Onboarding components. The user types, API purposes and username patterns are at raw lines 19-52; Capital needs additional configuration.
- Additional web-service or LEM credentials are created at the **company account** level in Customer Area. Adyen frames fewer credentials as simpler to operate and extra credentials as a way to segment permissions, including sensitive PIN/payment-instrument reveal. Test credentials do not carry to live: create new credentials in live Customer Area. See raw lines 54-127.
- Every web-service and LEM user has its own API key. Generating a new key activates it immediately; the previous key remains active for 24 hours, can have its expiry reset to 24 hours or be expired immediately, and cannot be copied again after leaving the generation page. A new key for live must be generated in live Customer Area. See raw lines 129-176.
- Basic authentication is an alternative **if** used. A newly generated basic-auth password deactivates the previous one immediately; the guide suggests creating a separate credential if overlap is needed during migration. The password also cannot be copied after leaving the page, and live requires live basic-auth credentials. See raw lines 178-206.
- Web-service permissions are enabled roles, with at least one role required. Credentials cannot be deleted; deactivation makes their API keys unusable. These are distinct actions from key rotation. See raw lines 208-232.

## Detail locators

- Default user types, username formats and API coverage: raw lines 42-52.
- Customer Area procedures to create web-service and LEM credentials: raw lines 65-127.
- API-key generation and previous-key expiry controls: raw lines 129-176.
- Basic-auth password, roles and deactivation procedures: raw lines 178-232.

## Related

- [[adyen-issuing]] — Issuing route; note the page's Platforms-only requirement.
- [[adyen-api-access]] — generic Adyen API-access context.
- [[source-adyen-docs-issuing-integration-checklist]] — Issuing test/live credential sequence.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-access/api-credentials-web-service/2026-09-15|Adyen balance-platform API credentials, captured 2026-09-15]]
