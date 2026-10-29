# ANCV Web chooser retrieval checks

## Q1 — Purpose and limits

Query: What does Adyen's ANCV for Web page contain, and can it prove current merchant eligibility or a completed payment?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2610 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-ancv-web.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/ancv/web/2026-09-15.md` `# ANCV for Web` lines 15–27 and `## See also` lines 29–36. Expected answer: a 2026-09-15-captured chooser for ANCV Web Drop-in/Components and main Sessions/Advanced guides, not a complete integration or live-payment proof.

## Q2 — Routes and method prerequisites

Query: Which Web ANCV integration routes are offered, what main integration step precedes them, and where are the ANCV contract/partial-payment conditions found?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ancv-web.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/ancv/web/2026-09-15.md` lines 19–36; for method-level conditions follow `wiki/sources/adyen/source-adyen-docs-payment-methods-ancv.md` Detail locators → `raw/adyen/docs/payment-methods/ancv/2026-09-15.md` lines 25 and 35–39. Expected answer: Web Drop-in all-in-one UI and Components Redirect child guides, plus base Web Drop-in/Components guides in Sessions and Advanced flows; create main integration first. The separate overview says merchants contract directly with ANCV, ANCV settles/reports while Adyen is gateway, and partial authorization requires partial payments with orderData from /payments/details. Warning: those method claims are overview evidence, not this chooser's raw; its links alone do not establish child flow support, current enablement or transaction success.
