# Fixed retrieval checks: Bancontact Mobile overview

Canonical source stem: `source-adyen-docs-payment-methods-bancontact-bancontact-mobile`
Pinned raw: `raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/2026-09-15.md` (SHA-256 `4f48bbc37a09583cec8d63d24822a6eb9150567a6e3b93b0367c0b4c6485bbae`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-bancontact-bancontact-mobile.md`

## Q1 — What is this page for, and what should a reader not infer?

This is the captured Bancontact Mobile method overview: it describes a mobile/bank-app payment, mobile direct-app or desktop QR path, and a separate Bancontact card route (`raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/2026-09-15.md:15-27`). It gives a BE/EUR wallet capability matrix (`:29-33`) and integration navigation for Web, iOS, Android, API-only and Pay by Link (`:35-65`). It has a 2023-04-11 last-modified marker (`:11`), so its popularity and feature claims are historical page claims, not current merchant eligibility, app support, live settlement or successful payment proof. It provides no request fields, SDK/version prerequisites or outcome-handling steps.

## Q2 — What capabilities, prerequisites and warnings matter most?

The page's shopper path is app completion through Payconiq by Bancontact or another supporting bank app, with direct app routing on mobile or desktop QR scanning (`:25`); Bancontact card is distinct (`:27`). Its matrix says wallet, Redirect or Additional action, BE/EUR; recurring, refunds and partial refunds are marked supported, while separate/partial captures and chargebacks are marked unsupported (`:29-31`). The recurring footnote limits that mark to WIP (`:33`), so do not infer merchant WIP enrollment or an automatic recurring workflow. This overview points to Web/iOS/Android, API-only and Pay by Link guides for implementation (`:35-65`); it does not supply the platform details itself.
