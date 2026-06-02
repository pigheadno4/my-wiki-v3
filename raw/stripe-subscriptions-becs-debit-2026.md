<!-- Source URL: https://docs.stripe.com/billing/subscriptions/au-becs-debit -->
<!-- Fetched: 2026-05-13 -->

# Set up a subscription with BECS Direct Debit in Australia

Learn how to create and charge for a subscription with BECS Direct Debit.

> If you’re a new user, use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) instead of using Stripe Elements as described in this guide. The Payment Element provides a low-code integration path with built-in conversion optimizations. For instructions, see [Build a subscription](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=elements).

Use this guide to set up a _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) using [BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit.md) as a payment method.

## Create a product and price [Dashboard]

[Products](https://docs.stripe.com/api/products.md) represent the item or service you’re selling. [Prices](https://docs.stripe.com/api/prices.md) define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 AUD monthly subscription. To model this:

1. Go to the [Products](https://dashboard.stripe.com/products?active=true) page and click **Create product**.
1. Enter a **Name** for the product. You can optionally add a **Description** and upload an image of the product.
1. Select a **Product tax code**. Learn more about [product tax codes](https://docs.stripe.com/tax/tax-codes.md).
1. Select **Recurring**. Then enter **15** for the price and select **AUD** as the currency.
1. Choose whether to **Include tax in price**. You can either use the default value from your [tax settings](https://dashboard.stripe.com/test/settings/tax) or set the value manually. In this example, select **Auto**.
1. Select **Monthly** for the **Billing period**.
1. Click **More pricing options**. Then select **Flat rate** as the pricing model for this example. Learn more about [flat rate](https://docs.stripe.com/products-prices/pricing-models.md#flat-rate) and other [pricing models](https://docs.stripe.com/products-prices/pricing-models.md).
1. Add an internal **Price description** and [Lookup key](https://docs.stripe.com/products-prices/manage-prices.md#lookup-keys) to organize, query, and update specific prices in the future.
1. Click **Next**. Then click **Add product**.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: `price_G0FvDp6vZvdwRZ`.

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` will track the steps of this set-up process. For BECS Direct Debit, this includes collecting a mandate from the customer and tracking its validity throughout its lifecycle.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server with [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) set to `au_becs_debit`:

#### Node.js

```javascript
// Using Express
const express = require("express");
const app = express();
app.use(express.json());
const { resolve } = require("path");

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ["au_becs_debit"],
});
const clientSecret = setupIntent.client_secret;
// Pass the client secret to the client
```

The returned `SetupIntent` object contains a `client_secret` property. Pass the client secret to the client-side application to continue with the setup process.

## Collect payment method details and mandate acknowledgment [Client-side]

You’re ready to collect payment information on the client with [Stripe Elements](https://docs.stripe.com/payments/elements.md). Elements is a set of prebuilt UI components for collecting payment details.

A Stripe Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection. The checkout page address must also start with https:// rather than http:// for your integration to work.

You can test your integration without using HTTPS. [Enable it](https://docs.stripe.com/security/guide.md#tls) when you’re ready to accept live payments.

### Set up Stripe Elements

#### HTML + JS

Stripe Elements is automatically available as a feature of Stripe.js. Include the Stripe.js script on your payment page by adding it to the `head` of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Payment Setup</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create an instance of [Elements](https://docs.stripe.com/js.md#stripe-elements) with the following JavaScript on your payment page:

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
const elements = stripe.elements();
```

### Direct Debit Requests

Before you can create a BECS Direct Debit payment, your customer must agree with the Direct Debit Request Service Agreement. They do so by submitting a completed Direct Debit Request (DDR). The approval gives you a mandate to debit their account. The `Mandate` is a record of the permission to debit a payment method.

For online mandate acceptance, you can create a form to collect the necessary information. Serve the form over [HTTPS](https://docs.stripe.com/security/guide.md#tls) and capture the following information:

| Information        | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| **Account name**   | The full name of the account holder                                       |
| **BSB number**     | The Bank-State-Branch number of the bank account (for example, `123-456`) |
| **Account number** | The bank account number (for example, `87654321`)                         |

When collecting a Direct Debit Request, follow our [BECS Direct Debit Terms](https://stripe.com/au-becs/legal) and as part of your checkout form:

- Display the exact terms of [Stripe’s DDR service agreement](https://stripe.com/au-becs-dd-service-agreement/legal) either inline on the form, or on a page linked from the form, and identifying it as the “DDR service agreement.”
- Make sure the accepted DDR and its accompanying [DDR service agreement](https://stripe.com/au-becs-dd-service-agreement/legal) can be shared with your customer at all times, either as a printed or non-changeable electronic copy (such as email). Stripe hosts this for you.
- Display the following standard authorization text for your customer to accept the BECS DDR, where you replace _Rocketship Inc_ with your company name. Their acceptance authorizes you to initiate BECS Direct Debit payments from their bank account.

> By providing your bank account details, you agree to this Direct Debit Request and the [Direct Debit Request service agreement](https://stripe.com/au-becs-dd-service-agreement/legal), and authorize Stripe Payments Australia Pty Ltd ACN 160&nbsp;180&nbsp;343 Direct Debit User ID number 507156 (“Stripe”) to debit your account through the Bulk Electronic Clearing System (BECS) on behalf of _Rocketship Inc_ (the “Merchant”) for payments as per the terms of your agreement with the Merchant. You certify that you’re either an account holder or an authorized signatory on the account listed above.

The details of the accepted mandate are generated when setting up a [PaymentMethod](https://docs.stripe.com/payments/payment-methods.md) or confirming a `PaymentIntent`. At all times, you should be able to share this mandate—the accepted DDR and its accompanying DDR service agreement—with your customer, either in print or as a non-changeable electronic copy (such as email). Stripe hosts this for you under the `url` property of the `Mandate` object linked to the `PaymentMethod`.

### Add and configure an Australia Bank Account Element

The Australia Bank Account Element will help you collect and validate both the BSB number and the account number. It needs a place to live in your payment form. Create empty DOM nodes (containers) with unique IDs in your payment form. Additionally, your customer must read and accept the [Direct Debit Request service agreement](https://stripe.com/au-becs-dd-service-agreement/legal).

#### HTML

```html
<form action="/setup" method="post" id="setup-form">
  <div class="form-row inline">
    <div class="col">
      <label for="accountholder-name"> Name </label>
      <input
        id="accountholder-name"
        name="accountholder-name"
        placeholder="John Smith"
        required
      />
    </div>
    <div class="col">
      <label for="email"> Email Address </label>
      <input
        id="email"
        name="email"
        type="email"
        placeholder="john.smith@example.com"
        required
      />
    </div>
  </div>

  <div class="form-row">
    <!--
    Using a label with a for attribute that matches the ID of the
    Element container enables the Element to automatically gain focus
    when the customer clicks on the label.
    --><label for="au-bank-account-element"> Bank Account </label>
    <div id="au-bank-account-element">
      <!-- A Stripe Element will be inserted here. -->
    </div>
  </div>

  <!-- Used to display bank (branch) name associated with the entered BSB -->
  <div id="bank-name"></div>

  <!-- Used to display form errors. -->
  <div id="error-message" role="alert"></div>

  <!-- Display mandate acceptance text. -->
  <div class="col" id="mandate-acceptance">
    By providing your bank account details, you agree to this Direct Debit
    Request and the
    <a href="stripe.com/au-becs-dd-service-agreement/legal"
      >Direct Debit Request service agreement</a
    >, and authorise Stripe Payments Australia Pty Ltd ACN 160 180 343 Direct
    Debit User ID number 507156 (“Stripe”) to debit your account through the
    Bulk Electronic Clearing System (BECS) on behalf ofRocket Rides(the
    "Merchant") for any amounts separately communicated to you by the Merchant.
    You certify that you are either an account holder or an authorised signatory
    on the account listed above.
  </div>

  <!-- Add the client_secret from the SetupIntent as a data attribute -->
  <button id="submit-button" data-secret="{{CLIENT_SECRET}}">
    Set up BECS Direct Debit
  </button>
</form>
```

When the form loads, you can [create an instance](https://docs.stripe.com/js/elements_object/create_element?type=au_bank_account) of the Australia Bank Account Element and mount it to the Element container:

```javascript
// Custom styling can be passed to options when creating an Element
const style = {
  base: {
    color: "#32325d",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
    ":-webkit-autofill": {
      color: "#32325d",
    },
  },
  invalid: {
    color: "#fa755a",
    iconColor: "#fa755a",
    ":-webkit-autofill": {
      color: "#fa755a",
    },
  },
};

const options = {
  style: style,
  disabled: false,
  hideIcon: false,
  iconStyle: "default", // or "solid"
};

// Create an instance of the auBankAccount Element.
const auBankAccount = elements.create("auBankAccount", options);

// Add an instance of the auBankAccount Element into
// the `au-bank-account-element` <div>.
auBankAccount.mount("#au-bank-account-element");
```

#### React

#### npm

Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

#### umd

We also provide a UMD build for sites that don’t use npm or modules.

Include the Stripe.js script, which exports a global `Stripe` function, and the UMD build of React Stripe.js, which exports a global `ReactStripe` object. Always load the Stripe.js script directly from **js.stripe.com** to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<!-- Stripe.js -->
<script src="https://js.stripe.com/dahlia/stripe.js"></script>

<!-- React Stripe.js development build -->
<script src="https://unpkg.com/@stripe/react-stripe-js@latest/dist/react-stripe.umd.js"></script>

<!-- When you are ready to deploy your site to production, remove the
      above development script, and include the following production build. -->
<script src="https://unpkg.com/@stripe/react-stripe-js@latest/dist/react-stripe.umd.min.js"></script>
```

> The [demo in CodeSandbox](https://codesandbox.io/s/react-stripe-official-q1loc?fontsize=14&hidenavigation=1&theme=dark) lets you try out React Stripe.js without having to create a new project.

### Add Stripe.js and Elements to your page

To use Element components, wrap your checkout page component in an [Elements provider](https://docs.stripe.com/sdks/stripejs-react.md#elements-provider). Call `loadStripe` with your publishable key and pass the returned `Promise` to the `Elements` provider.

```jsx
import React from "react";
import ReactDOM from "react-dom";
import { Elements } from "@stripe/react-stripe-js";
import { loadStripe } from "@stripe/stripe-js";

import PaymentSetupForm from "./PaymentSetupForm";

// Make sure to call `loadStripe` outside of a component's render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe("<<YOUR_PUBLISHABLE_KEY>>");

function App() {
  return (
    <Elements stripe={stripePromise}>
      <PaymentSetupForm />
    </Elements>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

### Direct Debit Requests

Before you can create a BECS Direct Debit payment, your customer must agree with the Direct Debit Request Service Agreement. They do so by submitting a completed Direct Debit Request (DDR). The approval gives you a mandate to debit their account. The `Mandate` is a record of the permission to debit a payment method.

For online mandate acceptance, you can create a form to collect the necessary information. Serve the form over [HTTPS](https://docs.stripe.com/security/guide.md#tls) and capture the following information:

| Information        | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| **Account name**   | The full name of the account holder                                       |
| **BSB number**     | The Bank-State-Branch number of the bank account (for example, `123-456`) |
| **Account number** | The bank account number (for example, `87654321`)                         |

When collecting a Direct Debit Request, follow our [BECS Direct Debit Terms](https://stripe.com/au-becs/legal) and as part of your checkout form:

- Display the exact terms of [Stripe’s DDR service agreement](https://stripe.com/au-becs-dd-service-agreement/legal) either inline on the form, or on a page linked from the form, and identifying it as the “DDR service agreement.”
- Make sure the accepted DDR and its accompanying [DDR service agreement](https://stripe.com/au-becs-dd-service-agreement/legal) can be shared with your customer at all times, either as a printed or non-changeable electronic copy (such as email). Stripe hosts this for you.
- Display the following standard authorization text for your customer to accept the BECS DDR, where you replace _Rocketship Inc_ with your company name. Their acceptance authorizes you to initiate BECS Direct Debit payments from their bank account.

> By providing your bank account details, you agree to this Direct Debit Request and the [Direct Debit Request service agreement](https://stripe.com/au-becs-dd-service-agreement/legal), and authorize Stripe Payments Australia Pty Ltd ACN 160&nbsp;180&nbsp;343 Direct Debit User ID number 507156 (“Stripe”) to debit your account through the Bulk Electronic Clearing System (BECS) on behalf of _Rocketship Inc_ (the “Merchant”) for payments as per the terms of your agreement with the Merchant. You certify that you’re either an account holder or an authorized signatory on the account listed above.

The details of the accepted mandate are generated when setting up a [PaymentMethod](https://docs.stripe.com/payments/payment-methods.md) or confirming a `PaymentIntent`. At all times, you should be able to share this mandate—the accepted DDR and its accompanying DDR service agreement—with your customer, either in print or as a non-changeable electronic copy (such as email). Stripe hosts this for you under the `url` property of the `Mandate` object linked to the `PaymentMethod`.

### Add and configure an AuBankAccountElement component

The `AuBankAccountElement` component will help you collect and validate both the BSB number and the account number. Additionally, your customer must read and accept the [Direct Debit Request service agreement](https://stripe.com/au-becs-dd-service-agreement/legal).

#### JSX

```jsx
/**
* Use the CSS tab above to style your Element's container.
*/
import React from 'react';
import {AuBankAccountElement} from '@stripe/react-stripe-js';
import './BecsFormStyles.css'

// Custom styling can be passed as options when creating an Element.
const AU_BANK_ACCOUNT_STYLE = {
  base: {
    color: '#32325d',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    },
    ':-webkit-autofill': {
      color: '#32325d',
    },
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a',
    ':-webkit-autofill': {
      color: '#fa755a',
    },
  }
};

const AU_BANK_ACCOUNT_ELEMENT_OPTIONS = {
  style: AU_BANK_ACCOUNT_STYLE,
  disabled: false,
  hideIcon: false,
  iconStyle: "default", // or "solid"
};

export default function BecsForm({onSubmit, disabled}) {
  return (
    <form onSubmit={onSubmit}>
      <div className="form-row inline">
        <div className="col">
          <label>
            Name
            <input
              name="accountholder-name"
              placeholder="John Smith"
              required
            />
          </label>
        </div>

        <div className="col">
          <label>
            Email Address
            <input
              name="email"
              type="email"
              placeholder="john.smith@example.com"
              required
            />
          </label>
        </div>
      </div>
<div className="form-row">
        <label>
          Bank Account
          <AuBankAccountElement options={AU_BANK_ACCOUNT_ELEMENT_OPTIONS} />
        </label>
      </div>

      {/* Display mandate acceptance text. */}<div className="mandate-acceptance">
        By providing your bank account details, you agree to this Direct Debit Request
        and the <a href="https://stripe.com/au-becs-dd-service-agreement/legal">Direct Debit Request service agreement</a>,
        and authorise Stripe Payments Australia Pty Ltd ACN 160 180 343
        Direct Debit User ID number 507156 (“Stripe”) to debit your account
        through the Bulk Electronic Clearing System (BECS) on behalf ofRocket Rides(the "Merchant") for any amounts separately
        communicated to you by the Merchant. You certify that you are either
        an account holder or an authorised signatory on the account listed above.
      </div>

      <button type="submit" disabled={disabled}>Confirm Payment</button>
    </form>
```

Elements are completely customizable. You can [style Elements](https://docs.stripe.com/js/elements_object/create_element?type=au_bank_account#elements_create-options) to match the look and feel of your site, providing a seamless checkout experience for your customers. It’s also possible to style various input states, for example when the Element has focus.

## Submit the payment method details to Stripe [Client-side]

Rather than sending the entire `SetupIntent` object to the client, use its [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) from [step 2](https://docs.stripe.com/billing/subscriptions/au-becs-debit.md#web-create-setup-intent). This is different from your API keys that authenticate Stripe API requests.

The client secret should be handled carefully because it can complete the setup. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

#### HTML + JS

Use [stripe.confirmAuBecsDebitSetup](https://docs.stripe.com/js/setup_intents/confirm_au_becs_debit_setup) to complete the setup when the user submits the form. A successful setup returns a `succeeded` value for the SetupIntent’s `status` property. If the setup isn’t successful, inspect the returned `error` to determine the cause.

```javascript
const form = document.getElementById("setup-form");
const accountholderName = document.getElementById("accountholder-name");
const email = document.getElementById("email");
const submitButton = document.getElementById("submit-button");
const clientSecret = submitButton.dataset.secret;

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  stripe.confirmAuBecsDebitSetup(clientSecret, {
    payment_method: {
      au_becs_debit: auBankAccount,
      billing_details: {
        name: accountholderName.value,
        email: email.value,
      },
    },
  });
});
```

After successfully confirming the `SetupIntent`, you should share the [mandate URL](https://docs.stripe.com/api/mandates/object.md#mandate_object-payment_method_details-au_becs_debit-url) from the [Mandate object](https://docs.stripe.com/api/mandates.md) with your customer. We also recommend including the following details to your customer when you confirm their mandate has been established:

- an explicit confirmation message that indicates a Direct Debit arrangement has been set up
- the [business name](https://docs.stripe.com/billing/subscriptions/au-becs-debit.md#statement-descriptors) that will appear on the customer’s bank statement whenever their account gets debited
- the payment amount and schedule (if applicable)
- a link to the generated DDR mandate URL

The `Mandate` object’s ID is accessible from the `mandate` on the SetupIntent object, which is sent as part of the `setup_intent.succeeded` event sent after confirmation, but can also be [retrieved through the API](https://docs.stripe.com/api/setup_intents/retrieve.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve("{{SETUP_INTENT_ID}}", {
  expand: ["mandate"],
});
```

#### React

Use [stripe.confirmAuBecsDebitSetup](https://docs.stripe.com/js/setup_intents/confirm_au_becs_debit_setup) to complete the mandate collection when the user submits the form. Including the customer’s email address and the account holder’s name in the `billing_details` property of the `payment_method` parameter is required to create a BECS Direct Debit `PaymentMethod`.

To call `stripe.confirmAuBecsDebitSetup` from your payment form component, use the [useStripe](https://docs.stripe.com/sdks/stripejs-react.md#usestripe-hook) and [useElements](https://docs.stripe.com/sdks/stripejs-react.md#useelements-hook) hooks. If you prefer traditional class components over hooks, you can instead use an [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer).

#### Hooks

```jsx
import React from "react";
import {
  useStripe,
  useElements,
  AuBankAccountElement,
} from "@stripe/react-stripe-js";

import BecsForm from "./BecsForm";

export default function PaymentSetupForm() {
  const stripe = useStripe();
  const elements = useElements();

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    const auBankAccount = elements.getElement(AuBankAccountElement);

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name and email. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const accountholderName = event.target["accountholder-name"];
    const email = event.target.email;

    const result = await stripe.confirmAuBecsDebitSetup("{{CLIENT_SECRET}}", {
      payment_method: {
        au_becs_debit: auBankAccount,
        billing_details: {
          name: accountholderName.value,
          email: email.value,
        },
      },
    });

    if (result.error) {
      // Show error to your customer.
      console.log(result.error.message);
    } else {
      // Show a confirmation message to your customer.
      // The SetupIntent is in the 'succeeded' state.
    }
  };

  return <BecsForm onSubmit={handleSubmit} disabled={!stripe} />;
}
```

#### Class Components

```jsx
import React from "react";
import {
  ElementsConsumer,
  AuBankAccountElement,
} from "@stripe/react-stripe-js";

import BecsForm from "./BecsForm";

class PaymentSetupForm extends React.Component {
  handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    const { stripe, elements } = this.props;

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    const auBankAccount = elements.getElement(AuBankAccountElement);

    // For brevity, this example is using uncontrolled components for
    // the accountholder's name and email. In a real world app you will
    // probably want to use controlled components.
    // https://reactjs.org/docs/uncontrolled-components.html
    // https://reactjs.org/docs/forms.html#controlled-components

    const accountholderName = event.target["accountholder-name"];
    const email = event.target.email;

    const result = await stripe.confirmAuBecsDebitSetup("{{CLIENT_SECRET}}", {
      payment_method: {
        au_becs_debit: auBankAccount,
        billing_details: {
          name: accountholderName.value,
          email: email.value,
        },
      },
    });

    if (result.error) {
      // Show error to your customer.
      console.log(result.error.message);
    } else {
      // Show a confirmation message to your customer.
      // The SetupIntent is in the 'succeeded' state.
    }
  };

  render() {
    const { stripe } = this.props;
    return <BecsForm onSubmit={this.handleSubmit} disabled={!stripe} />;
  }
}

export default function InjectedPaymentSetupForm() {
  return (
    <ElementsConsumer>
      {({ stripe, elements }) => (
        <PaymentSetupForm stripe={stripe} elements={elements} />
      )}
    </ElementsConsumer>
  );
}
```

After successfully confirming the `SetupIntent`, you should share the [mandate URL](https://docs.stripe.com/api/mandates/object.md#mandate_object-payment_method_details-au_becs_debit-url) from the [Mandate object](https://docs.stripe.com/api/mandates.md) with your customer. We also recommend including the following details to your customer when you confirm their mandate has been established:

- an explicit confirmation message that indicates a Direct Debit arrangement has been set up
- the [business name](https://docs.stripe.com/billing/subscriptions/au-becs-debit.md#statement-descriptors) that will appear on the customer’s bank statement whenever their account gets debited
- the payment amount and schedule (if applicable)
- a link to the generated DDR mandate URL

The `Mandate` object’s ID is accessible from the `mandate` on the SetupIntent object, which is sent as part of the `setup_intent.succeeded` event sent after confirmation, but can also be [retrieved through the API](https://docs.stripe.com/api/setup_intents/retrieve.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const setupIntent = await stripe.setupIntents.retrieve("{{SETUP_INTENT_ID}}", {
  expand: ["mandate"],
});
```

## Create a customer with a PaymentMethod [Server-side]

Creating subscriptions requires an object that represents the customer, which can be either a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md) or a [Customer](https://docs.stripe.com/api.md#customer_object). Because the subscription charges recurring payments, you need to add a stored payment method to the customer to use for future payments.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

#### Accounts v2

[Create a customer-configured Account](https://docs.stripe.com/api/v2/core/accounts/create.md), then update it to set the payment method you just collected as its [configuration.customer.billing.default_payment_method](https://docs.stripe.com/api/v2/core/accounts/update.md#v2_update_accounts-configuration-customer-billing-default_payment_method). This makes the payment method the default for invoices and subscriptions.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const account = await stripe.v2.core.accounts.update("acct_Gk0uVzT2M4xOKD", {
  configuration: {
    customer: {
      billing: {
        default_payment_method: "pm_1FU2bgBF6ERF9jhEQvwnA7sX",
      },
    },
  },
});
```

#### Customers v1

Create a `Customer` object and set the payment method you just collected as both the [payment_method](https://docs.stripe.com/api/customers/create.md#create_customer-payment_method) and the [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/create.md#create_customer-invoice_settings-default_payment_method):

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const customer = await stripe.customers.create({
  email: "jenny.rosen@example.com",
  payment_method: "pm_1FU2bgBF6ERF9jhEQvwnA7sX",
  invoice_settings: {
    default_payment_method: "pm_1FU2bgBF6ERF9jhEQvwnA7sX",
  },
});
```

This returns a `Customer` object. You can see the default payment method in the `invoice_settings`:

```json
{
  "id": "cus_Gk0uVzT2M4xOKD",
  "object": "customer",
  "address": null,
  "balance": 0,
  "created": 1581797088,
  "currency": null,
  "default_source": null,
  "delinquent": false,
  "description": null,
  "discount": null,
  "email": "jenny.rosen@example.com",
  "invoice_prefix": "11D0B3D7",
  "invoice_settings": {
    "custom_fields": null,
    "default_payment_method": "pm_1FU2bgBF6ERF9jhEQvwnA7sX",
    "footer": null
  },
  "livemode": false,
  "metadata": {},
  "name": null,
  "phone": null,
  "preferred_locales": [],
  "shipping": null,
  "sources": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/customers/cus_Gk0uVzT2M4xOKD/sources"
  },
  "subscriptions": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/customers/cus_Gk0uVzT2M4xOKD/subscriptions"
  },
  "tax_exempt": "none",
  "tax_ids": {
    "object": "list",
    "data": [],
    "has_more": false,
    "total_count": 0,
    "url": "/v1/customers/cus_Gk0uVzT2M4xOKD/tax_ids"
  }
}
```

After creating the customer, store its ID in your own database so you can use it later.

## Create the subscription [Server-side]

Create a [subscription](https://docs.stripe.com/api/subscriptions.md) with the price and customer:

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "price_F52b2UdntfQsfR",
    },
  ],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "cus_Gk0uVzT2M4xOKD",
  items: [
    {
      price: "price_F52b2UdntfQsfR",
    },
  ],
});
```

Creating subscriptions automatically charges customers using the default payment method. After the first successful payment, the subscription status [in the Dashboard](https://dashboard.stripe.com/test/subscriptions) changes to **Active**. Subsequent charges use the price you created earlier.

## Manage subscription status [Client-side]

When the initial payment succeeds, the status of the _subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) is `active` and no further action is needed. When payments fail, the status is changed to the **Subscription status** configured in your [automatic collection settings](https://docs.stripe.com/invoicing/automatic-collection.md). Notify the customer after a failure and [charge them with a different payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

> BECS Direct Debit payments are never automatically retried, even if you have a [retry schedule](https://docs.stripe.com/invoicing/automatic-collection.md) configured for other payment methods.

## Test the integration

You can test your form using the test BSB number `000000` and one of the test account numbers below with your [confirmAuBecsDebitSetup](https://docs.stripe.com/js/setup_intents/confirm_au_becs_debit_setup) request, or use the corresponding token to skip manually entering bank account details.

| BSB Number | Account number | Token                                    | Description                                                                                                                                                                                                                     |
| ---------- | -------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `000000`   | `000123456`    | `pm_auBecsDebit_success`                 | The PaymentIntent created with the resulting PaymentMethod transitions from `processing` to `succeeded`. The mandate status remains `active`.                                                                                   |
| `000000`   | `900123456`    | `pm_auBecsDebit_successDelayed`          | The PaymentIntent created with the resulting PaymentMethod transitions from `processing` to `succeeded` (with a three-minute delay). The mandate status remains `active`.                                                       |
| `000000`   | `111111113`    | `pm_auBecsDebit_accountClosed`           | The PaymentIntent created with the resulting PaymentMethod transitions from `processing` to `requires_payment_method` with an `account_closed` failure code. The mandate status becomes `inactive` at that point.               |
| `000000`   | `111111116`    | `pm_auBecsDebit_noAccount`               | The PaymentIntent created with the resulting PaymentMethod transitions from `processing` to `requires_payment_method` with a `no_account` failure code. The mandate status becomes `inactive` at that point.                    |
| `000000`   | `222222227`    | `pm_auBecsDebit_referToCustomer`         | The PaymentIntent created with the resulting PaymentMethod transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code. The mandate status remains `active`.                             |
| `000000`   | `922222227`    | `pm_auBecsDebit_referToCustomerDelayed`  | The PaymentIntent created with the resulting PaymentMethod transitions from `processing` to `requires_payment_method` with a `refer_to_customer` failure code (with a three-minute delay). The mandate status remains `active`. |
| `000000`   | `333333335`    | `pm_auBecsDebit_debitNotAuthorized`      | The PaymentIntent created with the resulting PaymentMethod transitions from `processing` to `requires_payment_method` with a `debit_not_authorized` failure code. The mandate status becomes `inactive` at that point.          |
| `000000`   | `666666660`    | `pm_auBecsDebit_dispute`                 | The PaymentIntent created with the resulting PaymentMethod transitions from `processing` to `succeeded`, but a dispute is immediately created.                                                                                  |
| `000000`   | `343434343`    | `pm_auBecsDebit_exceedsWeeklyLimit`      | The PaymentIntent that was created with the resulting PaymentMethod fails with a `charge_exceeds_source_limit` error due to the payment amount causing the account to exceed its weekly payment volume limit.                   |
| `000000`   | `121212121`    | `pm_auBecsDebit_exceedsTransactionLimit` | The PaymentIntent that was created with the resulting PaymentMethod fails with a `charge_exceeds_transaction_limit` error due to the payment amount exceeding the account’s transaction volume limit.                           |

## Optional: Set the billing period

When you create a subscription, it automatically sets the billing cycle by default. For example, if a customer subscribes to a monthly plan on September 7, they’re billed on the 7th of every month after that. Some businesses prefer to set the billing cycle manually so that they can charge their customers at the same time each cycle. The [billing cycle anchor](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_cycle_anchor) argument allows you to do this.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  billing_cycle_anchor: 1611008505,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  billing_cycle_anchor: 1611008505,
});
```

Setting the billing cycle manually automatically charges the customer a prorated amount for the time between the subscription being created and the billing cycle anchor. If you don’t want to charge customers for this time, you can set the [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) argument to `none`. You can also combine the billing cycle anchor with [trial periods](https://docs.stripe.com/billing/subscriptions/au-becs-debit.md#trial-periods) to give users free access to your product and then charge them a prorated amount.

## Optional: Subscription trials

Free trials allow customers access to your product for a period of time for free. Using free trials is different from setting [proration_behavior](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-proration_behavior) to `none` because you can customize how long the free period lasts. Pass a timestamp in [trial end](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-trial_end) to set the trial period.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  trial_end: 1610403705,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const subscription = await stripe.subscriptions.create({
  customer: "{{CUSTOMER_ID}}",
  items: [
    {
      price: "{{PRICE_ID}}",
    },
  ],
  trial_end: 1610403705,
});
```

You can also combine a [billing cycle anchor](https://docs.stripe.com/billing/subscriptions/au-becs-debit.md#billing-cycle) with a free trial. For example, say it’s September 15 and you want to give your customer a free trial for seven days and then start the normal billing cycle on October 1. You can set the free trial to end on September 22 and the billing cycle anchor to October 1. This gives the customer a free trial for seven days and then charges a prorated amount for the time between the trial ending and October 1. On October 1, you charge them the normal subscription amount for their first full billing cycle.
