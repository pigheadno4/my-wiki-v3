# Fixed retrieval checks — Adyen supported payout currencies

## Q1 — What is this page for, what is its scope, and what should not be inferred?

This 2023-modified, 2026-09-15-captured Adyen page lists payout-currency and local/cross-border rail availability by acquiring connection, after an acquiring → settlement → payout explanation. It is not a universal payment-method or merchant-account enablement list, a guarantee of same-currency processing/settlement/payout, a merchant-specific FX quote, or proof of transfer or bank receipt. Retrieve through `[[adyen-currencies-and-fx]]` → `[[source-adyen-docs-account-supported-currencies]]` → `[[raw/adyen/docs/account/supported-currencies/2026-09-15]]`; raw lines 15–44 and regional tables 48–224. Canonical page: https://docs.adyen.com/account/supported-currencies.

## Q2 — What determines settlement and payout currency/rail, and what warnings matter?

The acquiring region and payment method determine settlement currency; Adyen bank location follows currency and acquiring entity, while the receiving-bank location determines whether local rails or SWIFT are used (raw lines 19–39). Configure a payout account per payout currency on the merchant account, and use the actual acquiring-connection region when the merchant country is absent (lines 42–44). The prose says BRL, INR, MYR, MXN and AED have no SWIFT payout (line 40), but EU/UK rows mark cross-border payout for MXN and AED (lines 123, 138, 154, 166). Preserve that unresolved conflict and verify current route/account eligibility; the tables do not establish a like-for-like currency or FX-free transaction. Route through the same concept→source→raw path and separately consult currency-code/contract FX guidance.
