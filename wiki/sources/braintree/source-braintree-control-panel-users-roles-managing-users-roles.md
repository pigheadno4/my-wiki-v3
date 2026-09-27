---
title: "Braintree Control Panel Managing Users and Roles"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/users-roles/managing-users-roles"
raw_files:
  - "braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16.md"
  - "braintree/articles/control-panel/users-roles/log-in-with-paypal-2026-09-16.md"
tags: [braintree, control-panel, users, roles, access-control, account-security]
---

## Overview

This collected Braintree article documents Control Panel administration for users, roles and password resets. Roles grant or restrict access to gateway information and functions, while unique credentials let the merchant track which user interacted with certain transactions; the page also records account-activation, editing and security boundaries.

## Key takeaways

- The page says each person who needs Control Panel access must have a separate user and recommends enabling two-factor authentication for every user. It attributes the separate-user requirement to the PCI Security Standards Council.
- Each user must have at least one role. When several roles are assigned, the role with the greatest permissions prevails. Roles can be created or edited, but the maximum-permission **Account Admin** role cannot be edited or renamed.
- Creating a user includes specifying an email address, whether the user should have API access, a Control Panel role and accessible merchant accounts. Braintree then emails the user to complete account information and credentials; the Control Panel status changes from **Pending** to **Active** after the user logs in.
- Most user information and permissions can be changed after creation, but the username cannot. Changing the Name or Email fields requires continued access to the original email account for confirmation; otherwise the page instructs the administrator to create a new user.
- Anyone can initiate their own reset from the sign-in page, while resetting another user's password in the Control Panel requires the **Manage Users** role permission. The Control Panel requires a password reset after six failed login attempts, and a user with an associated phone number must also authenticate the reset with a texted code. If an unrequested password-reset email arrives, the page warns that it may be phishing and instructs the user to avoid the suspect email link and sign in directly to reset the password.

## Detail locators

- User/role purpose, support-information effect, separate-user requirement and 2FA recommendation: `# Managing Users and Roles`, lines 16-22.
- Role assignment, greatest-permission precedence, create/edit route and fixed Account Admin role: `## Creating and editing roles`, lines 27-41.
- New-user fields, merchant-account access, activation email and Pending-to-Active transition: `## Creating users`, lines 44-62.
- Editable user data, immutable username and original-email confirmation prerequisite: `## Editing users`, lines 65-82.
- Suspicious reset-email warning, failed-attempt threshold, self-service versus Manage Users reset routes and phone-code requirement: `## Password safety` and `### Resetting user passwords`, lines 87-125.
- Password composition and history rules: `### Password requirements`, lines 130-137.

## Evidence boundary

> [!warning] Control Panel administration scope
> This page documents Control Panel actions and does not establish an API user-management contract. It does not state whether a described action applies to Sandbox, Production or both, and its link to the full role-permission catalog is navigation only here. Treat the 2026-09-16 raw as collected evidence rather than proof of current behavior.

> [!warning] Contradiction: collected password minimums
> This article's general **Password requirements** section says new passwords must be at least **14 characters**, while [[source-braintree-control-panel-users-roles-log-in-with-paypal]] says the new Braintree password set when disabling Log In with PayPal must be at least **7 characters**. The statements occur in different flows, but neither collected page says the minimum is flow-specific or reconciles the difference. Treat the minimum as unresolved in these 2026-09-16 snapshots; do not infer one current Control Panel password rule without current verification.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/control-panel/users-roles/role-permissions-2026-09-16|Braintree Control Panel role permissions]] - unread navigation-only permission catalog; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree Control Panel Managing Users and Roles]] - complete collected article covering user and role administration, activation, editing and password-reset boundaries
- [[raw/braintree/articles/control-panel/users-roles/log-in-with-paypal-2026-09-16|Braintree Control Panel Log In with PayPal]] - complete cross-read supporting the collected 7-character minimum in the disablement flow
