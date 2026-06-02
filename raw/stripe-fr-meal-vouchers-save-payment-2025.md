<!-- Source URL: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/saving-payment-details -->
<!-- Fetched: 2026-05-05 -->

# Save a customer's payment method without making a payment

Learn how to save a customer's French meal vouchers payment method using a SetupIntent.

> #### Want to accept France titres-restaurant payments?
>
> France titres-restaurant is in private preview. >

> This guide is only for the following French meal vouchers issuers:
>
> - Bimpli

- Pluxee
- Up Déjeuner

Before you begin, make sure that you [provisioned your restaurant or store SIRET](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant.md) for French meal vouchers acceptance with Stripe.

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/saving-payment-details?payment-ui=elements.

## Review the Saved Payment Methods documentation

Make sure to first review how to [save a customer’s payment method](https://docs.stripe.com/payments/save-and-reuse.md) without making a payment.

## Create a SetupIntent

To specify that the payment method is set up as a French meal vouchers payment, you must pass the SIRET of your business branch in the [siret](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-setup_details-benefit-fr_meal_voucher-siret) field, as shown in the following example:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  customer: "{{CUSTOMER_ID}}",
  setup_details: {
    benefit: {
      fr_meal_voucher: {
        siret: "42424242424242",
      },
    },
  },
});
```

After you create the `SetupIntent`, return its [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) to the client.

## Submit the payment details to Stripe

Use [stripe.confirmSetup](https://docs.stripe.com/js/setup_intents/confirm_setup) to complete the setup using details collected by the Payment Element. Provide a [return_url](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-return_url) to indicate where Stripe redirects the user after they complete setup.

## Charge the saved payment method later

When you charge the saved payment method *on-session* (A payment is described as on-session if it occurs while the customer is actively in your checkout flow and able to authenticate the payment method), use the `Customer` and `PaymentMethod` IDs to create a `PaymentIntent`.

Pass the SIRET of your business branch in the [siret](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_details-benefit-fr_meal_voucher-siret) field, as shown in the following example:

French meal vouchers payments are in EUR only.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1211 \
  -d currency=eur \
  -d "customer={{CUSTOMER_ID}}" \
  -d "payment_method={{PAYMENTMETHOD_ID}}" \
  -d confirm=true \
  -d "payment_details[benefit][fr_meal_voucher][siret]=42424242424242"
```

## Test your integration

You can use the following cards to test your integration:

| French meal vouchers issuer | Number           | CVC          | Expiry date     |
| --------------------------- | ---------------- | ------------ | --------------- |
| Bimpli with Conecs          | 4000002501000002 | Any 3 digits | Any future date |

You can test different scenarios with the SIRET passed into `setup_details[benefit][fr_meal_voucher][siret]`.

| SIRET            | Scenario                                                                     |
| ---------------- | ---------------------------------------------------------------------------- |
| `42424242424242` | A SIRET that you provisioned for French meal vouchers acceptance with Stripe |
| `00000000000000` | Invalid SIRET                                                                |

## Temporary card authorization charge

When storing customer details, Stripe might send a request to the issuer to verify the card. A customer might see a 0.30 EUR charge on their bank statement resulting from this card authorization process. Stripe reverses this temporary charge almost immediately, restoring the charge to the customer’s daily balance.
