# Fixed retrieval queries — Ratepay for Web

## Q1 — Identity and scope

**Query:** What does the Ratepay for Web page cover, and what cannot be inferred from it?

**Expected:** The 2026-09-15-captured page at `https://docs.adyen.com/payment-methods/ratepay/web` is a short UI integration chooser for Ratepay on websites. It links Drop-in and Components child guides and general Web UI guides. It does not establish current merchant enablement, supported country/method details, request fields, invoice/capture behavior, live readiness or a successful payment. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ratepay-web.md` → `raw/adyen/docs/payment-methods/ratepay/web/2026-09-15.md`. Evidence: raw `# Ratepay for Web` lines 15–17 and `## How do you want to integrate?` lines 19–29.

## Q2 — Child routes

**Query:** Where should a website implementer go for Ratepay Drop-in versus Components and detailed payment rules?

**Expected:** `/payment-methods/ratepay/web-drop-in` is the all-in-one UI child route (raw lines 21–23); `/payment-methods/ratepay/web-component` is the prebuilt Component child route (raw lines 25–27). General Web Drop-in and Components are linked at raw line 29. Use the selected child guide for Open Invoice/Direct Debit, fingerprint, request, result and capture/refund specifics; the chooser does not specify them. Route: root → provider index → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ratepay-web.md` → pinned raw; child links in source Related.
