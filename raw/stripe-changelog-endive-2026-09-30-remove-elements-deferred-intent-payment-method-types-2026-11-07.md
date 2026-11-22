<!-- Source URL: https://docs.stripe.com/changelog/endive/2026-09-30/remove-elements-deferred-intent-payment-method-types -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Removes support for the payment method types option in Elements

## What’s new

Removes support for setting [paymentMethodTypes](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodTypes) when you create Elements without a Payment or Setup Intent or call [elements.update()](https://docs.stripe.com/js/elements_object/update). Use `allowedPaymentMethodTypes` to limit available payment methods, or use [Dynamic Payment Methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to manage them from the Dashboard.

## Why is this a breaking change?

If your integration sets `paymentMethodTypes`, Stripe.js now throws an integration error and prevents the Elements instance from being created or updated.

## Impact

You can no longer set `paymentMethodTypes` in your Elements options on Endive. Remove it, replace it with `allowedPaymentMethodTypes` to limit available payment methods, or manage payment methods in the Dashboard. Previously, Stripe.js versions through Dahlia supported `paymentMethodTypes`.

## Related changes

- [Removes the payment method types parameter from Checkout Sessions](https://docs.stripe.com/changelog/endive/2026-09-30/remove-payment-method-types-checkout-sessions.md)
- [Adds support for Data Share Only for 3D Secure authentication](https://docs.stripe.com/changelog/endive/2026-09-30/data-share-only.md)
- [Makes Payment Evaluation signal scores nullable](https://docs.stripe.com/changelog/endive/2026-09-30/payment-evaluations-nullable-score.md)
- [Removes PayTo-specific fields from Payment Methods](https://docs.stripe.com/changelog/endive/2026-09-30/removed-payto-fields.md)
- [Removes the payment method types parameter from Payment Intents and Setup Intents](https://docs.stripe.com/changelog/endive/2026-09-30/removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents.md)
- [Returns specific decline codes for BLIK payment failures](https://docs.stripe.com/changelog/endive/2026-09-30/blik-granular-decline-codes.md)
- [Deprecates the payment request button](https://docs.stripe.com/changelog/endive/2026-09-30/deprecate-payment-request-button.md)
- [Shows pending-authorization UI for MB WAY, Bizum, and BLIK with stripe.handleNextAction](https://docs.stripe.com/changelog/endive/2026-09-30/handle-next-action-mb-way-bizum-ui.md)
- [Saves Bancontact payment details for future off-session payments in Checkout](https://docs.stripe.com/changelog/endive/2026-09-30/bancontact-off-session-payments-checkout.md)
- [Adds the Standalone 3D Secure API](https://docs.stripe.com/changelog/endive/2026-09-30/standalone-3ds.md)
- [Adds support for SeQura payments](https://docs.stripe.com/changelog/endive/2026-09-30/sequra-payments.md)
- [Adds card-present payment methods to allowed payment method types](https://docs.stripe.com/changelog/endive/2026-09-30/card-present-and-interac-present-enum-values-for-allowed-payment-method-types.md)
- [Adds Link funding source group details on Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/link-funding-source-group-payment-records.md)
- [Adds early fraud warnings and fraudulent dispute signals for Payment Evaluations](https://docs.stripe.com/changelog/endive/2026-09-30/new-radar-signals-for-payment-evaluations.md)
- [Adds the ability to report canceled payments](https://docs.stripe.com/changelog/endive/2026-09-30/reporting-canceled-payments.md)
- [Adds support for expanding the mandate on card payment method details](https://docs.stripe.com/changelog/endive/2026-09-30/expand-mandate-on-card-payments-details.md)
- [Adds the Payment Record property to the Payment Intent object](https://docs.stripe.com/changelog/endive/2026-09-30/payment-records-on-payment-intents.md)
- [Adds Link wallet details to Payment Records for card payments](https://docs.stripe.com/changelog/endive/2026-09-30/adds-link-wallet-details-to-payment-records-for-card-payments.md)
- [Adds 3D Secure versions 2.3.0 and 2.3.1 to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/3d-secure-payment-records.md)
- [Adds support for BLIK recurring off-session payments](https://docs.stripe.com/changelog/endive/2026-09-30/blik-recurring-off-session-payments.md)
- [Adds PayPay support for one-time online payments in Japan](https://docs.stripe.com/changelog/endive/2026-09-30/paypay-payments-japan.md)
- [Exposes the network response electronic commerce indicator on card charges](https://docs.stripe.com/changelog/endive/2026-09-30/view-network-response-eci-on-card-charges.md)
- [Adds payment method type information for failed payments](https://docs.stripe.com/changelog/endive/2026-09-30/payment-method-type-payment-failures.md)
- [Adds MoMo payment method details to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/adds-momo-payment-method-details-to-payment-records.md)
