# Fixed queries — Online banking Czech Republic Web Drop-in

## Q1 — purpose, scope and limits

**Query:** What does the captured Czech Republic Web Drop-in page cover, and what should not be inferred from it?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/online-banking-czech-republic/web-drop-in` is a 2026-09-15-captured Web Drop-in Sessions/Advanced add-on for redirect prerequisites, optional `OnlineBankingCZ` import and test/live steps. It does not prove current account enablement, a complete base API request or a successful payment from redirect handling. Method-level CZ/CZK context is in `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic.md` (full pinned `raw/adyen/docs/payment-methods/online-banking-czech-republic/web-drop-in/2026-09-15.md`, `# Online banking Czech Republic Web Drop-in` lines 15–23; flow headings lines 25 and 66). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-web-drop-in.md`.

## Q2 — flow prerequisites, fields and warning

**Query:** What do the captured Sessions and Advanced Czech Web Drop-in sections require and what caveat affects the Advanced base-guide link?

**Expected answer:** Sessions requires existing Web Drop-in Sessions, Checkout API v68+, `action.type: redirect` handling and Customer Area addition, with no extra **method-specific** `/sessions` parameters (pinned `raw/adyen/docs/payment-methods/online-banking-czech-republic/web-drop-in/2026-09-15.md`, `## Sessions flow Drop-in` lines 25–42). The `OnlineBankingCZ` import is optional for tree shaking (lines 44–54). Advanced requires existing Web Drop-in Advanced, redirect handling and Customer Area addition, with no extra **method-specific** `/payments` fields (lines 66–94); base fields still apply and no Advanced API minimum is stated here. Its prerequisite URL contains unresolved `{{getParameter('platform')}}` rather than a concrete Web value (line 74), so verify the actual base guide. Both flows instruct small-amount tests, test Customer Area Payment list checks and Customer Area method addition for live acceptance (lines 56–64, 96–104). Redirect alone is not final paid status. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-web-drop-in.md`.
