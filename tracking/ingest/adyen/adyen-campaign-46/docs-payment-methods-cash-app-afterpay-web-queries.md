# Fixed retrieval queries — Cash App Afterpay Web chooser

## Q1 — Identity and scope

**Query:** Why is the page titled Afterpay for Web under a Cash App Afterpay path, and what does it actually cover?

**Expected:** The captured chooser at `https://docs.adyen.com/payment-methods/cash-app-afterpay/web` has visible title “Afterpay for Web” but child links under `cash-app-afterpay`. It routes to Web Drop-in/Components guides and general Web UI guides; it does not state eligibility, request fields, redirect/capture behavior or a payment result. The related method overview supplies US/USD regional context; do not apply this path's details to AU/NZ Afterpay or UK Clearpay. Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-web.md` → `raw/adyen/docs/payment-methods/cash-app-afterpay/web/2026-09-15.md`. Evidence: raw lines 6–10 and 15–29; related `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay.md`.

## Q2 — Child routes

**Query:** Where does this Web chooser send Drop-in and Components implementers?

**Expected:** Drop-in links to `/payment-methods/cash-app-afterpay/web-drop-in` as all-in-one UI (raw lines 21–23). Components links to `/payment-methods/cash-app-afterpay/web-component` as prebuilt UI (raw lines 25–27). It separately links generic Web Drop-in and Components at raw line 29. Detailed payment instructions live in the selected child, not this chooser. Route: root → provider index → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-web.md` → pinned raw; child links in Related.
