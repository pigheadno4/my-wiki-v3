<!-- Source: Stripe — Stripe Payment Element -->
<!-- Fetched: 2026-04-21 -->
<!-- URL: https://docs.stripe.com/payments/payment-element -->

# Stripe Payment Element

Accept payment methods from around the globe with a secure, embeddable UI component.

The Payment Element is a UI component for the web that lets you accept more than 100 payment methods, validates input, and handles errors. Use it alone or with other elements in your web app's front end.

## Compatible APIs

Stripe offers two core payments APIs compatible with Elements. We recommend the Checkout Sessions API for most integrations.

**Checkout Sessions API (Recommended)**: Build your checkout flow. Covers similar use cases as Payment Intents, including basic payments using `price_data` or full checkout with line items, tax, discounts, shipping, subscriptions, or Adaptive Pricing (only available with Checkout Sessions).

**Payment Intents API**: A lower-level API that models only the payment step. You pass in a final amount and build all checkout logic yourself. Use Payment Intents only if you want to deeply own your checkout state and build these features yourself.

## Quickstart integrations

- Build an advanced integration with Payment Element and Checkout Sessions
- Build an integration with Payment Element and Payment Intents
- Clone a sample app on GitHub: HTML · React · Vue
- View the Stripe.js reference

## Combine elements

The Payment Element interoperates with other elements. For instance, a form can use:
- **Link Authentication Element** — for contact info with Link autofill
- **Address Element** — to collect shipping address
- **Payment Element** — for payment fields

![Form combining Link Authentication, Address, and Payment Elements](assets/stripe-payment-element-link-with-elements.png)

> You can't remove the Link legal agreement because it's required to ensure compliance with proper user awareness of terms of services and privacy policies. The `terms` object doesn't apply to the Link legal agreement.

For the complete code for this example, see Add Link to an Elements integration.

You can also combine the Payment Element with the Express Checkout Element. In this case, wallet payment methods such as Apple Pay and Google Pay are only displayed in the Express Checkout Element to avoid duplication.

## Payment methods

Stripe enables certain payment methods for you by default and might enable additional payment methods after notifying you. Use the Dashboard to enable or disable payment methods at any time.

With the Payment Element, you can use **Dynamic payment methods** to:
- Manage payment methods in the Dashboard without coding
- Dynamically display the most relevant payment options based on factors such as location, currency, and transaction amount

For example, if a customer in Germany is paying in EUR, they see all active payment methods that accept EUR, starting with ones widely used in Germany.

![Payment methods shown in order of relevance to the customer](assets/stripe-payment-element-methods.png)

To further customize how payment methods render, see Customize payment methods. To add payment methods integrated outside of Stripe, use custom payment methods.

## Layout

You can customize the Payment Element's layout to fit your checkout flow.

![Payment Element with three layout options: tabs, accordion with radio buttons, accordion without radio buttons](assets/stripe-payment-element-layout.png)

Three layout options:
- **Tabs**: payment methods displayed horizontally as tabs
- **Accordion with radio buttons**: payment methods listed vertically with radio buttons
- **Accordion without radio buttons**: payment methods listed vertically without radio buttons

```javascript
const options = {
  layout: {
    type: 'tabs',          // 'tabs' | 'accordion'
    defaultCollapsed: false,
  }
};
```

## Appearance API

Use the Appearance API to control the style of all elements. Choose a theme or update specific details.

![Light and dark mode examples of the payment element](assets/stripe-payment-element-appearance.png)

```javascript
const appearance = {
  theme: 'flat',
  variables: { colorPrimaryText: '#262626' }
};
```

Available themes: `stripe`, `night`, `flat`, `none`. See Appearance API documentation for a full list of themes and variables.

## Options

```javascript
const options = {
  business: { name: "RocketRides" }
};
```

| Option | Description |
| --- | --- |
| `layout` | Layout for the Payment Element (tabs or accordion) |
| `defaultValues` | Initial customer information to prefill |
| `business` | Business information to display (e.g., name) |
| `paymentMethodOrder` | Order to list payment methods |
| `fields` | Whether to display certain fields |
| `readOnly` | Whether payment details can be changed |
| `terms` | Whether mandates/legal agreements are displayed (default: only when necessary) |
| `wallets` | Whether to show wallets like Apple Pay or Google Pay (default: show when possible) |

## Errors

Payment Element automatically shows localized customer-facing error messages during client confirmation for the following decline codes:

`card_declined`, `card_velocity_exceeded`, `expired_card`, `fraudulent`, `generic_decline`, `incorrect_cvc`, `incorrect_number`, `incorrect_zip`, `insufficient_funds`, `invalid_cvc`, `invalid_expiry_month`, `invalid_expiry_year`, `live_mode_test_card`, `lost_card`, `processing_error`, `stolen_card`, `test_mode_live_card`

To display messages for other types of errors, refer to error codes and error handling.
