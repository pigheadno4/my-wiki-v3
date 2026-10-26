---
title: "Adyen iDEAL | Wero React Native Drop-in guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ideal/react-native-drop-in/2026-09-15.md"
tags: [adyen, ideal, wero, react-native, drop-in, redirect, sepa, recurring]
---

## Overview

This 2026-09-15 Adyen guide adds iDEAL | Wero to an existing React Native Drop-in integration in Sessions or Advanced server-side flow. It separately describes stored SEPA Direct Debit details for later shopper-absent payments. The method add-on relies on the main React Native Drop-in guides for the full checkout flow and does not establish current merchant eligibility or a completed payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- Sessions requires an existing React Native Drop-in Sessions integration, Checkout API v68 or later, `action.type: redirect` handling and iDEAL | Wero added in Customer Area. Its prerequisite row says Sessions but links to an Advanced-flow Drop-in URL; its session-creation and redirect links do target Sessions. It says no method-specific `/sessions` parameters or Drop-in configuration are needed. Advanced requires an existing React Native Drop-in Advanced integration, redirect handling and Customer Area addition; it likewise says no method-specific normal `/payments` parameters or Drop-in configuration. The Advanced section does not state a Checkout API minimum.
- The recurring route is through **SEPA Direct Debit**, not a repeated iDEAL redirect. Create a shopper token using standard tokenization request parameters; on token creation a `recurring.token.created` webhook supplies `storedPaymentMethodId`. Subsequent tokenised payments are restricted by this guide to shopper-absent `Subscription` and `UnscheduledCardOnFile` scenarios with standard tokenization parameters. The examples use `paymentMethod.type: sepadirectdebit`, stored method ID and `shopperInteraction: ContAuth`. The Java example differs from adjacent examples in amount (15000 versus 1000) and omits the displayed `shopperReference`; resolve actual request requirements against tokenization/API authority rather than merging snippets into one contract. A token request or example webhook is not an observed created token.
- For the illustrated token payment, a successfully received request has `resultCode: Received` and a `pspReference`; webhooks track whether it succeeds. `Received` does not mean successful authorization, capture or settlement.
- The guide warns the iDEAL | Wero TEST environment may not work reliably and recommends low-amount LIVE testing. Its LIVE path calls for an issuer bank account, a live payment with Payment Page QR or bank selection, shopper authorization and a live Customer Area status check. If TEST is available, issuer `TESTNL2A` offers simulated Authorised, Canceled, Pending/Received on expiration and Refused result codes. Those are simulations, not live outcomes. The heading for a LIVE request provides no extra activation instructions beyond the Customer Area setup prerequisite.

## Detail locators

- Scope and Sessions prerequisite-link mismatch, redirect, no-extra-fields/configuration: pinned raw lines 15–48.
- Sessions SEPA token route, shopper-absent restriction and multi-language examples: pinned raw lines 50–275; `Received`/webhook boundary: lines 277–282.
- Sessions unreliable TEST, LIVE penny path and conditional TEST simulations: pinned raw lines 284–320.
- Advanced prerequisites, redirect and no-extra-fields/configuration: pinned raw lines 322–344.
- Advanced recurring/token examples and `Received`/webhook boundary: pinned raw lines 346–578; testing and LIVE path: lines 580–616.

## Related

- [[adyen-online-payments]] — main concept and redirect/result context
- [[adyen-tokenization]] — provider token lifecycle and shopper-absent use cases

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/react-native-drop-in/2026-09-15|iDEAL | Wero React Native Drop-in guide, 2026-09-15]]
