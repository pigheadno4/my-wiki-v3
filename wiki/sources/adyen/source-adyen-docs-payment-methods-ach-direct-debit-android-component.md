---
title: "ACH Direct Debit Android Component integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/android-component"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/android-component/2026-09-15.md"
tags: [adyen, ach, direct-debit, android, component, sessions, advanced]
---

## Overview

This 2026-09-15 guide adds ACH Direct Debit to **existing Android Components** Sessions and Advanced integrations. It identifies the ACH module and Compose option, payment-method sourcing, UI configuration, request additions and delayed outcome. It is not a full Android integration, an account-verification guide or proof of an authorized/settled ACH debit. [[adyen]] [[adyen-online-payments]] [[adyen-android-sdk]]

## Key takeaways

- **Sessions prerequisites:** existing Android Components Sessions, Checkout API **v68 or later**, ACH added in Customer Area and `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` subscription for outdated bank details. The **Merchant allow bank-refund** API-credential and Customer Area roles in the requirements table apply to **issuing refunds through those channels**, not to all ACH payment acceptance. No ACH-specific extra `/sessions` parameters are required. See raw lines 25–44.
- **Android module and UI:** both flows include `com.adyen.checkout:ach:YOUR_VERSION`, adding `components-compose:YOUR_VERSION` only for Jetpack Compose. `ACHDirectDebitComponent` is shown for Compose and non-Compose. Optional configuration defaults: submit button visible true, full-address form, and save-payment-details checkbox visible true; `setShowStorePaymentField(false)` hides that checkbox. The US/PR country-code list appears in an example address configuration, not as a standalone current eligibility guarantee or SDK minimum. See raw lines 46–102, 197–247.
- **Sessions versus Advanced:** Sessions gets the ACH payment method from `checkoutSession.getPaymentMethod(PaymentMethodTypes.ACH)`; Advanced selects `PaymentMethodTypes.ACH` from `/paymentMethods` and passes it into the Component. Compose examples require a unique key for each different screen/payment session, regenerating it on reset. Advanced says no **ACH-specific additional** `/payments` parameters, which does not remove the base Advanced payment request or ACH mandate/validation obligations. See raw lines 104–150, 249–304.
- **Outcome:** after Adyen receives the payment request, bank authorization may take up to **five business days**. A bank-authorized payment appears in the Settlement details report; failed bank authorization results in a `CHARGEBACK` webhook. Component completion or request receipt is not final bank authorization or settlement. See raw lines 153–159 and 306–312.
- **TEST:** guide offers correctly formatted account/routing fixtures and `ownerName=chargeback:<ACH return reason>` (for example `chargeback:R01`) to simulate returns. These are test scenarios, not live payment or dispute evidence. See raw lines 161–177 and 314–330. The related [[source-adyen-docs-payment-methods-ach-direct-debit]] supplies US-entity, SEC, mandate, return and refund boundaries; [[source-adyen-docs-payment-methods-ach-direct-debit-verification-with-giact]] covers separate consumer bank validation.

## Detail locators

- Sessions requirements and no-extra-parameter statement: raw lines 25–44.
- Sessions modules, configuration and Component setup: raw lines 46–150.
- Sessions delayed outcome and TEST flow: raw lines 153–177.
- Advanced requirements, modules and configuration: raw lines 179–247.
- Advanced method selection, no-extra-parameter statement and outcome: raw lines 249–312.
- Advanced TEST return simulation and related guide links: raw lines 314–336.

## Related

- [[adyen-online-payments]] — online payment integration route.
- [[adyen-android-sdk]] — native Component/module context.
- [[source-adyen-docs-payment-methods-ach-direct-debit]] — ACH method overview, mandate and lifecycle.
- [[source-adyen-docs-payment-methods-ach-direct-debit-verification-with-giact]] — separate bank-account validation.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/android-component/2026-09-15|ACH Direct Debit Android Component, captured 2026-09-15]]
