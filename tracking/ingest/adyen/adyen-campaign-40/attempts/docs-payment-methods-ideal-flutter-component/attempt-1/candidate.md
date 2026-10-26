---
title: "iDEAL | Wero Flutter Component | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/ideal/flutter-component/2026-09-15.md"
tags: [adyen, ideal, wero, flutter, components, redirect, sepa, tokenization]
---

## Overview

This [[adyen]] guide gives iDEAL | Wero-specific additions to an existing Flutter Components checkout, with separate Sessions and Advanced server-side flows. Both state redirect handling and Customer Area method setup. It also describes **SEPA Direct Debit** tokenization for later shopper-absent payments; the stored method in the examples is `sepadirectdebit`, not an iDEAL redirect payment. See [[adyen-online-payments]] and [[adyen-tokenization]]. The dated guide does not prove current merchant eligibility or any completed payment.

## Key takeaways

- **Sessions and Advanced setup:** Sessions requires an existing Flutter Components Sessions integration, Checkout API v68 or later, `action.type: redirect` handling, and iDEAL | Wero in Customer Area. It says no additional method-specific `/sessions` fields or Component configuration are needed. Advanced requires an existing Flutter Components Advanced integration, redirect handling and Customer Area setup, and says no extra method-specific `/payments` fields or configuration are needed for an ordinary payment. Neither section pins a Flutter SDK version or supplies Component initialization code. See raw lines 25–46 and 320–342.
- **Separate recurring path:** The page says recurring payments for iDEAL | Wero go through SEPA Direct Debit. It routes token creation to standard tokenization parameters in a payment request, without extra SEPA-specific fields; a `recurring.token.created` webhook then supplies `storedPaymentMethodId`. It limits tokenized payments here to shopper-absent `Subscription` or `UnscheduledCardOnFile` scenarios. The examples show a later `sepadirectdebit` stored-method `Subscription` request with `shopperInteraction: ContAuth`; they do not turn ordinary iDEAL redirect payments into reusable iDEAL tokens. See raw lines 48–75, 77–272 and 344–371, 373–568.
- **Result boundary:** For the illustrated stored-method request, a successfully received payment can return `resultCode: Received` and `pspReference`. The page says to use webhooks to track whether the payment was successful. Treat `Received` and the example TEST endpoints as intermediate/sample evidence, not authorization or settlement. See raw lines 275–280 and 571–576.
- **TEST and live guidance:** The page calls the iDEAL | Wero TEST environment unreliable and recommends low-amount live testing. Its live checklist uses a live issuer bank account, redirect to the iDEAL | Wero payment page, QR scan or bank selection, shopper authorization and status check in the live Customer Area. If TEST is operating, the page describes TESTNL2A simulations for success, cancellation, expiration and refusal; expiration can yield `Pending` or `Received`, which still requires an outcome check. The “Request iDEAL | Wero for the live environment” heading has no actual request procedure under it; do not infer a completed or specified account-approval step here. See raw lines 282–318 and 578–614.

> [!warning] Prerequisite links and examples
> Both prerequisite rows say **Flutter Components** but link to an **Advanced Flutter Drop-in** base guide; the Sessions row also points to Advanced rather than Sessions. The dedicated redirect links point to the corresponding Components guides. Follow the stated flow and verify the base route before implementing. The Java stored-method example omits `shopperReference` while the surrounding examples include it, and uses 15000 minor units where most other examples use 1000; example requests are not a universal parameter contract or payment proof. See raw lines 31–33, 77–129, 328–329 and 373–424.

## Detail locators

- Sessions/Advanced requirements and no-extra-parameter statements: raw lines 25–46 and 320–342.
- SEPA token creation and shopper-absent reuse: raw lines 48–75 and 344–371; stored-method request examples: raw lines 77–272 and 373–568.
- `Received` versus webhook outcome: raw lines 275–280 and 571–576; qualified TEST/LIVE instructions and simulation table: raw lines 282–318 and 578–614.

## Related

- [[source-adyen-docs-payment-methods-ideal]] — method overview and channel context.
- [[adyen-tokenization]] — general stored-method lifecycle, consent and merchant-server boundary.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/flutter-component/2026-09-15|iDEAL | Wero Flutter Component, 2026-09-15 snapshot]]
