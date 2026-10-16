---
title: "Adyen for Platforms user capabilities and verification status"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-overview/capabilities"
raw_files:
  - "adyen/docs/platforms/verification-overview/capabilities/2026-09-15.md"
tags: [adyen, platforms, account-holders, capabilities, verification]
---

## Overview

This 2024-modified, 2026-09-15-captured Adyen for Platforms guide describes account-holder capabilities, financial-product capability names, capability verification statuses, and the distinct `requested`, `allowed`, and `enabled` settings. It concerns permissions for a platform user’s account holder, not evidence that a particular user passed KYC, has an enabled product, received a payment, or moved funds. See [[adyen-platforms]].

## Key takeaways

- Adyen says it configures default capabilities for a platform during design in most cases; those are requested automatically when the platform creates users’ account holders. A nondefault capability must be requested separately and may prompt additional KYC checks. Requested is therefore not the same as verified, allowed, or enabled.
- The core table distinguishes receiving from another account holder’s balance account, receiving top-ups from a verified transfer instrument, receiving split-payment funds, receiving payments by a payment method, sending to another account holder’s balance account, and sending to a verified transfer instrument. The receive/send balance-account capabilities are required only across different account holders. `receiveFromTransferInstrument` is required only for the top-up feature and its request triggers upfront verification. Consult raw lines 25–36 for exact API names and conditions.
- Additional capabilities depend on the business offering the relevant financial product: business accounts (`issueBankAccount`, third-party receive/send), issuing (`issueCard`, `useCard`, ATM/restricted-country/industry and transfer capabilities), or Capital (`getGrantOffers`, `receiveGrants`). The business-account table says third-party receive/send are enabled by default when `issueBankAccount` is present. For issuing, the guide says Legal Entity Management API v3 verifies `sendToTransferInstrument` at transfer-instrument level, so one verified card can be usable independently of the legal entity’s other instruments. These are product-scoped statements, not universal platform permissions.
- Card-issuing capability levels are low, medium, or high, with per-card, per-day thresholds in the table and potentially more checks and monitoring at higher levels. Restricted-industry limits are industry-specific; the table is dated, and a level label alone does not establish current geography, product access, or transaction approval.
- An initially requested capability under `pending` verification has `requested=true` and `allowed=false`. A previously allowed capability may remain `allowed=true` while changed user data is checked. `valid` normally sets `allowed=true`; `rejected` is final and sets `allowed=false`. `invalid` normally sets `allowed=false` with remediation errors, yet the page describes a distinct post-success user-data-change/missing-data period where status reverts to `invalid`, a deadline applies, and `allowed` stays true so use may continue during that period. Do not reduce status alone to a permission decision.
- The account-holder API response and created/updated webhooks expose capability state. `requested` indicates request, `allowed` indicates Adyen permission, and `enabled` controls the platform’s offer/access; use requires both `allowed=true` and `enabled=true`. Changing `enabled` does not itself trigger verification or prevent a capability request. The document names no fixed grace deadline, and reading a state is not authorization to change a live account.

## Detail locators

- Account-holder default versus added capability requests: pinned raw lines 15–27.
- Core capability names and cross-account/top-up conditions: pinned raw lines 29–36.
- Business account, card issuing and Legal Entity Management API v3 transfer-instrument qualification: pinned raw lines 38–69.
- Issuing levels, per-card/day thresholds and Capital capabilities: pinned raw lines 71–93.
- `pending`, `valid`, `invalid`, `rejected` and remediation/deadline exceptions: pinned raw lines 95–109.
- Account-holder webhook/GET routes and requested/allowed/enabled settings: pinned raw lines 111–128.

## Related

- [[adyen]]
- [[adyen-platforms]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/platforms/verification-overview/capabilities/2026-09-15|Platforms capability-status snapshot (2026-09-15)]]
