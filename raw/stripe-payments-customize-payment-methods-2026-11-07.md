<!-- Source URL: https://docs.stripe.com/payments/customize-payment-methods -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Customize payment methods

Choose how the Payment Element displays payment methods.

The Payment Element supports many payment methods. It displays the payment methods you enabled, hides any that won’t work for the current transaction, and sorts them dynamically for the best conversion rates.

You can customize its behavior in these ways:

- [Enable different payment methods](https://docs.stripe.com/payments/customize-payment-methods.md#enable-different-payment-methods).
- [Sort payment methods](https://docs.stripe.com/payments/customize-payment-methods.md#sort-payment-methods) differently than the default.
- [Filter card brands and funding types](https://docs.stripe.com/payments/customize-payment-methods.md#filter-card-brands-and-funding-types) that you don’t want to support.
- [Limit the number of payment methods](https://docs.stripe.com/payments/customize-payment-methods.md#limit-payment-method-count) displayed.

## Enable different payment methods 

You can specify [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to enable different payment methods by selecting them in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe enables this functionality by default in the latest version of the API.

This allows Stripe to pull your payment method preferences from the Dashboard and dynamically show the most relevant payment methods to your customers. Alternatively, you can specify the allowed payment method types manually using [allowed_payment_method_types](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-allowed_payment_method_types).

There’s one situation where the Payment Element overrides your choice. It hides payment methods that don’t support the current payment. For instance, in a recurring payment for 10 JPY, the Payment Element hides methods that don’t support JPY or recurring payments.

## Sort payment methods 

By default, the Payment Element uses dynamic ordering to optimize which payment methods appear for each user. With the [paymentMethodOrder](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-paymentMethodOrder) parameter, you can override the default order for payment methods in the Payment Element, including Apple Pay and Google Pay.

Payment methods that you specify in `paymentMethodOrder` are shown first, followed by any additional payment methods. If you specify payment method types that Stripe wouldn’t show, they’re ignored.

```javascript
elements.create('payment', {
  paymentMethodOrder: ['apple_pay', 'google_pay', 'card', 'klarna']
});
```

You can include Apple Pay (`apple_pay`) and Google Pay (`google_pay`) when setting the order for payment methods in addition to a full list of [payment method types](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-type). When you specify sorting, Stripe applies dynamic ordering to any remaining available payment methods.

> Regulations in [Finland](https://support.stripe.com/questions/payment-method-legislation-in-finland) and [Sweden](https://support.stripe.com/questions/payment-method-legislation-in-sweden) require that debit payment methods must be presented before credit payment methods at checkout in those countries.

## Filter card brands and funding types 

When your customers pay with a card through the Payment Element, you can block specific card brands and funding types. This applies to the card input field, Apple Pay, and Google Pay.

When you initialize the Elements group, you can use [disallowedCardBrands](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-disallowedCardBrands) and [disallowedCardFundingTypes](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-disallowedCardFundingTypes) to block card brands and funding types in the Payment Element.

Pass an array to `disallowedCardBrands` with any of the following values:

- `visa`
- `mastercard`
- `american_express`
- `discover_global_network`

The `discover_global_network` value includes Discover, Diners, JCB, UnionPay, and Elo.

Pass an array to `disallowedCardFundingTypes` with any of the following values:

- `credit`
- `debit`
- `prepaid`

You can’t block every supported card brand or every supported card funding type.

The following example blocks American Express and prepaid cards:

#### HTML + JS

```javascript
const elements = stripe.elements({
  disallowedCardBrands: ['american_express'],
  disallowedCardFundingTypes: ['prepaid'],
});
```

#### React

```jsx
function App() {
  const options = {
    disallowedCardBrands: ['american_express'],
    disallowedCardFundingTypes: ['prepaid'],
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutPage />
    </Elements>
  );
}
```

### Enforce card restrictions

The Payment Element validates blocked cards in the browser and shows an error while the customer enters the card. This client-side validation doesn’t enforce your payment policy on the server. If you need server-side enforcement, use one of the following options:

- **Radar rules:** [Screen and block payments](https://docs.stripe.com/radar/rules.md) based on card attributes, including card brand and funding type.
- **Server-side confirmation:** [Finalize payments on your server](https://docs.stripe.com/payments/finalize-payments-on-the-server.md?platform=web&type=payment) with a [ConfirmationToken](https://docs.stripe.com/api/confirmation_tokens.md). Create the ConfirmationToken from the Payment Element in Stripe.js, send its ID to your server, retrieve the token, inspect `payment_method_preview.card.brand` and `payment_method_preview.card.funding`, and confirm the PaymentIntent only when your policy permits it.

Funding can be `unknown` or unavailable. If your policy requires strict enforcement, decide whether to reject an indeterminate value.

> Apple Pay doesn’t support filtering prepaid cards, and Google Pay doesn’t support filtering debit cards. For Elements with Checkout Sessions, Checkout still enforces blocked funding types when confirming a payment.

## Limit the number of payment methods 

When you use the [accordion layout](https://docs.stripe.com/payments/payment-element.md#layout), the Payment Element displays up to five payment methods by default and hides the rest behind a **More** button.

To adjust the number of payment methods you want to display, set the [layout.visibleAccordionItemsCount](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout-visibleAccordionItemsCount) property.

```javascript
elements.create('payment', {
  layout: {
    type: 'accordion',
    // Set a different default, or set to 0 to disable the
    // "More" button and render all available Payment Methods
    visibleAccordionItemsCount: 3
  }
});
```
