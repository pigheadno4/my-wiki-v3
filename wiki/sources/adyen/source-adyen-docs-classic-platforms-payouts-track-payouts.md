---
title: "Classic Platforms payout tracking and returns"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/payouts/track-payouts"
raw_files:
  - "adyen/docs/classic-platforms/payouts/track-payouts/2026-09-15.md"
tags: [adyen, classic-platforms, payouts, notifications, returns]
---

## Overview

This 2026-09-15 Classic Adyen for Platforms guide explains how to track a sub-merchant/account-holder bank payout through notifications or Customer Area and respond to a return. It directs new integrations to a different guide. The statuses are for the **Classic** payout flow under [[adyen-classic-platforms]], with provider context at [[adyen]]; a confirmed platform debit is not independent evidence of receiving-bank credit.

## Key takeaways

- The page gives general timing: a regular-speed payout may take **1–2 business days** to confirm success or failure; if successful, funds may take **another 3 business days** to reach the receiving bank (raw lines 19–23). These are guide estimates, not an account-specific arrival guarantee.
- `ACCOUNT_HOLDER_PAYOUT` with `statusCode=Initiated` signals initiation. From **notification version 5**, `content.estimatedArrivalDate` can provide an estimated date. A later `Confirmed` notification means the payout was **debited from the platform account**; Customer Area payout History can show these states (raw lines 25–59). A payout confirmation letter can be downloaded after confirmation only with the stated Customer Area role; it is a confirmation artifact, not bank-receipt proof (raw lines 61–75).
- A receiving bank can return a payout **after Confirmed**, causing another `ACCOUNT_HOLDER_PAYOUT` notification with `status.statusCode=Failed`. The bank may provide a return code/text, but sometimes gives no reason. Customer Area has a **Payout reversed** type; after funds return to Adyen, booking back to the account holder's payable balance may take around **3–6 business days** (raw lines 77–124).
- For a returned **scheduled** payout, Adyen says it blocks further payouts to that bank account. For **manual** payouts, retrying unchanged bank details is likely to return again. The guide first calls for verifying/updating details or discussing a bank rejection with the account holder's bank, then distinguishes manual reissue from scheduled payout-state unblocking (raw lines 126–152, 199–215). A new instruction does not establish a successful retry or bank receipt.

## Detail locators

- Customer Area payout History paths for initiated/confirmed status and payout-letter download, including role gate and support escalation if still Initiated after 2–3 business days: raw lines 31–75.
- Return-reason code examples and notification payload: raw lines 79–114. No bank-supplied reason is guaranteed.
- Manual reissue: Customer Area requires **Instruct payouts to bank accounts for all account holders from the customer area** role, a positive source-account balance, and explicit source account, bank destination and amount; Classic Fund API `POST /payoutAccountHolder` is an alternative (raw lines 148–197).
- Scheduled payout-state unblocking: Customer Area **Unblock payouts** or Classic Account API `POST /updateAccountHolderState` with `disable=false`, `stateType=Payout` (raw lines 199–228). This is a state/action route after correcting the returned payout, not confirmation of a later payment.

## Related

- [[adyen-classic-platforms]] — Classic concept and source route.
- [[adyen]] — provider.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/payouts/track-payouts/2026-09-15|Classic Platforms payout tracking, captured 2026-09-15]]
