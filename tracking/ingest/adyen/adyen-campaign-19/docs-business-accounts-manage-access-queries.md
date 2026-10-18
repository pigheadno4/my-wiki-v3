# Business accounts manage access — retrieval probes

## Q1 — Purpose and authorization boundary

**Query:** Does seeing a Business accounts role in this guide show that my user has a live opened account or can initiate a transfer?

**Expected answer:** No. The 2023-modified guide describes Customer Area team access and API-credential role types for a balance-platform integration. Admin activation follows email verification, team users use MFA or SSO, and Customer Area can manage resources, transfers, credentials and webhooks. The documentation does not establish any particular person's assignment, live Business account, request acceptance, transfer booking or bank receipt.

**Raw locators:** lines 15–39 and 50–59. **Canonical discovery route:** [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-manage-access]] → [[raw/adyen/docs/business-accounts/manage-access/2026-09-15]]. Provider-index Business accounts link is pending coordinator repair.

## Q2 — Roles, dependencies and API version

**Query:** Which roles view Business accounts or sole-proprietor IBAN, mutate platform resources, handle SCA or initiate/retrieve transfers?

**Expected answer:** Customer Area Balance platform base role views transfers and platform/account resources. View payment instrument PII adds sole-proprietor Adyen-issued IBAN visibility and requires base role. Separately, web-service BCL creates/updates/deletes platform configuration resources; BCL PCI additionally requires BCL and is limited to PAN/CVV/CVC unmasking in the described payment-instrument POST response; Bank SCA manages SCA devices. Transfer initiation roles differ: Bank Transfer Initiation is stated as Transfers API v1-only, TransferService Initiate initiates, and TransferService Retrieve views initiated transfers. These descriptions are not evidence of actual assigned access or financial execution.

**Raw locators:** lines 41–48 and 50–83. **Canonical discovery route:** [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-manage-access]] → [[raw/adyen/docs/business-accounts/manage-access/2026-09-15]]. Provider-index Business accounts link is pending coordinator repair.
