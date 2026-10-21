# C24 query checks — docs-classic-platforms-reconciliation-use-cases-reconcile-accounts-receivable

## Q1 — Purpose and report route
Q: In Classic Platforms, which report reconciles the net amount settled to platform accounts, and what can it identify?
A: The guide uses the Settlement details report created for a settled batch. It can identify settled transactions, batch net debit/credit and associated fees; the Classic payment flow is through platform merchant accounts to accounts in the platform after Adyen receives funds. See raw/adyen/docs/classic-platforms/reconciliation-use-cases/reconcile-accounts-receivable/2026-09-15.md:19-27. For account-by-account credits/debits, follow the separate transactional-ledger guide (raw/adyen/docs/classic-platforms/reconciliation-use-cases/reconcile-accounts-receivable/2026-09-15.md:54).
Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-reconciliation-use-cases-reconcile-accounts-receivable]] → [[raw/adyen/docs/classic-platforms/reconciliation-use-cases/reconcile-accounts-receivable/2026-09-15]].

## Q2 — Calculation and evidence boundary
Q: What does the sample XASTransfer row represent, and does it prove an actual bank receipt or per-account allocation?
A: It represents the illustrated net amount settled to platform accounts, EUR 390.28, using the source's Net credit minus Net debit formula. The selected underlying rows total 297.60 + 147.00 - 54.00 - 0.32 = 390.28; the XASTransfer debit row records that amount and must not be double-counted in the subtotal. The table is selected illustrative rows, with no actual bank receipt or per-account breakdown; the latter belongs to the linked transactional-ledger guide. See raw/adyen/docs/classic-platforms/reconciliation-use-cases/reconcile-accounts-receivable/2026-09-15.md:29-54.
Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-reconciliation-use-cases-reconcile-accounts-receivable]] → [[raw/adyen/docs/classic-platforms/reconciliation-use-cases/reconcile-accounts-receivable/2026-09-15]].
