# Afterpay React Native Drop-in retrieval checks

## Q1 — What does this guide add, and what must not be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-afterpaytouch-react-native-drop-in]]` → `[[raw/adyen/docs/payment-methods/afterpaytouch/react-native-drop-in/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-afterpaytouch-react-native-drop-in`. Full pinned raw path: `raw/adyen/docs/payment-methods/afterpaytouch/react-native-drop-in/2026-09-15.md`. Raw lines 15–36 and 789–800 make this an existing React Native Drop-in Sessions/Advanced add-on with Customer Area setup and redirect handling. AU/AUD examples and sandbox region choices do not prove current live eligibility or payment execution. The Sessions integration-type link incorrectly targets an Advanced-flow URL at line 33.

## Q2 — Which request, redirect and capture qualifications matter?

Use the same root/provider/concept/source/raw route. Sessions needs Checkout API v68+ (line 34); lines 40–53 require shopper name/email/reference, country code, both addresses and line items, with phone optional. Advanced adds required `paymentMethod: afterpaytouch` at lines 809–824. No extra Drop-in parameters are required (741–743 and 803–805). A `redirect` action/`RedirectShopper` example is at 1538–1552, not proof of authorization. Capture may be automatic or manual; production capture limit is 13 days, with first-installment refund on noncapture, while test manual capture has a one-day limit (1554–1562). Partial capture cancels the remainder unless Support-enabled multiple partial captures are configured, creating a new invoice per capture (1564–1573). Test account, CVV and live-request steps are at 1575–1594.
