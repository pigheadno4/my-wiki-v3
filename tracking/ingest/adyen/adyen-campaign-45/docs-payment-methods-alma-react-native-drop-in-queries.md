# Alma React Native Drop-in worker retrieval queries

## Q1 — Purpose and scope

**Query:** What integration does this Alma React Native Drop-in guide extend, and which server-side flows does it cover?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma-react-native-drop-in.md` → `raw/adyen/docs/payment-methods/alma/react-native-drop-in/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/alma/react-native-drop-in`; full pinned raw `raw/adyen/docs/payment-methods/alma/react-native-drop-in/2026-09-15.md`, `# Alma React Native Drop-in` lines 15–23, `## Sessions flow Drop-in` lines 25–36 and `## Advanced flow Drop-in` lines 99–109. Sessions requires Checkout API v68+; its base-guide link points to Advanced despite the Sessions label, while other Sessions links point to Sessions. The page does not prove live eligibility or an executed payment.

## Q2 — Capability, prerequisites and warnings

**Query:** Which Alma fields and optional installment choice does the React Native Drop-in guide specify, and what does its redirect example establish?

**Expected route:** Same root → Adyen index → online-payments concept → Alma React Native Drop-in source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path; `## Add additional parameters to your /sessions request` lines 40–49, `## Add additional parameters to your /payments request` lines 119–129, Advanced response lines 171–185, and `## Test and go live` lines 93–97 and 187–191. Telephone, email and addresses have blank Required cells. Optional `alma.installments_count` is 3 or 4, or omitted for shopper choice. Both sections say no extra Alma configuration. `RedirectShopper` is an intermediate action; example return URL schemes and FR/EUR values are not universal rules.
