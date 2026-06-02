<!-- Source URL: https://docs.stripe.com/payments/payment-intents/migration/charges -->
<!-- Fetched: 2026-04-20 -->

# Charges versus Payment Intents APIs

Learn about the differences between Stripe's two core payment APIs and when to use them.

## Understanding the Stripe payment APIs

There are three ways to accept payments on Stripe today:

- Stripe Checkout
- Charges API
- _Payment Intents API_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods)

[Stripe Checkout](https://docs.stripe.com/payments/checkout.md) is a prebuilt payment page that you can redirect your customer to for simple purchases and _subscriptions_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis). It provides many features, such as Apple Pay, Google Pay, internationalization, and form validation.

The [Charges](https://docs.stripe.com/api/charges.md) and [Payment Intents](https://docs.stripe.com/api/payment_intents.md) APIs let you build custom payment flows and experiences.

The Payment Intents API is the unifying API for all Stripe products and payment methods. While we aren’t deprecating Charges, new features are only available with the Payment Intents API.

For a full feature comparison, see the table below:

| Charges API                                                                                           | Payment Intents API                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Used by businesses with customers primarily in the US / Canada who want a simple way to accept cards. | Required for businesses that accept multiple payment methods and cards requiring authentication (for example, due to _Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) in Europe). |
| Works on Web, iOS, and Android.                                                                       | Works on Web, iOS, and Android. Can also be used to accept in-store payments with Terminal.                                                                                                                                                                                                                                                                                                                         |
| Supports cards and all payment methods on the [Sources API](https://docs.stripe.com/sources.md).      | Supports cards, cards requiring 3DS, iDEAL, SEPA, and [many other payment methods](https://docs.stripe.com/payments/payment-methods/overview.md).                                                                                                                                                                                                                                                                   |
| Is **not SCA** ready                                                                                  | _Is SCA ready_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase)                                                                                                                                                    |

## Migrating code that reads from charges

If you have an application with multiple payment flows and incrementally migrating each one from the Charges API to the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md), you should first update any code that reads from the [Charge](https://docs.stripe.com/api/charges.md) object. To help with this, the charge object has two additional properties, [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) and [billing_details](https://docs.stripe.com/api/charges/object.md#charge_object-billing_details), which provide a consistent interface for reading the details of the payment method used for the charge.

These fields are available on all API versions and on charge objects created with both the Charges API and the Payment Intents API.

The following table shows commonly used properties on a charge and how the same information can be accessed using the additional properties:

#### Cards and bank accounts

| Description                                                           | Before                                                                                                                      | After                                                                                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Details about the payment method used to create a charge              | `charge.source`                                                                                                             | `charge.payment_method_details`                                                                                                 |
| ID of the payment method used for the charge                          | `charge.source.id`                                                                                                          | `charge.payment_method`                                                                                                         |
| Type of payment method used                                           | `charge.source.object` (for example, `card` or `bank_account`)                                                              | `charge.payment_method_details.type`                                                                                            |
| Billing information for the charge (for example, billing postal code) | `charge.source.address_zip`                                                                                                 | `charge.billing_details.address.postal_code`                                                                                    |
| Name of the cardholder                                                | `charge.source.name`                                                                                                        | `charge.billing_details.name`                                                                                                   |
| Last 4 digits of the card used                                        | `charge.source.last4`                                                                                                       | `charge.payment_method_details.card.last4`                                                                                      |
| Fingerprint of the card                                               | `charge.source.fingerprint`                                                                                                 | `charge.payment_method_details.card.fingerprint`                                                                                |
| CVC verification status for the charge                                | `charge.source.cvc_check`                                                                                                   | `charge.payment_method_details.card.checks.cvc_check`                                                                           |
| Card brand values                                                     | `charge.source.brand` can be one of: `American Express`, `Diners Club`, `Discover`, `JCB`, `MasterCard`, `UnionPay`, `Visa` | `charge.payment_method_details.card.brand` can be one of: `amex`, `diners`, `discover`, `jcb`, `mastercard`, `unionpay`, `visa` |
| Google Pay enum value                                                 | `charge.source.tokenization_method` is `android_pay`                                                                        | `card.wallet.type` within `charge.payment_method_details` is `google_pay`                                                       |

#### Sources

| Description                                                           | Before                                                                                                                           | After                                                                                                                           |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Details about the payment method used to create a charge              | `charge.source`                                                                                                                  | `charge.payment_method_details`                                                                                                 |
| ID of the payment method used for the charge                          | `charge.source.id` (`charge.source.three_d_secure.card` if 3D Secure source used)                                                | `charge.payment_method`                                                                                                         |
| Type of payment method used                                           | `charge.source.object == 'source' && charge.source.type` (unless `charge.source.type` is `three_d_secure`)                       | `charge.payment_method_details.type`                                                                                            |
| Billing information for the charge (for example, billing postal code) | `charge.source.owner.address.postal_code`                                                                                        | `charge.billing_details.address.postal_code`                                                                                    |
| Name of the cardholder                                                | `charge.source.owner.name`                                                                                                       | `charge.billing_details.name`                                                                                                   |
| Last 4 digits of the card used                                        | `charge.source.card.last4` `charge.source.three_d_secure.last4`                                                                  | `charge.payment_method_details.card.last4`                                                                                      |
| Whether or not 3D Secure was successful                               | `charge.source.object == 'source' && charge.source.type == 'three_d_secure'`                                                     | `charge.payment_method_details.card.three_d_secure.succeeded`                                                                   |
| Fingerprint of the card                                               | `charge.source.card.fingerprint`                                                                                                 | `charge.payment_method_details.card.fingerprint`                                                                                |
| CVC verification status for the charge                                | `charge.source.card.cvc_check`                                                                                                   | `charge.payment_method_details.card.checks.cvc_check`                                                                           |
| Card brand values                                                     | `charge.source.card.brand` can be one of: `American Express`, `Diners Club`, `Discover`, `JCB`, `MasterCard`, `UnionPay`, `Visa` | `charge.payment_method_details.card.brand` can be one of: `amex`, `diners`, `discover`, `jcb`, `mastercard`, `unionpay`, `visa` |
| Google Pay enum value                                                 | `charge.source.card.tokenization_method` is `android_pay`                                                                        | `card.wallet.type` within `charge.payment_method_details` is `google_pay`                                                       |

## See also

- [Migrate to Payment Intents](https://docs.stripe.com/payments/payment-intents/migration.md)
