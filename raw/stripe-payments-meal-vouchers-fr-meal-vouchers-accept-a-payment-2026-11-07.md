<!-- Source URL: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Accept titres-restaurant payments

Learn how to accept French meal vouchers payments on Stripe.

> #### Want to accept France titres-restaurant payments?
> 
> France titres-restaurant is in private preview. Enter your email address to [join the waitlist](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment.md#fr_meal_voucher_preview). Stripe will contact you when we can onboard additional users.

### Want to accept France titres-restaurant payments?

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment" \
  -d '{"email": "EMAIL", "preview": "fr_meal_voucher_preview"}'
```

> This guide is only for the following French meal vouchers issuers: Bimpli, Pluxee, and Up Déjeuner. It also requires preview [Stripe version](https://docs.stripe.com/sdks/set-version.md) `2026-05-27.preview` or later—see [Update the Stripe SDK](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant-api.md#update-sdk) for setup instructions.

## Before you begin

[Set up your restaurant](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant-api.md) using the Payment Locations API. Make sure the location’s `fr_meal_vouchers_conecs_payments` capability status is `active` before accepting payments.

## Review Payment Element documentation

The Payment Element allows you to collect French meal vouchers payments. For information about setting up the Payment Element, see the [quickstart](https://docs.stripe.com/payments/quickstart-payment-intents.md).

## Create a PaymentIntent

To specify that the payment is a French meal vouchers payment, pass the ID of your [payment location](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant-api.md#create-location) in [payment_details[location]](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-05-27.preview#create_payment_intent-payment_details-location) and set [payment_details[benefit][fr_meal_voucher][enabled]](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-05-27.preview#create_payment_intent-payment_details-benefit-fr_meal_voucher-enabled) to `if_payment_method_is_eligible`:

French meal vouchers payments are in EUR only.

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=1211 \
  -d currency=eur \
  -d "payment_details[location]=loc_xxx" \
  -d "payment_details[benefit][fr_meal_voucher][enabled]=if_payment_method_is_eligible"
```

After you create the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md), return its [client_secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) to the client.

## Optional: Save a French meal voucher during payment

[Save a customer’s card details for future payments using PaymentIntents](https://docs.stripe.com/payments/save-during-payment.md).

French meal vouchers require the CVC on the first payment before they can be reused for future payments without a CVC.

## Complete the payment

When your customer clicks the **Pay** button, call [confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) with the Payment Element and pass a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to indicate where Stripe redirects the user after they complete the payment.

> Stripe resolves the SIRET from the payment location at confirmation, not at PaymentIntent creation. If you update the location’s SIRET between creation and confirmation, Stripe uses the new SIRET. Changes to the location’s SIRET don’t affect already-confirmed payments.

## Optional: Check the SIRET used for payment

To find the SIRET used on the most recent charge, retrieve the PaymentIntent with the [latest_charge](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge) object [expanded](https://docs.stripe.com/api/expanding_objects.md):

```curl
curl -G https://api.stripe.com/v1/payment_intents/{{PAYMENTINTENT_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "expand[]=latest_charge"
```

In the response, the SIRET is at [benefits.fr_meal_voucher.siret](https://docs.stripe.com/api/charges/object.md?api-version=2026-05-27.preview#charge_object-payment_method_details-card-benefits-fr_meal_voucher-siret) on `latest_charge.payment_method_details.card`:

```json
{
  "id": "pi_...",
  "object": "payment_intent",
  ...
  "latest_charge": {
    "id": "ch_...",
    "object": "charge",
    ...
    "payment_method_details": {
      "card": {
        ...
        "benefits": {
          "fr_meal_voucher": {
            "siret": "83871460800067"
          }
        },
        ...
      },
      "type": "card"
    }
  }
}
```

### Test your integration 

Use the following cards to test your integration in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes):

| French meal vouchers issuer | Number | CVC | Expiration date |
| --- | --- | --- | --- |
| Bimpli with Conecs | 4000002501000002 | Any 3 digits | Any future date |

Use the PaymentLocation ID from your [sandbox onboarding setup](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant-api.md#testing). Pass this location ID in `payment_details[location]` when creating the PaymentIntent in the same sandbox.
