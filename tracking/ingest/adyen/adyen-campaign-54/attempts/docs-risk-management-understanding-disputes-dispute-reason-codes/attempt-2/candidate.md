---
title: "Adyen dispute reason codes and defense requirements"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/risk-management/understanding-disputes/dispute-reason-codes"
raw_files:
  - "adyen/docs/risk-management/understanding-disputes/dispute-reason-codes/2026-09-15.md"
tags: [adyen, risk-management, disputes, reason-codes, defense]
---

## Overview

This [[adyen]] webpage snapshot catalogs reason codes for **Chargeback**, **Request for Information (RFI)**, and **Notification of Fraud (NoF)** events. Its chargeback tables are separated by scheme or payment method and often by fraud, authorization, processing-error, or consumer-dispute ground. They give a description, a defendable indicator, a response window measured from the Notification of Chargeback (NoC), and a defense-requirements link where applicable. The RFI tables use receipt of the RFI as their stated clock; the NoF tab says its reason codes cannot be defended. Select the event, scheme or method, region, reason code, and applicable note before using a row.

## Key takeaways

- A reason-code string alone is not a universal dispute rule. Codes repeat across schemes and event tabs, and the same scheme can have regional code columns. For example, American Express distinguishes its North-American reason-code column from the column for other countries or regions; Mastercard's 4834 and 4853 rows group multiple scenarios and retain separately labeled legacy codes. Use the specific row's description, defendability, deadline, and linked requirement rather than merging matching numbers or labels.
- Chargeback defense windows and eligibility differ. The snapshot includes defended rows with 7, 10, 13, 14, 15, 18, 25, 30, and 40-day NoC windows, alongside rows marked not defendable. Visa's defended 10.4, 12.x, and 13.x rows state 9 or 18 days from NoC: the 9-day note applies only to disputes opened from 21 July 2025 on payments processed locally in the United States or Canada; earlier such cases and other regions use 18 days in this snapshot. This is dated documentation, not proof of a current case deadline or network rule.
- RFI handling is distinct from chargeback defense. The 2026-09-15 table records Klarna's earlier-phase standard 14-day RFI window, with 7 days for `unauthorized_purchase` and 96 hours for `high_risk_order`. The separately captured [[source-adyen-docs-risk-management-chargeback-guidelines-klarna-chargebacks|Klarna chargebacks guide]] announces a 21-day standard RFI window for most reason codes from 1 November 2026, while those two exceptions remain 7 days and 96 hours. That announcement does not establish the deadline of a live case; select the applicable phase and case notice. Other RFI rows include scheme-specific windows, eftpos's optional second RFI, and Riverty's separate second-RFI appeal windows. UnionPay RFI codes 6300–6302 are marked auto-defended with no merchant action; other UnionPay RFI rows list 30 days. The NoF tab expressly says its codes cannot be defended.
- The shared defense section requires transaction-detail documents and lists permitted formats and size/page limits, with scheme-specific exceptions. It says meeting defense requirements does **not** guarantee a win. Use the linked requirement heading for the dispute ground and the full raw evidence list for merchandise, digital goods, or services as applicable. Do not convert examples of evidence into a universal checklist or treat an upload as an accepted defense.
- ACH return-code rows describe whether and when retry is allowed, separately from card-chargeback defense. BACS and SEPA tables largely mark rows not defendable. The BillDesk 1065 note states a penalty condition after accepting a chargeback; its PDF size cell reads “500 HB” in this snapshot, so verify that typo against the live case guidance before using it. The raw also repeats the heading “Incorrect transaction amount presented” with different evidence lists at lines 1993 and 2000; identify the intended row and location rather than treating those lists as interchangeable.

## Detail locators

- `# Dispute reason codes and defense requirements`, raw lines 15–29 — scope, event tabs, table interpretation, and NoC clock.
- `### Tab: Chargeback`, raw lines 23–912 — complete chargeback and return-code tables: Accel & STAR 31–70; ACH 72–95; Affirm/Afterpay 97–119; American Express 120–186; BillDesk RuPay/UPI 187–267; Cartes Bancaires 269–312; Cash App Pay 314–326; Diners through PULSE 328–773; SEPA 775–805; TWINT/UnionPay 807–855; Visa 856–912. These are row-level locators, not an exhaustive summary.
- `## Mastercard`, raw lines 527–605 — 4834/4853 grouped scenarios, legacy-code labels, and codes flagged as disappearing in the future.
- `## Visa`, raw lines 856–912 — fraud, authorization, processing, and consumer rows; raw lines 868–870, 893–894, and 910–911 contain the dated regional 9/18-day notes and the historical 10.5 note.
- `### Tab: Request for Information`, raw lines 913–1083 — complete scheme/method RFI tables, Klarna's earlier-phase windows at 1018–1029, Riverty first and second windows, eftpos optional second RFI, and UnionPay auto-replied versus merchant-response rows.
- `### Tab: Notification of Fraud`, raw lines 1085–1149 — nondefendable NoF statement and ELO, Mastercard, RatePay, Riverty, and Visa code tables.
- `## Defense requirements`, raw lines 1151–1175 — outcome caveat, document upload, file formats, size and page constraints; `### BillDesk defense requirements`, lines 1216–1221 — its one-document rule and captured size wording.
- `### Addendum dispute` through `### Unrecognizable charge`, raw lines 1176–2427 — reason-specific evidence headings and examples. The duplicate `### Incorrect transaction amount presented` headings are at 1993 and 2000.

## Related

- [[adyen]] — provider page.
- [[adyen-risk-management]] — provider risk and dispute source routes.
- [[disputes]] — general dispute concept.
- [[source-adyen-docs-risk-management-understanding-disputes-dispute-timeframes]] — separate timing overview.
- [[source-adyen-docs-risk-management-understanding-disputes-dispute-process-and-flow]] — dispute-stage flow.
- [[source-adyen-docs-risk-management-chargeback-guidelines-klarna-chargebacks]] — captured Klarna guide with the announced November 2026 RFI phase change.

## Raw Sources

- [[raw/adyen/docs/risk-management/understanding-disputes/dispute-reason-codes/2026-09-15|Adyen dispute reason codes and defense requirements (2026-09-15 snapshot)]]
