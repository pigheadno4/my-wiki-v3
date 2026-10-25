# Bank Transfer via KCP iOS chooser retrieval questions

## Q1 — What is this page's purpose and scope, and what cannot be inferred?

It is an **iOS navigation chooser** for Bank Transfer via KCP, linking method-specific Drop-in and Components pages (raw lines 15–27; [[source-adyen-docs-payment-methods-bank-transfer-kcp-ios]]). The Components label mentions `InstantPaymentComponent`, but the chooser does not specify its setup, a KCP method type, redirect handling, bank certificate requirements, current eligibility or final payment outcome. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bank-transfer-kcp-ios]] → [[raw/adyen/docs/payment-methods/bank-transfer-kcp/ios/2026-09-15]].

## Q2 — What prerequisite and flow options are visible?

The page instructs readers to create the **main integration before adding KCP bank transfer**, then links iOS Drop-in and iOS Components base guides for both Sessions and Advanced flows (raw lines 29–36). It does not state a Checkout API/SDK minimum, Customer Area setup, country/currency or TEST/live condition. Those require the relevant child/overview guide; links alone do not establish a successful transfer ([[source-adyen-docs-payment-methods-bank-transfer-kcp-ios]]). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bank-transfer-kcp-ios]] → [[raw/adyen/docs/payment-methods/bank-transfer-kcp/ios/2026-09-15]].
