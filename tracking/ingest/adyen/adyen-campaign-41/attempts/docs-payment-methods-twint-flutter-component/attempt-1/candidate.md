---
title: "Adyen TWINT Flutter Component guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/twint/flutter-component/2026-09-15.md"
tags: [adyen, twint, flutter, components, redirect, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds TWINT to an existing Flutter Components integration using Sessions or Advanced server-side flow. Sessions specifies Checkout API v68 or later; both flows require redirect handling and Customer Area setup. The page gives conditional shopper-token creation and `ContAuth` reuse fields, but no Flutter Component initialization code, complete initial-payment response or result procedure. It does not prove present enablement or a successful payment. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-twint]].

## Key takeaways

- The Sessions requirement names Flutter Components and Checkout API v68+, with `action.type: redirect` handling and TWINT added in Customer Area. It says no ordinary TWINT-specific `/sessions` parameters or configuration parameters. However, its prerequisite link points to an **Advanced Flutter Drop-in** integration, while its redirect/session links point to Sessions Components. The text and linked routes conflict; the wrong link does not change the stated Sessions Components scope. No Flutter SDK version is pinned.
- Advanced likewise names Flutter Components, requires redirect handling and Customer Area setup, and says no ordinary TWINT-specific configuration or `/payments` additions. Its prerequisite link also points to Advanced Flutter Drop-in, while its action/payment-step links point to Advanced Components. The page states no Advanced-specific Checkout API minimum.
- For token creation in either flow, the guide instructs `/payments` with `storePaymentMethod: true` and a unique `shopperReference` of at least three characters. After details are stored, `recurring.token.created` carries `shopperReference`, initial payment `pspReference` as `eventId`, and `storedPaymentMethodId`; the server must receive the Recurring tokens life cycle webhook. This page does not describe collection of shopper consent or prove a token has been created.
- Later `/payments` using the token needs `paymentMethod.storedPaymentMethodId`, the same `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`; `/listRecurringDetails` is named as another way to get the stored ID. The token fields are conditional and do not contradict the no-extra-fields statements for ordinary payments. The page repeats this same route in both flow sections, without a separate Flutter-specific reuse sequence or outcome evidence.
- The test sections direct payment-status checks to Customer Area and say a live Customer Area request is needed before accepting TWINT. Market/currency, shopper handoff, final authorization, capture and settlement are not established by this method add-on.

## Detail locators

- Sessions Components/Advanced Drop-in link mismatch, v68+, redirect and setup: pinned raw lines 25–34.
- Sessions no-extra-fields/configuration and token create/reuse: pinned raw lines 36–87; test/live: lines 89–93.
- Advanced Components/Drop-in link mismatch, redirect, no-extra-fields/configuration: pinned raw lines 95–117.
- Advanced repeated token route and test/live: pinned raw lines 119–164.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[adyen-tokenization]] — provider token lifecycle and recurring scopes
- [[source-adyen-docs-payment-methods-twint]] — method overview and market/capture context

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/flutter-component/2026-09-15|TWINT Flutter Component guide, 2026-09-15]]
