# Retrieval checks — docs-payouts-payout-service-manage-access-webservice-roles

Q1. Which integration/key does this Payout Service-path page require, and what are the transfer-role actions?

A1. It requires an Adyen for Platforms integration and a Balance Platform API key for Configuration API and Transfers API access (raw lines 21–28). The Bank Transfer Initiation Webservice role is v1-only; TransferService Webservice Initiate can initiate transfers, while TransferService Webservice Retrieve can view initiated transfers (raw lines 30–38). Defaults are assigned at company-account creation, but additional roles may need enabling for a specific API action (raw line 19). Route: [[index]] → [[adyen-index]] → [[adyen-payouts]] → [[source-adyen-docs-payouts-payout-service-manage-access-webservice-roles]] → [[raw/adyen/docs/payouts/payout-service/manage-access/webservice-roles/2026-09-15]].

Q2. Does a Balance Platform API key or Retrieve role authorize initiation, and is the v1 limit stated for both initiation roles?

A2. No. Roles specify which requests a credential may perform (raw line 19). Retrieve is limited here to viewing initiated transfers, whereas the separate Initiate role permits initiation (raw lines 37–38). The v1-only note is attached to **Bank Transfer Initiation Webservice role** alone, not to TransferService Webservice Initiate (raw lines 36–37). The page's Platforms prerequisite and `ca-test.adyen.com` navigation do not prove a LIVE grant, accepted request or completed payout (raw lines 19, 27–28). Route: [[index]] → [[adyen-index]] → [[adyen-payouts]] → [[source-adyen-docs-payouts-payout-service-manage-access-webservice-roles]] → [[raw/adyen/docs/payouts/payout-service/manage-access/webservice-roles/2026-09-15]].
