---
title: "Adyen Marketplace web service roles for API credentials"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-access/webservice-roles"
raw_files:
  - "adyen/docs/marketplaces/manage-access/webservice-roles/2026-09-15.md"
tags: [adyen, marketplaces, api-credentials, roles, transfers, issuing]
---

## Overview

This 2023-modified Marketplace-route Adyen for Platforms guide, captured 2026-09-15, maps frequently used web service roles on a balance-platform API credential to Configuration API, Transfers API and optional Issuing actions. Adyen assigns default company-account roles, but specific functions may require enabling additional roles in Customer Area. [[adyen]] [[adyen-platforms]]

## Key takeaways

- The guide requires an Adyen for Platforms integration and a **Balance Platform API key** for Configuration and Transfers APIs. Web service roles determine requests a particular credential may perform; default role assignment at company-account creation does not imply every listed permission is present (raw lines 19–28). The displayed `ws...@BalancePlatform...` identifier is an example format, not a credential to use.
- **Balance Platform BCL role** permits creation, update and deletion of balance-platform resources such as account holders, balance accounts and transfer instruments. **Balance Platform BCL PCI role** permits unmasking/viewing PAN and CVV/CVC in a POST `/paymentInstruments` response and additionally requires BCL role enabled (raw lines 34–41). This is a sensitive-data permission description, not authorization to reveal card data outside an approved integration.
- If the integration includes Issuing, **Bank SCA Webservice Role** manages SCA device registration. **Bank Manage TransactionRules role** manages platform risk-engine rules, but the guide says BCL already includes all its permissions (raw lines 43–50). Issuing inclusion is conditional; a role listing does not establish that product access is enabled.
- For fund transfers, **Bank Transfer Initiation Webservice role** can initiate transfers **only with Transfers API v1**. **TransferService Webservice Initiate role** initiates transfers, and **TransferService Webservice Retrieve role** views initiated transfers (raw lines 53–61). The v1-only role must not be generalized to later Transfers API versions. Role possession alone does not prove a transfer was submitted or booked.

## Detail locators

- Credential role model, default versus additional roles, integration/API key prerequisites: raw lines 19–28. Balance-platform BCL and PCI dependency/sensitive response: raw lines 34–41.
- Optional Issuing SCA/risk-rule roles and BCL inclusion: raw lines 43–50. Transfers roles and v1-only initiation qualifier: raw lines 53–61.

## Related

- [[adyen-platforms]] — balance-platform model for this Marketplace route.
- [[source-adyen-docs-marketplaces-manage-access-api-credentials-web-service]] — credential setup and lifecycle.
- [[adyen-issuing]] — optional Issuing product, with separate eligibility and card-data requirements.
- [[adyen-classic-platforms]] — separate older account/API model.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-access/webservice-roles/2026-09-15|Marketplace web service roles, captured 2026-09-15]]
