# PayNow iOS Drop-in retrieval checks

**Q1. What is the page for, and what cannot be inferred?** It is a PayNow-specific iOS Drop-in add-on for existing Sessions or Advanced flows. It does not establish current eligibility, a QR scan, bank transfer, final payment result, QR expiry, or iOS SDK version. Raw locators: `raw/adyen/docs/payment-methods/paynow/ios-drop-in/2026-09-15.md:17-46,60-82`. Canonical stem: `https://docs.adyen.com/payment-methods/paynow/ios-drop-in`.

**Q2. What capability, prerequisites, and warnings matter?** Sessions requires Checkout API v68+, existing iOS Drop-in and PayNow setup; Advanced requires existing iOS Drop-in, `qrCode` action handling and setup. Neither branch adds method-specific ordinary request/configuration fields. Support must add PayNow in live Customer Area before live acceptance. Penny testing uses a real banking app in live Customer Area; testing in test Customer Area is discouraged because transfers cannot be reversed and funds are deducted. Raw locators: `raw/adyen/docs/payment-methods/paynow/ios-drop-in/2026-09-15.md:29-58,64-94`. Canonical stem: `https://docs.adyen.com/payment-methods/paynow/ios-drop-in`.

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paynow-ios-drop-in]] → [[raw/adyen/docs/payment-methods/paynow/ios-drop-in/2026-09-15]].
