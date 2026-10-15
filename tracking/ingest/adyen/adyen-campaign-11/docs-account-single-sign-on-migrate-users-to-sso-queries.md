# Fixed retrieval checks: Customer Area user migration to SSO

## Q1 — Scope, prerequisites and email limits

**Query:** Who can migrate Adyen Customer Area users to SSO, does migration have to include every user, and how do test/live and duplicate email addresses affect access?

**Expected answer:** The guide concerns existing Customer Area users after SSO has already been set up for the company account. Migration is optional and can cover some or all users. The administrator needs Merchant admin or Merchant user management role. Test and live Customer Area users must be migrated separately; completing test migration grants SSO access only in test. An SSO user's email becomes the username and must identify one user. If one email is used across multiple company accounts, SSO migration leaves access to only one company account; use separate email addresses per account or keep the username/account/password route. The status report distinguishes duplicate email `EMAIL_ADDRESS_ALREADY_IN_USE` from `SELECTED_MIGRATION_UNAVAILABLE`, where a separate email-login user in the same organization must change login method first.

**Raw locators:** optionality, environments and company-account email limit, lines 15–28; SSO and admin prerequisites, lines 30–39; status reasons, lines 54–68; duplicate-email correction, lines 70–80. **Canonical retrieval route:** [[adyen-customer-area-iam]] → [[source-adyen-docs-account-single-sign-on-migrate-users-to-sso]] → [[raw/adyen/docs/account/single-sign-on/migrate-users-to-sso/2026-09-15|pinned raw]].

## Q2 — Start, lockout, completion and recovery

**Query:** Does an administrator's Start migration action immediately grant SSO access, and when can migration be canceled or reversed?

**Expected answer:** No. `Ready to migrate` permits the administrator to start; `Pending migration` means the user must complete the emailed or next-login steps using previous credentials. Username-login users have individual and bulk start paths; a bulk success popup confirms only that the start succeeded. Email-login users use the user-details path with first and last name and an SSO login selection. The guide says users cannot access Customer Area until completion, and after completion cannot use previous credentials. An administrator can cancel only an unfinished migration and may start it again after canceling. Separately, an email-login user's method can be changed from SSO back to Email at any time; the page does not promise an equivalent rollback for every completed username-login migration. These are procedural snapshot statements, not proof of a real user's changed account or working IdP.

**Raw locators:** statuses, lines 54–68; username individual and bulk flow, lines 91–124; email-login flow, lines 126–146; incomplete-only cancellation and restart, lines 148–173. **Canonical retrieval route:** [[adyen-customer-area-iam]] → [[source-adyen-docs-account-single-sign-on-migrate-users-to-sso]] → [[raw/adyen/docs/account/single-sign-on/migrate-users-to-sso/2026-09-15|pinned raw]].
