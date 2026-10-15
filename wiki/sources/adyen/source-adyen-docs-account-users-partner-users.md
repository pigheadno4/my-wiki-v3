---
title: "Manage partner users | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/users/partner-users"
raw_files:
  - "adyen/docs/account/users/partner-users/2026-09-15.md"
tags: [adyen, customer-area, partner-users, account-access, user-roles]
---

## Overview

This Adyen partner-user guide (last modified 2023-06-19; collected 2026-09-15) describes how a merchant grants an existing Adyen Partner Portal user selected Customer Area company or merchant-account access and roles, then later edits or revokes that access. Partner Portal identity and merchant-granted Customer Area access are distinct. The page documents an administrator workflow, not an actual user creation or access change. [[adyen-customer-area-iam]]

## Key takeaways

- To add a partner user, the acting merchant user needs the **Merchant admin** role, access to the relevant company or merchant account, and all roles and permissions the partner is requesting. The entered email must match the partner's existing Adyen Partner Portal account. The merchant then chooses one or more accounts and roles, reviews the grant, and confirms responsibility; the page does not describe a separate partner request or approval step. See raw lines 23–56.
- Selecting the company account gives access to **all** the merchant accounts; choosing a merchant account limits the selected account scope. Adyen advises selecting only roles the partner needs. Successful addition sends confirmation to merchant admins and an invitation to the partner. See raw lines 39–56.
- To change roles or account access afterward, the acting user needs **Merchant admin** or **Merchant user management**, and may assign only roles or accounts that their own user already has. Revocation can be temporary: the guide says previously enabled roles can be restored. See raw lines 58–83.
- This page does not specify Partner Portal account onboarding, SSO/MFA setup, merchant payment permissions beyond granted user roles, or a completed change in any real account.

## Detail locators

- **Partner purpose, merchant-account scope and roles:** raw lines 15–21.
- **Add prerequisites, Portal email match, company-wide scope, role selection and confirmation:** raw lines 23–56.
- **Later role/account changes and grant ceiling:** raw lines 58–72.
- **Revocation and possible restoration:** raw lines 74–83.

## Related

- [[adyen]]
- [[adyen-customer-area-iam]]
- [[source-adyen-docs-account-users]] — general Customer Area user management and grant ceilings

## Raw Sources

- [[raw/adyen/docs/account/users/partner-users/2026-09-15|Adyen partner users — collected 2026-09-15]]
