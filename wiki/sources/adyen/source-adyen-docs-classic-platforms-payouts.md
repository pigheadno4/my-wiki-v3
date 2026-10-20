---
title: "Adyen Classic Platforms: Payouts"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/payouts"
raw_files:
  - "adyen/docs/classic-platforms/payouts/2026-09-15.md"
tags: [adyen, classic-platforms, payouts, bank-accounts, cards]
---

## Overview

This 2023-modified, 2026-09-15-captured **Classic Adyen for Platforms** overview compares scheduled and manual payouts from an account holder's funded Classic account. Payout timing and amount are controlled by the platform but remain subject to the account holder's **current payout tier**, verification and a **positive account balance**. It directs new implementations to a separate new-integration guide.

## Key takeaways

- **Scheduled payouts** have a cadence per individual account, send the **full available balance**, and are limited here to **bank-account destinations**. **Manual payouts** can be triggered for a specified partial amount to a bank account or an **eligible card**. The guide recommends scheduled payouts for timing and mentions separate premium faster options for both routes. See raw lines 21–29.
- The page states that the payout method's country must normally match the account holder's country, with more flexible bank-account placement across European countries. It limits an account holder to **200 bank accounts**. Its dated currency rule says local currencies only, except EUR in SEPA countries outside the eurozone and USD in Canada. See raw lines 31–44; the country/currency table is at raw lines 46–80.
- Default processing depends on regional rails (the page gives UK BACS and US ACH examples). These are route descriptions, not evidence of a payout's final status or bank receipt. For verification and notification outcomes, follow the linked detail guides. See raw lines 21, 28–29 and 82–86.

## Source table discrepancy

The prose explicitly gives **USD in the United States** as a supported local-currency example (raw line 39), but the supported-currency table shown in this capture has **no United States row** (raw lines 46–80). The snapshot does not explain the omission; do not infer unsupported US payout from the missing row or use this dated table as a current availability decision.

## Detail locators

- Classic scope, payout-tier gate and scheduled-versus-manual destinations/amounts: [[raw/adyen/docs/classic-platforms/payouts/2026-09-15|raw lines 15–29]].
- Country/bank-account and currency limits, including the missing-US table row: [[raw/adyen/docs/classic-platforms/payouts/2026-09-15|raw lines 31–80]].

## Related

- [[adyen-classic-platforms]] — Classic platform account and payout context.
- [[adyen]] — provider context.
- [[source-adyen-docs-classic-platforms-payouts-track-payouts]] — detailed payout-status tracking route.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/payouts/2026-09-15|Payouts (captured 2026-09-15)]]
