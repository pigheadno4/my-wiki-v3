---
title: "Adyen Issuing API credential web service roles"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-access/webservice-roles"
raw_files:
  - "adyen/docs/issuing/manage-access/webservice-roles/2026-09-15.md"
tags: [adyen, issuing, api-credentials, access-roles, transfers]
---

## Overview

Adyen's API-credential role reference (last modified 2022-12-16, captured 2026-09-15) describes web service roles that control which Configuration API and Transfers API requests a credential may make. Although published under Issuing, the page's requirements specify an **Adyen for Platforms integration** and a **Balance Platform API key** for those APIs. Default roles are assigned when a company account is created; additional roles may need enabling in Customer Area. A listed permission is not evidence that a particular credential already has it. [[adyen-issuing]] [[adyen]]

## Key takeaways

- **Balance platform configuration:** Balance Platform BCL role permits creating, updating and deleting resources such as account holders, payment instruments and transaction rules. Balance Platform BCL PCI role permits unmasking PAN and CVV/CVC in the response to POST `/paymentInstruments` and additionally requires BCL. This sensitive role is scoped to that response description in this source. See raw lines 34–41.
- **Issuing roles:** Bank SCA Webservice Role manages device registration for Strong Customer Authentication. Bank Manage TransactionRules role manages platform risk-engine rules; its permissions are included in Balance Platform BCL role. See raw lines 43–50.
- **Transfer roles:** Bank Transfer Initiation Webservice role permits initiating transfers **only for Transfers API v1**. TransferService Webservice Initiate role also permits initiating transfers; TransferService Webservice Retrieve role permits viewing initiated transfers. The table does not establish transfer execution or settlement. See raw lines 53–61.

## Detail locators

- Credential role model, default roles and Customer Area enablement: raw lines 19–20.
- Platforms integration and Balance Platform API key requirements: raw lines 21–28.
- Configuration and PCI role dependency: raw lines 34–41.
- SCA, risk-rule and transfer role table: raw lines 43–61.

## Related

- [[adyen-issuing]] — Issuing concept.
- [[adyen-platforms]] — required integration context in this guide.
- [[adyen-api-access]] — broader API credential context.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-access/webservice-roles/2026-09-15|Roles for API credentials, captured 2026-09-15]]
