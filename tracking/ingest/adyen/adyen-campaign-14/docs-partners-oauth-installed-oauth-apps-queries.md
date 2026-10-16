# Fixed retrieval checks — docs-partners-oauth-installed-oauth-apps

## Q1 — Purpose, scope, and what not to infer

**Query:** What does the installed OAuth apps page explain, and what does it not establish?

**Answer:** It describes the customer-side Customer Area route for authorizing a partner-created OAuth app on selected merchant accounts, viewing installed apps, uninstalling one, and interpreting the audit-trail actor. It does not show that any named customer granted or revoked access, that all merchant accounts were included, or that a partner performed an authorized payment. The raw webpage was last modified 2023-05-04 and captured 2026-09-15. Evidence: raw lines 11, 15–25, 27–65. Canonical route: [[adyen-index]] → [[adyen-partner-oauth]] → ## Sources → [[source-adyen-docs-partners-oauth-installed-oauth-apps]] → [[raw/adyen/docs/partners/oauth/installed-oauth-apps/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** How are installed apps consented to, viewed and revoked, and what access/token boundary matters?

**Answer:** A partner creates the app and redirects the customer to Adyen. The customer authenticates, selects one or more merchant accounts, and reviews a fixed app scope they cannot modify. Viewing installed apps and revoking one each require company-account access plus Merchant admin role in Customer Area. Revocation is **Developers → OAuth authorizations → Edit → Uninstall**; the page says it immediately revokes app access to the account and invalidates all active access. It does not specify token-type-by-token-type invalidation or a revocation API. The audit actor uses `oauth_[Authorization_ID]@Company.[YourCompanyAccount]`. The page is procedural, not a record of actual consent or revocation. Evidence: raw lines 19–65. Canonical route: [[adyen-index]] → [[adyen-partner-oauth]] → ## Sources → [[source-adyen-docs-partners-oauth-installed-oauth-apps]] → [[raw/adyen/docs/partners/oauth/installed-oauth-apps/2026-09-15]].
