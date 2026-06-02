<!-- Source URL: https://docs.stripe.com/crypto/onramp/embedded-quickstart -->
<!-- Fetched: 2026-05-11 -->

# Set up an embeddable onramp integration

Build a full, working Stripe fiat-to-crypto onramp integration with your test API key. To customize the look and feel, go to the branding settings of the Dashboard. In the Dashboard, make sure you've added domains to the domain allowlist for the domains you'll use to host the onramp page.

## 1. Set up the server

### Install the Stripe Node library

Install the package and import it in your code.

```bash
npm install --save stripe
```

### Create an OnrampSession

Add an endpoint on your server that creates an OnrampSession object. An OnrampSession object tracks the customer's onramp lifecycle, keeping track of order details and ensuring the customer is only charged once. Return the OnrampSession object's client secret in the response to finish the onramp on the client.

> Note: Our official libraries don't contain built-in support for the API endpoints because the onramp API is in limited beta. This guide includes custom extension to the official Stripe libraries for minting onramp sessions. You can find them in the downloadable sample code.

```javascript
const express = require("express");
const app = express();
// This is a public sample test API key.
// Don't submit any personally identifiable information in requests made with this key.
// Sign in to see your own test API key embedded in code samples.
const Stripe = require("stripe");
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const stripe = Stripe('sk_test_Ou1w6LVt3zmVipDVJsvMeQsc');
const OnrampSessionResource = Stripe.StripeResource.extend({
  create: Stripe.StripeResource.method({
    method: 'POST',
    path: 'crypto/onramp_sessions',
  }),
});

app.use(express.static("public"));
app.use(express.json());

app.post("/create-onramp-session", async (req, res) => {
  const { transaction_details } = req.body;

  // Create an OnrampSession with the order amount and currency
  const onrampSession = await new OnrampSessionResource(stripe).create({
    transaction_details: {
      destination_currency: transaction_details["destination_currency"],
      destination_exchange_amount: transaction_details["destination_exchange_amount"],
      destination_network: transaction_details["destination_network"],
    },
    customer_ip_address: req.socket.remoteAddress,
  });

  res.send({
    clientSecret: onrampSession.client_secret,
  });
});

app.listen(4242, () => console.log("Node server listening on port 4242!"));
```

## 2. Build an onramp page on the client

### Add Stripe to your React app

Use the Stripe.js and the Stripe crypto SDK to remain PCI compliant. The crypto SDK includes Typescript type definitions.

```bash
npm install --save @stripe/crypto @stripe/stripe-js
```

### Initialize the Stripe crypto SDK

Call `loadStripeOnramp()` with your Stripe publishable API key to configure the Stripe library.

### Fetch an OnrampSession

Immediately make a request to the endpoint on your server to create a new OnrampSession object as soon as your page loads. The `clientSecret` returned by your endpoint is used to complete the onramp.

### Define Stripe Elements

Define components in your code to simplify the access of the `StripeOnramp` object and rendering of the onramp widget.

> Note: These components will be released as an ES module in the future similar to `@stripe/react-stripe-js`.

### Initialize Stripe Elements

Pass the resulting promise from the `loadStripeOnramp` call to the Elements provider. This allows the child components to access the Stripe service through the Elements consumer.

### Add the OnrampElement

Add an `OnrampElement` component to your page. It embeds an iframe with a dynamic UI that collects necessary order, identity, and payment details to complete the purchase and delivery of crypto.

> Note: Use the values provided here to complete an onramp transaction in sandbox.

```jsx
// App.jsx
import React, { useState, useEffect } from "react";
import { loadStripeOnramp } from "@stripe/crypto";

import { CryptoElements, OnrampElement } from './StripeCryptoElements';
import "./App.css";

// Make sure to call loadStripeOnramp outside of a component's render to avoid
// recreating the StripeOnramp object on every render.
// This is a public sample test API key.
// Don't submit any personally identifiable information in requests made with this key.
// Sign in to see your own test API key embedded in code samples.
const stripeOnrampPromise = loadStripeOnramp("pk_test_GvF3BSyx8RSXMK5yAFhqEd3H");

export default function App() {
  const [clientSecret, setClientSecret] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    // Fetches an onramp session and captures the client secret
    fetch("/create-onramp-session", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        transaction_details: {
          destination_currency: "usdc",
          destination_exchange_amount: "13.37",
          destination_network: "ethereum",
        }
      }),
    })
      .then((res) => res.json())
      .then((data) => setClientSecret(data.clientSecret));
  }, []);

  const onChange = React.useCallback(({ session }) => {
    setMessage(`OnrampSession is now in ${session.status} state.`);
  }, []);

  return (
    <div className="App">
      <CryptoElements stripeOnramp={stripeOnrampPromise}>
        {clientSecret && (
          <OnrampElement
            id="onramp-element"
            clientSecret={clientSecret}
            appearance={{ theme: "dark" }}
            onChange={onChange}
          />
        )}
      </CryptoElements>
      {message && <div id="onramp-message">{message}</div>}
    </div>
  );
}
```

```jsx
// StripeCryptoElements.jsx
import React from 'react';

// ReactContext to simplify access of StripeOnramp object
const CryptoElementsContext = React.createContext(null);
CryptoElementsContext.displayName = 'CryptoElementsContext';

export const CryptoElements = ({ stripeOnramp, children }) => {
  const [ctx, setContext] = React.useState(() => ({ onramp: null }));

  React.useEffect(() => {
    let isMounted = true;

    Promise.resolve(stripeOnramp).then((onramp) => {
      if (onramp && isMounted) {
        setContext((ctx) => (ctx.onramp ? ctx : { onramp }));
      }
    });

    return () => { isMounted = false; };
  }, [stripeOnramp]);

  return (
    <CryptoElementsContext.Provider value={ctx}>
      {children}
    </CryptoElementsContext.Provider>
  );
};

// React hook to get StripeOnramp from context
export const useStripeOnramp = () => {
  const context = React.useContext(CryptoElementsContext);
  return context?.onramp;
};

// Helper hook for session event listeners
const useOnrampSessionListener = (type, session, callback) => {
  React.useEffect(() => {
    if (session && callback) {
      const listener = (e) => callback(e.payload);
      session.addEventListener(type, listener);
      return () => { session.removeEventListener(type, listener); };
    }
    return () => {};
  }, [session, callback, type]);
};

export const OnrampElement = ({ clientSecret, appearance, onReady, onChange, ...props }) => {
  const stripeOnramp = useStripeOnramp();
  const onrampElementRef = React.useRef(null);
  const [session, setSession] = React.useState();

  const appearanceJSON = JSON.stringify(appearance);
  React.useEffect(() => {
    const containerRef = onrampElementRef.current;
    if (containerRef) {
      containerRef.innerHTML = '';

      if (clientSecret && stripeOnramp) {
        setSession(
          stripeOnramp
            .createSession({
              clientSecret,
              appearance: appearanceJSON ? JSON.parse(appearanceJSON) : {}
            })
            .mount(containerRef)
        );
      }
    }
  }, [appearanceJSON, clientSecret, stripeOnramp]);

  useOnrampSessionListener('onramp_ui_loaded', session, onReady);
  useOnrampSessionListener('onramp_session_updated', session, onChange);

  return <div {...props} ref={onrampElementRef}></div>;
};
```

```css
/* App.css */
#root {
  display: flex;
  align-items: center;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  display: flex;
  justify-content: center;
  align-content: center;
  height: 100vh;
  width: 100vw;
}

#onramp-message {
  color: rgb(105, 115, 134);
  font-size: 16px;
  line-height: 20px;
  padding-top: 12px;
  text-align: center;
}

#onramp-element {
  min-width: min(450px, 60vw);
  margin-bottom: 24px;
}
```

## Enhance your integration

### Style the onramp widget

Customize the Onramp UI with brand settings in your dashboard. Apply dark mode to the onramp widget with the `theme` parameter:

```jsx
<OnrampElement appearance={{ theme: "dark" }} ... />
```

### Set up OnrampSession state callbacks

Initialize callbacks to create a responsive interface when an onramp session completes:

```jsx
const onChange = React.useCallback(({ session }) => {
  setMessage(`OnrampSession is now in ${session.status} state.`);
}, []);
```

Events:
- `onramp_ui_loaded` — fires when the onramp UI finishes loading (`onReady` prop)
- `onramp_session_updated` — fires on any session status change (`onChange` prop)

## Next steps

- **Customize appearance**: Customize the appearance of the onramp via Dashboard branding settings
- **Pre-populate parameters**: Customize the OnrampSession, such as pre-populating customer information and setting default cryptocurrencies
- **Configure conversion quotes**: Use the Onramp Quotes API to fetch estimated quotes for onramp conversions into various cryptocurrencies on different networks
- **Back-end integration best practices**: Review the suggested OnrampSession parameters to set based on your product use case
