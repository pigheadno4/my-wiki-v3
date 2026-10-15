# Customer Area user roles retrieval checks

## Q1 — Purpose and scope

**Query:** What does Adyen's user-roles page describe, and can it tell me what my API credential or current user can do?

**Answer:** It catalogs Customer Area roles for human users and their documented permissions; users can have multiple roles directly or through role groups. It does not establish a particular user's present assignments or account scope. A user role such as **Manage API credentials** permits credential administration, while the created API credential has separate roles and scope. The 2026-09-15 snapshot is not proof that any access has been granted today. **Raw locators:** `raw/adyen/docs/account/user-roles/2026-09-15.md:15-27`, `:57-65`. **Canonical route:** [[source-adyen-docs-account-user-roles]] → [[raw/adyen/docs/account/user-roles/2026-09-15]]; [[adyen-api-access]] for the separate credential boundary.

## Q2 — Grant and approval boundaries

**Query:** Can a user manager grant any role, and does a request-capable role mean the requested access or payment method is approved?

**Answer:** No. **Merchant user management** can grant only roles and account access that the managing user already has. Some permissions require company-account access or another role, so check the exact row; for example, **Manage Merchant Account Groups role** requires company access. Request-capable roles, including payment-method and merchant-account requests and partner merchant-access requests, document the ability to request, not approval or enablement. The page gives no universal restricted-role approval process. Sensitive privileges are separate: **Merchant View PII** carries a PCI-scope warning, and the default **Merchant standard role** governs login only. **Raw locators:** `raw/adyen/docs/account/user-roles/2026-09-15.md:43-65`, `:132-141`, `:198-203`, `:284-288`. **Canonical route:** [[source-adyen-docs-account-user-roles]] → [[raw/adyen/docs/account/user-roles/2026-09-15]]; [[adyen-api-access]] for API credential roles.
