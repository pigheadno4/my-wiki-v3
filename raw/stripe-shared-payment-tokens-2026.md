<!-- Source URL: https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens -->
<!-- Fetched: 2026-05-12 -->

# Shared payment tokens

Learn how to use shared payment tokens.

> Shared payment tokens (SPTs) are available to agents, customers, and sellers in the US.

# Sellers

> This is a Sellers for when agent-seller is seller. View the full page at https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens?agent-seller=seller.

As the seller, you receive a [shared payment token (SPT)](https://docs.stripe.com/api/shared-payment/granted-token.md) from the agent. An SPT is a scoped grant to use the customer’s payment method. The agent grants SPTs to your [Stripe profile](https://docs.stripe.com/get-started/account/profile.md), each with usage and expiration limits.
Payment method registration and processing (See full diagram at https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens)

## Before you begin

- By using SPTs, you agree to the [terms of service](https://stripe.com/legal/ssa-services-terms#stripe-agentic-commerce-seller-services-preview).
- If you don’t already have a Stripe account, [create one](https://stripe.com/register).
- Make sure you create your [Stripe profile](https://docs.stripe.com/get-started/account/profile.md) in the Stripe Dashboard.

## Test receiving an SPT

Use test helpers to simulate receiving an SPT granted by the agent. The following request grants your account an SPT using a test payment method and simulates limits that agents might set, such as currency, maximum amount, and expiration window.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const grantedToken =
  await stripe.testHelpers.sharedPayment.grantedTokens.create({
    payment_method: "pm_card_visa",
    usage_limits: {
      currency: "usd",
      max_amount: 1000,
      expires_at: 1751587220,
    },
  });
```

### Set usage limits

Use the `usage_limits` parameter to specify the maximum amount and expiration window. The agent sets the maximum amount to match the total amount of the transaction.

### Specify the payment method

Use the `payment_method` parameter to specify the payment method the customer selected for the purchase.

## Test your live mode integration

To test your integration in live mode, use the [link-cli](https://link.com/agents) to issue SPTs from your personal Link account. The `link-cli` can provision one-time shared payment token credentials. Follow the instructions at [link.com/agents](https://link.com/agents) to install the `link-cli` skills or register it as an MCP server in your preferred agent.

1. Log in to your personal Link account, or [sign up](https://app.link.com) if you don’t have one.

```bash
npx @stripe/link-cli auth login
```

1. Choose the payment method you want to use. If you don’t already have one, [add a payment method](https://app.link.com/wallet).

```bash
npx @stripe/link-cli payment-methods list
```

1. Create a spend request to issue a one-time SPT scoped to your business profile.

```bash
npx @stripe/link-cli spend-request create \
  --payment-method-id csmrpd_xxx \
  --context "Machine payments with SPTs in live mode" \
  --amount 100 \
  --credential-type shared_payment_token \
  --network-id profile_... \
  --request-approval
```

## Use a shared payment token

After you receive a granted `SharedPaymentToken`, create a `PaymentIntent` to complete the payment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_data: {
    shared_payment_granted_token: "spt_123",
  },
  confirm: true,
});
```

When you confirm a `PaymentIntent` with the SPT, Stripe sets `payment_method` to a new `PaymentMethod` cloned from the customer’s original payment method. Subsequent events, such as refunds and reporting, behave as if you provided the `PaymentMethod` directly.

You can retrieve details about the granted `SharedPaymentToken`, including limited information about the underlying payment method, such as the card brand, last four digits, and usage limits.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const grantedToken =
  await stripe.sharedPayment.grantedTokens.retrieve("spt_123");
```

```
{
  "id": "spt_123",
  "object": "shared_payment.granted_token",
  "created": 1751500820,
  "deactivated_at": null,
  "deactivated_reason": null,
  "usage_limits": {
    "currency": "usd",
    "expires_at": 1781172017,
    "max_amount": 1000
  }
  ...
}
```

### Listen for webhook events

We send events to you and the agent when:

- You use a granted SPT to accept a payment.
- The agent revokes a granted SPT. You can’t create a payment with a revoked SPT.

| Event                                      | Description                                        | Use case                                                          |
| ------------------------------------------ | -------------------------------------------------- | ----------------------------------------------------------------- |
| `shared_payment.granted_token.deactivated` | The SPT has been deactivated (revoked or expired). | Listen for this event to know when you can no longer use the SPT. |

# Agents

> This is a Agents for when agent-seller is agent. View the full page at https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens?agent-seller=agent.

As the agent, use [shared payment tokens (SPTs)](https://docs.stripe.com/api/shared-payment/issued-token/.md) to grant the seller scoped access to the customer’s payment method for payment processing.
Payment method registration and processing (See full diagram at https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens)

## Before you begin

- By using SPTs, you agree to the [terms of service](https://stripe.com/legal/ssa-services-terms#stripe-agentic-commerce-agent-services-preview).
- If you don’t already have a Stripe account, [create one](https://stripe.com/register).
- Make sure you create your [Stripe profile](https://docs.stripe.com/get-started/account/profile.md) in the Stripe Dashboard.

## Collect Stripe profile from seller

During seller onboarding, collect the seller’s Stripe profile. Sellers can create a new profile or find their current profile in the [Stripe Dashboard](https://dashboard.stripe.com/profiles). You issue an SPT to this profile for each transaction.

## Collect the customer’s payment details

Use the [Payment Element](https://docs.stripe.com/payments/payment-element.md) to securely collect payment details and support multiple payment methods through a single integration. It automatically helps ensure that the payment methods you show customers are supported by sellers. Your checkout page URL must start with `https://` rather than `http://` for your integration to work. You can test your integration without HTTPS, but you must [enable it](https://docs.stripe.com/security/guide.md#tls) before you accept live payments.

### Set up Stripe.js

The Payment Element is automatically available in Stripe.js. Include the Stripe.js script on your checkout page by adding it to the `head` of your HTML file. Always load Stripe.js directly from `js.stripe.com` to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

```html
<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/dahlia/stripe.js"></script>
</head>
```

Create a `Stripe` instance with the following JavaScript on your checkout page.

```javascript
// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe("<<YOUR_PUBLISHABLE_KEY>>");
```

### Add the Payment Element to your checkout page

> #### Conflicting iframes
>
> Don’t place the Payment Element inside another `iframe` because it conflicts with payment methods that require a redirect to another page for payment confirmation.

The Payment Element needs a container on your checkout page. Create an empty DOM node with a unique ID in your payment form.

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

After your form loads, create an `Elements` instance with `mode`, `amount`, `currency`, and `paymentMethodCreation`. Specify `sellerDetails` and pass the seller’s `networkBusinessProfile` to make sure that Stripe displays the payment methods that the seller supports. This lets you support a different set of payment methods from the seller while showing the buyer compatible payment methods.

Then, create a Payment Element instance and mount it to the container DOM node.

```javascript
const options = {
  mode: "payment",
  amount: 1000,
  currency: "usd",
  paymentMethodCreation: "manual",
  sellerDetails: {
    networkBusinessProfile: "profile_123",
  },
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

### Collect addresses

By default, the Payment Element only collects the necessary billing address details. Some behavior, such as [calculating tax](https://docs.stripe.com/api/tax/calculations/create.md) or entering shipping details, requires your customer’s full address. You can:

- Use the [Address Element](https://docs.stripe.com/elements/address-element.md) to take advantage of autocomplete and localization features to collect your customer’s full address. This helps ensure the most accurate tax calculation.
- Collect address details using your own custom form.

### Create the PaymentMethod

When the customer submits your payment form, create a `PaymentMethod` and send it to your server to create an SPT.

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

  // Create the PaymentMethod using the details collected by the Payment Element
  const { error, paymentMethod } = await stripe.preparePaymentMethod({
    elements,
    params: {
      billing_details: {
        name: "Jenny Rosen",
      },
    },
  });

  if (error) {
    // This point is only reached if there's an immediate error when
    // creating the PaymentMethod. Show the error to your customer (for example, payment details incomplete)
    handleError(error);
    return;
  }

  // Create the Shared Payment Token
  const res = await fetch("/create-spt", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      paymentMethodId: paymentMethod.id,
    }),
  });

  const data = await res.json();

  // Handle any next actions or errors. See the Handle any next actions step for implementation.
  handleServerResponse(data);
});
```

## Issue a shared payment token to a seller

As the agent, create a `SharedPaymentIssuedToken` for the transaction using your customer’s payment method and the seller’s Stripe profile. Set limits such as currency, maximum amount, and expiration window for use. This request returns a `SharedPaymentToken` ID that you share with the seller for payment processing.

Pass the seller’s `network_business_profile` in `seller_details` to make sure the SPT is granted to the correct party. In test mode, you can use `profile_test_61TU90nIeGjU7NNVXA6TU90m7ISQWsBxpcx9lASWWXTk` as a test seller profile.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const issuedToken = await stripe.sharedPayment.issuedTokens.create({
  payment_method: "pm_1RgaZbFPC5QUO6ZCe2ekOCNX",
  seller_details: {
    network_business_profile:
      "profile_test_61TU90nIeGjU7NNVXA6TU90m7ISQWsBxpcx9lASWWXTk",
  },
  usage_limits: {
    currency: "usd",
    expires_at: 1751587220,
    max_amount: 1000,
  },
  return_url: "http://example.com/agent-checkout/return",
});
```

### Supported payment methods

| Payment method                                                 | Availability    |
| -------------------------------------------------------------- | --------------- |
| [Cards](https://docs.stripe.com/payments/cards/overview.md)    | ✓ Supported 1   |
| [Link](https://docs.stripe.com/payments/wallets/link.md)       | ✓ Supported     |
| [Apple Pay](https://docs.stripe.com/apple-pay.md)              | ✓ Supported     |
| [Google Pay](https://docs.stripe.com/google-pay.md)            | ✓ Supported     |
| [Klarna](https://docs.stripe.com/payments/klarna.md)           | ✓ Supported     |
| [Affirm](https://docs.stripe.com/payments/affirm.md) (limited) | ✓ Supported 2,3 |

1 In collaboration with the card networks, Stripe might use tokens issued through network programs such as Mastercard’s Agent Pay and Visa’s Intelligent Commerce programs on your behalf. Stripe submits the requested data to the card networks to provision and process those tokens for related transactions. 2 An agent might not programmatically interact with the Affirm loan application UI inside the webview; the buyer must be the one navigating and confirming. It also might not render the Affirm checkout in a browser on the device over which the agent doesn’t have navigation control. 3 If an agent markets Affirm to customers, the agent must comply with Affirm’s [marketing compliance guides](https://docs.affirm.com/developers/docs/compliance_and_guidelines) and use the Affirm [guide](https://businesshub.affirm.com/hc/en-us/articles/10653174159636-Affirm-Marketing-Compliance-Guides) that relates to the Affirm payment options you display to your customers.

### Handle next actions

A `SharedPaymentToken` can transition to the `requires_action` state when a payment created by the seller needs additional customer action before it can complete. If the payment requires additional customer action, such as 3D Secure authentication or a redirect for a local payment method, you must handle that action. For card payments, Stripe might trigger 3D Secure automatically in these cases:

- Industry guidelines require it.
- The issuer requests it.
- Seller requests it while using the `SharedPaymentToken` to process a `PaymentIntent`.
- Certain Stripe optimizations apply.

When Stripe triggers 3D Secure, Stripe redirects the customer to the bank’s user interface. When the SPT transitions to `requires_action`, Stripe sends the `shared_payment.issued_token.requires_action` webhook. Retrieve the SPT on your server.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const issuedToken = await stripe.sharedPayment.issuedTokens.retrieve("spt_123");
```

```
{
  "id": "spt_123",
  "object": "shared_payment.issued_token",
  "status": "requires_action",
  "next_action": {
    "type": "use_stripe_sdk",
    "use_stripe_sdk": {
      "value": "ewogICJ0eXBlIjogInN0cmlwZV8zZHN 2X2ZpbmdlcnByaW50IiwKICAic291cmNlIjogInNyY18xQThYeUwyZVp2S1lsbzJDOXhROXpSNXQiLAogICJvbmVfY2xpY2tfYXV0aCI6IHRydWUKfQ=="
    }
  }
  ...
}
```

On your client, display the next action flow. Stripe automatically displays the authentication user interface in a pop-up modal when you call `handleNextAction`.

#### JavaScript

```javascript
const handleServerResponse = async (response) => {
  if (response.error) {
    // Show error from server on payment form
  } else if (response.status === "requires_action") {
    // Use Stripe.js to handle the required next action
    const result = await stripe.handleNextAction({
      hashedValue: response.next_action.use_stripe_sdk.value
    });

    const actionError = result && (result as any).error;

    if (actionError) {
      // Show error from Stripe.js in payment form
    } else {
      // Actions handled, show success message
    }
  } else {
    // No actions needed, show success message
  }
}
```

After the customer completes the required action, Stripe sends the `shared_payment.issued_token.active` webhook unless you deactivated the `SharedPaymentToken` in the meantime.

### Revoke a SPT

As the agent, you can revoke the SPT at any time. Revocation prevents the seller from using it to create a payment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const issuedToken = await stripe.sharedPayment.issuedTokens.revoke("spt_123");
```

### Listen for webhook events

We send events to you and the seller when:

- Sellers use a granted SPT to accept a payment.
- You revoke an SPT. Sellers can’t create a payment with a revoked SPT.

| Event                                         | Description                                                                                   | Use case                                                                                                                                               |
| --------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `shared_payment.issued_token.requires_action` | The SPT requires additional customer action before the seller can complete the payment.       | You listen for this event to retrieve the SPT, inspect `next_action`, and present the required authentication or redirect flow on the agent interface. |
| `shared_payment.issued_token.active`          | The customer completed the required action and the SPT can continue through the payment flow. | You listen for this event to know the SPT is usable again after the required action completes.                                                         |
| `shared_payment.issued_token.used`            | You receive this event when the seller uses the SPT.                                          | You listen for this event to notify the customer that the payment has been processed.                                                                  |
| `shared_payment.issued_token.deactivated`     | The SPT has been deactivated (revoked or expired).                                            | You listen for this event to track when the SPT is no longer valid.                                                                                    |
