---
title: "PayTo Android Component integration"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/payto/android-component"
raw_files:
  - "adyen/docs/payment-methods/payto/android-component/2026-09-15.md"
tags: [adyen, payto, android, components, australia, mandate, subscription]
---

## Overview

This 2026-09-15-captured Adyen guide adds **PayTo to an existing Android Components integration**. It separates Sessions and Advanced server-side flows, one-time payments from subscription-agreement setup and later subscription charges, and bank agreement approval from eventual payment outcome. The guide's examples use AU/AUD, consistent with the separate [[source-adyen-docs-payment-methods-payto|PayTo method overview]]; neither source proves current merchant enablement, bank acceptance, a live charge or final payment success. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Prerequisites and Component:** both Sessions and Advanced require an existing Android Components integration, Checkout API **v70 or later**, and PayTo added in Customer Area. Advanced additionally requires handling `action.type: await`. Import the `payto` module, plus `components-compose` for Jetpack Compose; the guide uses `PayToComponent` and `PaymentMethodTypes.PAY_TO`, with an optional `setSubmitButtonVisible` configuration. Compose examples require a unique Component key per screen/payment session (raw lines 25–35, 258–355, 372–483).
- **One-time Sessions:** the `/sessions` table marks shopper first and last name required. It lists optional statement, line-item details and payment reference, with a PayTo **35-character maximum** for the reference. The example uses AU/AUD and includes `shopperReference` and `returnUrl`; it omits a comma after `shopperReference`, so it is not literal copy-ready JSON. The response description says Adyen creates an **adhoc**, one-count, exact-amount mandate whose `endsAt` defaults to one day after the request, rather than a reusable subscription agreement (raw lines 39–120).
- **Subscription setup and first payment:** Sessions and Advanced require shopper name, `storePaymentMethod: true`, `recurringProcessingModel: Subscription`, `shopperInteraction: Ecommerce`, and mandate frequency, end date, amount, amount rule and remarks. `mandate.count` is listed as optional in the table but its description says it **must be supplied and at least 1 when frequency is not `adhoc`**; `startsAt` is optional. Scheduled frequencies suit Subscription; `adhoc` is described for CardOnFile/UnscheduledCardOnFile models. `amountRule` is `max` or `exact`; the sample weekly 30 AUD first/90 AUD maximum future payment is an example, not a guaranteed recurring limit. The bank notifies the shopper to authorize or decline the agreement (Sessions raw lines 122–219; Advanced raw lines 562–665).
- **Advanced requests and later charges:** one-time and setup `/payments` tables also require `paymentMethod: payto` and `paymentMethod.shopperAccountIdentifier` (bank details or PayID) in addition to shopper name. A successful request example returns **Pending** with an `await` action, which is not final authorization. Later subscription payments are **Advanced flow or API-only**, not Sessions; the subsequent `/payments` table requires `paymentMethod.storedPaymentMethodId` and `shopperInteraction: ContAuth`, and says the token may be used only within the agreement's conditions. Its example response is `Received`, not a final payment outcome (raw lines 48–51, 487–560, 562–727).
- **Token and outcome lifecycle:** after the shopper accepts a subscription agreement, the text names a `RECURRING_CONTRACT` webhook with `recurringDetailReference`, while its webhook section says the token is in `pspReference`. The subsequent-payment table instead points to `data.storedPaymentMethodId` in `recurring.token.created`. These are different documented token references; do not substitute one for another or infer a single mapping from this guide. `OFFER_CLOSED` describes failed/cancelled agreements, `AUTHORISATION` can report an authorized **or rejected** payment on an accepted agreement, `REFUND_FAILED` can follow an initially received refund, and `DISABLE_RECURRING` reports token deletion when an agreement ends/cancels. Agreement acceptance, token creation and payment authorization are distinct events (raw lines 217–256, 663–675, 741–771).
- **Test and source-example cautions:** the guide gives `shopperAccountIdentifier` test values for agreement expiry/refusal and payment refusal/error, under both flows; these are simulations. Several request examples omit a comma after `shopperReference`, and “response” blocks are rendered as `curl` commands; use tables and actual API schemas before execution. The child guide's Test and go live sections provide test identifiers but no separate live-operation proof (raw lines 69–120, 162–215, 358–370, 605–660, 678–727, 773–785). The separate PayTo overview describes asynchronous method setup and bank authorization/final webhook sequencing (overview pinned raw lines 29–107).

## Detail locators

- Sessions/Advanced prerequisites and API minimum: raw lines 25–35 and 372–381.
- One-time Sessions fields, reference length and default mandate: raw lines 39–120.
- Subscription setup fields, count condition and bank agreement approval: raw lines 122–225 and 562–665.
- Webhook lifecycle: raw lines 226–256 and 741–771.
- Android imports, optional configuration, Component launch and Compose key: raw lines 258–355 and 383–483.
- Advanced one-time fields and Pending/await response: raw lines 487–560.
- Subsequent subscription payment/token source and Received example: raw lines 667–727; identifier formats lines 729–739.
- Test scenario tables: raw lines 358–370 and 773–785.
- Method-level AU/AUD scope and asynchronous setup/bank approval: [[source-adyen-docs-payment-methods-payto]] and its pinned raw lines 23–107; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-payto]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/payto/android-component/2026-09-15|PayTo Android Component guide, captured 2026-09-15]]
