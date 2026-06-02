<!-- Source URL: https://docs.stripe.com/payments/payment-methods/transitioning -->
<!-- Fetched: 2026-04-20 -->

# Migrate to the Payment Intents and Payment Methods APIs

Learn how to transition from the Sources and Tokens APIs to the Payment Methods API.

The [Payment Methods API](https://docs.stripe.com/api/payment_methods.md) replaces the existing [Tokens](https://docs.stripe.com/api/tokens.md) and [Sources](https://docs.stripe.com/api/sources.md) APIs as the recommended way for integrations to collect and store payment information. It works with the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to create payments for a wide range of payment methods.

We plan to turn off Sources API support for _local payment methods_ (Payment methods used in specific countries or regions, such as bank transfers, vouchers, and digital wallets. Examples include Pix (Brazil, bank transfers), Konbini (Japan, vouchers), and WeChat Pay (China, digital wallet)). If you currently handle any local payment methods using the Sources API, you must [migrate them to the Payment Methods API](https://docs.stripe.com/payments/payment-methods/transitioning.md#migrate-local-payment-methods). We’ll send email communication with more information about the end of support for the Sources and Tokens APIs.

While we don’t plan to turn off support for card payment methods, we still recommend that you migrate them to the Payment Methods and Payment Intents APIs. For more information about migrating card payment methods, see [Migrating to the Payment Intents API](https://docs.stripe.com/payments/payment-intents/migration.md).

## Migrate local payment methods from the Sources API to the Payment Intents API

To migrate your integration for local payment methods, update your server and front end to use the [PaymentIntents API](https://docs.stripe.com/api/payment_intents.md). There are three typical integration options:

- Redirect to [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) for your payment flow.
- Use the Stripe [Payment Element](https://docs.stripe.com/payments/payment-element.md) on your own payment page.
- Build your own form and use the Stripe JS SDK to complete the payment.

If you use Stripe Checkout or the Payment Element, you can add and manage most payment methods from the Stripe Dashboard without making code changes.

For specific information about integrating a local payment method using the Payment Methods API, see the instructions for that payment method in [the payment methods documentation](https://docs.stripe.com/payments/payment-methods/overview.md). The following table provides a high-level comparison of the different payment types.

| Old integration                                                                 | Stripe Checkout                                                                    | Payment Element                                                                                                       | Own form                                                                                                                                                   |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                 | Low complexity                                                                     | Medium complexity                                                                                                     | High complexity                                                                                                                                            |
| Create a Source on the front end or on the server                               | Create a Checkout Session on the server                                            | Create a PaymentIntent on the server                                                                                  | Create a PaymentIntent on the server                                                                                                                       |
| Authorize payment by loading a widget or redirecting to a third party           | Not needed                                                                         | Pass the client secret to the front end and use the Stripe JS SDK to render a Payment Element to complete the payment | Pass the client secret to the front end, use your own form to collect details from your customer, and complete the payment according to the payment method |
| Confirm the source is chargeable and charge the Source                          | Not needed                                                                         | Not needed                                                                                                            | Not needed                                                                                                                                                 |
| Confirm the Charge succeeded asynchronously with the `charge.succeeded` webhook | Confirm the Checkout session succeeded with the `payment_intent.succeeded` webhook | Confirm the PaymentIntent succeeded with the `payment_intent.succeeded` webhook                                       | Confirm the PaymentIntent succeeded with the `payment_intent.succeeded` webhook                                                                            |

> A PaymentIntent object represents a payment in the new integration, and it creates a Charge when you confirm the payment on the front end. If you previously stored references to the Charge, you can continue to do so by fetching the Charge ID from the PaymentIntent after the customer completes the payment. However, we also recommend that you store the PaymentIntent ID.

### Checking payment status

Previously, your integration should have checked both the status of the Source and the status of the Charge after each API call. You no longer need to check two statuses—you only need to check the status of the PaymentIntent or the Checkout Session after you confirm it on the front end.

| payment_intent.status     | Meaning                                                | Special instructions                                                                                                                                              |
| ------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `succeeded`               | The payment succeeded.                                 | Not applicable                                                                                                                                                    |
| `requires_payment_method` | The payment failed.                                    | Not applicable                                                                                                                                                    |
| `requires_action`         | The customer hasn’t completed authorizing the payment. | If the customer doesn’t complete the payment within 48 hours, then the PaymentIntent transitions to `requires_payment_method` and you can retry the confirmation. |

Always confirm the status of the PaymentIntent by fetching it on your server or listening for the webhooks on your server. Don’t rely solely on the user returning to the `return_url` that’s provided when you confirm the PaymentIntent.

### Refunds

You can continue to call the Refunds API with a Charge that the PaymentIntent creates. The ID of the Charge is accessible on the `latest_charge` parameter.

Alternatively, you can provide the PaymentIntent ID to the Refunds API instead of the Charge.

### Error handling

Previously, you had to handle errors on the Sources. With PaymentIntents, instead of checking for errors on a Source, you check for errors on the PaymentIntent when it’s created and after the customer has authorized the payment. Most errors on the PaymentIntent are of `invalid_request_error` type, returned in an invalid request.

When you migrate your integration, keep in mind that PaymentIntent error codes can differ from the corresponding error codes for Sources.

### Webhooks

If you previously listened to Source events, you might need to update your integration to listen to new event types. The following table shows some examples.

| Old webhook              | New webhook on Checkout                                                                                                                                                                                                                                              | New webhook on PaymentIntents   | Special instructions                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `source.chargeable`      | Not applicable                                                                                                                                                                                                                                                       | Not applicable                  |                                                                                                                         |
| `source.failed`          | Not applicable                                                                                                                                                                                                                                                       | Not applicable                  |                                                                                                                         |
| `source.canceled`        | Not applicable                                                                                                                                                                                                                                                       | Not applicable                  |                                                                                                                         |
| `charge.succeeded`       | `checkout.session.completed`                                                                                                                                                                                                                                         | `payment_intent.succeeded`      | The `charge.succeeded` webhook is also sent, so you don’t have to update your integration to listen to the new webhook. |
| `charge.failed`          | Not applicable - The customer can re-attempt the payment on the same Checkout Session until it [expires](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-expires_at), at which point you receive a `checkout.session.expired` event. | `payment_intent.payment_failed` | The `charge.failed` webhook is also sent, so you don’t have to update your integration to listen to the new webhook.    |
| `charge.dispute.created` | `charge.dispute.created`                                                                                                                                                                                                                                             | `charge.dispute.created`        |                                                                                                                         |

## Transitioning to the Payment Methods API

The main difference between the Payment Methods and Sources APIs is that Sources describes the transaction state through the [status](https://docs.stripe.com/api/sources/object.md#source_object-status) property. That means that each `Source` object must transition to a chargeable state before you can use it for a payment. By contrast, a `PaymentMethod` is stateless, relying on the _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) object to represent payment state.

> The following table isn’t a comprehensive list of payment methods. If you integrate other payment methods with the Sources API, migrate them to the Payment Methods API as well.

| Flows                | Integrate Payment Method with Payment Intents API                                                              | Tokens or Sources with Charges API                                                                 |
| -------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Cards                | [Card payments](https://docs.stripe.com/payments/cards.md)                                                     | [Supported on Tokens](https://docs.stripe.com/payments/charges-api.md); Not recommended on Sources |
| ACH Direct Debit     | [US bank account direct debits](https://docs.stripe.com/payments/ach-direct-debit.md)                          | [Supported on Tokens](https://docs.stripe.com/ach-deprecated.md) Not supported on Sources          |
| ACH Credit Transfer  | [USD Bank Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sources.md)              | [Deprecated](https://docs.stripe.com/sources/ach-credit-transfer.md)                               |
| Alipay               | [Alipay payments](https://docs.stripe.com/payments/alipay.md)                                                  | [Deprecated](https://docs.stripe.com/sources/alipay.md)                                            |
| Bancontact           | [Bancontact payments](https://docs.stripe.com/payments/bancontact.md)                                          | [Deprecated](https://docs.stripe.com/sources/bancontact.md)                                        |
| EPS                  | [EPS payments](https://docs.stripe.com/payments/eps.md)                                                        | Deprecated                                                                                         |
| giropay              | [giropay payments](https://docs.stripe.com/payments/giropay.md)                                                | [Deprecated](https://docs.stripe.com/sources/giropay.md)                                           |
| iDEAL                | [iDEAL payments](https://docs.stripe.com/payments/ideal.md)                                                    | [Deprecated](https://docs.stripe.com/sources/ideal.md)                                             |
| Klarna               | [Klarna payments](https://docs.stripe.com/payments/klarna.md)                                                  | Deprecated                                                                                         |
| Multibanco           | [Multibanco payments](https://docs.stripe.com/payments/multibanco.md)                                          | [Deprecated Beta](https://docs.stripe.com/sources/multibanco.md)                                   |
| Przelewy24           | [Przelewy24 payments](https://docs.stripe.com/payments/p24.md)                                                 | [Deprecated](https://docs.stripe.com/sources/p24.md)                                               |
| SEPA Credit Transfer | [EUR Bank Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sepa-credit-transfer.md) | [Deprecated](https://docs.stripe.com/sources/sepa-credit-transfer.md)                              |
| SEPA Direct Debit    | [Single Euro Payments Area direct debits](https://docs.stripe.com/payments/sepa-debit.md)                      | [Deprecated](https://docs.stripe.com/sources/sepa-debit.md)                                        |
| WeChat Pay           | [WeChat Pay payments](https://docs.stripe.com/payments/wechat-pay.md)                                          | [Deprecated](https://docs.stripe.com/sources/wechat-pay.md)                                        |

After you choose the API to integrate with, use the [guide to payment methods](https://stripe.com/payments/payment-methods-guide) to help you determine the right payment method types you need to support.

This guide includes detailed descriptions of each payment method and describes the differences in the customer-facing flows, along with the [geographic regions](https://stripe.com/payments/payment-methods-guide#payment-methods-fact-sheets) where they’re most relevant. You can enable any payment method available to you within the [Dashboard](https://dashboard.stripe.com/account/payments/settings). Activation is generally instantaneous and doesn’t require additional contracts.

## Compatibility with legacy reusable payment methods

If you previously processed any of the following reusable payment methods using [Sources](https://docs.stripe.com/sources.md), the existing saved sources don’t migrate automatically:

- Alipay
- Bacs Direct Debit
- SEPA Direct Debit

To preserve your existing customers’ saved payment methods, you must convert those sources to payment methods using a data migration tool in the Stripe Dashboard. For instructions on how to convert them, see [the support page](https://support.stripe.com/questions/reusable-object-migration).

## Compatibility with legacy card objects

If you previously collected card customer payment details with Stripe using [cards](https://docs.stripe.com/payments/charges-api.md) or [Sources](https://docs.stripe.com/sources.md), you can start using the Payment Methods API immediately without migrating any payment information.

Compatible payment methods that have been saved to a _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) are usable in any API that accepts a _PaymentMethod_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) object. For example, you can use a saved card as a PaymentMethod when creating a PaymentIntent:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ["card"],
  amount: 1099,
  currency: "usd",
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{CARD_ID}}",
});
```

Remember to provide the customer ID that your compatible payment method is saved to when attaching the object to a PaymentIntent.

You can [retrieve](https://docs.stripe.com/api/payment_methods/retrieve.md) all saved compatible payment methods through the Payment Methods API.

#### Card

```json
{
  "id": "card_1EBXBSDuWL9wT9brGOaALeD2",
  "object": "card",
  "address_city": "San Francisco",
  "address_country": "US",
  "address_line1": "1234 Fake Street",
  "address_line1_check": null,
  "address_line2": null,
  "address_state": null,
  "address_zip": null,
  "address_zip_check": null,
  "brand": "Visa",
  "country": "US",
  "customer": "{{CUSTOMER_ID}}",
  "cvc_check": null,
  "dynamic_last4": null,
  "exp_month": 8,
  "exp_year": 2024,
  "fingerprint": "53v265akSHAnIk1X",
  "funding": "credit",
  "last4": "4242",
  "metadata": {},
  "name": null,
  "tokenization_method": null
}
```

```json
{
  "id": "card_1EBXBSDuWL9wT9brGOaALeD2",
  "object": "payment_method",
  "billing_details": {
    "address": {
      "city": "San Francisco",
      "country": "US",
      "line1": "1234 Fake Street",
      "line2": null,
      "postal_code": null,
      "state": null
    },
    "name": null,
    "phone": null,
    "email": null
  },
  "card": {
    "brand": "visa",
    "checks": {
      "address_line1_check": null,
      "address_postal_code_check": null,
      "cvc_check": null
    },
    "country": "US",
    "exp_month": 8,
    "exp_year": 2024,
    "fingerprint": "53v265akSHAnIk1X",
    "funding": "credit",
    "last4": "4242",
    "three_d_secure_usage": {
      "supported": true
    },
    "wallet": null
  },
  "created": 123456789,
  "customer": "cus_EepWxEKrgMaywv",
  "livemode": false,
  "metadata": {},
  "type": "card"
}
```

#### Card Source

```json
{
  "id": "src_1AhIN74iJb0CbkEwmbRYPsd4",
  "object": "source",
  "amount": null,
  "client_secret": "src_client_secret_sSPHZ17iQG6j9uKFdAYqPErO",
  "created": 1500471469,
  "currency": null,
  "flow": "none",
  "livemode": false,
  "metadata": {},
  "owner": {
    "address": {
      "city": "Berlin",
      "country": "DE",
      "line1": "Nollendorfstraße 27",
      "line2": null,
      "postal_code": "10777",
      "state": null
    },
    "email": "jenny.rosen@example.com",
    "name": "Jenny Rosen",
    "phone": null,
    "verified_address": null,
    "verified_email": null,
    "verified_name": null,
    "verified_phone": null
  },
  "status": "chargeable",
  "type": "card",
  "usage": "reusable",
  "card": {
    "exp_month": 4,
    "exp_year": 2024,
    "address_line1_check": "unchecked",
    "address_zip_check": "unchecked",
    "brand": "Visa",
    "country": "US",
    "cvc_check": "unchecked",
    "funding": "credit",
    "last4": "4242",
    "three_d_secure": "optional",
    "tokenization_method": null,
    "dynamic_last4": null
  }
}
```

```json
{
  "id": "card_1EBXBSDuWL9wT9brGOaALeD2",
  "object": "payment_method",
  "billing_details": {
    "address": {
      "city": "Berlin",
      "country": "DE",
      "line1": "Nollendorfstraße 27",
      "line2": null,
      "postal_code": "10777",
      "state": null
    },
    "name": "Jenny Rosen",
    "phone": null,
    "email": "jenny.rosen@example.com"
  },
  "card": {
    "brand": "visa",
    "checks": {
      "address_line1_check": null,
      "address_postal_code_check": null,
      "cvc_check": null
    },
    "country": "US",
    "exp_month": 4,
    "exp_year": 2024,
    "fingerprint": "53v265akSHAnIk1X",
    "funding": "credit",
    "last4": "4242",
    "three_d_secure_usage": {
      "supported": true
    },
    "wallet": null
  },
  "created": 1500471469,
  "customer": "{{CUSTOMER_ID}}",
  "livemode": false,
  "metadata": {},
  "type": "card"
}
```

With this compatibility, no new objects are created; the Payment Methods API provides a different view of the same underlying object. For example, updates to a compatible payment method through the Payment Methods API is visible through the Sources API, and vice versa.

## See also

- [Guide to payment methods](https://stripe.com/payments/payment-methods-guide)
- [Connect payments](https://docs.stripe.com/connect/charges.md)
- [Payment Methods API reference](https://docs.stripe.com/api/payment_methods.md)
