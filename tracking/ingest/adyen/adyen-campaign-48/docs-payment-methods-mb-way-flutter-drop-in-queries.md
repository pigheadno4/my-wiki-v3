# MB WAY Flutter Drop-in retrieval checks

## Q1 — Purpose and proof boundary

Query: What does the MB WAY Flutter Drop-in guide cover, and does it establish App2App implementation or live payment success?

Expected route: `wiki/index.md` line 10 → `wiki/adyen-index.md` line 2663 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-flutter-drop-in.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/mb-way/flutter-drop-in/2026-09-15.md` `# MB Way Flutter Drop-in` lines 15–23, `## Sessions flow Drop-in` lines 25–35 and `## Advanced flow Drop-in` lines 95–105. Expected answer: a 2026-09-15-captured method-specific add-on to existing Flutter Drop-in Sessions/Advanced flows. It does not supply an App2App recipe or prove current enablement, complete base integration or completed live payment.

## Q2 — Required fields, await and source cautions

Query: What are the MB WAY Flutter Drop-in flow-specific fields and `await` handling, what setup is required, and which links/test examples need caution?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-flutter-drop-in.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/mb-way/flutter-drop-in/2026-09-15.md` `## Sessions flow Drop-in` lines 25–93 and `## Advanced flow Drop-in` lines 95–187. For method-level shopper journeys, PT/EUR/capability indicators and cumulative limit, follow `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way.md` → `raw/adyen/docs/payment-methods/mb-way/2026-09-15.md` lines 23–36. Expected answer: Sessions requires existing Drop-in, Checkout API v68+, Support/Customer Area setup, and marks shopperStatement required; its integration-type link mistakenly points to Advanced flow. Advanced requires existing Drop-in with await-action handling, Customer Area setup, and required type mbway and telephoneNumber; shopperStatement is optional there. Pending/await is a waiting state, not final authorization. Neither flow needs MB WAY-specific configuration. Live Customer Area setup is required; the Sessions test-trigger text points to /payments and is not a /sessions recipe. App2App is only overview-level context here.
