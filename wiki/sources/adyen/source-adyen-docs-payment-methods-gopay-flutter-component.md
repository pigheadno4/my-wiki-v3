---
title: "Adyen GoPay Flutter Components integration guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/gopay/flutter-component/2026-09-15.md"
tags: [adyen, gopay, flutter, components, redirect, tokenization, recurring]
---

## Overview

This 2026-09-15 Adyen guide adds GoPay to an existing Flutter Components integration in Sessions or Advanced server-side flow. It covers redirect prerequisites, request additions and distinct tokenized Subscription and CardOnFile routes. This method-specific guide relies on the main Flutter Components guides for the full integration and does not prove current merchant enablement or an executed payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- Sessions requires an existing Flutter Components Sessions flow, Checkout API v68 or later, `action.type: redirect` handling and GoPay added in Customer Area. Its `/sessions` table marks `shopperInteractionDevice` and `channel` as required additions. The prerequisite text says Sessions Components but links to an Advanced Drop-in URL; the payment-session and redirect links target Sessions Components. The table's `shopperInteractionDevice` link points to an `applicationInfo` child anchor while the example puts that field at top level. Its TEST `/v71/sessions` sample also renders the device data as malformed quoted object text and uses `channel: Flutter`, while the table lists Web/Android/iOS examples. Check endpoint-specific field placement and channel values; the snippet is not a validated request. No GoPay-specific Component configuration is stated.
- Advanced requires an existing Flutter Components Advanced flow, redirect handling and Customer Area setup. Its prerequisite text again says Components but links to Drop-in; the other Advanced links target Components. Its `/payments` table marks `paymentMethod.type: gopay_wallet`, `browserInfo` and applicable `channel` as required additions. The TEST `/v72/payments` sample represents `browserInfo` as malformed quoted object text and uses lowercase `channel: web` rather than the table's Web/Android/iOS examples. The sample `RedirectShopper`/`action.type: redirect` is an intermediate handoff, not authorization. No GoPay-specific Component configuration is stated.
- For token creation, the guide says an initial `/payments` request includes `storePaymentMethod: true`, shopper-unique `shopperReference` of at least three characters and `recurringProcessingModel`. After that payment has **settled**, a `recurring.token.created` webhook carries `storedPaymentMethodId`, shopper reference and the original PSP reference. The merchant server must receive recurring-token lifecycle events. This separate `/payments` token step is not established by the normal Sessions `/sessions` add-on, and a submitted request alone does not prove token creation.
- Later `Subscription` payments use the stored method ID, shopper reference, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription`. The guide gives `resultCode` for shopper display and a later `AUTHORISATION` webhook for final payment status. Subscription samples have blank currency, method type and return URL values, so they are not copy-ready or outcome evidence.
- `CardOnFile` reuse has a different challenge: redirect the shopper to GoPay to enter a PIN. Send stored method ID, shopper reference, `ContAuth` and `CardOnFile`; the `RedirectShopper` URL is intermediate. After return, call `/payments/details` with `redirectResult`, then use the `AUTHORISATION` webhook for final status. PIN entry, details response and webhook authorization remain distinct from capture or settlement.
- For TEST, the page directs merchants to Adyen Support. Before LIVE acceptance, submit a separate GoPay request in the live Customer Area. TEST snippets and Support links do not establish test-account readiness or live enablement.

## Detail locators

- Sessions prerequisites, table, example and no-extra-configuration: pinned raw lines 25–77.
- Initial token request and settlement-gated recurring webhook: pinned raw lines 79–100 and 441–462.
- Subscription fields, incomplete examples and webhook boundary: pinned raw lines 102–325 and 464–687.
- CardOnFile PIN challenge, redirect/details/webhook sequence: pinned raw lines 327–352 and 689–714.
- Advanced prerequisite link mismatch, request table, example and redirect response: pinned raw lines 362–439.
- TEST Support and LIVE Customer Area gates: pinned raw lines 354–360 and 716–722.

## Related

- [[adyen-online-payments]] — main provider concept and payment-state context
- [[adyen-tokenization]] — provider token and recurring lifecycle
- [[source-adyen-docs-payment-methods-gopay]] — method overview and separate eligibility/feature scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/flutter-component/2026-09-15|GoPay Flutter Components guide, 2026-09-15]]
