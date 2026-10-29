# Multibanco iOS Drop-in retrieval checks

## Q1 — What does the captured iOS Drop-in guide add to Sessions and Advanced flows?
Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco-ios-drop-in.md` → `raw/adyen/docs/payment-methods/multibanco/ios-drop-in/2026-09-15.md`.
Expected answer: this is a supplement to existing iOS Drop-in integration. Sessions requires Checkout API v68+ and Customer Area method setup but no extra Multibanco `/sessions` parameters or configuration. Advanced requires voucher-action handling and Customer Area setup but no extra method-specific `/payments` parameters or configuration. The page does not state an Advanced-specific API minimum. Raw locators: lines 19–46 and 67–89. Route voucher-contents and PT/EUR claims to approved `wiki/sources/adyen/source-adyen-docs-payment-methods-multibanco.md`, not solely this child guide.

## Q2 — How are test payments simulated, and what must happen before live acceptance?
Expected route: same root/provider/concept/source/raw chain.
Expected answer: submit a test Customer Area request for Multibanco. A pending Multibanco offer can be selected by PSP reference under Payments > Offers and manually promoted to sale in the test environment; paid/promoted test offers appear in Payment list, and this can exercise reconciliation. Submit a separate request in live Customer Area before live acceptance. The Advanced flow handles a voucher action; voucher display or a pending offer is not payment completion. Raw locators: lines 48–65, 75–76, 91–108; approved overview raw lines 23–32 for later shopper payment via ATM/online banking. Do not present test promotion as a live payment or capture recipe.
