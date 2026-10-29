# Afterpay React Native Component worker retrieval queries

## Q1 — Purpose and scope

**Query:** Which React Native Component server-side flow does this Afterpay guide support?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-afterpaytouch-react-native-component.md` → `raw/adyen/docs/payment-methods/afterpaytouch/react-native-component/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/afterpaytouch/react-native-component`; full pinned raw `raw/adyen/docs/payment-methods/afterpaytouch/react-native-component/2026-09-15.md`, `## Sessions flow Component` lines 25–29 and `## Advanced flow Component` lines 31–41. Sessions is explicitly unsupported; the page is an Advanced add-on to an existing Components integration. Its base-guide link labelled Components has `integration=Drop-in`, a source link mismatch, while payment and redirect links say Components.

## Q2 — Capability, prerequisites and warnings

**Query:** What Advanced request and redirect fields, capture constraints and live gate does this guide state?

**Expected route:** Same root → Adyen index → online-payments concept → React Native Component source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path; `## Add additional parameters to your /payments request` lines 51–65, response lines 780–794, `## Capture the payment` lines 796–815, `## Test and go live` lines 817–836. Advanced requires `afterpaytouch`, shopper/address/line-item data and redirect handling. Capture has a 13-day production window, one-day test expiry and a conditional multiple-partial-capture remainder exception. The sandbox country selector and redirect response do not establish live eligibility or final payment success.
