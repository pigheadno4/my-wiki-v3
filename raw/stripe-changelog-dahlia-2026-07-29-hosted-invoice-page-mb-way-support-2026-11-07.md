<!-- Source URL: https://docs.stripe.com/changelog/dahlia/2026-07-29/hosted-invoice-page-mb-way-support -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Adds MB WAY support to the hosted invoice page

## What’s new

Adds support for [MB WAY](https://docs.stripe.com/payments/mb-way.md) to the [hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page.md). You can enable MB WAY through the Dashboard or pass `mb_way` to `payment_settings.payment_method_types`  when you [create](https://docs.stripe.com/api/invoices/create.md?api-version=2026-07-29.dahlia#create-payment_settings-payment_method_types) or [update](https://docs.stripe.com/api/invoices/update.md?api-version=2026-07-29.dahlia#update_invoice-payment_settings-payment_method_types) Invoices and [create](https://docs.stripe.com/api/subscriptions/create.md?api-version=2026-07-29.dahlia#create_subscription-payment_settings-payment_method_types) or [update](https://docs.stripe.com/api/subscriptions/update.md?api-version=2026-07-29.dahlia#update_subscription-payment_settings-payment_method_types) Subscriptions. You also need to set [collection_method](https://docs.stripe.com/api/invoices/object.md?api-version=2026-07-29.dahlia#invoice_object-collection_method) for the Invoice or Subscription to `send_invoice`.

## Impact

You can now enable your customers to use MB WAY, a popular payment method in Portugal that supports EUR payments. Because MB WAY requires customer authorization for each payment, it’s only available when you use the `send_invoice` collection method, where customers complete payment through the [hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page.md).

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [Invoice#update.payment_settings.payment_method_types](/api/invoices/update?api-version=2026-07-29.dahlia#update_invoice-payment_settings-payment_method_types), [Invoice#create.payment_settings.payment_method_types](/api/invoices/create?api-version=2026-07-29.dahlia#create-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription#update.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2026-07-29.dahlia#update_subscription-payment_settings-payment_method_types), [Subscription#create.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2026-07-29.dahlia#create_subscription-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-payment_method_types) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [InvoiceModifyParamsPaymentSetting.payment_method_types](/api/invoices/update?api-version=2026-07-29.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParamsPaymentSetting.payment_method_types](/api/invoices/create?api-version=2026-07-29.dahlia#create-payment_settings-payment_method_types), [Invoice.PaymentSetting.payment_method_types](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-payment_method_types), [SubscriptionModifyParamsPaymentSetting.payment_method_types](/api/subscriptions/update?api-version=2026-07-29.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParamsPaymentSetting.payment_method_types](/api/subscriptions/create?api-version=2026-07-29.dahlia#create_subscription-payment_settings-payment_method_types), [Subscription.PaymentSetting.payment_method_types](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-payment_method_types) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-payment_method_types) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [InvoiceUpdateParams.payment_settings.paymentMethodTypes](/api/invoices/update?api-version=2026-07-29.dahlia#update_invoice-payment_settings-paymentMethodTypes), [InvoiceCreateParams.payment_settings.paymentMethodTypes](/api/invoices/create?api-version=2026-07-29.dahlia#create-payment_settings-paymentMethodTypes), [SubscriptionUpdateParams.payment_settings.paymentMethodTypes](/api/subscriptions/update?api-version=2026-07-29.dahlia#update_subscription-payment_settings-paymentMethodTypes), [SubscriptionCreateParams.payment_settings.paymentMethodTypes](/api/subscriptions/create?api-version=2026-07-29.dahlia#create_subscription-payment_settings-paymentMethodTypes) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [InvoiceUpdateParams.payment_settings.payment_method_types](/api/invoices/update?api-version=2026-07-29.dahlia#update_invoice-payment_settings-payment_method_types), [InvoiceCreateParams.payment_settings.payment_method_types](/api/invoices/create?api-version=2026-07-29.dahlia#create-payment_settings-payment_method_types), [Invoice.payment_settings.payment_method_types](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-payment_method_types), [SubscriptionUpdateParams.payment_settings.payment_method_types](/api/subscriptions/update?api-version=2026-07-29.dahlia#update_subscription-payment_settings-payment_method_types), [SubscriptionCreateParams.payment_settings.payment_method_types](/api/subscriptions/create?api-version=2026-07-29.dahlia#create_subscription-payment_settings-payment_method_types), [Subscription.payment_settings.payment_method_types](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-payment_method_types) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `mb_way` | Added | [InvoicePaymentSettings.PaymentMethodTypes](/api/invoices/object?api-version=2026-07-29.dahlia#invoice_object-payment_settings-PaymentMethodTypes), [SubscriptionPaymentSettings.PaymentMethodTypes](/api/subscriptions/object?api-version=2026-07-29.dahlia#subscription_object-payment_settings-PaymentMethodTypes) |

#### .NET

This change doesn’t affect the .NET SDK.

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
- [Adds the allowed payment method types parameter to Payment Intents and Setup Intents](https://docs.stripe.com/changelog/dahlia/2026-07-29/allowed-payment-method-types-parameter.md)
- [Adds card network details to the Dispute object](https://docs.stripe.com/changelog/dahlia/2026-07-29/dispute-payment-method-details-card-network.md)
- [Adds the ability to list Payment Records](https://docs.stripe.com/changelog/dahlia/2026-07-29/list-payment-records.md)
