# Fixed queries — docs-platforms-quickstart-guide-payments

## Q1 — purpose, scope, and non-inference

**Query:** What does this Platforms payments quickstart cover, and what does its flow not establish?

**Answer:** After platform account structure and necessary resources are created, it orients the reader to online and in-person transactions on behalf of third-party users and names merchant account, store, balance platform and user balance account (raw lines 15–29). Its sequence describes method selection, store processing, balance splits, later settlement and payout to a verified transfer instrument (lines 31–38). This is a conceptual route, not evidence of an authorized or captured payment, actual balance booking, settlement, payout, legal seller or merchant-of-record status. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-quickstart-guide-payments]] → [[raw/adyen/docs/platforms/quickstart-guide/payments/2026-09-15|pinned raw]].

## Q2 — central capability, prerequisites, and warnings

**Query:** How does the quickstart distinguish payment-method setup, split instructions and settlement, and what detail belongs to linked guides?

**Answer:** Payment methods are added to user stores during onboarding; the page lists Management API request/get/update settings routes but does not establish method activation or user eligibility (raw lines 40–54). Per-transaction instructions can allocate sale, commission and fees; manual online splits use Checkout API, manual POS splits Terminal API, and store-based automatic profiles Management API. API-request split instructions override profile instructions (lines 56–66). Captured user funds enter independent settlement batches by balance account and sales day; model and delay settings determine batch inclusion and availability (lines 74–78). The page gives no currency list, roles, fee formula, fallback, webhook status, capture mechanics, exact settlement timing or completed payout; consult the linked operational guides for those. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-quickstart-guide-payments]] → [[raw/adyen/docs/platforms/quickstart-guide/payments/2026-09-15|pinned raw]].
