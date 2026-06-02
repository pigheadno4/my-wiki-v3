<!-- Source URL: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/checking-a-card-balance -->
<!-- Fetched: 2026-05-05 -->

# Check French meal vouchers balances

Learn how to check the available balance on a French meal voucher.

> #### Want to accept France titres-restaurant payments?
>
> France titres-restaurant is in private preview. >

> This guide is only for the following French meal vouchers issuers:
>
> - Bimpli

- Pluxee
- Up Déjeuner

Meal vouchers in France typically have daily allowances that might not cover an entire purchase, and restrictions on eligible purchases. For example, customers can’t use a French meal voucher for non-food fees, such as service fees or delivery charges.

If you charge an amount that exceeds the available balance on the card, you’ll receive a card decline. To prevent this, perform balance checks for French meal vouchers payments. Balance checks don’t hold any amount on the French meal vouchers. Authorizations can still decline if the available amount is used by a concurrent purchase.

To check the available balance before payment, use the Payment Method Balance Check API. This allows you to:

- Display balance information to your customers during checkout
- Calculate how much to charge the French meal voucher versus a secondary payment method for [split tender](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers.md#split-tender)
- Verify that the French meal voucher has sufficient funds before creating a `PaymentIntent`

## Before you begin

[Provision your restaurant or store SIRET](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant.md) for French meal vouchers acceptance with Stripe.

## Save a French meal voucher

To check the available balance on a French meal voucher, you must first [save it as a payment method](https://docs.stripe.com/payments/save-and-reuse.md). You can also check the balance of cards that you [saved during payment](https://docs.stripe.com/payments/save-during-payment.md).

## Check the balance

Use the [Check Balance API](https://docs.stripe.com/api/payment_methods/check_balance.md) to verify the available amount on a French meal voucher.

```curl
curl -X POST https://api.stripe.com/v1/payment_methods/{{PAYMENTMETHOD_ID}}/check_balance \
  -u "<<YOUR_SECRET_KEY>>:"
```

## Handle the response

The response contains the balance information, available by benefit type and as a list of available amounts by currency. You can use this information to display the balance to your customer and calculate the amount of any extra payments to charge another payment method. The `as_of` field indicates when the balance on the card was retrieved, but the balance can change at any point after this timestamp.

```json
{
  "object": "payment_method_balance",
  "as_of": 1750768577,
  "balance": {
    "fr_meal_voucher": {
      "available": [
        {
          "amount": 2500,
          "currency": "eur"
        }
      ]
    }
  },
  "livemode": true
}
```

## Test your integration

To test your integration, you can use the payment method `pm_card_conecs_fr_frMealVoucher`. This card always returns a balance of 10.00 EUR in a sandbox.

```curl
curl -X POST https://api.stripe.com/v1/payment_methods/pm_card_conecs_fr_frMealVoucher/check_balance \
  -u "<<YOUR_SECRET_KEY>>:"
```

## Split tender considerations

You can use the following approach to split a payment between the French meal voucher and a secondary payment method:

1. Check the balance on the French meal voucher.
1. If the balance is insufficient, create two `PaymentIntent` objects: one for the French meal voucher and one for the secondary payment method.
1. Because you can’t refund French meal vouchers, always process the secondary payment method first. Alternatively, use manual capture for French meal vouchers after confirming the secondary payment succeeded.
1. If any of the payments fail, revert the other payment.
   (See full diagram at https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/checking-a-card-balance)

## See also

- [Accept titres-restaurant payments](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment.md)
