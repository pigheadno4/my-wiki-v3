# Adyen Customer Area SSO setup retrieval probes

## Q1 — Purpose, scope and inference boundary

**Query:** What does Adyen's Set up SSO guide configure, and does it prove an account's users can sign in through SSO?

**Expected route:** [[source-adyen-docs-account-single-sign-on-set-up-sso]] via [[adyen-customer-area-iam]].

**Answer boundary:** It is a SAML 2.0 Customer Area SSO setup guide for a company account and its IdP, captured 2026-09-15. It documents prerequisites, metadata exchange, test then live setup, and user creation or migration. A saved configuration, Management API example, or HTTP 200 user-creation response does not prove a live account was changed, a verification email was completed, permissions are correct, or SSO login works. Raw lines 15–34, 49–85, 134–179.

## Q2 — Configuration, permissions and recovery

**Query:** What are the company-account, IdP, signing, user-permission and recovery conditions for Customer Area SSO?

**Expected route:** [[source-adyen-docs-account-single-sign-on-set-up-sso]], then [[raw/adyen/docs/account/single-sign-on/set-up-sso/2026-09-15]].

**Answer boundary:** Raw lines 23–34 require SAML 2.0, company-account setup, a configuring user with Merchant admin or Merchant user management, and legal-notice acceptance by an authorized representative; retaining a non-SSO admin is recommended for troubleshooting. Lines 36–69 give IdP field mappings, test-before-live order, SAML request/response signing, email NameID and provider-specific Azure/Google metadata conditions. Lines 71–92 make existing-user SSO migration separate from configuration save. Lines 94–132 require an existing IdP account, let the creator select account access and only roles they hold. Lines 134–179 distinguish company and merchant-access user-creation API routes and test example. Merchant-account user access does not mean a merchant account can configure SSO.
