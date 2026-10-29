# MB WAY Android Drop-in retrieval checks

## Q1 — Purpose and proof boundary

Query: What does the MB WAY Android Drop-in guide cover, and can it prove a complete integration or live merchant/payment success?

Expected route: `wiki/index.md` line 10 → `wiki/adyen-index.md` line 2663 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-android-drop-in.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/mb-way/android-drop-in/2026-09-15.md` `# MB Way Android Drop-in` lines 15–23, Sessions heading/requirements lines 25–34 and Advanced heading/requirements lines 112–120. Expected answer: 2026-09-15-captured MB WAY-specific additions to an existing Android Drop-in integration for Sessions or Advanced flows, including an optional App2App path. It is not the base integration, evidence of current merchant enablement or completed live payment.

## Q2 — Flow fields, App2App and caveats

Query: Which MB WAY Android Drop-in fields and action handling apply to Sessions versus Advanced, how does App2App change the shopper path, and what test/live and method-level conditions matter?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-android-drop-in.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/mb-way/android-drop-in/2026-09-15.md` `## Sessions flow Drop-in` lines 25–110, `## Advanced flow Drop-in` lines 112–197, `## Enable App2App switch` lines 201–255, and `## Test and go live` lines 257–276. For PT/EUR, capability indicators and daily cumulative user limit, follow `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way.md` → `raw/adyen/docs/payment-methods/mb-way/2026-09-15.md` lines 23–36. Expected answer: Sessions requires existing Drop-in, Checkout API v68+, Customer Area setup, and marks shopperStatement required. Advanced requires await-action handling and setup; its standard flow requires type mbway and telephoneNumber while shopperStatement is optional; Pending/await is a waiting state. App2App uses iOS/Android channel and returnUrl to obtain and directly follow an MB WAY deep link, avoiding manual phone entry; missing/Web channel falls back to standard flow. Live Customer Area enablement is required. The App2App JSON comments/placeholder and Kotlin snippets are illustrative, and the overview's PT/EUR/capability/limit facts are method-level snapshot context, not guaranteed account eligibility.
