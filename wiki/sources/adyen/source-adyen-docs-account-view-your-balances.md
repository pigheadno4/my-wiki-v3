---
title: "Adyen view your balances"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/view-your-balances"
raw_files:
  - "adyen/docs/account/view-your-balances/2026-09-15.md"
tags: [adyen, account-balances, balance-control-api, customer-area, reconciliation]
---

## Overview

This Adyen account guide (last-modified metadata 2026-09-15; captured 2026-09-15) shows how to view merchant-account balances and a company-level sum by currency in Customer Area or with the Balance Control API. It defines displayed components and access requirements; a balance overview is not a bank receipt, a guarantee that every component can be paid out, or a transaction-level reconciliation record. See [[adyen-account-structure]] for the account hierarchy and [[adyen]] for provider context.

## Key takeaways

- Merchant-account balances hold business funds. The company view aggregates balances from its merchant accounts **in the selected currency**; merchant and company views are available in Customer Area or via Balance Control API. The page supports online or POS integrations. Customer Area requires `Merchant financial` or `Manage key financial tasks`; API access requires `Balance control API - Balances management`. Only Customer Area supports the merchant-account activity log. [Raw lines 17–33, 35–37, 60–82]
- `Available funds`/`availableFund` is defined here as pending balance + next payout amount + reserve + applicable negative refund allowance. **Pending** is not yet settled; **next payout/payable** is the amount slated for the next bank payout; **reserve** covers refunds, payouts, chargebacks and other operating expenses; the negative refund allowance, if Adyen permits it, adds refund-covering capacity. These labels therefore do not all mean immediately withdrawable cash or completed bank credit. [Raw lines 41–57, 75–82]
- `Deposit` is separately shown as the amount Adyen withholds to cover potential payment-processing losses and liabilities. It is not identified as the next payout amount or part of the stated available-funds sum. [Raw lines 53–58, 204–208, 255–264]
- Company API view uses `GET /balanceOverview/companies/{companyAccountCode}/balances` and a required three-character `currency` query, returning a `merchantBalancesOverview` array per merchant. Merchant API view separately describes required `merchantAccountCode` and currency, but its printed path uses `/companies/{merchantAccountCode}/balances`, and its example response labels `merchantAccount` as `YOUR_COMPANY_ACCOUNT`. The company USD example also includes EUR/GBP/AUD entries. Treat these as unresolved example/path inconsistencies; verify the live endpoint/schema before implementing. [Raw lines 84–121, 129–196, 227–300]

## Detail locators

- Scope, roles and Customer Area activity-log limit: raw lines 19–33. Company view components and currency selection: raw lines 35–82. Company Balance Control API parameters and illustrative response: raw lines 84–196.
- Merchant Customer Area tabs and activity/deposit views: raw lines 198–225. Merchant Balance Control API path/table and example: raw lines 227–300.
- The guide has no as-of timestamp rule for a displayed amount, bank posting confirmation, payout execution state, or reconciliation proof for a specific payment. Use account payout/reconciliation sources and actual bank evidence for those questions.

## Related

- [[adyen-account-structure]]
- [[adyen]]
- [[source-adyen-docs-account-payments-lifecycle]]

## Raw Sources

- [[raw/adyen/docs/account/view-your-balances/2026-09-15|Adyen view your balances, 2026-09-15 snapshot]]
