---
title: "Adyen Received payment details report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/received-payment-details-report"
raw_files:
  - "adyen/docs/reporting/received-payment-details-report/2026-09-15.md"
tags: [adyen, reporting, received-payments, authorisation, transaction-details]
---

## Overview

Adyen's Received payment details report is a transaction-detail report for authorised and refused payments processed through Adyen. It includes shopper interaction, risk score and acquirer response, and can be obtained manually or automatically. This 2026-09-15 snapshot describes a report, not capture, settlement, payout or financial finality.

## Key takeaways

- Each line below the header is a separate entry; the report can contain line items for multiple merchant accounts. It is available for company and merchant accounts and uses the account's reporting time-zone setting. The Creation Date is when the payment was created on Adyen's platform, with a separate Creation Date Time Zone column; it is not a settlement date.
- The standard Amount is the positive **authorisation amount**, including when the payment was cancelled before capture. Currency is a three-character ISO code. Do not use Amount as a captured, settled or paid-out balance.
- The normalized Acquirer Response is **not necessarily the final payment status**; for a payment cancelled before capture it is Unknown, and the raw acquirer response is empty. The report's authorised/refused scope and response fields do not by themselves establish later lifecycle outcomes.
- Standard columns include company/merchant account, PSP and merchant references, payment method, creation date, currency, Amount, risk score, shopper interaction, acquirer response and authorisation code. The schema can contain sensitive shopper/card/bank details: Shopper PAN shows last four card digits for cards but IBAN/BIC for SEPA; other columns include shopper IP, email and billing/delivery data. Check the raw column definitions before handling or exporting these fields.
- Adyen says its report-generation migration may require automated ingestion pipelines to change. Standard-column names/order reflect the post-migration default; additional columns and order are configurable, some reserved columns were removed, and removing Creation Date means sort order is no longer guaranteed. Column configuration in Customer Area requires one of Merchant admin, Merchant report role, Merchant financial or Merchant POS Report role; this role list is for configuration, not proof of any user's access.

## Detail locators

- Opening paragraphs before `## Sample report` — purpose, manual/automatic generation routes, account time zone, company/merchant availability and migration warning.
- `## Report structure` > `### Entries` and `#### Standard columns` — row grain; identifiers; Creation Date/time zone; currency and positive authorisation Amount; shopper, risk and acquirer fields.
- `#### Removed standard columns` and `### Additional columns` — removed reserved columns and configurable original/POS amounts, DCC, metadata, risk, token and POS fields. Additional fields are not assumed present in every report.
- `## Configure report columns` — Customer Area roles and steps, automated-system impact, and Creation Date sorting condition.

## Related

- Company: [[adyen]]
- Reporting concept: [[adyen-reporting]]
- Account hierarchy: [[adyen-account-structure]]

## Raw Sources

- [[raw/adyen/docs/reporting/received-payment-details-report/2026-09-15|2026-09-15 Received payment details report]]
