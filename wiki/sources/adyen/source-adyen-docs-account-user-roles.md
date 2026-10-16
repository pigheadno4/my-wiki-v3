---
title: "Adyen Customer Area User Roles"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/user-roles"
raw_files:
  - "adyen/docs/account/user-roles/2026-09-15.md"
tags: [adyen, customer-area, user-roles, access-control, permissions]
---

## Overview

This Adyen page catalogs **Customer Area user roles** and the actions they permit across account, developer, finance, POS, platform, risk and transaction functions. It was captured 2026-09-15 with page metadata last modified 2024-12-09. It is a role reference, not evidence of a specific user's current assignments, account scope, or approval of a requested action.

> [!warning] Contradiction
> The separately reviewed Donation campaigns guide includes **Merchant financial** among its report roles, then says those roles give no access to other payment information. This role catalog instead grants Merchant financial broader payment-analytics, payout and financial-report access. Do not treat Merchant financial as donation-only; the two snapshot statements conflict. Verify the actual role grants and account scope before assigning access. [[source-adyen-docs-reporting-donation-campaigns]]

## Key takeaways

- A user can have multiple Customer Area roles, assigned individually or through **role groups**. The initial admin user has common roles including **Merchant admin** and can create other users. **Merchant user management** can create/edit users and grant only roles and account access that the managing user already has. Role assignment, account access and actual action outcome remain distinct.
- Customer Area user roles are not API-credential roles. The **Manage API credentials** user role permits management of credentials, including generating an API key; the resulting API credential has its own permissions and account scope. **Manage test cards** permits viewing, creating and deleting test cards; **Merchant technical integrator** covers webhooks and API URLs. Use the separate API-credential source for request authentication and credential-level access.
- Some catalog entries have additional access or paired-role conditions: **Manage Merchant Account Groups role** requires company-account access; examples in POS and Platforms require **View Payments** or **Balance platform base role**. **Merchant standard role** is enabled by default and controls Customer Area login; disabling it prevents login. Check the specific role's row before granting or assuming access.
- The catalog distinguishes viewing from changing sensitive data and money movement. **Merchant View PII** exposes sensitive shopper data and the page warns unmasked PII can affect PCI DSS compliance level. **View key payments data** excludes shopper/risk/technical detail, while **View Payments** includes them. Finance, payout, refund, capture and other transaction powers are separate named roles; a login role alone does not imply them.
- Entries such as **Change payment methods**, **Merchant additional merchant accounts**, **Merchant access manage** and **Manage account holder capabilities** sometimes grant the ability to **request** access, a method, account or capability. A request role does not itself establish that Adyen or another administrator approved the request or enabled the resource. This page does not provide a universal restricted-role approval workflow.

## Detail locators

- Opening paragraphs and `## Manage user roles` — user roles, individual versus role-group assignment, initial admin and category index.
- `## Account` / `## Developer` — account-group/company-access condition, user-management grant boundary, API-credential/test-card/webhook role distinctions.
- `## General` — Merchant admin, PII and PCI warning, report roles and Customer Area login role.
- `## In-person payments (POS)`, `## Platforms`, `## Transactions` — examples of paired-role prerequisites, account-holder and money-movement powers, plus view-only versus action roles.
- `## Partners` and specific request-role rows — requests for access or resources rather than proof of approval.

## Related

- Company: [[adyen]]
- Separate API credential access route: [[adyen-api-access]]
- API credential role reference: [[source-adyen-docs-development-resources-api-credentials-roles]]

## Raw Sources

- [[raw/adyen/docs/account/user-roles/2026-09-15|2026-09-15 Adyen Customer Area user-role catalog]]
