# Fixed queries — docs-reporting-invoice-reconciliation

## Q1 — Purpose, scope, and what must not be inferred

**Answer:** This Adyen guide matches transaction costs from a Payment accounting report to the relevant month's Payment processing invoice. It requires both artifacts. The report and invoice are distinct, and this guide is the procedure for comparing fee entries and invoice sections. It does not establish a merchant's actual totals, full reconciliation, accounting sign-off, or final bank receipt. It states no user-role prerequisite; the linked report reference owns report access and generation details.

**Raw locators:** lines 15–24 (purpose and required report/invoice); lines 37–62 (processing-fee comparison); lines 64–90 (acquiring/payment-method fees, discrepancies, and Amount due).

**Canonical route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-invoice-reconciliation]] → [[raw/adyen/docs/reporting/invoice-reconciliation/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Answer:** For a whole month, generate an Interactive payment accounting report from the first day at 00:00:00 to the next month's first day at 00:00:00, in Central European Time, and obtain that month's invoice. The guide identifies four entries for a settled transaction, but processing-fee totals use Received and SentForRefund rows with Processing Fee Currency/Amount. Compare those with the invoice's already-deducted Processing Fees subtotal, checking the final-calculation section and possible extra lines when totals differ. Acquiring/payment-method fees are examined at Settled status via Markup, Scheme Fees and Interchange; line differences may reflect per-transaction versus aggregate rounding. Invoice Amount due equals costs calculated at month-end minus already-deducted amounts and is booked into or out of the next payout as an Invoice deduction entry. Do not conflate these fee subtotals with payment gross/net or treat that future entry as proof of funds arriving.

**Raw locators:** lines 21–24 (artifacts and CET window); 26–35 (four status entries); 37–62 (processing fees and invoice sections); 64–86 (settled-stage fees and rounding); 88–90 (Amount due).

**Canonical route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-invoice-reconciliation]]; field definitions at [[source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report]], raw procedure at [[raw/adyen/docs/reporting/invoice-reconciliation/2026-09-15]].
