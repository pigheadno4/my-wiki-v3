# Fixed retrieval queries — Platforms split chargebacks

## Q1 — Purpose, scope, and what it does not infer

**Question:** What does the split-chargebacks page control, and what does that control not establish?

**Answer:** It documents how a current Adyen for Platforms online-payment integration books an issuer-dispute chargeback amount and associated fees among platform balance accounts. The normal liable-balance debit, possible reversal credit and possible second-chargeback debit are dispute lifecycle events, distinct from the initial payment split, capture or refund. Configured booking does not prove a particular dispute outcome, contractual seller/MOR or ultimate commercial liability, available funds, completed transfer or bank receipt. Canonical route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-online-payments-split-transactions-split-chargebacks]]. Raw: `raw/adyen/docs/platforms/online-payments/split-transactions/split-chargebacks/2026-09-15.md`, lines 15–35 and 37–74.

## Q2 — Central capability, prerequisites, and warnings

**Question:** Which chargeback booking choices, precedence and failure checks does the guide describe?

**Answer:** A platform already processing online payments has no special chargeback-handling prerequisite in this page. Support may configure a balance-platform default; payment-level `platformChargebackLogic` overrides it, and capture-request logic overrides payment-request logic. Behaviors book the disputed amount to the liable account, one `targetAccount`, or the original split ratio; the ratio is relative and can apply when the chargeback amount/currency differs from the sale. Optional `costAllocationAccount` routes fees, otherwise defaulting to liable. Checkout validates split format rather than target existence/status, so a nonexistent or closed-holder target can shift the full transaction and fees to liable despite request success. Listen to `CHARGEBACK` and per-split transfer/transaction webhooks; distinguish received/authorised from chargeback/transaction booked. The examples contain mixed USD/EUR and fee-balance anomalies, so do not infer conversion or general fee arithmetic from them. Raw lines 23–25, 37–74, 767–780, 1475–1503, 2189–2224, 2524–2537, 2839–2852. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-online-payments-split-transactions-split-chargebacks]].
