---
title: "Stripe Docs — Strong Customer Authentication readiness"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/strong-customer-authentication"
raw_files:
  - "stripe-sca-readiness-2025.md"
tags: [stripe, sca, psd2, 3d-secure, payment-intents, setup-intents, off-session, grandfathering, mit, eea]
---

## Summary

Stripe's SCA readiness guide covers which integrations should be updated, SCA-ready products, prior authorization agreements, and preparation for off-session charges. The 2026-05-08 guide dates PSD2 SCA to September 14, 2019 and treats country-specific enforcement as a separate question.

## Impacted Businesses and Payments

Stripe advises updating an integration when all three conditions apply:

1. The business is based in the EEA or creates payments on behalf of EEA-based connected accounts.
2. The business serves customers in the EEA.
3. The business accepts credit or debit cards.

Issuers can still request authentication for low-risk transactions. The guide identifies the legacy Charges API as an example of an integration that is unprepared for SCA.

## SCA-Ready Products

- **One-time payments.** Use the Payment Intents API or the prebuilt, Stripe-hosted Checkout flow described in this section, which handles SCA.
- **Saving cards.** Use Payment Intents when saving during payment or Setup Intents when saving separately. The guide also describes Checkout for saving cards and Billing for subscriptions.
- **Third-party integrations.** Merchants relying on a plugin, platform or extension should ask their partner about updates. The guide's separate plugin and library section describes embedded or hosted Checkout, or Intents APIs with Elements for more control. It asks builders to identify the integration with `setAppInfo`, test successful and unsuccessful authentication and notify their customers and Stripe when they release an SCA-ready update.

## Grandfathering (Previous Authorization Agreements)

| Customer | Card saved before |
| --- | --- |
| EU | December 31, 2020 |
| UK | September 14, 2021 |

These cutoffs apply to this off-session pathway regardless of payment amount or frequency. Create a PaymentIntent and flag it off-session. Stripe looks for eligible older card transactions and attempts to reuse the previous authorization agreement. If the bank accepts it, the transaction is outside SCA scope and can proceed without additional authentication. If it declines, the PaymentIntent moves to `requires_payment_method` (`requires_source` before API version 2019-02-11) and the merchant must notify the customer to complete payment.

## Off-Session Readiness Checklist

1. Authenticate the card when saving it while the customer is on-session.
2. When saving during payment, set `setup_future_usage: 'off_session'` on the PaymentIntent.
3. When saving without payment, set `usage: 'off_session'` on the SetupIntent.
4. When creating an off-session PaymentIntent, set `off_session: true`.

## MIT Mandate Requirements

Stripe says it marks subsequent off-session payments as merchant-initiated transactions (MITs) for the described Payment Intents or Setup Intents card-saving flow. A properly authenticated saved-card payment can qualify as an out-of-scope MIT. The bank can still request authentication on a later off-session payment.

Obtain an agreement or mandate between the merchant and customer. It should at minimum cover permission to initiate payments, the anticipated frequency, and how the amount is determined. Reference the payment terms in the checkout flow.

## Incomplete Payments and Disputes

- **Billing.** Handle incomplete statuses when integrating the Billing API for subscriptions or invoices. The November capture links to the Subscription object's status reference, listed below.
- **Payment troubleshooting.** For a payment shown as `incomplete` in the Dashboard or `requires_action` in the API, check whether the customer is actively authenticating an on-session payment or has abandoned checkout. Verify that your integration handles next actions such as authentication.
- **Fraud-dispute liability.** Successful 3DS authentication typically shifts fraud-dispute liability to the issuer. In the issuer-applied exemption described by the guide, the payment has no 3DS authentication and that liability shift does not apply.

## Related Pages

- [[stripe-3d-secure]] — 3D Secure concept and SCA readiness
- [[source-stripe-sca-exemptions]] — SCA exemptions
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-sca-readiness-2025]] — 2026-05-08 SCA readiness guide (175 lines)

## Related raw API references

- [[raw/stripe-strong-customer-authentication-2026-11-07|2026-11-07 SCA readiness guide]] — corroborating capture with an updated [Subscription object status reference](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-status).
