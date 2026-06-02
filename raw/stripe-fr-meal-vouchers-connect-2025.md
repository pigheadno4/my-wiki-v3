<!-- Source URL: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-with-connect -->
<!-- Fetched: 2026-05-05 -->

# Accept titres-restaurant payments with Connect

Learn how to accept French meal vouchers payments with your Connect platform.

> #### Want to accept France titres-restaurant payments?
>
> France titres-restaurant is in private preview. >

French meal vouchers payments work with *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients). However, [destination charges](https://docs.stripe.com/connect/destination-charges.md) and [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) aren’t supported because funds settle outside Stripe, so there’s no balance to transfer to connected accounts. See [settlement](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers.md#settlement) for details.

## Supported charge types

French meal vouchers payments support the following charge types:

| Charge type                                                                                         | French meal vouchers payments support |                                                                                                         |
| --------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Platform charges                                                                                    | ✓ Supported                           | Recommended if you’re using destination or separate charges and transfers for your other card payments. |
| [Direct charges](https://docs.stripe.com/connect/direct-charges.md)                                 | ✓ Supported                           | Recommended if you’re using direct charges for your other card payments.                                |
| [Destination charges](https://docs.stripe.com/connect/destination-charges.md)                       | ❌ Unsupported                        | Not supported                                                                                           |
| [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md) | ❌ Unsupported                        | Not supported                                                                                           |

## Before you begin

[Provision your restaurant or store SIRET](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant.md#set-up-a-restaurant-with-connect) for French meal vouchers acceptance with Stripe. You must provision the SIRET on the [merchant of record](https://docs.stripe.com/connect/merchant-of-record.md).

## Integration

#### Your integration path - Integrate direct charges

Follow the [accept titres-restaurant payments guide](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment.md) and use the Stripe-Account header in your API request.

Learn more about [making API calls for connected accounts](https://docs.stripe.com/connect/authentication.md).

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Account: {{CONNECTEDACCOUNT_ID}}" \
  -d amount=1211 \
  -d currency=eur \
  -d "payment_details[benefit][fr_meal_voucher][siret]=42424242424242"
```

#### Your integration path - Integrate platform charges

With this integration:

- If the customer pays with a French meal voucher, create a `PaymentIntent` on your platform’s account without setting `transfer_data`, `application_fee_amount` or `transfer_group` parameters. Pass the SIRET of the restaurant for which the payment is created for.
- Collect fees from the connected account by [debiting its Stripe balance](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-with-connect.md#collect-fees).
- Your account balance is debited for the cost of the Stripe fees.

## Check if the payment method is a French meal voucher

#### Set up a payment method

We recommend creating a *SetupIntent* (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method) to save a payment method for future payments without charging your customer. Follow [this guide](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/saving-payment-details.md) to save the payment method, and look for the [benefits](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-card-benefits) hash in the [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) object to determine whether the payment method is a French meal voucher:

```json
{
  "id": "pm_1Q0PsIJvEtkwdCNYMSaVuRz6",
  "object": "payment_method",
  "card": {"benefits": {
      "issuer": "pluxee",
      "programs": "fr_meal_voucher"
    },
    ...
  },
  ...
}
```

#### Accept a payment

Follow [this guide](https://docs.stripe.com/payments/finalize-payments-on-the-server.md) to render the Payment Element, then insert custom business logic before creating the `PaymentIntent` to inspect the *confirmation token* (ConfirmationTokens help capture data from your client, such as your customer's payment instruments and shipping address, and are used to confirm a PaymentIntent or SetupIntent). To determine whether the payment method is a French meal voucher, check the [benefits](https://docs.stripe.com/api/confirmation_tokens/object.md#confirmation_token_object-payment_method_preview-card-benefits) hash in the [ConfirmationToken](https://docs.stripe.com/api/confirmation_tokens.md) object:

```json
{
  "id": "ctoken_1NnQUf2eZvKYlo2CIObdtbnb",
  "object": "confirmation_token",
  "payment_method_preview": {
    "card": {"benefits": {
        "issuer": "pluxee",
        "programs": "fr_meal_voucher"
      },
      ...
    },
  },
  ...
}
```

## Create a PaymentIntent

If the payment method is a French meal voucher, create a PaymentIntent on your platform account. Omit the `transfer_data`, `application_fee_amount` and `transfer_group` parameters.

#### Destination charges

### Before

Pass the connected account ID using `transfer_data[destination]`.

```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'eur',
  on_behalf_of: {{CONNECTED_ACCOUNT_ID}},
})
```

### After

Omit `transfer_data` and `application_fee_amount` and add the `payment_details[benefit][fr_meal_voucher]`.

```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'eur',
  on_behalf_of: {{CONNECTED_ACCOUNT_ID}},payment_details: {
    benefit: {
      fr_meal_voucher: {
        siret: '42424242424242'
      }
    }
  }
}
```

#### Separate charges and transfers

### Before

Create charges on the platform, then transfer funds to the connected account.

```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'eur',
  on_behalf_of: {{CONNECTED_ACCOUNT_ID}},
})

```

### After

Omit `transfer_group` and don’t make the transfer to the connected account. Add the `payment_details[benefit][fr_meal_voucher]`.

```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'eur',
  on_behalf_of: {{CONNECTED_ACCOUNT_ID}},payment_details: {
    benefit: {
      fr_meal_voucher: {
        siret: '42424242424242'
      }
    }
  }
}
```

## Collect fees

Collect fees from the connected account by debiting its Stripe balance. See the [debit connected accounts](https://docs.stripe.com/connect/account-debits.md) guide for more information.

> #### Requirements
>
> Learn about the [requirements](https://docs.stripe.com/connect/account-debits.md#requirements) for debiting connected accounts.

### Transfer from the connected account

After you capture the PaymentIntent, create a transfer from the connected account to your platform account to collect an application fee. This transfer object lives on the connected account. Use the `Stripe-Account` header to authenticate as the connected account and provide your platform’s Stripe account ID as the destination:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const transfer = await stripe.transfers.create(
  {
    amount: 30,
    currency: "eur",
    destination: "{{ACCOUNT_ID}}",
  },
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

We recommend using the [metadata](https://docs.stripe.com/api/transfers/create.md#create_transfer-metadata) field to link the transfer to the original PaymentIntent.

### Refund application fees

French meal vouchers [don’t support refunds](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers.md#no-refunds-disputes). To refund the application fee to the connected account, create a transfer reversal on the connected account:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const transferReversal = await stripe.transfers.createReversal(
  "{{TRANSFER_ID}}",
  {
    stripeAccount: "{{CONNECTEDACCOUNT_ID}}",
  },
);
```

### Flow of funds

(See full diagram at https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-with-connect)

1. The customer pays a 10.00 EUR charge. The charge lives on the platform. The platform’s balance doesn’t increase.
1. Stripe collects payment processing fees from the platform.
1. The platform application fee is transferred from the connected account to the platform through `v1/transfers`.
1. Outside of Stripe, French meal vouchers issuers settle directly with the connected account.
