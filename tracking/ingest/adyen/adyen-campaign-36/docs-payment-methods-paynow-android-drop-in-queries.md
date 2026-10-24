# Retrieval checks — PayNow Android Drop-in

## Q1. What is this source's purpose and scope, and what cannot be inferred?

`source-adyen-docs-payment-methods-paynow-android-drop-in` adds PayNow-specific guidance to an existing Android Drop-in integration, split into Sessions and Advanced (raw lines 15–25 and 60–68). It does not establish current merchant eligibility, an actual scanned QR/payment, QR expiry, refund or recurring behavior, or final settlement. The Advanced action is `qrCode`, even though the linked base-guide anchor says handle-the-redirect (raw line 67). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paynow-android-drop-in]] → [[raw/adyen/docs/payment-methods/paynow/android-drop-in/2026-09-15]].

## Q2. What central capability, prerequisites and warnings matter?

Sessions needs an existing Android Drop-in integration, Checkout API v68+ and PayNow added in Customer Area; no PayNow-specific extra `/sessions` or configuration fields are stated (raw lines 29–46). Advanced needs the base integration, `qrCode` additional-action handling and Customer Area setup; no extra PayNow configuration or ordinary `/payments` fields are stated (raw lines 62–80). Live acceptance separately requires Support adding PayNow to live Customer Area. The page suggests small live penny tests using a real banking app, but warns against test Customer Area transfers because they cannot be reversed and funds are deducted (raw lines 50–58 and 82–90). No test or payment was executed here. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paynow-android-drop-in]] → [[raw/adyen/docs/payment-methods/paynow/android-drop-in/2026-09-15]].
