# C24 query checks — docs-marketplaces-manage-access-api-credentials-web-service

## Q1 — Purpose and prerequisites
Q: Which Marketplace balance-platform API credentials are used for web service versus LEM requests, and who can configure them?
A: This guide distinguishes web-service users for Configuration/Transfers/Platform Experience session authentication (Capital needs additional configuration) from LEM users for Legal Entity Management and Onboarding-component session authentication. Configuration is at company-account level and needs an Adyen for Platforms integration plus a Customer Area user with Manage API credentials or Merchant admin role. See raw/adyen/docs/marketplaces/manage-access/api-credentials-web-service/2026-09-15.md:33-53, :68-75.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-access-api-credentials-web-service]] → [[raw/adyen/docs/marketplaces/manage-access/api-credentials-web-service/2026-09-15]].

## Q2 — Rotation and lifecycle boundary
Q: Do API-key and basic-auth-password rotations have the same overlap, and can a credential be deleted?
A: No. A new API key activates immediately and the previous key stays active for 24 hours unless expiry is reset or accelerated; a new basic-auth password deactivates the previous password immediately. Live credentials/keys are separately created in live Customer Area. Credentials cannot be deleted; deactivation blocks use of their API keys. A credential's existence alone does not prove its enabled roles. See raw/adyen/docs/marketplaces/manage-access/api-credentials-web-service/2026-09-15.md:128-156, :158-185, :207-233.
Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-access-api-credentials-web-service]] → [[raw/adyen/docs/marketplaces/manage-access/api-credentials-web-service/2026-09-15]].
