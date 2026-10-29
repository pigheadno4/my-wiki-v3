# Alma React Native Component worker retrieval queries

## Q1 — Purpose and scope

**Query:** Is Alma supported with React Native Components Sessions flow, and which integration does this page extend?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma-react-native-component.md` → `raw/adyen/docs/payment-methods/alma/react-native-component/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/alma/react-native-component`; full pinned raw `raw/adyen/docs/payment-methods/alma/react-native-component/2026-09-15.md`, `# Alma React Native Component` lines 15–23, `## Sessions flow Component` lines 25–29 and `## Advanced flow Component` lines 31–41. Sessions is explicitly unsupported. Advanced assumes existing Components redirect handling and Customer Area setup. The Components-labelled base guide link points to `integration=Drop-in`, while redirect/payment links point to Components; that mismatch does not establish Drop-in scope.

## Q2 — Capability, prerequisites and warnings

**Query:** Which Alma Advanced fields and installment choice are specified, and what does the redirect example establish?

**Expected route:** Same root → Adyen index → online-payments concept → Alma React Native Component source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path; `## Add additional parameters to your /payments request` lines 51–61, TEST curl example lines 63–101, response lines 103–117, and `## Test and go live` lines 119–123. The field table's Required cells are blank. `alma.installments_count` may be 3 or 4 or omitted for shopper choice. The TEST curl omits a line continuation after `-X POST` before `-d` at lines 70–71, so the literal command is not copy-ready. `RedirectShopper` is an intermediate action; FR/EUR examples do not prove live eligibility or outcome.
