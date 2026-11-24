<!-- Source URL: https://docs.stripe.com/changelog/dahlia/2026-06-24/satispay-recurring-payments -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Adds support for recurring payments with Satispay

## What’s new

The [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay-setup_future_usage) parameter is now supported on [PaymentIntents](https://docs.stripe.com/api/payment_intents.md?api-version=2026-06-24.dahlia) and [SetupIntents](https://docs.stripe.com/api/setup_intents.md?api-version=2026-06-24.dahlia) for Satispay, enabling both on-session and off-session payment flows.

Satispay is also now a supported payment method type for [Subscriptions](https://docs.stripe.com/api/subscriptions.md?api-version=2026-06-24.dahlia) and [Invoices](https://docs.stripe.com/api/invoices.md?api-version=2026-06-24.dahlia). Include `satispay` in the [payment_method_types](https://docs.stripe.com/api/subscriptions/create.md?api-version=2026-06-24.dahlia#create_subscription-payment_settings-payment_method_types) parameter of the payment settings for both resources.

## Impact

You can now accept [Satispay](https://docs.stripe.com/payments/satispay.md) payments on a recurring basis, including for subscriptions and invoices.

To save a Satispay payment method for future use, set [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay-setup_future_usage) to `off_session` or `on_session` when creating a PaymentIntent or SetupIntent. To enable Satispay for subscriptions or invoices, add `satispay` to the `payment_method_types` parameter in your Subscription or Invoice payment settings. For full implementation details, see [Accept a Satispay payment](https://docs.stripe.com/payments/satispay/accept-a-payment.md) and [Set up future payments](https://docs.stripe.com/payments/satispay/set-up-future-payments.md).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentIntent#confirm.payment_method_options.satispay](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options-satispay), [PaymentIntent#create.payment_method_options.satispay](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay), [PaymentIntent#update.payment_method_options.satispay](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options-satispay), [PaymentIntent.payment_method_options.satispay](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options-satispay) |
| `satispay` | Added | [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-06-24.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay` | Added | [Invoice#update.payment_settings.payment_method_types](/api/invoices/update?api-version=2026-06-24.dahlia#update_invoice-payment_settings-payment_method_types), [Invoice#create.payment_settings.payment_method_types](/api/invoices/create?api-version=2026-06-24.dahlia#create-payment_settings-payment_method_types), [Subscription#update.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2026-06-24.dahlia#update_subscription-payment_settings-payment_method_types), [Subscription#create.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2026-06-24.dahlia#create_subscription-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-06-24.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-06-24.dahlia#subscription_object-payment_settings-payment_method_types) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentIntent::PaymentMethodOption::Satispay](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options-satispay), [PaymentIntentConfirmParams::PaymentMethodOption::Satispay](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options-satispay), [PaymentIntentCreateParams::PaymentMethodOption::Satispay](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay), [PaymentIntentUpdateParams::PaymentMethodOption::Satispay](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options-satispay) |
| `satispay` | Added | [SetupAttempt::PaymentMethodDetail](/api/setup_attempts/object?api-version=2026-06-24.dahlia#setup_attempt_object-payment_method_details) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentIntent.PaymentMethodOption.Satispay](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options-satispay), [PaymentIntentConfirmParamsPaymentMethodOptionSatispay](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options-satispay), [PaymentIntentCreateParamsPaymentMethodOptionSatispay](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay), [PaymentIntentModifyParamsPaymentMethodOptionSatispay](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options-satispay) |
| `satispay` | Added | [SetupAttempt.PaymentMethodDetail](/api/setup_attempts/object?api-version=2026-06-24.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay` | Added | [InvoiceModifyParamsPaymentSetting.payment_method_types](/api/invoices/update?api-version=2026-06-24.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParamsPaymentSetting.payment_method_types](/api/invoices/create?api-version=2026-06-24.dahlia#create-payment_settings-payment_method_types), [SubscriptionModifyParamsPaymentSetting.payment_method_types](/api/subscriptions/update?api-version=2026-06-24.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParamsPaymentSetting.payment_method_types](/api/subscriptions/create?api-version=2026-06-24.dahlia#create_subscription-payment_settings-payment_method_types), [Invoice.PaymentSetting.payment_method_types](/api/invoices/object?api-version=2026-06-24.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.PaymentSetting.payment_method_types](/api/subscriptions/object?api-version=2026-06-24.dahlia#subscription_object-payment_settings-payment_method_types) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentIntent.confirm().$params.payment_method_option.satispay](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options-satispay), [PaymentIntent.create().$params.payment_method_option.satispay](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay), [PaymentIntent.payment_method_options.satispay](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options-satispay), [PaymentIntent.update().$params.payment_method_option.satispay](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options-satispay) |
| `satispay` | Added | [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-06-24.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay` | Added | [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-06-24.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-06-24.dahlia#subscription_object-payment_settings-payment_method_types) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setupFutureUsage` | Added | [PaymentIntent.payment_method_options.satispay](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options-satispay), [PaymentIntentConfirmParams.payment_method_options.satispay](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options-satispay), [PaymentIntentCreateParams.payment_method_options.satispay](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay), [PaymentIntentUpdateParams.payment_method_options.satispay](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options-satispay) |
| `satispay` | Added | [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-06-24.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay` | Added | [InvoiceUpdateParams.payment_settings.paymentMethodTypes](/api/invoices/update?api-version=2026-06-24.dahlia#update_invoice-payment_settings-paymentMethodTypes), [InvoiceCreateParams.payment_settings.paymentMethodTypes](/api/invoices/create?api-version=2026-06-24.dahlia#create-payment_settings-paymentMethodTypes), [SubscriptionUpdateParams.payment_settings.paymentMethodTypes](/api/subscriptions/update?api-version=2026-06-24.dahlia#update_subscription-payment_settings-paymentMethodTypes), [SubscriptionCreateParams.payment_settings.paymentMethodTypes](/api/subscriptions/create?api-version=2026-06-24.dahlia#create_subscription-payment_settings-paymentMethodTypes) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentIntent.payment_method_options.satispay](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options-satispay), [PaymentIntentConfirmParams.payment_method_options.satispay](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options-satispay), [PaymentIntentCreateParams.payment_method_options.satispay](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay), [PaymentIntentUpdateParams.payment_method_options.satispay](/api/payment_intents/update?api-version=2026-06-24.dahlia#update_payment_intent-payment_method_options-satispay) |
| `satispay` | Added | [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2026-06-24.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay` | Added | [InvoiceUpdateParams.payment_settings.payment_method_types](/api/invoices/update?api-version=2026-06-24.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings.payment_method_types](/api/invoices/create?api-version=2026-06-24.dahlia#create-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2026-06-24.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2026-06-24.dahlia#create_subscription-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-06-24.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-06-24.dahlia#subscription_object-payment_settings-payment_method_types) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SetupFutureUsage` | Added | [PaymentIntentConfirmPaymentMethodOptionsSatispayParams](/api/payment_intents/confirm?api-version=2026-06-24.dahlia#confirm_payment_intent-payment_method_options-satispay), [PaymentIntentPaymentMethodOptionsSatispay](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options-satispay), [PaymentIntentPaymentMethodOptionsSatispayParams](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay) |
| `Satispay` | Added | [SetupAttemptPaymentMethodDetails](/api/setup_attempts/object?api-version=2026-06-24.dahlia#setup_attempt_object-payment_method_details) |

| Value | Change | Enums |
| --- | --- | --- |
| `satispay` | Added | [InvoicePaymentSettings.PaymentMethodTypes](/api/invoices/object?api-version=2026-06-24.dahlia#invoice_object-payment_settings-PaymentMethodTypes), [SubscriptionPaymentSettings.PaymentMethodTypes](/api/subscriptions/object?api-version=2026-06-24.dahlia#subscription_object-payment_settings-PaymentMethodTypes) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SetupFutureUsage` | Added | [PaymentIntent.PaymentMethodOptions.Satispay](/api/payment_intents/object?api-version=2026-06-24.dahlia#payment_intent_object-payment_method_options-satispay), [PaymentIntentPaymentMethodOptionsSatispayOptions](/api/payment_intents/create?api-version=2026-06-24.dahlia#create_payment_intent-payment_method_options-satispay) |
| `Satispay` | Added | [SetupAttempt.PaymentMethodDetails](/api/setup_attempts/object?api-version=2026-06-24.dahlia#setup_attempt_object-payment_method_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.dahlia`
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

- [Adds buyer ID support for Bizum payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/bizum-payments-buyer-id.md)
- [Enables manual capture for Sunbit payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/enables-manual-capture-for-sunbit-payments.md)
- [Adds buyer ID support for BLIK payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/blik-payments-buyer-id.md)
- [Adds a fingerprint to Pix payment method details](https://docs.stripe.com/changelog/dahlia/2026-06-24/pix-fingerprint-payment-method-details.md)
- [Adds transaction link ID to card payment method details for Mastercard and Maestro transactions](https://docs.stripe.com/changelog/dahlia/2026-06-24/card-payment-method-details-transaction-link-id.md)
- [Adds payment method options for Sunbit in Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-06-24/sunbit-checkout-pmo.md)
- [Adds support for the Sui network and USDsui token for crypto payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/sui-network-and-usdsui-token-support.md)
- [Adds support for Mastercard compliance disputes](https://docs.stripe.com/changelog/dahlia/2026-06-24/mastercard-compliance-disputes.md)
