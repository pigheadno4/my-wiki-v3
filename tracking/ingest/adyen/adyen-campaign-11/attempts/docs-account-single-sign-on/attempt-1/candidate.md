---
title: "Adyen Customer Area Single Sign-On Overview"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/single-sign-on"
raw_files:
  - "adyen/docs/account/single-sign-on/2026-09-15.md"
tags: [adyen, customer-area, sso, saml, identity-access]
---

## Overview

This [[adyen]] account overview introduces single sign-on (SSO) for **Customer Area users**. It says the Customer Area supports SAML 2.0 SSO and routes readers to separate setup, existing-user migration, and login guides. Use [[adyen-customer-area-iam]] for the provider user-access concept; web service API credentials are a separate subject.

## Key takeaways

- The overview describes SSO as using one set of credentials across connected services, including the Adyen Customer Area. It names Okta, Azure and Microsoft AD FS as examples of SAML 2.0 solutions; the examples do not prove a particular identity provider is configured for a merchant.
- Its high-level flow says users sign in at their identity provider, which authenticates them and grants access to connected services. The page gives this conceptual handoff, not SAML assertions, roles, session lifetime, account entitlements, or a tested login outcome.
- The listed capabilities are SSO authentication, creating SSO users, migrating existing users, and exchanging service-provider information using a metadata URL. Setup and migration are separate routes; this overview does not itself specify company-account prerequisites, administrator roles, user eligibility or test-versus-live steps. Follow their dedicated guides before taking action.
- The page cites controlled Customer Area access and a single credential set as benefits, including an employee-departure example. The example is a proposed benefit, not evidence of actual deprovisioning, an enabled SSO policy, effective MFA, or current access for a specific user.
- This 2026-09-15 snapshot is a documentation overview. It does not establish that any merchant has configured SSO, migrated users, verified an IdP, or changed Customer Area account access.

## Detail locators

- Customer Area purpose, credential reuse and SAML 2.0 support/examples: raw lines 15–21.
- Stated benefits and supported SSO/user/metadata routes: raw lines 23–33.
- Conceptual identity-provider authentication flow: `## How it works`, raw lines 35–39.
- Links to setup, migration and login guides: `## Next steps`, raw lines 41–50.

## Related

- [[adyen]] — provider context.
- [[adyen-customer-area-iam]] — Customer Area user identity and access route.
- [[source-adyen-docs-account-single-sign-on-set-up-sso]] — company-account setup, IdP metadata, administrator and test/live details.
- [[source-adyen-docs-account-single-sign-on-migrate-users-to-sso]] — optional existing-user migration and its access conditions.
- [[adyen-api-access]] — separate web service API credentials and permissions.

## Related raw API references

- [[raw/adyen/docs/account/single-sign-on/log-in-with-sso/2026-09-15|Customer Area SSO login guide]] — linked navigation only; not read for this entry.

## Raw Sources

- [[raw/adyen/docs/account/single-sign-on/2026-09-15|Adyen Customer Area SSO overview — collected 2026-09-15]]
