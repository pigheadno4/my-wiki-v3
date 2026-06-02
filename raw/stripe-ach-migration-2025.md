<!-- Source URL: https://docs.stripe.com/payments/ach-direct-debit/migrating-to-new-apis -->
<!-- Fetched: 2026-05-02 -->

# Migrating to new ACH Direct Debit APIs

Learn why and how to migrate to new APIs.

Stripe is removing support for [ACH Direct Debit](https://docs.stripe.com/ach-deprecated.md) using [legacy integrations](https://docs.stripe.com/payments/ach-direct-debit/migrating-to-new-apis.md#identifying-legacy-payments).

If you create legacy ACH Direct Debit payments, you must migrate to the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md) or [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md).

## Feature comparison

Stripe’s new APIs offer features that aren’t available in legacy integrations:

| Feature                                                                                                       | Legacy Integrations                                     | Payment Intents API or Checkout Sessions API                                                          |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Checkout support                                                                                              | No                                                      | Yes                                                                                                   |
| Payment Element support                                                                                       | No                                                      | Yes                                                                                                   |
| [Dynamic payment method support](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) | No                                                      | Yes                                                                                                   |
| Settlement speed                                                                                              | T+6                                                     | T+4 (T+2 when using [faster settlement](https://docs.stripe.com/payments/ach-direct-debit.md#timing)) |
| Instant bank account verification                                                                             | Only available through custom, third-party integrations | Instant verification with [Financial Connections](https://docs.stripe.com/financial-connections.md)   |
| Fraud prevention                                                                                              | No                                                      | - Radar for ACH                                                                                       |

- Balance checks using Financial Connections
- Smart Retries |
  | Supported countries | US | US, EU, and UK |

## Compare the Checkout Sessions and Payment Intents APIs

Stripe offers two new APIs to accept ACH Direct Debits payments: Payment Intents and Checkout Sessions APIs.

- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md): Supports common checkout workflows with built-in features that remove the need for custom code and is recommended for most developers.

- [Payment Intents API](https://docs.stripe.com/api/payment_intents.md): A lower-level API for building your own checkout flow. It requires significantly more code and ongoing maintenance. We recommend [Checkout Sessions](https://docs.stripe.com/payments/quickstart-checkout-sessions.md) for most integrations.

[Learn more](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison.md#feature-comparison) about the differences, and how to evaluate which is right for you.

## Build an ACH Direct Debit integration

To build an ACH Direct Debit integration on Payment Intents or Checkout Sessions:

1. Enable ACH Direct Debit in your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

1. To collect and use new payment methods, integrate with [ACH on Payment Intents or Checkout Sessions](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md).

1. For bank accounts previously collected using the [Tokens API](https://docs.stripe.com/ach-deprecated.md), you can continue to use saved `BankAccount` objects as `PaymentMethod` objects with the Payment Intents API. For details, see [Migrate existing bank accounts](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges.md).

1. [Test your integration](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md?web-or-mobile=web&payments-ui-type=direct-api#test-integration).

1. Gradually migrate all payments using existing bank accounts to the Payment Intents or Checkout Sessions API.

1. Remove your legacy integration.

## Behavioral differences

Some features that exist in both APIs work differently. If you rely on any of the following behaviors, update your integration accordingly.

| Behavior | Legacy Integrations      | Payment Intents or Checkout Sessions API                                      |
| -------- | ------------------------ | ----------------------------------------------------------------------------- |
| Mandates | Not enforced by the API. | - Enforced by the API. Payments can’t be initiated without an active mandate. |

- Mandates can become inactive, which renders the payment method unusable. This can occur when a customer disputes a payment, when certain payment failures occur, or when Stripe becomes aware that the payment method is no longer valid. For more information, see [Blocked bank accounts](https://docs.stripe.com/payments/ach-direct-debit/blocked-bank-accounts.md).
- If you reuse bank accounts created with the Tokens API, you must first create mandates for them. See [Migrate existing bank accounts](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges.md#mandate-acknowledgement). |
  | Balance transactions | - Created when the charge is created.
- The `Balance transaction` object is present in the `charge.pending` event and the API response. | - Created when the payment is submitted to the banking partner.
- The `Balance transaction` object is present in the `charge.updated` event, but not the API response. |
  | Balance type | Funds settle in `source_type=bank_account`. | - Funds settle in `source_type=card`, shared with cards and other payment methods.
- If you manually specify the balance type for payouts or Connect transfers, update your integration to use the new balance type.
- During migration, you receive one payout for each balance type until all new payments use the new API.
- For separate charges and transfers with `source_transaction`, wait for the `charge.updated` webhook before creating a transfer. |
  | Microdeposits | - Two microdeposits of random, small amounts for verification.
- No hosted verification UI. | - One 1¢ microdeposit with a descriptor code for verification. In rare cases, Stripe sends two microdeposits of random, small amounts instead.
- Stripe provides a [hosted verification page](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment.md?web-or-mobile=web&payments-ui-type=direct-api#web-verify-with-microdeposits) and sends automatic reminder emails to customers.
- Customers must verify their bank account within 10 days. If they don’t verify in time, the PaymentIntent or SetupIntent reverts to requiring new payment method details. |
  | Emails | Stripe doesn’t send automatic emails. | - Stripe automatically emails customers a mandate confirmation when mandates are created.
- When a customer attempts to verify a bank account using microdeposits, Stripe emails customers with a link to a hosted verification page.
- You can [disable Stripe emails](https://dashboard.stripe.com/settings/emails) and send custom notifications instead. For sample mandate text and required content, see [Mandate and microdeposit emails](https://docs.stripe.com/payments/ach-direct-debit.md#mandate-and-microdeposit-emails). |

## Webhook differences

If you previously listened to Charge events, you might need to update your integration to listen to new event types. The following table shows how webhook events differ.

| Old webhook              | New webhook on Checkout                                                                                                                                                                                                                                             | New webhook on Payment Intents  | Special instructions                                                                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `charge.pending`         | `payment_intent.processing`                                                                                                                                                                                                                                         | `payment_intent.processing`     | In legacy integrations, `charge.pending` includes balance transaction. In new integrations, the balance transaction isn’t available until the `charge.updated` event. |
| `charge.updated`         | `charge.updated`                                                                                                                                                                                                                                                    | `charge.updated`                | Sent when the payment is submitted to the banking partner. Includes the balance transaction.                                                                          |
| `charge.succeeded`       | `checkout.session.completed`                                                                                                                                                                                                                                        | `payment_intent.succeeded`      | The `charge.succeeded` webhook is also sent, so you don’t have to update your integration to listen to the new webhook.                                               |
| `charge.failed`          | Not applicable. The customer can re-attempt the payment on the same Checkout Session until it [expires](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-expires_at), at which point you receive a `checkout.session.expired` event. | `payment_intent.payment_failed` | The `charge.failed` webhook is also sent, so you don’t have to update your integration to listen to the new webhook.                                                  |
| `charge.dispute.created` | `charge.dispute.created`                                                                                                                                                                                                                                            | `charge.dispute.created`        | Not applicable                                                                                                                                                        |
| Not applicable           | `mandate.updated`                                                                                                                                                                                                                                                   | `mandate.updated`               | Sent when a mandate becomes inactive.                                                                                                                                 |

## Identify Legacy ACH Payments

On a [Charge](https://docs.stripe.com/api/charges/object.md) object, the `payment_method_details.type` property is `ach_debit` for the legacy integration and `us_bank_account` for the newer integration.

A legacy ACH payment is created when a legacy `BankAccount` is the payment [source](https://docs.stripe.com/api/charges/object.md#charge_object-source). This happens when:

- You call the [Create Charge API](https://docs.stripe.com/api/charges/create.md).
- A [Subscription](https://docs.stripe.com/billing/subscriptions/overview.md) or [Invoice](https://docs.stripe.com/invoicing/overview.md) charges a customer whose `default_source` is a legacy BankAccount, and no `default_payment_method` is set on the customer, subscription, or invoice.
- You call the PaymentIntent API with a `payment_method_type` of `ach_debit`.
