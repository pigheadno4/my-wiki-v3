# C31 Flutter Drop-in cards retrieval checks

## Q1 — Main purpose and prerequisites

**Question:** What must exist before adding cards to Flutter Drop-in, and how do the Sessions and Advanced server routes differ?

**Answer:** The page is an add-on to an **existing Flutter Drop-in** integration and says to add cards in the Customer Area for either route (pinned raw lines 15–37). It says base card requests need no extra fields: `/sessions` in Sessions (line 43) and `/payments` in Advanced (line 47), with no extra base Drop-in configuration (lines 49–57). Advanced points to required callbacks in a separate guide (lines 82–84). Optional split debit/credit requires server `splitCardFundingSources: true` on `/sessions`, or on Advanced `/paymentMethods` with a **Checkout API v53-or-later** gate (lines 93–124). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/cards/flutter-drop-in/2026-09-15]].

## Q2 — Material boundary or conflict

**Question:** Does the Flutter card guide establish a consented stored-card payment and live readiness, and what source differences require care?

**Answer:** No. It strongly recommends explicit permission for future recurring charges (pinned raw lines 194–198); its Sessions curl uses `askForConsent` (line 227), while Java/Python examples use `enabled` (lines 251–260, 435–449). The optional table says `showStorePaymentMethodField` (line 70), while Advanced token prose says `showStorePaymentField` (line 838); the page does not reconcile the names. It says `recurring.token.created` is received when a token is created (line 519), not that a later charge succeeded. The test `test_` prefix is for encrypted test-card details (line 2302); before live card payments it calls for live Customer Area card setup and PCI DSS assessment plus required SAQ A (lines 2304–2310). Code examples and token creation do not prove authorization, capture or settlement. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/cards/flutter-drop-in/2026-09-15]].
