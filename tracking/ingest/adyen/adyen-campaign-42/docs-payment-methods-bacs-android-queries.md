# Fixed retrieval checks — BACS Android chooser

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-bacs-android.md`.

## Q1. What is this source's purpose and scope, and what cannot be inferred?

The 2026-09-15 page is a **BACS Direct Debit Android integration chooser**: it links Drop-in and Components method children and four base Android Sessions/Advanced guides (primary raw `raw/adyen/docs/payment-methods/bacs/android/2026-09-15.md:15-36`; canonical source stem `source-adyen-docs-payment-methods-bacs-android`). It does not define required BACS payment fields, SDK/API versions, Direct Debit Instruction, eligibility, clearing or payment success. Use reviewed child sources `source-adyen-docs-payment-methods-bacs-android-drop-in` and `source-adyen-docs-payment-methods-bacs-android-component`, plus `source-adyen-docs-payment-methods-bacs` for DDI/lifecycle context.

## Q2. What are the central routes, prerequisites and warnings?

The chooser links the **Drop-in** all-in-one UI child and the `BacsDirectDebitComponent` child (`:19-27`), and says the main Android integration should be built first, with separate Sessions/Advanced Drop-in/Components guides (`:29-36`). Its Component blurb says it handles a **redirect** (`:27`), but the linked Component child contains an Advanced `Direct` prose versus `voucher` response-example mismatch; this chooser alone is not a complete action-handling recipe. None of these links proves live BACS enablement or a cleared payment.
