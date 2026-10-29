# Klarna invoice-line retrieval checks

## Q1 — What is the page's scope and what must not be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-invoice-lines]]` → `[[raw/adyen/docs/payment-methods/klarna/invoice-lines/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-klarna-invoice-lines`. Full pinned raw path: `raw/adyen/docs/payment-methods/klarna/invoice-lines/2026-09-15.md`. Raw lines 15–25 enumerate payment, partial capture/refund, discount and adjustment use cases. Request examples and webhooks do not prove successful capture, refund or a live account outcome.

## Q2 — What rules, exceptions and warnings distinguish the page?

Use the same root/provider/concept/source/raw route. Raw lines 27–45 require Klarna payment `lineItems`, total equal to `amount.value`, and listed item fields. Raw lines 83–189 specify partial `/captures` and `/refunds` fields and later CAPTURE/REFUND webhooks. Raw lines 204–355 present reduced item prices, a negative Discount line, and an Adyen-added discount fallback when `amount.value` is less than submitted line total; that fallback qualifies the ordinary matching rule. Raw lines 357–359 require all previously captured/refunded items in a pre-full-capture adjustment and scope it to Checkout API v70+. Raw lines 1063–1143 show `/amountUpdates` examples whose base order is SEK but updates are EUR and whose curl URLs have a space after `https:`; do not infer a validated cross-currency change.
