# PayBright Web chooser retrieval check

- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paybright-web.md` → `raw/adyen/docs/payment-methods/paybright/web/2026-09-15.md`.

## Q1 — Purpose, scope, and what not to infer

**Query:** What is the PayBright for Web page for, and can its integration choices establish that a new merchant can add PayBright?

**Expected:** It is a Web chooser linking Drop-in and Components. It explicitly says Adyen will not accept new PayBright integrations after the Affirm acquisition. Its navigation does not establish current merchant eligibility or payment success. Evidence: raw `# PayBright for Web` lines 15–19 and `## How do you want to integrate?` lines 21–29.

## Q2 — Central routes and warning

**Query:** Which Web routes does this page point to, what do the labels promise, and what prerequisite warning governs their use?

**Expected:** Drop-in is labelled an all-in-one UI solution; Components is labelled a pre-built Component. General Web Drop-in/Components references appear at line 31. The page does not provide child flow/version prerequisites; consult `source-adyen-docs-payment-methods-paybright-web-drop-in` or `source-adyen-docs-payment-methods-paybright-web-component` for them. Adyen's no-new-integrations notice at line 19 governs interpretation of the chooser. Evidence: raw lines 19, 21–31.
