---
title: "Adyen Payouts in Stages to Bank Accounts and Wallets"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/online-payouts/payouts-to-bank-accounts-and-wallets"
raw_files:
  - "adyen/docs/online-payments/online-payouts/payouts-to-bank-accounts-and-wallets/2026-09-15.md"
tags: [adyen, payouts, payout-api, bank-accounts, wallets, four-eye-review]
---

## Overview

This Adyen Docs snapshot explains staged outbound payouts to bank accounts or wallets through the legacy Payout API. The page's worked requests use bank accounts; its recipient-region table separately lists bank and PayPal payout methods. This is a merchant payout flow, distinct from accepting shopper payments. See [[adyen]] and [[adyen-payouts]].

Adyen says it no longer accepts new Payout API integrations. It directs new integrations to the Transfers API and existing Payout API integrators to their Adyen contact for migration information. Staged payouts require Adyen compliance approval and additional configuration; this snapshot does not establish current merchant eligibility or successful payout execution.

## Key takeaways

- A four-eye check separates the submitting user from the user who confirms or declines the payout. The documented `storePayout` credential stores recipient details and submits payouts, while `reviewPayout` confirms or declines them.
- The merchant first saves recipient account details in a recurring contract, then either submits with `/submitThirdParty` or stores details and submits in one `/storeDetailAndSubmitThirdParty` call. The last stage is confirmation or decline through the corresponding review endpoint or Customer Area. The examples use test endpoints and versioned API-library snippets; they are illustrations of this legacy path.
- Every staged payout must be confirmed or declined within seven days or it expires. Review requests use the PSP reference returned by the submit or combined store-and-submit response as `originalReference`. A submit response in the examples is receipt of a payout submission, not evidence of successful disbursement.
- The snapshot's recipient-country table is method-specific for bank payouts and PayPal. It states that payouts are only in local currency and that a local entity is required in most cases. The table does not determine present-day availability or approval for an account.

## Detail locators

- Opening notice and prerequisites, raw lines 19–38 — Payout API migration direction, separate credential roles, four-eye check, compliance approval, and configuration.
- `## Overview`, raw lines 40–57 — alternative store-then-submit and combined store-and-submit paths, followed by review.
- `## Store payout details`, raw lines 59–563 — recurring contract, `/storeDetail`, bank-account examples, and example response.
- `## Submit a payout`, raw lines 564–821 — `/submitThirdParty`, stored-detail reference, example request and submission response.
- `## Store details and submit a payout`, raw lines 822–1271 — combined endpoint, `RECURRING,PAYOUT` contract example, and example response.
- `## Confirm or decline a payout`, raw lines 1272–1685 — seven-day expiry, Customer Area route, `/confirmThirdParty`, `/declineThirdParty`, reviewer permissions, and `originalReference`.
- `## Supported countries/regions`, raw lines 1686–1723 — recipient-country/method matrix, local-currency condition, and qualified local-entity condition.

## Related

- [[adyen]] — provider page.
- [[adyen-payouts]] — outbound payout concept and legacy API boundary.
- [[source-adyen-docs-online-payments-online-payouts]] — separate legacy Payout API overview and instant-versus-staged route.

## Raw Sources

- [[raw/adyen/docs/online-payments/online-payouts/payouts-to-bank-accounts-and-wallets/2026-09-15|Adyen Docs — Payouts in stages (2026-09-15 snapshot)]]
