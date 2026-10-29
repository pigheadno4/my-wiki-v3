# docs-payment-methods-gift-cards retrieval checks

## Q1 — Definition, funding and route

Query: What are gift cards in this Adyen snapshot, and how do provider onboarding, partial payment and funding differ?

Expected: The 2023-modified, 2026-09-15-captured overview defines stored value on virtual/plastic cards, some reloadable and some disposable (raw line 19). Adyen describes online and in-person processing but provider onboarding is prerequisite (line 21). A low-balance gift card may cover part with another method covering the rest; integration-specific steps may apply (lines 23–27). Merchant-only cards are described as funded upfront with provider debit on redemption and no new funds exchange, while multi-business cards yield funds from the provider (lines 29–35). This is not a merchant settlement schedule or evidence of current eligibility. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gift-cards]] → [[raw/adyen/docs/payment-methods/gift-cards/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/gift-cards/2026-09-15.md`, heading `# Gift cards` line 15.

## Q2 — Capability, directory and channel caveats

Query: Which capabilities and brand/provider routes does the gift-card overview list, and what should not be generalized?

Expected: Other stored-value transactions such as balance inquiry/deactivation depend on provider and online/POS channel (raw lines 37–39). One “Loyalty program” matrix row lists Direct, International/Multiple, no recurring/chargebacks/partial captures, yes refunds/partial refunds/separate captures; its refunds note [1] discusses possible regulatory amount limits (lines 41–45), so do not project the row to every card. The page routes to Web, API-only and POS child guides (lines 47–65). It says genericgiftcard can be used for an unlisted card and gives a dated card-country-brand-provider table (lines 67–115); Netscard country wording includes “?” and Savvy is listed with genericgiftcard, so this is not current availability or unique brand proof. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gift-cards]] → [[raw/adyen/docs/payment-methods/gift-cards/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/gift-cards/2026-09-15.md`.
