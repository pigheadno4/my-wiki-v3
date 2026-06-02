<!-- Source URL: https://docs.stripe.com/payments/affirm/affirm-messaging -->
<!-- Fetched: 2026-05-06 -->

# Display Affirm messaging

Increase conversion by informing customers that you offer Affirm ahead of checkout.

> This doc refers to a *Legacy* (Technology that's no longer recommended) feature that’s no longer available in the latest version of Stripe.js. We recommend you use the [Payment Method Messaging Element](https://docs.stripe.com/elements/payment-method-messaging.md) to dynamically show your customers relevant buy now, pay later payment options for their purchase.

Let your customers know you accept payments with Affirm by including the Affirm messaging Element on your site. We suggest adding the messaging Element to your product, cart, and payment pages. The Affirm messaging Element takes care of:

- Calculating and displaying the installments amount
- Displaying the Affirm information modal

## Include the Element

> Affirm’s minimum transaction amount is 50 USD or 50 CAD. The promotional message isn’t rendered if the amount parameter is set to a number less than 50 USD or 50 CAD.

#### HTML + JS

Use Stripe Elements to include the [affirmMessage](https://docs.stripe.com/js/elements_object/create_element?type=affirmMessage) Element on your site.

If you haven’t already, include the Stripe.js script on your page by adding it to the `head` of your HTML file:

```html
<script src="https://js.stripe.com/clover/stripe.js"></script>
```

Create a placeholder element on your page where you want to mount the messaging Element:

```html
<div id="affirm-message"></div>
```

On your product, cart, and payment pages, include the following code to create an instance of Stripe.js and mount the messaging Element:

```javascript
// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");

const elements = stripe.elements();

const options = {
  amount: 5000, // 50.00 USD
  currency: "USD",
};

const affirmMessageElement = elements.create("affirmMessage", options);

affirmMessageElement.mount("#affirm-message");
```

#### React

Use Stripe Elements to include the [affirmMessage](https://docs.stripe.com/js/elements_object/create_element?type=affirmMessage) Element on your site.

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

On your product, cart, and payment pages, include the `AffirmMessageElement` Component:

```jsx
import { Elements, AffirmMessageElement } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

const ProductDetail = () => (
  <div>
    {/* ... */}
    <Elements stripe={stripePromise}>
      <AffirmMessageElement options={{ amount: 5000, currency: "USD" }} />
    </Elements>
  </div>
);
```

## Customize the message

There are many options available to customize the appearance and contents of the messaging Element. See the [API reference](https://docs.stripe.com/js/elements_object/create_element?type=affirmMessage) for the full list of options.

### Logo color

Use the `logoColor` option to choose between the following styles.

### Style with CSS

Additional configuration options allow you to use CSS to style the messaging to better fit the look and feel of your site. You can customize the `fontColor`, `fontSize`, and `textAlign` of the messaging.
