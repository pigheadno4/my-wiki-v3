<!-- Source URL: https://docs.stripe.com/payments/afterpay-clearpay/site-messaging -->
<!-- Fetched: 2026-05-06 -->

# Display Afterpay or Clearpay messaging

Inform customers that you accept payments with Afterpay (also known as Clearpay in the UK).

> This doc refers to a *Legacy* (Technology that's no longer recommended) feature that’s no longer available in the latest version of Stripe.js. We recommend you use the [Payment Method Messaging Element](https://docs.stripe.com/elements/payment-method-messaging.md) to dynamically show your customers relevant buy now, pay later payment options for their purchase.

Let your customers know you accept payments with Afterpay by including the Afterpay messaging Element on your site. We suggest adding the messaging Element to your product, cart, and payment pages. The [afterpayClearpayMessage](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage) Element takes care of:

- Calculating and displaying the installments amount
- Displaying the Afterpay information modal
- Localizing text and currencies

## Include the Element

#### HTML + JS

Use Stripe Elements to include the [afterpayClearpayMessage](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage) Element on your site.

If you haven’t already, include the Stripe.js script on your page by adding it to the `head` of your HTML file:

```html
<script src="https://js.stripe.com/clover/stripe.js"></script>
```

Create a placeholder element on your page where you want to mount the messaging Element:

```html
<div id="afterpay-clearpay-message"></div>
```

On your product, cart, and payment pages, include the following code to create an instance of Stripe.js and mount the messaging Element:

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

const elements = stripe.elements();

const options = {
  amount: 1000, // 10.00 USD
  currency: "USD",
};

const afterpayClearpayMessageElement = elements.create(
  "afterpayClearpayMessage",
  options,
);

afterpayClearpayMessageElement.mount("#afterpay-clearpay-message");
```

#### React

Use Stripe Elements to include the [afterpayClearpayMessage](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage) Element on your site.

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

On your product, cart, and payment pages, include the `AfterpayClearpayMessageElement` Component:

```jsx
import {
  Elements,
  AfterpayClearpayMessageElement,
} from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

const ProductDetail = () => (
  <div>
    {/* ... */}
    <Elements stripe={stripePromise}>
      <AfterpayClearpayMessageElement
        options={{ amount: 1000, currency: "USD" }}
      />
    </Elements>
  </div>
);
```

## Customize the message

There are many options available to customize the appearance and contents of the messaging Element. See the [API reference](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage) for the full list of options.

#### Badge logo

Set `logoType` to `'badge'` and use the `badgeTheme` option to choose between the following styles.

#### Lockup logo

Set `logoType` to `'lockup'` and use the `lockupTheme` option to choose between the following styles.

> Clearpay branding is displayed automatically based on the `locale` option. See [Locale and currency](https://docs.stripe.com/payments/afterpay-clearpay/site-messaging.md#locale-and-currency) for details.

### Style with CSS

In addition to the configuration options, use CSS to style the messaging to better fit the look and feel of your site. You can customize the `font-family`, `font-size`, and `color` of the messaging.

You can also control the size of the logo by setting its `width` and `height`.

## Handle ineligible items

You can’t use Afterpay for certain [prohibited business categories](https://docs.stripe.com/payments/afterpay-clearpay.md#prohibited-business-categories). If you sell items in these categories, you can still display the messaging Element to clearly indicate Afterpay isn’t available.

Use the `isEligible` or `isCartEligible` options to indicate that the current product or cart isn’t eligible.

Afterpay also has [default transactions limits](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule) for each country. When the provided `amount` exceeds these limits, the Element automatically displays ineligible price range messaging. You can customize this message by hiding the lower or upper limit with `showLowerLimit` and `showUpperLimit`.

## Locale and currency

Afterpay and clearpay support the following locales and currencies:

Supported locales: `en-US`, `en-CA`, `en-AU`, `en-NZ`, `en-GB`

Supported currencies: `USD`, `CAD`, `AUD`, `NZD`, `GBP`

Afterpay’s messaging always the appropriate number of installments a user can pay based on their locale and country. For more information, see [payment collection](https://docs.stripe.com/payments/afterpay-clearpay.md#collection-schedule).

#### HTML + JS

Set the locale of your message by passing the `locale` option into the `options` parameter of the [elements group](https://docs.stripe.com/js/elements_object/create) used to create the `afterpayClearpayMessage` Element. You can then define your `currency` by passing it to the [element.create](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage) options directly.

#### React

Set the locale of your message by passing `locale` into the `options` prop of the `Elements` provider. Define your `currency` by passing it to the `options` prop of the `AfterpayClearpayMessageElement` component.
