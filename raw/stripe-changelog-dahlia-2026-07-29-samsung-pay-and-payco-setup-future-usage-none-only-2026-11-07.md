<!-- Source URL: https://docs.stripe.com/changelog/dahlia/2026-07-29/samsung-pay-and-payco-setup-future-usage-none-only -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Adds the ability to indicate that you don't intend to reuse Samsung Pay and PAYCO payment method types

## What’s new

Adds the ability to explicitly indicate that you don’t intend to reuse the `samsung_pay` and `payco` payment method types for future payments by setting the [setup_future_usage](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-samsung_pay-setup_future_usage) parameter to `none`.

## Impact

For [Payment Intents](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-07-29.dahlia) and [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2026-07-29.dahlia) using `samsung_pay` or `payco` as payment method types, you can now set `setup_future_usage` to `none` to indicate you won’t save the payment method for future use.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `setup_future_usage` | Added | [Checkout.Session#create.payment_method_options.payco](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-payco), [Checkout.Session#create.payment_method_options.samsung_pay](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-samsung_pay), [Checkout.Session.payment_method_options.payco](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-payco), [Checkout.Session.payment_method_options.samsung_pay](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-samsung_pay), [PaymentIntent#confirm.payment_method_options.payco](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-payco), [PaymentIntent#confirm.payment_method_options.samsung_pay](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-samsung_pay), [PaymentIntent#create.payment_method_options.payco](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-payco), [PaymentIntent#create.payment_method_options.samsung_pay](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-samsung_pay), [PaymentIntent#update.payment_method_options.payco](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-payco), [PaymentIntent#update.payment_method_options.samsung_pay](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-samsung_pay), [PaymentIntent.payment_method_options.payco](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-payco), [PaymentIntent.payment_method_options.samsung_pay](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-samsung_pay) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [Checkout::Session::PaymentMethodOption::Payco](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-payco), [Checkout::Session::PaymentMethodOption::SamsungPay](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-samsung_pay), [Checkout::SessionCreateParams::PaymentMethodOption::Payco](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-payco), [Checkout::SessionCreateParams::PaymentMethodOption::SamsungPay](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-samsung_pay), [PaymentIntent::PaymentMethodOption::Payco](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-payco), [PaymentIntent::PaymentMethodOption::SamsungPay](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-samsung_pay), [PaymentIntentConfirmParams::PaymentMethodOption::Payco](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-payco), [PaymentIntentConfirmParams::PaymentMethodOption::SamsungPay](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-samsung_pay), [PaymentIntentCreateParams::PaymentMethodOption::Payco](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-payco), [PaymentIntentCreateParams::PaymentMethodOption::SamsungPay](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-samsung_pay), [PaymentIntentUpdateParams::PaymentMethodOption::Payco](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-payco), [PaymentIntentUpdateParams::PaymentMethodOption::SamsungPay](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-samsung_pay) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [Checkout.Session.PaymentMethodOption.Payco](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-payco), [Checkout.Session.PaymentMethodOption.SamsungPay](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-samsung_pay), [PaymentIntent.PaymentMethodOption.Payco](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-payco), [PaymentIntent.PaymentMethodOption.SamsungPay](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-samsung_pay), [PaymentIntentConfirmParamsPaymentMethodOptionPayco](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-payco), [PaymentIntentConfirmParamsPaymentMethodOptionSamsungPay](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-samsung_pay), [PaymentIntentCreateParamsPaymentMethodOptionPayco](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-payco), [PaymentIntentCreateParamsPaymentMethodOptionSamsungPay](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-samsung_pay), [PaymentIntentModifyParamsPaymentMethodOptionPayco](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-payco), [PaymentIntentModifyParamsPaymentMethodOptionSamsungPay](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-samsung_pay), [checkout.SessionCreateParamsPaymentMethodOptionPayco](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-payco), [checkout.SessionCreateParamsPaymentMethodOptionSamsungPay](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-samsung_pay) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [Checkout.Session.payment_method_options.payco](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-payco), [Checkout.Session.payment_method_options.samsung_pay](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-samsung_pay), [Checkout\Session.create().$params.payment_method_option.payco](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-payco), [Checkout\Session.create().$params.payment_method_option.samsung_pay](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-samsung_pay), [PaymentIntent.confirm().$params.payment_method_option.payco](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-payco), [PaymentIntent.confirm().$params.payment_method_option.samsung_pay](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-samsung_pay), [PaymentIntent.create().$params.payment_method_option.payco](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-payco), [PaymentIntent.create().$params.payment_method_option.samsung_pay](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-samsung_pay), [PaymentIntent.payment_method_options.payco](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-payco), [PaymentIntent.payment_method_options.samsung_pay](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-samsung_pay), [PaymentIntent.update().$params.payment_method_option.payco](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-payco), [PaymentIntent.update().$params.payment_method_option.samsung_pay](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-samsung_pay) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `setupFutureUsage` | Added | [PaymentIntent.payment_method_options.payco](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-payco), [PaymentIntent.payment_method_options.samsung_pay](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-samsung_pay), [PaymentIntentConfirmParams.payment_method_options.payco](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-payco), [PaymentIntentConfirmParams.payment_method_options.samsung_pay](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-samsung_pay), [PaymentIntentCreateParams.payment_method_options.payco](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-payco), [PaymentIntentCreateParams.payment_method_options.samsung_pay](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-samsung_pay), [PaymentIntentUpdateParams.payment_method_options.payco](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-payco), [PaymentIntentUpdateParams.payment_method_options.samsung_pay](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-samsung_pay), [checkout.Session.payment_method_options.payco](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-payco), [checkout.Session.payment_method_options.samsung_pay](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-samsung_pay), [checkout.SessionCreateParams.payment_method_options.payco](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-payco), [checkout.SessionCreateParams.payment_method_options.samsung_pay](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-samsung_pay) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [Checkout.Session.payment_method_options.payco](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-payco), [Checkout.Session.payment_method_options.samsung_pay](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-samsung_pay), [Checkout.SessionCreateParams.payment_method_options.payco](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-payco), [Checkout.SessionCreateParams.payment_method_options.samsung_pay](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-samsung_pay), [PaymentIntent.payment_method_options.payco](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-payco), [PaymentIntent.payment_method_options.samsung_pay](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-samsung_pay), [PaymentIntentConfirmParams.payment_method_options.payco](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-payco), [PaymentIntentConfirmParams.payment_method_options.samsung_pay](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-samsung_pay), [PaymentIntentCreateParams.payment_method_options.payco](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-payco), [PaymentIntentCreateParams.payment_method_options.samsung_pay](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-samsung_pay), [PaymentIntentUpdateParams.payment_method_options.payco](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-payco), [PaymentIntentUpdateParams.payment_method_options.samsung_pay](/api/payment_intents/update?api-version=2026-07-29.dahlia#update_payment_intent-payment_method_options-samsung_pay) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SetupFutureUsage` | Added | [CheckoutSessionPaymentMethodOptionsPayco](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-payco), [CheckoutSessionPaymentMethodOptionsPaycoParams](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-payco), [CheckoutSessionPaymentMethodOptionsSamsungPay](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-samsung_pay), [CheckoutSessionPaymentMethodOptionsSamsungPayParams](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-samsung_pay), [PaymentIntentConfirmPaymentMethodOptionsPaycoParams](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-payco), [PaymentIntentConfirmPaymentMethodOptionsSamsungPayParams](/api/payment_intents/confirm?api-version=2026-07-29.dahlia#confirm_payment_intent-payment_method_options-samsung_pay), [PaymentIntentPaymentMethodOptionsPayco](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-payco), [PaymentIntentPaymentMethodOptionsPaycoParams](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-payco), [PaymentIntentPaymentMethodOptionsSamsungPay](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-samsung_pay), [PaymentIntentPaymentMethodOptionsSamsungPayParams](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-samsung_pay) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SetupFutureUsage` | Added | [Checkout.Session.PaymentMethodOptions.Payco](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-payco), [Checkout.Session.PaymentMethodOptions.SamsungPay](/api/checkout/sessions/object?api-version=2026-07-29.dahlia#checkout_session_object-payment_method_options-samsung_pay), [CheckoutSessionPaymentMethodOptionsPaycoOptions](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-payco), [CheckoutSessionPaymentMethodOptionsSamsungPayOptions](/api/checkout/sessions/create?api-version=2026-07-29.dahlia#create_checkout_session-payment_method_options-samsung_pay), [PaymentIntent.PaymentMethodOptions.Payco](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-payco), [PaymentIntent.PaymentMethodOptions.SamsungPay](/api/payment_intents/object?api-version=2026-07-29.dahlia#payment_intent_object-payment_method_options-samsung_pay), [PaymentIntentPaymentMethodOptionsPaycoOptions](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-payco), [PaymentIntentPaymentMethodOptionsSamsungPayOptions](/api/payment_intents/create?api-version=2026-07-29.dahlia#create_payment_intent-payment_method_options-samsung_pay) |

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
- [Adds customer and payment method details to the Refunds API](https://docs.stripe.com/changelog/dahlia/2026-07-29/adds-customer-and-payment-method-details-to-the-refunds-api.md)
- [Adds support for new banks to FPX payments](https://docs.stripe.com/changelog/dahlia/2026-07-29/fpx-payments-new-banks.md)
- [Adds CHAPS as a supported network for funding instructions](https://docs.stripe.com/changelog/dahlia/2026-07-29/chaps-as-supported-networks.md)
- [Adds the allowed payment method types parameter to Payment Intents and Setup Intents](https://docs.stripe.com/changelog/dahlia/2026-07-29/allowed-payment-method-types-parameter.md)
- [Adds MB WAY support to the hosted invoice page](https://docs.stripe.com/changelog/dahlia/2026-07-29/hosted-invoice-page-mb-way-support.md)
- [Adds card network details to the Dispute object](https://docs.stripe.com/changelog/dahlia/2026-07-29/dispute-payment-method-details-card-network.md)
- [Adds the ability to list Payment Records](https://docs.stripe.com/changelog/dahlia/2026-07-29/list-payment-records.md)
