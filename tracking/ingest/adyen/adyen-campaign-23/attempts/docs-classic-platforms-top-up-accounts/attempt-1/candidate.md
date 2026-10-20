---
title: "Adyen Classic Platforms: Top up accounts by direct debit"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/top-up-accounts"
raw_files:
  - "adyen/docs/classic-platforms/top-up-accounts/2026-09-15.md"
tags: [adyen, classic-platforms, direct-debit, top-ups, account-holders]
---

## Overview

This 2023-modified, 2026-09-15-captured **Classic Adyen for Platforms** guide describes pulling funds from an account holder's bank account by direct debit to top up platform accounts, for example to cover a negative balance or costs. The documented funds path is **account holder bank debit → Adyen merchant-account settlement → credits to accounts according to split instructions**. It directs new implementations to the separate new-integration guide; its Classic Fund API/account model must not be conflated with modern balance-platform top-ups.

## Key takeaways

- The page lists account-holder bank accounts in the **EU, UK and US**, using SEPA, BACS and ACH respectively, as its dated support scope. The platform must have direct debits enabled through Support and obtain the account holder's agreement. For ACH, business and non-profit holders must arrange for their bank to allow specified Adyen originator IDs or the debit may be blocked. See raw lines 19–37.
- A Classic Fund API `POST /debitAccountHolder` request identifies the holder with `accountHolderCode`, debits the account-holder bank instrument identified by `bankAccountUUID`, names the platform `merchantAccount`, and supplies one or more `splits` to receiving platform accounts. The guide gives **EUR 500 per transaction** as the maximum when debiting EU bank accounts. Its example uses a **v6 test** endpoint and illustrates USD 62 split USD 60 to an account-holder account and USD 2 to the platform liable account. See raw lines 39–99.
- The API response `resultCode: Received` only acknowledges the request. The direct debit is asynchronous: inspect `DIRECT_DEBIT_INITIATED` notification `status.statusCode` for `Initiated` or `Failed`. `Initiated` is not settlement; rails have their own timing and settled transactions appear in reports. `Failed` can arrive up to three business days later, with causes including validation, limits, bank-blocked originator IDs, missing funds receipt and insufficient bank funds. See raw lines 101–117.
- The guide says successful debits settle to the Adyen merchant account and appear as `MerchantPayin` in Settlement details. Credits made under the split instructions appear in the Marketplace Payments accounting report, where the request `description` can be matched to `Payment Merchant Reference`. See raw lines 207–211.

## Example discrepancy

The illustrative request and response are **USD 62**, split **USD 60 + USD 2** (raw lines 52–98). Its `Initiated` notification keeps the total at **USD 62** but labels the split amounts **EUR 60 + EUR 2** (raw lines 127–151). The capture does not explain any FX conversion; do not use this specimen as a coherent currency or reconciliation example.

## Detail locators

- Scope, consent, ACH allowlist and direct-debit request fields/limit: [[raw/adyen/docs/classic-platforms/top-up-accounts/2026-09-15|raw lines 19–52]].
- Test request/response, asynchronous statuses and failure reasons: [[raw/adyen/docs/classic-platforms/top-up-accounts/2026-09-15|raw lines 54–117]].
- Notification examples and merchant-account/split-account report routes: [[raw/adyen/docs/classic-platforms/top-up-accounts/2026-09-15|raw lines 119–211]].

## Related

- [[adyen-classic-platforms]] — Classic platform account and payment model.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/top-up-accounts/2026-09-15|Top up funds in accounts (captured 2026-09-15)]]
