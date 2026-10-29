# Fixed queries — Online banking Czech Republic iOS Drop-in

## Q1 — purpose, scope and limits

**Query:** What does the captured Czech Republic iOS Drop-in page cover, and what should not be inferred from it?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/online-banking-czech-republic/ios-drop-in` is a 2026-09-15-captured iOS Drop-in Sessions/Advanced add-on for method prerequisites, no extra method fields/configuration, Advanced redirect handling and test/live instructions. It does not prove current merchant enablement, a complete base API request or a successful payment from a redirect. Method-level CZ/CZK and lifecycle context is in `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic.md` (full pinned `raw/adyen/docs/payment-methods/online-banking-czech-republic/ios-drop-in/2026-09-15.md`, `# Online banking Czech Republic iOS Drop-in` lines 15–23; flow headings lines 25 and 58). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-ios-drop-in.md`.

## Q2 — flow prerequisites, fields and limitations

**Query:** What do the captured Sessions and Advanced Czech iOS Drop-in sections require, and what do their no-extra-fields statements mean?

**Expected answer:** Sessions requires an existing iOS Sessions Drop-in integration, Checkout API v68 or later and Customer Area method addition (pinned `raw/adyen/docs/payment-methods/online-banking-czech-republic/ios-drop-in/2026-09-15.md`, `## Sessions flow Drop-in` lines 25–34). It needs no additional **Czech-specific** `/sessions` parameters or method configuration (lines 36–46). Advanced requires existing iOS Advanced Drop-in, handling `action.type: redirect` and Customer Area method addition (lines 58–68), with no additional **Czech-specific** configuration or `/payments` parameters (lines 70–80). Base integration fields remain applicable; this page states no separate Advanced API minimum. Both flows instruct small-amount tests, test Customer Area Payment list checks and Customer Area method addition for live acceptance (lines 48–56, 82–90). Redirect alone does not prove final paid status or merchant eligibility. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-ios-drop-in.md`.
