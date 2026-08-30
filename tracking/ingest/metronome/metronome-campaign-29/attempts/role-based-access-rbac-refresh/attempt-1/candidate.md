---
title: "Metronome Role-Based Access Control (RBAC)"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/guides/platform-configuration/role-based-access-rbac"
original_format: webpage
raw_files:
  - "metronome/guides/platform-configuration/role-based-access-rbac-2026-08-28.md"
  - "metronome/guides/platform-configuration/role-based-access-rbac-2026-07-13.md"
tags: [metronome, rbac, access-control, sso, identity-provider, api-tokens]
---

## Overview

This guide defines how Metronome RBAC limits what users and API tokens can see or change. It documents three built-in roles, custom-role availability, identity-provider claim mapping through SSO, and immutable role assignment when an API token is created; it is not a complete permission matrix or propagation specification.

## Query-critical facts

- Metronome presents RBAC as control over the data a user can access and the actions a user can take, intended to reduce security-vulnerability scope and human error.
- The three out-of-the-box display roles are **Administrator**, **Writer**, and **Reader**. Administrator has full CRUD access to all Metronome components; Writer has CRUD access except API-key creation and administrative settings such as data-export setup; Reader can view all components but cannot create, update, or delete.
- Metronome also supports custom roles whose permissions can be tailored. The guide routes custom-role creation for API-token assignment through the support portal but does not define the available permission units or design process.
- User RBAC requires SSO and is defined through the customer's identity provider. The claim name is customer-chosen (`role` is recommended), while documented claim values are `admin`, `writer`, `reader`, or a custom value created with the Metronome team; these lowercase claim values are distinct from the built-in display-role names.
- The customer submits the claim name and any desired missing-role default through the support portal. By default, a user without a specified role is denied access; if SSO is not configured, all users who have Metronome access receive full permissions.
- At API-token creation, the current UI route is **Developer > API tokens**. The creator can select Administrator, Writer, or Reader; the token inherits that role's permissions, and the assigned role cannot be changed after creation. A custom role must be created through the support portal first.

## Material boundaries and authority conflicts

The guide does not provide a field- or endpoint-level permission matrix, custom-role permission catalog, authorization-error behavior, claim assertion format, claim-refresh cadence, session-revocation behavior, or timing and propagation guarantees for identity-provider role changes, missing-role default changes, or custom-role permission changes. Its statements about full component access and CRUD scope should therefore not be expanded into undocumented enforcement mechanics.

> [!warning] Authorization-model conflict
> The API-authentication source says tokens inherit the creating user's permissions by default and can be restricted by access level, environment, or endpoint through the support portal. This RBAC guide separately says a selected role is assigned at token creation and cannot later be changed. The sources do not define precedence, whether explicit selection overrides default inheritance, or whether support-mediated scope changes affect an assigned role; preserve both as source-scoped statements.

The refreshed guide moves token creation from the prior snapshot's **Connections > API tokens & webhooks** route to **Developer > API tokens**, and replaces representative-mediated setup language with support-portal routes. These are documentation changes, not evidence of when the product UI or operational process changed.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| RBAC purpose and customization | Data and action scope, stated security and human-error purpose, custom-role support, and expert-contact control |
| Built-in roles | Intended human actors and exact Administrator, Writer, and Reader CRUD or view boundaries |
| SSO and identity-provider setup | SSO prerequisite, customer-chosen claim name, lowercase claim values, support-portal handoff, configurable missing-role default, default denial, and no-SSO full-access boundary |
| API-token assignment | Refreshed **Developer > API tokens** steps, selectable built-in roles, inherited permissions, immutable assignment, and support-mediated custom-role creation |

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-security-principles]]
- Related sources: [[source-metronome-guides-platform-configuration-single-sign-on-sso]], [[source-metronome-api-reference-authentication]]

## Raw Sources

- [[raw/metronome/guides/platform-configuration/role-based-access-rbac-2026-08-28|2026-08-28 snapshot - current built-in roles, SSO claim setup, support-portal routing, and Developer token-role assignment]]
- [[raw/metronome/guides/platform-configuration/role-based-access-rbac-2026-07-13|2026-07-13 snapshot - prior immutable RBAC guide and earlier UI and representative routes]]
