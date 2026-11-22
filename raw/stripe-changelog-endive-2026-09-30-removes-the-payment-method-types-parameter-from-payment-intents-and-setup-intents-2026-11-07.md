<!-- Source URL: https://docs.stripe.com/changelog/endive/2026-09-30/removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Removes the payment method types parameter from Payment Intents and Setup Intents

## What’s new

Removes `payment_method_types` as a writable parameter from the [create](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive), [update](https://docs.stripe.com/api/payment_intents/update.md?api-version=2026-09-30.endive), and [confirm](https://docs.stripe.com/api/payment_intents/confirm.md?api-version=2026-09-30.endive) methods on Payment Intents, and from the [create](https://docs.stripe.com/api/setup_intents/create.md?api-version=2026-09-30.endive) and [update](https://docs.stripe.com/api/setup_intents/update.md?api-version=2026-09-30.endive) methods on Setup Intents. Passing `payment_method_types` on this API version returns a 400 error with the code `payment_method_types_no_longer_supported`.

Use [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to automatically determine available payment methods based on other parameters such as `currency`, `amount`, and `customer`. If you need more control:

- Use [excluded_payment_method_types](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-excluded_payment_method_types) to exclude specific types from the set determined by dynamic payment methods.
- Use [allowed_payment_method_types](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-09-30.endive#create_payment_intent-allowed_payment_method_types) to specify a list of types you want to accept. Stripe filters out incompatible types instead of returning an error.

`payment_method_types` remains as a read-only property on the [Payment Intent](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.endive#payment_intent_object-payment_method_types) and [Setup Intent](https://docs.stripe.com/api/setup_intents/object.md?api-version=2026-09-30.endive#setup_intent_object-payment_method_types) objects, reflecting the computed list of available payment methods.

## Why is this a breaking change?

Previously, `payment_method_types` accepted a list of payment method types to explicitly set which methods are available on a PaymentIntent or SetupIntent. This parameter is no longer writable. Requests that pass `payment_method_types` on the affected endpoints return a `400` error.

To migrate, use [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) and remove `payment_method_types` and manage available methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically filters for compatibility. Use `excluded_payment_method_types` to exclude specific types per request.

If you need more control, you can also use `allowed_payment_method_types` to pass a list of types you want to accept, similar to the old `payment_method_types` parameter. Incompatible types are silently filtered rather than returning an error.

## Impact

If your integration passes `payment_method_types` when creating, updating, or confirming a Payment Intent or Setup Intent, remove it before upgrading to API version `2026-08-26.preview`. Replace it with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) (optionally combined with `excluded_payment_method_types`), or use `allowed_payment_method_types`. Dynamic payment methods automatically handle compatibility filtering, so you no longer need to maintain eligibility logic in your code.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `payment_method_types` | Removed | [PaymentIntent#confirm](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent), [PaymentIntent#create](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent), [PaymentIntent#update](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent), [SetupIntent#create](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent), [SetupIntent#update](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_method_types` | Removed | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent), [SetupIntentUpdateParams](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_method_types` | Removed | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent), [PaymentIntentModifyParams](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent), [SetupIntentModifyParams](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_method_types` | Removed | [PaymentIntent.confirm().$params](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent), [PaymentIntent.create().$params](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent), [PaymentIntent.update().$params](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent), [SetupIntent.create().$params](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent), [SetupIntent.update().$params](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `paymentMethodTypes` | Removed | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent), [SetupIntentUpdateParams](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_method_types` | Removed | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent), [SetupIntentUpdateParams](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PaymentMethodTypes` | Removed | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent), [PaymentIntentParams](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent), [SetupIntentParams](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PaymentMethodTypes` | Removed | [PaymentIntentConfirmOptions](/api/payment_intents/confirm?api-version=2026-09-30.endive#confirm_payment_intent), [PaymentIntentCreateOptions](/api/payment_intents/create?api-version=2026-09-30.endive#create_payment_intent), [PaymentIntentUpdateOptions](/api/payment_intents/update?api-version=2026-09-30.endive#update_payment_intent), [SetupIntentCreateOptions](/api/setup_intents/create?api-version=2026-09-30.endive#create_setup_intent), [SetupIntentUpdateOptions](/api/setup_intents/update?api-version=2026-09-30.endive#update_setup_intent) |

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
- [Returns specific decline codes for BLIK payment failures](https://docs.stripe.com/changelog/endive/2026-09-30/blik-granular-decline-codes.md)
- [Deprecates the payment request button](https://docs.stripe.com/changelog/endive/2026-09-30/deprecate-payment-request-button.md)
- [Shows pending-authorization UI for MB WAY, Bizum, and BLIK with stripe.handleNextAction](https://docs.stripe.com/changelog/endive/2026-09-30/handle-next-action-mb-way-bizum-ui.md)
- [Removes support for the payment method types option in Elements](https://docs.stripe.com/changelog/endive/2026-09-30/remove-elements-deferred-intent-payment-method-types.md)
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
