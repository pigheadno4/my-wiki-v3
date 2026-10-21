---
title: "Adyen Payout Service API credential roles"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/manage-access/webservice-roles"
raw_files:
  - "adyen/docs/payouts/payout-service/manage-access/webservice-roles/2026-09-15.md"
tags: [adyen, payouts, payout-service, platforms, api-credentials, roles]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] Payout Service-path page maps Balance Platform API credential webservice roles to fund-transfer actions. Although located under Payout Service, its requirements explicitly call for an **Adyen for Platforms integration** and a **Balance Platform API key** for Configuration API and Transfers API access. It is an access-role guide, not proof that a particular credential has any role, that a request succeeded, or that funds moved. [[adyen-payouts]] [[adyen-platforms]]

## Key takeaways

- Adyen assigns default webservice roles when the company account is created, but additional roles may need enabling in Customer Area for specific Configuration API or Transfers API functionality. The linked `ca-test.adyen.com` Customer Area is a documentation navigation target, not evidence of LIVE credential setup. See raw lines 19–28.
- The **Bank Transfer Initiation Webservice role** permits transfer initiation **only for Transfers API v1**. The distinct **TransferService Webservice Initiate role** permits initiating transfers; the page does not assign it a version limit. Do not carry the v1-only constraint to that separate role, or infer one role is sufficient for every endpoint/version. See raw lines 30–37.
- The **TransferService Webservice Retrieve role** permits viewing initiated transfers. Retrieve and Initiate are separate permissions; possessing a key or read role alone is not initiation authority. See raw lines 28, 36–38.
- This page's Platforms integration prerequisite is specific to this guide. It does not convert the broader Payout Service umbrella into the legacy Online Payout API, or establish eligibility for another Payout Service workflow. See raw lines 21–28, 36–42.

## Detail locators

- **Default roles, additional grant and API scope:** raw lines 19–28.
- **Version-qualified and action-qualified transfer roles:** raw lines 30–38.
- **Platforms manage-access onward route:** raw lines 40–42.

## Related

- [[adyen-payouts]]
- [[adyen-platforms]]
- [[source-adyen-docs-payouts-payout-service-manage-access-api-credentials-web-service]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/manage-access/webservice-roles/2026-09-15|Adyen Payout Service webservice roles — collected 2026-09-15]]
