---
title: "FPX Online Banking Malaysia Android Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/android-component"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/android-component/2026-09-15.md"
tags: [adyen, fpx, malaysia, android, components, online-banking]
---

## Overview

Adyen's 2026-09-15 FPX Online Banking Malaysia Android Component page gives method-specific additions for existing Android Components Sessions and Advanced flows. It uses `InstantPaymentComponent` for `molpay_ebanking_fpx_MY` and relies on the base integration for redirect and result handling. The snapshot does not prove current issuer availability, merchant eligibility or a completed bank payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Requires an existing Android Components Sessions flow, Checkout API v68 or later, `action.type: redirect` handling, and FPX added in Customer Area. The page says no FPX-specific `/sessions` fields or Component configuration are needed. Import the `instant` module; Compose also imports `components-compose`. The examples get `molpay_ebanking_fpx_MY` from the checkout session and launch `InstantPaymentComponent`. [Raw lines 25–125]
- **Advanced:** Requires an existing Android Components Advanced flow, handling the additional redirect action, and FPX added in Customer Area. The examples take the `molpay_ebanking_fpx_MY` method from the `/paymentMethods` response and launch `InstantPaymentComponent`; the page says no extra FPX-specific configuration or ordinary `/payments` fields are needed. This method-specific add-on does not spell out the complete base payment request or issuer selection payload. [Raw lines 136–236]
- **Issuer/test/live scope:** The test section says to use any issuer ID available for this Online Banking Malaysia Component in the relevant country/region to exercise different test results, then check the test payment list. A live Customer Area request precedes live acceptance. Issuer ID availability and a test result are not proof of present bank enablement or live authorization. [Raw lines 128–134, 238–244]

## Detail locators

- Compose/non-Compose launch examples and provider calls: raw lines 73–125 and 175–230. The Compose snippets say their unique key creates a new Component for a different screen/session and should change on reset; these are example lifecycle instructions, not a payment result. [Raw lines 97–99, 200–202]
- The page gives no current bank list, country/currency discovery table, expiry, refund/cancel behavior or FPX-specific final webhook sequence. The separate API-only guide documents explicit issuer selection for its merchant-built form; do not project that API-only implementation detail onto this Component page without its base-flow evidence.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-api-only]] — separate API-only form and issuer guide; route only for comparison.

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/android-component/2026-09-15|FPX Malaysia Android Component (2026-09-15)]]
