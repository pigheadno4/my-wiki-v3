# Retrieval checks — Issuing API credential roles

## Q1: What prerequisites and roles are needed to configure Issuing resources and reveal card details?

This 2022-modified page requires an Adyen for Platforms integration and Balance Platform API key to access the Configuration and Transfers APIs; a credential may need additional web service roles enabled in Customer Area (raw lines 19–28). Balance Platform BCL permits create/update/delete of balance-platform resources. BCL PCI permits PAN and CVV/CVC unmasking in the POST `/paymentInstruments` response and requires BCL as well (raw lines 34–41). The catalog does not prove that any specific credential has these roles. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-access-webservice-roles]] → [[raw/adyen/docs/issuing/manage-access/webservice-roles/2026-09-15]].

## Q2: Which roles cover SCA, risk rules and transfers, and what version boundary applies?

Bank SCA Webservice Role manages SCA device registration; Bank Manage TransactionRules manages risk-engine rules and is included in BCL permissions (raw lines 43–50). Bank Transfer Initiation Webservice role initiates transfers only with Transfers API v1, while TransferService Webservice Initiate initiates and TransferService Webservice Retrieve views initiated transfers (raw lines 53–61). Permission labels do not establish a successful or settled transfer. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-manage-access-webservice-roles]] → [[raw/adyen/docs/issuing/manage-access/webservice-roles/2026-09-15]].
