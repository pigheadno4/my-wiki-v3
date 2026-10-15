---
title: "Manage Customer Area users | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/users"
raw_files:
  - "adyen/docs/account/users/2026-09-15.md"
tags: [adyen, customer-area, users, roles, account-access]
---

## Overview

This 2026-09-15 snapshot of Adyen's **Customer Area user** administration guide covers viewing roles, creating or duplicating users, changing account and role access, trusted login IPs, deactivation, and a company user report. It is about human logins and permissions, distinct from web service API credentials and API-key lifecycle under [[adyen-api-access]]. See [[adyen]] and [[adyen-customer-area-iam]].

## Key takeaways

- User permissions combine assigned roles and accessible merchant accounts. The initial admin login has common roles and access to linked merchant accounts; it is not described as having every possible role. Creating, duplicating, editing, and deactivating users requires **Merchant admin** or **Merchant user management** role.
- A creator may grant only merchant accounts/account groups and roles they already hold. Giving an account group does not expand the new user's access beyond the creator's member-account access. A duplicated user can therefore receive fewer permissions than the original user. If neither creator nor admin has a needed role, the guide directs contact with Adyen Support.
- Creation offers SSO (recommended) or email/password. The new-user verification/MFA setup link lasts two weeks; a resent email-verification link and a password-reset link last 24 hours each. The page does not prove the merchant has configured SSO or MFA enforcement.
- A user's trusted login IP range blocks login attempts outside it; the page states a maximum of 45 trusted IP addresses. Under a **Delete an existing user** heading, the actual action is **deactivate**, which removes Customer Area access and can be reversed with **Reactivate user**. The currently logged-in user cannot deactivate themself.
- The **Users within a company** report includes each user's roles and last Customer Area login. Generating it requires **Merchant admin** or **Merchant report** role; the report can target one user or all company users and exclude accounts, account groups, or roles. The snapshot does not establish any particular account's users, permissions, or audit state.

## Detail locators

- Customer Area identity, roles, account access and initial admin scope: lines 15–30.
- Own-role inspection: `View your own roles`, lines 32–39.
- Creation roles, SSO/email choice, account-group/role grant ceilings, setup link: `Create a user`, lines 41–67.
- Resent verification and password-reset 24-hour links: lines 69–91.
- Duplicate-role limit and creation permissions: `Duplicate an existing user`, lines 93–113.
- Edit permissions and role requirement: `View and change user permissions`, lines 115–129.
- Trusted login IP limit and blocking effect: lines 131–143.
- Reversible deactivation and no self-deactivation: `Delete an existing user`, lines 145–160.
- Company user report, distinct report role, and selectable scope: lines 162–187.

## Related

- [[adyen-customer-area-iam]] — provider user-access controls.
- [[adyen-api-access]] — separate web service credential permissions and key lifecycle.

## Raw Sources

- [[raw/adyen/docs/account/users/2026-09-15|Manage users (2026-09-15)]]
