---
title: "Cash App Pay Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-pay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/cash-app-pay/web-drop-in/2026-09-15.md"
tags: [adyen, cash-app-pay, web, drop-in, tokenization]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Cash App Pay** to an existing **Web Drop-in** integration, with separate Sessions and Advanced flow instructions and optional tokenization for future card-on-file or recurring payments. It is Cash App Pay guidance, not Cash App Afterpay guidance. The captured page documents configuration and examples; it does not prove current merchant enablement, shopper consent, successful payment, or a live recurring charge. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Base integration and setup:** Both Sessions and Advanced require an existing Web Drop-in integration at **v5.44.0 or later**, the recurring tokens life cycle events webhook, Cash App Pay added in Customer Area, and **Recurring details** selected under Developer > Additional data > Payment. Web Drop-in v6 has a separate CashAppPay import. These are the source's stated requirements, not proof that a given account is configured. [Raw: lines 18–46]
- **Amount and UI:** The page says Cash App Pay needs no extra **method-specific API fields** for ordinary payment requests, but requires the transaction amount for authorization: on /sessions when creating the session, or in the AdyenCheckout instance for a /payments integration. It exempts zero-value authorizations from passing amount. Optional UI settings include a consent toggle (enableStoreDetails), automatic storage (storePaymentMethod), Pay-button visibility, and an onClick resolve/reject handler. The page strongly recommends explicit shopper permission for future recurring or card-on-file use; its automatic-storage option is not evidence of such permission. [Raw: lines 48–85]
- **Token creation differs by flow/version:** For Sessions with Checkout API **v70+**, the text calls for recurringProcessingModel, shopperReference and storePaymentMethodMode; the mode can disable storage, ask for consent, or enable it. For **v69**, a toggle uses enableStoreDetails; storing without a toggle uses storePaymentMethodMode enabled together with storePaymentMethod true. In Advanced, pass state.data.storePaymentMethod from onChange/onSubmit to the server and include it plus shopperReference in /payments. The v70+ sample request omits shopperReference even though the nearby table says to include it, so use the stated field requirement and base API contract rather than treating the sample as a complete tokenization recipe. [Raw: lines 95–125, 126–146, 411–426]
- **Stored details and $cashtag:** To display saved methods, send shopperReference in /sessions for Sessions or /paymentMethods for Advanced; Drop-in shows available stored methods by default unless showStoredPaymentMethods is false. The page recommends including the shopper's $cashtag on recurring payments to make them recognizable. It says obtain the $cashtag through /payments/details with **Token information for digital wallets** enabled; a Sessions integration wanting that value must switch to Advanced and implement /payments/details and /payments. The recurring.token.created webhook includes the shopper reference and recurring detail reference, **not** the $cashtag. [Raw: lines 428–463]
- **Stored payment and lifecycle:** In Advanced, pass state.data.paymentMethod from onSubmit to the server and follow tokenized-payment parameters; paymentMethod.cashtag is optional. The example uses type cashapp, a storedPaymentMethodId, shopperReference, shopperInteraction ContAuth, and recurringProcessingModel CardOnFile. Its Authorised response is illustrative, not live-payment evidence. If the shopper deletes stored Cash App Pay details, the source says a recurring.token.disabled webhook is sent; remove the unusable token and ask for another payment method. Testing uses the test environment and Cash App Pay magic values; live use requires adding Cash App Pay in live Customer Area. [Raw: lines 488–534, 857–896]

> [!warning] Tokenization example and consent boundaries
> The Sessions v70+ field table calls for shopperReference, but the displayed /sessions example omits it (raw lines 110–116, 126–146). The page permits a no-toggle storage setting while strongly recommending explicit permission for future recurring/card-on-file use (raw lines 70–71, 83–85, 411–419). Preserve both statements; neither the setting nor the sample proves valid consent or a complete token-creation request.

## Detail locators

- Sessions and Advanced Web Drop-in prerequisites, v6 import, base API reference: pinned raw lines 18–53.
- Amount, optional UI configuration, tokenization purpose and permission recommendation: pinned raw lines 55–93.
- Sessions v70+ field/mode table and examples, v69 and Advanced storage: pinned raw lines 95–426.
- Stored-method display and $cashtag acquisition/flow switch: pinned raw lines 428–486.
- Stored-token payment, illustrative response, token-disabled webhook, and test/live gates: pinned raw lines 488–896.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-pay/web-drop-in/2026-09-15|Cash App Pay Web Drop-in guide, captured 2026-09-15]]
