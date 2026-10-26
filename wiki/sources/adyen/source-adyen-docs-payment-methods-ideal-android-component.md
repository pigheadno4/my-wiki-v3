---
title: "iDEAL | Wero Android Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/android-component"
raw_files:
  - "adyen/docs/payment-methods/ideal/android-component/2026-09-15.md"
tags: [adyen, ideal, wero, android, components, online-payments, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds iDEAL | Wero to an existing Android Components integration, with distinct Sessions and Advanced server-side flows. It also documents a separate recurring path through SEPA Direct Debit tokens and conditional TEST/LIVE verification guidance. It is a documentation snapshot, not evidence of current merchant enablement, a working app or a completed payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Sessions:** The guide requires an existing Android Components Sessions integration using Checkout API v68 or later, redirect handling for `action.type: redirect`, and iDEAL | Wero addition in Customer Area (raw lines 25–36). It says there are no additional method-specific `/sessions` parameters or Component configuration (lines 38–42, 67–71).
- **Advanced:** The guide requires an existing Android Components Advanced integration, an additional redirect-action handler and Customer Area addition (lines 400–408). It says there is no additional method-specific Component configuration or ordinary `/payments` parameters (lines 433–437, 496–500). The v68-or-later Checkout API statement appears in the Sessions requirements; this page does not repeat it for Advanced.
- The native UI route imports `com.adyen.checkout:ideal`, adding `components-compose` for Jetpack Compose, then creates `IdealComponent` from a supported iDEAL payment method and attaches or displays it (Sessions lines 44–126; Advanced lines 410–494). `YOUR_VERSION` and other placeholders do not state an Android SDK version or prove the snippets run unchanged.
- **Recurring is a distinct SEPA Direct Debit route:** The page says iDEAL | Wero recurring payments use SEPA Direct Debit. It directs creating a shopper token with standard tokenization parameters, receiving `storedPaymentMethodId` in a `recurring.token.created` webhook, then using the token for shopper-not-present `UnscheduledCardOnFile` or `Subscription` payments (Sessions lines 128–155; repeated Advanced lines 502–529). The later `/payments` examples use `paymentMethod.type: sepadirectdebit`, `storedPaymentMethodId`, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription` (lines 157–353, 531–727). The recurring path is not an ordinary iDEAL redirect payment, and the subscription example does not demonstrate every processing model.
- The recurring request's `Received` response means it was received, with a `pspReference`; the page directs webhooks to track whether payment succeeded (lines 355–360, 729–734). It is not final authorization, capture or settlement. The Java recurring examples omit `shopperReference` while curl/PHP/Node/Python/Ruby include it (lines 157–353, 531–727); do not treat one sample as a complete cross-language schema.
- **Testing:** The page calls the iDEAL | Wero TEST environment unreliable and recommends live penny tests (lines 362–364, 736–738). A live test path requires a live issuer bank account, initiating an iDEAL payment, bank/QR selection and authorization, then checking live Customer Area status (lines 368–374, 742–748). If TEST is available, its payment page uses issuer `TESTNL2A` and simulated outcome codes, including expiration as `Pending` or `Received` (lines 376–398, 750–772). Those are test fixtures, not observed successful transactions. The “Request iDEAL | Wero for the live environment” headings have no substantive instructions in this pinned page (lines 366–368, 740–742); do not infer a specific approval step from the heading alone.

## Detail locators

- Sessions prerequisites, import and Component launch (Compose/non-Compose): raw lines 25–126.
- Sessions SEPA token creation, subsequent shopper-absent payment samples and webhook/result boundary: raw lines 128–360.
- Advanced prerequisites, import, launch and ordinary request boundary: raw lines 400–500.
- Advanced SEPA token route, samples and `Received`/webhook boundary: raw lines 502–734.
- TEST limitations, live penny-test procedure, conditional TEST simulation table: raw lines 362–398 and 736–772.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/android-component/2026-09-15|iDEAL | Wero Android Component, fetched 2026-09-15]]
