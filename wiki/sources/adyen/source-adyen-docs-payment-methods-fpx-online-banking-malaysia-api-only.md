---
title: "FPX Online Banking Malaysia for API only"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/api-only"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/api-only/2026-09-15.md"
tags: [adyen, fpx, malaysia, online-banking, api-only]
---

## Overview

Adyen's 2026-09-15 FPX Online Banking Malaysia API-only guide adds bank selection and redirect payment to an existing **Web API-only Advanced-flow** integration. It documents MY/MYR method discovery, FPX issuer IDs and a server payment request, with the base integration handling the redirect. The snapshot does not prove current bank availability, merchant eligibility or a completed transfer. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Prerequisites and discovery:** The page requires an existing API-only integration with `action.type: redirect` handling and FPX added in Customer Area. `/paymentMethods` discovery uses `countryCode: MY` and `amount.currency: MYR`; the example response type is `molpay_ebanking_fpx_MY` with `issuers`. Examples use Checkout v72 TEST and `shopperLocale: my-MY`, but example availability is not merchant enablement proof. [Raw lines 23–29, 71–99, 356–374]
- **Bank selection:** The merchant-built form must show the bank list; the selected bank's Issuer ID passes to the server for payment. The page says all listed issuers must be included on checkout to comply with PayNet local regulations. Its list names 18 banks and IDs; refer to raw lines 42–67 for the exact snapshot list rather than treating it as a current bank roster. [Raw lines 38–69]
- **Request conflict:** Most examples use `paymentMethod.type: molpay_ebanking_fpx_MY` plus `issuer` (for example `fpx_abb`), MYR amount, reference, return URL and merchant account. The page nevertheless says no additional `/payments` parameters are needed, and its “how it works” step mentions purchased-item information that is absent from the examples. The PHP example also sets type `fpx_MY`, unlike discovery and most other examples. Preserve these prose/example/type differences; do not infer an item schema or silently normalize the PHP type. [Raw lines 31–36, 376–403, 465–476, 545–557, 617–629]
- **Redirect and environments:** An example `/payments` response has `RedirectShopper` and `action.type: redirect`; the existing API-only flow handles the action. The testing section suggests using available issuer IDs to exercise different test results and checking Customer Area, but calls this an “Online banking Malaysia Component” despite this being an API-only page. Live acceptance requires a request in the live Customer Area. A redirect, issuer selection, shopper return, or test request is not final authorization, capture or settlement. [Raw lines 703–725]

## Detail locators

- Complete request examples and SDK-specific variants: discovery raw lines 80–354; payment raw lines 380–701. The example response includes a JavaScript-style comment inside a JSON fence, so it is illustrative rather than strict JSON. [Raw lines 356–374]
- No FPX-specific final result-code/webhook sequence, expiry, retry, tokenization, cancellation or refund route is defined here; use separately read outcome authority before asserting those behaviors.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/api-only/2026-09-15|FPX Online Banking Malaysia API only (2026-09-15)]]
