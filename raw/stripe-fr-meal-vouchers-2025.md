<!-- Source URL: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers -->
<!-- Fetched: 2026-05-05 -->

# France titres-restaurant

Learn about meal vouchers in France ("titres-restaurant"), a common benefit payment system provided by French employers as employee benefits.

> #### Want to accept France titres-restaurant payments?
>
> France titres-restaurant is in private preview.

Meal vouchers in France, or “titres-restaurant”, is a local benefits program commonly offered by employers for their employees to purchase prepared food and beverages on working days. Employers commonly provide them in the form of a prepaid card with a daily refreshed balance.

#### Payment method properties

- **Customer locations**

  France

- **Presentment currency**

  EUR

- **Payment method family**

  Cards

- **Recurring payments**

  No

- **Payout timing**

  French meal vouchers issuers control payouts

- **Connect support**

  Yes, with caveats (see details in the [Connect guide](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-with-connect.md))

- **Dispute support**

  No

- **Manual capture support**

  Yes

- **Refunds / Partial refunds**

  No / No

#### Business locations

Stripe accounts in France that have received regulatory approval can accept French meal vouchers payments.

- FR

#### Product support

- Connect1
- Elements

1 Partial support available. If you intend to accept French meal vouchers with Connect, contact Stripe at [fr-meal-voucher-beta@stripe.com](mailto:fr-meal-voucher-beta@stripe.com).

## Availability

Stripe supports online payments for the following French meal vouchers issuers:

- Bimpli (formerly Apetiz)
- Pluxee (formerly Sodexo)
- Up Déjeuner
- Swile1

Only businesses that have received approval from the [Commission Nationale des Titres-Restaurant](https://www.cntr.fr/) (CNTR), the French regulatory agency for meal vouchers, can accept French meal vouchers payments.

1 Stripe processes Swile meal vouchers over the Mastercard network without any additional action required from eligible businesses. Swile determines eligibility and generally isn’t available for businesses that accept meal vouchers through food service platforms. Contact [Swile](https://www.swile.co/fr-fr) for more information.

The behaviors and integration changes described in this document don’t apply to Swile cards.

## Requirements

You need to obtain approval from the Commission Nationale des Titres-Restaurant (CNTR) to accept French meal vouchers payments in France. You also need to have commercial acceptance agreements with at least one of the French meal vouchers issuers supported by Stripe.

Generally, only restaurants, grocers, canteens and other businesses that serve prepared food can qualify for CNTR approval. Each branch of your business must be individually approved by the CNTR to accept French meal vouchers at that branch. Check the [CNTR website](https://www.cntr.fr/) for precise requirements.

## Merchant provisioning

Before you can accept French meal vouchers on Stripe, you need to [provide the SIRET](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant.md) for your approved branch to Stripe to create and bind your merchant identifier in the French meal vouchers system. This process can take 1–3 business days.

## Settlement

French meal vouchers payments processed by Stripe are paid directly by the French meal vouchers issuer to the French meal vouchers acceptor in accordance with French law governing meal vouchers. You need to contact the issuers you’ve contracted with to set up your settlement bank account details, and any settlement-related queries.

French meal vouchers payments incur a negative value [BalanceTransaction](https://docs.stripe.com/api/balance_transactions/object.md). The negative value represents a Stripe processing fee that we deduct from your Stripe balance for processing French meal vouchers payments without the payment being settled to your Stripe merchant balance. It doesn’t include the fees payable to the French meal vouchers issuer.

## No refunds or disputes

French meal vouchers don’t support refunds after the payment is captured. You need to support [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md) if there’s a chance you can’t fulfill the purchase, such as order-and-pickup flows, or accepting orders past branch closure. Doing so allows you to release uncaptured authorizations on your customer’s French meal voucher.

French meal vouchers issued by Bimpli, Pluxee and Up Déjeuner don’t have a dispute resolution system.

## Statement descriptors

The issuer determines the statement descriptor based on the SIRET that you set on the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) or [SetupIntent](https://docs.stripe.com/api/setup_intents.md). We don’t send any statement descriptors to the network for French meal vouchers.

## Integration

If your [PaymentIntent integration](https://docs.stripe.com/payments/accept-a-payment.md) can already accept card payments, you can also accept French meal vouchers with minor integration changes.

To accept a charge as a French meal vouchers payment, you must explicitly opt in for every [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) by passing the [siret](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_details-benefit-fr_meal_voucher-siret) for the physical branch that collects the French meal vouchers payment.

> #### You must have completed provisioning for SIRETs
>
> The SIRET, which you pass into [siret](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_details-benefit-fr_meal_voucher-siret), must have already been [successfully provisioned with Stripe](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers.md#provisioning) or `PaymentIntent` creation fails.

In doing so, you accept the limitations of accepting French meal vouchers such as low credit limits and off-Stripe settlement. Stripe never retries a French meal vouchers payment as a normal card payment nor the other way around.

### Identifying French meal vouchers

To check if a saved card is eligible for French meal vouchers and to identify the issuer, look for the [benefits](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-card-benefits) hash in the [PaymentMethod](https://docs.stripe.com/api/payment_methods.md) object:

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

### Balance checks

French meal vouchers have a daily balance cap of 25 EUR set by the CNTR. The available balance refreshes every day at midnight French local time.

Query for the remaining balance using the [/v1/payment_methods/:id/check_balance](https://docs.stripe.com/api/payment_methods/check_balance.md) endpoint for saved French meal vouchers payment methods. This is optional for businesses, but you can use it as part of your checkout to inform customers of their available balance, or use it to orchestrate split tender operations.

### Split tender

French meal vouchers can only be used for food-related expenses. Ancillary fees such as delivery charges or service fees can’t be charged to a French meal voucher and must be charged to the customer on a different payment method (this is known as *split tender*). Another common use-case for split tender is if the order value is greater than the available balance on the French meal vouchers instrument.

Stripe doesn’t directly support split tender. You must orchestrate the split tender process by creating separate payments for the French meal vouchers payment, and on one or more other payment methods for the overage or ineligible amount. We recommend using the balance check function so that you can present a checkout summary of what amounts are charged to which payment methods to inform your customers.
