# Walley overview retrieval checks

## Q1 — What is Walley's scope here, and what cannot be inferred?

Route `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-walley]]` → `[[raw/adyen/docs/payment-methods/walley/2026-09-15]]`. Canonical source stem: `source-adyen-docs-payment-methods-walley`. Full pinned raw path: `raw/adyen/docs/payment-methods/walley/2026-09-15.md`. Raw lines 23–28 identify Nordic Walley B2C `walley` and B2B `walley_b2b` redirect rows. The 2024-modified, 2026-captured overview does not prove current merchant eligibility, account enablement, a country/currency pairing beyond explicit limits, or payment success.

## Q2 — What regional, capture and capability limits matter?

Use the same root/provider/concept/source/raw route. Raw lines 27–28 list B2C DK/FI/NO/SE and DKK/EUR/NOK/SEK versus B2B FI/NO/SE and EUR/NOK/SEK. Line 32 explicitly restricts Denmark **or DKK** to B2C; line 30 requires capture of authorised payments within 90 days. The matrix marks recurring and multiple partial refunds unavailable while marking refunds, partial refunds, separate/partial/multiple partial captures and chargebacks available (lines 25–28). These are overview flags; raw lines 34–58 route Web, iOS, Android and API-only child guides for implementation details.
