# Fixed retrieval checks — docs-payment-methods-online-banking-czech-republic-react-native-drop-in

## Q1 — Find purpose, flow scope and base-guide routes

- Query: What does the Czech online banking React Native Drop-in guide add to Sessions and Advanced, and which Sessions base-guide link is inconsistent?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-react-native-drop-in.md` → `raw/adyen/docs/payment-methods/online-banking-czech-republic/react-native-drop-in/2026-09-15.md`.
- Expected: Existing Sessions React Native Drop-in, Checkout API v68+, redirect handling and Customer Area setup (raw lines 25–36). No method-specific `/sessions` or configuration additions (38–48). Existing Advanced React Native Drop-in, redirect handling and Customer Area setup, with no additional method configuration or `/payments` parameters (58–80). Sessions integration-type link targets Advanced flow (33) while redirect and create-session links target Sessions flow (35, 42).
- Scope: The v68 floor appears in Sessions requirements only. Do not read the no-additional-parameters statement as an empty base request or transfer API-only issuer examples into this Drop-in flow. `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic.md` gives CZ/CZK method context.

## Q2 — Recover redirect and test/live qualifications

- Query: What does this React Native Drop-in page say about redirect handling, test payments and live setup?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-react-native-drop-in.md` → pinned raw.
- Expected: Both flows list redirect handling for `action.type: redirect` (raw lines 35, 67). Test with real payment details and small amounts; check test-payment status in Customer Area > Payments > Payment list; add the method in Customer Area before live acceptance (50–56, 82–88). The Sessions requirements link points to Advanced flow despite its Sessions label, unlike the Sessions redirect and create-session links (33, 35, 42).
- Scope: This 2026-09-15 capture contains no payment execution or final status evidence. API-only guide `wiki/sources/adyen/source-adyen-docs-payment-methods-online-banking-czech-republic-api-only.md` has distinct merchant issuer selection instructions.
