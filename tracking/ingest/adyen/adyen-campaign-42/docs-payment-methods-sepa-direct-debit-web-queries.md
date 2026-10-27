# Fixed retrieval checks — SEPA Direct Debit Web chooser

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-sepa-direct-debit-web.md`.

## Q1. What is this source's purpose and scope, and what cannot be inferred?

This 2026-09-15 source is a **Web SEPA Direct Debit integration chooser** linking Web Drop-in and Components child guides and four base Sessions/Advanced guides (primary raw `raw/adyen/docs/payment-methods/sepa-direct-debit/web/2026-09-15.md:15-36`; canonical source stem `source-adyen-docs-payment-methods-sepa-direct-debit-web`). It does not give API/Web version requirements, IBAN or billing fields, mandate/permission duties, capture rules, enabled merchant coverage, authorization or settlement evidence. Reviewed child sources `source-adyen-docs-payment-methods-sepa-direct-debit-web-drop-in` and `source-adyen-docs-payment-methods-sepa-direct-debit-web-component`, plus the SEPA overview, carry the actual method details.

## Q2. What are the central routes, prerequisites and warnings?

Choose **Web Drop-in** for the linked all-in-one UI guide or **Web Components** for the linked `SepaDirectDebit` guide (`:19-27`); first build the matching main Web Sessions or Advanced integration from the four base-guide links (`:29-36`). This navigation text alone does not establish a completed SEPA debit, a valid mandate, implementation compatibility or current account eligibility. The matching child and overview must be read before using payment fields or lifecycle claims.
