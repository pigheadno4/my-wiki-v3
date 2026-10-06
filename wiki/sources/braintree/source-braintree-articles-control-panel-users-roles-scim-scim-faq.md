---
title: "Braintree SCIM FAQ"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/users-roles/scim/scim-faq"
raw_files:
  - "braintree/articles/control-panel/users-roles/scim/scim-faq-2026-09-16.md"
tags: [braintree, scim, sso, identity-management, idp, control-panel, users, roles]
---

## Overview

This Braintree FAQ describes merchant administration of SSO users and group-backed access through SCIM, including the division of responsibility between an identity provider (IdP) and the Braintree Control Panel. It is an operational FAQ for the collected page snapshot, not the onboarding procedure, a complete SCIM specification, proof of current merchant eligibility, or confirmation that a particular synchronization or lifecycle operation completed.

## Key takeaways

- After SCIM is enabled for a merchant, the page makes the IdP the change surface for SCIM-managed SSO users: Braintree and merchant admins cannot create or edit SSO users or convert non-SSO users to SSO in the Control Panel. Non-SSO users remain managed only in the Control Panel, and only SSO users can be SCIM users.
- The page maps SCIM groups to membership in Braintree roles, merchant accounts, grant-all-merchant-accounts access and API-access groups. IdPs may manage membership, but they may not edit, add or remove the Braintree application groups themselves; changes to the underlying roles and merchant accounts remain Control Panel operations. A SCIM group's display name is separate from its associated role or merchant-account name, so renaming one does not rename the other, and admin-role names cannot be changed.
- Lifecycle behavior is provider- and action-specific. The page says Braintree matches SSO/SAML identities by email, so an Okta email or username change creates a user under the new email and suspends the old Braintree user rather than editing it. It also says removing an Okta user from the Braintree application suspends the user, while Okta does not send the delete call needed for permanent Braintree deletion.
- The page contains a material offboarding tension: its main flow calls SCIM onboarding a one-way street, while the FAQ says Braintree can roll a merchant off. The FAQ warns that changes made independently while SCIM is disabled can make later re-enablement and re-synchronization difficult, especially at high user/group volume. Treat roll-off and re-enablement as Braintree-assisted exception handling, not a documented self-service or lossless reversal.
- Group assignment can change privileges immediately. Linking an empty Okta push group to an imported app group removes every member from the associated Braintree role, including Account Admin in the example. The page separately requires an Okta group distinct from application assignment for Push Groups and warns that the wrong assignment flow can lock users out or grant excessive privileges.

## Detail locators

- SCIM definition, merchant/IdP purpose and bulk provisioning scope: `## What is SCIM?` and `## Why SCIM?`, lines 27-34.
- Token handoff, IdP-to-Braintree synchronization and SSO versus non-SSO administration boundaries: `## How does SCIM work?`, lines 37-39.
- Roll-off/re-enablement tension and disabled Control Panel actions for SSO users: `## Troubleshooting and FAQs`, lines 47-58.
- Pending-user import, Push Groups recovery, empty-group destructive effect and missing-member error: lines 60-83.
- Login checks, required role assignment and SSO metadata/username-format diagnostics: lines 86-107.
- Okta OIN cutover, email identity matching and separate SCIM-group versus role/account naming: lines 116-133.
- Okta suspension-versus-deletion behavior, group-structure permissions and Push Groups assignment warning: lines 136-150.
- Entra naming, multi-merchant Okta name collisions and Entra Entity ID diagnostics: lines 152-170.

## Related

- [[braintree]]
- [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/control-panel/users-roles/scim/scim-faq-2026-09-16|Braintree SCIM FAQ (collected 2026-09-16)]]
