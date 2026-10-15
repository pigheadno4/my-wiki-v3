---
title: "Adyen Customer Area IAM"
type: concept
category: technology
tags: [adyen, iam, customer-area, rbac, sso, mfa]
---

## Definition

Adyen's IAM guidance recommends role-based access control, single sign-on and multifactor authentication for user access across all integration types. It says Customer Area accounts, roles and user permissions can be structured for RBAC; the Customer Area supports SAML 2.0 SSO and MFA with an authenticator app or SMS. The page recommends documenting and regularly reviewing RBAC. [[source-adyen-docs-development-resources-security-iam]]

## Evidence boundary

The 2026-09-15 captured page explicitly presents incomplete, non-definitive security guidance. Support for a capability does not prove a merchant has enabled it, that SSO deprovisioning or MFA enforcement is configured, or that access is secure. These are Customer Area **user** access controls; web service API credential identity, roles, account scope and key lifecycle remain under [[adyen-api-access]].

## Sources

- [[source-adyen-docs-development-resources-security-iam]] — Adyen RBAC, SAML 2.0 SSO and MFA guidance for Customer Area user access (2026-09-15 snapshot).
