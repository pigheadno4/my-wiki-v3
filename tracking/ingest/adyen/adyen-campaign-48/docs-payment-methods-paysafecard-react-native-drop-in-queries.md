# PaySafeCard React Native Drop-in retrieval checks

## Q1 — Purpose and proof boundary

Query: What does the PaySafeCard React Native Drop-in guide cover, and can it prove a complete integration, merchant entitlement or live success?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2663 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard-react-native-drop-in.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/paysafecard/react-native-drop-in/2026-09-15.md` `# PaySafeCard React Native Drop-in` lines 15–23, Sessions requirements lines 25–36 and Advanced requirements lines 286–296. Expected answer: 2026-09-15-captured method-specific additions to existing React Native Drop-in Sessions/Advanced flows, not a complete base implementation or live entitlement/execution proof.

## Q2 — Required field, redirect and source caveats

Query: Which PaySafeCard React Native Drop-in fields and redirect prerequisites differ by flow, what setup is needed, and which source examples need caution?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard-react-native-drop-in.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/paysafecard/react-native-drop-in/2026-09-15.md` lines 29–46, 270–284, 290–312 and 599–623; for method-level conditional CDE, follow `wiki/sources/adyen/source-adyen-docs-payment-methods-paysafecard.md` Detail locators → `raw/adyen/docs/payment-methods/paysafecard/2026-09-15.md` lines 29–31. Expected answer: Sessions requires Checkout API v68+, redirect handling and Customer Area setup; Advanced requires redirect handling and setup. Both add required shopperReference and no method-specific configuration; Support must add PaySafeCard to live Customer Area before live acceptance. Warning: Sessions integration-type link is an Advanced-flow URL, and Advanced request samples omit paymentMethod, so are not copy-ready method-selection recipes. The overview's CDE option applies conditionally where EU gambling KYC is required; it is not a child-guide request-field rule.
