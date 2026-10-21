# docs-marketplaces — attempt 1 retrieval checks

## Q1. What is this Marketplace integration model, and what are its primary prerequisites and flows?

It is an **Adyen for Platforms** route for a marketplace whose brand is known to users and customers and that processes **online payments only** (raw lines 19–29). The page routes to onboarding and Adyen verification before payout, payments on behalf of users with possible splits/cost deductions, managed or custom payouts, risk controls and reconciliation (raw lines 31–41). Linked API Explorer calls are examples (raw lines 33–35); detailed prerequisites live in the linked guides. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces]] → [[raw/adyen/docs/marketplaces/2026-09-15]].

## Q2. Does the country list or financial-products section establish Marketplace POS support, live eligibility or completed financial outcomes?

No. The model says online payments only (raw line 27). Its dated supported-country list has an in-person/store footnote for Channel Islands and Isle of Man (raw lines 43–99), but that does not grant Marketplace POS scope; acquiring regions are listed separately (raw lines 101–114). Issuing, business accounts and Capital are optional and point to availability/additional-verification requirements (raw lines 116–143). These overview claims and API examples do not show a user's verification approval, a successful payment or split, a product grant, payout execution or bank receipt. Forward route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces]] → [[raw/adyen/docs/marketplaces/2026-09-15]].
