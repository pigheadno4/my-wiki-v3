---
title: "Adyen Customer Area Multifactor Authentication"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/multifactor-authentication"
raw_files:
  - "adyen/docs/account/multifactor-authentication/2026-09-15.md"
tags: [adyen, customer-area, mfa, authentication, user-security]
---

## Overview

This [[adyen]] account guide describes **Customer Area user** multifactor authentication (MFA): an authenticator-app or live-only SMS verification method, device registration and removal, and the limited device-management action available to a Merchant admin. It states that Customer Area users must set up MFA **or** SSO. This is a user-login route under [[adyen-customer-area-iam]], separate from web service API credential authentication and payment authorization.

## Key takeaways

- The page says all Customer Area users must set up MFA **or single sign-on**. It describes MFA as an extra verification form at login, not a requirement to use both MFA and SSO. Its statement is a documented login rule, not evidence of the authentication state or enforcement outcome for a particular user.
- Each user can register **two devices**, with **one authentication method per device**. The methods described are time-based one-time passwords from an authenticator app and SMS-delivered one-time passwords. SMS is available only in the **live** environment; a verification-capable mobile device is required. Do not infer SMS availability in test from links to the test Customer Area within this page.
- The authenticator-app setup shown for first login registers a named device using a scanned QR code or manual key, a six-digit code, and **Add**. After registration, that app's code is required at each Customer Area login. The SMS setup is a separate Profile route: add authentication, switch to SMS, enter a phone number and received six-digit code, then add the method; the SMS code is required at later logins. These steps do not prove that either method was registered for a real account.
- A user can remove an existing authentication method from their own Profile. For a new device, the guide says to remove the registered device and add an authenticator-app method; the next login requires registering the new device. It gives no complete lost-device or locked-out-user recovery procedure. Do not treat deletion as assurance that a user without current Customer Area access can recover unaided.
- A **Merchant admin** can view user details and remove registered devices for users in the organization. The page describes device removal, not the admin adding a factor for another user, disabling all MFA, bypassing verification, changing SSO policy, or gaining access to that user's account.
- This page was collected 2026-09-15 and carries 2024-01-12 last-modified metadata. It does not establish a specific merchant's MFA/SSO configuration, user access state, current policy enforcement, or successful login.

## Detail locators

- Customer Area MFA-or-SSO statement, verification purpose, device count, admin scope and method choices: raw lines 15–31.
- Integration, live-only SMS and mobile-device requirements: `## Requirements`, raw lines 33–41.
- First-login authenticator-app enrollment and later code prompt: raw lines 43–52.
- Live-only SMS enrollment and later code prompt: raw lines 54–68.
- Own-profile authentication-method deletion: raw lines 70–77.
- New-device removal, own-versus-other-user detail route and next-login registration: raw lines 79–89.

## Related

- [[adyen]] — provider context.
- [[adyen-customer-area-iam]] — Customer Area user identity and access route.
- [[source-adyen-docs-account-single-sign-on-set-up-sso]] — alternate SSO setup route.
- [[source-adyen-docs-account-users]] — separate user-management roles and permissions.
- [[adyen-api-access]] — separate web service API credential route.

## Raw Sources

- [[raw/adyen/docs/account/multifactor-authentication/2026-09-15|Adyen Customer Area MFA guide — collected 2026-09-15]]
