# Customer Area SSO overview retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** What does Adyen's single sign-on overview establish for the Customer Area, and does it prove a company's SSO is enabled?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-account-single-sign-on.md` → pinned raw `raw/adyen/docs/account/single-sign-on/2026-09-15.md`, lines 15–37. The overview introduces Customer Area SSO using SAML 2.0, gives IdP examples, and says users sign in through the IdP for connected services. Its employee-departure access-removal sentence (line 25) is a benefit example, not account-specific deprovisioning proof. It does not prove any merchant has set up SSO, migrated users, configured roles, tested a live login or changed an account. It is about Customer Area users rather than web service API keys.

## Q2 — Central routes and prerequisites owned elsewhere

**Query:** Which SSO capabilities and follow-up guides does the overview list, and where should company scope, roles and test/live setup be checked?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-account-single-sign-on.md` → raw lines 28–33 for SSO authentication, SSO-user creation, existing-user migration and service-provider metadata exchange; lines 41–50 for setup, migration and login links. This overview gives navigation and a conceptual IdP flow (lines 35–37). The already retained `source-adyen-docs-account-single-sign-on-set-up-sso` owns company-account prerequisites, SAML/IdP configuration, administrator roles and test-then-live setup. `source-adyen-docs-account-single-sign-on-migrate-users-to-sso` owns existing-user migration conditions and separate test/live migration. The raw login guide link is navigation until independently read. Do not turn this overview's links into proof of user eligibility, configured SSO or successful authentication.
