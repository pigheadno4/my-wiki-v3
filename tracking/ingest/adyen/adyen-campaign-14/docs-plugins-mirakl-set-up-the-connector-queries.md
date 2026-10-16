# Fixed retrieval checks — docs-plugins-mirakl-set-up-the-connector

## Q1 — Purpose, scope, and what not to infer

**Query:** What does the Mirakl connector setup page configure, and what does it not establish?

**Answer:** It sets out Mirakl Operator API access-token creation, seller-shop custom-field and feature setup, connector/Mirakl/Adyen onboarding settings and test/live sync scheduling for Adyen for Platforms. It does not define an OAuth app secret, establish seller KYC completion, live eligibility, merchant-of-record identity, a completed split payment, payout or bank receipt. The page was last modified and captured 2026-09-15. Evidence: raw lines 11, 15–17, 19–136. Canonical route: [[adyen-index]] → [[adyen-mirakl]] → ## Sources → [[source-adyen-docs-plugins-mirakl-set-up-the-connector]] → [[raw/adyen/docs/plugins/mirakl/set-up-the-connector/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** Which tokens, fields, feature switches, credentials and synchronization conditions does this Mirakl setup require?

**Answer:** Create and securely retain a Mirakl **Operator API** access token. Add the specified marketplace-model seller fields without marking them required; their Adyen account/balance/legal-entity/transfer IDs and HOP URL support seller sync/KYC, with VAT and channel fields conditional. Ask Mirakl Support to enable **KYC status** and **Payment confirmation**; the latter lets the connector distinguish Pending payment and Paid invoice labels, not bank-settled funds. Give Adyen connector settings and Mirakl URL/token, the liable balance account (sufficient funds matter for negative commissions), a Configuration/Transfers Balance Platform credential with **Balance Platform BCL** role, and separate Scope/LEM credential. Optional defaults include payment block enabled, subscription payout separation disabled, and new-shop unsuspension enabled after KYC success. Partial/Full sync update shops; Start Invoice Sync schedules payouts and needs a start date confirmed for test and live to avoid older invoices. A maximum failed-invoice-payout retry setting is a count, not proof a retry succeeds. Evidence: raw lines 19–58, 60–65, 91–136. Canonical route: [[adyen-index]] → [[adyen-mirakl]] → ## Sources → [[source-adyen-docs-plugins-mirakl-set-up-the-connector]] → [[raw/adyen/docs/plugins/mirakl/set-up-the-connector/2026-09-15]].
