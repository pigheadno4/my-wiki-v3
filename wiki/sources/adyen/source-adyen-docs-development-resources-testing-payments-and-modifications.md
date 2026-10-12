---
title: "Testing payments and modifications | Adyen Docs"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/testing/payments-and-modifications"
raw_files:
  - "adyen/docs/development-resources/testing/payments-and-modifications/2026-09-15.md"
tags: [adyen, testing, online-payments, payment-modifications, webhooks]
---

## Overview

This Adyen documentation page is a test guide for checking whether an integration handles payments and payment modifications before going live. It routes test scenarios for ordinary payments, encrypted card details, third-party authentication data, captures, cancellations, refunds, reversals, authorization adjustments, and Level 2/3 data.

## Key takeaways

- Adyen recommends its test card numbers or supported alternative-payment-method test credentials and recommends starting each scenario with a test payment amount of **100**. These are test instructions, not evidence of a live payment or a universal production amount requirement.
- The ordinary payment check covers a conditional return to the merchant website or app after a redirect and receipt of the `AUTHORISATION` webhook on the server; the webhook carries payment status and should not be summarized as an automatic successful authorization.
- A single partial manual capture automatically cancels the remaining payment amount. Multiple partial manual capture is a separate scenario that requires Adyen Support to enable it.
- The failed-capture and failed-refund fixtures demonstrate that a later failure event can follow a successful `CAPTURE` or `REFUND` webhook. The guide says either failed-modification simulation can take up to 24 hours to finish.
- Cancellation testing is limited to authorized payments configured for delayed automatic capture or manual capture. The pre-authorization and adjustment test described here is limited to cards and Klarna, while the Level 2/3 scenario requires Support enablement for the relevant Customer Area setting.

> [!warning] Test evidence boundary
> The documented credentials, values, holder-name triggers, and expected events are simulation fixtures for exercising integration handling. This snapshot does not prove current production availability, merchant or payment-method eligibility, live authorization, capture, refund, settlement, or funding outcomes.

## Detail locators

- `## Payment` — conditional client return after redirect and server-side `AUTHORISATION` webhook receipt.
- `## Payment with encrypted card details` — server testing before the client integration is complete, using the `test_` prefix and a request example.
- `## Payment with third-party authentication data` — authorization-only test route and test payment details.
- `## Manual capture`, `## Partial manual capture`, and `## Multiple partial manual capture` — full and partial capture checks, `CAPTURE` webhooks, remaining-balance behavior, and enablement.
- `## Failed capture` and `## Failed refund` — holder-name fixtures, later failure webhooks, and the up-to-24-hour simulation timing.
- `## Cancel`, `## Full refund`, `## Partial refund`, `## Multiple partial refund`, and `## Reversal` — modification-specific action and webhook checks.
- `## Pre-authorization and adjustment` — cards-and-Klarna scope, recommended test amounts, and `AUTHORISATION` / `ADJUST_AUTHORISATION` events.
- `## Payment with level 2/3 data` — Support enablement, response-specific card fixtures, `additionalData`, and webhook check.

## Related

- Company: [[adyen]]
- Concept: [[adyen-payment-testing]]
- Related lifecycle concepts: [[adyen-payment-capture]], [[adyen-refunds]], [[adyen-authorization-adjustment]], and [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/development-resources/testing/payments-and-modifications/2026-09-15|2026-09-15 snapshot — Adyen payment and modification testing guide]]
