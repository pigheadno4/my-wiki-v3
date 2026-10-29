# PayPo Flutter Drop-in retrieval checks

## Q1 — Purpose and scope

Query: What does the PayPo Flutter Drop-in page cover, and is it a complete integration or proof of live enablement?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2610 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-flutter-drop-in.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/paypo/flutter-drop-in/2026-09-15.md` `# PayPo Flutter Drop-in` lines 15–23, `## Sessions flow Drop-in` lines 25–41 and `## Advanced flow Drop-in` lines 443–465. Expected answer: 2026-09-15-captured method-specific additions to existing Flutter Drop-in Sessions/Advanced integrations; no complete base implementation, current account enablement, or payment proof.

## Q2 — Fields, redirect and capture conditions

Query: Which PayPo Flutter Drop-in fields and action handling differ by flow, and what are the offer, payment-term, capture and funding conditions?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-flutter-drop-in.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/paypo/flutter-drop-in/2026-09-15.md` lines 29–48, 391–427, 447–473, 845–875. Expected answer: Sessions requires Checkout API v68+, Support/Customer Area setup and shopper name/email; Advanced requires redirect action handling, PayPo method type and shopper name/email. Addresses are unmarked optional in both tables; no PayPo-specific configuration. An unaccepted offer lasts up to 72 hours; shopper has 30 days to pay after authorization; capture is full amount only and required after authorization, with optional immediate automatic capture. Merchant funding is stated after capture, without waiting for shopper repayment. Warning: Sessions requirement links to an Advanced-flow URL; the Sessions create-session link and flow headings define this route, and sample returnUrls differ between flows.
