# Fixed retrieval checks — Adyen Shopify supported methods

## Q1 — Purpose, scope, and non-inference

**Question:** What does this Shopify method table establish, and what cannot be inferred from a checked row or “International”?

**Expected answer:** It is a captured plugin-supported-method list with a Countries/regions column, described as for the “latest version” but without an exact app/plugin version. A checked row describes listed compatibility, not merchant-account approval, universal country/currency eligibility, shopper availability, or a successful payment. “International” is a literal row label for some card and wallet methods, not a complete eligibility rule. The page does not establish recurring, refund, capture, or order outcomes.

**Raw locators:** Frontmatter line 11; introduction lines 15–19; method tables lines 21–84.

**Canonical wiki route:** [[adyen-index]] → [[adyen-shopify]] → [[source-adyen-docs-plugins-shopify-supported-payment-methods]] (provider-index link to Shopify concept awaits coordinator placement).

## Q2 — Central capability, prerequisites, and warnings

**Question:** How should a merchant use the region table and Trustly note alongside Shopify setup?

**Expected answer:** Read the method-specific Countries/regions row within card, cash/ATM, direct-debit, online-banking, or wallet categories. Examples include Pix for BR, ACH Direct Debit for US, and Apple Pay marked International. Trustly lists DK, FI, NO, SE “and more,” with a Support contact for additional European countries; its “See note [4]” marker does not match the captured note prefix “1 Trustly,” so its list should remain qualified. The separate Shopify installation guide supplies app setup and merchant-account method-request steps; a method request and table row do not prove enablement. The page has no exact plugin version, currency conditions, recurring/refund feature rules, or financial-result proof.

**Raw locators:** Category tables lines 21–84, especially ACH line 49, Pix line 64, Trustly lines 65–67, Apple Pay line 75; unnumbered latest-version statement line 19.

**Canonical wiki route:** [[adyen-index]] → [[adyen-shopify]] → [[source-adyen-docs-plugins-shopify-supported-payment-methods]] → [[raw/adyen/docs/plugins/shopify/supported-payment-methods/2026-09-15|pinned raw snapshot]].
