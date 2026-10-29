# Fixed retrieval checks — Pay by Bank (Europe) Web Drop-in

## Q1 — Purpose, scope and proof boundary

**Query:** What does the captured Pay by Bank (Europe) Web Drop-in page add, and what does it not prove about a merchant, country or payment result?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-pay-by-bank-europe-web-drop-in.md` → full pinned raw `raw/adyen/docs/payment-methods/pay-by-bank-europe/web-drop-in/2026-09-15.md`. Canonical stem: `https://docs.adyen.com/payment-methods/pay-by-bank-europe/web-drop-in`.

**Expected answer:** This captured method-specific guide adds Pay by Bank (Europe) to existing Web Drop-in Sessions or Advanced flows; both require v5.70.0+ and Support setup in Customer Area (pinned raw lines 15–37). It covers countryCode, optional Tink issuer selection, separate SEPA recurring guidance, and tests. It does not establish current market/merchant eligibility or a completed/settled bank transfer. Related method overview `raw/adyen/docs/payment-methods/pay-by-bank-europe/2026-09-15.md` line 23 also says onboarding requires approval; its prose at line 27 lists DE/FR/UK while its matrix at line 43 also lists FI, and this child has Finland test credentials (pinned raw 1548–1556). Do not convert that into live Finland support.

## Q2 — Fields, issuer choice, recurring and outcome warnings

**Query:** What are the Web Drop-in requirements and optional bank-choice behavior, how are future recurring payments actually made, and which example/result caveats matter?

**Expected route:** Same root → Adyen index → online-payments concept → Pay by Bank (Europe) Web Drop-in source → pinned raw; follow related method overview source/raw for approval, market and settlement caveats.

**Expected answer:** The /sessions and /payments tables mark countryCode required; QZ is a country-code format exception, not method availability (pinned raw 47–65). In Germany, Tink handles bank choice; in the UK a merchant can optionally show an issuer list before Tink, with optional logo, preselected/highlighted issuers and placeholder config under paymentMethodsConfiguration.paybybank (67–156). Future recurring payments use **SEPA Direct Debit** tokenization, not a repeated paybybank request; explicit shopper permission is strongly recommended, and later off-session payments use a stored ID with Subscription or UnscheduledCardOnFile (158–173, 523–555, 872–899). The “Create a token” examples already include storedPaymentMethodId (175–198), so they do not show how the initial ID was obtained; a later unscheduled section's legacy example uses Subscription (1215–1235). A Received resultCode means received, with success tracked by webhook (1496). The related overview raw 45–60 warns even successful AUTHORISATION does not guarantee funds, and documents possible later chargeback/reversal. Test/demo credentials (1498–1556) and a live Customer Area addition (1502) do not prove live operation. Canonical stem and full pinned path as in Q1.
