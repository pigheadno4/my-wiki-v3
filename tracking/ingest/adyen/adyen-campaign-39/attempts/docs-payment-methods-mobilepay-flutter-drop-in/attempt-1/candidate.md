---
title: "MobilePay Flutter Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/flutter-drop-in/2026-09-15.md"
tags: [adyen, mobilepay, flutter, drop-in, redirect, payouts]
---

## Overview

This 2026-09-15 MobilePay page gives method-specific additions to an existing Flutter Drop-in integration, separated by Sessions and Advanced server-side flows. It also describes an experimental, separate `/payments` path that creates a token for future payouts to MobilePay wallets. The snapshot is integration guidance, not current enablement or an observed payment or payout. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** the requirement text names an existing Sessions Flutter Drop-in flow, Checkout API v68 or later, `action.type: redirect` handling, and MobilePay added in Customer Area. It says no MobilePay-specific `/sessions` fields or configuration. The Sessions integration-type row links to an **Advanced-flow** Flutter Drop-in page, while the session creation and redirect links point to Sessions; retain the label/link mismatch. (raw lines 25–48)
- **Advanced normal payment:** requires an existing Advanced Flutter Drop-in flow, redirect handling, and MobilePay added in Customer Area. It says no method-specific configuration or ordinary `/payments` parameters. The page does not state the Sessions v68+ minimum for this Advanced section. (raw lines 85–107)
- **Normal payment test and live gate:** the guide says ordinary MobilePay payments cannot be tested in the test environment. It directs a live Customer Area request, then low-amount live payments with an `AUTHORISATION` webhook received by the merchant server and status checked in the live payment list. These steps are instructions, not proof of an executed payment. (raw lines 50–60, 327–337)
- **Experimental payout-token path:** only `/payments` supports the described MobilePay wallet payout feature. To create a token for future payouts, the prose requires a recurring lifecycle webhook and `telephoneNumber`, `shopperReference`, and `enablePayout: true` on a payment. On `recurring.token.created`, save `storedPaymentMethodId` against `shopperReference`; a later `/transfers` request places the token in `counterparty.card.cardIdentification`. The test-app instructions for this payout path are separate from the live-only normal-payment testing statement and do not establish that a test payout succeeded. (raw lines 62–83, 293–325, 339–360)
- **Sample limits:** the payout-oriented curl sample has empty currency, payment-method type and return URL values, literal hint markup in JSON property names, and `enablePayOut` spelling, while the procedural text says `enablePayout`. Other language samples also leave core values blank and omit some token parameters. Use the prose and linked API references as navigation; the snippets are not complete or internally consistent executable requests. (raw lines 109–290, 299–305)

## Detail locators

- Sessions requirement/link conflict, no extra fields or configuration: raw lines 29–48.
- Advanced prerequisites and ordinary payment boundary: raw lines 89–107.
- Payout sample defects and prose/token webhook/transfer flow: raw lines 109–325.
- Normal live-payment instructions versus test-app payout instructions: raw lines 50–83 and 327–360.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/flutter-drop-in/2026-09-15|MobilePay Flutter Drop-in guide, 2026-09-15 snapshot]]
