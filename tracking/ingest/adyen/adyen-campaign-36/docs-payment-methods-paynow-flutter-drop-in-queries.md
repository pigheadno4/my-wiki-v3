# Retrieval checks — docs-payment-methods-paynow-flutter-drop-in

Q1. What does this PayNow Flutter Drop-in page cover, and what cannot be inferred?
Answer: It is a PayNow add-on to existing Flutter Drop-in, split into Sessions and Advanced sections (raw lines 17–25, 59–81). It does not provide a full QR lifecycle, webhook-final status or proof of merchant enablement/payment; the Advanced action is qrCode (raw line 68). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paynow-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/paynow/flutter-drop-in/2026-09-15]].

Q2. Which setup/version and real-funds warning must be retained?
Answer: Sessions states Checkout API v68+ and Support setup, though its integration-type hyperlink goes to an Advanced guide (raw lines 29–35). Advanced specifies qrCode action and Customer Area setup, with separate Support contact before live acceptance (raw lines 63–69, 83–85). The page describes LIVE small-amount tests with a real banking app and warns against TEST Customer Area tests because bank transfers cannot be reversed and funds are deducted (raw lines 51–57, 85–91). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paynow-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/paynow/flutter-drop-in/2026-09-15]].
