# PayPal iOS Drop-in retrieval checks

Q1. What does this guide add, and what setup and flow must already exist?

It adds PayPal to an existing iOS Drop-in integration after the PayPal setup steps (raw lines 15–26). `/sessions` is the default for Drop-in v5.0.0 or later (lines 28–34), while `/payments` is offered for an additional use case (lines 510–512). Forward route: [[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-paypal-ios-drop-in]] → [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15]].

Q2. Why cannot a merchant treat the API response or a refund request as final success?

The page says a synchronous `resultCode`, even `Authorised`, does not give the final outcome; await `AUTHORISATION`, and `OFFER_CLOSED` appears only when enabled (raw lines 1125–1151). Before capture use cancellation and after capture use refund (line 1225); delayed capture with multiple partial captures needs the capture PSP reference or the refund can fail (lines 1308–1326). The immediate-capture partial-refund prose says line items are needed while its table leaves them unmarked as required (lines 1227–1243), so that instruction needs version-specific checking. Forward route: [[index]] → [[adyen-index]] → [[adyen-ios-sdk]] → [[source-adyen-docs-payment-methods-paypal-ios-drop-in]] → [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15]].
