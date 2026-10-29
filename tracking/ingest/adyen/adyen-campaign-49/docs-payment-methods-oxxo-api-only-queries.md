# Fixed queries — OXXO API-only

## Q1 — purpose, scope and limits

**Query:** What does the captured OXXO API-only guide cover, and what does an issued voucher establish?

**Expected answer:** The page at `https://docs.adyen.com/payment-methods/oxxo/api-only` is a 2026-09-15-captured API-only add-on for OXXO method discovery, voucher-action presentation, offline offer-to-sale webhooks, test promotion and live setup. An issued voucher is an **Open** offer, not proof of shopper payment or a completed live transaction. The method overview `wiki/sources/adyen/source-adyen-docs-payment-methods-oxxo.md` adds Mexican cash-payment, unpaid-expiry and capability context (full pinned `raw/adyen/docs/payment-methods/oxxo/api-only/2026-09-15.md`, `# OXXO for API only` lines 15–21; `## Requirements` lines 23–29). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-oxxo-api-only.md`.

## Q2 — discovery, conflicting fields and finality

**Query:** What OXXO API-only request/setup and status steps does the captured guide give, and how should its conflicting field instructions be handled?

**Expected answer:** Existing API-only Advanced flow, voucher-action handling, and OXXO Customer Area addition are prerequisites (pinned `raw/adyen/docs/payment-methods/oxxo/api-only/2026-09-15.md`, `## Requirements` lines 23–29). `/paymentMethods` discovery uses `countryCode: MX` and `amount.currency: MXN`; sample method type is `oxxo` (lines 46–85). The dedicated form and `/payments` sections say no shopper information or additional OXXO request fields are needed, and the response voucher must be shown (lines 38–44, 87–91). **Conflict:** the `How it works` list says shoppers enter details and requests include item information (lines 34–35); it does not identify required fields, so verify rather than invent them. The sample curl command lacks a continuation after `-X POST` before `-d` (lines 57–72). Voucher creation is an Open offer; optional OXXO PENDING webhook reports pending, while in-store payment changes it to Received sale and the final result arrives in AUTHORISATION webhook (lines 93–101). Test promotion simulates payment, and live acceptance requires a live Customer Area request (lines 103–114). Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-oxxo-api-only.md`.
