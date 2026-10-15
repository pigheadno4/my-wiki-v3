---
title: "Adyen Customer Area SSO login and email verification"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/single-sign-on/log-in-with-sso"
raw_files:
  - "adyen/docs/account/single-sign-on/log-in-with-sso/2026-09-15.md"
tags: [adyen, customer-area, sso, identity-provider, user-access]
---

## Overview

This [[adyen]] account guide explains the user-facing email-verification and identity-provider (IdP) login path for Customer Area single sign-on. After an administrator adds a Customer Area user, that user verifies the email address, then enters it on the Customer Area login page or starts from the IdP. The guide names Okta, Azure and Microsoft AD FS as IdP examples. It is about an individual Customer Area user login, not an API credential, payment authorization, merchant-account hierarchy change, or proof that a particular user has access. See [[adyen-account-structure]] for broader account and user-access context.

## Key takeaways

- The administrator-added user receives an automated verification email. The user must complete the verification separately for **test** and **live** Customer Area. If the link expires, the page instructs the user to request a new one from the administrator; first and last name entry is optional after verification.
- After verification, the user enters the verified email as Username and selects Next. A user already signed in to the IdP is redirected to Customer Area; otherwise the user is sent to the IdP to sign in and then redirected back. The guide also permits starting from the IdP and choosing Adyen Customer Area.
- The page says that, from then on, the user must access Customer Area using SSO. It does not define a domain-verification or SSO migration procedure, IdP configuration, session expiry or refresh rules, account membership, or user-role permissions. Verification and the described redirects alone do not establish an actual successful session, live access, or a permission to operate on payments.

## Detail locators

- **Purpose, IdP role and examples:** raw lines 15–20, under `# Log in with single sign-on`.
- **Admin-added user, verification email, test/live separation and expired-link handling:** raw lines 22–33, under `## Verify your email address`.
- **Customer Area username/IdP redirect branch and SSO-only continuation:** raw lines 35–44.
- **Customer Area and IdP initiated entry routes:** raw lines 46–61, under `## Log in from Customer Area` and `## Log in from your identity provider`.

## Related

- [[adyen]]
- [[adyen-account-structure]]

## Raw Sources

- [[raw/adyen/docs/account/single-sign-on/log-in-with-sso/2026-09-15|Adyen Customer Area SSO login guide — collected 2026-09-15]]
