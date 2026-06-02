<!-- Source URL: https://docs.stripe.com/elements/currency-selector-element -->
<!-- Fetched: 2026-04-21 -->

# Currency Selector Element

Let customers pay in their local currency with Adaptive Pricing.

The Currency Selector Element is an embeddable UI component that automatically displays prices in your customer’s local currency based on their location. For details about how to enable the Currency Selector Element, see the [integration guide](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md?payment-ui=embedded-components#render-currency-selector-element).

> [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md) and the Currency Selector Element are only available when using Elements with the [Checkout Sessions API](https://docs.stripe.com/payments/quickstart-checkout-sessions.md).

If you don’t see the demo, try viewing this page in a supported browser.

> You’re responsible for complying with laws that apply to price localization in your or your customers’ regions. You must render the Currency Selector Element in your use of Adaptive Pricing with Elements. Stripe recommends you consult your legal advisor for advice specific to your business.

## Appearance

Use the [Appearance API](https://docs.stripe.com/elements/appearance-api.md) to control the style of all elements. Choose a theme or update specific details.
![Currency Selector toggle UI showing three variations of EU (€625.51) and US (665.00 USD) buttons with labeled design elements.](assets/stripe-currency-selector-element-appearance.png)

For instance, choose the “flat” theme and override the [.ToggleItem](https://docs.stripe.com/elements/appearance-api.md#toggle) styles.

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

const appearance = {
  theme: "flat",
  rules: {
    ".ToggleItem": {
      backgroundColor: "#000000",
      color: "#ffffff",
    },
  },
};
const elementsOptions = { appearance };
const checkout = stripe.initCheckoutElementsSdk({
  clientSecret,
  elementsOptions,
});
const currencySelectorElement = checkout.createCurrencySelectorElement();
currencySelectorElement.mount("#currency-selector-element");
```

## Design best practices

We offer a configurable Currency Selector Element for your checkout page. Follow these best practices when choosing where to place your selector:

- Add the Currency Selector near where payment details are entered, ideally directly above the Payment Element, since the selected currency might affect available payment methods. If you only accept cards, you can also place the Currency Selector directly below the Payment Element.
- If the Payment Element isn’t initially visible (due to multi-step flows or being lower on the page), position the Currency Selector near the total price display.
- If you’re using the [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md), we recommend placing the Currency Selector Element above the Express Checkout Element to ensure your customers know what currency they will be charged in.
- Apply these best practices to your page layouts for all screen sizes.

For more information about using the Currency Selector Element, see the [integration guide](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md?payment-ui=embedded-components#render-currency-selector-element).
