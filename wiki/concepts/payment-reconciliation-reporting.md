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

- [[source-braintree-articles-br-reporting-reconciliation-disbursement-report]] - 2026-09-16 Braintree-hosted Brazil-route Disbursement Report version 1.1 for daily PayPal/Braintree deposit reconciliation, including the Brazil PayPal Account Number funding-account rule, merchant-account and transfer grouping, transaction-versus-settlement currency and report-event time locators, and previous-failed-disbursement carryover; not merchant pricing, current account eligibility or access, independent bank policy, or proof that a deposit arrived
- [[source-braintree-articles-br-reporting-reconciliation-activity-report]] - 2026-09-16 Braintree Brazil Activity Report document-version-1.1 snapshot for previous-processing-day Submitted for Settlement and Settlement Declined records, projected disbursement and fee forecasting, installment adjustments, and distinct presentment/settlement amounts; account-, time-, pricing- and report-event-qualified guidance, not current policy or proof of settlement, disbursement or deposit
- [[source-braintree-articles-br-reporting-reconciliation-statements]] - 2026-09-16 Braintree-hosted Brazil-route monthly merchant-statement snapshot covering permission-gated Control Panel access, statement-period disbursement and fee reconciliation, selected-merchant-account Pricing Schedule rates, date-label differences and transaction/refund/chargeback fee-event qualifications; not sibling regional or processor guidance, current pricing or currency policy, independent bank authority, or proof that funds arrived
- [[source-braintree-articles-br-reporting-reconciliation-transaction-level-fee-report]] - 2026-09-16 Braintree Brazil-route Document Version 1.0 for pricing-dependent transaction-fee detail, installment disbursement/adjustment fee matching and qualified Funds Anticipation fields; the page states no currency or account-program rule, does not override the separate IC+ no-reconciliation limit, and is not payout or bank-arrival proof
- [[source-braintree-articles-br-reporting-reconciliation-reconciliation]] - 2026-09-16 Braintree-hosted Brazil-route reconciliation snapshot covering monthly statement and PayPal-to-bank sweep anchors, debt-repayment-qualified Unified Disbursement Report use, combined PayPal/Braintree disbursement events, and permission- and delay-qualified Disbursement Summary use; no stated pricing or currency scope, sibling-region authority, settlement proof or bank-deposit proof
- [[source-braintree-articles-moneris-statements]] - 2026-09-16 Braintree-hosted Moneris-route monthly statement snapshot covering mailed-statement timing, no-transaction qualification, sales/refund/fee/chargeback and account debit/credit sections, reconciliation use, and an interchange-plus-only fee section; it states no currency and is not independent current Moneris policy, account eligibility or pricing, an API contract, payment or deposit proof, or authority for sibling processor, regional or Marketplace routes
- [[source-braintree-articles-moneris-reconciliation]] - 2026-09-16 Braintree-hosted Moneris-account reconciliation snapshot routing daily Settlement Batch Summary totals to monthly statement activity and account-deposit comparisons, with refund-before-funding and next-month void-fee deposit locators; not evidence for sibling account or processor routes, independent Moneris authority, current currency or pricing policy, or proof of an individual deposit

- [[source-braintree-articles-au-reconciliation]] - 2026-09-16 Braintree-hosted Australia-route reconciliation snapshot covering statement Disbursement Details-to-bank-deposit matching, created-versus-billed fee-event anchors, permission- and delay-qualified Disbursement Summary use and dispute dates; not generic APAC, another account or pricing scope, independent bank authority, or proof of actual fund arrival
- [[source-braintree-articles-au-statements]] - 2026-09-16 Braintree Australia monthly merchant-statement route for permission-gated Control Panel access, statement-period disbursement and fee reconciliation, fee creation-versus-billing timing, account pricing and GST qualifications, and pricing-dependent sections; not current bank, pricing, currency or surcharge-policy authority, proof of deposit, or evidence that sibling regional and processor statement guides are equivalent
- [[source-braintree-articles-apac-statements-reconciliation]] - 2026-09-16 Braintree-hosted APAC statements and daily Transaction Detail Report route covering monthly availability, settlement-currency disbursement details, permission-gated access and fee-qualified reconciliation; captured APAC account/pricing/timing guidance, not Australian transfer authority, current independent bank policy, a bank guarantee, or proof that a deposit arrived

- [[source-braintree-articles-aib-bf-reconciliation]] - 2026-09-16 Braintree-hosted exact AIB BF reconciliation snapshot covering statement Disbursement Details-to-bank-deposit matching, permission- and delay-qualified Disbursement Summary use, dispute disbursement dates and transaction-level fee routes; not AIB AF or LR guidance, current independent bank authority, proof of deposit, or evidence that linked targets agree

- [[source-braintree-articles-aib-af-reconciliation]] - 2026-09-16 Braintree-hosted ordinary AIB AF reconciliation snapshot covering Funding Totals comparison, permission-gated AIB Transaction Fee Report access, processing-date net-settlement matching, discrepancy techniques and Total Fee Amount treatment; distinct from AIB AF LR and AIB BF, not independent current bank policy or proof of deposit arrival

- [[source-braintree-articles-aib-bf-statements-reporting]] - Braintree-hosted AIB BF statements and monthly Transaction Fee Report route covering Control Panel permissions, account-dependent statement sections, VAT exclusion and report reconciliation limits; not AIB AF, independent current bank policy, or proof that linked targets agree

- [[source-braintree-articles-aib-af-reconciliation-lr]] - Braintree-hosted AIB AF `Reconciliation (LR)` route for statement Funding Totals and Transaction Fee Report matching, with net/gross settlement qualifications and failed-disbursement records; not ordinary reconciliation, AIB BF, current independent bank authority, or proof that a deposit arrived

- [[source-braintree-articles-wells-ic-statements-reconciliation]] - captured Braintree Wells IC+ statement and reconciliation route covering fee timing and Disbursement Details matching; not flat-rate, Marketplace, independent bank-policy, or individual-deposit proof
- [[source-braintree-articles-wells-flat-statements-reconciliation]] - Braintree-hosted Wells Flat statement and reconciliation route for disbursement matching, merchant-account fee treatment, report permissions and limitations, and qualified multi-currency-to-USD behavior; Marketplace is separate, and the snapshot is not independent current bank policy or proof of deposit
- [[source-braintree-articles-chase-reporting-reconciliation]] - Braintree-owned Chase-partnership reporting route to Chase Paymentech Online, including report retention and named financial reports for recurring reconciliation; daily deposit amounts are not proof of an individual funded deposit
- [[source-braintree-articles-adyen-reconciliation]] - Braintree-hosted Settlement Details Report route for merchants whose transactions are processed with Adyen, covering permission-gated access, per-MID reports, payout and transaction references, and reserve, fee, invoice and batch-transfer adjustment locators; not independent Adyen authority or proof of an individual bank deposit
- [[source-braintree-payment-methods-paypal-funding-reconciliation]] - PayPal-through-Braintree route distinguishing the PayPal Business Account funding destination and optional Settlement Withdrawal from reconciliation reports, with merchant-size report recommendations and the PayPal Transaction ID to Braintree Authorization Unique Transaction ID crosswalk
- [[source-braintree-control-panel-reporting-decline-analysis]] - Braintree operational reporting route for processor-declined transaction searches and CSV trend analysis by processor response or BIN, with separate verification-search and repeated-attempt skew boundaries; not settlement, reconciliation, or retry-policy evidence
- [[source-braintree-control-panel-reporting-transaction-summary]] - Braintree processing-trend report whose grouped amounts reflect current transaction statuses and which is explicitly unsuitable for reconciliation because statuses can change
- [[source-braintree-control-panel-reporting-1099-k]] - qualified tax-form reporting route whose gross-sales totals exclude credits, refunds and chargebacks, with PayPal excluded to a separate form and aggregated-versus-direct Amex treatment
- [[source-braintree-control-panel-reporting-settlement-batch-summary]] — Braintree Control Panel totals for processor settlement batches, with date/account/payment-type filters and explicit PayPal-disbursement and own-Amex-account deposit reconciliation boundaries
- [[source-braintree-control-panel-reporting-transaction-level-fee-report]] - Braintree flat-rate/blended actual-fee reporting and transaction-level reconciliation use versus IC+ reporting whose interchange amounts are estimates and which is explicitly unsuitable for reconciliation, with three- versus five-calendar-day post-disbursement availability
- [[source-braintree-control-panel-reporting-overview]] - Braintree Control Panel report-category route with account, location and eligibility qualifications; statements may help with reconciliation, while the page establishes neither Dashboard behavior nor reconciliation sufficiency

- [[source-braintree-settlement-batch-summary-generate-node]] - Braintree Node.js reporting route for per-date settlement batch totals of sales and credits, with optional single-custom-field grouping shown in the examples

- [[source-metronome-guides-reporting-insights-financial-reporting-asc-606-revenue-recognition]] - product-level and period-specific billing data for merchant-owned ASC 606 workflows, external subledger and ERP routing, and accounting, completeness, and sign-off boundaries

- [[source-metronome-guides-reporting-insights-financial-reporting-revenue-recognition-examples]] — illustrative billing-data revenue scenarios, sample-key conflicts, and accounting-authority boundary
- [[source-paypal-reports-analytics]] — Reports & Analytics overview, integration options, SFTP automation
- [[source-paypal-reports-fields-formats]] — Full Activity Download Report field reference (87 fields)
