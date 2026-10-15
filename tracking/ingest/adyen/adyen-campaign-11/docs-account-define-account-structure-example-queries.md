# Fixed retrieval checks: example Adyen account structures

## Q1 — Online, POS and US legal-entity example

**Query:** In Adyen's Dutch tea-merchant example, how are the initial online and POS accounts arranged, and what changes when the business adds a US legal entity?

**Expected answer:** The hypothetical Netherlands legal entity sells tea online across the EU and runs an Amsterdam store. The illustration starts with company account `TeaShop` and online merchant account `TeaShop_ECOM`, then adds `TeaShop_POS` for in-person processing. It describes separate reports and payouts for the two merchant accounts and a company-level invoice. When the merchant launches a US legal entity to use local acquiring, it adds `TeaShop_US_ECOM`; that account has separate reporting, payout and invoice from the Netherlands company-level invoice. The described local-acquiring benefit is an example rationale, not a guaranteed fee or authorization improvement. This dated scenario does not determine another merchant's required structure or legal seller.

**Raw locators:** hypothetical merchant and smallest setup, lines 23–39; US expansion and invoicing, lines 41–50. **Canonical retrieval route:** [[adyen-account-structure]] → [[source-adyen-docs-account-define-account-structure-example]] → [[raw/adyen/docs/account/define-account-structure/example/2026-09-15|pinned raw]].

## Q2 — Regional accounts, legal-entity link and EU grouping

**Query:** When the example adds Germany and Netherlands merchant accounts, do they move to new legal entities or merge payouts through an EU account group?

**Expected answer:** The scenario adds `TeaShop_DE_ECOM` and `TeaShop_NL_ECOM` to separate funds, reports and user permissions. Both are linked to the Netherlands legal entity, and their invoice stays with the company-level Netherlands invoice. The older `TeaShop_ECOM` remains for other EU business. The optional `Account group EU` includes those two accounts, `TeaShop_ECOM` and `TeaShop_POS` to share user access and cross-account payment search. The page does not say that grouping merges payouts or invoices, and it gives no transaction migration or reassignment procedure. Account names and sales geographies alone do not establish merchant-of-record identity or full funds flow.

**Raw locators:** regional split and legal-entity/invoice treatment, lines 52–62; account-group access and search, lines 64–72. **Canonical retrieval route:** [[adyen-account-structure]] → [[source-adyen-docs-account-define-account-structure-example]] → [[raw/adyen/docs/account/define-account-structure/example/2026-09-15|pinned raw]].
