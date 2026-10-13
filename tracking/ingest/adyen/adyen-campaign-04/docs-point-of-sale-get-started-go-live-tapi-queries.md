# Fixed retrieval checks — Terminal API go-live

## Purpose, scope, and limits

**Query:** What is this checklist for, and what does it not prove?

**Answer:** It is Adyen's go-live sequence for a merchant Terminal API integration with Adyen-provided payment terminals. The 2026-09-15 capture has a 2020-09-25 `last_modified` value. It describes actions and a suggested real-card test, but proves no live-account approval, merchant or terminal eligibility, successful authorization/capture/settlement, refund, or reconciliation. It does not establish a current processing or shipping SLA. Raw `Terminal API go-live checklist` / `Requirements`, lines 5–35; `1. Set up your Adyen live account`, lines 37–43; `6. Test your integration`, lines 175–199. Route after catalog update: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-terminal-api.md` → `wiki/sources/adyen/source-adyen-docs-point-of-sale-get-started-go-live-tapi.md` → `raw/adyen/docs/point-of-sale/get-started/go-live-tapi/2026-09-15.md`.

## Central steps, prerequisites, and warnings

**Query:** What must move from test to live, and how do local and cloud paths differ?

**Answer:** Apply for a live account and sign the contract; create live merchant accounts and stores because test structure is not copied. Review payout bank accounts and reconciliation; optional schedule change and Reserve/auto-funding are presented with their own qualifiers (raw lines 27–96). Order live terminals because test terminals cannot process live payments, then configure live Terminal API and payment features from scratch, assign terminals to stores, and board/check them (raw lines 98–130, 162–173). Add live credentials. Local POS code must use live terminal IPs/hostnames, validate the live certificate (or use a library), and encrypt requests; the guide says live terminals reject unencrypted requests. Cloud code needs a new API key and live endpoints (raw lines 132–160). The guide recommends live end-to-end testing with a real low-value card payment, Customer Area journal review, reconciliation, and refund. Its Received → Authorised → Settled example does not mean a capture configuration or completed live payment was evidenced (raw lines 175–199). Linked credential, security, terminal, finance, and diagnostics documents are navigation until read. Route after catalog update: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-terminal-api.md` → `wiki/sources/adyen/source-adyen-docs-point-of-sale-get-started-go-live-tapi.md` → `raw/adyen/docs/point-of-sale/get-started/go-live-tapi/2026-09-15.md`.
