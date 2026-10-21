---
title: "Adyen Marketplace user capabilities"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/verification-overview/capabilities"
raw_files:
  - "adyen/docs/marketplaces/verification-overview/capabilities/2026-09-15.md"
tags: [adyen, marketplaces, account-holders, capabilities, verification]
---

## Overview

This 2024-modified Marketplace-route Adyen for Platforms guide, captured 2026-09-15, explains account-holder capabilities: default or additional requests, KYC verification status, and separate `requested`, `allowed` and `enabled` settings. A capability is usable only when allowed and enabled; requesting it can prompt further checks. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Adyen usually configures default capabilities during design; they are automatically requested when account holders are created. A nondefault capability must be requested separately and may trigger additional KYC checks (raw lines 19–27). `requested: true` records the request, not verification approval or usability.
- Base capabilities cover receiving platform split payments, receiving/sending between balance accounts, and transfers to/from verified bank-account instruments. The between-balance-account capabilities are only required across different account holders; `receiveFromTransferInstrument` is only required for top-ups and its request triggers upfront verification (raw lines 29–35).
- Optional financial-product sections list Business Account, Issuing and Capital capabilities only if the business offers those products. `issueBankAccount` enables `receiveFromThirdParty` and `sendToThirdParty` by default; Issuing includes card issue/use, ATM/restricted-use levels, and a LEM API v3 transfer-instrument-level `sendToTransferInstrument` verification qualifier; Capital has `getGrantOffers` and `receiveGrants` (raw lines 37–92). The Issuing level amounts are dated per-card/per-day thresholds, not proof of current eligibility or an enabled card (raw lines 70–83).
- Verification status can be read in `balancePlatform.accountHolder.created/updated` webhooks or GET `/accountHolders/{id}`. First-time `pending` normally has requested true, allowed false; re-verification after changed data can show `pending` while allowed true. `valid` sets allowed true. Ordinary `invalid` sets allowed false with problems/remediation data, and `rejected` is final and cannot be repaired by updating data or uploading documents (raw lines 94–108).
- There is a consequential `invalid` exception: after previously successful verification, changed or missing user data can revert the status to `invalid` while allowed remains true during a specific remediation deadline. The user must supply the required information in that period; the page does not specify a universal duration (raw lines 107, 120). Thus status alone must be read with the current `allowed` setting and deadline context.
- The API capability object exposes `requested`, `allowed` and `enabled`. `enabled` is a platform access control; changing it does not trigger verification or stop a request. A capability can be used only when **both** `allowed` and `enabled` are true, including during any permitted re-verification or deadline window (raw lines 110–121).

## Detail locators

- Default/additional request and KYC trigger: raw lines 19–27. Base capability names and conditional use: raw lines 29–35. Conditional financial-product names, LEM v3 qualifier and Issuing levels: raw lines 37–92.
- Status update routes and `pending`/`valid`/`invalid`/`rejected` distinctions: raw lines 94–108. Requested/allowed/enabled settings and deadline exception: raw lines 110–121.

## Related

- [[adyen-platforms]] — broader account-holder and balance-platform model for this Marketplace route.
- [[source-adyen-docs-platforms-verification-overview-capabilities]] — related Platforms capability guide; consult it separately for its own snapshot.
- [[adyen-classic-platforms]] — older Classic model, with different resources and verification workflow.

## Raw Sources

- [[raw/adyen/docs/marketplaces/verification-overview/capabilities/2026-09-15|Marketplace user capabilities, captured 2026-09-15]]
