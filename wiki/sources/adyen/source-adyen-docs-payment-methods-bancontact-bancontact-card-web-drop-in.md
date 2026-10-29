---
title: "Adyen Bancontact card Web Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/web-drop-in/2026-09-15.md"
tags: [adyen, bancontact, web, drop-in, online-payments]
---

## Overview

Adyen's guide for adding **Bancontact card** to an existing **Web Drop-in** integration. It covers both Sessions and Advanced server-side flows and requires Bancontact card added in the Customer Area. The page was last modified 2022-12-19 in the pinned capture, so its versioned options and examples are historical source evidence, not proof of current merchant enablement or live payment behavior. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Bancontact card is described as card-like, with no CVC for Bancontact (a co-badged card may still show the CVC field), mandatory 3D Secure authentication, and no separate captures. Web Drop-in collects card information and redirects the shopper for 3D Secure. See raw lines 19–27.
- The base Bancontact card API reference says there are **no additional fields** to send. It points to `/sessions` as the default with Drop-in v5.0.0+ and to `/payments` for additional use cases; choose the corresponding existing Web Drop-in flow. For v6, the page shows an `AdyenCheckout` import. See raw lines 29–60. These base-flow statements do not remove the separate fields required for optional tokenization.
- Optional `bcmc` configuration includes a cardholder-name field and requiredness (`holderNameRequired` also needs `hasHolderName`), a stored-details checkbox, brands, styling, billing-address controls and version-marked options. The example adds `bcmcConfiguration` under `paymentMethodsConfiguration.bcmc`. See raw lines 62–125.
- To put Bancontact card among other cards instead of showing it separately, the prose says to include `bcmc` in `blockedPaymentMethods` when making a `/sessions` or `/paymentMethods` request, then include `bcmc` in the `card` brands array. **Placement conflict:** the immediately following example puts `blockedPaymentMethods` in a client `configuration` object alongside `environment` and `clientKey`, while the prose names server requests. The example also has a stray closing `});`. Do not treat it as a validated copy-and-paste request or resolve placement from this source alone. See raw lines 128–159.
- Recurring payments are described through the **Bancontact Wallet Initiated Program (WIP)**, for which signup and eligibility are required and amount limits apply. The page strongly recommends explicit shopper permission; its WIP discussion says the first consented transaction uses SCA, subsequent transactions do not, and the issuer remains liable without a liability shift for the first transaction. Testing recurring payments needs Support configuration. See raw lines 161–189.
- For token creation, the `/sessions` or `/payments` request includes `storePaymentMethod: true` and a unique `shopperReference`. After the initial payment settles, a `recurring.token.created` webhook contains the `storedPaymentMethodId`. Future `/payments` pass that ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. The sample uses test `/payments` v72 and `bcmc`; it is not evidence that an account is WIP-enabled. See raw lines 191–240.
- The test table has co-badged card examples; one Bancontact/Visa test card can route to either method depending on payment-method setup. A `DECLINED` holder-name example illustrates a refusal. Live setup points to adding Bancontact card in the live Customer Area, without documenting a completed live transaction. See raw lines 557–590.

## Detail locators

- Method identity, 3DS/capture limitations and base Web integration: raw lines 15–60.
- Optional Drop-in settings and separate-versus-card-list configuration: raw lines 62–159.
- WIP eligibility, token lifecycle and conditional request fields: raw lines 161–240.
- Recurring request examples across server libraries: raw lines 220–555.
- Test cards, co-badge routing and live Customer Area link: raw lines 557–590.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/web-drop-in/2026-09-15|Bancontact card Web Drop-in documentation capture (2026-09-15)]]
