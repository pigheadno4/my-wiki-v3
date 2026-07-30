---
title: "Metronome Role-Based Access Control (RBAC)"
type: source
date_ingested: 2026-07-30
canonical_url: "https://docs.metronome.com/guides/platform-configuration/role-based-access-rbac"
original_format: webpage
raw_files:
  - "metronome/guides/platform-configuration/role-based-access-rbac-2026-07-13.md"
tags: [metronome, rbac, access-control, sso, api-tokens, platform-configuration]
---

## Overview

This Metronome guide documents the platform's role-based access control (RBAC) policy, its three built-in roles, SSO/identity-provider setup, and assigning an RBAC role to a newly created API token. It is a configuration guide, not a complete role-permission matrix, SSO protocol reference, or token-management API specification.

## Key takeaways

- Metronome says RBAC policies control what users can see and change, and are intended to reduce security-vulnerability scope and human error.
- The built-in roles are Administrator (full CRUD), Writer (CRUD except API-key creation and administrative settings), and Reader (view-only).
- RBAC policies are defined by the customer's identity provider and require SSO; without SSO, every user with Metronome access has full permissions.
- The identity-provider claim can have any name (with `role` recommended) and uses `admin`, `writer`, `reader`, or a custom-role value agreed with Metronome; an unspecified user role is denied access by default.
- A newly created API token can be assigned an Administrator, Writer, or Reader role in the UI; that role scopes the token's access and cannot be changed after creation.

## Built-in roles and identity-provider policy

Administrator has full create, read, update, and delete access to all Metronome components. Writer has CRUD access except for creating API keys and changing administrative settings such as data-export setup. Reader can view every component but cannot create, update, or delete anything. The guide also says custom roles are supported, but directs users to work with a Metronome representative to create them.

RBAC is configured through the identity provider after SSO is set up. The provider supplies a claim name and role values, and the customer tells Metronome which role should apply when a role is absent. The stated default is denial of access for users without a specified role. The guide does not define the claim's assertion format, how claims are refreshed, how a custom role's permissions are designed, or whether changes to an identity-provider role take effect for an existing session.

## API-token role assignment

When creating an API token in **Connections > API tokens & webhooks**, a user can directly select one of the three built-in RBAC roles. The token inherits the selected role's permissions, and the guide says the role cannot be changed once the token has been created. A custom role must first be created through a Metronome representative before it can be assigned to a token.

> [!info] Documentation boundary
> This guide does not state the permissions for a custom role, token expiry or rotation behavior, an API for token-role management, or whether a token follows later changes to its assigned role. It also does not reconcile direct role selection at token creation with the API-authentication guide's separate statement that tokens inherit the creating user's permissions by default.

## Related

- Company: [[metronome]]
- Concept: [[metronome-security-principles]]
- Related source: [[source-metronome-api-reference-authentication]]

## Raw Sources

- [[raw/metronome/guides/platform-configuration/role-based-access-rbac-2026-07-13]] — verbatim Metronome RBAC guide
