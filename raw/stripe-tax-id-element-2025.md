<!-- Source URL: https://docs.stripe.com/elements/tax-id-element -->
<!-- Fetched: 2026-04-21 -->

# Tax ID Element

Collect business tax IDs for invoices and VAT refunds.

The Tax ID Element is an embeddable UI component that collects customer tax ID information. You can use the Tax ID Element with either the Elements with [Checkout Sessions API](https://docs.stripe.com/payments/quickstart-checkout-sessions.md) or the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) integrations.

For details about how to integrate the Tax ID Element, see the integration guide for your chosen approach:

- [Checkout Sessions API integration guide](https://docs.stripe.com/payments/advanced/tax.md?api-integration=checkout#render-tax-id-element)
- [Payment Intents API integration guide](https://docs.stripe.com/payments/advanced/tax.md?api-integration=elements#collect-customer-tax-ids)

If you don’t see the demo, try viewing this page in a supported browser.

| Option                      | Description                                                                                                                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Theme**                   | Use the dropdown to choose a theme or customize the theme with the [Elements Appearance API](https://docs.stripe.com/elements/appearance-api.md).                                             |
| **Desktop and mobile size** | Use the dropdown to set the max pixel width of the parent element that the Tax ID Element is mounted to. You can set it to 750px (desktop) or 320px (mobile).                                 |
| **Customer location**       | Use the dropdown to choose a location for collecting tax ID information. Changing the location updates the tax ID type and format requirements, and controls element visibility in auto mode. |
| **Visibility**              | Use the dropdown to choose a visibility mode. In auto mode, the Tax ID Element only displays for countries that support tax ID collection.                                                    |
| **Business name**           | Enable this option to collect the business name. The collected business name appears as the customer name on invoices.                                                                        |

## Supported regions

The Tax ID Element supports tax ID collection in the following countries and regions. When using auto mode, the element automatically displays only for customers in these supported locations. Each region has specific tax ID types and format requirements.

### North America

- AW
- BB
- BS
- CA
- CR
- MX

### South America

- CL
- EC
- PE
- SR
- UY

### Europe

- AL
- AM
- AT
- AZ
- BA
- BE
- BG
- BY
- CH
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GB
- GE
- GR
- HR
- HU
- IE
- IS
- IT
- LI
- LT
- LU
- LV
- MD
- ME
- MK
- MT
- NL
- NO
- PL
- PT
- RO
- RS
- RU
- SE
- SI
- SK
- UA

### Asia

- AE
- BD
- BH
- IN
- KG
- KH
- KR
- KZ
- LA
- NP
- OM
- PH
- SA
- SG
- TH
- TJ
- TR
- TW
- UZ

### Oceania

- AU
- NZ

### Africa

- AO
- BF
- BJ
- CD
- CM
- CV
- EG
- ET
- GN
- KE
- MA
- MR
- NG
- SN
- TZ
- UG
- ZA
- ZM
- ZW

When you use the Tax ID Element and the [Address Element](https://docs.stripe.com/elements/address-element.md) together, Stripe automatically determines the tax ID type and element visibility based on the customer’s address. This ensures the correct tax ID format is displayed for the customer’s location.

## Visibility of the Tax ID Element

You can collect Tax IDs for a number of reasons but the most common reasons are to help calculate sales tax or to display on invoices.

The Tax ID Element adapts to the location of a customer by default, and it only shows if tax ID collection is common in their country. To determine if the tax ID is relevant, the Tax ID Element checks the customer’s IP address and country from the [Address Element](https://docs.stripe.com/elements/address-element.md) (in either shipping or billing mode). If the Address Element isn’t present, we use the customer’s IP address. If you want to make sure that you always show the Tax ID Element (even for countries that don’t typically collect tax IDs), you can set the visibility to `always`.

## Create a Tax ID Element

# Checkout Sessions API

> This is a Checkout Sessions API for when payment-ui is embedded-components. View the full page at https://docs.stripe.com/elements/tax-id-element?payment-ui=embedded-components.

Here’s how you can use the [Tax ID Element](https://docs.stripe.com/js/custom_checkout/create_tax_id_element) with the Checkout Sessions API to collect tax IDs:

```html
<div class="tax-id-form">
  <div id="tax-id-element"></div>
</div>
```

```javascript
const stripe = window.Stripe("<<YOUR_PUBLISHABLE_KEY>>", {
  betas: ["custom_checkout_tax_id_1"],
});
const appearance = {
  /* appearance */
};
const elementsOptions = { appearance };

const clientSecret = fetch("/create-checkout-session", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
})
  .then((res) => res.json())
  .then((res) => {
    return res.clientSecret;
  });

const checkout = stripe.initCheckoutElementsSdk({
  clientSecret,
  elementsOptions,
});

const taxIdElementOptions = {
  visibility: "always",
};
const taxIdElement = checkout.createTaxIdElement(taxIdElementOptions);
taxIdElement.mount("#tax-id-element");
```

For more information about using the Tax ID Element with Checkout Sessions, see the [Checkout Sessions integration guide](https://docs.stripe.com/payments/advanced/tax.md?api-integration=checkout#enable-tax-id-collection).

# Payment Intents API

> This is a Payment Intents API for when payment-ui is elements. View the full page at https://docs.stripe.com/elements/tax-id-element?payment-ui=elements.

Here’s how you can use the [Tax ID Element](https://docs.stripe.com/js/elements_object/create_tax_id_element) with the Payment Intents API to collect tax IDs:

```html
<div class="tax-id-form">
  <div id="tax-id-element"></div>
</div>
```

```javascript
const stripe = window.Stripe("<<YOUR_PUBLISHABLE_KEY>>", {
  betas: ["elements_tax_id_1"],
});

// Create a PaymentIntent on your server
const { clientSecret } = await fetch("/create-payment-intent", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
}).then((res) => res.json());

const appearance = {
  /* appearance */
};
const elements = stripe.elements({
  clientSecret,
  appearance,
});

const taxIdElementOptions = {
  visibility: "always",
};
const taxIdElement = elements.create("taxId", taxIdElementOptions);
taxIdElement.mount("#tax-id-element");
```

To save and redisplay the tax ID, you must create a [CustomerSession](https://docs.stripe.com/api/customer_sessions.md). For more information about using the Tax ID Element with Payment Intents API, see the [integration guide](https://docs.stripe.com/payments/advanced/tax.md?api-integration=elements#collect-customer-tax-ids).
