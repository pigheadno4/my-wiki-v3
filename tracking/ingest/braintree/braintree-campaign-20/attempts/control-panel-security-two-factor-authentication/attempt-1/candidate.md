---
title: "Braintree Control Panel Two-Factor Authentication"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/risk-and-security/control-panel-security/two-factor-authentication"
raw_files:
  - "braintree/articles/risk-and-security/control-panel-security/two-factor-authentication-2026-09-16.md"
tags: [braintree, control-panel, two-factor-authentication, account-security, webauthn]
---

## Overview

This collected Braintree article documents two-factor authentication for user access to the Braintree Control Panel. It covers the page's stated access requirement, available second-factor routes, sign-in fallback order, administrator-assisted lockout recovery and user-initiated reset boundary.

## Key takeaways

- The page says that, starting in September 2023, every Braintree user must enable 2FA to access the Control Panel. An enabled user signs in with a normal password and a separate code received from an authenticator application or by SMS.
- After 2FA is enabled, a user can register a WebAuthn U2F-compatible hardware security key. At sign-in, the page orders available factors as a registered hardware key, a registered authenticator app and then SMS; it also documents fallback from an unavailable preferred method and routes a user with no working option to an Account Admin or, when that is unavailable, Braintree support.
- For a locked-out user or one without access to their mobile device, the page assigns temporary 2FA disablement to the Braintree Account Admin and says the user will be prompted to set up 2FA at the next login. It separately says users cannot disable 2FA for themselves; their self-service reset is intended for changing a phone number or authenticator app, and an incomplete reset requires setup again.

## Evidence boundary

> [!warning] Collected Control Panel access evidence
> This page concerns authentication to the Braintree Control Panel, not payment authentication, transaction fraud screening or 3D Secure. The September 2023 statements are preserved as wording in the 2026-09-16 collected snapshot; immutable collection does not by itself prove current behavior, method availability or browser compatibility. Use the exact raw sections for procedural steps and compatibility lists.

## Detail locators

- Purpose, stated access requirement, password-plus-code flow and app/SMS choices: `# Two-Factor Authentication`, lines 14-18.
- Automatic setup assistant and manual enablement procedure: `## How to enable 2FA`, lines 21-37.
- Hardware-key registration and WebAuthn browser prerequisite: `## Setting up a Hardware Security Key`, lines 40-55.
- Sign-in factor order, method fallback and admin/support recovery route: `## Signing in with 2FA`, lines 60-77.
- Hardware-key management procedure: `## Managing a Web Authentication (WebAuthn) Security Key`, lines 82-91.
- Temporary administrator disablement and role boundary: `## How to Temporarily Disable 2FA for a user`, lines 94-113.
- Self-service reset purpose, procedure and incomplete-setup consequence: `## How to reset 2FA`, lines 116-131.
- TOTP application and hardware-key compatibility lists: `## Compatibility`, lines 134-165.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- Related account-administration source: [[source-braintree-control-panel-users-roles-managing-users-roles]]
- Separate PayPal-credential login source: [[source-braintree-control-panel-users-roles-log-in-with-paypal]]

## Raw Sources

- [[raw/braintree/articles/risk-and-security/control-panel-security/two-factor-authentication-2026-09-16|Braintree Control Panel Two-Factor Authentication]] - complete collected article covering Control Panel 2FA access, setup, factors, fallback, recovery, reset and compatibility
