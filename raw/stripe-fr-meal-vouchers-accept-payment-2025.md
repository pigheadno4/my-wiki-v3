<!-- Source URL: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment -->
<!-- Fetched: 2026-05-05 -->

# Accept titres-restaurant payments

Learn how to accept French meal vouchers payments on Stripe.

> #### Want to accept France titres-restaurant payments?
>
> France titres-restaurant is in private preview. >

> This guide is only for the following French meal vouchers issuers:
>
> - Bimpli

- Pluxee
- Up Déjeuner

## Before you begin

[Provision your restaurant or store SIRET](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant.md) for French meal vouchers acceptance with Stripe.

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment?payment-ui=elements.

## Review Payment Element documentation

The Payment Element allows you to collect French meal vouchers payments. For information about setting up the Payment Element, see the [quickstart](https://docs.stripe.com/payments/quickstart.md?platform=web).

## Create a PaymentIntent

To specify that the payment is a French meal vouchers payment, pass the SIRET of your business branch in the [siret](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_details-benefit-fr_meal_voucher-siret) field, as shown in the following example:

French meal vouchers payments are in EUR only.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1211 \
  -d currency=eur \
  -d "payment_details[benefit][fr_meal_voucher][siret]=42424242424242"
```

After you create the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md), return its [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) to the client.

## Optional: Save a French meal voucher during payment

[Save a customer’s card details for future payments using PaymentIntents](https://docs.stripe.com/payments/save-during-payment.md).

French meal vouchers require the CVC on the first payment before they can be reused for future payments without a CVC.

## Complete the payment

When your customer clicks the pay button, call [confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) with the Payment Element and pass a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to indicate where Stripe redirects the user after they complete the payment.

## Test your integration

You can use the following cards to test your integration:

| French meal vouchers issuer | Number           | CVC          | Expiry date     |
| --------------------------- | ---------------- | ------------ | --------------- |
| Bimpli with Conecs          | 4000002501000002 | Any 3 digits | Any future date |

You can test different scenarios with the SIRET passed into `payment_details[benefit][fr_meal_voucher][siret]`.

| SIRET            | Scenario                                                                     |
| ---------------- | ---------------------------------------------------------------------------- |
| `42424242424242` | A SIRET that you provisioned for French meal vouchers acceptance with Stripe |
| `00000000000000` | Invalid SIRET                                                                |
