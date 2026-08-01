---
title: "Metronome Single Sign-On (SSO)"
type: source
date_ingested: 2026-08-01
canonical_url: "https://docs.metronome.com/guides/platform-configuration/single-sign-on-sso"
original_format: webpage
raw_files:
  - "metronome/guides/platform-configuration/single-sign-on-sso-2026-07-13.md"
tags: [metronome, sso, saml, identity-provider, user-provisioning, access-control, platform-configuration]
---

## Overview

This Metronome guide describes SAML 2.0 single sign-on for team-member access, covering supported initiation paths, identity-provider-controlled login access, retained user metadata, setup handoff, attribute mapping, and password-login cutover. It is a platform-login guide, not a complete SAML profile, user-lifecycle specification, RBAC policy, or API-authentication reference.

## Key takeaways

- SSO lets team members use an organization's existing sign-in process instead of creating another Metronome username and password.
- Metronome supports SAML 2.0 with both service-provider-initiated and identity-provider-initiated authentication.
- Metronome says its SSO handles user provisioning between the identity provider and the Metronome instance, but this page does not define the provisioning lifecycle or protocol.
- The identity provider controls login eligibility. Removing a user's Metronome access on the customer side prevents that user from logging in, while Team Settings continues to show metadata for all users, including the role recorded at each user's last login.
- Setup exchanges Metronome service-provider values for an identity-provider URL and X509 signing certificate, maps name and email claims, and ends with joint verification. After the account switches to SSO, existing username-and-password logins stop working.

## SSO and user-management boundary

Metronome frames SSO as federated team-member login through an organization's existing identity system. It lists ADFS, Azure, Google, Okta, OneLogin, Ping Identity, and SecureAuth as supported examples and documents both directions of SAML 2.0 initiation. The page also says Metronome handles user provisioning, but it does not specify just-in-time account creation, SCIM, profile synchronization, reactivation, or deletion behavior.

Identity-provider configuration controls whether a user can log in. Removing Metronome access on the customer side prevents subsequent login, while Metronome retains user metadata on Team Settings, including the role each user had at the last login. This establishes a future-login and metadata-retention boundary; it does not establish deletion of the Metronome user record or termination of an already active session.

## Setup and cutover

A Metronome representative supplies the Assertion Consumer Service URL, Metronome Entity ID, and logo. The customer uses the setup values to generate an Identity Provider URL and X509 signing certificate, then provides both to Metronome so it can create the connection. The customer also provides equivalent claim attribute names for `name` or `firstName lastName`, and for `email`.

After Metronome and the customer complete final tests, the account is switched to SSO and its existing username-and-password logins cease to work. The page does not document SAML bindings, assertion-signing or encryption requirements, certificate expiry or rotation, metadata exchange, multi-IdP support, MFA policy, single logout, session lifetime, active-session revocation, fallback login, or recovery from IdP unavailability. It also does not define the separate RBAC role claim or API bearer-token authentication behavior.

## Related

- Company: [[metronome]]
- Concept: [[metronome-security-principles]]
- Related sources: [[source-metronome-guides-platform-configuration-role-based-access-rbac]], [[source-metronome-guides-platform-configuration-security-principles]], [[source-metronome-api-reference-authentication]]

## Raw Sources

- [[raw/metronome/guides/platform-configuration/single-sign-on-sso-2026-07-13|2026-07-13 snapshot - SAML SSO setup, access removal, and password-login cutover]]
