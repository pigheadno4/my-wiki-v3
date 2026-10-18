# C16 Platforms online currency-conversion hub retrieval checks

## Q1 — Purpose, scope, and inference boundary

Query: What does the Adyen for Platforms online currency-conversion hub establish, and does it prove current access, an FX quote, or a completed user settlement?

Expected route: `wiki/sources/adyen/source-adyen-docs-platforms-online-payments-currency-conversion.md` through the Adyen FX concept. Answer: the dated page introduces a limited-availability pilot in which API requests may accept a transaction in one currency and settle it in another for platform users and their customers. It does not provide current eligibility, supported currency pairs, rate/fee, request schema, balance-account allocation, or a transaction outcome. Raw locators: lines 15–26.

## Q2 — Capability, prerequisites, and warnings

Query: Where should a reader go for implementing payment versus refund conversion, and what can be inferred from this hub alone about each path?

Expected route: same source, then the separate `payments` and `refunds` child guides linked in its Next steps. Answer: the hub only distinguishes accepted and settled currencies and points to the two guides; it does not establish that a refund reuses the original payment's rate, fee, or split. Its 2023-modified, 2026-09-15-captured pilot statement must not be treated as current availability. Raw locators: lines 19–20, 24–36.
