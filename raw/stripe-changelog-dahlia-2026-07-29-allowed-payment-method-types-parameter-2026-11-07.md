<!-- Source URL: https://docs.stripe.com/changelog/dahlia/2026-07-29/allowed-payment-method-types-parameter -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Adds the allowed payment method types parameter to Payment Intents and Setup Intents

## What’s new

Adds the [allowed_payment_method_types](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-07-29.dahlia#create_payment_intent-allowed_payment_method_types) parameter to [Payment Intents](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-07-29.dahlia) and [Setup Intents](https://docs.stripe.com/api/setup_intents/create.md?api-version=2026-07-29.dahlia). This parameter accepts an array of payment method types and filters the list to only compatible payment methods based on other parameters such as `currency`, `amount`, and `customer`. We reflect the resulting compatible subset in the [payment_method_types](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_types) property of the response.

Unlike the [payment_method_types](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_types) parameter, which returns an error when you specify an incompatible payment method, `allowed_payment_method_types` silently filters out incompatible methods and returns only those that work with the current configuration.

This parameter is mutually exclusive with `payment_method_types`, `excluded_payment_method_types`, `automatic_payment_methods`, and `payment_method_configuration`.

## Impact

If your integration currently uses `payment_method_types` to manually specify which methods to accept, you can switch to `allowed_payment_method_types` to get automatic compatibility filtering instead of errors. To migrate:

- Replace `payment_method_types` with `allowed_payment_method_types` on your create, update, or confirm calls, passing the same array of payment method types you support.
- Remove any error-handling logic that catches incompatible payment method errors, since incompatible types are filtered out automatically.
- Read the `payment_method_types` property on the response to see which of your allowed types we determined to be compatible with the current configuration.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object), [PaymentIntent#confirm](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent), [PaymentIntent#create](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent), [PaymentIntent#update](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent), [SetupIntent](/api/setup_intents/object?api-version=2026-07-29.dahlia#setup_intent_object), [SetupIntent#confirm](/api/setup_intents/confirm?api-version=2026-07-29.dahlia#confirm_setup_intent), [SetupIntent#create](/api/setup_intents/create?api-version=2026-07-29.dahlia#create_setup_intent), [SetupIntent#update](/api/setup_intents/update?api-version=2026-07-29.dahlia#update_setup_intent) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent), [SetupIntent](/api/setup_intents/object?api-version=2026-07-29.dahlia#setup_intent_object), [SetupIntentConfirmParams](/api/setup_intents/confirm?api-version=2026-07-29.dahlia#confirm_setup_intent), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2026-07-29.dahlia#create_setup_intent), [SetupIntentUpdateParams](/api/setup_intents/update?api-version=2026-07-29.dahlia#update_setup_intent) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent), [PaymentIntentModifyParams](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent), [SetupIntent](/api/setup_intents/object?api-version=2026-07-29.dahlia#setup_intent_object), [SetupIntentConfirmParams](/api/setup_intents/confirm?api-version=2026-07-29.dahlia#confirm_setup_intent), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2026-07-29.dahlia#create_setup_intent), [SetupIntentModifyParams](/api/setup_intents/update?api-version=2026-07-29.dahlia#update_setup_intent) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object), [PaymentIntent.confirm().$params](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent), [PaymentIntent.create().$params](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent), [PaymentIntent.update().$params](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent), [SetupIntent](/api/setup_intents/object?api-version=2026-07-29.dahlia#setup_intent_object), [SetupIntent.confirm().$params](/api/setup_intents/confirm?api-version=2026-07-29.dahlia#confirm_setup_intent), [SetupIntent.create().$params](/api/setup_intents/create?api-version=2026-07-29.dahlia#create_setup_intent), [SetupIntent.update().$params](/api/setup_intents/update?api-version=2026-07-29.dahlia#update_setup_intent) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `allowedPaymentMethodTypes` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent), [SetupIntent](/api/setup_intents/object?api-version=2026-07-29.dahlia#setup_intent_object), [SetupIntentConfirmParams](/api/setup_intents/confirm?api-version=2026-07-29.dahlia#confirm_setup_intent), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2026-07-29.dahlia#create_setup_intent), [SetupIntentUpdateParams](/api/setup_intents/update?api-version=2026-07-29.dahlia#update_setup_intent) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent), [SetupIntent](/api/setup_intents/object?api-version=2026-07-29.dahlia#setup_intent_object), [SetupIntentConfirmParams](/api/setup_intents/confirm?api-version=2026-07-29.dahlia#confirm_setup_intent), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2026-07-29.dahlia#create_setup_intent), [SetupIntentUpdateParams](/api/setup_intents/update?api-version=2026-07-29.dahlia#update_setup_intent) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AllowedPaymentMethodTypes` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent), [PaymentIntentParams](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent), [SetupIntent](/api/setup_intents/object?api-version=2026-07-29.dahlia#setup_intent_object), [SetupIntentConfirmParams](/api/setup_intents/confirm?api-version=2026-07-29.dahlia#confirm_setup_intent), [SetupIntentParams](/api/setup_intents/create?api-version=2026-07-29.dahlia#create_setup_intent) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AllowedPaymentMethodTypes` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object), [PaymentIntentConfirmOptions](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent), [PaymentIntentCreateOptions](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent), [PaymentIntentUpdateOptions](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent), [SetupIntent](/api/setup_intents/object?api-version=2026-07-29.dahlia#setup_intent_object), [SetupIntentConfirmOptions](/api/setup_intents/confirm?api-version=2026-07-29.dahlia#confirm_setup_intent), [SetupIntentCreateOptions](/api/setup_intents/create?api-version=2026-07-29.dahlia#create_setup_intent), [SetupIntentUpdateOptions](/api/setup_intents/update?api-version=2026-07-29.dahlia#update_setup_intent) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.dahlia`
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

- [Adds the ability to update shipping options, consent collection, and future usage support on Payment Links](https://docs.stripe.com/changelog/dahlia/2026-07-29/payment-links-update-endpoint-new-parameters.md)
- [Adds the ability to indicate that you don’t intend to reuse Samsung Pay and PAYCO payment method types](https://docs.stripe.com/changelog/dahlia/2026-07-29/samsung-pay-and-payco-setup-future-usage-none-only.md)
- [Adds customer and payment method details to the Refunds API](https://docs.stripe.com/changelog/dahlia/2026-07-29/adds-customer-and-payment-method-details-to-the-refunds-api.md)
- [Adds support for new banks to FPX payments](https://docs.stripe.com/changelog/dahlia/2026-07-29/fpx-payments-new-banks.md)
- [Adds CHAPS as a supported network for funding instructions](https://docs.stripe.com/changelog/dahlia/2026-07-29/chaps-as-supported-networks.md)
- [Adds MB WAY support to the hosted invoice page](https://docs.stripe.com/changelog/dahlia/2026-07-29/hosted-invoice-page-mb-way-support.md)
- [Adds card network details to the Dispute object](https://docs.stripe.com/changelog/dahlia/2026-07-29/dispute-payment-method-details-card-network.md)
- [Adds the ability to list Payment Records](https://docs.stripe.com/changelog/dahlia/2026-07-29/list-payment-records.md)
