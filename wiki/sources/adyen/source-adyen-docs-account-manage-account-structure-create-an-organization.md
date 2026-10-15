---
title: "Adyen Create an Organization"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/manage-account-structure/create-an-organization"
raw_files:
  - "adyen/docs/account/manage-account-structure/create-an-organization/2026-09-15.md"
tags: [adyen, account-structure, organization, company-accounts, customer-area, sso]
---

## Overview

This Adyen Customer Area guide describes an **organization** as a grouping of legally related **company accounts** that lets authorized users reach multiple company accounts through one login. The page was captured 2026-09-15 with 2024-09-16 last-modified metadata. An organization is an access and login layer above company accounts; this guide does not create or merge merchant accounts, change contracts, or define payment settlement or funds flow.

## Key takeaways

- The feature requires additional Adyen-side configuration through Support or an Adyen contact. Only legally related company accounts can be grouped, and **Merchant admin** is the stated role to manage organizations in Customer Area. Each company account is added individually through its **Settings > Account settings > Unified account login** flow; after accepting terms, the UI returns a message to confirm whether it was added. The page is a setup guide, not evidence that any account was added.
- One login can reach multiple company accounts in the organization, but **membership does not give a user access to every company account by default**. To add access where absent, the guide directs creation of a user for that company using email/password or SSO login. For companies already accessible, the user's roles remain distinct and unchanged **for each company account** after joining the organization.
- For a user with access to multiple company accounts in the organization, edits to email, first or last name, removal of an MFA device, and password reset are reflected under all those company accounts. Per-company role differences still remain; do not infer shared authorizations from shared identity.
- Organization SSO configuration follows the documented sequence: inherit from the first added company if it has SSO; otherwise inherit from a later added company with SSO; if none has SSO, wait until a member company configures it. Copying that configuration to a company account and migrating users to SSO are separate Customer Area actions, each with its own UI flow.
- Grouping does not, by itself, establish a new legal seller, merchant of record, contract holder, payout recipient, consolidated balance, or money flow. Those questions require separate account, contractual and payment evidence. The dated page does not prove current feature eligibility or completed organization setup.

## Detail locators

- Opening through `## Add a company account to an organization` — purpose, Support configuration, legal relationship, Merchant admin role and per-company addition.
- `## Copy SSO configuration from the organization` / `## Manage user migration to SSO` — SSO inheritance, copy and migration steps.
- `## Give a user access to a company account in an organization` — nonautomatic access, cross-company profile changes, email and SSO user-creation routes.
- `## User roles for each company account` — unchanged per-company role example.

## Related

- Company: [[adyen]]
- Account hierarchy: [[adyen-account-structure]]
- Customer Area roles: [[source-adyen-docs-account-user-roles]]

## Raw Sources

- [[raw/adyen/docs/account/manage-account-structure/create-an-organization/2026-09-15|2026-09-15 Adyen create-an-organization snapshot]]
