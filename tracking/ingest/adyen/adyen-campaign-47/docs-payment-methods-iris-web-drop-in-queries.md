# Fixed retrieval queries — IRIS Web Drop-in

## Q1 — Purpose and scope

**Query:** What is this IRIS Web Drop-in guide, and what does its captured evidence not prove?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-iris-web-drop-in.md` → `raw/adyen/docs/payment-methods/iris/web-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/iris/web-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/iris/web-drop-in/2026-09-15.md`, `# IRIS Web Drop-in` lines 15–23, Sessions requirements lines 25–35, Advanced requirements lines 68–78. It is a method-specific add-on to existing Web Drop-in, not evidence of current enablement or an executed payment. Sessions requires Checkout API v68+; the Advanced row does not state that version minimum.

## Q2 — Issuer versus QR and operational qualifications

**Query:** What selects issuer redirect versus QR, how is each result handled, and what onboarding and example caveats apply?

**Expected route:** Same root → Adyen index → online-payments concept → IRIS Web Drop-in source → pinned raw.

**Evidence locator:** Same canonical stem and full raw path. `## Add additional parameters to your /payments request` lines 94–102 makes `paymentMethod.type: iris` required; issuer ID and `returnUrl` are required for issuer redirect, whereas no issuer produces QR data and QR does not require `returnUrl`. Issuer redirect response and return/details are at lines 426–455 and 694–706; QR `Pending` action, ten-minute window and webhook result are at lines 1026–1052. Greek-bank and Adyen DIAS-code, account/store onboarding is at lines 35, 78 and 1065. The issuer-flow SDK samples omit issuer despite the branch rule (lines 153–253, 305–327, 403–424); both payment curl blocks lack a shell continuation before `-d` (lines 112–130, 716–734); the Advanced base requirement link has an unresolved platform template (line 76). Simulator outcomes at lines 57–64 and 1056–1063 are test-only.
