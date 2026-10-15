---
title: "Adyen identity and access management guidance"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/security/iam"
raw_files:
  - "adyen/docs/development-resources/security/iam/2026-09-15.md"
tags: [adyen, iam, customer-area, rbac, sso, mfa]
---

## Overview

This [[adyen]] page gives identity and access management guidance for all Adyen integrations. It discusses role-based access control (RBAC), single sign-on (SSO), and multifactor authentication (MFA) for application and Customer Area user access. Use [[adyen-customer-area-iam]] for this user-access route; [[adyen-api-access]] covers separate web service API credentials and their permission/key lifecycle.

## Key takeaways

- The page expressly says its security measures are guidance only, incomplete, and not definitive advice. It recommends role-based permissions, SSO, and MFA but does not show that any merchant has configured them. See **Identity and access management**, raw lines 15–27.
- RBAC assigns user permissions by role or function. The page recommends limiting access to what users need, documenting the RBAC implementation, and reviewing it regularly; it says Customer Area accounts, roles, and user permissions can be arranged accordingly. These are user-access practices, not an API credential-role catalog. See **Role-based access control**, raw lines 37–45.
- The Customer Area supports SSO based on **SAML 2.0**. The page describes extending an organization's SSO solution to the Customer Area, including removing a departing employee's access through that solution, as an example benefit. It does not establish an organization's SSO configuration or its account's actual sign-in policy. See **Single sign-on**, raw lines 47–53.
- The Customer Area supports MFA through an **authenticator app or SMS**. The captured page says each user can set up one authentication method per device and register two devices. This support statement is not proof that MFA is enabled or enforced for a given user/account. See **Multifactor authentication**, raw lines 55–59.

## Detail locators

- Guidance-only warning, three recommended practices, all-integration scope: raw lines 15–35.
- RBAC role/function model, least privilege, review, Customer Area setup: **Role-based access control**, raw lines 37–45.
- SSO definition, SAML 2.0 support and employee-removal example: **Single sign-on**, raw lines 47–53.
- MFA purpose and supported Customer Area methods/device count: **Multifactor authentication**, raw lines 55–59.
- Account structure, SSO setup and MFA setup navigation: **See also**, raw lines 61–65.

## Related

- Company: [[adyen]]
- Concept: [[adyen-customer-area-iam]]
- Separate API credential lifecycle: [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/docs/development-resources/security/iam/2026-09-15|Adyen IAM guidance]] — full pinned 2026-09-15 snapshot for RBAC, SAML 2.0 SSO and MFA guidance
