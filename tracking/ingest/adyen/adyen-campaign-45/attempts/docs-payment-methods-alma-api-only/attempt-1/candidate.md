---
title: "Adyen Alma API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/api-only"
raw_files:
  - "adyen/docs/payment-methods/alma/api-only/2026-09-15.md"
tags: [adyen, alma, api-only, redirect, installments]
---

## Overview

This 2026-09-15 Adyen Docs page describes Alma-specific additions to an **existing Web API-only Advanced-flow** integration. The merchant builds the payment form, adds Alma in Customer Area, and handles a redirect action. Its FR/EUR method-discovery request is a documented selection condition, not proof that Alma is currently enabled for a particular merchant or that a payment has completed. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The shopper chooses Alma and enters details in the merchant-built form. The page says no additional form fields are required for Alma. It directs an existing API-only flow to handle `action.type: redirect`, rather than supplying the full base integration or a final result flow (pinned raw lines 23–42).
- For `/paymentMethods`, the table specifies `countryCode: FR` and `amount.currency: EUR` to include Alma; the test response illustrates `type: alma`. This is a method-discovery example, not a guarantee of method availability across accounts or amounts (lines 44–83).
- The `/payments` add-on table lists telephone number, shopper email, billing and delivery addresses and `additionalData.alma.installments_count`; none has a required mark. Set installments count to `3` or `4` to determine the shopper's installment count, or omit it to let the shopper choose. The test request illustrates four installments and returns a redirect action with `RedirectShopper`, which is a handoff, not final authorization or capture (lines 85–151).
- The guide points to Customer Area for test-payment status and says a live Customer Area request for Alma is needed before live acceptance. It gives no Alma-specific capture, refund or cancellation procedure (lines 153–161).

> [!warning] Request example and prose gaps
> The “How it works” step says to include information about purchased items in the payment request (raw line 35), but the add-on field table and `/payments` example show no item field (lines 85–135). The example also omits a `paymentMethod` object even though it is presented as an Alma request and followed by an Alma redirect response (lines 99–150). Both curl examples put `-X POST` on a line without a continuation before `-d` (lines 60–61 and 104–105). The `/payments` example uses FR/EUR with `shopperLocale: en-US` and four-character French postal codes `2000` (lines 106–129); verify these examples against the intended request and base integration before use. The page does not resolve the omissions.

## Detail locators

- Existing API-only prerequisites and merchant-built form: pinned raw lines 15–42.
- FR/EUR method discovery and example: lines 44–83.
- Payment add-on table, four-installment example and redirect response: lines 85–151.
- Test status and live request: lines 153–161.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-alma]] — Alma method overview for product and capability scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/api-only/2026-09-15|Alma API-only guide, captured 2026-09-15]]
