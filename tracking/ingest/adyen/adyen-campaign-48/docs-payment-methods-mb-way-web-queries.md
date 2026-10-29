# Fixed queries — MB WAY Web chooser

## Q1 — purpose and limits

**Query:** What does the captured MB WAY Web page provide, and what does it leave to child guides?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/mb-way/web` is a 2026-09-15-captured chooser for website Drop-in and Components routes and the main Web server-side integrations. It gives navigation, not request fields, action/result behavior, current merchant eligibility, or proof of payment (full pinned `raw/adyen/docs/payment-methods/mb-way/web/2026-09-15.md`, `# MB Way for Web` lines 15–17 and chooser/See also lines 19–36). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-web.md`.

## Q2 — UI and flow routes

**Query:** Which MB WAY Web UI paths and base Sessions/Advanced routes does this page link?

**Expected answer:** Drop-in is the all-in-one website UI route `/payment-methods/mb-way/web-drop-in`. Components routes to `/payment-methods/mb-way/web-component` and names `MBWay` but provides no initialization recipe (pinned `raw/adyen/docs/payment-methods/mb-way/web/2026-09-15.md`, `### How do you want to integrate?` lines 19–27). The page directs readers to create the main integration first and links Web Drop-in/Components for both Sessions and Advanced flows (`## See also` lines 29–36). Select the corresponding child and base guide for actual request/configuration behavior; the chooser alone does not establish live availability. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-mb-way-web.md`.
