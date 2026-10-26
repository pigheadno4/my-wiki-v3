---
title: "Adyen TWINT iOS Component guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/ios-component"
raw_files:
  - "adyen/docs/payment-methods/twint/ios-component/2026-09-15.md"
tags: [adyen, twint, ios, components, redirect, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds TWINT to an existing iOS Components integration in Sessions or Advanced server-side flow. Sessions states Checkout API v68 or later; both flows require redirect handling. It initializes `TwintComponent` and gives conditional token creation and later-payment fields. The page does not provide a complete initial payment response, return/result sequence or proof of current enablement or successful payment. See [[adyen]], [[adyen-online-payments]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-twint]].

## Key takeaways

- Sessions requires an existing iOS Components Sessions integration, Checkout API v68+, `action.type: redirect` handling and TWINT added in Customer Area. It says no TWINT-specific `/sessions` parameters or configuration parameters. The Swift example finds `TwintPaymentMethod`, creates `TwintComponent`, assigns the session as delegate and presents it. The example passes a `twintConfiguration` object despite saying no additional TWINT parameters; this need not mean method-specific settings are required.
- Advanced requires an existing iOS Components Advanced integration, redirect handling and Customer Area setup. It says no TWINT-specific configuration or ordinary `/payments` additions. Its Swift example assigns `self` as Component delegate. The Advanced prerequisite text names Components, but its linked integration URL has `integration=Drop-in`; the redirect and payment-step links use Components. The page states no Advanced-specific Checkout API minimum.
- For a shopper token, the guide instructs `/payments` with `storePaymentMethod: true` and a unique `shopperReference` of at least three characters. Once details are stored, `recurring.token.created` carries `shopperReference`, initial payment `pspReference` as `eventId`, and `storedPaymentMethodId`; receiving the Recurring tokens life cycle webhook is needed. This source does not itself describe how shopper consent is collected or prove a token was created.
- Later server `/payments` with the token uses `paymentMethod.storedPaymentMethodId`, the same `shopperReference`, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`; `/listRecurringDetails` is listed as another token-ID source. These token fields are conditional and do not contradict the ordinary no-extra-parameter statements. The recurring material is repeated after both flow sections and again at the end, with no separate alternative outcome model; do not infer three distinct mechanisms.
- The page directs test-payment status checks to Customer Area and says to request TWINT in the live Customer Area before live acceptance. It does not establish market/currency availability, an executed redirect, authorization, capture or settlement; consult the TWINT overview and main integration guidance for those topics.

## Detail locators

- Sessions prerequisites, v68+, redirect, no extra fields/configuration and Swift Component: pinned raw lines 25–73.
- First token creation/reuse and test/live route: pinned raw lines 75–120.
- Advanced Components-label/Drop-in-link mismatch, redirect, ordinary no-extra-fields and Swift delegate: pinned raw lines 122–168.
- Advanced repeated token path and test/live: pinned raw lines 170–215; final duplicate token path: lines 217–254.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[adyen-tokenization]] — provider token lifecycle and later-payment context
- [[source-adyen-docs-payment-methods-twint]] — TWINT overview and market/capture context

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/ios-component/2026-09-15|TWINT iOS Component guide, 2026-09-15]]
