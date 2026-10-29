# docs-payment-methods-pix-ios-drop-in retrieval checks

## Q1 — Integration scope and fields

Query: What does Pix iOS Drop-in add in Sessions versus Advanced, and which fields are required or advisory?

Expected: This dated add-on is for existing iOS Drop-in, not a standalone integration. Sessions requires Checkout API v68+, method setup and amount in /sessions; shopperName, CPF/CNPJ socialSecurityNumber, shopperStatement up to 140 characters and line-item fields are listed without required marks (raw lines 25–49). The BR/BRL sample includes app returnUrl and an old 2021 sessionValidity, not reusable values (lines 51–90). Advanced requires qrCode action handling and setup; paymentMethod and amount are marked required, other listed fields optional, with shopperName plus socialSecurityNumber advised (lines 535–570). Advanced supplied shopperStatement must be under 60 characters and sessionValidity default is 1 hour through Checkout v71 or 24 hours from v72 (lines 565–566); these differ from the Sessions table. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-pix-ios-drop-in]] → [[raw/adyen/docs/payment-methods/pix/ios-drop-in/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/pix/ios-drop-in/2026-09-15.md`, heading line 15.

## Q2 — QR, expiry and lifecycle

Query: Does a Pix qrCode response mean the iOS Drop-in payment is paid, and what testing/refund/live limits are stated?

Expected: The Advanced example returns resultCode Pending with action.type qrCode and additionalData pix.expirationDate (raw lines 1058–1078); QR display and the payment expiration value do not prove paid/final status or define a separate display timer. The page calls Pix asynchronous and documents test Customer Area offer promotion to sale, Payment list and reconciliation testing (lines 520–533, 1088–1101). Refund is described within 90 days after payment (lines 514–516, 1082–1084), and live acceptance requires a Pix request in live Customer Area (lines 533 and 1101). Warn that the Advanced table uses onSubmit/state.data wording in an iOS guide (line 561), its qrCode action link points to handle-the-redirect (line 544), and sample sessionValidity dates precede the captured page (lines 70, 600). These instructions are not proof of performed operations. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-pix-ios-drop-in]] → [[raw/adyen/docs/payment-methods/pix/ios-drop-in/2026-09-15]]. Full pinned raw: `raw/adyen/docs/payment-methods/pix/ios-drop-in/2026-09-15.md`.
