# Fixed retrieval queries — Cegid Retail Y2 gift cards

## Q1 — Purpose, scope, and what it does not infer

**Question:** What does the Cegid Retail Y2 gift-card page document, and what cannot be inferred from it?

**Answer:** It is a 2023-modified, 2026-09-15-captured CPOS configuration guide for gift-card operations, keypad buttons, a Cegid gift-card payment method, mapping table and EPT configuration. It is not an activation record, payment authorization, current merchant/provider eligibility statement or package-version assertion. It does not describe partial-tender authorization or balance-shortfall handling. Canonical route: [[index]] → [[adyen-index]] → [[adyen-cegid-retail-y2]] → [[source-adyen-docs-plugins-cegid-retail-y2-giftcards]]. Raw: `raw/adyen/docs/plugins/cegid-retail-y2/giftcards/2026-09-15.md`, lines 5–33 and 63–97.

## Q2 — Central capability, prerequisites, and warnings

**Question:** How are gift-card operations and redemption configured in Cegid, and how do activation, entry mode, and refunds differ?

**Answer:** The guide lists activation with optional initial load, balance check, cash-out, credit note/refund, redemption and reload. Configure register operations and keypad buttons for desired operations except Redemption; then create a Gift card-type Cegid payment method for redemption, put it in the plugin mapping table, and add the EPT Payment Configuration line using the chosen payment code, `GC` marker, entry mode and stored-value provider. Entry modes are `MSE` swipe, `SCA` barcode scan and `MKE` terminal manual entry; without one, cashier chooses per transaction. The source lists `svs`, `givex` and `valuelink` provider values, not universal enablement. A gift-card credit note is described as referenced or unreferenced refund, but this page gives no detailed eligibility limits or partial-tender sequence. Activation prepares a card; redemption is the payment operation, whose actual result must be checked separately. Raw lines 19–32, 34–61 and 63–97. Route: [[index]] → [[adyen-index]] → [[adyen-cegid-retail-y2]] → [[source-adyen-docs-plugins-cegid-retail-y2-giftcards]]; [[adyen-pos-gift-cards]] is a separate generic Terminal API route.
