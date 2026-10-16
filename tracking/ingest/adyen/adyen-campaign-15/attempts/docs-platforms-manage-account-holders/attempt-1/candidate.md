---
title: "Adyen Platforms manage account holders"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-account-holders"
raw_files:
  - "adyen/docs/platforms/manage-account-holders/2026-09-15.md"
tags: [adyen, platforms, account-holders, verification]
---

## Overview

This Adyen for Platforms guide (last modified 2023-03-28; captured 2026-09-15) describes account-holder operations through the **Configuration API** and Customer Area. An account holder is the platform-user API resource linking legal entities, balance accounts and capability information. It is distinct from the underlying legal entity, its balance accounts and the platform's liable account holder; the guide does not itself prove a merchant's legal role, live eligibility, verification, payment or payout. See [[adyen]] and proposed [[adyen-platforms]].

## Key takeaways

- **Create and view:** Create a legal entity first, then POST an account holder with its legal-entity ID; for a sole proprietorship, the page specifies the owner's individual legal-entity ID. The response includes a distinct account-holder ID and default capability object; save the ID to match later webhooks, create a balance account and update the holder. Creation is part of broader onboarding and verification, not approval. Customer Area and GET routes show holder status, linked legal entities, separate balance accounts, capabilities and verification deadlines. The liable account holder is related to the platform company's legal entity, not a synonym for each seller holder.
- **Update and status:** PATCH can update an account holder, with changing its primary balance account shown as an example. Holders cannot be deleted. API suspension disables **payout capabilities** while related balance accounts and payment instruments remain active. API reactivation is limited to a holder currently suspended by the platform; the guide says an Adyen-suspended holder cannot be reactivated through that API. Status-change webhooks cover platform and Adyen-initiated updates. Do not infer all linked resources are disabled by suspension.
- **Permanent close:** To close a holder, first bring **each balance account to zero** by payout or transfer if necessary, close non-primary balance accounts before the primary, then set the account holder status to Closed. The guide also permits closing a balance account while retaining an active holder. These are consequential instructions, not an authorization to operate on a real account; completion of a transfer or bank payout is not established by the page.
- **Capabilities:** `requested`, `allowed`, `enabled` and `verificationStatus` convey different states. A request goes to Adyen for approval; the example response has requested true, allowed false and pending verification, so a request is not permission to use the capability. Customer Area request and enable/disable actions require the **Manage account holder capabilities** role. Audit-log viewing requires **View capabilities audit trail**.
- **KYC and access:** The Customer Area shows a legal-entity KYC summary/timeline and documents. Its legal-entity statuses include awaiting data, in review, verified, unsuccessful and rejected; **Rejected** is described as final. Viewing/downloading KYC documents requires respective roles and privacy care; searching an individual's legal-entity name/email requires **View account holders PII**. These status views are historical source descriptions, not a particular person's current compliance proof.
- API URLs and SDK examples in the raw use **test** environments and named library versions; they are illustrations rather than live-operation evidence. The page does not establish country- or entity-type-specific eligibility beyond its stated sole-proprietorship ID rule.

## Detail locators

- Resource identity, create prerequisite, API examples, response ID/default capabilities and webhook: pinned raw lines 15–290.
- View/search, liable account holder and distinct balance accounts: pinned raw lines 292–538.
- PATCH primary balance account and suspend/reactivate effects: pinned raw lines 540–1211.
- Destructive close ordering and zero-balance prerequisite: pinned raw lines 1213–1223.
- Capability state/request/enable roles and examples: pinned raw lines 1225–1859.
- Capability audit log, KYC status, documents and access roles: pinned raw lines 1861–1939.

## Related

- [[adyen-platforms]] — proposed platform account-holder and balance-platform hub owned by the campaign foundation worker; this entry requests a reciprocal link only.
- [[adyen-account-structure]] — Adyen company/merchant account hierarchy, a separate account model from the platform account holder.

## Raw Sources

- [[raw/adyen/docs/platforms/manage-account-holders/2026-09-15|Adyen Manage account holders, captured 2026-09-15]]
