<!-- Source: npm package README — @paypal/react-paypal-js v8.9.2 -->
<!-- URL: https://www.npmjs.com/package/@paypal/react-paypal-js -->
<!-- Fetched: 2026-04-13 -->
<!-- SDK version: v8.x (uses PayPal JS SDK v5 / CardFields) -->

# @paypal/react-paypal-js

**Version:** 8.9.2 | **License:** Apache-2.0

React components for the PayPal JS SDK.

## Why use react-paypal-js?

### The Problem

Developers integrating with PayPal are expected to add the JS SDK `<script>` to a website and then render components like the PayPal Buttons after the script loads. This architecture works great for simple websites but can be challenging when building single page apps.

React developers think in terms of components and not about loading external scripts from an index.html file. It's easy to end up with a React PayPal integration that's sub-optimal and hurts the buyer's user experience. For example, abstracting away all the implementation details of the PayPal Buttons into a single React component is an anti-pattern because it tightly couples script loading with rendering. It's also problematic when you need to render multiple different PayPal components that share the same global script parameters.

### The Solution

react-paypal-js provides a solution to developers to abstract away complexities around loading the JS SDK. It enforces best practices by default so buyers get the best possible user experience.

### Features

- Enforce async loading the JS SDK upfront so when it's time to render the buttons to your buyer, they render immediately.
- Abstract away the complexity around loading the JS SDK with the global `PayPalScriptProvider` component.
- Support dispatching actions to reload the JS SDK and re-render components when global parameters like currency change.
- Easy to use components for all the different Braintree/PayPal product offerings:
  - `PayPalButtons`
  - `PayPalMarks`
  - `PayPalMessages`
  - `PayPalHostedFields`
  - `BraintreePayPalButtons`

## Installation

```bash
npm install @paypal/react-paypal-js
```

## Usage

This PayPal React library consists of two main parts:

- **Context Provider** — `<PayPalScriptProvider />` manages loading the JS SDK script. Add it to the root of your React app. Uses the Context API for managing state and communicating to child components. Supports reloading the script when parameters change.
- **SDK Components** — components like `<PayPalButtons />` render the UI for PayPal products served by the JS SDK.

```javascript
// App.js
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
    return (
        <PayPalScriptProvider options={{ clientId: "test" }}>
            <PayPalButtons style={{ layout: "horizontal" }} />
        </PayPalScriptProvider>
    );
}
```

## PayPalScriptProvider

### Options

Use the `options` prop to configure the JS SDK. Keys use camelCase (`clientId`, `dataClientToken`, `dataNamespace`, etc.).

```javascript
const initialOptions = {
    clientId: "test",
    currency: "USD",
    intent: "capture",
};

export default function App() {
    return (
        <PayPalScriptProvider options={initialOptions}>
            <PayPalButtons />
        </PayPalScriptProvider>
    );
}
```

### deferLoading

Control when the JS SDK script loads. Default: `false` (loads immediately).

Set to `true` to prevent loading the script when `PayPalScriptProvider` renders, then dispatch an action later to load it.

```javascript
<PayPalScriptProvider deferLoading={true} options={initialOptions}>
    <PayPalButtons />
</PayPalScriptProvider>
```

### Tracking loading state — `usePayPalScriptReducer`

Same API as React's `useReducer`. Provides derived loading state attributes:

- `isInitial` — not started (only when `deferLoading={true}`)
- `isPending` — loading (default)
- `isResolved` — successfully loaded
- `isRejected` — failed to load

```javascript
const [{ isPending }] = usePayPalScriptReducer();

return (
    <>
        {isPending ? <div className="spinner" /> : null}
        <PayPalButtons />
    </>
);
```

### Reloading when parameters change

Use `resetOptions` action to reload the JS SDK with new parameters (e.g. currency change):

```javascript
const [{ options }, dispatch] = usePayPalScriptReducer();
const [currency, setCurrency] = useState(options.currency);

function onCurrencyChange({ target: { value } }) {
    setCurrency(value);
    dispatch({
        type: "resetOptions",
        value: {
            ...options,
            currency: value,
        },
    });
}
```

## PayPalButtons

```javascript
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
    function createOrder() {
        return fetch("/my-server/create-paypal-order", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                cart: [{ id: "YOUR_PRODUCT_ID", quantity: "YOUR_PRODUCT_QUANTITY" }],
            }),
        })
            .then((response) => response.json())
            .then((order) => order.id);
    }

    function onApprove(data) {
        return fetch("/my-server/capture-paypal-order", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ orderID: data.orderID }),
        })
            .then((response) => response.json())
            .then((orderData) => {
                const name = orderData.payer.name.given_name;
                alert(`Transaction completed by ${name}`);
            });
    }

    return (
        <PayPalScriptProvider options={{ clientId: "test" }}>
            <PayPalButtons createOrder={createOrder} onApprove={onApprove} />
        </PayPalScriptProvider>
    );
}
```

## BraintreePayPalButtons

For Braintree merchants. Uses `actions.braintree.createPayment()` and `actions.braintree.tokenizePayment()`.

```javascript
import { PayPalScriptProvider, BraintreePayPalButtons } from "@paypal/react-paypal-js";

export default function App() {
    return (
        <PayPalScriptProvider
            options={{
                clientId: "test",
                dataClientToken: "<server-generated data-client-token>",
            }}
        >
            <BraintreePayPalButtons
                createOrder={(data, actions) => {
                    return actions.braintree.createPayment({
                        flow: "checkout",
                        amount: "10.0",
                        currency: "USD",
                        intent: "capture",
                    });
                }}
                onApprove={(data, actions) => {
                    return actions.braintree
                        .tokenizePayment(data)
                        .then((payload) => {
                            // call server-side endpoint to finish the sale
                        });
                }}
            />
        </PayPalScriptProvider>
    );
}
```

## PayPal Hosted Fields (legacy)

For the hosted-fields component (legacy). Three parts:
1. `<PayPalHostedFieldsProvider />` — wraps field elements, accepts `createOrder()`
2. `<PayPalHostedField>` — individual card field (number, cvv, expirationDate)
3. `usePayPalHostedFields` hook — exposes `submit()` function

```javascript
import {
    PayPalScriptProvider,
    PayPalHostedFieldsProvider,
    PayPalHostedField,
    usePayPalHostedFields,
} from "@paypal/react-paypal-js";

const SubmitPayment = () => {
    const hostedFields = usePayPalHostedFields();

    const submitHandler = () => {
        if (typeof hostedFields.submit !== "function") return;
        hostedFields.submit({ cardholderName: "John Wick" })
            .then((order) => {
                // capture payment
            });
    };
    return <button onClick={submitHandler}>Pay</button>;
};

export default function App() {
    return (
        <PayPalScriptProvider options={{ clientId: "your-client-id", dataClientToken: "your-data-client-token" }}>
            <PayPalHostedFieldsProvider
                createOrder={() => fetch("/orders").then(r => r.json()).then(o => o.id)}
            >
                <PayPalHostedField id="card-number" hostedFieldType="number" options={{ selector: "#card-number" }} />
                <PayPalHostedField id="cvv" hostedFieldType="cvv" options={{ selector: "#cvv" }} />
                <PayPalHostedField id="expiration-date" hostedFieldType="expirationDate" options={{ selector: "#expiration-date", placeholder: "MM/YY" }} />
                <SubmitPayment />
            </PayPalHostedFieldsProvider>
        </PayPalScriptProvider>
    );
}
```

## PayPal Card Fields (recommended — v5 SDK)

For the card-fields component (current, v5 SDK). Two integration styles:

### Using PayPalCardFieldsForm (all-in-one)

Three parts:
1. `<PayPalCardFieldsProvider />` — wraps form, accepts `createOrder()`, `onApprove()`, `onError()`
2. `<PayPalCardFieldsForm />` — renders all 4 fields out of the box
3. `usePayPalCardFields` hook — exposes `cardFields.submit()` and individual field refs

```javascript
import {
    PayPalScriptProvider,
    PayPalCardFieldsProvider,
    PayPalCardFieldsForm,
    usePayPalCardFields,
} from "@paypal/react-paypal-js";

const SubmitPayment = () => {
    const { cardFields } = usePayPalCardFields();

    function submitHandler() {
        if (typeof cardFields.submit !== "function") return;
        cardFields.submit().then(() => { /* success */ }).catch(() => { /* error */ });
    }
    return <button onClick={submitHandler}>Pay</button>;
};

export default function App() {
    return (
        <PayPalScriptProvider options={{ clientId: "your-client-id", components: "card-fields" }}>
            <PayPalCardFieldsProvider
                createOrder={createOrder}
                onApprove={onApprove}
                onError={onError}
            >
                <PayPalCardFieldsForm />
                <SubmitPayment />
            </PayPalCardFieldsProvider>
        </PayPalScriptProvider>
    );
}
```

### Using individual Card Fields

Four individual components — each must be a child of `<PayPalCardFieldsProvider />`:
- `<PayPalNameField />`
- `<PayPalNumberField />`
- `<PayPalExpiryField />`
- `<PayPalCVVField />`

`usePayPalCardFields` exposes `{ cardFields, fields }`:
- `cardFields.submit()` — submit the form
- `fields.CVVField.focus()` — programmatic DOM manipulation

```javascript
import {
    PayPalScriptProvider,
    PayPalCardFieldsProvider,
    PayPalNameField,
    PayPalNumberField,
    PayPalExpiryField,
    PayPalCVVField,
    usePayPalCardFields,
} from "@paypal/react-paypal-js";

export default function App() {
    return (
        <PayPalScriptProvider options={{ clientId: "your-client-id", components: "card-fields" }}>
            <PayPalCardFieldsProvider createOrder={createOrder} onApprove={onApprove} onError={onError}>
                <PayPalNameField />
                <PayPalNumberField />
                <PayPalExpiryField />
                <PayPalCVVField />
                <SubmitPayment />
            </PayPalCardFieldsProvider>
        </PayPalScriptProvider>
    );
}
```

## Browser Support

Supports all popular browsers including IE 11. Same browser support as the JS SDK.
