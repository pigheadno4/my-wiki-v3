# Classic raw 3D Secure response retrieval checks

Canonical route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-3d-secure.md` → `wiki/sources/adyen/source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-raw-3d-secure-responses.md` → `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/raw-3d-secure-responses/2026-09-15.md`.

## Q1 — purpose, scope, and what not to infer

This is a Customer Area lookup for raw 3DS1 and 3DS2 authentication responses in a Classic documentation path (`raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/raw-3d-secure-responses/2026-09-15.md:15–19`). Its metadata says last modified 2021-01-27 (`:11`). It distinguishes requested from challenged statuses; a raw authentication code does not prove payment authorization, capture, settlement, PSD2 compliance or liability shift. The page is no evidence of current 3DS1 availability or a new Classic integration route.

## Q2 — central capability, prerequisites, and warnings

The first lookup key is **stage**. At requested stage, 3DS1 `threeDOfferedResponse` reports enrollment/offering: `Y` means enrolled, not authenticated (`:21–32`). Requested-stage 3DS2 `threeDS2Result.transStatus` applies where `ChallengeShopper` was not received, with `Y` frictionless and additional `U/N/A/C/D/R/I` labels in the raw table (`:34–47`). At challenged stage, 3DS1 `threeDAuthenticatedResponse` reports authentication result, where `Y` means authenticated (`:49–61`); challenged-stage 3DS2 `transStatus` applies where `ChallengeShopper` was received, where `Y` means successful and the table lists `U/N/A/R` alternatives (`:63–73`). Matching the response field, stage and `ChallengeShopper` condition is necessary before interpreting a code. Use separate payment-result evidence for any financial outcome.
