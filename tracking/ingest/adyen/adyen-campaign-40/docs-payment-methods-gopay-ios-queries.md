# Q1 — Purpose, scope and limits

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-ios-sdk.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gopay-ios.md` → pinned raw.

This 2026-09-15 GoPay iOS page is an integration chooser. It routes to iOS Drop-in and Components child guides, then lists their Sessions and Advanced base guides (raw `adyen/docs/payment-methods/gopay/ios/2026-09-15.md:15-36`). It does not itself establish country/currency request fields, redirect or recurring steps, SDK/API minimums, current method eligibility or a successful transaction. Those require the selected child/base guide, rather than inference from a navigation label (raw lines 19-36).

# Q2 — Central capability, prerequisites and warnings

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-ios-sdk.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gopay-ios.md`. Online-payment retrieval can also route through `wiki/concepts/adyen-online-payments.md`.

Use the Drop-in child for the all-in-one iOS UI route or the Components child for `InstantPaymentComponent` (raw `adyen/docs/payment-methods/gopay/ios/2026-09-15.md:19-27`). The page says to create the main integration first and links iOS Drop-in/Components Sessions and Advanced base guides (raw lines 29-36). It supplies no method-specific request, test, redirect, token, webhook or result instructions, so the chooser must not be treated as payment-operation proof (raw lines 15-36). Source stem: `source-adyen-docs-payment-methods-gopay-ios`.
