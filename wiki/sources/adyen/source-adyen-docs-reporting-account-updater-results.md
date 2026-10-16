---
title: "Adyen Account Updater results report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/account-updater-results"
raw_files:
  - "adyen/docs/reporting/account-updater-results/2026-09-15.md"
tags: [adyen, reporting, account-updater, card-details, fees]
---

## Overview

This Adyen reporting reference (last-modified metadata 2026-09-15; captured 2026-09-15) defines the **Account Updater results** report for a selected date range. It summarizes submitted requests, responses and pending counts, batch versus realtime service, result categories, and related fees; it does not list a successful later authorization or guarantee that an updated card will support future payments. See [[adyen-reporting]], [[adyen-tokenization]], and [[adyen]].

## Key takeaways

- The report is available daily, weekly, or monthly in CET, at company- or merchant-account scope. Viewing it requires the `Merchant view Account Updater Reports (Adyen)` user role. Adyen links manual and automatic report retrieval and says multiple reports can be generated at once in Customer Area. [Raw lines 17–29]
- The first three report lines are summary metadata: company/merchant account, start and end dates, time zone, and display flags for merchant, acquirer, card scheme, and date grouping. Entries begin after the summary; each later line is a separate **report entry** with grouped counts, not a raw request-by-request card record. [Raw lines 35–61]
- `Service` distinguishes `batch` and `realtime`; optional merchant, acquirer, and scheme columns depend on their display flags, and the scheme values shown are `visa`/`mc`. `Creation date` is submission date grouped as day/week/month, while `Booking date` is when an updater response was received. [Raw lines 63–71]
- `Total requests` counts submissions in the creation-date period; `Responses received` counts responses through report end date; `Responses pending` counts requests with no response by that date. Result-count columns distinguish account number changed, expiry changed, account closed, Visa-only contact cardholder (updated but details unavailable), no change, and technical error. A response category is an Account Updater outcome, not proof of a future payment authorization or settlement. [Raw lines 72–80]
- Fee currency is a three-character ISO code; the report lists per-response fees for changed number, changed expiry, closed account, and contact-cardholder categories, plus a total fee amount to be charged on the monthly Adyen invoice. These are report/accounting figures, not a bank-deposit record. [Raw lines 81–86]

## Detail locators

- Access, reporting interval, CET, and account scope: raw lines 19–29. Summary and entry layout: raw lines 35–61. Full column-level types, conditions, counts and fees: raw lines 63–86.
- The linked sample CSV at raw line 33 is navigation only; its contents were not read for this entry. The report counts have a bounded date range and distinct creation, booking, and end-date meanings.
- This source contains no underlying card number/token detail, per-payment response, future issuer approval, or completed funds movement.

## Related

- [[adyen-reporting]]
- [[adyen-tokenization]]
- [[adyen]]
- [[source-adyen-docs-online-payments-account-updater]]

## Raw Sources

- [[raw/adyen/docs/reporting/account-updater-results/2026-09-15|Adyen Account Updater results, 2026-09-15 snapshot]]
