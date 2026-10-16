# Fixed retrieval checks — Disputed transactions

Q1. What is this Adyen report for, what is its entry scope, and what must not be inferred?
- Expected: Dispute transaction details help manage disputes. Each line after the header is one entry; the filename date reflects when included disputes were recorded in the account time zone. Original payment PSP reference and dispute PSP reference differ. Do not infer a complete dispute, final outcome, funds movement, current availability or accounting treatment from one report row.
- Raw locators: `raw/adyen/docs/reporting/disputed-transactions/2026-09-15.md:19-39`, `:45-64`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-reporting-disputed-transactions.md` → `[[adyen-reporting]]`.

Q2. Which fields distinguish dispute events from original payments, and what configuration warnings apply?
- Expected: Record Type names dispute events; Record Date, Payment Date, Dispute Date and Dispute End Date have distinct meanings and time-zone columns. Dispute amount/currency can differ from original authorisation amount/payment currency. Scheme reason codes and free-form reason have different roles; auto-defense indication does not prove success, and optional Status means most recent chargeback status. Additional columns depend on account settings; changing columns or order can affect automated consumers and requires one listed merchant role.
- Raw locators: `raw/adyen/docs/reporting/disputed-transactions/2026-09-15.md:47-79`, `:96-129`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-reporting-disputed-transactions.md` → `[[adyen-reporting]]`.
