<!-- Source URL: https://docs.stripe.com/payments/payment-methods/transitioning -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Migrate to the Payment Intents and Payment Methods APIs

Learn how to transition from the Sources and Tokens APIs to the Payment Methods API.

The [Payment Methods API](https://docs.stripe.com/api/payment_methods.md) replaces the existing [Tokens](https://docs.stripe.com/api/tokens.md) and [Sources](https://docs.stripe.com/api/sources.md) APIs as the recommended way for integrations to collect and store payment information. It works with the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to create payments for a wide range of payment methods.

We plan to stop Sources API support for card payments, and to stop support for [Cards](https://docs.stripe.com/api/cards.md). If you currently handle any card payment methods using the Sources API, you must migrate them to the Payment Intents API. We’ll send email communication with more information about the end of support for the Sources API.

This page provides a general overview of the differences between the legacy and current processes. For detailed information about the migration process, see the [legacy cards (Tokens/Cards APIs) and Sources API migration doc](https://docs.stripe.com/payments/payment-methods/migrate-from-legacy-cards-sources.md).

## Migrate to the Payment Intents API

To migrate your integration, update your server and front end to use the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md). Typical integration options include:

- Redirect to [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) for your payment flow.
- Use the Stripe [Payment Element](https://docs.stripe.com/payments/payment-element.md) on your own payment page.
- Build a custom form and use the Stripe JS SDK to complete the payment.

If you use Checkout or the Payment Element, you can add and manage most payment methods from the Stripe Dashboard without making code changes.

For specific information about integrating a card payment method using the Payment Methods API, see the instructions for that payment method in [the payment methods documentation](https://docs.stripe.com/payments/payment-methods/overview.md). The following table provides a high-level comparison of the different payment types.

| Old integration | Stripe Checkout | Payment Element | Custom form |
| --- | --- | --- | --- |
|  | Low complexity | Medium complexity | High complexity |
| Create a Source on the front end or on the server. | Create a `CheckoutSession` on the server. | Create a `PaymentIntent` on the server. | Create a `PaymentIntent` on the server. |
| Authorize payment by loading a widget or redirecting to a third party. | Not needed | Pass the client secret to the front end and use the Stripe JS SDK to render a Payment Element to complete the payment. | Pass the client secret to the front end, use your own form to collect details from your customer, and complete the payment according to the payment method. |
| Confirm the source is chargeable and charge the Source. | Not needed | Not needed | Not needed |
| Confirm that the Charge succeeded asynchronously with the `charge.succeeded` webhook. | Confirm that the Checkout session succeeded with the `payment_intent.succeeded` webhook. | Confirm that the PaymentIntent succeeded with the `payment_intent.succeeded` webhook. | Confirm that the PaymentIntent succeeded with the `payment_intent.succeeded` webhook. |

> #### Continued use of Charge objects
> 
> A `PaymentIntent` object represents a payment in the new integration, and it creates a `Charge` when you confirm the payment on the front end. If you previously stored references to the `Charge`, you can continue to do so by fetching the `Charge` ID from the `PaymentIntent` after the customer completes the payment. However, we also recommend that you store the `PaymentIntent` ID.

### Checking payment status

Previously, your integration should have checked both the status of the `Source` and the status of the `Charge` after each API call. You no longer need to check two objects—you only need to check the status of the `PaymentIntent` or the `CheckoutSession` after you confirm it on the front end.

| payment_intent.status | Meaning |
| --- | --- |
| `succeeded` | The payment succeeded. |
| `requires_payment_method` | The payment failed. |
| `requires_action` | The customer hasn’t completed authorizing the payment, possibly [due to a 3DS requirement](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#check-status). |

Always confirm the status of the `PaymentIntent` by fetching it on your server or listening for the webhook events on your server. Don’t rely solely on the user returning to the `return_url` that’s provided when you confirm the `PaymentIntent`.

### Refunds

You can call the Refunds API using the `PaymentIntent` ID instead of the `Charge` ID.

Alternatively, you can continue to call the Refunds API with the ID of the `Charge` that the `PaymentIntent` creates. You can get the ID of the `Charge` from the [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) property.

### Error handling

Previously, you had to handle errors on the `Source`. With `PaymentIntents`, you instead check for errors on the `PaymentIntent` when it’s created and after the customer has authorized the payment. Most errors on the `PaymentIntent` are of `invalid_request_error` type, returned in an invalid request.

When you migrate your integration, keep in mind that `PaymentIntent` error codes can differ from the corresponding error codes for `Sources`.

### Webhooks

If you previously listened to `Source` events, you might need to update your integration to listen to events for other objects instead. The following table shows some examples.

| Old event | New Checkout event | New PaymentIntent event | Special instructions |
| --- | --- | --- | --- |
| `source.chargeable` | Not applicable | Not applicable |  |
| `source.failed` | Not applicable | Not applicable |  |
| `source.canceled` | Not applicable | Not applicable |  |
| `charge.succeeded` | `checkout.session.completed` | `payment_intent.succeeded` | The `charge.succeeded` event is also sent, so you can continue listening for it instead of the others. |
| `charge.failed` | Not applicable - The customer can re-attempt the payment on the same Checkout Session until it [expires](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-expires_at), at which point you receive a `checkout.session.expired` event. | `payment_intent.payment_failed` | The `charge.failed` event is also sent, so you can continue listening for it instead of the others. |
| `charge.dispute.created` | `charge.dispute.created` | `charge.dispute.created` |  |

## Transition to the Payment Methods API 

The main difference between the Payment Methods and Sources APIs is that Sources describes the transaction state through the [status](https://docs.stripe.com/api/sources/object.md#source_object-status) property. That means that each `Source` object must transition to a chargeable state before you can use it for a payment. By contrast, a `PaymentMethod` is stateless, relying on the PaymentIntent object to represent payment state.

> The following table isn’t a comprehensive list of payment methods. If you integrate other payment methods with the Sources API, migrate them to the Payment Methods API as well.

| Flows | Payment Methods and Payment Intents APIs | Tokens or Sources with Charges APIs |
| --- | --- | --- |
| Cards | [Card payments](https://docs.stripe.com/payments/cards.md) | Deprecated |
| ACH Direct Debit | [US bank account direct debits](https://docs.stripe.com/payments/ach-direct-debit.md) | [Supported on Tokens](https://docs.stripe.com/ach-deprecated.md); Not supported on Sources |

After you choose the API to integrate with, use the [guide to payment methods](https://stripe.com/payments/payment-methods-guide) to help you determine the right payment method types you need to support.

This guide includes detailed descriptions of each payment method and describes the differences in the customer-facing flows, along with the [geographic regions](https://stripe.com/payments/payment-methods-guide#payment-methods-fact-sheets) where they’re most relevant. You can enable any payment method available to you within the [Dashboard](https://dashboard.stripe.com/account/payments/settings). Activation is generally instantaneous and doesn’t require additional contracts.

## See also

- [Guide to payment methods](https://stripe.com/payments/payment-methods-guide)
- [Connect payments](https://docs.stripe.com/connect/charges.md)
- [Payment Methods API reference](https://docs.stripe.com/api/payment_methods.md)
