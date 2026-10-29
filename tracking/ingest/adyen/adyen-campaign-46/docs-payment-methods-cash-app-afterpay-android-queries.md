# Afterpay Android chooser worker retrieval queries

## Q1 — Identity and purpose

**Query:** What is the page at the Cash App Afterpay Android URL, and does it itself describe a payment flow?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-android.md` → `raw/adyen/docs/payment-methods/cash-app-afterpay/android/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/cash-app-afterpay/android`; full pinned raw `raw/adyen/docs/payment-methods/cash-app-afterpay/android/2026-09-15.md`, `# Afterpay for Android` lines 15–17 and `## How do you want to integrate?` lines 19–29. This 2019-modified page is a 2026-09-15-captured chooser; the body says Afterpay while the path says Cash App Afterpay. It supplies no transaction or live-enablement proof.

## Q2 — Child and base routes

**Query:** Which Android integration choices and base guides does the chooser link?

**Expected route:** Same root → Adyen index → online-payments concept → Afterpay Android chooser source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: Drop-in links lines 21–23, Components/Redirect Component lines 25–27 and Android Sessions base links line 29. Use child and base guides for version, request, country/currency, redirect-result and capture/refund detail; this chooser does not state those rules.
