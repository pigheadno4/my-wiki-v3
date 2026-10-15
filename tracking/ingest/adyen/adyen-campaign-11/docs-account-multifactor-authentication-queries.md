# Customer Area MFA retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** Does Adyen require both MFA and SSO for Customer Area users, and does this guide prove a merchant has enabled either method?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-account-multifactor-authentication.md` → pinned raw `raw/adyen/docs/account/multifactor-authentication/2026-09-15.md`, lines 15–31. The account guide says Customer Area users must set up MFA **or** SSO (line 19), and describes MFA as additional login verification. It is about human Customer Area logins, not web service API credentials or payment authorization. The page gives setup procedures and does not prove a specific user's enrollment, effective account policy, working login, or any payment result. Its metadata last-modified date is 2024-01-12 (line 11).

## Q2 — Methods, prerequisites, admin scope, recovery limit

**Query:** What MFA methods and device limits does the guide give, who may remove a user's device, and does it document locked-out recovery?

**Expected route and answer:** `wiki/sources/adyen/source-adyen-docs-account-multifactor-authentication.md` → raw lines 23–41 for one method per device, two devices, app/SMS and hardware requirements; lines 43–52 for first-login authenticator-app enrollment; lines 54–68 for **live-only** SMS enrollment; lines 70–77 for own-method deletion; lines 79–89 for new-device removal and next-login registration. A Merchant admin may view user details and remove devices for users in the organization (lines 23–26); the page does not say the admin can add a factor for another user or bypass MFA. It does not provide a complete recovery flow for someone already locked out and unable to access the Customer Area; device removal and later re-registration should not be expanded into such a guarantee.
