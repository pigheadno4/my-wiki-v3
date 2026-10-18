# Fixed retrieval checks — Capital manage access

Q1. What is the purpose and scope of this source, and what does it not establish?
- Expected: A 2023-modified Capital guide captured 2026-09-15 describing Customer Area admin/team roles and balance-platform web-service API credential roles. It says an admin account is created at signup and activated after email verification; team access is role-assigned, and users set up MFA or SSO. The guide lists frequently used roles, not an exhaustive matrix. It cannot prove any actual person's active access, credential role assignment, account capability, grant initiation, disbursement or financial outcome.
- Raw locators: `raw/adyen/docs/capital/manage-access/2026-09-15.md:15-39`, `:51-64`.
- Canonical route (provider-index `[[adyen-capital]]` link is coordinator-owned and was missing at worker audit): `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-capital]]` → `wiki/sources/adyen/source-adyen-docs-capital-manage-access.md` → `[[raw/adyen/docs/capital/manage-access/2026-09-15]]`.

Q2. How do Customer Area, configuration, PCI and Capital credential roles differ?
- Expected: The Customer Area **Capital base role** views grants and grant details; it is a user role, not stated as API initiation. The setup has separate web-service and LEM credentials; web-service roles scope API requests. **Balance Platform BCL** creates/updates/deletes platform resources. **BCL PCI** additionally allows unmasked PAN/CVV/CVC in the specified `POST /paymentInstruments` response and requires BCL too. **Capital Configuration** views grant-offer and grant-account details; **Capital Grant Initiation** is described as configuring grants. These role descriptions do not grant blanket financial authority or confirm the permissions on a particular live credential.
- Raw locators: `raw/adyen/docs/capital/manage-access/2026-09-15.md:33-49`, `:51-82`.
- Canonical route (subject to coordinator index repair): `wiki/index.md` → `wiki/adyen-index.md` → `[[adyen-capital]]` → `wiki/sources/adyen/source-adyen-docs-capital-manage-access.md` → `[[raw/adyen/docs/capital/manage-access/2026-09-15]]`.
