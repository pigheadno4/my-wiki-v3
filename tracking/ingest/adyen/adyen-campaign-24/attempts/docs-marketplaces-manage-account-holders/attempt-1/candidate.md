---
title: "Adyen Marketplace: Manage account holders"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-account-holders"
raw_files:
  - "adyen/docs/marketplaces/manage-account-holders/2026-09-15.md"
tags: [adyen, marketplaces, platforms, account-holders, capabilities]
---

## Overview

This Marketplace-path Balance Platform guide (last modified 2023-03-28; captured 2026-09-15) treats the account holder as the marketplace user's Configuration API resource, linked to legal entities, balance accounts and capabilities. It covers lookup, primary-balance-account updates, suspension/reactivation/closure, capability controls and Customer Area KYC views. It uses modern `/accountHolders/{id}` and related Balance Platform routes, distinct from Classic Account API account holders. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Account holders cannot be deleted. Customer Area and GET `/accountHolders/{id}` show status, linked legal entities/balance accounts, documents and capabilities; paginated list routes cover marketplace account holders and an account holder's balance accounts. Searching an individual main legal entity by name or email needs the **View account holders PII** role. The liable account holder belongs to the company's legal entity. See raw lines 19–73 and 218–271.
- PATCH `/accountHolders/{id}` can update fields such as `primaryBalanceAccount`. Setting `status=suspended` temporarily disables payout capabilities; when suspended through the API, related balance accounts and payment instruments remain active. Status changes are reported through `balancePlatform.accountHolder.updated` webhooks, including Adyen-initiated changes. See raw lines 273–290, 468–485 and 704–713.
- Reactivation by API uses `status=active` only from `suspended`; the page says an account holder suspended by Adyen cannot be reactivated through the API. Permanent closure requires empty balance accounts, then closing non-primary accounts before the primary account, then closing the account holder. If funds remain, the guide routes to payout or internal transfer before closure; the described sequence is not evidence those movements occurred. See raw lines 714–718 and 942–956.
- A capability response separates `requested`, `allowed`, `enabled`, `verificationStatus` and `problems`. An additional capability can be requested through Customer Area or PATCH with `requested=true` and `requestedLevel` if required; the example response is `requested=true`, `allowed=false`, `pending`, so request is not approval. Customer Area requests and enable/disable edits require **Manage account holder capabilities** role; PATCH `enabled` toggles platform use separately from Adyen's `allowed` decision. See raw lines 958–1024, 1268–1326 and 1569–1591.
- **Example mismatches:** The additional-capability prose calls the example `receivePayment`, while most request/response payloads use `receivePayments`; Python/Ruby examples use `withdrawFromAtm` instead. In the disable-capability API example, the request targets `sendToTransferInstrument`, but the displayed response names `receivePayments`. Use these snippets as illustrations, not a verified one-to-one request/response trace. See raw lines 1020–1044, 1196–1242 and 1328–1345, 1569–1591.
- Customer Area provides a capability audit log with a **View capabilities audit trail** role. KYC summary/timeline distinguishes awaiting data, in review, verified, unsuccessful and rejected; the page says rejected is final and cannot be remedied by data/document updates. KYC document access requires **View KYC documents** and **Download KYC documents** roles and has a privacy boundary. These views do not establish live verification or payout for a specific account holder. See raw lines 1593–1671.

## Detail locators

- Account-holder identity, view/search, liable holder and API list routes: raw lines 19–271.
- Primary-account update, suspend/reactivate and status webhooks: raw lines 273–945.
- Zero-balance and ordered permanent closure: raw lines 946–956.
- Capability view/request/enable controls and response examples: raw lines 958–1591.
- Capability audit, KYC statuses, document roles and views: raw lines 1593–1671.

## Related

- [[adyen-platforms]] — main concept for this Marketplace-path Balance Platform resource.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-account-holders/2026-09-15|Manage account holders, captured 2026-09-15]]
