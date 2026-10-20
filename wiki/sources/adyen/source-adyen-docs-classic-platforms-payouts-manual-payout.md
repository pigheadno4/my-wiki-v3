---
title: "Adyen Classic Platforms: manual payouts"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/payouts/manual-payout"
raw_files:
  - "adyen/docs/classic-platforms/payouts/manual-payout/2026-09-15.md"
tags: [adyen, classic-platforms, payouts, fund-api]
---

## Overview

This 2020-modified Classic Adyen for Platforms guide, captured 2026-09-15, describes initiating off-schedule, including partial, payouts from a sub-merchant **account's positive balance less any negative pending balance** to a bank account, or through the Fund API to a payout-eligible card. It directs new implementations to a newer integration guide. The Classic account-holder/account and Fund API model is distinct from the current Platforms balance-account payout model. A payout request or initial response does not establish a confirmed payout or beneficiary receipt. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Customer Area can initiate a bank-account payout when the user has the **Instruct payouts to bank accounts for all account holders from the customer area** role and the selected account has a positive balance. The operator selects source account, destination bank account and amount; an optional description/merchant reference is for statement text/reconciliation. A dimmed **Payout to bank** action signals no positive account balance.
- The Classic Fund API route is `POST /payoutAccountHolder` for an account holder's bank account or eligible payout card; the bank example supplies `accountCode`, `accountHolderCode`, `amount` and `bankAccountUUID`. The sample success response contains `pspReference`, while a validation-error example also contains `pspReference` and `resultCode: Failed`. Therefore a reference alone does not prove success. Wait for `ACCOUNT_HOLDER_PAYOUT` notification to confirm payout status, and use Customer Area tracking for further status.
- Bank-method and regional cutoffs affect expected receipt time. The page lists faster payout support in **Australia, United Kingdom and United States**, subject to method availability and bank cutoff; platform-wide enablement goes through Support, or a specific Fund API request can include `payoutSpeed: SAME_DAY`. Same-day availability is conditional, not proof of bank credit.
- The `description` payout descriptor is stated to allow 1–35 characters from the specified letters, digits and punctuation. The sample bank payout description contains a dash/en dash (`12345 – Test`) absent from that allowed-character list. Treat the example as illustrative and follow the explicit character rule rather than assuming the sample is accepted.

## Detail locators

- Raw lines 19–27 define Classic scope, source-balance constraint, cutoff caveat and payout channels.
- Raw lines 29–52 give the Customer Area role, positive-balance condition and bank payout steps.
- Raw lines 54–105 give Fund API bank/card route, sample request, success and validation-error responses, and asynchronous payout-status notification.
- Raw lines 107–135 give regional faster-payout support, enablement and `SAME_DAY` option.
- Raw lines 138–144 give descriptor length and character set; compare the example description at line 71.

## Related

- [[adyen-classic-platforms]] — Classic account and payout model.
- [[adyen]] — provider context.
- [[adyen-platforms]] — separate current Platforms model.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/payouts/manual-payout/2026-09-15|Adyen Classic Platforms manual-payout guide, captured 2026-09-15]]
