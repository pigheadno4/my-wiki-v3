---
title: "Braintree Control Panel Role Permissions"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/users-roles/role-permissions"
raw_files:
  - "braintree/articles/control-panel/users-roles/role-permissions-2026-09-16.md"
tags: [braintree, control-panel, roles, permissions, access-control, oauth]
---

## Overview

This collected Braintree reference defines the **Rights Granted** that can be assigned to Control Panel roles. It organizes permissions by category and maps them to action scopes across transaction and customer operations, reporting and security, fraud and recurring billing, user administration, account surfaces, specialized APIs, read-only access and search.

## Key takeaways

- A role can receive every right in one category or selected rights across several categories. Assigning the **Manage Roles** or **Manage Users** permissions is itself restricted to the **Account Admin** role.
- The table distinguishes operational actions from visibility and download rights. Its scopes include transaction creation, refund, settlement, escrow and void actions; Vault customer and payment-method management; reports and dashboard access; processing and IP-restriction settings; fraud-tool actions; user/role administration; recurring-billing management and viewing; dispute, webhook, statement, merchant-account and business-document actions; and separate read-only and search access. Use the table locators below for the exact permission-to-action mapping rather than treating these categories as interchangeable.
- Several rights have narrower prerequisites or effects. Creating, running and downloading reports does not grant statement access; production merchant-account management is described for Braintree Marketplace accounts, whereas sandbox users can create test merchant accounts.
- **Forward Payment Methods with the Forward API** is available to all sandbox merchants and approved production merchants, and the page explicitly says it is not included in the Account Admin role. The separately collected managing-users reference calls Account Admin the maximum-permission role, so these statements should be treated as a documented scope tension rather than evidence that Account Admin automatically contains every permission.
- OAuth-application permissions are limited to merchants participating in the Braintree Auth and OAuth betas. The **Manage Connected OAuth Applications** permission can authorize or deauthorize connections and can consent to requested scopes even when those scopes correspond to rights the user does not have.

## Detail locators

- Role-permission identity, category assignment behavior and the Account Admin gate for assigning Manage Roles or Manage Users: `# Role Permissions`, lines 16-22.
- Transaction actions: `## Rights Granted`, lines 29-36.
- Customer Management, Reporting, Processing and Security Options: `## Rights Granted`, lines 37-42.
- Fraud Tools, Fraud Protection Advanced Dashboard, User Management, Recurring Billing and Dispute Management: `## Rights Granted`, lines 43-60.
- Webhooks, account agreements, statements, merchant accounts, business documents, Forward API and OAuth categories: `## Rights Granted`, lines 61-69.
- Read-Only Access and Search categories: `## Rights Granted`, lines 70-79.

## Evidence boundary

> [!warning] Permission and snapshot scope
> This is a collected Control Panel role-permission reference, not a general API authorization contract. Some rows explicitly permit API actions, but that does not establish that every Control Panel permission governs every API operation. Except where a row names sandbox, production, Marketplace, approval or beta eligibility, the page does not state environment or merchant eligibility. Treat the 2026-09-16 raw as collected evidence rather than proof of current behavior.

> [!warning] Account Admin scope tension
> This page says the Forward API permission is not included in Account Admin, while [[source-braintree-control-panel-users-roles-managing-users-roles]] describes Account Admin as having the maximum permissions possible. Preserve both statements and verify the intended role setup rather than assuming one silently overrides the other.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Related source: [[source-braintree-control-panel-users-roles-managing-users-roles]]

## Raw Sources

- [[raw/braintree/articles/control-panel/users-roles/role-permissions-2026-09-16|Braintree Control Panel Role Permissions]] - complete collected permission-category and action-scope reference
