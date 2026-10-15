---
title: "Adyen Docs: Set up Customer Area single sign-on"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/single-sign-on/set-up-sso"
raw_files:
  - "adyen/docs/account/single-sign-on/set-up-sso/2026-09-15.md"
tags: [adyen, customer-area, iam, sso, saml, user-management]
---

## Overview

This Adyen guide describes configuring **SAML 2.0 single sign-on** for Customer Area users with an identity provider (IdP). It covers company-account prerequisites, exchanging service-provider and IdP metadata, testing before live setup, and creating SSO users. The documented settings and example API request do not show that any merchant has enabled SSO or that a user can successfully sign in.

## Key takeaways

- SSO setup requires a SAML 2.0 IdP and a **Customer Area company account**; the guide says SSO cannot be set up with a merchant account. The configuring user needs **Merchant admin** or **Merchant user management**, and an organization-authorized person must accept the SSO legal notice. Adyen recommends retaining at least one admin who does not use SSO for troubleshooting.
- Start in the **test Customer Area**, then repeat the process in **live**. Copy Adyen's service-provider SSO/AssertionConsumerService URL into the IdP, enable SAML2 request and response signing, use an email address for `SubjectNameID`, and obtain the IdP metadata URL. Azure additionally requires the response-and-assertion signing option. The Customer Area fetches the IdP configuration for review before saving it.
- The guide specifies Google IdP metadata hosting: its metadata file must be permanently publicly accessible and unencrypted. See the raw IdP field table and Google branch for provider-specific names and the Sign-on URL instruction. A metadata URL is configuration input, not proof of a working federation.
- Saving the SSO configuration permits testing but does **not** automatically enable SSO for existing users. Create new SSO users or migrate existing users separately. A new user must already have an IdP account; Customer Area creation selects SSO as the login method, a unique email username, account access, and roles. The creator can assign only roles they already hold.
- New users can instead be created through a Management API request: the guide distinguishes company-level `POST /companies/{companyId}/users` from merchant-access `POST /merchants/{merchantId}/users`. Merchant-account access for a user is distinct from the company-account prerequisite for setting up SSO. Its sample targets the **test** Management API, uses an API key, and says HTTP 200 means user creation; a verification email follows. That response is not proof of email verification, correct permissions, or successful SSO login.

## Detail locators

- Raw lines 15–34: SAML 2.0 scope, company-account and role/legal prerequisites, and non-SSO admin recommendation.
- Raw lines 36–47: IdP field-name table and metadata hosting statement.
- Raw lines 49–69: test-then-live order, service-provider URL, SAML signing, email NameID, Azure and Google qualifications, IdP metadata URL.
- Raw lines 71–92: Customer Area metadata fetch/save, testing, existing-user migration requirement, and metadata URL change steps.
- Raw lines 94–132: IdP-account prerequisite and Customer Area SSO-user creation, including scoped account access and role assignment.
- Raw lines 134–179: company-versus-merchant Management API user-creation routes, request fields, test example, HTTP response and verification email.

## Related

- [[adyen]]
- [[adyen-customer-area-iam]]
- [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/docs/account/single-sign-on/set-up-sso/2026-09-15|Adyen Customer Area SSO setup guide snapshot (2026-09-15)]]
