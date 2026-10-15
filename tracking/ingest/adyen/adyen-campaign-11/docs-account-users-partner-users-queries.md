# Fixed retrieval checks — Adyen partner users

## Q1 — What is this page for, what is its scope, and what should not be inferred?

This 2023-modified guide, captured 2026-09-15, describes merchant-controlled Customer Area access for a partner who already has an Adyen Partner Portal account. The merchant selects company or merchant-account scope and user roles, then can edit or revoke access. It does not create the partner's Portal identity, define a separate partner request/approval workflow, or prove any real merchant made a user change. Retrieve through `[[adyen-customer-area-iam]]` → `[[source-adyen-docs-account-users-partner-users]]` → `[[raw/adyen/docs/account/users/partner-users/2026-09-15]]`; raw lines 15–21 and 23–83. Canonical page: https://docs.adyen.com/account/users/partner-users.

## Q2 — What are the access prerequisites, account/role choices, and lifecycle warnings?

To add, the acting user needs Merchant admin, relevant company/merchant-account access, and the roles/permissions requested by the partner; the email must match the existing Partner Portal account (raw lines 23–39). Selecting a company account grants access to all its merchant accounts, so choose scope and roles deliberately; the merchant reviews and confirms responsibility before the documented invitation/confirmation emails (lines 41–56). Later changes require Merchant admin or Merchant user management and cannot exceed the acting user's own account/role grants (lines 58–72). Access can be revoked and restored for previously enabled roles (lines 74–83). This is Customer Area user access, not API-credential scope or proof of actual account state; follow the same concept→source→raw route.
