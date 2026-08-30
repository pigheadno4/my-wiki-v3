---
title: "Payment Reconciliation & Reporting"
type: concept
category: framework
tags: [reporting, reconciliation, transaction-search, settlement, activity-download, analytics]
---

## Definition

**Payment reconciliation** is the process of matching payment processor records against internal accounting systems to verify that every transaction recorded internally corresponds to actual money movement. **Reporting** is the extraction and presentation of transaction data for business intelligence, compliance, and operational monitoring.

Together they form the backbone of financial operations for any merchant processing payments at scale.

## Why It Matters

- **Accounting accuracy**: ensures books reflect actual cash flow, not just orders placed
- **Fraud detection**: discrepancies between expected and actual settlements surface unauthorized activity
- **Compliance**: regulators and auditors require transaction-level records with timestamps, amounts, and counterparty info
- **Chargebacks and disputes**: evidence for dispute resolution requires accurate transaction records
- **Revenue recognition**: subscription and SaaS businesses need granular event-level data for revenue timing

## Report Types

| Type | Description | Best for |
| --- | --- | --- |
| Transaction Reports | Individual payment event details | Dispute evidence, customer service |
| Settlement Reports | Batch processing summaries affecting balance | Accounting, cash flow |
| Activity Reports | Comprehensive business activity across all event types | General reconciliation |
| Balance Reports | Account balance history | Treasury, cash management |

## Access Methods

### No-code

- **Dashboard Downloads**: manual, on-demand via web UI; CSV/PDF/TAB/IIF/QIF formats
- **Scheduled Reports**: automated delivery via email or SFTP; Transaction Detail Report available by **12:00 PM daily**
- **Basic Analytics**: built-in dashboard charts and summaries

### Pro-code

- **Transaction Search API** (`GET /v1/reporting/transactions`): real-time query; **3-hour latency** before transactions appear; **3-year** history; key params: `start_date`, `end_date`, `transaction_status`, `page_size`
- **Reporting APIs**: automated report generation/retrieval; schedule via `POST /v1/reporting/templates/schedule`; types: DAILY/WEEKLY/MONTHLY
- **Webhooks**: event-driven — trigger reporting on `PAYMENT.CAPTURE.COMPLETED` and similar events

## PayPal Activity Download Report

The primary reconciliation artifact for PayPal merchants. Key specs:

- **87 fields** — positions 1–87, with Mandatory/Selected/Unselected states
- **5 formats**: PDF, CSV, TAB, Quickbooks IIF (US only), Quicken QIF (USD only)
- **Encoding**: UTF-8
- **CSV/TAB max**: 50,000 records per file — larger exports auto-split into ZIP
- **Retention**: 7 years; max 12 months per request
- **Filename**: `Download.<format>`

### Mandatory fields (always included)

Date, Time, TimeZone, Name, Type, Status, Currency, Gross, Fee, Net, From Email, To Email, Transaction ID (17-char unique), Reference Txn ID, Receipt ID (16-digit `xxxx-xxxx-xxxx-xxxx`)

### Key field values

**Status**: Completed, Denied, Reversed, Pending, Active, Expired, Removed, Unverified, Voided, Processing, Created, Canceled; plus invoice-specific values (Draft, Unpaid, Paid, Refunded, etc.)

**Payment Source** (pos 46): PayPal, Venmo, Apple Pay, Google Pay, Network Token, eCheck, Credit Card, Debit Card, PayPal Credit, Pay Later, and APMs

**Card Type** (pos 47): VISA, MASTERCARD, AMEX, DISCOVER, DINERS, JCB, etc.

### T-codes (Transaction Event Codes)

| T-code | Meaning |
| --- | --- |
| T0001 | Mass Payment (successful) |
| T0104 | Mass Payment batch fee |
| T1105 | Account hold released |
| T1114 | Mass Payment reversal |
| T1115 | Mass Payment refund |
| T1503 | Temporary hold on payout amount |

## Reconciliation Best Practices

- **Store transaction IDs** for deduplication — PayPal's 17-char Transaction ID is unique and immutable
- **Use `Reference Txn ID`** to link child transactions (refunds, captures) to parent authorization
- **Check `Balance Impact`** field (Debit/Credit/Memo) to understand balance effect
- **Match T-codes** to understand transaction types in settlement reports
- **Use `RESULTSET_TOO_LARGE` error** as a signal to tighten date ranges — max 31 days per API query
- **3-hour latency** means real-time reconciliation requires webhook-triggered approach, not polling

## Common Errors (Reporting APIs)

| Error | Cause |
| --- | --- |
| `RESULTSET_TOO_LARGE` | Too many results — narrow date range |
| `INVALID_REQUEST` | Malformed parameters |
| `INVALID_RESOURCE_ID` | Resource not found |
| `INTERNAL_SERVICE_ERROR` | Server error — retry |

HTTP 429 → read `Retry-After` header, use exponential backoff.

## Key Players

- [[paypal]] — Activity Download Report, Transaction Search API, Reporting APIs
- [[stripe]] — reporting dashboard + sigma (SQL-based analytics)
- **Adyen** — settlement detail reports, DataTeam reports

## Billing-data reconciliation beyond processor settlement

Metronome documents a billing-data reconciliation pattern that extends beyond matching processor transactions or settlement records to internal accounting data. Data Export supports warehouse-scale comparisons, while list endpoints provide lower-latency access; the worked flow maps Salesforce contract records through custom fields and compares a customer's most recent finalized Metronome invoice with Stripe. This evidence covers cross-system contract terms and invoice records, not proof of payment, settlement, or money movement. The guide does not show the Salesforce-side join, the Stripe matching key, mismatch remediation, export completeness, pagination, or accounting sign-off. [[source-metronome-guides-reporting-insights-financial-reporting-reconcile-data]]

## Sources

- [[source-metronome-guides-reporting-insights-financial-reporting-asc-606-revenue-recognition]] - product-level and period-specific billing data for merchant-owned ASC 606 workflows, external subledger and ERP routing, and accounting, completeness, and sign-off boundaries

- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples]] — illustrative billing-data revenue scenarios, sample-key conflicts, and accounting-authority boundary
- [[source-paypal-reports-analytics]] — Reports & Analytics overview, integration options, SFTP automation
- [[source-paypal-reports-fields-formats]] — Full Activity Download Report field reference (87 fields)
