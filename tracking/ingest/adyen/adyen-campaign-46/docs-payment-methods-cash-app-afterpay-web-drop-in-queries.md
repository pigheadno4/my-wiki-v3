# Cash App Afterpay Web Drop-in retrieval checks

## Q1 — Identity and scope

Query: What does Adyen's Cash App Afterpay Web Drop-in guide cover, and can it establish current eligibility or live-payment success?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2557 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-web-drop-in.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/cash-app-afterpay/web-drop-in/2026-09-15.md` lines 15–42 and 1215–1305. Expected answer: a 2026-09-15-captured guide for adding Cash App Afterpay to existing Web Drop-in, with Sessions/Advanced request and lifecycle detail; the snapshot does not prove current account enablement or live execution.

## Q2 — Flow, conditions, and warning

Query: What request data and capture/refund conditions does this guide give for Cash App Afterpay Web Drop-in, and how should its discount sample be interpreted?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-web-drop-in.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/cash-app-afterpay/web-drop-in/2026-09-15.md` `## Requirements` lines 21–42, `## API reference` lines 44–61 and 745–819, `## Capture the payment` lines 1219–1238, `## Refunds and cancellations` lines 1240–1249, and `## Discounts` lines 1251–1285. Expected answer: existing Sessions or Advanced Web Drop-in plus Customer Area method setup; shopper identity/address and item fields marked required, phone optional; manual capture for partial capture, 13-day production and one-day test capture deadlines, conditional remainder cancellation and Support-enabled multiple partial captures; cancel before capture and refund after. Warning: the discount sample's USD 1 phrase is ambiguous between per-unit and line-total because it discounts two units by USD 1 each, and its JSON is missing a comma before the discount object. No current eligibility or live success follows from the sample.
