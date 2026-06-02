<!-- Source: Stripe Checkout — Collect customer phone numbers -->
<!-- Fetched: 2026-04-20 -->

# Collect customer phone numbers

Collect a phone number for shipping or invoicing when your customer makes a payment.

# Hosted page

> This is a Hosted page for when payment-ui is stripe-hosted. View the full page at https://docs.stripe.com/payments/checkout/phone-numbers?payment-ui=stripe-hosted.

You can enable phone number collection on all `payment` and `subscription` [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) Sessions (phone number collection isn’t supported in `setup` mode). Only collect phone numbers if you need them for the transaction.

## Enable phone number collection

To enable phone number collection, set [phone_number_collection[enabled]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-phone_number_collection-enabled) to `true` when creating a Checkout Session.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        unit_amount: 1000,
        product_data: {
          name: "T-shirt",
        },
        currency: "eur",
      },
      quantity: 2,
    },
  ],
  phone_number_collection: {
    enabled: true,
  },
  mode: "payment",
  success_url: "https://example.com/success",
});
```

With phone number collection enabled, Checkout adds a _required_ phone number field to the payment form. If you’re collecting a shipping address, the phone number field displays under the address fields. Otherwise, Checkout displays the phone number field below the email input. Customers can only enter one phone number per session.

## Retrieve the phone number

When your customer checks out with third-party wallets, such as [Apple Pay](https://docs.stripe.com/apple-pay.md) or [Google Pay](https://docs.stripe.com/google-pay.md), the phone number format isn’t guaranteed because of limitations on those platforms. We return the phone number value that’s provided by the third-party wallet.

We guarantee phone numbers in the [E.164](https://en.wikipedia.org/wiki/E.164) format when a customer doesn’t use [wallet payments](https://docs.stripe.com/payments/wallets.md).

After the session, you can retrieve customer phone numbers from the resulting `Account`, `Customer`, or _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) objects:

- [On the customer-configured Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer): Checkout saves collected phone numbers on the [contact_phone](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-contact_phone) property of the `Account`. You can [retrieve](https://docs.stripe.com/api/v2/core/accounts/retrieve.md) the value using the API or listen for the [v2.core.account.created](https://docs.stripe.com/api/v2/core/events/event-types.md#v2_event_types-v2.core.account.created) event in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). You can also view the customer’s phone number in the [Dashboard](https://dashboard.stripe.com/customers).
- [On the Customer](https://docs.stripe.com/api/customers.md): Checkout saves collected phone numbers onto the [phone](https://docs.stripe.com/api/customers/object.md#customer_object-phone) property of the `Customer`. You can [retrieve](https://docs.stripe.com/api/customers/retrieve.md) the value using the API or listen for the [customer.created](https://docs.stripe.com/api/events/types.md#event_types-customer.created) event in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). You can also view the customer’s phone number in the [Dashboard](https://dashboard.stripe.com/customers).
- [On the Checkout Session](https://docs.stripe.com/api/checkout/sessions.md): The Checkout Session also saves the customer’s phone number in the [customer_details.phone](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-customer_details-phone) property. You can listen for the [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) event in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), which contains the Checkout Session object (and phone number).

## Collect phone numbers for existing customers

Passing in an existing customer with a populated phone number to the [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) prefills the phone number field. Use the [contact_phone](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-contact_phone) property for a customer-configured `Account` or the [phone](https://docs.stripe.com/api/customers/object.md#customer_object-phone) property for a `Customer`.

A customer-updated phone number persists on the `contact_phone` property for `Account` objects or the `phone` property for `Customer` objects, overwriting any previously saved phone number.

### Update phone numbers with the customer portal

You can allow customers to manage their own accounts (which includes [updating their phone numbers](https://docs.stripe.com/api/customer_portal/configurations/create.md#create_portal_configuration-features-customer_update-allowed_updates)) in the customer portal.

## See also

- [Integrate the customer portal](https://docs.stripe.com/customer-management.md)

# Embedded Page

> This is a Embedded Page for when payment-ui is embedded-form. View the full page at https://docs.stripe.com/payments/checkout/phone-numbers?payment-ui=embedded-form.

You can enable phone number collection on all `payment` and `subscription` [mode](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-mode) Sessions (phone number collection isn’t supported in `setup` mode). Only collect phone numbers if you need them for the transaction.

## Enable phone number collection

To enable phone number collection, set [phone_number_collection[enabled]](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-phone_number_collection-enabled) to `true` when creating a Checkout Session.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const session = await stripe.checkout.sessions.create({
  line_items: [
    {
      price_data: {
        unit_amount: 1000,
        product_data: {
          name: "T-shirt",
        },
        currency: "eur",
      },
      quantity: 2,
    },
  ],
  phone_number_collection: {
    enabled: true,
  },
  mode: "payment",
  ui_mode: "embedded_page",
  return_url: "https://example.com/return",
});
```

With phone number collection enabled, Checkout adds a _required_ phone number field to the payment form. If you’re collecting a shipping address, the phone number field displays under the address fields. Otherwise, Checkout displays the phone number field below the email input. Customers can only enter one phone number per session.

## Retrieve the phone number

When your customer checks out with third-party wallets, such as [Apple Pay](https://docs.stripe.com/apple-pay.md) or [Google Pay](https://docs.stripe.com/google-pay.md), the phone number format isn’t guaranteed because of limitations on those platforms. We return the phone number value that’s provided by the third-party wallet.

We guarantee phone numbers in the [E.164](https://en.wikipedia.org/wiki/E.164) format when a customer doesn’t use [wallet payments](https://docs.stripe.com/payments/wallets.md).

After the session, you can retrieve customer phone numbers from the resulting `Account`, `Customer`, or _Checkout Session_ (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription) objects:

- [On the customer-configured Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer): Checkout saves collected phone numbers on the [contact_phone](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-contact_phone) property of the `Account`. You can [retrieve](https://docs.stripe.com/api/v2/core/accounts/retrieve.md) the value using the API or listen for the [v2.core.account.created](https://docs.stripe.com/api/v2/core/events/event-types.md#v2_event_types-v2.core.account.created) event in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). You can also view the customer’s phone number in the [Dashboard](https://dashboard.stripe.com/customers).
- [On the Customer](https://docs.stripe.com/api/customers.md): Checkout saves collected phone numbers onto the [phone](https://docs.stripe.com/api/customers/object.md#customer_object-phone) property of the `Customer`. You can [retrieve](https://docs.stripe.com/api/customers/retrieve.md) the value using the API or listen for the [customer.created](https://docs.stripe.com/api/events/types.md#event_types-customer.created) event in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). You can also view the customer’s phone number in the [Dashboard](https://dashboard.stripe.com/customers).
- [On the Checkout Session](https://docs.stripe.com/api/checkout/sessions.md): The Checkout Session also saves the customer’s phone number in the [customer_details.phone](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-customer_details-phone) property. You can listen for the [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) event in a _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), which contains the Checkout Session object (and phone number).

## Collect phone numbers for existing customers

Passing in an existing customer with a populated phone number to the [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) prefills the phone number field. Use the [contact_phone](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-contact_phone) property for a customer-configured `Account` or the [phone](https://docs.stripe.com/api/customers/object.md#customer_object-phone) property for a `Customer`.

A customer-updated phone number persists on the `contact_phone` property for `Account` objects or the `phone` property for `Customer` objects, overwriting any previously saved phone number.

### Update phone numbers with the customer portal

You can allow customers to manage their own accounts (which includes [updating their phone numbers](https://docs.stripe.com/api/customer_portal/configurations/create.md#create_portal_configuration-features-customer_update-allowed_updates)) in the customer portal.

## See also

- [Integrate the customer portal](https://docs.stripe.com/customer-management.md)
