---
title: "MobilePay Android Component | Adyen Docs"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/android-component"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/android-component/2026-09-15.md"
tags: [adyen, mobilepay, android, components, wallet, payout]
---

## Overview

This [[adyen]] guide adds MobilePay to an existing Android Components checkout integration using either Sessions or Advanced server-side flow. Both paths use `InstantPaymentComponent` for the `mobilepay` payment method and require redirect-action handling. It also describes an experimental, Advanced `/payments`-based route to create a token for later payouts to MobilePay wallets. The dated page does not establish current merchant eligibility, supported countries or currencies, successful authorization, or payout availability. See [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Requires an existing Android Components Sessions integration, Checkout API v68 or later, `action.type: redirect` handling, and MobilePay added in Customer Area. The guide says no MobilePay-specific `/sessions` parameters or Component configuration are needed. See raw lines 25–42 and 67–77.
- **Advanced:** Requires an existing Android Components Advanced integration, additional-action handling for `action.type: redirect`, and MobilePay added in Customer Area. Ordinary `/payments` requests need no MobilePay-specific parameters unless creating a future-payout token. See raw lines 163–171 and 259–263.
- **Component setup:** The examples import `com.adyen.checkout:instant:YOUR_VERSION`, plus `components-compose:YOUR_VERSION` for Compose, select `mobilepay` from the Session or `/paymentMethods` response, and create an `InstantPaymentComponent`. Compose wraps it in `AdyenComponent` with a unique reset key; View examples attach it to a view. `YOUR_VERSION` is a placeholder, not a pinned SDK minimum. See raw lines 44–125 and 173–256.
- **Payment testing and outcome:** The page says normal MobilePay payments cannot be tested in the test environment and directs low-amount live payments after a live Customer Area request. It directs the merchant to check the server's `AUTHORISATION` webhook and the live Payment list for status. Redirect handoff alone is not payment authorization. See raw lines 128–138 and 483–493.
- **Experimental payout token:** The page limits the payout feature to `/payments`. For a MobilePay payment that creates a token for later wallet payouts, it calls for a recurring lifecycle webhook and `telephoneNumber`, `shopperReference`, and `enablePayout: true` in the payment request. The merchant then receives `storedPaymentMethodId` in the recurring lifecycle webhook, associates it with `shopperReference`, and uses that token in `counterparty.card.cardIdentification` on a later `/transfers` request. The separate payout-test instructions use a Vipps MobilePay test app; they do not overturn the page's normal-payment live-test warning. See raw lines 140–161 and 449–516.

> [!warning] Payout example inconsistencies
> The prose spells the flag `enablePayout`, while the annotated curl example spells it `enablePayOut`. The Java/PHP/C#/Node/Python/Ruby examples show `telephoneNumber` but omit the other token-creation fields, and several fields contain empty placeholder values. The curl example targets a TEST endpoint even though the page says MobilePay payments cannot be tested in the test environment. Treat the examples as incomplete or inconsistent, not proof of a working payout-token request or normal-payment test path. See raw lines 263–446 and 449–459.

## Detail locators

- Sessions and Advanced Compose/View snippets: raw lines 44–125 and 173–256.
- Payout-token creation, webhook payload and subsequent transfer field: raw lines 449–481. The token-webhook payload is illustrative, not a promise of token issuance for every payment.
- Live-payment testing and separate experimental payout testing: raw lines 128–161 and 483–516. The page supplies no MobilePay country/currency eligibility matrix or full base-flow result contract.

## Related

- [[adyen-android-sdk]] — native Components context; this page leaves the SDK dependency version unspecified.
- [[adyen-payouts]] — separate payout and transfer context; the experimental token route here has its own scope.

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/android-component/2026-09-15|MobilePay Android Component, 2026-09-15 snapshot]]
