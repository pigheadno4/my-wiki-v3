<!-- Source URL: https://docs.stripe.com/terminal/features/collecting-tips/on-receipt -->
<!-- Fetched: 2026-04-27 -->

# Collect on-receipt tips

Learn how to allow customers to add tips to receipts.
Available in: US
Some business types allow customers to add a tip to a transaction after authorizing the card. This is most common for businesses in the dining and hospitality space (for example, a restaurant or bar), where a customer can add a tip onto the receipt.

In the US, after you confirm a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md), you can collect a tip by capturing more than the authorized amount. This is known as overcapture. After you capture the PaymentIntent, your customer sees the full captured amount reflected on their statement.

To collect a tip, [create and confirm a PaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment.md) with `capture_method` set to `manual`. To determine overcapture eligibility, expand the PaymentIntent’s `latest_charge` and inspect its [overcapture_supported](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-overcapture_supported) property.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.retrieve(
  '{{PAYMENT_INTENT}}',
  {
    expand: ['latest_charge'],
  }
);
```

Next, [capture](https://docs.stripe.com/api/payment_intents/capture.md) more than the authorized amount by providing an [amount_to_capture](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-amount_to_capture) that’s equal to the sum of the confirmed PaymentIntent and tip amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.capture(
  '{{PAYMENT_INTENT_ID}}',
  {
    amount_to_capture: 1800,
  }
);
```

Overcapturing updates the PaymentIntent [amount](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount) to reflect the new total, inclusive of the tip. This doesn’t result in an additional authorization, so your customer won’t see any immediate updates on their credit card statement. To see the original amount authorized, use the [amount_authorized](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card_present-amount_authorized) field in the PaymentIntent’s underlying [Charge](https://docs.stripe.com/api/charges.md) object.

## Limits

You can overcapture up to 50% of the PaymentIntent’s authorized `amount`, or 50 USD, whichever is greater. For example, if your PaymentIntent’s authorized `amount` is 40 USD, you can capture up to 90 USD; if your PaymentIntent’s `amount` is 100 USD, you can capture up to 150 USD.

If you need to capture more than these limits allow, there are two options:

- If your _MCC_ (A Merchant Category Code (MCC) is a four-digit number that classifies the type of goods or services a business offers) is eligible, you can use [incremental authorization](https://docs.stripe.com/terminal/features/incremental-authorizations.md) to increase the PaymentIntent’s `amount`.
- You can create a new PaymentIntent to capture the tip amount using the [generated_card](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error-payment_method-card-generated_from-payment_method_details-card_present-generated_card) payment method from the first PaymentIntent.

## Availability

On-receipt tipping is available for United States businesses with eligible merchant category codes (MCCs), for payments using Visa, Mastercard, Discover, and American Express card brands.

Businesses in the following categories are eligible to collect tips using overcapture:

- Taxicabs and limousines
- Eating places and restaurants
- Drinking places (alcoholic beverages)
- Fast food restaurants
- Beauty and barber shops
- Health and beauty spas

> #### Merchant category codes (MCCs)
>
> If you’re not sure about the eligibility of your merchant category, you can contact [support](https://support.stripe.com/contact). If you’re a _Connect_ (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) user, [set the merchant category codes](https://docs.stripe.com/connect/setting-mcc.md) for your connected accounts to match their businesses.
