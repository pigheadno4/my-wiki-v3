---
title: "Adyen Fund API v6: Pay out from an account to its holder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Fund/latest/post/payoutAccountHolder"
raw_files:
  - "adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15.md"
tags: [adyen, classic-platforms, fund-api, payouts, account-holders]
---

## Overview

This 2026-09-15-captured Classic Fund API v6 reference describes `POST /payoutAccountHolder` at the listed **test** server (`https://cal-test.adyen.com/cal/services/Fund/v6`): a payout from a Classic `accountCode` to its owning `accountHolderCode`. The opening description names a bank-account destination; the request table also exposes a holder-owned `payoutMethodCode` for a stored payout method. The separate Classic card-payout guide describes the eligible-card path. Keep these Classic IDs separate from newer balance-platform transfer resources. [[adyen-classic-platforms]] [[adyen]]

## Key takeaways

- The request table marks `accountCode` and owning `accountHolderCode` required. `amount` is **not marked required** as a top-level property, although its nested `currency` and minor-unit `value` are marked required when the amount object is used; the endpoint's purpose describes a specified amount, so do not infer an amount-free payout contract from the table. For a multi-currency account, the table says to specify the currency. See [[raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15|raw lines 14–21]].
- Optional `bankAccountUUID` selects a bank account held by that holder; if blank, a bank account is automatically selected. Optional `payoutMethodCode` selects a holder-owned payout method; if blank, a payout instrument is automatically selected. The `amount` note says a supplied bank UUID uses the bank-supported currency and a supplied payout method code selects that method. The page does not define precedence when **both** destination identifiers are supplied. See [[raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15|raw lines 19–26]].
- `payoutSpeed` lists `STANDARD` and `SAME_DAY`, but this table alone does not establish same-day eligibility. Optional `merchantReference` links transactions. `description` is limited to 200 characters and a stated character set; the one-off example uses an en dash in `12345 – Test`, outside that stated set, so use the field rule rather than treating the example as validation proof. See [[raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15|raw lines 23–42]].
- HTTP 200 is labeled succeeded, while HTTP 202 is accepted for processing **but incomplete**. Both response schemas list optional `bankAccountUUID`, `merchantReference`, `payoutSpeed`, request-identifying `pspReference`, `resultCode` and validation `invalidFields`. A response reference or destination field does not prove bank/card receipt. The Classic manual-payout guide explicitly says to wait for `ACCOUNT_HOLDER_PAYOUT` for payout status; the status guide distinguishes `Initiated`, `Confirmed` and `Failed`, and says a bank can return funds after `Confirmed`. See [[raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15|raw lines 43–82]], [[source-adyen-docs-classic-platforms-payouts-manual-payout|manual payout guide]], and [[source-adyen-docs-classic-platforms-payouts-payout-notifications|payout notifications]].
- Errors list 400 unreadable request, 401 authentication, 403 insufficient permissions, 422 validation and 500 server failure. See [[raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15|raw lines 85–147]]. This page does not establish a specific role, successful account eligibility, available balance, live payout or current rail availability.

## Detail locators

- Request fields, conditional nested amount properties and bank-versus-payout-method selection: [[raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15|raw lines 14–26]].
- One-off bank example and 200/202 response schemas: [[raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15|raw lines 28–82]].
- Error response schemas: [[raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15|raw lines 85–147]].

## Related

- [[adyen-classic-platforms]] — Classic holder/account context.
- [[source-adyen-docs-classic-platforms-payouts-manual-payout-payout-to-cards]] — eligible stored-card route and its separate enablement/PCI gates.
- [[source-adyen-docs-classic-platforms-payouts-payout-notifications]] — outcome and possible return tracking.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/Fund/latest/post/payoutAccountHolder/2026-09-15|Payout account holder API reference (captured 2026-09-15)]]
