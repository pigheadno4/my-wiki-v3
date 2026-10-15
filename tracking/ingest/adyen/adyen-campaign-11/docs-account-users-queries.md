# C11 fixed queries — docs-account-users

## Q1 — Purpose, scope, and inference boundary

**Query:** What does Adyen's Manage users page administer, and does it create API credentials or show the current users and permissions of a merchant account?

**Expected answer:** It is a Customer Area human-user administration guide: roles and merchant-account access, creation/duplication, editing, trusted login IPs, deactivation, and a user report. API credential identity, key rotation, and service-account scope are separate. The 2026-09-15 documentation snapshot does not reveal any particular merchant's actual users, access state, or completed account change.

**Evidence:** `raw/adyen/docs/account/users/2026-09-15.md:15-30`, `raw/adyen/docs/account/users/2026-09-15.md:41-59`, `raw/adyen/docs/account/users/2026-09-15.md:145-187`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-customer-area-iam]]` → `[[source-adyen-docs-account-users]]` → pinned raw.

## Q2 — Central capability, prerequisites, and warnings

**Query:** Who may create or remove a Customer Area user, how are account and role grants limited, and is “Delete an existing user” permanent deletion?

**Expected answer:** Creation, duplication, permission changes, and deactivation require Merchant admin or Merchant user management. A creator can grant only roles and merchant accounts/groups already accessible to them; group membership does not elevate access beyond the creator's accessible merchant accounts, and a duplicate can lose permissions the creator lacks. The “Delete” section describes deactivation, blocks self-deactivation, removes Customer Area access, and allows later reactivation. Trusted IP ranges can constrain login, with a 45-address maximum. This applies to Customer Area users, not API credentials.

**Evidence:** `raw/adyen/docs/account/users/2026-09-15.md:41-67`, `raw/adyen/docs/account/users/2026-09-15.md:93-135`, `raw/adyen/docs/account/users/2026-09-15.md:145-160`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-customer-area-iam]]` → `[[source-adyen-docs-account-users]]` → pinned raw.
