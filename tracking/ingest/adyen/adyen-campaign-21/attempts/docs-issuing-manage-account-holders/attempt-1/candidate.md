---
title: "Adyen Issuing: Manage account holders"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-account-holders"
raw_files:
  - "adyen/docs/issuing/manage-account-holders/2026-09-15.md"
tags: [adyen, issuing, account-holders, capabilities, verification]
---

## Overview

This Adyen Issuing guide (last modified 2023-03-28; captured 2026-09-15) describes Configuration API and Customer Area operations for an account holder: the user resource associated with legal entities, balance accounts, and capability information. It is part of onboarding and verification, rather than evidence that a holder is verified or a card or payment is active. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- **Create and observe:** Create a legal entity before POST `/accountHolders` with its ID; for a sole proprietorship, the guide specifies the owner's individual legal-entity ID. Save the distinct account-holder ID for webhook matching, balance-account creation, and later updates. The creation example returns `status: active` while its default capabilities are `allowed: false` and `verificationStatus: pending`; active resource status does not establish usable capabilities. The `balancePlatform.accountHolder.updated` webhook reports resulting capability verification statuses after Adyen's checks.
- **Identify and update:** Customer Area and GET `/accountHolders/{id}` show the holder and associated legal entities, balance accounts, capabilities, and verification information. The *liable account holder* relates to the platform company's legal entity; it is not every user holder. PATCH `/accountHolders/{id}` can update the holder; changing `primaryBalanceAccount` is the guide's example.
- **Suspend, reactivate, close:** Holders cannot be deleted. API suspension disables payout capabilities while related balance accounts and payment instruments remain active. API reactivation to `active` is only for a currently suspended holder; an Adyen-suspended holder cannot be reactivated with this API. Permanent close requires each balance account to be empty, closing non-primary accounts before the primary, then closing the holder. A balance account can also be closed while the holder stays active. Status-change webhooks cover API and Adyen-initiated changes. These instructions do not prove a transfer or close has completed.
- **Capabilities:** Read `allowed`, `enabled`, `verificationStatus`, and nonempty `problems` separately. Some capabilities are requested automatically; additional requests go to Adyen for approval. The request example returns `requested: true`, `allowed: false`, and pending verification. Customer Area requests and enable/disable actions require the **Manage account holder capabilities** role; the API examples use PATCH. The raw enable/disable example sends `sendToTransferInstrument.enabled: false` but its displayed response instead names `withdrawFromAtm`; do not use that response to verify the requested field.
- **KYC and access:** Customer Area provides a legal-entity KYC summary/timeline and uploaded documents. Its **Rejected** legal-entity status is final in this guide; **Unsuccessful** directs the reader to resolve errors. Capability audit-log access, individual PII search, and KYC-document view/download have distinct Customer Area roles, with privacy caution for document roles.

## Detail locators

- Resource definition, creation prerequisite, response/default capabilities, and webhook: pinned raw lines 19–290.
- Holder lookup, liable-holder distinction, and primary-balance-account PATCH: pinned raw lines 292–748.
- Suspension, reactivation, permanent-close order and zero-balance prerequisite: pinned raw lines 750–1223.
- Capability states, request/enable roles and API examples, including the mismatched enable/disable response: pinned raw lines 1225–1868.
- Capability audit role and KYC statuses/document roles: pinned raw lines 1870–1944.

## Related

- [[adyen-issuing]] — Issuing resource and card-program context.
- [[source-adyen-docs-platforms-manage-account-holders]] — parallel Platforms guide; keep its platform scope distinct.
- API URLs and SDK examples in the raw use test environments and named library versions; they do not establish current eligibility, live card issuance, authorization, capture, or settlement.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-account-holders/2026-09-15|Adyen Issuing Manage account holders, captured 2026-09-15]]
