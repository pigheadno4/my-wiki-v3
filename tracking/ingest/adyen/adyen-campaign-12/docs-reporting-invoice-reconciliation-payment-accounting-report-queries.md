# Fixed retrieval checks — Payment accounting report

Q1. What is the purpose and scope of Adyen's Payment accounting report, and what must not be inferred?
- Expected: Payment-lifecycle status changes, events and modifications with cost by status for invoice reconciliation; each row is an accounting entry, not a complete payment. The captured documentation says company and merchant accounts. Do not infer current availability, completed settlement, bank arrival, financial finality or accounting advice from the report.
- Raw locators: `raw/adyen/docs/reporting/invoice-reconciliation/payment-accounting-report/2026-09-15.md:17-27`, `:54-58`, `:196-253`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report.md` → `[[adyen-reporting]]`.

Q2. What are the central capability, prerequisites and material warnings for using this report to reconcile an invoice?
- Expected: Separate payment, settlement and processing-fee currency/register columns and record types support fee-to-status matching. Interactive report generation lets users choose date range, time zone and columns; Adyen instructs first-of-month to first-of-next-month at midnight CET for payment-processing-invoice reconciliation. Standard report uses the account time zone. Interactive and ordinary columns differ. February 2025 filename change and column configuration can affect automated ingestion; column configuration requires a listed Customer Area role. Preserve pending, failed, reversed and externally settled record-type distinctions.
- Raw locators: `raw/adyen/docs/reporting/invoice-reconciliation/payment-accounting-report/2026-09-15.md:21-46`, `:62-89`, `:175-194`, `:196-253`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report.md` → `[[adyen-reporting]]`.

Counterpart qualification: the Brazil installment guide alternates Installment/Installments and Advanced (PC)/Advancement (PC); this report schema names Installments (raw line 141) and Advanced (PC) (raw line 136). Preserve the mismatch, without assuming aliases or extra columns; follow the source contradiction route to the installment guide.
