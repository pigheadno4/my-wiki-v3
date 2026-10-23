---
title: "Adyen Customer Area IAM"
type: concept
category: technology
tags: [adyen, iam, customer-area, rbac, sso, mfa]
---

## Definition

Adyen's IAM guidance recommends role-based access control, single sign-on and multifactor authentication for user access across all integration types. It says Customer Area accounts, roles and user permissions can be structured for RBAC; the Customer Area supports SAML 2.0 SSO and MFA with an authenticator app or SMS. The page recommends documenting and regularly reviewing RBAC. [[source-adyen-docs-development-resources-security-iam]]



## Customer Area login requirement

Adyen's dated Customer Area MFA account guide says users must set up MFA or SSO. It permits one authentication method per device and two registered MFA devices; SMS enrollment is live-environment only. Merchant admins can remove organization users' registered devices, while the user must register a new device at the next login. This is a stated account-guide requirement and procedure, not proof of a particular user's factor enrollment, working login or recovery from lockout. [[source-adyen-docs-account-multifactor-authentication]]
## Evidence boundary

The 2026-09-15 captured page explicitly presents incomplete, non-definitive security guidance. Support for a capability does not prove a merchant has enabled it, that SSO deprovisioning or MFA enforcement is configured, or that access is secure. These are Customer Area **user** access controls; web service API credential identity, roles, account scope and key lifecycle remain under [[adyen-api-access]].

## Sources

- [[source-adyen-docs-about-our-customer-area]] — 2026-09-15-captured dated BPCA-to-unified-Customer-Area migration guide for TEST/LIVE setup, company/merchant role scope, access copying and deep-link changes; timeline remains indicative.


- [[source-adyen-docs-new-customer-area-menu]] — 2026-09-15 Customer Area menu-transition and old-to-new page navigation guide; rollout/menu visibility does not establish user roles or successful operations.


- [[source-adyen-docs-account-single-sign-on]] — 2026-09-15 Customer Area SAML 2.0 SSO overview and navigation to setup, SSO-user creation, existing-user migration and login guidance; no merchant enablement or actual access outcome established.


- [[source-adyen-docs-account-single-sign-on-log-in-with-sso]] — Customer Area user email-verification and IdP SSO login guide, with separate test/live verification and no role or session-entitlement proof (webpage snapshot, 2026-09-15).


- [[source-adyen-docs-account-users-partner-users]] — 2023-modified, 2026-09-15-captured Customer Area partner-user guide for Partner Portal email matching, merchant-selected account/role grants, later edits and reversible revocation.


- [[source-adyen-docs-account-multifactor-authentication]] — 2026-09-15 Customer Area MFA account guide for MFA-or-SSO login requirement, app/live-only SMS enrollment, two-device limit, and scoped device removal and re-registration.


- [[source-adyen-docs-account-email-log-in]] — 2026-09-15 Customer Area email-login migration guide for Merchant admin control, separate test/live scope, email/SSO uniqueness, pending-user access and unfinished-only cancellation.


- [[source-adyen-docs-account-single-sign-on-set-up-sso]] — 2026-09-15 Adyen Customer Area SAML 2.0 SSO setup guide for company-account configuration, IdP metadata and SSO-user creation.


- [[source-adyen-docs-account-single-sign-on-migrate-users-to-sso]] — 2026-09-15 snapshot of optional Customer Area user migration to preconfigured SSO, with separate test/live scope, email uniqueness, admin-role prerequisites, pending-user access interruption and unfinished-only cancellation.


- [[source-adyen-docs-account-users]] — 2026-09-15 Customer Area user-management guide for role/account grant ceilings, creation and duplication, trusted login IPs, reversible deactivation, and company user reports.


- [[source-adyen-docs-development-resources-security-iam]] — Adyen RBAC, SAML 2.0 SSO and MFA guidance for Customer Area user access (2026-09-15 snapshot).
