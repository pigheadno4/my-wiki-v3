---
title: "Adyen iDEAL | Wero iOS Component guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/ios-component"
raw_files:
  - "adyen/docs/payment-methods/ideal/ios-component/2026-09-15.md"
tags: [adyen, ideal, wero, ios, components, redirect, sepa, recurring]
---

## Overview

This 2026-09-15 Adyen guide adds iDEAL | Wero to an existing iOS Components integration in Sessions or Advanced server-side flow. Both paths use an `InstantPaymentComponent` selected by `.other("ideal")` and require redirect handling. It separately describes future shopper-absent recurring payments through a stored SEPA Direct Debit method. The page's `WeroiOS` title runs words together; that heading does not establish a separate Wero component or payment-method type. This captured guide does not prove current enablement or an executed payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- Sessions requires an existing iOS Components Sessions integration, Checkout API v68 or later, `action.type: redirect` handling and iDEAL | Wero added in Customer Area. It states no method-specific `/sessions` parameters or Component configuration. The Swift example checks `.other("ideal")`, creates `InstantPaymentComponent`, sets the session as delegate and initiates payment. Advanced requires existing iOS Components Advanced, redirect handling and Customer Area setup; it likewise states no method-specific configuration or normal `/payments` additions. Its Swift example uses the same `.other("ideal")` lookup but sets `self` as delegate. The Advanced prerequisite text says Components while its linked main guide URL has `integration=Drop-in`; the other Advanced links specify Components. Neither section pins an iOS SDK version.
- For later payments the guide says iDEAL | Wero recurring support runs through SEPA Direct Debit, not a repeat iDEAL redirect. Create a shopper token using standard tokenization parameters; a `recurring.token.created` webhook carries `storedPaymentMethodId`. Subsequent tokenised payments are limited here to shopper-absent `Subscription` or `UnscheduledCardOnFile` scenarios with standard tokenization parameters. The sample requests use `paymentMethod.type: sepadirectdebit`, a stored method ID, `shopperInteraction: ContAuth` and subscription model. Example server requests and the webhook description are not proof of a created token or completed charge. The Java example uses amount 15000 while other snippets use 1000, and it omits `shopperReference` shown by the other samples; resolve actual request fields against the tokenization and API authority instead of treating the samples as one consistent contract.
- For the illustrated token payment, a successfully received request yields `resultCode: Received` and `pspReference`; the page directs status tracking to webhooks. `Received` is not successful payment authorization, capture or settlement.
- The page warns that the iDEAL | Wero TEST environment is unreliable and recommends live low-amount testing. Its LIVE path describes an issuer bank account, live payment and payment-page QR or issuer selection, shopper authorization and live Customer Area status check. If TEST is available, the `TESTNL2A` issuer offers simulations for Authorised, Canceled, Pending/Received on expiration, and Refused; these are simulated result codes, not live outcomes. The TEST and LIVE procedures do not by themselves establish current merchant or issuer eligibility.

## Detail locators

- Sessions requirements, no-extra-fields/configuration and Swift Component: pinned raw lines 25–70.
- Sessions SEPA token creation, shopper-absent limit and multi-language request examples: pinned raw lines 72–297; `Received`/webhook outcome boundary: lines 299–304.
- Sessions TEST reliability, LIVE penny path and TEST simulations: pinned raw lines 306–342.
- Advanced Components-label/Drop-in-link mismatch, redirect, no-extra-fields/configuration and Swift delegate: pinned raw lines 344–387.
- Advanced recurring/token examples and `Received`/webhook boundary: pinned raw lines 389–621; TEST/LIVE procedures: lines 623–659.

## Related

- [[adyen-online-payments]] — main concept and redirect/result context
- [[adyen-tokenization]] — provider token lifecycle and shopper-absent use cases

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/ios-component/2026-09-15|iDEAL | Wero iOS Component guide, 2026-09-15]]
