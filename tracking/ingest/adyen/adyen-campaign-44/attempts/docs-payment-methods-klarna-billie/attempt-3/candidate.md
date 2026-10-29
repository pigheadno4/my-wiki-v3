---
title: "Billie via Klarna | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/billie"
raw_files:
  - "adyen/docs/payment-methods/klarna/billie/2026-09-15.md"
tags: [adyen, billie, klarna, b2b, buy-now-pay-later]
---

## Overview

This 2026-09-15 Adyen Docs page describes **Billie via Klarna**, a B2B open-invoice/deferred-payment option offered through an Adyen Klarna integration. The page says Billie invoice payments can be immediately settled in full; that is a product description, not evidence of any particular merchant's settlement. Billie is not one of the consumer Klarna Pay later/Pay over time/Pay now choices. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-klarna]] and [[adyen]].

> [!warning] Payment-flow contradiction
> This Billie child page lists "Redirect, Inline widget" in its feature matrix (raw lines 27–29) and says the widget requires `paymentMethod.subtype: sdk` (lines 815–843). The linked Klarna overview lists only "Redirect" for Billie (B2B) (`raw/adyen/docs/payment-methods/klarna/2026-09-15.md`, line 36). Preserve both captured claims when selecting an integration flow; these pages do not establish whether the inline widget is currently available to a particular merchant.

## Key takeaways

- The feature matrix labels Billie BNPL with **redirect or inline widget**, broad "International" country and "Multiple" currency categories but does not enumerate an eligibility list. It marks **recurring unsupported** and marks refunds, partial/multiple partial refunds, separate/partial/multiple partial captures and chargebacks available. These icons are documentation claims, not proof that a specific merchant is configured or that a modification succeeded.
- Before adding Billie in **test Customer Area**, the guide requires a Klarna integration for the intended platform and integration type. Billie is an extension of that integration: use `paymentMethod.type: klarna_b2b` wherever the Klarna integration requires a method type. The `/payments` request must include `shopperName` and `company`; `company.name` is required, while `company.registrationNumber` is required outside DE and AT. The page also lists optional homepage, registry location, tax ID and company type fields. The DE/EUR example is a fixture, not a universal country/currency rule.
- The **default redirect** `/payments` response carries `resultCode: RedirectShopper` and an `action` for the shopper to complete the payment at Klarna. For the **inline widget**, include `paymentMethod.subtype: sdk`; its sample response is `Pending` with `paymentData` and client-token data to be used later with `/payments/details`. Neither initial response proves final authorization, capture, settlement or payout. The page does not provide the full returned-shopper/details or webhook result path; follow the relevant platform's Klarna guide for that flow.
- The sample curl `/payments` request has a trailing comma after `paymentMethod.type` before the object closes (raw lines 68–70), so the literal JSON block is malformed. Some language-library examples set subtype `sdk` even before the later text distinguishes widget from default redirect; select subtype according to the actual intended flow and its API/SDK reference.
- The page's `## Test and go live` section only says to test Billie in Customer Area with its sandbox, then routes to Web, iOS, Android and API-only Klarna guides. It gives no live-account approval or live-payment outcome.

## Detail locators

- B2B identity, Adyen/Klarna relationship and feature matrix including no recurring: raw lines 23–29.
- Klarna integration and test Customer Area prerequisites: `## Requirements`, lines 31–36.
- `klarna_b2b`, required `shopperName`/`company`, registration-number country exception and other company fields: `## Required fields`, lines 38–51.
- Versioned `/payments` request examples and malformed curl JSON: `## Payment request and response`, lines 53–782; curl lines 61–121, with trailing comma at line 69. Examples include TEST endpoint and DE/EUR values.
- Redirect `RedirectShopper`/action versus widget `Pending`/`paymentData`/client token: lines 784–843. The inline-widget requirement for `paymentMethod.subtype: sdk` is at lines 815–823.
- Sandbox statement and platform/integration chooser: lines 845–873. Child guides own implementation and outcome behavior.

## Related

- [[adyen-online-payments]] — provider online-payment context.
- [[source-adyen-docs-payment-methods-klarna]] — Klarna overview with a separate Billie (B2B) row.

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/billie/2026-09-15|2026-09-15 Billie via Klarna B2B overview and flow examples]]
