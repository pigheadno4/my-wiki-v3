# Fixed retrieval checks — docs-payment-methods-iris-web-component

## Q1 — Purpose and scope

**Query:** What does Adyen's IRIS Web Component page add to an integration, and does its simulator show current live eligibility or a completed payment?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-iris-web-component.md` → `raw/adyen/docs/payment-methods/iris/web-component/2026-09-15.md`.

**Answer:** The 2026-09-15 guide adds IRIS to existing Web Components Sessions and Advanced flows. Sessions uses Checkout API v68+ and has no method-specific `/sessions` fields or configuration; Advanced branches between issuer redirect and QR. This is a TEST-oriented snapshot, not proof of merchant activation, a live payment or settlement. Before live use the page requires Greek-bank and Adyen onboarding with DIAS code, merchant account and stores, plus live Customer Area enablement (pinned raw `# IRIS Web Component` lines 15–35, Sessions 39–75, Advanced 88–136, test/live 1088–1097). Canonical stem: `https://docs.adyen.com/payment-methods/iris/web-component`.

## Q2 — Action choice, result and warnings

**Query:** How do issuer redirect and QR differ in the IRIS Web Component Advanced flow, and how is each result obtained?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Advanced must handle `redirect` and `qrCode` actions (`## Requirements`, raw 90–96). `/payments` requires `paymentMethod.type: iris`; issuer redirect also requires `paymentMethod.issuer` and `returnUrl`, while omitting issuer yields QR data and QR does not require `returnUrl` (payment table 128–136). Redirect response is `RedirectShopper`; use `action.url`, then POST `/payments/details` with URL-decoded `redirectResult` after return. Its `Authorised` response is an example, not independent success or settlement proof (460–488, 728–740). QR response is `Pending` with `qrCodeData`; render the code, give the shopper 10 minutes to complete, and use the later webhook result (1060–1086). The QR example includes an optional `returnUrl` (742–768). The redirect curl supplies issuer, but Java, PHP, C#, Go and TypeScript snippets under that heading omit it, contrary to the table's redirect condition (146–165, 183–199, 220–242, 263–286, 339–360, 443–457). Both request curls omit a shell continuation before `-d` (151–152, 755–756), so they are not copy-ready. Canonical stem: `https://docs.adyen.com/payment-methods/iris/web-component`; pinned raw: `raw/adyen/docs/payment-methods/iris/web-component/2026-09-15.md`.
