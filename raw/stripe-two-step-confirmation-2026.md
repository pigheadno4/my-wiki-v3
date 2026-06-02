<!-- Source URL: https://docs.stripe.com/payments/build-a-two-step-confirmation -->
<!-- Fetched: 2026-05-11 -->

# Build two-step confirmation

Add an optional review page or run validations after a user enters their payment details.

While we recommend the [standard integration](https://docs.stripe.com/payments/accept-a-payment-deferred.md) for most scenarios, this integration allows you to add an extra step in your checkout. This allows you to perform other actions before confirming the order, such as:

- Presenting the customer their order details for review.
- Running additional validations.
- Calculating tax and updating the total due.

## Set up Stripe

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Enable payment methods

> This integration path doesn’t support BLIK or pre-authorized debits that use the Automated Clearing Settlement System (ACSS). Also, if you create the deferred intent from the client-side, you can’t use `customer_balance` with dynamic payment methods because the PaymentIntent requires a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/object.md) object, which the client-side flow doesn’t support. To use `customer_balance`, create the `PaymentIntent` server-side with an `Account` or `Customer` and return its `client_secret` to the client.

View your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods) and enable the payment methods you want to support. You need at least one payment method enabled to create a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods).

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md) for product and payment method support, and our [pricing page](https://stripe.com/pricing/local-payment-methods) for fees.

## Collect payment details [Client-side]

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to securely send payment information collected in an iFrame to Stripe over an HTTPS connection.

> #### Conflicting iFrames
>
> Avoid placing the Payment Element within another iframe because it conflicts with payment methods that require redirecting to another page for payment confirmation.

Your checkout page URL must start with `https://` rather than `http://` for your integration to work. You can test your integration without using HTTPS, but remember to [enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

#### HTML + JS

### Set up Stripe.js

The Payment Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of Stripe with the following JavaScript on your checkout page:

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

### Add the Payment Element to your checkout page

The Payment Element needs a place to live on your checkout page. Create an empty DOM node (container) with a unique ID in your payment form:

```html
<form id="payment-form">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>
  <button id="submit">Submit</button>
  <div id="error-message">
    <!-- Display error message to your customers here -->
  </div>
</form>
```

After your form loads, create an Elements instance with the mode, amount, and currency. These values determine which payment methods the Element presents to your customer.

Then, create an instance of the Payment Element and mount it to the container DOM node.

```javascript
const options = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout formconst elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

#### React

### Set up Stripe.js

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add and configure the Elements provider to your checkout page

To use the Payment Element component, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key, and pass the returned `Promise` to the `Elements` provider.

The `Elements` provider also accepts the mode, amount, and currency. These values determine which payment methods are shown to your customer.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import CheckoutForm from "./CheckoutForm";

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  const options = {
    mode: "payment",
    amount: 1099,
    currency: "usd",
    // Fully customizable with appearance API.
    appearance: {
      /*...*/
    },
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Add the Payment Element component

Use the `PaymentElement` component to build your form.

```jsx
import React from "react";
import { PaymentElement } from "@stripe/react-stripe-js";

const CheckoutForm = () => {
  return (
    <form>
      <PaymentElement />
      <button>Submit</button>
    </form>
  );
};

export default CheckoutForm;
```

The Payment Element renders a dynamic form that allows your customer to pick a payment method. The form automatically collects all necessary payments details for the payment method selected by the customer.

You can customize the Payment Element to match the design of your site by passing the [appearance object](https://docs.stripe.com/elements/appearance-api.md) into `options` when creating the `Elements` provider.

### Collect addresses

By default, the Payment Element only collects the necessary billing address details. Some behavior, such as [calculating tax](https://docs.stripe.com/api/tax/calculations/create.md) or entering shipping details, requires your customer’s full address. You can:

- Use the [Address Element](https://docs.stripe.com/elements/address-element.md) to take advantage of autocomplete and localization features to collect your customer’s full address. This helps ensure the most accurate tax calculation.
- Collect address details using your own custom form.

## Optional: Customize the layout [Client-side]

You can customize the Payment Element’s layout (accordion or tabs) to fit your checkout interface. For more information about each of the properties, see [elements.create](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options).

#### Accordion

You can start using the layout features by passing a layout `type` and other optional properties when creating the Payment Element:

```javascript
const paymentElement = elements.create("payment", {
  layout: {
    type: "accordion",
    defaultCollapsed: false,
    radios: "always",
    spacedAccordionItems: false,
  },
});
```

#### Tabs

### Specify the layout

Set the value for layout to `tabs`. You also have the option to specify other properties, such as the ones in the following example:

```javascript
const paymentElement = elements.create("payment", {
  layout: {
    type: "tabs",
    defaultCollapsed: false,
  },
});
```

The following image is the same Payment Element rendered using different layout configurations:
![Three checkout form experiences](assets/stripe-payment-element-layouts.png)

Payment Element layouts

## Optional: Customize the appearance [Client-side]

Now that you’ve added the Payment Element to your page, you can customize its appearance to make it fit your design. To learn more about customizing the Payment Element, see [Elements Appearance API](https://docs.stripe.com/elements/appearance-api.md).
![Customize the Payment Element](assets/stripe-payment-element-appearance.png)

Customize the Payment Element

## Optional: Save and retrieve customer payment methods

You can configure the Payment Element to save your customer’s payment methods for future use. This section shows you how to integrate the [saved payment methods feature](https://docs.stripe.com/payments/save-customer-payment-methods.md), which enables the Payment Element to:

- Prompt buyers for consent to save a payment method
- Save payment methods when buyers provide consent
- Display saved payment methods to buyers for future purchases
- [Automatically update lost or expired cards](https://docs.stripe.com/payments/cards/overview.md#automatic-card-updates) when buyers replace them
  ![The Payment Element and a saved payment method checkbox](assets/stripe-payment-element-spm-save.png)

Save payment methods.
![The Payment Element with a Saved payment method selected](assets/stripe-payment-element-spm-saved.png)

Reuse a previously saved payment method.

### Enable saving the payment method in the Payment Element

Create a [CustomerSession](https://docs.stripe.com/api/customer_sessions/.md) on your server by providing the customer’s ID (using either `customer` for a `Customer` object or `customer_account` for a customer-configured `Account` object) and enabling the [payment_element](https://docs.stripe.com/api/customer_sessions/object.md#customer_session_object-components-payment_element) component for your session. Configure which saved payment method [features](https://docs.stripe.com/api/customer_sessions/create.md#create_customer_session-components-payment_element-features) you want to enable. For instance, enabling [payment_method_save](https://docs.stripe.com/api/customer_sessions/create.md#create_customer_session-components-payment_element-features-payment_method_save) displays a checkbox that allows customers to save their payment details for future use.

You can specify `setup_future_usage` on a PaymentIntent or Checkout Session to override the default behavior for saving payment methods. This ensures that you automatically save the payment method for future use, even if the customer doesn’t explicitly choose to save it. If you intend to specify `setup_future_usage`, don’t set `payment_method_save_usage` in the same payment transaction because this causes an integration error.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

app.post('/create-customer-session', async (req, res) => {
  const customerSession = await stripe.customerSessions.create({
    customer_account: {{CUSTOMER_ACCOUNT_ID}},
    components: {
      payment_element: {
        enabled: true,
        features: {
          payment_method_redisplay: 'enabled',
          payment_method_save: 'enabled',
          payment_method_save_usage: 'off_session',
          payment_method_remove: 'enabled',
        },
      },
    },
  });
  res.json({
    customer_session_client_secret: customerSession.client_secret
  });
});
```

#### Customers v1

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

app.post('/create-customer-session', async (req, res) => {
  const customerSession = await stripe.customerSessions.create({
    customer: {{CUSTOMER_ID}},
    components: {
      payment_element: {
        enabled: true,
        features: {
          payment_method_redisplay: 'enabled',
          payment_method_save: 'enabled',
          payment_method_save_usage: 'off_session',
          payment_method_remove: 'enabled',
        },
      },
    },
  });
  res.json({
    customer_session_client_secret: customerSession.client_secret
  });
});
```

Your Elements instance uses the CustomerSession’s _client secret_ (A client secret is used with your publishable key to authenticate a request for a single object. Each client secret is unique to the object it's associated with) to access that customer’s saved payment methods. [Handle errors](https://docs.stripe.com/error-handling.md) properly when you create the CustomerSession. If an error occurs, you don’t need to provide the CustomerSession client secret to the Elements instance, as it’s optional.

Create the Elements instance using the CustomerSession client secret. Then, use the Elements instance to create a Payment Element.

```javascript
// Create the CustomerSession and obtain its clientSecret
const res = await fetch("/create-customer-session", {
  method: "POST",
});

const { customer_session_client_secret: customerSessionClientSecret } =
  await res.json();

const elementsOptions = {
  mode: "payment",
  amount: 1099,
  currency: "usd",
  customerSessionClientSecret,
  // Fully customizable with appearance API.
  appearance: {
    /*...*/
  },
};

// Set up Stripe.js and Elements to use in checkout form, passing the client secret
// and CustomerSession's client secret obtained in a previous step
const elements = stripe.elements(elementsOptions);

// Create and mount the Payment Element
const paymentElementOptions = { layout: "accordion" };
const paymentElement = elements.create("payment", paymentElementOptions);
paymentElement.mount("#payment-element");
```

When confirming the PaymentIntent, Stripe.js automatically controls setting [setup_future_usage](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-setup_future_usage) on the PaymentIntent and [allow_redisplay](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-allow_redisplay) on the PaymentMethod, depending on whether the customer checked the box to save their payment details.

### Enforce CVC recollection

Optionally, specify `require_cvc_recollection` both [when creating the PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card-require_cvc_recollection) and [when creating Elements](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions-card-require_cvc_recollection) to enforce CVC recollection when a customer is paying with a card.

### Detect the selection of a saved payment method

To control dynamic content when a saved payment method is selected, listen to the Payment Element `change` event, which is populated with the selected payment method.

```javascript
paymentElement.on("change", function (event) {
  if (event.value.payment_method) {
    // Control dynamic content if a saved payment method is selected
  }
});
```

## Optional: Additional Elements options [Client-side]

The [Elements object](https://docs.stripe.com/js/elements_object/create_without_intent) accepts additional options that influence payment collection. Based on the options provided, the Payment Element displays available payment methods from those you’ve enabled. Learn more about [payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md).

Make sure the Elements options you provide (such as `captureMethod`, `setupFutureUsage`, and `paymentMethodOptions`) match the equivalent parameters you pass when creating and confirming the Intent. Mismatched parameters can result in unexpected behavior or errors.

| Property | Type        | Description | Required |
| -------- | ----------- | ----------- | -------- |
| `mode`   | - `payment` |

- `setup`
- `subscription` | Indicates whether the Payment Element is used with a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods), _SetupIntent_ (The Setup Intents API lets you build dynamic flows for collecting payment method details for future payments. It tracks the lifecycle of a payment setup flow and can trigger additional authentication steps if required by law or by the payment method), or _Subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis). | Yes |
  | `currency` | `string` | The currency of the amount to charge the customer. | Yes |
  | `amount` | `number` | The amount to charge the customer, shown in Apple Pay, Google Pay, or BNPL UIs. | For `payment` and `subscription` mode |
  | `setupFutureUsage` | - `off_session`
- `on_session` | Indicates that you intend to make future payments with the payment details collected by the Payment Element. | No |
  | `captureMethod` | - `automatic`
- `automatic_async`
- `manual` | Controls when to capture the funds from the customer’s account. | No |
  | `onBehalfOf` | `string` | Connect only. The Stripe account ID, which is the business of record. See [use cases](https://docs.stripe.com/connect/charges.md) to determine if this option is relevant for your integration. | No |
  | `paymentMethodTypes` | `string[]` | A list of payment method types to render. You can omit this attribute to manage your payment methods in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). | No |
  | `paymentMethodConfiguration` | `string` | The [payment method configuration](https://docs.stripe.com/api/payment_method_configurations.md) to use when managing your payment methods in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). If not specified, your default configuration is used. | No |
  | `paymentMethodCreation` | `manual` | Allows PaymentMethods to be created from the Elements instance using [stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method_elements). | No |
  | `paymentMethodOptions` | `{us_bank_account: {verification_method: string}}` | Verification options for the `us_bank_account` payment method. Accepts the same verification methods as [Payment Intents](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-us_bank_account-verification_method). | No |
  | `paymentMethodOptions` | `{card: {installments: {enabled: boolean}}}` | Allows manually enabling the card installment plan selection UI if applicable when you aren’t managing your payment methods in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). You must set `mode='payment'` _and_ explicitly specify `paymentMethodTypes`. Otherwise an error is raised. Incompatible with `paymentMethodCreation='manual'`. | No |
  | `paymentMethodOptions` | `{[paymentMethod]: {setup_future_usage: string}}` | Allows you to specify `setup_future_usage` for only payment methods that support reuse. Only applicable when `mode` is `payment`. The value for each payment method must match the corresponding `payment_method_options[paymentMethod][setup_future_usage]` on the PaymentIntent during confirmation. See the [Stripe.js reference](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodOptions) for supported payment methods and values. | No |

## Create a ConfirmationToken [Client-side]

> #### Use createPaymentMethod through a legacy implementation
>
> If you’re using a legacy implementation, you might be using the information from `stripe.createPaymentMethod` to finalize payments on the server. Although we encourage you to follow this guide to [Migrate to Confirmation Tokens](https://docs.stripe.com/payments/payment-element/migration-ct.md), you can still access our old documentation to [Build two-step confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation-legacy.md).

When the customer submits your payment form, call [stripe.createConfirmationToken](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token) to create a _ConfirmationToken_ (ConfirmationTokens help capture data from your client, such as your customer's payment instruments and shipping address, and are used to confirm a PaymentIntent or SetupIntent) to send to your server for additional validation or business logic before confirmation. You can inspect the [`payment_method_preview`](https://docs.stripe.com/api/confirmation_tokens/object.md#confirmation_token_object-payment_method_preview) field to run the additional logic.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");
const submitBtn = document.getElementById("submit");

const handleError = (error) => {
  const messageContainer = document.querySelector("#error-message");
  messageContainer.textContent = error.message;
  submitBtn.disabled = false;
};

form.addEventListener("submit", async (event) => {
  // We don't want to let default form submission happen here,
  // which would refresh the page.
  event.preventDefault();

  // Prevent multiple form submissions
  if (submitBtn.disabled) {
    return;
  }

  // Disable form submission while loading
  submitBtn.disabled = true;

  // Trigger form validation and wallet collection
  const { error: submitError } = await elements.submit();
  if (submitError) {
    handleError(submitError);
    return;
  }

  // Create the ConfirmationToken using the details collected by the Payment Element
  const { error, confirmationToken } = await stripe.createConfirmationToken({
    elements,
    params: {
      payment_method_data: {
        billing_details: {
          name: "Jenny Rosen",
        },
      },
    },
  });

  if (error) {
    // This point is only reached if there's an immediate error when
    // creating the ConfirmationToken. Show the error to your customer (for example, payment details incomplete)
    handleError(error);
    return;
  }

  // Now that you have a ConfirmationToken, you can use it in the following steps to render a confirmation page or run additional validations on the server
  return fetchAndRenderSummary(confirmationToken);
});
```

#### React

```jsx
import React, { useState } from "react";
import {
  useStripe,
  useElements,
  PaymentElement,
} from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  const [errorMessage, setErrorMessage] = useState();
  const [loading, setLoading] = useState(false);

  const handleError = (error) => {
    setLoading(false);
    setErrorMessage(error.message);
  };

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    setLoading(true);

    // Trigger form validation and wallet collection
    const { error: submitError } = await elements.submit();
    if (submitError) {
      handleError(submitError);
      return;
    }

    // Create the ConfirmationToken using the details collected by the Payment Element
    const { error, confirmationToken } = await stripe.createConfirmationToken({
      elements,
      params: {
        payment_method_data: {
          billing_details: {
            name: "Jenny Rosen",
          },
        },
      },
    });

    if (error) {
      // This point is only reached if there's an immediate error when
      // creating the ConfirmationToken. Show the error to your customer (for example, payment details incomplete)
      handleError(error);
      return;
    }

    // Now that you have a ConfirmationToken, you can use it in the following steps to render a confirmation page or run additional validations on the server
    return fetchAndRenderSummary(confirmationToken);
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button type="submit" disabled={!stripe || loading}>
        Submit
      </button>
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  );
}
```

## Show the payment details on the confirmation page

At this point, you have all of the information you need to render the confirmation page. Call the server to obtain the necessary information and render the confirmation page accordingly.

#### Node.js

```javascript
// Using Express
const express = require("express");
const app = express();
app.use(express.json());

app.post("/summarize-payment", async (req, res) => {
  try {
    // Retrieve the confirmationTokens and generate the response
    const confirmationToken = await stripe.confirmationTokens.retrieve(
      req.body.confirmation_token_id,
    );
    const response = summarizePaymentDetails(confirmationToken);

    // Send the response to the client
    res.json(response);
  } catch (e) {
    // Display error on client
    return res.json({ error: e.message });
  }
});

function summarizePaymentDetails(confirmationToken) {
  // Use confirmationToken.payment_method_preview to derive the applicable summary fields for your UI
  return {
    type: confirmationToken.payment_method_preview.type,
    // Add other values (such as Tax Calculation amount) as needed here
  };
}
```

#### JavaScript

```javascript
const fetchAndRenderSummary = async (confirmationToken) => {
  const res = await fetch("/summarize-payment", {
    method: "POST",
    body: JSON.stringify({ confirmation_token_id: confirmationToken.id }),
  });

  const summary = await res.json();

  // Render the summary object returned by your server
};
```

## Optional: Calculate Tax before checkout [Server-side]

The Payment Element doesn’t calculate tax by default. Use the [Tax API](https://docs.stripe.com/api/tax.md) to calculate the tax owed on the transaction.

> To calculate tax in the Payment Element, you must first:
>
> - [Enable Stripe Tax](https://docs.stripe.com/tax/calculating.md).

- [Collect the billing address](https://docs.stripe.com/payments/build-a-two-step-confirmation.md#collect-addresses)

Update the `summarizePaymentDetails` function to create a Tax Calculation based on the customer billing address returned in the ConfirmationToken.

### Before

```js
function summarizePaymentDetails(confirmationToken) {
  // Use confirmationToken.payment_method_preview to derive the applicable summary fields for your UI
}
```

### After

```js
  function summarizePaymentDetails(confirmationToken) {
    tax_calculation = await stripe.tax.calculations.create({
      currency: 'usd',
      line_items: [
        {
          amount: 1000,
          reference: 'L1',
        },
      ],
      customer_details: {// Use ConfirmationToken's address for TaxCalculation
        address: confirmationToken.paymentMethodPreview.billingDetails.address,
        address_source: 'shipping',
      },
    });
```

Update the return to include the Tax Calculation `amount_total`, which represents the charge amount plus the tax, so you can present the customer with the total amount owed.

### Before

```js
return {
  type: confirmationToken.payment_method_preview.type,
  // Add other values as needed here
};
```

### After

```js
return {
  type: confirmationToken.payment_method_preview.type, // Add any other values from TaxCalculation for your display purposes. For example, you can use [tax_breakdown](/tax/standalone-tax-api#tax-breakdowns) to display what tax was applied
  amount_total: tax_calculation.amount_total,
  tax_calculation_id: tax_calculation.id,
  // Add other values as needed here
};
```

## Create a PaymentIntent [Server-side]

> #### Run custom business logic immediately before payment confirmation
>
> Navigate to [step 5](https://docs.stripe.com/payments/finalize-payments-on-the-server.md?platform=web&type=payment#submit-payment) in the finalize payments guide to run your custom business logic immediately before payment confirmation. Otherwise, follow the steps below for a simpler integration, which uses `stripe.confirmPayment` on the client to both confirm the payment and handle any next actions.

When the customer submits your payment form, create a _PaymentIntent_ (The Payment Intents API tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods) on your server with an `amount` and `currency` enabled.

Return the _client secret_ (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) value to your client for Stripe.js to use to complete the payment process.

The following example includes commented code to illustrate the optional [Tax Calculation](https://docs.stripe.com/payments/build-a-two-step-confirmation.md#calculate-tax).

#### Accounts v2

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  // If you used a Tax Calculation, optionally recalculate taxes
  //const confirmationToken = await stripe.confirmationTokens.retrieve(req.body.confirmation_token_id)
  //const summarizePaymentDetails = summarizePaymentDetails(confirmationToken)

  const intent = await stripe.paymentIntents.create(
    {
      // To allow saving and retrieving payment methods, provide the Account ID.
      customer_account: customer_account.id,
      // If you used a Tax Calculation, use its `amount_total`.
      //amount: summarizePaymentDetails.amount_total,
      amount: 1099,
      currency: "usd",
      // Specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
      automatic_payment_methods: { enabled: true },
      // If you used a Tax Calculation, link it to the PaymentIntent to make sure any transitions accurately reflect the tax.
      //hooks: {
      //  inputs: {
      //    tax: {
      //      calculation: tax_calculation.id
      //    }
      //  }
      //}
    },
    //{
    //  stripe_version: '2025-09-30.preview'
    //}
  );
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

#### Customers v1

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");
const express = require("express");
const app = express();

app.use(express.static("."));

app.post("/create-intent", async (req, res) => {
  // If you used a Tax Calculation, optionally recalculate taxes
  //const confirmationToken = await stripe.confirmationTokens.retrieve(req.body.confirmation_token_id)
  //const summarizePaymentDetails = summarizePaymentDetails(confirmationToken)

  const intent = await stripe.paymentIntents.create(
    {
      // To allow saving and retrieving payment methods, provide the Customer ID.
      customer: customer.id,
      // If you used a Tax Calculation, use its `amount_total`.
      //amount: summarizePaymentDetails.amount_total,
      amount: 1099,
      currency: "usd",
      // Specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
      automatic_payment_methods: { enabled: true },
      // If you used a Tax Calculation, link it to the PaymentIntent to make sure any transitions accurately reflect the tax.
      //hooks: {
      //  inputs: {
      //    tax: {
      //      calculation: tax_calculation.id
      //    }
      //  }
      //}
    },
    //{
    //  stripe_version: '2025-09-30.preview'
    //}
  );
  res.json({ client_secret: intent.client_secret });
});

app.listen(3000, () => {
  console.log("Running on port 3000");
});
```

## Submit the payment to Stripe [Client-side]

Use [stripe.confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) to complete the payment using details from the Payment Element.

Provide the `confirmation_token` parameter with the ID of the ConfirmationToken you created on the previous page, which contains the payment information collected from the Payment Element.

Provide a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to this function to indicate where Stripe redirects the user after they complete the payment. Your user might be initially redirected to an intermediate site, such as a bank authorization page, before being redirected to the `return_url`. Card payments immediately redirect to the `return_url` when a payment is successful.

If you don’t want to redirect for card payments after payment completion, you can set [redirect](https://docs.stripe.com/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect) to `if_required`. This only redirects customers that check out with redirect-based payment methods.

#### HTML + JS

```javascript
const form = document.getElementById("payment-form");
const submitBtn = document.getElementById("submit");

const handleError = (error) => {
  const messageContainer = document.querySelector("#error-message");
  messageContainer.textContent = error.message;
  submitBtn.disabled = false;
};

form.addEventListener("submit", async (event) => {
  // We don't want to let default form submission happen here,
  // which would refresh the page.
  event.preventDefault();

  // Prevent multiple form submissions
  if (submitBtn.disabled) {
    return;
  }

  // Disable form submission while loading
  submitBtn.disabled = true;

  // Create the PaymentIntent and obtain clientSecret
  const res = await fetch("/create-intent", {
    method: "POST",
  });

  const { client_secret: clientSecret } = await res.json();

  // Confirm the PaymentIntent using the details collected by the ConfirmationToken
  const { error } = await stripe.confirmPayment({
    clientSecret,
    confirmParams: {
      confirmation_token: "{{CONFIRMATION_TOKEN_ID}}",
      return_url: "https://example.com/order/123/complete",
    },
  });

  if (error) {
    // This point is only reached if there's an immediate error when
    // confirming the payment. Show the error to your customer (for example, payment details incomplete)
    handleError(error);
  } else {
    // Your customer is redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer is redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});
```

#### React

```jsx
import React, { useState } from "react";
import {
  useStripe,
  useElements,
  PaymentElement,
} from "@stripe/react-stripe-js";

export default function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();

  const [errorMessage, setErrorMessage] = useState();
  const [loading, setLoading] = useState(false);

  const handleError = (error) => {
    setLoading(false);
    setErrorMessage(error.message);
  };

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    setLoading(true);

    // Create the PaymentIntent and obtain clientSecret
    const res = await fetch("/create-intent", {
      method: "POST",
    });

    const { client_secret: clientSecret } = await res.json();

    // Confirm the PaymentIntent using the details collected by the ConfirmationToken
    const { error } = await stripe.confirmPayment({
      clientSecret,
      confirmParams: {
        confirmation_token: "{{CONFIRMATION_TOKEN_ID}}",
        return_url: "https://example.com/order/123/complete",
      },
    });

    if (error) {
      // This point is only reached if there's an immediate error when
      // confirming the payment. Show the error to your customer (for example, payment details incomplete)
      handleError(error);
    } else {
      // Your customer is redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer is redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button type="submit" disabled={!stripe || loading}>
        Submit Payment
      </button>
      {errorMessage && <div>{errorMessage}</div>}
    </form>
  );
}
```

## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide services to you, prevent fraud, and improve its services. This includes using cookies and IP addresses to identify which Elements a customer saw during a single checkout session. You’re responsible for disclosing and obtaining all rights and consents necessary for Stripe to use data in these ways. For more information, visit our [privacy center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).

## See also

[Design an integration](https://docs.stripe.com/payments/payment-element/design-an-integration.md)
