---
title: "Braintree Single Sign-On (SSO) Onboarding Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/single-sign-on-sso"
raw_files:
  - "braintree/articles/guides/single-sign-on-sso-2026-09-16.md"
tags: [braintree, control-panel, sso, saml, identity-provider, user-access]
---

## Overview

This collected [[braintree]] guide describes SAML 2.0 single sign-on for access to the [[braintree-control-panel]]. Braintree is the service provider: the organization’s identity provider authenticates the user and returns a SAML assertion, while Braintree users remain created, edited, suspended, and otherwise managed in the Control Panel. The page covers SP-initiated and IdP-initiated login, merchant onboarding inputs, provider-side configuration examples, user creation and conversion, post-configuration testing, and provider or application migration.

## Key takeaways

- SP-initiated login uses separate Production and Sandbox Braintree SSO session URLs; IdP-initiated login begins from the organization’s IdP dashboard. The guide names Okta, OneLogin, and Microsoft Entra ID setup paths, but their UI steps are provider-specific examples rather than a universal IdP procedure.
- The setup exchange requires the merchant public ID, every permitted login email domain, the IdP’s SSO HTTP POST-binding URL, and an X.509 signing certificate. Braintree supplies the callback URL and may supply a distinct issuer/audience value. On the IdP side, the NameID format and value are the user’s email address.
- User identity is email-based: the IdP and Braintree email addresses must match exactly, and an address outside the configured email domains cannot log in. A new SSO user must exist in and be assigned to the IdP application and must also be created in the Braintree Control Panel.
- Suspending a user in the IdP denies Braintree access but does not suspend or delete the still-active Control Panel record. Converting an existing user to SSO removes username-and-password login on Braintree; the guide says to allow up to five minutes for cache invalidation before testing. A user enabled for SSO on multiple Braintree merchants is prompted to choose a merchant during Braintree-initiated login.
- The page requires MFA attribution for all SSO applications and routes the exact compliance procedure to a separate MFA guide. Its SAML configuration uses an X.509 certificate to validate responses.
- The guide does not name a Control Panel role or permission required to request onboarding, create an SSO user, convert a user, or migrate the IdP. It says merchant SSO configuration involves Braintree support or a CSM/TAM; submitting inputs or receiving a callback URL is not itself evidence that SSO has been enabled or that a login test succeeded.
- Convert every existing non-SSO user who should use SSO before SCIM onboarding: once a merchant is on SCIM, this guide says non-SSO users can no longer be converted to SSO. A missing **SSO Status** section may indicate incomplete SSO onboarding or a SCIM merchant.
- Provider or application migration requires coordination with Braintree support, assignment of users to the replacement application, and a test login after the configuration switch. The guide says the Braintree callback URL does not change during that migration.

> [!warning] Snapshot and outcome boundary
> This 2026-09-16 snapshot documents the guide’s onboarding and login model. It does not prove current product availability, a merchant’s SSO or SCIM eligibility, a user’s role or account assignment, support approval, completed configuration, successful authentication, or security compliance.

## Detail locators

- SSO/SAML roles and assertion flow: `## What is SSO? What is SAML? How does this all work?`, lines 20-46.
- Braintree user-management boundary, IdP authentication, suspension mismatch, and Production/Sandbox plus IdP-initiated entry points: `## What does SSO/SAML at Braintree look like?`, lines 53-74.
- Required merchant, domain, POST-binding and certificate inputs plus optional logout redirect: `## Required Setup Values`, lines 83-99.
- Audience, ACS/recipient and email NameID mapping: `## IdP-Side Configuration Details`, lines 102-112.
- Support handoff and Braintree callback response: `## Step-by-Step Setup (Any IdP)`, lines 115-135.
- Okta, OneLogin and Entra configuration examples, environment endpoints and MFA route: `### Okta`, lines 142-221; `### OneLogin`, lines 228-285; `### Microsoft Entra ID (Azure AD)`, lines 292-355.
- Post-configuration tests and pre-SCIM conversion order: `## Post-Configuration Steps`, lines 370-383.
- Exact email identity, two-sided user creation, assignment and cache wait: `## How to Create a new SSO Enabled User`, lines 390-450.
- Existing-user conversion, SSO-status availability, password-login consequence, multi-merchant selection and the documented 403 workaround: `## How to Convert an Existing Non-SSO User to SSO`, lines 455-477.
- Coordinated IdP/application migration and stable callback URL: `## How to Perform an SSO Provider or Application Migration`, lines 480-496.

## Related

- [[braintree-control-panel]] - main Control Panel administration route.
- [[source-braintree-control-panel-users-roles-managing-users-roles]] - separate general user and role management source.
- [[source-braintree-articles-control-panel-users-roles-scim-scim-faq]] - separate SCIM qualification and behavior route linked by this guide.
- [[source-braintree-articles-control-panel-users-roles-scim-scim-integration]] - separate SCIM onboarding route linked by this guide.

## Raw Sources

- [[raw/braintree/articles/guides/single-sign-on-sso-2026-09-16|Braintree Single Sign-On (SSO) Onboarding Guide]]
