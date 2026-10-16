---
title: "Adyen Platforms web service roles for API credentials"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-access/webservice-roles"
raw_files:
  - "adyen/docs/platforms/manage-access/webservice-roles/2026-09-15.md"
tags: [adyen, platforms, api-credentials, roles, access-control]
---

## Overview

Adyen lists frequently used web service roles for a Balance Platform API credential used with its Configuration and Transfers APIs. Roles control which API requests that credential can perform. The page is scoped to an Adyen for Platforms integration with a Balance Platform API key; Issuing roles apply only if the integration includes Adyen Issuing. See [[adyen]] and [[adyen-platforms]]. This documented role catalog does not show which roles are actually granted to a particular credential, account, or environment, nor does it prove that an API operation succeeded.

## Key takeaways

- Adyen assigns default roles when a company account is created, but specific Configuration or Transfers API functionality may require enabling additional roles in Customer Area. The required API credential is a Balance Platform API key; the displayed `ws...@BalancePlatform...` name is only an example. Check the credential's actual role assignment and environment before relying on any permission. See raw lines 17–32.
- **Balance platform configuration:** `Balance Platform BCL role` permits creating, updating, and deleting resources such as account holders, balance accounts, and transfer instruments. `Balance Platform BCL PCI role` can unmask/view PANs and CVVs/CVCs in a POST `/paymentInstruments` response and additionally requires the BCL role. The latter is a sensitive-data permission, not a generic configuration role. See raw lines 34–42.
- **Issuing:** `Bank SCA Webservice Role` manages device registration for SCA. `Bank Manage TransactionRules role` manages platform risk-engine rules; Adyen says its permissions are included in the Balance Platform BCL role. These entries are for integrations that include Issuing, not a claim that Issuing is enabled. See raw lines 43–51.
- **Transfers:** `Bank Transfer Initiation Webservice role` initiates transfers only for Transfers API v1. `TransferService Webservice Initiate role` initiates transfers, while `TransferService Webservice Retrieve role` views initiated transfers. These distinct roles do not demonstrate an actual transfer, transfer approval, or bank receipt. See raw lines 53–61.

## Detail locators

- **Scope and credential prerequisite:** raw lines 17–29. The Customer Area links in this snapshot point to `ca-test.adyen.com`; the page does not establish live credentials or grants.
- **Frequently used-role table:** raw lines 30–61, split among balance platform configuration (34–42), Issuing (43–51), and Transfers (53–61). Use the literal role names and stated API-version qualification.
- **Related access guide:** raw lines 63–65 links the manage-access overview; it is navigation, not independently read evidence for this entry.

## Related

- [[adyen-platforms]] — platform architecture and integration context.
- [[source-adyen-docs-platforms-manage-access-api-credentials-web-service]] — separately captured credential setup and role-management guide.

## Raw Sources

- [[raw/adyen/docs/platforms/manage-access/webservice-roles/2026-09-15|Adyen Roles for API credentials, fetched 2026-09-15]]
