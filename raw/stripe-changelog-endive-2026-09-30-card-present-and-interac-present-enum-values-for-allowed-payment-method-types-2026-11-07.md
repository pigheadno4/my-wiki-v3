<!-- Source URL: https://docs.stripe.com/changelog/endive/2026-09-30/card-present-and-interac-present-enum-values-for-allowed-payment-method-types -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Adds card-present payment methods to allowed payment method types

## What’s new

You can now specify `card_present` or `interac_present` when setting [allowed_payment_method_types](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-allowed_payment_method_types) on a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.endive#payment_intent_object-allowed_payment_method_types) or [SetupIntent](https://docs.stripe.com/api/setup_intents/object.md?api-version=2026-09-30.endive#setup_intent_object-allowed_payment_method_types).

- `card_present`: Use this when you [collect in-person card payments](https://docs.stripe.com/terminal/payments/collect-card-payment.md) with Stripe Terminal.
- `interac_present`: Use this if you [collect Interac payments](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#interac-payments) in person in Canada through Stripe Terminal.

You can use these values when you create, update, confirm, or retrieve Payment Intents or Setup Intents.

## Impact

You can now specify which payment method types are supported for in-person payments through Stripe Terminal.

If you use a typed SDK (such as [stripe-java](https://github.com/stripe/stripe-java) or [stripe-node](https://github.com/stripe/stripe-node)), specify `card_present` or `interac_present` as typed enum values when you set `allowed_payment_method_types` on a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.endive#payment_intent_object-allowed_payment_method_types) or [SetupIntent](https://docs.stripe.com/api/setup_intents/object.md?api-version=2026-09-30.endive#setup_intent_object-allowed_payment_method_types).

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `card_present`, `interac_present` | Added | [PaymentIntent#create.allowed_payment_method_types](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-allowed_payment_method_types), [PaymentIntent#update.allowed_payment_method_types](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-allowed_payment_method_types), [PaymentIntent#confirm.allowed_payment_method_types](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-allowed_payment_method_types), [SetupIntent#create.allowed_payment_method_types](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-allowed_payment_method_types), [SetupIntent#update.allowed_payment_method_types](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-allowed_payment_method_types), [SetupIntent#confirm.allowed_payment_method_types](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-allowed_payment_method_types), [PaymentIntent.allowed_payment_method_types](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-allowed_payment_method_types), [SetupIntent.allowed_payment_method_types](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-allowed_payment_method_types) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `card_present`, `interac_present` | Added | [PaymentIntentCreateParams.allowed_payment_method_types](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-allowed_payment_method_types), [PaymentIntentModifyParams.allowed_payment_method_types](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-allowed_payment_method_types), [PaymentIntentConfirmParams.allowed_payment_method_types](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-allowed_payment_method_types), [SetupIntentCreateParams.allowed_payment_method_types](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-allowed_payment_method_types), [SetupIntentModifyParams.allowed_payment_method_types](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-allowed_payment_method_types), [SetupIntentConfirmParams.allowed_payment_method_types](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-allowed_payment_method_types), [PaymentIntent.allowed_payment_method_types](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-allowed_payment_method_types), [SetupIntent.allowed_payment_method_types](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-allowed_payment_method_types) |

#### PHP

| Values | Change | Enums |
| --- | --- | --- |
| `card_present`, `interac_present` | Added | [PaymentIntent.allowed_payment_method_types](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-allowed_payment_method_types), [SetupIntent.allowed_payment_method_types](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-allowed_payment_method_types) |

#### Java

| Values | Change | Enums |
| --- | --- | --- |
| `card_present`, `interac_present` | Added | [PaymentIntentCreateParams.allowedPaymentMethodTypes](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-allowedPaymentMethodTypes), [PaymentIntentUpdateParams.allowedPaymentMethodTypes](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-allowedPaymentMethodTypes), [PaymentIntentConfirmParams.allowedPaymentMethodTypes](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-allowedPaymentMethodTypes), [SetupIntentCreateParams.allowedPaymentMethodTypes](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-allowedPaymentMethodTypes), [SetupIntentUpdateParams.allowedPaymentMethodTypes](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-allowedPaymentMethodTypes), [SetupIntentConfirmParams.allowedPaymentMethodTypes](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-allowedPaymentMethodTypes) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `card_present`, `interac_present` | Added | [PaymentIntentCreateParams.allowed_payment_method_types](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent-allowed_payment_method_types), [PaymentIntentUpdateParams.allowed_payment_method_types](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent-allowed_payment_method_types), [PaymentIntentConfirmParams.allowed_payment_method_types](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent-allowed_payment_method_types), [SetupIntentCreateParams.allowed_payment_method_types](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent-allowed_payment_method_types), [SetupIntentUpdateParams.allowed_payment_method_types](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent-allowed_payment_method_types), [SetupIntentConfirmParams.allowed_payment_method_types](/api/setup_intents/confirm?api-version=2026-09-30.endive#confirm_setup_intent-allowed_payment_method_types), [PaymentIntent.allowed_payment_method_types](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-allowed_payment_method_types), [SetupIntent.allowed_payment_method_types](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-allowed_payment_method_types) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `card_present`, `interac_present` | Added | [PaymentIntent.AllowedPaymentMethodTypes](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-AllowedPaymentMethodTypes), [SetupIntent.AllowedPaymentMethodTypes](/api/setup_intents/object?api-version=2026-09-30.endive#setup_intent_object-AllowedPaymentMethodTypes) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Removes the payment method types parameter from Checkout Sessions](https://docs.stripe.com/changelog/endive/2026-09-30/remove-payment-method-types-checkout-sessions.md)
- [Adds support for Data Share Only for 3D Secure authentication](https://docs.stripe.com/changelog/endive/2026-09-30/data-share-only.md)
- [Makes Payment Evaluation signal scores nullable](https://docs.stripe.com/changelog/endive/2026-09-30/payment-evaluations-nullable-score.md)
- [Removes PayTo-specific fields from Payment Methods](https://docs.stripe.com/changelog/endive/2026-09-30/removed-payto-fields.md)
- [Removes the payment method types parameter from Payment Intents and Setup Intents](https://docs.stripe.com/changelog/endive/2026-09-30/removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents.md)
- [Returns specific decline codes for BLIK payment failures](https://docs.stripe.com/changelog/endive/2026-09-30/blik-granular-decline-codes.md)
- [Deprecates the payment request button](https://docs.stripe.com/changelog/endive/2026-09-30/deprecate-payment-request-button.md)
- [Shows pending-authorization UI for MB WAY, Bizum, and BLIK with stripe.handleNextAction](https://docs.stripe.com/changelog/endive/2026-09-30/handle-next-action-mb-way-bizum-ui.md)
- [Removes support for the payment method types option in Elements](https://docs.stripe.com/changelog/endive/2026-09-30/remove-elements-deferred-intent-payment-method-types.md)
- [Saves Bancontact payment details for future off-session payments in Checkout](https://docs.stripe.com/changelog/endive/2026-09-30/bancontact-off-session-payments-checkout.md)
- [Adds the Standalone 3D Secure API](https://docs.stripe.com/changelog/endive/2026-09-30/standalone-3ds.md)
- [Adds support for SeQura payments](https://docs.stripe.com/changelog/endive/2026-09-30/sequra-payments.md)
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
