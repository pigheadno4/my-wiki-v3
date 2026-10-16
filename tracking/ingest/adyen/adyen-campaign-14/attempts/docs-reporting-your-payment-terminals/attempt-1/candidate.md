---
title: "Adyen POS terminal fleet Scheduled report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/your-payment-terminals"
raw_files:
  - "adyen/docs/reporting/your-payment-terminals/2026-09-15.md"
tags: [adyen, reporting, point-of-sale, terminal-fleet, inventory]
---

## Overview

This 2022-01-06-last-modified, 2026-09-15-captured field guide describes the **POS Terminal fleet Scheduled report** for terminal inventory and last-seen technical status. It says a terminal receives a report entry upon shipment, and each data row represents one unique terminal. The report can be generated/downloaded manually or automatically, uses the account time-zone setting, and is described as available for company and merchant accounts. See [[adyen-reporting]], [[adyen-terminal-management]] and [[adyen]].

## Key takeaways

- **Fleet grain and identifiers:** The guide offers counts by model/software/country/store and fields such as Unique Terminal Id (Terminal API `POIID`), serial/permanent terminal ID, company/merchant registration, inventory versus in-store state, store code and boarded flag. A shipped terminal's row does not mean it has been assigned, boarded, powered, connected or used for a successful payment.
- **Last-seen status is historical:** The `Status` column says Online today, Last seen 1–7 days ago, or **Switched off** when last online more than a week ago. This is a report-defined last-online category, not a live power-state measurement or diagnosis. `Last Transaction` and `Last Activity` are timestamps omitted when their events were more than 14 days ago; omission does not prove no earlier activity or a failed transaction.
- **Technical inventory, not a transaction log:** Columns include firmware, network MAC/IP/SSID, link negotiation, SIM state and ICCID. A last-transaction timestamp has no payment identity, amount, outcome, authorization, capture or settlement fields on this page. The sample CSV is a data example, not evidence of the merchant's fleet.
- **Account and time boundary:** Availability to company and merchant accounts and use of their time-zone setting do not specify who has report-generation permission or ensure a particular account sees a complete cross-account fleet. Check the applicable account, report run and current device source before operational decisions.

## Detail locators

- Lines 15–33: fleet-report purpose, shipment entry, manual/automatic retrieval, account time zone and company/merchant availability.
- `## Structure`, lines 39–47: one row per unique terminal and column definitions.
- Lines 49–68: identifiers, last-seen `Status`, firmware, company/merchant/store assignment.
- Lines 69–81: 14-day omission rule for transaction/activity timestamps and network/SIM details.

## Related

- [[adyen-reporting]] — report retrieval and account/time-zone routes.
- [[adyen-terminal-management]] — separate live fleet administration and device assignment.
- [[source-adyen-docs-reporting-manually-get-reports]] — report generation/access procedure.
- [[source-adyen-docs-reporting-automatically-get-reports]] — scheduled report retrieval procedure.

## Raw Sources

- [[raw/adyen/docs/reporting/your-payment-terminals/2026-09-15|POS terminal fleet Scheduled report, captured 2026-09-15]]
