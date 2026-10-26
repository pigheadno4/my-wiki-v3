---
title: "MobilePay Flutter Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/flutter-component/2026-09-15.md"
tags: [adyen, mobilepay, flutter, components, online-payments, payouts]
---

## Overview

This 2026-09-15 Adyen guide describes MobilePay additions to an existing Flutter Components integration, separately for Sessions and Advanced server-side flows. Both require redirect handling and MobilePay addition in Customer Area. A separate Advanced-flow section describes creating a token through a payment for future MobilePay-wallet payouts. It is a captured guide, not evidence of current enablement, a valid runnable example, or a completed payment or transfer. See [[adyen]], [[adyen-online-payments]], and [[adyen-payouts]].

## Key takeaways

- **Sessions:** The guide calls for an existing Flutter Components Sessions flow using Checkout API v68 or later, redirect handling for `action.type: redirect`, and MobilePay addition in Customer Area (raw lines 25–34). It says no MobilePay-specific `/sessions` parameters or Component configuration are needed (lines 36–46).
- **Advanced:** The existing Flutter Components Advanced flow likewise requires redirect handling and Customer Area setup (lines 83–99). No extra MobilePay configuration or `/payments` parameters are stated for a normal payment; payout-token creation is the explicit exception (lines 97–105).
- **Payout-token path:** After recurring lifecycle webhook setup, the guide instructs an Advanced `/payments` request with `telephoneNumber`, `shopperReference`, and a true payout flag; retain the webhook's `storedPaymentMethodId` against `shopperReference`, then send it as `counterparty.card.cardIdentification` in POST `/transfers` (lines 291–323). This is a token for future payouts, not proof that a payout completed. The guide calls this payout feature experimental and says token creation is supported only through `/payments` (lines 337–339).
- **Testing distinction:** For ordinary MobilePay payments, the page says they cannot be tested in Adyen's test environment and directs low-amount LIVE payments after a live Customer Area request, checking AUTHORISATION webhook and Payment list status (lines 48–58, 325–335). A separate experimental payout section gives a Vipps MobilePay test-app simulation and checks the token webhook plus Transfers API request (lines 60–81, 337–358). The two testing descriptions have different subjects and should not be conflated.
- **Source inconsistencies:** The prose spells the payout flag `enablePayout` (line 301), while the annotated curl example spells it `enablePayOut` (line 126); the parent MobilePay overview also uses `enablePayOut`. The guide's Flutter Components integration prerequisites link to URLs with `integration=Drop-in` in both flow tables (lines 31, 91). Its Advanced sample contains blank currency, payment-method type and return URL placeholders and a TEST endpoint (lines 109–128), despite the ordinary-payment live-only testing instruction; do not treat the snippet as a validated executable request or as proof of Adyen TEST support.

## Detail locators

- Sessions prerequisite, redirect, setup and no-extra-configuration sections: raw lines 25–46.
- Advanced prerequisites, normal-payment exception and language-specific example blocks: raw lines 83–289. The examples are not a single SDK/version compatibility statement.
- Payout webhook, request-field and transfer routes: raw lines 291–323. The example webhook carries a `recurring.token.created` event and `storedPaymentMethodId` (lines 303–320); it is a fixture, not an observed event.
- Payment versus payout test instructions: raw lines 48–81 and 325–358. Test app phone/NIN fixtures remain in the raw.

## Related

- [[adyen-online-payments]]
- [[adyen-payouts]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/flutter-component/2026-09-15|MobilePay Flutter Component, fetched 2026-09-15]]
