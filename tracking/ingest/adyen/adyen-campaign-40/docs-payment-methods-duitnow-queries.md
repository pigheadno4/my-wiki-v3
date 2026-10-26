# DuitNow overview retrieval checks

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-duitnow]]`.

## Q1. What is its purpose and scope, and what cannot be inferred?

The canonical stem `source-adyen-docs-payment-methods-duitnow` is an Adyen DuitNow QR payment overview, captured 2026-09-15 with 2025-01-28 last-modified metadata (`raw/adyen/docs/payment-methods/duitnow/2026-09-15.md:1-17,23-25`). The network-level alias transfer description does not mean Adyen offers alias-transfer integration, because the page limits Adyen's offering to QR-code payments (`:23-25`). Its capability table and child links cannot establish current merchant eligibility, payment success, pricing or settlement terms (`:21,27-49`).

## Q2. What are the central capability, prerequisites, and warnings?

The source says DuitNow is a Malaysian real-time network managed by PayNet, while Adyen only offers QR-code payments (`raw/adyen/docs/payment-methods/duitnow/2026-09-15.md:23-25`). Its row lists real-time/additional-action MY/MYR, marks refunds including partial and multiple partial supported, and marks recurring, capture variants and chargebacks unsupported (`:27-29`). Those are overview marks, not an account-level or transaction-outcome proof. Web, iOS and Android child pages are the listed prebuilt-UI routes (`:31-49`); the overview supplies no channel-specific SDK/API prerequisites or payment-result procedure. The adyen.com pricing and settlement link supplies no terms in this raw (`:19-21`).
