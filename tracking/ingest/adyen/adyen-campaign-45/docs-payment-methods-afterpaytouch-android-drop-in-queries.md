# Afterpay Android Drop-in worker retrieval queries

## Q1 — Purpose and scope

**Query:** What does the Afterpay Android Drop-in page add, and which base integration does it assume?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-afterpaytouch-android-drop-in.md` → `raw/adyen/docs/payment-methods/afterpaytouch/android-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/afterpaytouch/android-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/afterpaytouch/android-drop-in/2026-09-15.md`, `# Afterpay Android Drop-in` lines 15–23, `## Sessions flow Drop-in` lines 25–34 and `## Advanced flow Drop-in` lines 787–795. This is method-specific work on an existing Android Drop-in integration; it does not demonstrate app execution or merchant approval.

## Q2 — Central capability, prerequisites and warnings

**Query:** What differs between Sessions and Advanced request setup, and what capture and test limits apply?

**Expected route:** Same root → Adyen index → online-payments concept → Afterpay Android Drop-in source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path, `## Add additional parameters to your /sessions request` lines 38–51, `## Add additional parameters to your /payments request` lines 805–822, Advanced redirect response lines 1534–1548, `## Capture the payment` lines 745–764 and 1550–1569, `## Test and go live` lines 766–785 and 1571–1590. Preserve Sessions API v68+, Advanced redirect handling, required shopper/address/line-item fields, Advanced `afterpaytouch`, no extra Drop-in configuration, 13-day production versus one-day test expiry, cancellation/refund, partial remainder exception and live request. A redirect response or sandbox account does not prove final payment or live availability.
