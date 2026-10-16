---
title: "Donation campaigns | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/donation-campaigns"
raw_files:
  - "adyen/docs/reporting/donation-campaigns/2026-09-15.md"
tags: [adyen, reporting, giving, donation-campaigns, reconciliation]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot describes Adyen Giving campaign insights and two distinct donation reports. Merchants use a campaign dashboard and the individual-donation Processed Donations Report; nonprofits can generate a grouped Received Donations Report. The page specifies Customer Area roles, report availability, columns, currencies and timing, but its descriptions do not establish bank receipt or an independently verified final outcome for a particular donation. [[adyen-reporting]] [[adyen-giving]]

## Key takeaways

- Donation campaigns must be set up first. Donation Campaigns Viewer can view campaigns, insights and Processed reports; Donation Campaigns Manager can also manage campaigns; Merchant financial can generate Received reports. This guide says these roles give no access to other payment information, but the separate [[source-adyen-docs-account-user-roles|User roles reference]] lists broader Merchant financial access to payouts, invoices, balances, payment analytics and reports. Do not treat Merchant financial as donation-only; verify actual grants before assignment. The User roles reference separately describes the Donation campaigns viewer and manager roles as not giving access to payment information.
- Each active or past campaign has an insights dashboard for online and in-store performance, including shopper location. It can lag a donation by up to four hours; the page recommends the merchant `DONATION` webhook for real-time information. Filters include date range, processing currency, merchant account, location and channel.
- The company-account-only Processed Donations Report is one row per donation described as settled to the nonprofit, with no aggregation. Standard fields include campaign and nonprofit identifiers, donation PSP reference, creation date in AMS/CET time, channel, settlement type, processing currency and amount. Configurable commercial-transaction PSP reference identifies the original payment that triggered the donation and is distinct from the donation PSP reference; optional merchant-time fields need the merchant account time zone.
- The nonprofit-only, company-account-only Received Donations Report aggregates donations paid out to the nonprofit by attributes. Its rows include count, original-donation gross currency/credit/debit, exchange rate and settlement-currency net credit/debit. Do not treat gross and net currency or amount as interchangeable, or interpret a grouped row as one donation.
- Both reports support manual or automatic retrieval in CSV/XLS/XLSX, use the account time-zone setting and a selected date range. Changing configured columns or their order can affect automated ingestion; configuration requires one of the listed Merchant admin, Merchant report role, Merchant financial or Merchant POS Report role permissions.

## Detail locators

- **Purpose, prerequisite and Customer Area roles:** raw lines 23–39. Cross-source role conflict: [[source-adyen-docs-account-user-roles]], raw/adyen/docs/account/user-roles/2026-09-15.md:67–92.
- **Campaign dashboard latency and filters:** raw lines 41–58.
- **Processed report availability, single-donation grain and standard/configurable fields:** raw lines 60–123.
- **Received report nonprofit scope, grouped grain and gross/net columns:** raw lines 125–172.
- **Report-column configuration and automation impact:** raw lines 174–193.

## Related

- [[adyen]]
- [[adyen-reporting]]
- [[adyen-giving]]
- [[source-adyen-docs-account-user-roles]] — separate role-permission authority for the Merchant financial access conflict

## Raw Sources

- [[raw/adyen/docs/reporting/donation-campaigns/2026-09-15|Adyen Donation campaigns — collected 2026-09-15]]
