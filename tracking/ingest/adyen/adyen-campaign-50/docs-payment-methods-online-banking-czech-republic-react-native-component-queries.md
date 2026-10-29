# docs-payment-methods-online-banking-czech-republic-react-native-component retrieval checks

## Q1 — Scope and route

Query: Is Online banking Czech Republic available through React Native Components Sessions flow, and what does this page cover?

Expected: The 2026-09-15-captured guide explicitly says React Native Components do not support Sessions flow (raw lines 25–29). It covers an existing Advanced React Native Components add-on, redirect, method setup and test/live steps (lines 31–61). It does not prove current merchant enablement or final payment success. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-czech-republic-react-native-component]] → [[raw/adyen/docs/payment-methods/online-banking-czech-republic/react-native-component/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-czech-republic/react-native-component/2026-09-15.md`.

## Q2 — Advanced prerequisites and caveats

Query: What does the React Native Components Advanced guide require and where is its base link inconsistent?

Expected: An existing Advanced React Native Components integration, action.type redirect handling and Customer Area method setup are prerequisites (raw lines 35–41). The page states no extra method configuration or /payments parameters (lines 43–53), scoped to this Components flow, not the separate API-only issuer-selection path [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]. The prerequisite's React Native Components label points to integration=Drop-in (line 39), while redirect and /payments links target Components (lines 40 and 53); verify the Components base guide. Test with real details/small amounts, inspect test Payment list, and add the method for live are captured instructions, not evidence of testing (lines 55–61). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-online-banking-czech-republic-react-native-component]] → [[raw/adyen/docs/payment-methods/online-banking-czech-republic/react-native-component/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/online-banking-czech-republic/react-native-component/2026-09-15.md`.
