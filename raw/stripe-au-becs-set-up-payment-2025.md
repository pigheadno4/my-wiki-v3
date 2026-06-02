<!-- Source URL: https://docs.stripe.com/payments/au-becs-debit/set-up-payment -->
<!-- Fetched: 2026-05-02 -->

# Save Australia BECS Direct Debit details for future payments

Use the Setup Intents API to save payment method details for future Australia BECS Direct Debit payments.

# Elements

> This is a Elements for when payment-ui is elements. View the full page at https://docs.stripe.com/payments/au-becs-debit/set-up-payment?payment-ui=elements.

Use [Stripe Elements](https://docs.stripe.com/payments/elements.md), our prebuilt UI components, to create a payment form that lets you securely collect bank details without handling the sensitive data. You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect BECS Direct Debit payment method details in advance, and determine the final amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

## Set up Stripe [Server-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

## Create or retrieve a customer [Server-side]

To reuse a BECS Direct Debit account for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {},
  },
  include: ['configuration.customer'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jenny.rosen@example.com',
});
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` will track the steps of this set-up process. For BECS Direct Debit, this includes collecting a mandate from the customer and tracking its validity throughout its lifecycle.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server. Add `au_becs_debit` to the [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) array and specify the ID of the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id) object:

#### Accounts v2

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['au_becs_debit'],
  customer_account: customer_account.id,
});
const clientSecret = setupIntent.client_secret;
// Pass the client secret to the client
```

#### Customers v1

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['au_becs_debit'],
  customer: customer.id,
});
const clientSecret = setupIntent.client_secret;
// Pass the client secret to the client
```

After creating a `SetupIntent` on your server, you can associate the `SetupIntent` ID with the current session’s customer in your application’s data model. Doing so allows you to retrieve the information after you’ve successfully collected a payment method.

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
const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
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
- Display the following standard authorization text for your customer to accept the BECS DDR, where you replace *Rocketship Inc* with your company name. Their acceptance authorizes you to initiate BECS Direct Debit payments from their bank account.

> By providing your bank account details, you agree to this Direct Debit Request and the [Direct Debit Request service agreement](https://stripe.com/au-becs-dd-service-agreement/legal), and authorize Stripe Payments Australia Pty Ltd ACN 160&nbsp;180&nbsp;343 Direct Debit User ID number 507156 (“Stripe”) to debit your account through the Bulk Electronic Clearing System (BECS) on behalf of *Rocketship Inc* (the “Merchant”) for payments as per the terms of your agreement with the Merchant. You certify that you’re either an account holder or an authorized signatory on the account listed above.

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
  iconStyle: 'default', // or "solid"
};

// Create an instance of the auBankAccount Element.
const auBankAccount = elements.create('auBankAccount', options);

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
const stripePromise = loadStripe('<<YOUR_PUBLISHABLE_KEY>>');

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
- Display the following standard authorization text for your customer to accept the BECS DDR, where you replace *Rocketship Inc* with your company name. Their acceptance authorizes you to initiate BECS Direct Debit payments from their bank account.

> By providing your bank account details, you agree to this Direct Debit Request and the [Direct Debit Request service agreement](https://stripe.com/au-becs-dd-service-agreement/legal), and authorize Stripe Payments Australia Pty Ltd ACN 160&nbsp;180&nbsp;343 Direct Debit User ID number 507156 (“Stripe”) to debit your account through the Bulk Electronic Clearing System (BECS) on behalf of *Rocketship Inc* (the “Merchant”) for payments as per the terms of your agreement with the Merchant. You certify that you’re either an account holder or an authorized signatory on the account listed above.

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
  iconStyle: 'default', // or "solid"
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

Rather than sending the entire `SetupIntent` object to the client, use its [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) from [step 2](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md#web-create-setup-intent). This is different from your API keys that authenticate Stripe API requests.

The client secret should be handled carefully because it can complete the setup. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

#### HTML + JS

Use [stripe.confirmAuBecsDebitSetup](https://docs.stripe.com/js/setup_intents/confirm_au_becs_debit_setup) to complete the setup when the user submits the form. A successful setup returns a `succeeded` value for the SetupIntent’s `status` property. If the setup isn’t successful, inspect the returned `error` to determine the cause.

As [customer](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer) was set, the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) is attached to the provided `Customer` object after a successful setup. At this point, you can associate the ID of the `Customer` object with your internal representation of a customer. This allows you to use the stored `PaymentMethod` to collect future payments without prompting for your customer’s payment method details.

```javascript
const form = document.getElementById('setup-form');
const accountholderName = document.getElementById('accountholder-name');
const email = document.getElementById('email');
const submitButton = document.getElementById('submit-button');
const clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', async (event) => {
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
- the [business name](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md#statement-descriptors) that will appear on the customer’s bank statement whenever their account gets debited
- the payment amount and schedule (if applicable)
- a link to the generated DDR mandate URL

The `Mandate` object’s ID is accessible from the `mandate` on the SetupIntent object, which is sent as part of the `setup_intent.succeeded` event sent after confirmation, but can also be [retrieved through the API](https://docs.stripe.com/api/setup_intents/retrieve.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

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
- the [business name](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md#statement-descriptors) that will appear on the customer’s bank statement whenever their account gets debited
- the payment amount and schedule (if applicable)
- a link to the generated DDR mandate URL

The `Mandate` object’s ID is accessible from the `mandate` on the SetupIntent object, which is sent as part of the `setup_intent.succeeded` event sent after confirmation, but can also be [retrieved through the API](https://docs.stripe.com/api/setup_intents/retrieve.md).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.retrieve("{{SETUP_INTENT_ID}}", {
  expand: ["mandate"],
});
```

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

## Optional: Validate the Australia Bank Account Element [Client-side]

The Australia Bank Account Element validates user input as it’s typed. To help your customers fix mistakes, you should listen to change events on the Australia Bank Account Element and display any errors:

#### HTML + JS

```javascript
auBankAccount.on('change', (event) => {
  const displayError = document.getElementById('error-message');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = "";
  }
});
```

#### React

```jsx
<AuBankAccountElement onChange={(event) => {
  if (event.error) {
    // Store event.error.message in state and display it.
  } else {
    // Remove existing error from state.
  }
}}>
```

The change event contains other parameters that can help to build a richer user experience. Refer to the [Stripe.js reference](https://docs.stripe.com/js/element/events/on_change?type=auBankAccountElement#element_on_change-handler) for more details.

## Optional: Accepting future payments [Client-side]

When the SetupIntent succeeds, it will create a new *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) and a [Mandate object](https://docs.stripe.com/api/mandates.md). These can be used to initiate future payments without having to prompt the customer for information information.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'aud',
  payment_method_types: ['au_becs_debit'],
  customer_account: "{{CUSTOMERACCOUNT_ID}}",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  confirm: true,
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'aud',
  payment_method_types: ['au_becs_debit'],
  customer: "{{CUSTOMER_ID}}",
  payment_method: "{{PAYMENTMETHOD_ID}}",
  confirm: true,
});
```

# iOS

> This is a iOS for when payment-ui is mobile and platform is ios. View the full page at https://docs.stripe.com/payments/au-becs-debit/set-up-payment?payment-ui=mobile&platform=ios.

Use STPAUBECSFormView, Stripe’s prebuilt BECS payment details collection UI, to create a payment form that lets you securely collect bank details without handling sensitive customer data. You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect BECS Direct Debit payment method details in advance, and determine the final amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source, [fully documented](https://stripe.dev/stripe-ios/index.html), and compatible with apps supporting iOS 13 or above.

#### Swift Package Manager

To install the SDK, follow these steps:

1. In Xcode, select **File** > **Add Package Dependencies…** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL.
1. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases).
1. Add the **StripePaymentsUI** product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:
   ```bash
   pod init
   ```
1. Add this line to your `Podfile`:
   ```podfile
   pod 'StripePaymentsUI'
   ```
1. Run the following command:
   ```bash
   pod install
   ```
1. Don’t forget to use the `.xcworkspace` file to open your project in Xcode, instead of the `.xcodeproj` file, from here on out.
1. In the future, to update to the latest version of the SDK, run:
   ```bash
   pod update StripePaymentsUI
   ```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:
   ```cartfile
   github "stripe/stripe-ios"
   ```
1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure to embed all of the required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of the SDK, run the following command:
   ```bash
   carthage update stripe-ios --platform ios
   ```

#### Manual Framework

1. Head to our [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip **Stripe.xcframework.zip**.
1. Drag **StripePaymentsUI.xcframework** to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure to select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/tree/master/StripePaymentsUI/README.md#manual-linking).
1. In the future, to update to the latest version of our SDK, repeat steps 1–3.

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-ios/releases) page on GitHub. To receive notifications when a new release is published, [watch releases](https://help.github.com/en/articles/watching-and-unwatching-releases-for-a-repository#watching-releases-for-a-repository) for the repository.

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/test/apikeys) on app start. This enables your app to make requests to the Stripe API.

#### Swift

```swift
import UIKitimportStripePaymentsUI

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {StripeAPI.defaultPublishableKey = "<<YOUR_PUBLISHABLE_KEY>>"
        // do any other necessary launch configuration
        return true
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create or retrieve a customer [Server-side]

To reuse a BECS Direct Debit account for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {},
  },
  include: ['configuration.customer'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jenny.rosen@example.com',
});
```

## Collect payment method details and mandate acknowledgment [Client-side]

You can securely collect BECS Debit payment information with [STPAUBECSFormView](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPAUBECSDebitFormView.html), a drop-in UI component provided by the SDK. `STPAUBECSFormView​` provides a UI for customers to enter their name, email, BSB number, and account number—in addition to displaying the [BECS Direct Debit Terms](https://stripe.com/au-becs/legal).

Create an instance of `STPAUBECSFormView​` configured with your company name and set up a delegate for the SDK to notify after the customer enters the required details to create an instance of `STPPaymentMethodParams`​. You can also customize `STPAUBECSFormView​` to match the look and feel of your app by providing values to `STPAUBECSFormView​'s` public properties.

#### Swift

```swift
import UIKit
import StripePaymentsUI

class CheckoutViewController: UIViewController {

    private var becsFormView = STPAUBECSDebitFormView(companyName: "Example Company Inc.")
    private let saveButton = UIButton()

    private var setupIntentClientSecret: String?

    override func viewDidLoad() {
        super.viewDidLoad()

        view.backgroundColor = .secondarySystemBackground

        saveButton.layer.cornerRadius = 5
        saveButton.contentEdgeInsets = UIEdgeInsets(top: 4, left: 8, bottom: 4, right: 8)
        saveButton.backgroundColor = .systemGray3
        saveButton.titleLabel?.font = UIFont.systemFont(ofSize: 18)
        saveButton.setTitle("Save", for: .normal)
        saveButton.addTarget(self, action: #selector(save), for: .touchUpInside)
        saveButton.isEnabled = false
        saveButton.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(saveButton)

        becsFormView.becsDebitFormDelegate = self
        becsFormView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(becsFormView)

        NSLayoutConstraint.activate([
                   becsFormView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
                   view.trailingAnchor.constraint(equalTo: becsFormView.trailingAnchor),

                   becsFormView.topAnchor.constraint(equalToSystemSpacingBelow: view.safeAreaLayoutGuide.topAnchor, multiplier: 2),

                   saveButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
                   saveButton.topAnchor.constraint(equalToSystemSpacingBelow: becsFormView.bottomAnchor, multiplier: 2),
               ])
    }

    @objc
    func save() {
        // ...
    }

}

extension CheckoutViewController: STPAUBECSDebitFormViewDelegate {
    func auBECSDebitForm(_ form: STPAUBECSDebitFormView, didChangeToStateComplete complete: Bool) {
        saveButton.isEnabled = complete
        saveButton.backgroundColor = complete ? .systemBlue : .systemGray3
    }
}
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` will track the steps of this set-up process. For BECS Direct Debit, this includes collecting a mandate from the customer and tracking its validity throughout its lifecycle.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server. Add `au_becs_debit` to the [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) array and specify the ID of the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id) object:

#### Accounts v2

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['au_becs_debit'],
  customer_account: customer_account.id,
});
const clientSecret = setupIntent.client_secret;
// Pass the client secret to the client
```

#### Customers v1

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['au_becs_debit'],
  customer: customer.id,
});
const clientSecret = setupIntent.client_secret;
// Pass the client secret to the client
```

After creating a `SetupIntent` on your server, you can associate the `SetupIntent` ID with the current session’s customer in your application’s data model. Doing so allows you to retrieve the information after you’ve successfully collected a payment method.

The returned `SetupIntent` object contains a `client_secret` property. Pass the client secret to the client-side application to continue with the setup process.

## Submit the payment method details to Stripe [Client-side]

After the user enters their payment details, confirm the `SetupIntent` to complete saving the debit information.

First, assemble a STPSetupIntentConfirmParams object with:

1. The [STPAUBECSFormView’s](https://stripe.dev/stripe-ios/stripe-payments-ui/Classes/STPAUBECSDebitFormView.html) `paymentMethodParams` property
1. The `SetupIntent` client secret from your server

Rather than sending the entire `SetupIntent` object to the client, use its [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) from [step 4](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md#ios-create-setup-intent). This is different from your API keys that authenticate Stripe API requests.

The client secret should still be handled carefully because it can complete the setup. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Next, complete the payment by calling the [STPPaymentHandler confirmSetupIntent](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:objc(cs)STPPaymentHandler(im)confirmSetupIntent:withAuthenticationContext:completion:>) method.

Because [customer](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer) was set, the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) will be attached to the provided *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object after a successful setup. This allows you to use the stored PaymentMethod to collect future payments without prompting the customer for payment method details.

#### Swift

```swift
import UIKit
import StripePaymentsUI

class CheckoutViewController: UIViewController {
    // ...
    @objc
    func save() {
        guard let setupIntentClientSecret = setupIntentClientSecret,
            let paymentMethodParams = becsFormView.paymentMethodParams else {
                return;
        }

        let setupIntentParams = STPSetupIntentConfirmParams(clientSecret: setupIntentClientSecret)
        setupIntentParams.paymentMethodParams = paymentMethodParams

        STPPaymentHandler.shared().confirmSetupIntent(withParams: setupIntentParams,
                                                      authenticationContext: self) { (handlerStatus, setupIntent, error) in
                                                        switch (handlerStatus) {
                                                        case .failed:
                                                            // Setup failed
                                                            break
                                                        case .canceled:
                                                            // Setup canceled
                                                            break
                                                        case .succeeded:
                                                            // Setup succeeded
                                                            break
                                                        @unknown default:
                                                            fatalError()
                                                            break
                                                        }
        }
    }
}

extension CheckoutViewController: STPAuthenticationContext {
    func authenticationPresentingViewController() -> UIViewController {
        return self
    }
}
```

After confirming the `SetupIntent`​, share the [mandate URL](https://docs.stripe.com/api/mandates/object.md#mandate_object-payment_method_details-au_becs_debit-url) from the [Mandate object](https://docs.stripe.com/api/mandates.md) with your customer. We also recommend including the following details when you confirm their mandate has been established:

- An explicit confirmation message that indicates a Direct Debit arrangement has been set up
- The [business name](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment.md) that will appear on the customer’s bank statement whenever their account gets debited
- The payment amount and schedule (if applicable)
- A link to the generated DDR mandate URL

​​You can access the `Mandate​` object’s ID from the `mandate` on the [SetupIntent object](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-mandate) (included with the `setup_intent.succeeded` event sent after confirmation) or you can [retrieve it through the API](https://docs.stripe.com/api/setup_intents/retrieve.md).

## Test the integration

You can test your form using the test BSB number `000000` and one of the test account numbers below with your [STPPaymentHandler confirmSetupIntent](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:objc(cs)STPPaymentHandler(im)confirmSetupIntent:withAuthenticationContext:completion:>) method call.

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

# Android

> This is a Android for when payment-ui is mobile and platform is android. View the full page at https://docs.stripe.com/payments/au-becs-debit/set-up-payment?payment-ui=mobile&platform=android.

Use [BecsDebitWidget](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/index.html), Stripe’s prebuilt BECS payment details collection UI, to create a payment form that lets you securely collect bank details without handling sensitive customer data. You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect BECS Direct Debit payment method details in advance, and determine the final amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

## Set up Stripe [Server-side] [Client-side]

First, you need a Stripe account. [Register now](https://dashboard.stripe.com/register).

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use the official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/).

To install the SDK, add `stripe-android` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

#### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
  // ...

  // Stripe Android SDK
  implementation("com.stripe:stripe-android:23.5.0")
  // Include the financial connections SDK to support US bank account as a payment method
  implementation("com.stripe:financial-connections:23.5.0")
}
```

> For details on the latest SDK release and past versions, see the [Releases](https://github.com/stripe/stripe-android/releases) page on GitHub. To receive notifications when a new release is published, [watch releases for the repository](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository).

Configure the SDK with your Stripe [publishable key](https://dashboard.stripe.com/apikeys) so that it can make requests to the Stripe API, such as in your `Application` subclass:

#### Kotlin

```kotlin
import com.stripe.android.PaymentConfiguration

class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        PaymentConfiguration.init(
            applicationContext,
            "<<YOUR_PUBLISHABLE_KEY>>"
        )
    }
}
```

> Use your [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

Stripe samples also use [OkHttp](https://github.com/square/okhttp) and [GSON](https://github.com/google/gson) to make HTTP requests to a server.

## Create or retrieve a customer [Server-side]

To reuse a BECS Direct Debit account for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {},
  },
  include: ['configuration.customer'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jenny.rosen@example.com',
});
```

## Collect payment method details and mandate acknowledgment [Client-side]

You can securely collect BECS Debit payment information with [BecsDebitWidget](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/index.html), a drop-in UI component provided by the SDK. `BecsDebitWidget` provides a UI for customers to enter their name, email, BSB number, and account number. It also displays the [BECS Direct Debit Terms](https://stripe.com/au-becs/legal).

### Add BecsDebitWidget to your layout

Add `BecsDebitWidget` to your layout and configure the `app:companyName` attribute with your company name.

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <LinearLayout
      xmlns:android="http://schemas.android.com/apk/res/android"
      xmlns:app="http://schemas.android.com/apk/res-auto"
      android:layout_width="match_parent"
      android:layout_height="match_parent"
      android:orientation="vertical">

      <!-- app:companyName is a required attribute -->
      <com.stripe.android.view.BecsDebitWidget
          android:id="@+id/becs_debit_widget"
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          app:companyName="@string/company_name" />

      <Button
          android:id="@+id/save_button"
          android:layout_width="300dp"
          android:layout_height="wrap_content"
          android:layout_gravity="center_horizontal"
          android:enabled="false"
          android:text="@string/save_with_becs_debit" />

  </LinearLayout>
```

#### Style the BecsDebitWidget

The `BecsDebitWidget` can be further customized by adding the following styles to your application’s `styles.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>

<!-- Optionally customize the widget's EditText fields -->
<style name="Stripe.BecsDebitWidget.EditText"
    parent="Stripe.Base.BecsDebitWidget.EditText">
    <!-- Add custom styles here -->
</style>

<!-- Optionally customize the mandate -->
<style name="Stripe.BecsDebitWidget.MandateAcceptanceTextView"
    parent="Stripe.Base.BecsDebitWidget.MandateAcceptanceTextView">
    <!-- Add custom styles here -->
</style>

```

### Configure your Activity

Set a [BecsDebitWidget.ValidParamsCallback](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/-valid-params-callback/index.html) instance on [BecsDebitWidget#validParamsCallback](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/index.html#com.stripe.android.view/BecsDebitWidget/validParamsCallback/#/PointingToDeclaration/) to be notified after the customer enters the required details to create an instance of `PaymentMethodCreateParams`​.

#### Kotlin

```kotlin
class CheckoutActivity : Activity() {
    private val stripe: Stripe by lazy {
        Stripe(this, PaymentConfiguration.getInstance(this).publishableKey)
    }

    private lateinit var becsDebitWidget: BecsDebitWidget
    private lateinit var setupIntentClientSecret: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.checkout_activity)

        becsDebitWidget = findViewById(R.id.becs_debit_widget)
        val saveButton = findViewById<Button>(R.id.save_button)

        becsDebitWidget.validParamsCallback =
            object : BecsDebitWidget.ValidParamsCallback {
                override fun onInputChanged(isValid: Boolean) {
                    // enable saveButton if the customer's input is valid
                    saveButton.isEnabled = isValid
                }
            }

        saveButton.setOnClickListener {
            onSaveClicked(paymentIntentClientSecret)
        }

        createSetupIntent()
    }

    private fun createSetupIntent() {
        // Create a SetupIntent on your backend and return the client_secret to
        // this Activity. Set setupIntentClientSecret to the client_secret.
    }
}
```

## Create a SetupIntent [Server-side]

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` will track the steps of this set-up process. For BECS Direct Debit, this includes collecting a mandate from the customer and tracking its validity throughout its lifecycle.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server. Add `au_becs_debit` to the [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) array and specify the ID of the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id) object:

#### Accounts v2

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['au_becs_debit'],
  customer_account: customer_account.id,
});
const clientSecret = setupIntent.client_secret;
// Pass the client secret to the client
```

#### Customers v1

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['au_becs_debit'],
  customer: customer.id,
});
const clientSecret = setupIntent.client_secret;
// Pass the client secret to the client
```

After creating a `SetupIntent` on your server, you can associate the `SetupIntent` ID with the current session’s customer in your application’s data model. Doing so allows you to retrieve the information after you’ve successfully collected a payment method.

The returned `SetupIntent` object contains a `client_secret` property. Pass the client secret to the client-side application to continue with the setup process.

## Submit the payment method details to Stripe [Client-side]

After the user enters their payment details, confirm the `SetupIntent` to complete saving the debit information.

First, assemble a [ConfirmSetupIntentParams](https://stripe.dev/stripe-android/payments-core/com.stripe.android.model/-confirm-setup-intent-params/index.html) object with:

1. The [BecsDebitWidget#params](https://stripe.dev/stripe-android/payments-core/com.stripe.android.view/-becs-debit-widget/index.html#com.stripe.android.view/BecsDebitWidget/params/#/PointingToDeclaration/) property
1. The `SetupIntent` client secret from your server

Rather than sending the entire `SetupIntent` object to the client, use its [client secret](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-client_secret) from [step 4](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md#android-create-setup-intent). This is different from your API keys that authenticate Stripe API requests.

The client secret should still be handled carefully because it can complete the setup. Don’t log it, embed it in URLs, or expose it to anyone but the customer.

Next, complete the payment by calling the [PaymentLauncher confirm](https://stripe.dev/stripe-android/payments-core/com.stripe.android.payments.paymentlauncher/-payment-launcher/index.html#74063765%2FFunctions%2F-1622557690) method.

When you set [customer_account](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer_account) or [customer](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-customer), the *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) is attached to the provided object. This allows you to use the stored `PaymentMethod` to collect future payments without prompting the customer for payment method details.

#### Kotlin

```kotlin
class CheckoutActivity : Activity() {
    // ...

    fun onSaveClicked(setupIntentClientSecret: String) {
        becsDebitWidget.params?.let { params ->
            paymentLauncher.confirm(
                ConfirmSetupIntentParams.create(
                    paymentMethodCreateParams = params,
                    clientSecret = setupIntentClientSecret
                )
            )
        }
    }

    private fun onPaymentResult(paymentResult: PaymentResult) {
        when (paymentResult) {
            is PaymentResult.Completed -> {
                // SetupIntent confirmation succeeded
            }
            is PaymentResult.Canceled -> {
                // SetupIntent confirmation canceled
            }
            is PaymentResult.Failed -> {
                // SetupIntent confirmation failed see here for message:
                // ((PaymentResult.Failed) paymentResult).getThrowable().getMessage();
            }
        }
    }
}
```

After confirming the `SetupIntent`​, share the [mandate URL](https://docs.stripe.com/api/mandates/object.md#mandate_object-payment_method_details-au_becs_debit-url) from the [Mandate object](https://docs.stripe.com/api/mandates.md) with your customer. We also recommend including the following details when you confirm their mandate has been established:

- An explicit confirmation message that indicates a Direct Debit arrangement has been set up
- The [business name](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment.md) that will appear on the customer’s bank statement whenever their account gets debited
- The payment amount and schedule (if applicable)
- A link to the generated DDR mandate URL

​​You can access the `Mandate​` object’s ID from the `mandate` on the [SetupIntent object](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-mandate) (included with the `setup_intent.succeeded` event sent after confirmation) or you can [retrieve it through the API](https://docs.stripe.com/api/setup_intents/retrieve.md).

## Test the integration

You can test your form using the test BSB number `000000` and one of the test account numbers below with your [Stripe#confirmSetupIntent()](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-stripe/confirm-setup-intent.html) method call.

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

# React Native

> This is a React Native for when payment-ui is mobile and platform is react-native. View the full page at https://docs.stripe.com/payments/au-becs-debit/set-up-payment?payment-ui=mobile&platform=react-native.

Use `AuBECSDebitForm`, Stripe’s prebuilt BECS payment details collection UI, to create a payment form that lets you securely collect bank details without handling sensitive customer data. You can use the [Setup Intents API](https://docs.stripe.com/payments/setup-intents.md) to collect BECS Direct Debit payment method details in advance, and determine the final amount or payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a subscription](https://docs.stripe.com/billing/subscriptions/trials.md)

## Set up Stripe [Server-side] [Client-side]

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

#### Node.js

```bash
# Install with npm
npm install stripe --save
```

### Client-side

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open source and fully documented. Internally, it uses the [native iOS](https://github.com/stripe/stripe-ios) and [Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s React Native SDK, run one of the following commands in your project’s directory (depending on which package manager you use):

#### yarn

```bash
yarn add @stripe/stripe-react-native
```

#### npm

```bash
npm install @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, go to the **ios** directory and run `pod install` to ensure that you also install the required native dependencies.
- For Android, there are no more dependencies to install.

> We recommend following the [official TypeScript guide](https://reactnative.dev/docs/typescript#adding-typescript-to-an-existing-project) to add TypeScript support.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen with the `StripeProvider` component, or use the `initStripe` initialization method. Only the API [publishable key](https://docs.stripe.com/keys.md#obtain-api-keys) in `publishableKey` is required. The following example shows how to initialize Stripe using the `StripeProvider` component.

```jsx
import { useState, useEffect } from "react";
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  const [publishableKey, setPublishableKey] = useState("");

  const fetchPublishableKey = async () => {
    const key = await fetchKey(); // fetch key from your server here
    setPublishableKey(key);
  };

  useEffect(() => {
    fetchPublishableKey();
  }, []);

  return (
    <StripeProvider
      publishableKey={publishableKey}
      merchantIdentifier="merchant.identifier" // required for Apple Pay
      urlScheme="your-url-scheme" // required for 3D Secure and bank redirects
    >
      {/* Your app code here */}
    </StripeProvider>
  );
}
```

> Use your API [test keys](https://docs.stripe.com/keys.md#obtain-api-keys) while you test and develop, and your [live mode](https://docs.stripe.com/keys.md#test-live-modes) keys when you publish your app.

## Create or retrieve a customer [Server-side]

To reuse a BECS Direct Debit account for future payments, attach it to an object that represents your customer.

> #### Use the Accounts v2 API to represent customers
>
> The Accounts v2 API is generally available for Connect users, and in public preview for other Stripe users. If you’re part of the Accounts v2 preview, you need to specify a [specify a preview version](https://docs.stripe.com/api-v2-overview.md#sdk-and-api-versioning) in your code.
>
> To request access to the Accounts v2 preview,
>
> For most use cases, we recommend [modeling your customers as customer-configured Account objects](https://docs.stripe.com/accounts-v2/use-accounts-as-customers.md) instead of using [Customer](https://docs.stripe.com/api/customers.md) objects.

Create a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/create.md#v2_create_accounts-configuration-customer) or [Customer](https://docs.stripe.com/api/customers/create.md) when your customer creates an account with your business, or when saving a payment method. Associate the object’s ID with your own internal representation of a customer.

Create a new customer or retrieve an existing one to associate with this payment.

#### Accounts v2

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const account = await stripe.v2.core.accounts.create({
  contact_email: 'jenny.rosen@example.com',
  display_name: 'Jenny Rosen',
  configuration: {
    customer: {},
  },
  include: ['configuration.customer'],
});
```

#### Customers v1

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const customer = await stripe.customers.create({
  name: 'Jenny Rosen',
  email: 'jenny.rosen@example.com',
});
```

## Collect payment method details and mandate acknowledgment [Client-side]

You can securely collect Australia BECS Direct Debit payment information with `AuBECSDebitForm`, a drop-in UI component provided by the SDK. `AuBECSDebitForm` provides a UI for customers to enter their name, email, BSB number, and account number in addition to displaying the [Australia BECS Direct Debit Terms](https://stripe.com/au-becs/legal).

Add an `AuBECSDebitForm` component to the screen with your company name as a prop. You can also customize `AuBECSDebitForm` to match the look and feel of your app by providing the `formStyle` prop. Collect form details with the `onComplete` prop.

```javascript
function BECSSetupFuturePaymentScreen() {
  const [formDetails, setFormDetails] = useState<
    AuBECSDebitFormComponent.FormDetails
  >();

  return (
    <View>
      <AuBECSDebitForm
        onComplete={(value) => setFormDetails(value)}
        companyName="Example Company Inc."
        formStyle={{
          textColor: '#000000',
          fontSize: 22,
          placeholderColor: '#999999',
        }}
      />
      <Button title="Save" variant="primary" onPress={handlePayPress} />
    </View>
  );
}
```

## Create a SetupIntent [Server-side] [Client-side]

### Server-side

A [SetupIntent](https://docs.stripe.com/api/setup_intents.md) is an object that represents your intent to set up a customer’s payment method for future payments. The `SetupIntent` will track the steps of this set-up process. For BECS Direct Debit, this includes collecting a mandate from the customer and tracking its validity throughout its lifecycle.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) on your server. Add `au_becs_debit` to the [payment_method_types](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_types) array and specify the ID of the customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-id) or [Customer](https://docs.stripe.com/api/customers/object.md#customer_object-id) object:

#### Accounts v2

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['au_becs_debit'],
  customer_account: customer_account.id,
});
const clientSecret = setupIntent.client_secret;
// Pass the client secret to the client
```

#### Customers v1

#### Node.js

```javascript
// Using Express
const express = require('express');
const app = express();
app.use(express.json());
const { resolve } = require('path');

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const setupIntent = await stripe.setupIntents.create({
  payment_method_types: ['au_becs_debit'],
  customer: customer.id,
});
const clientSecret = setupIntent.client_secret;
// Pass the client secret to the client
```

After creating a `SetupIntent` on your server, you can associate the `SetupIntent` ID with the current session’s customer in your application’s data model. Doing so allows you to retrieve the information after you’ve successfully collected a payment method.

The returned `SetupIntent` object contains a `client_secret` property. Pass the client secret to the client-side application to continue with the setup process.

### Client-side

On the client, request a SetupIntent from your server and store its client secret.

```javascript
const fetchSetupIntentClientSecret = async (customerEmail: string) => {
  const response = await fetch(`${API_URL}/create-setup-intent`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email: customerEmail,
      payment_method_types: ['au_becs_debit'],
    }),
  });
  const {clientSecret, error} = await response.json();

  return {clientSecret, error};
};
```

## Submit the payment method details to Stripe [Client-side]

Retrieve the client secret from the SetupIntent you created and call `confirmSetupIntent`. This presents a webview where the customer can complete the setup on their bank’s website or app.

```javascript
function BECSSetupFuturePaymentScreen() {
  const { confirmSetupIntent } = useConfirmSetupIntent();

  const [formDetails, setFormDetails] = useState<
    AuBECSDebitFormComponent.FormDetails
  >();

  const handlePayPress = async () => {
    const { error, setupIntent } = await confirmSetupIntent(clientSecret, {
      paymentMethodType: 'AuBecsDebit',
      paymentMethodData: {
        formDetails,
      }
    });

    if (error) {
      Alert.alert(`Error code: ${error.code}`, error.message);
      console.log('Setup intent confirmation error', error.message);
    } else if (setupIntent) {
      Alert.alert(
        `Success: Setup intent created. Intent status: ${setupIntent.status}`
      );
    }
  };

  return (
    <View>
      <AuBECSDebitForm
        onComplete={(value) => setFormDetails(value)}
        companyName="Example Company Inc."
        formStyle={{
          textColor: '#000000',
          fontSize: 22,
          placeholderColor: '#999999',
        }}
      />
      <Button title="Save" variant="primary" onPress={handlePayPress} />
    </View>
  );
}
```

## Test the integration

Test your form using the test BSB number `000000` and one of the test account numbers below when you call `confirmSetupIntent`.

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

## See also

- [Accept an Australia BECS Direct Debit payment](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment.md)
- [Connect payments](https://docs.stripe.com/connect/charges.md)
