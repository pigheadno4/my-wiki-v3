# Clearpay Android Drop-in worker retrieval queries

## Q1 — Purpose and scope

**Query:** What integration does the Clearpay Android Drop-in guide extend, and which flow prerequisites differ?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-clearpay-android-drop-in.md` → `raw/adyen/docs/payment-methods/clearpay/android-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/clearpay/android-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/clearpay/android-drop-in/2026-09-15.md`, `# Clearpay Android Drop-in` lines 15–23, `## Sessions flow Drop-in` lines 25–34, and `## Advanced flow Drop-in` lines 213–221. Sessions states Checkout API v68+; Advanced states redirect handling. The page is method-specific guidance for existing Android Drop-in flows, not proof of live enablement or a successful payment.

## Q2 — Capability, prerequisites and warnings

**Query:** What request fields, capture/refund and discount conditions does the captured guide state?

**Expected route:** Same root → Adyen index → online-payments concept → Clearpay Android Drop-in source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path; Sessions fields lines 38–51, Advanced fields/sample lines 231–256, redirect example lines 310–324, `## Capture the payment` lines 122–141 and 328–347, `## Refunds and cancellations` lines 145–154 and 349–358, `## Discounts` lines 158–192 and 360–394, `## Test and go live` lines 196–211 and 396–411. Preserve the 13-day production versus one-day test authorization windows, automatic/manual capture split, partial remainder exception, cancel-before-capture/refund-after-capture, and live request gate. The Advanced sample includes `paymentMethod.type: clearpay` although its table omits that row. Discount sample is not copy-ready JSON due to ellipsis and missing comma.
