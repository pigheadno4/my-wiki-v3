# Online banking Slovakia Flutter Drop-in retrieval checks

## Q1 — Purpose and proof boundary

Query: What does the Online banking Slovakia Flutter Drop-in guide cover, and can it prove a complete integration or successful/live bank payment?

Expected route: `wiki/index.md` line 10 → `wiki/adyen-index.md` line 2716 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia-flutter-drop-in.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/online-banking-slovakia/flutter-drop-in/2026-09-15.md` `# Online banking Slovakia Flutter Drop-in` lines 15–23, `## Sessions flow Drop-in` lines 25–48 and `## Advanced flow Drop-in` lines 58–84. Expected answer: a 2026-09-15-captured method-specific add-on to existing Flutter Drop-in Sessions/Advanced integrations. It covers redirect and issuer/setup details, not the full base integration, current account entitlement or proof of a completed bank payment.

## Q2 — Redirect, issuer, examples and test conditions

Query: Which Online banking Slovakia Flutter Drop-in prerequisites and fields differ by Sessions versus Advanced, and what source-link/example cautions apply?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia-flutter-drop-in.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/online-banking-slovakia/flutter-drop-in/2026-09-15.md` Sessions lines 25–56, Advanced lines 58–107, examples lines 109–396 including Go lines 263–272, and test/live lines 398–404. For bank-selection journey and SK/EUR/capability context, follow `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-slovakia.md` → `raw/adyen/docs/payment-methods/online-banking-slovakia/2026-09-15.md` lines 23–31. Expected answer: Sessions requires existing Drop-in, Checkout API v68+, redirect handling and Customer Area setup, with no extra method fields/configuration; its integration-type link erroneously points to Advanced. Advanced requires existing Drop-in, redirect handling, setup and required paymentMethod.issuer; sample type onlineBanking_SK, issuer cs and v72 are example values. Server library labels do not define minimums, and the Go v10.4.0 example imports /v9/ paths. Testing uses real details/small amounts and test Customer Area status; live acceptance requires method setup, with no proof of merchant-specific enablement.
