# Fixed queries — docs-platforms-automatic-split-configuration

## Q1 — purpose, scope, and non-inference

**Query:** What does automatic split configuration do for Adyen for Platforms stores, and what does the configuration not prove?

**Answer:** A platform processing its users' transactions through stores can create a split-configuration profile with conditional rules and link it to a user's store; Adyen describes applying the matching split logic to amounts and fees for the platform liable and user balance accounts (raw lines 15–33, 53–75). This is a configuration and expected-booking guide. It does not show an actual payment, split booking, settlement, payout, account eligibility, legal seller or merchant-of-record assignment. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-automatic-split-configuration]] → [[raw/adyen/docs/platforms/automatic-split-configuration/2026-09-15|pinned raw]].

## Q2 — central capability, prerequisites, and warnings

**Query:** How does a store-linked profile select and apply a rule, and which override, fallback, rounding and capture limits matter?

**Answer:** A profile needs at least one rule; all its conditions must match. When multiple rules match, priority runs currency, payment method or variant, card usage type, card region, funding source and shopper interaction, with more specific rules prevailing within a priority (raw lines 29–37, 77–96). Card usage type and in-person DCC markup allocation are pilot features (lines 49–51, 67–69). An all-ANY catch-all is recommended: unmatched transactions otherwise book to the platform liable balance account; individual payment, capture or refund request instructions override the automatic split (lines 71–75). Adyen rounds automatic splits to the transaction currency's maximum decimal precision using half-to-even logic; variable commission includes tip and surcharge by default unless Support configures another choice (lines 187–224, 226–239). At capture it reevaluates the then-current profile and recalculates for a changed amount; capture-request splits override it (lines 258–262). The example section's scenario 3 mislabels a funding-source comparison as payment-method granularity, so use the explicit hierarchy (lines 138–146). Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-automatic-split-configuration]] → [[raw/adyen/docs/platforms/automatic-split-configuration/2026-09-15|pinned raw]].
