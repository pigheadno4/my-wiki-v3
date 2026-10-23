---
title: "Card Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/web-component"
raw_files:
  - "adyen/docs/payment-methods/cards/web-component/2026-09-15.md"
tags: [adyen, cards, web-components, sessions-flow, advanced-flow, tokenization]
---

## Overview

This [[adyen]] Card Component guide, last modified in 2022 and captured 2026-09-15, describes adding a card form to an **existing Web Components integration**. It branches by server-side Sessions versus Advanced flow and by Web Component version. It is a card-specific source under [[adyen-online-payments]], not a complete payment, 3DS, PCI or live-enablement implementation.

## Key takeaways

- Both flow tabs require a prior Web Components integration of the selected flow and cards added in Customer Area. The guide says no extra API fields are needed merely for cards: Sessions generally uses `/sessions` with Components v5.0.0 or later, while `/payments` is for the additional Advanced use cases. Specific features have their own parameters.
- Web Components v6 imports `AdyenCheckout` and `Card` and constructs `new Card(checkout, ...)`; v5.x.x or earlier uses `checkout.create('card', ...)`. Mounting renders the form. Optional fields and events are version- and condition-dependent: holder name must be shown before it can be required; partial billing address depends on `billingAddressRequired`; address lookup (v5.45.0+) requires full billing address and an external API. `onConfigSuccess` means card fields are ready, whereas `onSubmit` concerns valid client input and is not payment authorization.
- Brand recognition attempts to render an icon and CVC form; co-badged cards have a shopper brand-choice path. Separate debit/credit forms depend on `splitCardFundingSources: true` in **Sessions `/sessions`** or **Advanced `/paymentMethods`**, plus returned `fundingSource` objects. The source specifically calls for debit-first, clearly labeled presentation when accepting payments in Sweden; that is dated source guidance, not a current legal determination.
- Card tokenization covers one-click, subscription and unscheduled card-on-file examples. The page strongly recommends explicit shopper permission for future recurring payments. Sessions examples use `/sessions` and a token-created webhook; Checkout API v69 or earlier instead uses the `enableStoreDetails` checkbox. Advanced token creation uses `/payments` plus the checkbox and receives `recurring.token.created` with `storedPaymentMethodId`. Advanced stored-card display uses the checkout instance's stored methods and valid `onSubmit` state sent to the server. The examples are test-environment illustrations, not token creation or payment success evidence.
- Before live card payments, the page calls for test cards, adding wanted cards in live Customer Area, assessing PCI DSS compliance and submitting the required SAQ A. For v5.20.0+ JSON Web Encryption card fields it requires a secure local or HTTPS test context in allowed origins. A rendered form, valid field, created session, token request or example API call does not prove 3DS authentication, authorization, capture or settlement.

## Source-specific cautions

- The Advanced stored-card mount example contains `});.mount('#stored-card');` (raw line 1461), which is malformed as shown. Address-lookup examples also use assignment syntax inside object literals and the two-request selection example resolves `mappedData` without defining it in the snippet (raw lines 225–303). Treat these as illustrative locators requiring implementation verification.
- The Advanced token-creation examples use test-only `test_` encrypted-card placeholders and mixed language-library versions; they do not show safe handling of real card data. The page does not specify a 3DS challenge or server-side result/webhook outcome procedure for an actual card payment.

## Detail locators

- [[raw/adyen/docs/payment-methods/cards/web-component/2026-09-15|Pinned raw]], lines 15–54: purpose, flow prerequisites, v6 import and card API-field distinction.
- Same raw, lines 56–185: versioned construction, optional configuration and event table; lines 187–305 cover external address-lookup callbacks and field mapping.
- Same raw, lines 307–393: brand/co-badged display and flow-specific debit/credit splitting.
- Same raw, lines 395–1032: recurring consent, Sessions token and one-click examples, and Checkout API v69-or-earlier checkbox note.
- Same raw, lines 1033–1499: Advanced token-creation examples, token webhook, stored-card lookup and onSubmit handoff; lines 1501–2560 contain Advanced one-click, subscription and unscheduled examples.
- Same raw, lines 2562–2574: test-only card values, secure-context/JWE condition and live PCI/SAQ A checklist.

## Related

- [[adyen-tokenization]] — token lifecycle and stored-payment-method context.
- [[adyen-card-recognition]] — brand/BIN and choice context.
- [[adyen-pci-dss-compliance]] — compliance guidance beyond this page's checklist.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/web-component/2026-09-15|Card Component]]
