---
title: "Adyen Error Codes and Messages"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/error-codes"
raw_files:
  - "adyen/docs/development-resources/error-codes/2026-09-15.md"
tags: [adyen, online-payments, api, error-handling]
---

## Overview

This Adyen development-resources snapshot is a diagnostic catalog for API errors in an online-payments integration. It identifies generic codes that any integration can receive and codes tied to Checkout, 3DS2, Amazon Pay, Apple Pay, Google Pay, and network tokens. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- For the page's described error response, a non-`2xx` HTTP status accompanies `errorCode` and `message`; its example also illustrates `status`, `errorType`, and `pspReference`. The example is illustrative, not a promise that every response has every field. Use [[source-adyen-docs-development-resources-response-handling]] for HTTP request handling and payment-outcome boundaries.
- Look up the exact code and message in the relevant section. Several codes have more than one possible cause, including generic `000` and `905`; a code alone does not uniquely diagnose the request or merchant configuration. The catalog's causes and solutions are scoped to their particular code, flow, or payment method.
- Consequential split warning: under generic `185`, an invalid or missing `splitPayment` in `additionalData` can leave a modification without a valid split even when the payment goes through. Do not infer that payment success proves the split was applied.
- Idempotency warning: generic `703` describes an unavailable comparison data store and suggests retrying later or omitting the `idempotency-key` header. Omitting the header removes that request's idempotency guard; consult [[adyen-api-idempotency]] for the retry boundary. Generic `704` covers an already processed or in-progress request, while `705` is rate limiting.
- Checkout `14_0475` says a MOTO payment cannot be processed until that integration's PCI compliance has been validated; the page directs the merchant to Adyen Support. Checkout `14_0493` states that UPI Collect transactions on Android are no longer supported and directs use of UPI Intent or UPI QR. These are code-specific snapshot statements, not proof of current merchant enablement.
- 3DS2 `15_023` flags a likely deprecated-flow combination of `threeDS2RequestData` and `threeDS2InMDFlow`; the page says to remove the object or use the native flow rather than rely on redirect.

## Detail locators

- Purpose, online-payments requirement, example error response, and field descriptions: lines 15–48.
- Generic code catalog and code-specific cause/solution entries: `## Generic error codes`, lines 50–1258; `185` split behavior at lines 588–595; `703`–`705` at lines 816–833; `905` configuration variants at lines 943–1026.
- Checkout code catalog: `## Checkout error codes`, lines 1259–1887; channel-specific `returnUrl` diagnosis at `14_0391`, lines 1458–1468; authentication-only `14_0392` at lines 1472–1474; MOTO PCI block `14_0475` at lines 1790–1810; Android UPI Collect `14_0493` at line 1882.
- 3DS2 code catalog: `## 3DS2 error codes`, lines 1888–2000; `15_023` deprecated-flow warning at lines 1980–1983.
- Payment-method and token catalogs: Amazon Pay lines 2001–2068, Apple Pay lines 2069–2121, Google Pay lines 2122–2146, and network tokens lines 2147–2204.

## Related

- [[adyen]] — provider context.
- [[adyen-online-payments]] — online-payments concept and reciprocal source route.
- [[adyen-api-idempotency]] — qualified retry and duplicate-request handling for `703` and `704`.
- [[source-adyen-docs-development-resources-response-handling]] — HTTP status and error-field interpretation.

## Raw Sources

- [[raw/adyen/docs/development-resources/error-codes/2026-09-15|Adyen error codes and messages (2026-09-15)]]
