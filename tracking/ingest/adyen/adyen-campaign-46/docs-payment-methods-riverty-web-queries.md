# Fixed retrieval queries — Riverty for Web

## Q1 — Identity and scope

**Query:** What does Adyen's Riverty for Web page contain, and what does it not establish?

**Expected:** It is the short 2026-09-15-captured chooser at `https://docs.adyen.com/payment-methods/riverty/web`, routing to Riverty Web Drop-in and Component child guides. It does not give method eligibility, request fields, redirect/capture behavior or a transaction result; those require the selected child and method overview. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-riverty-web.md` → `raw/adyen/docs/payment-methods/riverty/web/2026-09-15.md`. Evidence: raw `# Riverty for Web` lines 15–27.

## Q2 — Which integration guide?

**Query:** Which Riverty Web path should an implementer follow for Drop-in versus Components, and which general flow guides are linked?

**Expected:** Drop-in is the all-in-one UI child route `/payment-methods/riverty/web-drop-in`; Component is the prebuilt Component child route `/payment-methods/riverty/web-component` (raw lines 21–27). The page says to create a main integration first and links four general paths: Web Drop-in Sessions and Advanced, Web Components Sessions and Advanced (raw lines 29–36). The chooser does not reconcile the method overview's Direct-flow label with redirect handling in child guides; read those exact sources before choosing implementation details. Route: root → provider index → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-riverty-web.md` → pinned raw; child routes in source Related.
