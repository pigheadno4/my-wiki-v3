# Fixed retrieval checks: EPS API-only

Canonical source stem: `source-adyen-docs-payment-methods-eps-api-only`
Pinned raw: `raw/adyen/docs/payment-methods/eps/api-only/2026-09-15.md` (SHA-256 `d7be45c6c36679e8920170556708cca9ad053ece06980896933a68de7d83a690`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-eps-api-only.md`

## Q1 — What is this page for, and what should a reader not infer?

It is the EPS-specific add-on for an existing Adyen API-only integration, including bank selection and redirect (`raw/adyen/docs/payment-methods/eps/api-only/2026-09-15.md:15-42`), AT/EUR method discovery (`:86-94`), issuer and return URL additions to `/payments` (`:385-391`), and optional future recurring payments through SEPA Direct Debit (`:393-430`). The base guide owns general redirect handling (`:23-29`). The captured test/live bank list (`:44-84`) and sample responses do not prove current issuer availability, merchant enablement, successful bank authorisation, or live recurring eligibility. The v72 URLs are samples (`:101`, `:435`), not stated minimum API versions.

## Q2 — What capabilities, prerequisites and warnings matter most?

Start from an existing API-only integration with redirect handling and EPS added in Customer Area (`:23-29`). Show the shopper banks and send their chosen issuer ID server-side (`:37-42`); use `countryCode=AT`, EUR and payment amount in `/paymentMethods` (`:86-94`), then `paymentMethod.type=eps`, `paymentMethod.issuer` and a `returnUrl` no longer than 1024 characters in `/payments` (`:385-391`). Test/live issuer sets differ (`:44-84`); the Dolomitenbank live-list ID conflicts with the response example ID (`:65`, `:375-376`), and the `/payments` prose example gives the name rather than an ID (`:390`). For future recurring payments, this page routes through SEPA Direct Debit, recommends explicit permission, requests `storePaymentMethod=true` and a shopper reference, then waits until settlement for `recurring.token.created` and its `storedPaymentMethodId` (`:393-416`). Future-payment prose names `storedPaymentMethodId`, `ContAuth`, and Subscription/UnscheduledCardOnFile (`:418-430`), while examples use `recurringDetailReference` (`:432-453`), so do not silently equate those fields. The `/paymentMethods` curl lacks a continuation before `-d` (`:101-106`); use the sample only after fixing its shell syntax. Live EPS also requires a live Customer Area request (`:736-740`).
