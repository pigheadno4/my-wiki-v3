---
title: "PayPal Activity Download Report — Fields & Formats Reference"
type: source
date_ingested: 2026-04-18
original_format: webpage
raw_files:
  - "paypal-reports-fields-formats-2025.md"
tags: [paypal, reporting, activity-download, transaction-fields, csv, reconciliation]
---

## Summary

Complete field reference for the PayPal Activity Download Report — 87 fields with positions, data types, char limits, and mandatory/selected/unselected states. Covers all output formats, retention rules, and key field values.

## Key Takeaways

- **5 output formats**: PDF, CSV, TAB, Quickbooks IIF (US only), Quicken QIF (USD only)
- **CSV/TAB max**: 50,000 records per file — larger reports auto-split into ZIP
- **Encoding**: UTF-8
- **Retention**: 7 years history; max 12 months per report request
- **87 fields** total; fields are Mandatory / Selected (default on) / Unselected (default off)
- **Transaction ID** (pos 13): unique 17-character encrypted ID, max 24 chars
- **Receipt ID** (pos 35): 16-digit `xxxx-xxxx-xxxx-xxxx` format

## Output Formats

| Format | Extension | Notes |
| --- | --- | --- |
| PDF | `.PDF` | Limited fields (only "In PDF: Yes" columns) |
| CSV | `.CSV` | Max 50k rows; ZIP if larger |
| TAB | `.TAB` | Max 50k rows; ZIP if larger |
| Quickbooks | `.IFF` | US accounts only |
| Quicken | `.QIF` | USD only |

Filename convention: `Download.<format>`

## Mandatory Fields (Always Included)

| Pos | Field | Type | Max chars | In PDF |
| --- | --- | --- | --- | --- |
| 1 | Date | Date | 10 | Yes |
| 2 | Time | Time | 8 | No |
| 3 | TimeZone | Alphanumeric | 32 | No |
| 4 | Name | Alphanumeric | 200 | No |
| 5 | Type | Alphanumeric | 100 | Yes |
| 6 | Status | Alphanumeric | 127 | Yes |
| 7 | Currency | 3-char code | 3 | Yes |
| 8 | Gross | Currency/Money | 25 | Yes |
| 9 | Fee | Currency/Money | 25 | Yes |
| 10 | Net | Currency/Money | 25 | Yes |
| 11 | From Email Address | Alphanumeric | 127 | No |
| 12 | To Email Address | Alphanumeric | 127 | No |
| 13 | Transaction ID | Varchar | 24 | No |
| 31 | Reference Txn ID | Varchar | 24 | No |
| 35 | Receipt ID | Alphanumeric | 19 | No |

## Status Field Values

**General activity** (12 values): Completed, Denied, Reversed, Pending, Active, Expired, Removed, Unverified, Voided, Processing, Created, Canceled

**Invoice-specific additions** (12 values): Error, Draft, Unpaid, Paid, Unpaid (sent), Marked as paid, Marked as refunded, Refunded, Partially refunded, Scheduled, Partially paid, Payment pending

## Key Unselected Fields (Not Default — Must Opt In)

| Pos | Field | Notes |
| --- | --- | --- |
| 14 | CounterParty Status | Verified / Unverified / Unregistered |
| 26 | Auction Site | eBay, Yahoo! Auctions, Amazon, etc. |
| 46 | Payment Source | PayPal, Venmo, Apple Pay, Google Pay, Network Token, eCheck, Credit Card, Debit Card, PayPal Credit, Pay Later, 20+ values |
| 47 | Card Type | VISA, MASTERCARD, AMEX, DISCOVER, DINERS, JCB, etc. |
| 48 | Transaction Event Code | T-Code number (5 chars) |
| 56 | Authorization Review Status | 01=Green, 02=Yellow |
| 57 | Protection Eligibility | 01=eligible, 02=not eligible, 03=partially eligible |
| 60 | Buyer Wallet | Company processing the payment |
| 71 | Tax ID Type | CPF/CNPJ — Brazil only |
| 85 | Payment Source Subtype | Card brand detail (e.g. `Credit Card-VISA`); also Pay in 3/4, Installments |
| 87 | Fastlane Checkout Transaction | Was Fastlane used? |

## Transaction Event Codes (sample)

- **T0006**: Payment received
- **T0007**: Payment sent
- **T0111**: Refund issued
- **T0200**: Chargeback initiated

Full T-code list: [Transaction Detail Report Specification](https://developer.paypal.com/docs/reports/reference/tcodes/)

## API Status Code Mapping

| API code | Report Status value |
| --- | --- |
| S | Success / Completed |
| P | Pending |
| F | Failed |
| C | Cancelled |
| R | Refunded |

## Related Pages

- [[paypal]] — company page
- [[source-paypal-reports-analytics]] — Reports & Analytics overview

## Raw Sources

- [[paypal-reports-fields-formats-2025]] — full 1329-line Activity Download Report field reference: 87 fields, all data types, char limits, mandatory/selected/unselected states, status values, payment source values, card types
