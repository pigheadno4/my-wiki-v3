# Cash App Afterpay Android Component worker retrieval queries

## Q1 — Purpose, flow and version scope

**Query:** What does the Cash App Afterpay Android Component guide cover, and which version and base integrations does it require?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-android-component.md` → `raw/adyen/docs/payment-methods/cash-app-afterpay/android-component/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/cash-app-afterpay/android-component`; full pinned raw `raw/adyen/docs/payment-methods/cash-app-afterpay/android-component/2026-09-15.md`, `# Cash App Afterpay Component integration` lines 15–21 and `## Requirements` lines 23–39. It labels itself v5.0.0, requires at least v5.0.0 for both Sessions and Advanced, and points older versions elsewhere. It does not prove current enablement or real payment success.

## Q2 — Request/configuration and test gates

**Query:** Does Cash App Afterpay add Android Component request fields or configuration, and what are the US sandbox and live-account steps?

**Expected route:** Same root → Adyen index → online-payments concept → Cash App Afterpay Android Component source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `## API reference` lines 41–49, `## Cash App Afterpay Configuration` lines 51–67, and `## Test and go live` lines 69–87. Preserve “no additional” as method-specific relative to existing base flow, not absence of base request requirements. Sandbox instructions require a US test shopper account, real email, test SMS code, test card and CVV simulations; live use requires a request in live Customer Area. Do not treat simulated authorised/refused responses as real operational evidence.
