---
title: "Adyen API Credentials"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/api-credentials"
raw_files:
  - "adyen/docs/development-resources/api-credentials/2026-09-15.md"
tags: [adyen, api-credentials, authentication, access-control, key-rotation]
---

## Overview

This Adyen documentation page explains how web service API credentials identify an integration and how their API key or basic-authentication password, enabled roles, and account scope control API access. It covers Customer Area prerequisites and credential creation, rotation, environment separation, IP allowlisting, and deactivation.

## Key takeaways

- An API credential consists of a username, an API key used as a password for API requests, and enabled roles that define its permissions. Managing credentials in the Customer Area requires a user with either the **Manage API credentials** or **Merchant admin** role.
- Credential count is an access-design trade-off: fewer credentials reduce key-management overhead, while separate credentials can narrow permissions across channels, refund handling, systems, legal entities, or websites. These examples are recommendations and design options, not a required credential topology.
- By default, a credential created on a company account can reach that company account and all linked merchant accounts; one created on a merchant account is limited to that merchant account. The page also documents selecting only particular account groups and merchant accounts.
- Generating an API key activates the new key immediately and leaves the previous key active for 24 hours so systems can be updated. The previous key's expiry can be reset to 24 hours or forced to expire immediately. A generated key must be stored securely and cannot be copied again after leaving the page.
- Basic-authentication password rotation has a different cutover: generating a new password deactivates the old one immediately. Creating a separate credential is the documented option when both old and new basic-authentication credentials must remain active during a migration.
- Test and live credentials are separate: switching to live requires generating a new API key in the live Customer Area or using basic-authentication credentials from that environment.
- An allowed IP range restricts permitted requests to requests originating from that range. API credentials cannot be deleted; deactivation takes effect immediately, prevents requests using the credential, and can later be reversed by setting it active again.

> [!warning] Evidence boundary
> This collected, unversioned documentation snapshot describes credential administration and stated access controls. It does not prove current account eligibility, a user's Customer Area permissions, correct secret deployment, successful authentication, endpoint authorization, idempotency, API availability, or payment execution. Consult the separately collected authentication, credential-role, idempotency, and API-security pages for their own behavior and qualifications.

## Detail locators

- Credential identity, parts, and Customer Area management routes: `# API credentials`.
- Required Customer Area user roles: `## Requirements`.
- Credential-separation trade-offs and examples: `## Multiple API credentials`.
- Default company-versus-merchant scope and selectable account access: `## Create additional API credentials` and `## Manage API credential account scope`.
- API-key rotation, one-time visibility, live-environment generation, and previous-key expiry controls: `## Generate an API key` and `## Reset the expiry time of a previous API key`.
- Immediate basic-authentication password replacement and migration alternative: `## Generate a basic authentication password`.
- Role-based permission administration: `## Manage API permissions`.
- Request-origin restriction: `## Add an allowed IP range`.
- Non-deletability and immediate, reversible deactivation: `## Deactivate an API credential`.

## Related

- Company: [[adyen]]
- Concept: [[adyen-api-access]]

## Related raw API references

- [[raw/adyen/docs/development-resources/api-authentication/2026-09-15|API authentication]]
- [[raw/adyen/docs/development-resources/api-credentials/roles/2026-09-15|API credential roles]]
- [[raw/adyen/docs/development-resources/api-idempotency/2026-09-15|API idempotency]]
- [[raw/adyen/docs/development-resources/security/api-security/2026-09-15|API security]]

## Raw Sources

- [[raw/adyen/docs/development-resources/api-credentials/2026-09-15|Adyen API credentials]] — complete collected page for credential identity, creation, permission and account scope, key and password rotation, environment separation, IP allowlisting, and deactivation
