<!-- Source URL: https://docs.stripe.com/payments/checkout/dynamically-update-trial-durations -->
<!-- Fetched: 2026-04-21 -->

# Dynamically update trial durations

Learn how to modify subscription trial periods during checkout.

> #### Private preview
>
> Dynamic trial updates is in private preview.

Learn how to dynamically update trial durations on subscription [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions/object.md).

### Use cases

- **Dynamic trial management**: Add or remove trials based on promotional conditions or customer actions.
- **Extend trials for upsells**: Offer longer trial periods when customers upgrade to higher-tier plans (for example. 7 days for monthly gets extended to 14 days for yearly).

> #### Payment Intents API
>
> If you use the Payment Intents API, you can use the [Subscriptions API](https://docs.stripe.com/api/subscriptions.md) to adjust trial settings.

## Set up the SDK [Server-side]

Use our official libraries to access the Stripe API from your application:

#### Ruby

```bash
gem install stripe -v 15.1.0-beta.2
```

## Update the server SDK [Server-side]

To use this beta, first update your SDK to use the private preview API version and the `checkout_server_update_beta=v1` beta version header.

#### Node

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>", {
  apiVersion: "2025-03-31.preview; checkout_server_update_beta=v1;",
});
```

## Dynamically update trial durations [Server-side]

Create an endpoint on your server to update the trial duration for a yearly upsell on the Checkout Session. You call this from the front end in a later step.

> Client-side code runs in an environment that’s controlled by the user. A malicious user can bypass your client-side validation, intercept and modify requests, or create new requests to your server.

When creating an endpoint, we recommend the following:

- Create endpoints for specific customer interactions instead of making them generic. For example, “extend trial for yearly upgrade” instead of a general “update” action. Specific endpoints can help with writing and maintaining validation logic.
- Don’t pass [session data](https://docs.stripe.com/js/custom_checkout/session_object) directly from the client to your endpoint. Malicious clients can modify request data, making it an unreliable source for determining the Checkout Session state. Instead, pass the [session ID](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-id) to your server and use it to securely retrieve the data from the Stripe API.

You can update trial durations using either:

- `trial_period_days`: An integer that represents the number of days for the trial period, or an empty string to remove the trial.
- `trial_end`: A Unix timestamp that represents when the trial should end, or an empty string to remove the trial.

Keep in mind the following:

- The `trial_period_days` and `trial_end` parameters are mutually exclusive. You can only specify one of them in a single update request.
- When removing a trial, use the same field that it was set with. You can only use `trial_period_days: ""` to remove a trial set with `trial_period_days`. You can only use `trial_end: ""` to remove a trial set with `trial_end`.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>', {
  apiVersion: '2025-03-31.preview; checkout_server_update_beta=v1;',
});

const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

app.post('/extend-trial-for-yearly', async (req, res) => {
  const { checkout_session_id } = req.body;

  if (!checkout_session_id) {
    return res.status(400).json({
      type: 'error',
      message: 'We couldn't process your request. Please try again later.',
    });
  }

  try {
    // 1. Retrieve the current session to validate it's a subscription
    const session = await stripe.checkout.sessions.retrieve(checkout_session_id);

    if (session.mode !== 'subscription') {
      return res.status(400).json({
        type: 'error',
        message: 'Trial updates are only available for subscription sessions.',
      });
    }

    // 2. Update the Checkout Session with extended trial duration
    await stripe.checkout.sessions.update(checkout_session_id, {
      subscription_data: {
        trial_period_days: 14,
      },
    });

    // 3. Return success response
    return res.json({ type: 'success' });
  } catch (err) {
    if (err.type === 'StripeInvalidRequestError') {
      // Handle Stripe errors with a generic error message
      return res.status(400).json({
        type: 'error',
        message: 'We couldn't process your request. Please try again later.',
      });
    }

    // Handle unexpected errors
    return res.status(500).json({
      type: 'error',
      message: 'Something went wrong on our end. Please try again later.',
    });
  }
});

app.listen(4242, () => console.log('Server is running on port 4242'));
```

## Update the client SDK [Client-side]

#### HTML + JS

Initialize Stripe.js with the `custom_checkout_server_updates_1` beta header.

```javascript
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>", {
  betas: ["custom_checkout_server_updates_1"],
});
```

#### React

Pass the `custom_checkout_server_updates_1` beta header when initializing the `stripe` instance.

```javascript
import { loadStripe } from "@stripe/stripe-js";
const stripe = loadStripe("<<YOUR_PUBLISHABLE_KEY>>", {
  betas: ["custom_checkout_server_updates_1"],
});
```

## Request server updates [Client-side]

#### HTML + JS

From your front end, send an update request to your server and wrap it in [runServerUpdate](https://docs.stripe.com/js/custom_checkout/run_server_update). A successful request updates the [Session](https://docs.stripe.com/js/custom_checkout/session_object) object with the new trial duration.

```html
<button id="extend-trial-yearly">
  Upgrade to a yearly subscription and get an extended trial
</button>
```

```javascript
document
  .getElementById("extend-trial-yearly")
  .addEventListener("click", async (event) => {
    const updateCheckout = () => {
      return fetch("/extend-trial-for-yearly", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({
          checkout_session_id: actions.getSession().id,
        }),
      });
    };
    const response = await checkout.runServerUpdate(updateCheckout);
    if (!response.ok) {
      // Handle error state
      return;
    }

    // Update UI to reflect the extended trial
    event.target.textContent = "Trial extended to 14 days!";
    event.target.disabled = true;
  });
```

#### React

Trigger the update from your frontend by making a request to your server, wrapping it in [runServerUpdate](https://docs.stripe.com/js/custom_checkout/run_server_update). If the request is successful, the [session](https://docs.stripe.com/js/custom_checkout/session_object) object is updated with the new trial duration.

```jsx
import React from "react";
import { useCheckout } from "@stripe/react-stripe-js/checkout";

const ExtendTrialButton = () => {
  const [isExtended, setIsExtended] = React.useState(false);
  const checkoutState = useCheckout();

  if (checkoutState.type === "loading") {
    return <div>Loading...</div>;
  } else if (checkoutState.type === "error") {
    return <div>Error: {checkoutState.error.message}</div>;
  }
  const { runServerUpdate, id } = checkoutState.checkout;

  const updateCheckout = () =>
    fetch("/extend-trial-for-yearly", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify({
        checkout_session_id: id,
      }),
    });

  const handleClick = async () => {
    const response = await runServerUpdate(updateCheckout);
    if (!response.ok) {
      // set error state
      return;
    }

    // Update UI to reflect the extended trial
    setIsExtended(true);
  };

  return (
    <button onClick={handleClick} disabled={isExtended}>
      {isExtended ?
        "Trial extended to 14 days!"
      : "Upgrade to a yearly subscription and get an extended trial"}
    </button>
  );
};
```

## Test the integration

Test your integration to ensure trial duration updates work correctly:

1. Create a subscription Checkout Session with an initial trial period.
1. Trigger your server endpoint by interacting with the UI element you created.
1. Verify the trial duration is updated correctly in the Checkout Session.
1. Complete the checkout to ensure the subscription is created with the correct trial settings.

> When testing, use a [sandbox](https://docs.stripe.com/sandboxes.md) to avoid creating live subscriptions. You can verify the trial duration changes by inspecting the Checkout Session object or the created subscription.

## Common testing scenarios

- **Trial extension**: Start with a 7-day trial, extend to 14 days, and verify the change is reflected in the UI and session object.
- **Remove existing trial**: Start with a 7-day trial, remove it, and verify the change is reflected in the UI and session object. Remove the trial using the same field that it was set with.
- **Error handling**: Test invalid requests to ensure your error handling works correctly.
