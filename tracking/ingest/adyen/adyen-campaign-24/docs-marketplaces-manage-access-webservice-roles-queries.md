# C24 Marketplace web-service role retrieval checks

## Q1 — What credential and roles enable balance-platform resource and transfer API actions?

The page requires Adyen for Platforms and a Balance Platform API key; web-service roles control the credential's allowed API requests, with additional roles enabled in Customer Area when needed (raw lines 19–28). BCL covers creating/updating/deleting account holders, balance accounts and transfer instruments. TransferService Initiate starts transfers and TransferService Retrieve views initiated ones (raw lines 34–40, 53–61). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-access-webservice-roles]] → [[raw/adyen/docs/marketplaces/manage-access/webservice-roles/2026-09-15]].

## Q2 — Which dependencies and version limits prevent overbroad role assumptions?

BCL PCI can reveal PAN/CVV/CVC in a `/paymentInstruments` POST response and requires BCL in addition (raw line 41). Issuing roles apply only if the integration includes Issuing; the TransactionRules permission is also included in BCL (raw lines 43–50). Bank Transfer Initiation role applies only to Transfers API **v1**, unlike the separately listed TransferService roles (raw lines 53–61). A default-role statement or role description does not prove an actual credential's grant, card reveal or transfer outcome (raw lines 19–28). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-manage-access-webservice-roles]] → [[raw/adyen/docs/marketplaces/manage-access/webservice-roles/2026-09-15]].
