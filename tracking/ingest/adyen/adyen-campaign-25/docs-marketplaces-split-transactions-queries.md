# C25 Marketplace split-transactions retrieval checks

## Q1 — Where are Marketplace payment, capture, refund and chargeback booking instructions supplied?

Use an applicable split profile or transaction-specific instructions; without either, the whole amount and fees book to the marketplace liable balance account (raw lines 19–21). `/payments` or `/sessions` supplies authorization instructions, `amountUpdates` updates authorized amount, `captures` supplies capture instructions only for methods supporting separate captures, and `refunds` supplies refund instructions (raw lines 23–37). Payment/refund portions use a `splits` array; potential chargeback booking uses `platformChargebackLogic` at authorization or capture (raw lines 69–94). Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-split-transactions]] → [[raw/adyen/docs/marketplaces/split-transactions/2026-09-15]].

## Q2 — What falls to the liable account, and which split fields are conditional?

With no profile or API split instructions, the whole amount and fees go to the liable account; with an individual split lacking `account`, that split amount goes there, but the split type's required fields still apply (raw lines 19–21, 96–118). For `BalanceAccount`, the table requires `account`, `amount` and `reference`; `Commission` requires `amount` and books to liable. Fee/VAT/remainder/surcharge/top-up types have their own requirements (raw lines 104–118). These are intended booking rules, not proof of capture, settlement, payout or bank receipt. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-split-transactions]] → [[raw/adyen/docs/marketplaces/split-transactions/2026-09-15]].
