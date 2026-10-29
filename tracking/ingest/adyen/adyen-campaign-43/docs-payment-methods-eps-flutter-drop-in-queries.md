# Fixed retrieval checks: EPS Flutter Drop-in

Canonical source stem: `source-adyen-docs-payment-methods-eps-flutter-drop-in`
Pinned raw: `raw/adyen/docs/payment-methods/eps/flutter-drop-in/2026-09-15.md` (SHA-256 `4cd8776045017b1c463b1f41e4f30682a8a68f496eeecc00317106454e9640ab`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-eps-flutter-drop-in.md`

## Q1 — What is this page for, and what should a reader not infer?

It gives EPS-specific additions to an existing Flutter Drop-in integration in Sessions or Advanced flow (`raw/adyen/docs/payment-methods/eps/flutter-drop-in/2026-09-15.md:15-25`, `:97-105`). It covers redirect readiness (`:35`, `:106`), says no added ordinary request/configuration fields (`:40-48`, `:111-119`), and describes future recurring through SEPA Direct Debit (`:52-89`, `:123-160`). It does not by itself establish a complete Flutter checkout, current merchant EPS availability, successful payment or live recurring use. Live EPS still needs a live Customer Area request (`:166`).

## Q2 — What capabilities, prerequisites and warnings matter most?

Sessions calls for existing Flutter Drop-in Sessions flow, Checkout API v68+, `action.type=redirect` handling and contacting Support to add EPS (`:29-36`), but its integration-type link points to an Advanced-flow URL (`:33`) while its redirect link points to Sessions (`:35`). It calls for no EPS-specific `/sessions` fields or configuration (`:40-48`). Advanced requires an existing Advanced flow, redirect handling and EPS added in Customer Area (`:101-107`), and no extra configuration or ordinary `/payments` parameters (`:111-119`). The Advanced setup row links to add-payment-methods rather than the Sessions row's Support direction (`:36`, `:107`); the guide does not resolve that difference. For recurring, it strongly recommends shopper permission, uses `storePaymentMethod=true` and a shopper reference in `/payments`, waits until settlement for the `recurring.token.created` stored ID, then calls `/payments` with that ID, `ContAuth`, and Subscription or UnscheduledCardOnFile (`:52-89`, repeated `:123-160`). Test status is checked in test Customer Area and live EPS requires a request in live Customer Area (`:91-95`, `:162-166`).
