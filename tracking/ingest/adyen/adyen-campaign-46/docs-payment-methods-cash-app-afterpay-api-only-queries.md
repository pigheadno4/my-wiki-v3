# Cash App Afterpay API-only retrieval checks

## Q1 — Identity and scope

Query: What is the Cash App Afterpay API-only guide for, and does it prove current merchant enablement or live success?

Expected route: `wiki/index.md` PSP Indexes line 10 → `wiki/adyen-index.md` line 2557 → `wiki/concepts/adyen-online-payments.md` Sources → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-api-only.md` Overview/Detail locators → `raw/adyen/docs/payment-methods/cash-app-afterpay/api-only/2026-09-15.md` lines 15–43 and 663–681. Expected answer: 2026-09-15-captured API-only custom form guide for Cash App Afterpay, with US/USD availability request, test Customer Area setup and live request gate; the snapshot alone does not prove current eligibility or execution.

## Q2 — Redirect, finality, capture and warning

Query: How does the Cash App Afterpay API-only redirect complete, what outcomes and capture conditions matter, and what caveat applies to its discount example?

Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-cash-app-afterpay-api-only.md` Key takeaways/Detail locators → `raw/adyen/docs/payment-methods/cash-app-afterpay/api-only/2026-09-15.md` `## Make a payment` lines 45–61 and 518–532, `## Handle the redirect` lines 534–573, `## Present the payment result` lines 575–593, `## Capture the payment` lines 595–614, `## Refunds and cancellations` lines 616–625, and `## Discounts` lines 627–661. Expected answer: server `/payments` with shopper/address/item data, redirect via response action.url, URL-decoded redirectResult to `/payments/details`; Pending/Received waits for AUTHORISATION webhook and missing shopper return also relies on webhook. Partial capture requires manual capture, 13-day production and one-day test capture deadlines, conditional remainder cancellation and Support-enabled multiple partial captures, cancel/refund boundary. Warning: USD 1 wording in the two-unit discount example is ambiguous between per-unit and line-total, and the JSON misses a comma.
