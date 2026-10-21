---
title: "Adyen transfer route calculation"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/getting-paid/transfer-routes"
raw_files:
  - "adyen/docs/payouts/payout-service/getting-paid/transfer-routes/2026-09-15.md"
tags: [adyen, platforms, payout-service, transfer-routes, bank-payouts]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] guide explains how an **Adyen for Platforms** integration can calculate available bank transfer routes before sending funds to a new recipient. A recipient bank or regulator may limit supported priorities or transfer amounts, so Adyen recommends a route calculation to reduce failures. Despite its Payout Service URL, the page explicitly requires a Platforms integration and its next-step links lead to Platforms custom payouts; do not assume that this prerequisite applies to every Payout Service path. [[adyen-platforms]] [[adyen-payouts]]

## Key takeaways

- The Configuration API credential needs the **Balance Platform BCL role**. The guide uses `POST /transferRoutes/calculate` with `balancePlatform`, `currency`, `category: bank`, and either `country` or a `counterparty` containing a third-party bank account or transfer instrument. `priorities` is optional. For a counterparty by `transferInstrumentId`, `balanceAccountId` is conditionally required. See raw lines 23–48 and 359–372.
- The returned `transferRoutes` identify supported currency and priority plus route-specific requirements; counterparty results also identify country. The illustrative responses show amount, address, account-identification and payment-instrument requirements, but their figures and available routes are examples, not universal limits. See raw lines 301–355 and 716–779.
- This lookup informs route selection; it does not send a transfer, reserve/debit funds, guarantee payout success, or establish bank receipt. Bank/regulatory constraints may still govern the eventual payout. See raw lines 19–21, 301–305 and 716–721.

## Detail locators

- **Country/region request and TEST examples:** raw lines 34–299.
- **Country/region route response example:** raw lines 301–355.
- **Counterparty request and conditional source balance account:** raw lines 359–714.
- **Counterparty route response example and Platforms next steps:** raw lines 716–790.

## Related

- [[adyen-platforms]]
- [[adyen-payouts]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/getting-paid/transfer-routes/2026-09-15|Adyen transfer routes — collected 2026-09-15]]
