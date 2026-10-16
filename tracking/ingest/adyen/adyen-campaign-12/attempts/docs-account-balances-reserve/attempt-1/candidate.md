---
title: "Adyen reserve balance"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/balances/reserve"
raw_files:
  - "adyen/docs/account/balances/reserve/2026-09-15.md"
tags: [adyen, reserve, merchant-account, balances, refunds, funding]
---

## Overview

Adyen's reserve is a merchant-account balance intended to cover refunds, chargebacks and other operational expenses. This 2026-09-15 page explains reserve thresholds, funding methods, and merchant-account balance transfers. Its configuration and request procedures do not prove a particular transfer or debit has completed.

## Key takeaways

- For a refund, Adyen says funds first come from pending and next payout balances; if both are insufficient, the amount comes from reserve. If no reserve is set or it too is insufficient, the refund fails. Adyen does **not** automatically retry refunds that failed for insufficient funds; resubmit the failed request when funds are available. The `Modifications not processed` report is the route to these unprocessed refunds.
- A reserve threshold is the desired amount in reserve. On payout-batch close, an increase draws the needed amount from payable; lowering the threshold releases the excess to payable. A threshold edit is not an immediate bank transfer or evidence that a payout happened. Low-reserve Customer Area notifications can be configured as a percentage of the threshold.
- Auto-funding initiates a direct debit from the merchant account's payout bank account when the specified percentage **has been used** (for example, 30% used triggers below 70% of threshold). It seeks to fill reserve to the threshold. The page limits auto-funding to payout bank accounts in EUR, GBP or USD and requires both Merchant financial and Merchant admin roles to request setup; a request does not establish a completed debit.
- A top-up payment adds funds to reserve when Adyen receives it; the page says this can take up to four business days, with EUR/USD funds added within two business days and most other currencies within three. Funds above the reserve threshold return with the next payout. Funding in a currency different from the reserve currency credits payable instead, to offset negative payable amounts in that currency. Check currency-specific bank-transfer instructions where applicable.
- Transfers between merchant accounts require the same company account and legal entity plus at least one common processing currency, which is used for the transfer. Customer Area transfer includes a `Reconfigure reserve if necessary` option for the destination. The Balance Control API request specifies a minor-unit amount/currency, source and destination merchant accounts and `type: credit`; the documented successful response includes a PSP reference and creation time. Adyen says deduction from source pending is immediate after initiation, while destination pending visibility can take up to one hour. Do not infer immediate destination availability from the transfer request alone.
- Customer Area and API permissions differ by operation: reserve management lists Merchant financial, Merchant admin or Manage key financial tasks, while threshold setup/change names Merchant financial; top-up permits Merchant financial or Manage key financial tasks; auto-funding requires both Merchant financial and Merchant admin; Customer Area transfer names Merchant financial; API transfer requires `Balance control API - Balances management`. These are documented role requirements, not proof of actual user or credential access.

## Detail locators

- Opening paragraphs and `## Requirements` — refund balance order, failed-refund resubmission, report route, integration and role prerequisites.
- `## Set up a reserve`, `### Change the reserve threshold`, `## Receive notifications about your reserve` — payout-batch threshold behavior, permissions, notification trigger.
- `### Set up auto-funding` and `### Top up your Adyen account` — percentage-used trigger, payout-bank currency restriction, roles, top-up timing, excess and currency mismatch.
- `### Make a transfer from another merchant account` — legal-entity/company/common-currency conditions; Customer Area option; API request fields, minor units, response and visibility timing. The section links to `/balanceTransfers` and shows a plural-path curl example, but its numbered step says POST `/balanceTransfer`; consult the linked API reference before implementing the endpoint.

## Related

- Company: [[adyen]]
- Merchant-account hierarchy: [[adyen-account-structure]]

## Raw Sources

- [[raw/adyen/docs/account/balances/reserve/2026-09-15|2026-09-15 Adyen reserve guide]]
