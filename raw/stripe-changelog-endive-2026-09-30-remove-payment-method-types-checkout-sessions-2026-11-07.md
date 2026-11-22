<!-- Source URL: https://docs.stripe.com/changelog/endive/2026-09-30/remove-payment-method-types-checkout-sessions -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Removes the payment method types parameter from Checkout Sessions

## What’s new

Removes the [payment_method_types](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive#create_checkout_session-payment_method_types) parameter from the [create Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive) method. You can no longer pass `payment_method_types` when you create a Checkout Session. Use [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to manage payment methods from the Dashboard without writing code.

You can also use [excluded_payment_method_types](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive#create_checkout_session-excluded_payment_method_types) to exclude specific payment methods from the dynamic payment methods results or the new [allowed_payment_method_types](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive#create_checkout_session-allowed_payment_method_types) parameter to specify a set of payment methods.

The [allowed_payment_method_types](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive#create_checkout_session-allowed_payment_method_types)  parameter accepts an array of payment method type and filters the list to only compatible payment methods based on other parameters such as `currency`, `amount`, and `customer`. The compatible subset is shown in the [payment_method_types](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2026-09-30.endive#checkout_session_object-payment_method_types) property of the response.

Previously, [payment_method_types](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-08-26.dahlia#create_checkout_session-payment_method_types) returned an error when you specified an incompatible payment method. `allowed_payment_method_types` silently filters out incompatible methods and returns only those that work with the current configuration.

## Why is this a breaking change?

Passing `payment_method_types` as a parameter when you [create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive) now returns a `400` error. If your integration sets this parameter, you must remove it and migrate to [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) or [allowed_payment_method_types](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-09-30.endive#create_checkout_session-allowed_payment_method_types).

## Impact

This migration requires careful attention if your integration passes `payment_method_types` when creating a Checkout Session. You must update your integration to use [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) or switch to `allowed_payment_method_types` to get automatic compatibility filtering instead of errors. Requests that include `payment_method_types` on this now return a `400` error.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-09-30.endive#checkout_session_object), [Checkout.Session#create](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |
| `payment_method_types` | Removed | [Checkout.Session#create](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [Checkout::Session](/api/checkout/sessions/object?api-version=2026-09-30.endive#checkout_session_object), [Checkout::SessionCreateParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |
| `payment_method_types` | Removed | [Checkout::SessionCreateParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-09-30.endive#checkout_session_object), [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |
| `payment_method_types` | Removed | [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-09-30.endive#checkout_session_object), [Checkout\Session.create().$params](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |
| `payment_method_types` | Removed | [Checkout\Session.create().$params](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allowedPaymentMethodTypes` | Added | [checkout.Session](/api/checkout/sessions/object?api-version=2026-09-30.endive#checkout_session_object), [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |
| `paymentMethodTypes` | Removed | [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `allowed_payment_method_types` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-09-30.endive#checkout_session_object), [Checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |
| `payment_method_types` | Removed | [Checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AllowedPaymentMethodTypes` | Added | [CheckoutSession](/api/checkout/sessions/object?api-version=2026-09-30.endive#checkout_session_object), [CheckoutSessionParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |
| `PaymentMethodTypes` | Removed | [CheckoutSessionParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AllowedPaymentMethodTypes` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2026-09-30.endive#checkout_session_object), [Checkout.SessionCreateOptions](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |
| `PaymentMethodTypes` | Removed | [Checkout.SessionCreateOptions](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session) |

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
