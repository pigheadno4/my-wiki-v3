---
title: "Adyen Issuing: user capabilities and verification status"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/verification-overview/capabilities"
raw_files:
  - "adyen/docs/issuing/verification-overview/capabilities/2026-09-15.md"
tags: [adyen, issuing, capabilities, verification]
---

## Overview

This Adyen Issuing-path user-capabilities guide (last modified 2024-02-20; captured 2026-09-15) explains how account-holder capabilities govern actions on a platform, including balance-account and verified-transfer-instrument transfers and card issuing/use. Adyen generally configures default capabilities during design; those are requested automatically when account holders are created, while a missing capability must be requested separately and may trigger additional KYC checks. It is a dated description of configuration and verification, not evidence that any account holder currently has an enabled capability. [[adyen]] [[adyen-issuing]]

## Key takeaways

- General capabilities include receiving or sending funds via balance accounts or verified transfer instruments. The balance-account receive/send capabilities are only required when the accounts have different account holders. The card-issuing list also distinguishes `issueCard`, `useCard`, ATM withdrawal, restricted-country and restricted-industry card use, and transfer capabilities. The page states that from **LEM API v3**, `sendToTransferInstrument` verification is at the transfer-instrument level, so one verified instrument may be usable independently of another instrument's verification state.
- The level table applies **per card, per day** to ATM withdrawals and restricted-country/industry card use. Low/medium/high levels may entail additional checks and monitoring. The listed ATM high ranges use strict upper bounds (under EUR 1,500 for `withdrawFromAtm`, under EUR 1,000 for restricted-country ATM withdrawals); do not infer treatment at or above those bounds. Restricted-industry limits are described only as industry-specific.
- Read `verificationStatus` together with `requested`, `allowed`, and `enabled`. A capability is usable only when it is both allowed and enabled. First-time pending verification is requested=true, allowed=false; a previously allowed capability may remain allowed=true while changed user data is checked. The page likewise describes an `invalid` data-change/deadline case that remains allowed=true temporarily, although its ordinary invalid case is allowed=false. A `rejected` status is final and cannot be remedied by updating data or uploading documents.
- `enabled` is the platform's access switch and changing it does not initiate verification or stop a request. The source points to account-holder created/updated webhooks or `GET /accountHolders/{id}` for current capability status and settings. It does not establish a card's payment authorisation, live transfer, or settlement outcome.

## Detail locators

- Raw lines 19–23 explain default versus additional capability requests and possible KYC; lines 25–34 list general transfers.
- Raw lines 36–49 list Issuing capabilities and the LEM API v3 transfer-instrument qualification.
- Raw lines 51–64 give levels and per-card/day threshold table, including strict endpoint wording and industry-specific limits.
- Raw lines 66–80 define capability verification statuses and data-change exceptions; lines 82–93 define `requested`, `allowed`, and `enabled` and how to retrieve updates.

## Related

- [[adyen-issuing]] — Issuing program context.
- [[adyen]] — provider context.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/issuing/verification-overview/capabilities/2026-09-15|Adyen Issuing user capabilities, captured 2026-09-15]]
