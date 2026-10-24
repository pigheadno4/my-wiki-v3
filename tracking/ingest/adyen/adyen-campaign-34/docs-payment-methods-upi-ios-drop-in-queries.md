# UPI iOS Drop-in retrieval questions

## Q1 — What is this guide for, and what is required?

It adds UPI Intent to an existing iOS Drop-in integration. Sessions requires Checkout API v68+ and UPI added in Customer Area; its ordinary `/sessions` request needs no extra UPI fields (raw lines 25–40). Smart Intent shows detectable installed apps only if the merchant declares their schemes in iOS `Info.plist`, within the 50-scheme cap (lines 42–91). Advanced requires handling `action.type: await` and uses required `paymentMethod.appId` for `upi_intent` (lines 117–127, 180–210). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-upi-ios-drop-in]] → [[raw/adyen/docs/payment-methods/upi/ios-drop-in/2026-09-15]].

## Q2 — What is the QR/Collect and outcome boundary?

This page provides an iOS **Intent** path; its QR simulator line is explicitly labeled **on web**, and the page gives no iOS QR or Collect procedure, Collect migration date, manual app-return callback or iOS SDK minimum (raw lines 15–234, especially 103–104 and 222–223). The Advanced action is stated as `await` although the linked step's anchor reads “handle-the-redirect” (line 126). Its `v72`/`INR`/`IN`/`gpay` request is a test example; after a simulator outcome, the checklist calls for `AUTHORISED` webhook and Customer Area confirmation, which is separate from live authorization evidence (lines 190–234). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-upi-ios-drop-in]] → [[raw/adyen/docs/payment-methods/upi/ios-drop-in/2026-09-15]].
