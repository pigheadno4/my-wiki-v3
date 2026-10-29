# Fixed retrieval checks — docs-payment-methods-cash-app-afterpay-web-component

## Q1 — Purpose and scope

**Query:** What does Adyen's Cash App Afterpay Web Component page cover, and does it prove live enablement?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-web-component.md` → `raw/adyen/docs/payment-methods/cash-app-afterpay/web-component/2026-09-15.md`.

**Answer:** It adds Cash App Afterpay to existing Web Components Sessions or Advanced integrations, then covers method-specific requests, mounting, capture/refund/discount and TEST/live steps (raw 15–43, 1216–1334). The captured examples do not prove live merchant enablement or a completed payment; live acceptance requires a separate Customer Area request (1334). Canonical stem: `https://docs.adyen.com/payment-methods/cash-app-afterpay/web-component`.

## Q2 — Capture, expiry, partial changes and warnings

**Query:** What capture window and partial-capture behavior apply to Cash App Afterpay Web Component, and what setup is needed?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Sessions is default for Web Components v5+; both flow tables mark name, email, three-character-minimum shopperReference, country, billing/delivery addresses and lineItems required, with telephone optional (49–62, 746–759). TEST examples are US/USD and Advanced type afterpaytouch_US (67–84, 764–784). Web v6 uses new Afterpay; v5 or earlier uses checkout.create (1216–1246). Capture can be automatic or manual by account configuration; delayed automatic or manual capture is needed after shipment, and partial capture needs manual capture (1248–1250). Capture within 13 days; the first installment is charged during authorization and refunded if uncaptured at expiry; TEST manual capture must be within one day (1252–1256). Standard partial capture automatically cancels unclaimed balance, but enabled multiple partial captures retain it; Support setup is required and each capture creates an invoice (1258–1267). Cancel before capture, refund afterward (1269–1278). The discount example's 800 total can reflect two -100 units but JSON is not copy-ready due ellipsis and missing comma (1280–1314). Test uses Afterpay sandbox; live needs a separate Customer Area request (1316–1334). Canonical stem: `https://docs.adyen.com/payment-methods/cash-app-afterpay/web-component`; pinned raw: `raw/adyen/docs/payment-methods/cash-app-afterpay/web-component/2026-09-15.md`.
