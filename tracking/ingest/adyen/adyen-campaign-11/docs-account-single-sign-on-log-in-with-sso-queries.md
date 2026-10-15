# Fixed retrieval checks: Customer Area SSO login

## Q1 — Email verification and environment scope

**Query:** How does a newly added Adyen Customer Area SSO user verify their email, and does test verification also enable live access?

**Expected answer:** An administrator-added Customer Area user receives an automated verification email. The user follows the verification link; if it expires, they ask the administrator for a new one. First and last name entry after verification is optional. Email verification must be completed separately for test and live Customer Area; a test verification does not establish live access. This is an individual user login procedure, not API credential setup or evidence that a particular user currently has account membership or a role.

**Raw locators:** purpose and IdP context, lines 15–20; verification, expiry and test/live separation, lines 22–33. **Canonical retrieval route:** [[adyen-index]] → [[adyen-customer-area-iam]] → [[source-adyen-docs-account-single-sign-on-log-in-with-sso]] → [[raw/adyen/docs/account/single-sign-on/log-in-with-sso/2026-09-15|pinned raw]].

## Q2 — Customer Area and IdP login paths

**Query:** After verification, how does a user log in with SSO from Customer Area or from an IdP, and what does the guide establish about authorization?

**Expected answer:** From Customer Area, the user enters the verified email in Username and selects Next. If already signed in to the identity provider, the user is redirected to Customer Area; otherwise the user signs in at the IdP and is redirected back. The user can also start at the IdP and choose Adyen Customer Area. The guide says SSO becomes the required login method. Its examples of IdPs are Okta, Azure and Microsoft AD FS. The described redirects do not prove a successful session, specific role permission, payment-operation authorization, session lifetime or domain/IdP configuration.

**Raw locators:** IdP context, lines 19–20; post-verification login, lines 35–44; Customer Area and IdP entry routes, lines 46–61. **Canonical retrieval route:** [[adyen-index]] → [[adyen-customer-area-iam]] → [[source-adyen-docs-account-single-sign-on-log-in-with-sso]] → [[raw/adyen/docs/account/single-sign-on/log-in-with-sso/2026-09-15|pinned raw]].
