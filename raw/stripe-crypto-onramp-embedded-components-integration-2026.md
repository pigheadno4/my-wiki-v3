<!-- Source URL: https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide -->
<!-- Fetched: 2026-05-11 -->

# Integrate the Embedded Components onramp

Step-by-step integration guide for the Embedded Components onramp.

# Web

> This is a Web for when platform is web. View the full page at https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide?platform=web.

This guide provides step-by-step instructions for you to build your integration. Use this when you need full control over the onramp flow, want to understand each API, or want to customize the flow for your website. Alternatively, see the [quickstart](https://docs.stripe.com/crypto/onramp/embedded-components-quickstart.md) for a minimal example that shows the full flow.

## Before you begin

- The Embedded Components onramp is only available to users in the US (excluding New York).
- The Embedded Components API is in private preview. No API calls succeed until onboarding is complete, including in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes). To request access:
  1. [Submit your application](https://docs.stripe.com/crypto/onramp.md#submit-your-application).
  1. [Sign up to join the waitlist](https://docs.stripe.com/crypto/onramp.md#sign-up).
  1. Work with your Stripe account executive or solutions architect to complete onboarding before you start your integration. This includes, but isn’t limited to:
     - Confirm that your account is enrolled in the required feature gates for the Embedded Components onramp APIs and Link OAuth APIs.
     - Enable Link as a payment method in your [Dashboard](https://dashboard.stripe.com/settings/payment_methods).
     - Obtain your OAuth client ID and client secret. Stripe provisions these credentials, and you need them for the [authentication flow](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#authentication).
- After onboarding is complete, obtain your secret key and [publishable API key](https://docs.stripe.com/keys.md#obtain-api-keys) from the [API keys page](https://dashboard.stripe.com/apikeys).

## SDK configuration

### Step 1: Install the Stripe Crypto SDK

```shell
npm install @stripe/crypto
```

Or with yarn:

```shell
yarn add @stripe/crypto
```

### Step 2: Load and initialize the SDK (Client-side)

Call `loadCryptoOnrampAndInitialize` with your publishable key and optional configuration to initialize the SDK. You can customize the appearance (for example, colors) so the minimal Stripe UI matches your website.

```javascript
import { loadCryptoOnrampAndInitialize } from "@stripe/crypto";

const onramp = await loadCryptoOnrampAndInitialize("pk_test_...", {
  theme: "stripe",
});
```

## Authentication

### Step 1: Check for a Link account (Server-side)

The customer must have a [Link](https://link.com) account to use the onramp APIs. Create a `LinkAuthIntent` to determine if the customer’s email is associated with an existing Link account.

- If they have an account, proceed to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).
- If they don’t, use [Register a new Link user](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-register-a-new-link-user-if-needed), then proceed to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).

A `LinkAuthIntent` tracks scopes of the OAuth requests and the status of user consent. Your back end calls the [Create a LinkAuthIntent](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#create-a-linkauthintent) API with your `OAUTH_CLIENT_ID` and the onramp OAuth scopes. LinkAuthIntent returns an `authIntentId`, which your back end can share with your client application.

#### Client-side

```javascript
const response = await fetch("/create-link-auth-intent", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ email: email }),
});

if (response.ok) {
  // Successfully created a LinkAuthIntent, proceed to Authorize
}

if (response.status === 404) {
  // Request to POST https://login.link.com/v1/link_auth_intent returned a 404 response
  // There isn't an existing Link account associated with the email
  // Handle registering a new Link User
}
```

#### Server-side

```javascript
app.post("/create-link-auth-intent", async (req, res) => {
  const { email } = req.body;
  const linkRes = await fetch("https://login.link.com/v1/link_auth_intent", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}`,
    },
    body: JSON.stringify({
      email,
      oauth_scopes: process.env.LINK_OAUTH_SCOPES,
      oauth_client_id: process.env.LINK_OAUTH_CLIENT_ID,
    }),
  });
  const data = await linkRes.json();
  if (data.id) {
    res.json({ authIntentId: data.id });
  } else {
    res.status(linkRes.status).json(data);
  }
});
```

### Step 2: Register a new Link user (if needed) (Client-side)

If the customer doesn’t have a Link account, use `registerLinkUser` to create one with the customer information collected from your UI. Upon successful account creation, proceed to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).

```javascript
const userInfo = {
  email: "user@example.com",
  phone: "+12125551234", // E.164 formatted phone number
  country: "US",
  fullName: "John Smith",
};
const registerResult = await onramp.registerLinkUser(userInfo);
if (registerResult.created) {
  // Proceed to authorization.
}
```

### Step 3: Authorize (Client-side)

Call the `authenticate` SDK method, passing the LinkAuthIntent Id and a callback to start the authentication flow. Your callback is called when the user completes authentication. If the user successfully authenticates, the callback parameter contains `crypto_customer_id`. The `crypto_customer_id` is a unique identifier for the user that you need to [Create Onramp Session](https://docs.stripe.com/api/crypto/onramp_sessions/create.md) later.

`authenticate` returns an HTMLElement. Present this to the user to have them authenticate. We recommend presenting this to them as a modal.

If authentication isn’t required, your callback is called immediately. Don’t present the HTMLElement to the user in this case.

```javascript
const authenticationElement = await onramp.authenticate(
  linkAuthIntentId,
  async (result) => {
    if (result.result === "success") {
      if (result.crypto_customer_id) {
        // The user successfully authenticated
        // persist their crypto_customer_id in your backend, you will need it later to onramp
      }
    } else if (result.result === "abandoned") {
      // The user cancelled. Dismiss and let them try again
    } else if (result.result === "declined") {
      // The user declined the OAuth Consent Screen. Explain they need to consent to continue, or let them try again
    }
  },
);
// `authenticate` returns a Promise<HTMLElement>
// Render this in your UI, we recommend presenting this in a modal
document
  .getElementById("auth-container")
  .replaceChildren(authenticationElement);
```

#### Request access tokens

After the user authenticates, your back end calls the [Retrieve Access Tokens](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#retrieve-access-tokens) API to request access tokens. Store the access token and use it on all subsequent onramp API requests (for example, in the `Stripe-OAuth-Token` header).

```javascript
async function exchangeTokens(authIntentId) {
  const res = await fetch(
    `https://login.link.com/v1/link_auth_intent/${authIntentId}/tokens`,
    {
      method: "POST",
      headers: { Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}` },
    },
  );
  const data = await res.json();
  if (!data.access_token) throw new Error("Token exchange failed");
  const oauthToken = data.access_token;
  return oauthToken;
}
```

## Identity

For details on KYC tiers and their identity requirements, see the [KYC integration guide](https://docs.stripe.com/crypto/onramp/kyc-integration-guide.md).

### Step 1: Check if KYC collection is needed (Server-side)

Your back end calls the [Retrieve a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) API with the `customerId`. Inspect the response `verifications` array. If it includes an entry with type `kyc_verified` and status `not_started`, proceed to [Collect KYC](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-collect-kyc-if-needed).

### View example

```javascript
async function getCryptoCustomer(req, res) {
  const { id } = req.params;
  const response = await fetch(
    `https://api.stripe.com/v1/crypto/customers/${id}`,
    {
      headers: {
        Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}`,
        "Stripe-OAuth-Token": oauthToken,
        "Stripe-Version": "2026-03-25.dahlia;crypto_onramp_beta=v2",
      },
    },
  );

  const customer = await response.json();

  const verifications = customer.verifications ?? [];
  const kycVerified = verifications.find((v) => v.name === "kyc_verified");
  const idDocVerified = verifications.find(
    (v) => v.name === "id_document_verified",
  );

  res.json({
    customerId: customer.id,
    providedFields: customer.provided_fields ?? [],
    kycStatus: kycVerified?.status ?? "not_started",
    idDocStatus: idDocVerified?.status ?? "not_started",
  });
}
```

### Step 2: Collect KYC (if needed) (Client-side)

If the customer needs KYC verification, your client calls `submitKycInfo` to collect and submit user KYC data. Present your own interface to the user to collect this KYC information.

```javascript
const kycInfo = {
  given_name: "John",
  surname: "Smith",
  id_number: {
    value: "000000000", // Full ID number — for US, only SSN is currently supported.
    type: "us_ssn",
  },
  date_of_birth: {
    // Object with numeric fields, not a date string.
    day: 1, // Day of month (1-31).
    month: 1, // Month of year (1-12).
    year: 1990, // Full 4-digit year.
  },
  address: {
    line1: "123 Main St",
    line2: "Apt 4B",
    city: "San Francisco",
    state: "CA",
    postal_code: "94111",
    country: "US",
  },
};

try {
  await onramp.submitKycInfo(kycInfo);
} catch (e) {
  // Handle KYC Submission Errors
}
```

### Step 3: Verify identity (if needed) (Client-side)

Some users must verify their identity before continuing with checkout. When required, use the `verifyDocuments` method. It presents a Stripe-hosted flow where the user uploads an identity document and a selfie.

Verification is asynchronous. After the user completes the flow, your back end can call the [Retrieve a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) API and inspect the verifications array to see the results.

```javascript
const result = await onramp.verifyDocuments();

if (result === "abandoned") {
  // User canceled. Dismiss and let them try again.
} else {
  // Identity verified. Proceed to payment flow (register wallet, collect payment method).
}
```

## Payment

### Step 1: Register a crypto wallet (Client-side) (Server-side)

All wallet addresses must be registered to the user’s account before you can onramp to it. Your back end can call the [List ConsumerWallets](https://docs.stripe.com/api/crypto/consumer_wallets/list.md) API to see whether the user already has wallets on file.

If the list is empty or the user wants to add another address, have the client call `registerWalletAddress` with the user’s chosen address and network. You can reuse a previously registered wallet in future sessions. For all valid network values, see [Network](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#supported-networks-and-currencies).

#### List ConsumerWallets

```javascript
const response = await fetch(
  `https://api.stripe.com/v1/crypto/customers/${req.params.id}/crypto_consumer_wallets`,
  {
    headers: {
      Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}`,
      "Stripe-OAuth-Token": oauthToken,
      "Stripe-Version": "2026-03-25.dahlia;crypto_onramp_beta=v2",
    },
  },
);
const data = await response.json();
```

#### Register a wallet

```javascript
try {
  const result = await onramp.registerWalletAddress("3CgQg…", "solana");
} catch {
  // Registration failed
}
```

### Step 2: Collect a payment method (Client-side) (Server-side)

You must first collect a payment method before a transaction can occur. Your back end can call the [List PaymentTokens](https://docs.stripe.com/api/crypto/payment_tokens/list.md) API to see which payment methods the user already has. If the list is empty or the user wants to use a different method, have the client call `collectPaymentMethod`.

Cards and bank accounts are supported. `collectPaymentMethod` presents the Stripe wallet user interface, which lists existing stored payment methods, allows the user to add new ones, or select one. Upon successful payment method selection, it returns a result with a `displayData` property (icon, label, sublabel) that you can use in your UI to show the selected payment method.

#### List PaymentTokens

```javascript
const response = await fetch(
  `https://api.stripe.com/v1/crypto/customers/${req.params.id}/payment_tokens`,
  {
    headers: {
      Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}`,
      "Stripe-OAuth-Token": oauthToken,
      "Stripe-Version": "2026-03-25.dahlia;crypto_onramp_beta=v2",
    },
  },
);
const data = await response.json();
```

#### Collect a payment method

```javascript
try {
  const result = await onramp.collectPaymentMethod(
    {
      payment_method_types: ["card"],
      wallets: { applePay: "auto", googlePay: "auto" },
    },
    (result) => {
      const cryptoPaymentToken = result.cryptoPaymentToken; // Use this crypto payment token when Creating an Onramp Session
    },
  );
} catch {
  // Payment collection failed
}
```

### Step 3: Create a crypto onramp session (Server-side)

From your UI, determine the amount, source currency (for example, `usd`), destination currency (for example, `usdc`), and network. Your back end calls the [Create a CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/create.md) API to create a [CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/object.md). The example below shows how a client application might call your back end. Adapt it to your use case.

#### Client-side

```javascript
// createOnrampSession is a client-side function you must implement.
// Call your back end to create a CryptoOnrampSession using the API.
const result = await createOnrampSession({
  uiMode: "headless",
  cryptoCustomerId,
  cryptoPaymentToken,
  sourceAmount: 100.0, // Pass source_amount OR destination_amount, not both.
  sourceCurrency: "usd",
  destinationCurrency: "usdc",
  destinationNetwork: "solana", // Singular: pins the transaction to this network.
  destinationNetworks: ["solana"], // Array: must be set when walletAddress is set.
  walletAddress,
  customerIpAddress,
});

if (result.success) {
  const sessionId = result.data.id;
  // Call performCheckout with sessionId.
} else {
  // Creation failed. Show error and let the user retry.
}
```

#### Server-side

```javascript
app.post("/create-onramp-session", async (req, res) => {
  const {
    authIntentId,
    crypto_customer_id,
    payment_token,
    source_amount,
    source_currency,
    destination_currency,
    destination_network,
    wallet_address,
  } = req.body;

  const params = new URLSearchParams({
    ui_mode: "headless",
    crypto_customer_id,
    payment_token,
    source_amount: String(source_amount),
    source_currency,
    destination_currency,
    "destination_currencies[]": destination_currency,
    destination_network,
    "destination_networks[]": destination_network,
    wallet_address,
    customer_ip_address: req.socket.remoteAddress,
  });

  const stripeRes = await fetch(
    "https://api.stripe.com/v1/crypto/onramp_sessions",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}`,
        "Stripe-OAuth-Token": oauthToken,
        "Stripe-Version": "2026-03-25.dahlia;crypto_onramp_beta=v2",
      },
      body: params,
    },
  );
  const data = await stripeRes.json();
  if (data.id) {
    res.json({ id: data.id, quote_expires_at: data.quote?.expires_at });
  } else {
    res.status(stripeRes.status).json(data);
  }
});
```

### Step 4: Perform checkout (Client-side) (Server-side)

Call `performCheckout` to run the checkout flow for a crypto onramp session. It handles any required actions such as 3DS in the browser.

You must implement the client-side callback, which the SDK invokes to retrieve the checkout client secret. Have it call your back end, which calls the [onramp session checkout endpoint](https://docs.stripe.com/api/crypto/onramp_sessions/checkout.md) with the session ID. The response includes the `client_secret`, which your callback returns to the SDK.

For users paying with ACH, you also need to pass `mandate_data` and collect the user’s ip address and user agent.

#### Client-side

```javascript
const result = await onramp.performCheckout(
  sessionId,
  async (onrampSessionId) => {
    // Your backend calls POST /v1/crypto/onramp_sessions/{sessionId}/checkout.
    // Return the client secret from your backend response.
    const { client_secret } = await fetch(`/checkout/${onrampSessionId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    }).then((r) => r.json());
    return client_secret;
  },
);

if (result.successful) {
  // Purchase complete. Show success and that crypto was sent to their wallet.
}
```

#### Server-side

```javascript
app.post("/checkout/:sessionId", async (req, res) => {
  const stripeRes = await fetch(
    `https://api.stripe.com/v1/crypto/onramp_sessions/${req.params.sessionId}/checkout`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}`,
        "Stripe-OAuth-Token": oauthToken,
        "Stripe-Version": "2026-03-25.dahlia;crypto_onramp_beta=v2",
      },
      // pass mandate_data if the user is paying with ACH
      body: new URLSearchParams({
        "mandate_data[customer_acceptance][type]": "online",
        "mandate_data[customer_acceptance][accepted_at]": String(
          Math.floor(Date.now() / 1000),
        ),
        "mandate_data[customer_acceptance][online][ip_address]":
          req.ip || req.socket.remoteAddress,
        "mandate_data[customer_acceptance][online][user_agent]":
          req.headers["user-agent"],
      }),
    },
  );
  const data = await stripeRes.json();
  res.status(stripeRes.status).json({ client_secret: data.client_secret });
});
```

When the API returns 200 or 202 but the purchase isn’t done, the response body includes the [CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions.md) object with `transaction_details.last_error` set. Use that value to decide the next step:

| **last_error**                  | **Description**                                                 | **How to handle**                                                                                                  |
| ------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `action_required`               | The user must complete a payment step (for example, 3D Secure). | The SDK handles 3DS in the browser. After the user completes the step, call checkout again.                        |
| `missing_kyc`                   | KYC verification is required.                                   | Have the user complete KYC with `submitKycInfo`. Then call checkout again.                                         |
| `missing_document_verification` | Identity document verification is required.                     | Have the user complete verification with `verifyDocuments`. Then call checkout again.                              |
| `charged_with_expired_quote`    | Quote expired.                                                  | Call [Refresh a Quote](https://docs.stripe.com/api/crypto/onramp_sessions/quote.md) API, then call checkout again. |
| `transaction_limit_reached`     | User’s limit exceeded.                                          | Display an error message.                                                                                          |
| `location_not_supported`        | User’s location isn’t supported.                                | Show that the service isn’t available in their region.                                                             |
| `transaction_failed`            | Generic failure.                                                | Display a generic error message.                                                                                   |
| `missing_consumer_wallet`       | The wallet address doesn’t exist for the current user.          | Have the user register the wallet, then call checkout again.                                                       |

The following pseudocode shows how to handle these cases in a retry loop:

```javascript
async function handleCheckout() {
  // Step 1: Create a new session on your backend before starting checkout.
  let sessionId = await createSessionOnBackend();

  for (let attempt = 0; attempt < 5; attempt++) {
    try {
      const result = await onramp.performCheckout(sessionId, async (onrampSessionId: string) => {
        // Your backend calls POST /v1/crypto/onramp_sessions/{sessionId}/checkout.
        // Return the client secret from your backend response.
        const { client_secret } = await fetch(`/checkout/${onrampSessionId}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
        }).then(r => r.json());
        return client_secret;
      });

      if (result.successful) {
        // Purchase complete.
        return;
      }
    } catch {
       // Step 2: Inspect last_error from the session to decide the next action.
      const session = await fetchSessionFromBackend(sessionId);
      const lastError = session.transaction_details?.last_error;

      if (lastError === 'missing_kyc') {
        // Prompt user to provide KYC info, then retry checkout on the same session.
        await onramp.submitKycInfo({ given_name, surname, id_number, date_of_birth, address });
      } else if (lastError === 'missing_document_verification') {
        // Prompt user to complete identity verification, then retry on the same session.
        await onramp.verifyDocuments();
      } else if (lastError === 'missing_consumer_wallet') {
        // Prompt user to register a wallet, then retry on the same session.
        await onramp.registerWalletAddress(walletAddress, network);
      } else if (lastError === 'charged_with_expired_quote') {
        // Quote expired. Refresh the quote on your backend, then retry checkout on the same session.
        await refreshQuoteOnBackend(sessionId);
      } else {
        // Terminal errors: transaction_limit_reached, location_not_supported, transaction_failed.
        // Do not retry. Show an appropriate error message.
        showError(lastError);
        return;
      }
    }
  }
}
```

## SDK reference

### loadCryptoOnrampAndInitialize(publishableKey, options)

Loads and initializes the SDK. Returns a configured `OnrampCoordinator` instance.

| Parameter        | Type                      | Required | Description                  |
| ---------------- | ------------------------- | -------- | ---------------------------- |
| `publishableKey` | string                    | Yes      | Your Stripe publishable key. |
| `options`        | `CryptoOnrampInitOptions` | No       | SDK configuration options.   |

**`CryptoOnrampInitOptions`**

| Property | Type       | Required  | Description |
| -------- | ---------- | --------- | ----------- | --- | --------------------------------------------- |
| `theme`  | `'stripe'` | `'night'` | `'flat'`    | Yes | Visual theme for Stripe-provided UI elements. |

Returns: `Promise<OnrampCoordinator>`

### OnrampCoordinator

#### registerLinkUser(email, phone, country, fullName?)

Creates a new Link account for the user.

| Parameter  | Type   | Required | Description                                                           |
| ---------- | ------ | -------- | --------------------------------------------------------------------- |
| `email`    | string | Yes      | The user’s email address.                                             |
| `phone`    | string | Yes      | The user’s phone number in E.164 format, for example, `+12125551234`. |
| `country`  | string | Yes      | Two-letter ISO country code, for example, `US`.                       |
| `fullName` | string | No       | The user’s full name.                                                 |

Returns: `Promise<RegisterLinkUserResult>`

| Property  | Type    | Description                               |
| --------- | ------- | ----------------------------------------- |
| `created` | boolean | `true` if a new Link account was created. |

#### authenticate(linkAuthIntentId, onCompletion)

Presents the OTP consent screen. Calls `onCompletion` when the user completes, abandons, or declines the flow.

| Parameter          | Type                                     | Required | Description                                                                                                                                               |
| ------------------ | ---------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `linkAuthIntentId` | string                                   | Yes      | The `id` returned from [Create a LinkAuthIntent](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#create-a-linkauthintent). |
| `onCompletion`     | `(result: AuthenticationResult) => void` | Yes      | Callback invoked when the flow completes.                                                                                                                 |

**`AuthenticationResult`**

| Property             | Type        | Description                                                                    |
| -------------------- | ----------- | ------------------------------------------------------------------------------ | ------------ | ----------------------------------- |
| `result`             | `'success'` | `'abandoned'`                                                                  | `'declined'` | Outcome of the authentication flow. |
| `crypto_customer_id` | string      | Present when `result` is `'success'`. Use for all subsequent onramp API calls. |

Returns: `Promise<HTMLElement | null>`

#### submitKycInfo(params)

Submits KYC information for the user.

| Parameter | Type      | Required | Description                                                                                                                 |
| --------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------- |
| `params`  | `KycInfo` | Yes      | KYC data to submit. See [KycInfo](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#kyc-info). |

Returns: `Promise<void>`

#### registerWalletAddress(walletAddress, network)

Registers a wallet address for the user on the given network.

| Parameter       | Type            | Required | Description                                                                                                                                                 |
| --------------- | --------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `walletAddress` | string          | Yes      | The user’s crypto wallet address.                                                                                                                           |
| `network`       | `CryptoNetwork` | Yes      | The blockchain network for this wallet. See [CryptoNetwork](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#crypto-network). |

Returns: `Promise<CryptoConsumerWallet>`

| Property         | Type                       | Description                                   |
| ---------------- | -------------------------- | --------------------------------------------- |
| `id`             | string                     | Unique identifier for the wallet.             |
| `object`         | `'crypto.consumer_wallet'` | Object type. Always `crypto.consumer_wallet`. |
| `wallet_address` | string                     | The registered wallet address.                |
| `network`        | string                     | The blockchain network.                       |

#### deleteWalletAddress(walletId)

Removes a previously registered wallet address.

| Parameter  | Type   | Required | Description                                    |
| ---------- | ------ | -------- | ---------------------------------------------- |
| `walletId` | string | Yes      | The `id` from a `CryptoConsumerWallet` object. |

Returns: `Promise<void>`

#### collectPaymentMethod(options, onCompletion)

Presents the Stripe wallet UI for selecting a payment method.

| Parameter      | Type                                                         | Required | Description                                              |
| -------------- | ------------------------------------------------------------ | -------- | -------------------------------------------------------- |
| `options`      | `CollectPaymentMethodOptions`                                | Yes      | Payment method configuration.                            |
| `onCompletion` | `(request: CollectPaymentMethodOnCompletionRequest) => void` | Yes      | Callback invoked when the user selects a payment method. |

**`CollectPaymentMethodOptions`**

| Property               | Type     | Required  | Description                                            |
| ---------------------- | -------- | --------- | ------------------------------------------------------ | -------------------------------------------------------------------------- |
| `payment_method_types` | string[] | Yes       | Allowed payment method types, for example, `['card']`. |
| `wallets.applePay`     | `'auto'` | `'never'` | Yes                                                    | Whether to show Apple Pay. `'auto'` shows it when the device supports it.  |
| `wallets.googlePay`    | `'auto'` | `'never'` | Yes                                                    | Whether to show Google Pay. `'auto'` shows it when the device supports it. |

**`CollectPaymentMethodOnCompletionRequest`**

| Property             | Type   | Description                                                 |
| -------------------- | ------ | ----------------------------------------------------------- |
| `cryptoPaymentToken` | string | The payment token to pass when creating the onramp session. |

Returns: `Promise<HTMLElement>`

#### verifyDocuments()

Presents the Stripe-hosted identity document verification flow.

Returns: `Promise<DocumentVerificationResult>`

| Property | Type        | Description   |
| -------- | ----------- | ------------- | ------------------------------------------ |
| `result` | `'success'` | `'abandoned'` | Outcome of the document verification flow. |

#### performCheckout(onrampSessionId, checkout)

Runs the checkout flow for an onramp session, handling any required payment actions such as 3DS in the browser.

| Parameter         | Type                                           | Required | Description                                                                 |
| ----------------- | ---------------------------------------------- | -------- | --------------------------------------------------------------------------- |
| `onrampSessionId` | string                                         | Yes      | The `id` of the `CryptoOnrampSession` to check out.                         |
| `checkout`        | `(onrampSessionId: string) => Promise<string>` | Yes      | Callback that calls your back end to retrieve the checkout `client_secret`. |

Returns: `Promise<CheckoutResult>`

| Property     | Type    | Description                                      |
| ------------ | ------- | ------------------------------------------------ |
| `successful` | boolean | `true` when the purchase completed successfully. |

#### destroy()

Destroys the `OnrampCoordinator` instance and cleans up all associated resources.

Returns: `void`

### Types

#### KycInfo

| Property        | Type          | Required | Description                                                                                                                                |
| --------------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `given_name`    | string        | No       | The user’s given name.                                                                                                                     |
| `surname`       | string        | No       | The user’s surname.                                                                                                                        |
| `address`       | `Address`     | No       | The user’s address. See [Address](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#address).                 |
| `id_number`     | `IdNumber`    | No       | Government-issued ID number. See [IdNumber](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#id-number).     |
| `date_of_birth` | `DateOfBirth` | No       | The user’s date of birth. See [DateOfBirth](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#date-of-birth). |
| `nationalities` | string[]      | No       | ISO country codes for the user’s nationalities, for example, `['US']`.                                                                     |
| `birth_country` | string        | No       | ISO country code of the user’s birth country.                                                                                              |
| `birth_city`    | string        | No       | The user’s city of birth.                                                                                                                  |

#### Address

| Property      | Type   | Required | Description                                           |
| ------------- | ------ | -------- | ----------------------------------------------------- |
| `country`     | string | Yes      | Two-letter ISO country code, for example, `US`.       |
| `city`        | string | No       | City, district, suburb, town, or village.             |
| `line1`       | string | No       | Address line 1 (street address or PO box).            |
| `line2`       | string | No       | Address line 2 (apartment, suite, unit, or building). |
| `postal_code` | string | No       | ZIP or postal code.                                   |
| `state`       | string | No       | State, county, province, or region.                   |
| `town`        | string | No       | Town.                                                 |

#### IdNumber

| Property | Type       | Required | Description                                             |
| -------- | ---------- | -------- | ------------------------------------------------------- |
| `type`   | `'us_ssn'` | Yes      | ID number type. Currently only `'us_ssn'` is supported. |
| `value`  | string     | Yes      | The ID number value.                                    |

#### DateOfBirth

| Property | Type   | Required | Description                                |
| -------- | ------ | -------- | ------------------------------------------ |
| `day`    | number | Yes      | Day of the month (1–31).                   |
| `month`  | number | Yes      | Month of the year (1–12).                  |
| `year`   | number | Yes      | Full four-digit year, for example, `1990`. |

#### CryptoNetwork

| Value          | Network     |
| -------------- | ----------- |
| `'bitcoin'`    | Bitcoin     |
| `'ethereum'`   | Ethereum    |
| `'solana'`     | Solana      |
| `'polygon'`    | Polygon     |
| `'stellar'`    | Stellar     |
| `'avalanche'`  | Avalanche   |
| `'base'`       | Base        |
| `'aptos'`      | Aptos       |
| `'optimism'`   | Optimism    |
| `'worldchain'` | World Chain |
| `'xrpl'`       | XRP Ledger  |
| `'sui'`        | Sui         |
| `'tempo'`      | Tempo       |

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide?platform=react-native.

This guide provides step-by-step instructions for you to build your integration. Use this when you need full control over the onramp flow, want to understand each API, or want to customize the flow for your app. Alternatively, see the [quickstart](https://docs.stripe.com/crypto/onramp/embedded-components-quickstart.md) for a minimal example that shows the full flow, or explore the [example app](https://github.com/stripe-samples/crypto-embedded-components-onramp?platform=react-native) for a complete React Native project that demonstrates the full crypto purchase flow.

## Before you begin

- The Embedded Components onramp is only available to users in the US (excluding New York).
- The Embedded Components API is in private preview. No API calls succeed until onboarding is complete, including in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes). To request access:
  1. [Submit your application](https://docs.stripe.com/crypto/onramp.md#submit-your-application).
  1. [Sign up to join the waitlist](https://docs.stripe.com/crypto/onramp.md#sign-up).
  1. Work with your Stripe account executive or solutions architect to complete onboarding before you start your integration. This includes, but isn’t limited to:
     - Confirm that your account is enrolled in the required feature gates for the Embedded Components onramp APIs and Link OAuth APIs.
     - Enable Link as a payment method in your [Dashboard](https://dashboard.stripe.com/settings/payment_methods).
     - Obtain your OAuth client ID and client secret. Stripe provisions these credentials, and you need them for the [authentication flow](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#authentication).

     - Confirm that your app is registered as a trusted application. We require this before you can use the SDK, including for simulator testing.

- After onboarding is complete, obtain your secret key and [publishable API key](https://docs.stripe.com/keys.md#obtain-api-keys) from the [API keys page](https://dashboard.stripe.com/apikeys).

## Mobile SDK configuration

### Step 1: Install the Stripe React Native SDK

For Expo projects, run the following to automatically install the version compatible with your Expo SDK:

```shell
npx expo install @stripe/stripe-react-native
```

For bare React Native projects, follow the installation instructions in the [README](https://github.com/stripe/stripe-react-native?tab=readme-ov-file). See the [requirements section](https://github.com/stripe/stripe-react-native?tab=readme-ov-file#requirements) for the minimum compatible Expo SDK, React Native, iOS, and Android versions.

### Step 2: Add the onramp dependency (Client-side)

By default, the onramp dependency isn’t included in the Stripe React Native SDK to reduce bundle size. Include it as follows, depending on your platform.

#### Bare React Native App

```shell
# android/gradle.properties
StripeSdk_includeOnramp=true

# ios/Podfile – add pod
pod 'stripe-react-native/Onramp', path: '../node_modules/@stripe/stripe-react-native'
```

#### Expo

```javascript
// [Expo] Add `"includeOnramp": true` (default false)
{
  "expo": {
    ...
    "plugins": [
      [
        "@stripe/stripe-react-native",
        {
          "merchantIdentifier": string | string [],
          "enableGooglePay": boolean,
          "includeOnramp": boolean
        }
      ]
    ]
  }
}
```

```shell
# Add Expo BuildProperties (https://docs.expo.dev/versions/latest/sdk/build-properties/)
npx expo install expo-build-properties
```

If you’re testing on a physical device, install [expo-dev-client](https://docs.expo.dev/versions/latest/sdk/dev-client/) to avoid Metro bundler connection issues:

```shell
npx expo install expo-dev-client
```

### Step 3: Use StripeProvider (Client-side)

Wrap your app with [StripeProvider](https://stripe.dev/stripe-react-native/api-reference/functions/StripeProvider.html) at a high level so Stripe functionality is available throughout your component tree. Key properties:

- `publishableKey`: Your Stripe publishable key.
- `merchantIdentifier`: Your Apple Merchant ID (required for Apple Pay).
- `urlScheme`: Required for return URLs in authentication flows.

You need this component to initialize the Stripe SDK in your React Native application before using payment-related features.

```javascript
import { StripeProvider } from "@stripe/stripe-react-native";

function App() {
  return (
    <StripeProvider
      publishableKey="pk_test_..."
      merchantIdentifier="merchant.identifier"
      urlScheme="your-url-scheme"
    >
      {/* Your app components */}
    </StripeProvider>
  );
}
```

### Step 4: Configure the onramp SDK (Client-side)

Before you can successfully call any onramp APIs, you need to configure the SDK using the `configure` method. It’s provided by the [useOnramp()](https://stripe.dev/stripe-react-native/api-reference/functions/useOnramp.html) hook. The `configure` method takes an instance of [Onramp.Configuration](https://stripe.dev/stripe-react-native/api-reference/types/Onramp.Configuration.html) to customize your business display name and lightly customize elements in Stripe-provided interfaces, such as the user’s wallet, one-time passcode authorization, and identity verification UI.

```javascript
import { useOnramp } from "@stripe/stripe-react-native";

function OnrampComponent() {
  const { configure } = useOnramp();

  React.useEffect(() => {
    const setupOnramp = async () => {
      const result = await configure({
        merchantDisplayName: "My Crypto App",
        appearance: {
          lightColors: {
            primary: "#2d22a1",
            contentOnPrimary: "#ffffff",
            borderSelected: "#07b8b8",
          },
          darkColors: {
            primary: "#800080",
            contentOnPrimary: "#ffffff",
            borderSelected: "#526f3e",
          },
          style: "ALWAYS_DARK",
          primaryButton: { cornerRadius: 8, height: 48 },
        },
      });

      if (result.error) {
        console.error("Configuration failed:", result.error.message);
      }
    };
    setupOnramp();
  }, [configure]);

  return null;
}
```

## Authentication

### Step 1: Check for a Link account (Client-side)

The customer must have a [Link](https://link.com) account to use the onramp APIs. Use `hasLinkAccount` to determine if the customer’s email is associated with an existing Link account. See the [HasLinkAccountResult](https://stripe.dev/stripe-react-native/api-reference/types/Onramp.HasLinkAccountResult.html) for the return type and the [OnrampError](https://stripe.dev/stripe-react-native/api-reference/enums/OnrampError.html) for the error type.

- If they have an account, proceed to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).
- If they don’t, use [Register a new Link user](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-register-a-new-link-user-if-needed), then proceed to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).

```jsx
const { hasLinkAccount, registerLinkUser, authorize } = useOnramp();

const linkResult = await hasLinkAccount("user@example.com");
if (linkResult.error) return;

if (linkResult.hasLinkAccount) {
  // Proceed to authorization.
} else {
  // Register the user first (see next step).
}
```

### View example

```javascript
function AuthComponent() {
  const { hasLinkAccount, registerLinkUser } = useOnramp();

  const handleAuth = async () => {
    const linkResult = await hasLinkAccount("user@example.com");

    if (linkResult.error) {
      // Lookup failed. Show linkResult.error.message and stop.
      return;
    }

    if (linkResult.hasLinkAccount) {
      // User has Link account. Proceed to authorization.
    } else {
      const userInfo = {
        email: "user@example.com",
        phone: "+12125551234",
        country: "US",
        fullName: "John Smith",
      };

      const registerResult = await registerLinkUser(userInfo);

      if (registerResult.error) {
        // Registration failed. Show registerResult.error.message and let the user fix the data.
      } else if (registerResult.customerId) {
        // User registered. Proceed to authorization.
      }
    }
  };

  return <Button title="Authenticate" onPress={handleAuth} />;
}
```

### Step 2: Register a new Link user (if needed) (Client-side)

If the customer doesn’t have a Link account, use `registerLinkUser` to create one with the customer information collected from your UI. Upon successful account creation, proceed to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize). See the [RegisterLinkUserResult](https://stripe.dev/stripe-react-native/api-reference/types/Onramp.RegisterLinkUserResult.html) for the return type and the [OnrampError](https://stripe.dev/stripe-react-native/api-reference/enums/OnrampError.html) for the error type.

```jsx
const userInfo = {
  email: "user@example.com",
  phone: "+12125551234",
  country: "US",
  fullName: "John Smith",
};
const registerResult = await registerLinkUser(userInfo);
if (registerResult.error) return;
if (registerResult.customerId) {
  // Proceed to authorization.
}
```

### Step 3: Authorize (Client-side) (Server-side)

The primary method of authentication is through two-factor authorization.

#### Create a LinkAuthIntent

A `LinkAuthIntent` tracks scopes of the OAuth requests and the status of user consent. Your back end calls the [Create a LinkAuthIntent](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#create-a-linkauthintent) API with your `OAUTH_CLIENT_ID` and the onramp OAuth scopes. LinkAuthIntent will return a `authIntentId`, which your back end can share with your client application.

#### Client-side

```jsx
// createAuthIntent is a client-side function you must implement.
// Call your back end to create a LinkAuthIntent using the API.
const authIntentResponse = await createAuthIntent(
  email,
  // This is your OAUTH_CLIENT_ID, which identifies your application in the Link OAuth flow.
  authToken,
  "kyc.status:read,crypto:ramp",
);
const authIntentId = authIntentResponse.data.authIntentId;
```

#### Server-side

```shell
curl -X POST  https://login.link.com/v1/link_auth_intent \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "oauth_client_id": "$OAUTH_CLIENT_ID", "oauth_scopes": "kyc.status:read,crypto:ramp"}'

# Response
{
  "id": "lai_xxxx",
  "expires_at": 1756238966
}
```

#### User consents

The client calls `authorize` with the `authIntentId` to complete consent. The `authorize` SDK looks up and verifies the user’s Link session, shows them what your app is requesting (the OAuth scopes) on a consent screen or inline on the OTP screen, and collects their approval.

The SDK then sends that consent to Stripe so your backend can exchange the intent for an access token and finish the flow. The result includes a `customerId` that must be used for all subsequent onramp API calls. See the [AuthorizeResult](https://stripe.dev/stripe-react-native/api-reference/types/Onramp.AuthorizeResult.html) for the return type and the [OnrampError](https://stripe.dev/stripe-react-native/api-reference/enums/OnrampError.html) for the error type.

```jsx
const result = await authorize(authIntentId);

if (result?.error) {
  // Error occurred. Show result.error.message and stop.
} else if (result?.status === "Consented" && result.customerId) {
  // User consented. Call your backend to exchange for access token, then proceed to identity flow.
} else if (result?.status === "Denied") {
  // User denied. Explain they need to consent to continue, or let them try again.
} else {
  // User canceled. Dismiss and let them try again.
}
```

#### Request access tokens

If the result is `Consented`, your backend calls the [Retrieve Access Tokens](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#retrieve-access-tokens) API to request access tokens. Store the access token and use it on all subsequent onramp API requests (for example, in the `Stripe-OAuth-Token` header).

```shell
# Request
curl -X POST https://login.link.com/v1/link_auth_intent/{authIntentId}/tokens \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY"

# Response
{
  "access_token": "liwltoken_xxx",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh": {
    "refresh_token": "liwlrefresh_xxx",
    "expires_in": 7776000
  }
}
```

## Identity

For details on KYC tiers and their identity requirements, see the [KYC integration guide](https://docs.stripe.com/crypto/onramp/kyc-integration-guide.md).

### Step 1: Check if KYC collection is needed (Server-side)

Your back end calls the [Retrieve a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) API with the `customerId`. Inspect the response `verifications` array. If it includes an entry with type `kyc_verified` and status `not_started`, proceed to [Collect KYC](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-collect-kyc-if-needed).

```shell
curl https://api.stripe.com/v1/crypto/customers/{customerId} \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

### View example

```javascript
async function getCryptoCustomer(req, res) {
  const { id } = req.params;
  const oauthToken = req.headers["stripe-oauth-token"];

  const response = await fetch(
    `https://api.stripe.com/v1/crypto/customers/${id}`,
    {
      headers: {
        Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}`,
        "Stripe-OAuth-Token": oauthToken ?? "",
      },
    },
  );

  const customer = await response.json();

  const verifications = customer.verifications ?? [];
  const kycVerified = verifications.find((v) => v.name === "kyc_verified");
  const idDocVerified = verifications.find(
    (v) => v.name === "id_document_verified",
  );

  res.json({
    customerId: customer.id,
    providedFields: customer.provided_fields ?? [],
    kycStatus: kycVerified?.status ?? "not_started",
    idDocStatus: idDocVerified?.status ?? "not_started",
  });
}
```

### Step 2: Collect KYC (if needed) (Client-side)

If the customer needs KYC verification, your client calls `attachKycInfo` to collect and submit user KYC data. Present your own interface to the user to collect this KYC information. See [KycInfo](https://stripe.dev/stripe-react-native/api-reference/types/Onramp.KycInfo.html) for the full parameter type and the [OnrampError](https://stripe.dev/stripe-react-native/api-reference/enums/OnrampError.html) for the error type.

```jsx
import { useOnramp } from "@stripe/stripe-react-native";

function AttachKYCComponent() {
  const { attachKycInfo } = useOnramp();

  const handleAttachKycInfo = async () => {
    const kycInfo = {
      firstName: "FirstName",
      lastName: "LastName",
      idNumber: "000000000", // Full ID number — for US, only SSN is currently supported.
      dateOfBirth: {
        // Object with numeric fields, not a date string.
        day: 1, // Day of month (1-31).
        month: 1, // Month of year (1-12).
        year: 1990, // Full 4-digit year.
      },
      address: {
        line1: "123 Main St",
        line2: "Apt 4B",
        city: "San Francisco",
        state: "CA",
        postalCode: "94111",
        country: "US",
      },
    };

    const result = await attachKycInfo(kycInfo);

    if (result?.error) {
      // KYC failed to attach. Show result.error.message and let the user fix the data or retry.
    } else {
      // KYC attached. Proceed to identity verification (if needed) or payment flow.
    }
  };

  return <Button title="Attach KYC" onPress={handleAttachKycInfo} />;
}
```

### Step 3: Verify KYC and update address (if needed) (Client-side)

When a user already has KYC information, use `presentKycInfoVerification` to let them review and update it. This method presents a Stripe-hosted screen showing the user’s existing KYC data. See the [VerifyKycResult](https://stripe.dev/stripe-react-native/api-reference/types/Onramp.VerifyKycResult.html) for the return type and the [OnrampError](https://stripe.dev/stripe-react-native/api-reference/enums/OnrampError.html) for the error type.

> Only address updates are currently supported. Other KYC fields can’t be modified.

The typical flow is:

1. Call `presentKycInfoVerification(null)` to show existing KYC data. The SDK returns `Confirmed` if the user accepts, or `UpdateAddress` if they want to edit their address.
1. If the result status is `UpdateAddress`, show your address form to collect a new address.
1. Call `presentKycInfoVerification(updatedAddress)` with the new address to submit and verify it.
1. If the result status is `Confirmed`, the address is updated.

```jsx
import { useOnramp } from "@stripe/stripe-react-native";

function VerifyKYCComponent() {
  const { presentKycInfoVerification } = useOnramp();

  const handlePresentKycVerification = async () => {
    // Step 1: Show existing KYC data for review.
    const reviewResult = await presentKycInfoVerification(null);

    if (reviewResult?.error) {
      // Verification failed or user canceled.
      return;
    }

    if (reviewResult?.status === "Confirmed") {
      // User confirmed existing data. Proceed to identity verification (if needed) or payment flow.
      return;
    }

    if (reviewResult?.status === "UpdateAddress") {
      // Step 2: User wants to edit their address. Show your address form and collect input.
      const updatedAddress = await collectAddressFromUser();

      // Step 3: Submit the updated address.
      const updateResult = await presentKycInfoVerification({
        line1: updatedAddress.line1,
        line2: updatedAddress.line2,
        city: updatedAddress.city,
        state: updatedAddress.state,
        postalCode: updatedAddress.postalCode,
        country: updatedAddress.country,
      });

      if (updateResult?.error) {
        // Update failed. Show updateResult.error.message and let the user retry.
      } else if (updateResult?.status === "Confirmed") {
        // Address updated. Proceed to identity verification (if needed) or payment flow.
      }
    }
  };

  return <Button title="Verify KYC" onPress={handlePresentKycVerification} />;
}
```

### Step 4: Verify identity (if needed) (Client-side)

Some users must verify their identity before continuing with checkout. When required, use the `verifyIdentity` method. It presents a Stripe-hosted flow where the user uploads an identity document and a selfie.

Verification is asynchronous. After the user completes the flow, your backend can call the [Retrieve a CryptoCustomer](https://docs.stripe.com/api/crypto/customers/retrieve.md) API and inspect the verifications array to see the results.

On Android, the Stripe Identity SDK requires the app’s theme to extend `Theme.MaterialComponents`. For example, Expo defaults to `Theme.AppCompat`, so you need a config plugin to change the theme.

```jsx
import { useOnramp } from "@stripe/stripe-react-native";

function VerifyIdentityComponent() {
  const { verifyIdentity } = useOnramp();

  const handleVerifyIdentity = async () => {
    const result = await verifyIdentity();

    if (result?.error?.code === "Canceled") {
      // User canceled. Dismiss and let them try again.
    } else if (result?.error) {
      // Verification failed. Show result.error.message and let the user retry.
    } else {
      // Identity verified. Proceed to payment flow (register wallet, collect payment method).
    }
  };

  return <Button title="Verify Identity" onPress={handleVerifyIdentity} />;
}
```

## Payment

### Step 1: Register a crypto wallet (Client-side) (Server-side)

A [ConsumerWallet](https://docs.stripe.com/api/crypto/consumer_wallets/object.md) must be registered before you can create a [PaymentToken](https://docs.stripe.com/api/crypto/payment_tokens/list.md). This validates that the address is valid for the given network. Your back end can call the [List ConsumerWallets](https://docs.stripe.com/api/crypto/consumer_wallets/list.md) API to see whether the user already has wallets on file.

If the list is empty or the user wants to add another address, have the client call `registerWalletAddress` with the user’s chosen address and network. Replace the address and network with user-provided values. You can use a previously registered wallet in future sessions. For all valid network values, see [Network](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#supported-networks-and-currencies).

#### List ConsumerWallets

```shell
curl "https://api.stripe.com/v1/crypto/customers/{customerId}/crypto_consumer_wallets" \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

#### Register a wallet

```jsx
import { useOnramp } from "@stripe/stripe-react-native";
function RegisterWalletComponent() {
  const { registerWalletAddress } = useOnramp();

  const handleRegisterWallet = async () => {
    const result = await registerWalletAddress(
      "0x000…",
      Onramp.CryptoNetwork.ethereum,
    );

    if (result?.error) {
      // Registration failed. Show result.error.message and let the user retry with a different address.
    } else {
      // Wallet registered. Proceed to collect payment method.
    }
  };

  return <Button title="Register Wallet" onPress={handleRegisterWallet} />;
}
```

### Step 2: Collect a payment method (Client-side) (Server-side)

You must first collect a payment method before a transaction can occur. Your back end can call the [List PaymentTokens](https://docs.stripe.com/api/crypto/payment_tokens/list.md) API to see which payment methods the user already has. If the list is empty or the user wants to use a different method, have the client call `collectPaymentMethod`.

Card, Bank Account, Apple Pay, and Google Pay are supported. For Card and Bank Account, `collectPaymentMethod` presents Stripe’s wallet user interface, which lists existing stored payment methods, allows the user to add new ones, and select one. Upon successful payment method selection, it returns an instance of [CollectPaymentMethodResult](https://stripe.dev/stripe-react-native/api-reference/types/Onramp.CollectPaymentMethodResult.html), which includes a `displayData` property (icon, label, sublabel) that you can use in your UI to show the selected payment method.

#### List PaymentTokens

```shell
curl https://api.stripe.com/v1/crypto/customers/{customerId}/payment_tokens \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

#### Collect a payment method

```jsx
import { useOnramp } from "@stripe/stripe-react-native";

function CollectPaymentMethodComponent() {
  const { collectPaymentMethod } = useOnramp();

  const handleCollectPaymentMethod = async () => {
    const result = await collectPaymentMethod("Card");

    if (result?.error) {
      // Collection failed. Show result.error.message and let the user retry.
    } else if (result?.displayData) {
      // Payment method selected. Use result.displayData in your UI, then call createCryptoPaymentToken.
    } else {
      // User canceled. Dismiss and let them try again.
    }
  };

  return (
    <Button
      title="Collect Payment Method"
      onPress={handleCollectPaymentMethod}
    />
  );
}
```

#### Collect Apple Pay

To collect Apple Pay, first check [isPlatformPaySupported](https://stripe.dev/stripe-react-native/api-reference/functions/isPlatformPaySupported.html) in [useStripe()](https://stripe.dev/stripe-react-native/api-reference/functions/useStripe.html). See [Apple Pay on React Native](https://docs.stripe.com/apple-pay.md?platform=react-native#check-if-apple-pay-supported). If the user chooses Apple Pay, pass an instance of [PlatformPay.PaymentMethodParams](https://stripe.dev/stripe-react-native/api-reference/types/PlatformPay.PaymentMethodParams.html) into `collectPaymentMethod`.

#### Collect Google Pay

To collect Google Pay, first check [isPlatformPaySupported](https://stripe.dev/stripe-react-native/api-reference/functions/isPlatformPaySupported.html) in [useStripe()](https://stripe.dev/stripe-react-native/api-reference/functions/useStripe.html). See [Google Pay on React Native](https://docs.stripe.com/google-pay.md?platform=react-native#react-native-create-enable-google-pay). If the user chooses Google Pay, pass an instance of [PlatformPay.PaymentMethodParams](https://stripe.dev/stripe-react-native/api-reference/types/PlatformPay.PaymentMethodParams.html) into `collectPaymentMethod`.

### Step 3: Create a payment token (Client-side)

Create a [PaymentToken](https://docs.stripe.com/api/crypto/payment_tokens/list.md) by calling `createCryptoPaymentToken`. Use the returned token when creating the [CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/object.md).

```jsx
import { useOnramp } from "@stripe/stripe-react-native";

function CreatePaymentTokenComponent() {
  const { createCryptoPaymentToken } = useOnramp();

  const handleCreateCryptoPaymentToken = async () => {
    const result = await createCryptoPaymentToken();
    if (result?.error) {
      // Token creation failed. Show result.error.message and let the user retry.
    } else {
      // Token created. Pass result.cryptoPaymentToken to createOnrampSession.
    }
  };

  return (
    <Button
      title="Create Payment Token"
      onPress={handleCreateCryptoPaymentToken}
    />
  );
}
```

### Step 4: Create a crypto onramp session (Server-side)

From your UI, determine the amount, source currency (for example, `usd`), destination currency (for example, `usdc`), and network. Your backend calls the [Create a CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/create.md) API to create a [CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/object.md). The Stripe React Native SDK doesn’t provide APIs for creating a crypto onramp session. It happens on your backend. The example below shows how a client application might call your backend. Adapt it to your use case.

#### Client-side

```jsx
function CreateOnrampSessionComponent() {
  const handleCreateOnrampSession = async () => {
    // createOnrampSession is a client-side function you must implement.
    // Call your back end to create a CryptoOnrampSession using the API.
    const result = await createOnrampSession({
      uiMode: "headless",
      cryptoCustomerId,
      cryptoPaymentToken,
      sourceAmount: 100.0, // Pass source_amount OR destination_amount, not both.
      sourceCurrency: "usd",
      destinationCurrency: "usdc",
      destinationNetwork: Onramp.CryptoNetwork.bitcoin, // Singular: pins the transaction to this network.
      destinationNetworks: [Onramp.CryptoNetwork.bitcoin], // Array: must be set when walletAddress is set.
      walletAddress,
      customerIpAddress,
    });

    if (result.success) {
      const sessionId = result.data.id;
      // Call performCheckout with sessionId.
    } else {
      // Creation failed. Show error and let the user retry.
    }
  };

  return (
    <Button title="Create onramp Session" onPress={handleCreateOnrampSession} />
  );
}
```

#### Server-side

```shell
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN" \
  -d "ui_mode=headless" \
  -d "crypto_customer_id=crc_xxx" \
  -d "payment_token=cpt_xxx" \
  -d "source_amount=100" \              # Pass source_amount OR destination_amount, not both.
  -d "source_currency=usd" \
  -d "destination_currency=usdc" \
  -d "destination_network=base" \       # Singular: pins the transaction to this network.
  -d "destination_networks[]=base" \    # Array: required when wallet_address is set. Must match destination_network.
  -d "wallet_address=0x1234567890abcdef1234567890abcdef12345678" \
  -d "customer_ip_address=203.0.113.1"
```

### Step 5: Perform checkout (Client-side) (Server-side)

Call `performCheckout` to run the checkout flow for a crypto onramp session. It presents a UI for any required actions such as 3DS.

You must implement the client-side callback `fetchClientSecretFromBackend`, which the SDK invokes to retrieve the checkout client secret. Have it call your back end, which calls the [onramp session checkout endpoint](https://docs.stripe.com/api/crypto/onramp_sessions/checkout.md) with the session ID. The response includes the `client_secret`, which your callback can then return to the SDK.

For ACH, the API may indicate that `mandate_data` is missing. Collect acceptance and send it on a later checkout call if required.

#### Client-side

```jsx
import { useOnramp } from "@stripe/stripe-react-native";

function CheckoutComponent() {
  const { performCheckout } = useOnramp();

  const handleCheckout = async () => {
    const result = await performCheckout(sessionId, async () => {
      // fetchClientSecretFromBackend is a client-side function you must implement.
      // It calls your back end, which calls the onramp session checkout endpoint with the session ID
      // and returns the client_secret from the response.
      // Return the client secret on success, or throw an Error on failure.
      const clientSecret = await fetchClientSecretFromBackend(sessionId);
      return clientSecret;
    });

    if (result.error?.code === "Canceled") {
      // User canceled. Dismiss and let them try again.
    } else if (result.error) {
      // Checkout failed. Show result.error.message and let the user retry.
    } else {
      // Purchase complete. Show success and that crypto was sent to their wallet.
    }
  };

  return <Button title="Complete Purchase" onPress={handleCheckout} />;
}
```

#### Server-side

```shell
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions/{sessionId}/checkout \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

When the API returns 200 or 202 but the purchase isn’t done, the response body includes the [CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions.md) object with `transaction_details.last_error` set. Use that value to decide the next step:

| **last_error**                  | **Description**                                             | **How to handle**                                                                                                  |
| ------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `action_required`               | User must complete a payment step (for example, 3D Secure). | Run the SDK’s 3DS handling. After the user completes the step, call checkout again.                                |
| `missing_kyc`                   | KYC verification is required.                               | Have the user complete KYC in the SDK (for example, `attachKycInfo`). Then call checkout again.                    |
| `missing_document_verification` | Identity document verification is required.                 | Have the user complete verification in the SDK (for example, `verifyIdentity`). Then call checkout again.          |
| `charged_with_expired_quote`    | Quote expired.                                              | Call [Refresh a Quote](https://docs.stripe.com/api/crypto/onramp_sessions/quote.md) API, then call checkout again. |
| `transaction_limit_reached`     | User’s limit exceeded.                                      | Display an error message.                                                                                          |
| `location_not_supported`        | User’s location isn’t supported.                            | Show that the service isn’t available in their region.                                                             |
| `transaction_failed`            | Generic failure.                                            | Display a generic error message.                                                                                   |
| `missing_consumer_wallet`       | The wallet address doesn’t exist for the current user.      | Have the user register the wallet, then call checkout again.                                                       |

The following pseudocode shows how to handle these cases in a retry loop:

```jsx
import { useOnramp } from "@stripe/stripe-react-native";

function CheckoutWithRetryComponent() {
  const {
    attachKycInfo,
    verifyIdentity,
    registerWalletAddress,
    performCheckout,
  } = useOnramp();

  const handleCheckout = async () => {
    // Step 1: Create a new session on your backend before starting checkout.
    let sessionId = await createSessionOnBackend();

    for (let attempt = 0; attempt < 5; attempt++) {
      const result = await performCheckout(sessionId, async () => {
        // Your backend calls POST /v1/crypto/onramp_sessions/{sessionId}/checkout.
        // Return { clientSecret, lastError } from your backend response.
        return await fetchClientSecretFromBackend(sessionId);
      });

      if (!result.error) {
        // Purchase complete.
        return;
      }

      if (result.error.code === "Canceled") {
        // User canceled. Stop retrying.
        return;
      }

      // Step 2: Inspect last_error from the session to decide the next action.
      const session = await fetchSessionFromBackend(sessionId);
      const lastError = session.transaction_details?.last_error;

      if (lastError === "missing_kyc") {
        // Prompt user to provide KYC info, then retry checkout on the same session.
        await attachKycInfo({
          firstName,
          lastName,
          idNumber,
          dateOfBirth,
          address,
        });
      } else if (lastError === "missing_document_verification") {
        // Prompt user to complete identity verification, then retry on the same session.
        await verifyIdentity();
      } else if (lastError === "missing_consumer_wallet") {
        // Prompt user to register a wallet, then retry on the same session.
        await registerWalletAddress(walletAddress, network);
      } else if (lastError === "charged_with_expired_quote") {
        // Quote expired. Refresh the quote on your backend, then retry checkout on the same session.
        await refreshQuoteOnBackend(sessionId);
      } else {
        // Terminal errors: transaction_limit_reached, location_not_supported, transaction_failed.
        // Do not retry. Show an appropriate error message.
        showError(lastError);
        return;
      }
    }
  };

  return <Button title="Complete Purchase" onPress={handleCheckout} />;
}
```

## React Native SDK

| SDK method                                  | Presents a UI | What the user sees                                                                                                       |
| ------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `authorize(authIntentId)`                   | Yes           | Link consent screen (or consent inline on OTP screen).                                                                   |
| `attachKycInfo`                             | Optional      | Initial KYC submission only. Collect KYC in your own UI and pass data in. Errors if the user is already verified.        |
| `presentKycInfoVerification`                | Yes           | Review KYC and update addresses for verified users. Pass `null` to review existing data, or an address object to update. |
| `verifyIdentity`                            | Yes           | The Stripe-hosted flow (document + selfie).                                                                              |
| `collectPaymentMethod` (Card / BankAccount) | Yes           | The Stripe wallet UI: list saved methods, add new, choose one.                                                           |
| `performCheckout`                           | Maybe         | Only when needed (for example, 3DS).                                                                                     |
| `registerWalletAddress`                     | No            | No UI. You pass the address and network.                                                                                 |

## Troubleshooting

### App attestation is missing or device can’t use native Link

The Embedded Components onramp SDKs require device attestation to verify that API requests come from a legitimate app. To troubleshoot app attestation errors, check the following:

- Confirm your app is registered as a trusted application with Stripe. Contact your Stripe account executive or solutions architect to register your app. Stripe requires registration for both _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) and live mode. Make sure the bundle identifier on iOS or package name on Android matches the value registered with Stripe.

- Confirm your app includes the App Attest entitlement on iOS. Your app must include the `com.apple.developer.devicecheck.appattest-environment` entitlement.

- Confirm you’re running on a supported device and using a supported distribution method. We support simulators in _sandboxes_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes), but not in live mode. In live mode, use a physical device. On iOS, you can run from Xcode on a physical device, distribute through [TestFlight](https://developer.apple.com/testflight/), or publish to the App Store. When running from Xcode, set `com.apple.developer.devicecheck.appattest-environment` to `production` in your entitlements file, and delete and reinstall the app if you previously used the `development` environment.

- If you’re testing on an Android emulator and see the error `Native Link is not available`, confirm that your emulator uses a system image that includes Google APIs or Google Play. Standard emulator images without Google APIs don’t support the app attestation required by the SDK.

### Unrecognized request URL

If your API calls return a `404` with an `invalid_request_error` and the message `Unrecognized request URL`, your account might not be enrolled in the private preview or might be missing one or more required feature gates.

Contact your Stripe account executive or solutions architect to confirm that your account has access to all required feature gates for the Embedded Components onramp.

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide?platform=android.

This guide explains how to build your integration with the Android Crypto Onramp SDK. Use it when you need full control over the onramp flow, want to understand each API, or want to customize the flow for your app.

## Before you begin

- The Embedded Components onramp is only available to users in the US (excluding New York).
- The Embedded Components API is in private preview. No API calls succeed until onboarding is complete, including in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes). To request access:
  1. [Submit your application](https://docs.stripe.com/crypto/onramp.md#submit-your-application).
  1. [Sign up to join the waitlist](https://docs.stripe.com/crypto/onramp.md#sign-up).
  1. Work with your Stripe account executive or solutions architect to complete onboarding before you start your integration. This includes, but isn’t limited to:
     - Confirm that your account is enrolled in the required feature gates for the Embedded Components onramp APIs and Link OAuth APIs.
     - Enable Link as a payment method in your [Dashboard](https://dashboard.stripe.com/settings/payment_methods).
     - Obtain your OAuth client ID and client secret. Stripe provisions these credentials, and you need them for the [authentication flow](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#authentication).

     - Confirm that your app is registered as a trusted application. We require this before you can use the SDK, including for simulator testing.

- After onboarding is complete, obtain your secret key and [publishable API key](https://docs.stripe.com/keys.md#obtain-api-keys) from the [API keys page](https://dashboard.stripe.com/apikeys).

## Configure the mobile SDK

### Add the onramp dependency (Client-side)

The [Stripe Android SDK](https://github.com/stripe/stripe-android) is open source and [fully documented](https://stripe.dev/stripe-android/index.html). Add `crypto-onramp` to the `dependencies` block of your [app/build.gradle](https://developer.android.com/studio/build/dependencies) file:

```kotlin
dependencies {
    implementation 'com.stripe:crypto-onramp:23.1.0'
}
```

### Opt in to experimental APIs (Client-side)

The SDK is in private preview. You must opt in with the `ExperimentalCryptoOnramp` annotation. Choose one of the following approaches:

#### Per type

```kotlin
@ExperimentalCryptoOnramp
class MyOnrampActivity : AppCompatActivity() {
    // ...
}
```

#### Per file

```kotlin
@file:OptIn(com.stripe.android.crypto.onramp.ExperimentalCryptoOnramp::class)
```

#### Per module

```kotlin
// build.gradle
android {
    kotlin {
        compilerOptions {
            freeCompilerArgs.addAll([
                "-opt-in=com.stripe.android.crypto.onramp.ExperimentalCryptoOnramp",
            ])
        }
    }
}
```

### Create the `OnrampCoordinator` (Client-side)

Create an `OnrampCoordinator` instance to use for all onramp features. Don’t use more than one `OnrampCoordinator` at a time because it relies on a shared internal state.

```kotlin
val onrampCoordinator: OnrampCoordinator =
    OnrampCoordinator
        .Builder()
        .build(application, savedStateHandle, callbacks)
```

### Configure the SDK (Client-side)

Before you call any onramp APIs successfully, configure the SDK with the `configure` function on `OnrampCoordinator`. This lets you customize your business display name and appearance so the minimal Stripe UI matches your app. You can also enable Google Pay as a payment option.

```kotlin
val configuration = OnrampConfiguration()
    .merchantDisplayName(merchantDisplayName = "Onramp Example")
    .publishableKey(publishableKey = "pk_test_key")
    .appearance(
        appearance = LinkAppearance()
            .lightColors(
                LinkAppearance.Colors()
                    .primary(Color(0xFF635BFF))
                    .contentOnPrimary(Color.White)
                    .borderSelected(Color.Black)
            )
            .darkColors(
                LinkAppearance.Colors()
                    .primary(Color(0xFF9886E6))
                    .contentOnPrimary(Color(0xFF222222))
                    .borderSelected(Color.White)
            )
            .style(LinkAppearance.Style.ALWAYS_DARK)
            .primaryButton(LinkAppearance.PrimaryButton())
    )

onrampCoordinator.configure(configuration = configuration)
```

### View Google Pay configuration example

```kotlin
val configuration = OnrampConfiguration()
    .merchantDisplayName(merchantDisplayName = "Onramp Example")
    .publishableKey(publishableKey = "pk_test_key")
    .googlePayConfig(
        GooglePayPaymentMethodLauncher.Config(
            environment = GooglePayEnvironment.Test,
            merchantCountryCode = "US",
            merchantName = "Onramp Example",
            billingAddressConfig = GooglePayPaymentMethodLauncher.BillingAddressConfig(
                isRequired = true,
                format = GooglePayPaymentMethodLauncher.BillingAddressConfig.Format.Full,
                isPhoneNumberRequired = false
            ),
            existingPaymentMethodRequired = false
        )
    )

onrampCoordinator.configure(configuration = configuration)
```

### Create a presenter (Client-side)

For UI-based features such as authorization, identity verification, payment collection, and checkout, create an `OnrampCoordinator.Presenter`:

```kotlin
val onrampPresenter = onrampCoordinator.createPresenter(yourActivity)
```

Make sure that the hosting activity uses a Material theme. In your `app/src/main/AndroidManifest.xml`, set `android:theme` to a child of a Material theme such as `Theme.MaterialComponents.DayNight`. We require this for identity verification.

## Authenticate the user

### Check for a Link account (Client-side)

The user must have a [Link](https://link.com) account to use the onramp APIs. Use `hasLinkAccount` to determine whether the user’s email is associated with an existing Link account.

- If the user has an account, go to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).
- If the user doesn’t have an account, [register a new Link user](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-register-a-new-link-user-if-needed), then go to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).

```kotlin
when (val result = onrampCoordinator.hasLinkAccount(currentEmail)) {
    is OnrampHasLinkAccountResult.Completed -> {
        if (result.hasLinkAccount) {
            // Proceed to authorization.
        } else {
            // Register the user first (see next step).
        }
    }
    is OnrampHasLinkAccountResult.Failed -> {
        // Lookup failed. Inspect result.error and stop.
    }
}
```

### Register a new Link user if needed (Client-side)

If the user doesn’t have a Link account, use `registerLinkUser` to create one with information collected in your UI. After account creation succeeds, go to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).

```kotlin
val userInfo = LinkUserInfo(
    email = "stripe@stripe.com",
    fullName = "Stripe",
    phone = "+17777777777",
    country = "US"
)

when (val result = onrampCoordinator.registerLinkUser(userInfo)) {
    is OnrampRegisterLinkUserResult.Completed -> {
        // Registration successful. Proceed to authorization.
    }
    is OnrampRegisterLinkUserResult.Failed -> {
        // Registration failed. Inspect result.error and let the user fix the data.
    }
}
```

### Authorize (Client-side) (Server-side)

The primary authentication method uses two-factor authorization.

#### Create a `LinkAuthIntent`

A `LinkAuthIntent` tracks the scopes of the OAuth requests and the status of user consent. Your backend calls the Create a LinkAuthIntent API with your `OAUTH_CLIENT_ID` and the onramp OAuth scopes, receives the `authIntentId`, and sends it to the client.

#### Client-side

```kotlin
// createAuthIntent is a client-side function that you implement.
// Call your backend to create a LinkAuthIntent with the API.
val result = clientBackend.createAuthIntentId(oauthScopes, authToken)
val authIntentId = result.linkAuthIntentId
```

#### Server-side

```shell
curl -X POST https://login.link.com/v1/link_auth_intent \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "oauth_client_id": "$OAUTH_CLIENT_ID", "oauth_scopes": "kyc.status:read,crypto:ramp,auth.persist_login:read"}'
```

#### Collect user consent

The client calls `authorize` on `OnrampCoordinator.Presenter` with the `authIntentId` to complete consent. This presents the OTP dialog to authorize the user. Configure the `authenticateUserCallback` as part of `OnrampCallbacks` to handle the result.

```kotlin
// Present the authorization dialog.
onrampPresenter.authorize(authIntentId)
```

```kotlin
// Handle the result via callbacks.
OnrampCallbacks()
    .authenticateUserCallback { result ->
        when (result) {
            is OnrampAuthenticateResult.Completed -> {
                // User consented. Call your backend to exchange for access token.
            }
            is OnrampAuthenticateResult.Cancelled -> {
                // User canceled. Let them try again.
            }
            is OnrampAuthenticateResult.Failed -> {
                // Authentication failed. Inspect result.error.
            }
        }
    }
```

#### Request access tokens

If the result is `Completed`, your back end calls the Retrieve Access Tokens API to request access tokens. Store the access token and use it in all subsequent onramp API requests, for example, in the `Stripe-OAuth-Token` header.

```shell
# Request
curl -X POST https://login.link.com/v1/link_auth_intent/{authIntentId}/tokens \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY"

# Response
{
  "access_token": "liwltoken_xxx",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh": {
    "refresh_token": "liwlrefresh_xxx",
    "expires_in": 7776000
  }
}
```

#### Log out

Call `logOut` when the user logs out of your app to clear all SDK state, including authorization, selected payment method, and crypto payment token.

```kotlin
when (val result = onrampCoordinator.logOut()) {
    is OnrampLogOutResult.Completed -> {
        // Successfully logged out.
    }
    is OnrampLogOutResult.Failed -> {
        // Log out failed. Inspect result.error.
    }
}
```

## Verify identity

For details on KYC tiers and identity requirements, see the [KYC integration guide](https://docs.stripe.com/crypto/onramp/kyc-integration-guide.md).

### Check whether KYC collection is needed (Server-side)

Your back end calls the Retrieve a CryptoCustomer API with the `customerId`. Inspect the `verifications` array in the response. If it includes an entry with type `kyc_verified` and status `not_started`, go to [Collect KYC](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-collect-kyc-if-needed).

```shell
curl https://api.stripe.com/v1/crypto/customers/{customerId} \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

### Collect KYC if needed (Client-side)

If the customer needs KYC verification, call `attachKycInfo` to collect and submit KYC data. Present your own interface to collect this information.

```kotlin
val collectedKycInfo = KycInfo(
    firstName = "FirstName",
    lastName = "LastName",
    idNumber = "000000000",
    dateOfBirth = DateOfBirth(day = 1, month = 1, year = 1990),
    address = Address(
        line1 = "123 Main St",
        line2 = "Apt 4B",
        city = "San Francisco",
        state = "CA",
        postalCode = "94111",
        country = "US"
    )
)

when (val result = onrampCoordinator.attachKycInfo(collectedKycInfo)) {
    is OnrampAttachKycInfoResult.Completed -> {
        // KYC attached. Proceed to identity verification if needed or payment flow.
    }
    is OnrampAttachKycInfoResult.Failed -> {
        // KYC failed to attach. Inspect result.error and let the user fix the data.
    }
}
```

### Verify KYC if needed (Client-side)

When a customer already has KYC information, use `verifyKycInfo` on `OnrampCoordinator.Presenter` so the SDK can present a screen with the customer’s existing KYC information for verification. Configure the `verifyKycCallback` as part of `OnrampCallbacks` to handle the result. If the customer needs to update their address, call `verifyKycInfo` again with the updated address.

```kotlin
// Present the KYC verification screen.
onrampPresenter.verifyKycInfo()
```

```kotlin
// Handle the result via callbacks.
OnrampCallbacks()
    .verifyKycCallback { result ->
        when (result) {
            is OnrampVerifyKycInfoResult.Confirmed -> {
                // KYC verified. Proceed to identity verification or payment flow.
            }
            is OnrampVerifyKycInfoResult.UpdateAddress -> {
                // User needs to update their address.
                // Show your address form, then call verifyKycInfo(updatedAddress).
            }
            is OnrampVerifyKycInfoResult.Cancelled -> {
                // User canceled. Let them try again.
            }
            is OnrampVerifyKycInfoResult.Failed -> {
                // Verification failed. Inspect result.error.
            }
        }
    }
```

### Verify identity if needed (Client-side)

Some customers must verify their identity before they continue to checkout. When required, call `verifyIdentity` on `OnrampCoordinator.Presenter`. It presents a Stripe-hosted flow where the customer uploads an identity document and a selfie.

Verification is asynchronous. After the customer completes the flow, your back end can call the Retrieve a CryptoCustomer API and inspect the `verifications` array to see the result.

```kotlin
onrampPresenter.verifyIdentity()
```

```kotlin
// Handle the result via callbacks.
OnrampCallbacks()
    .verifyIdentityCallback { result ->
        when (result) {
            is OnrampVerifyIdentityResult.Completed -> {
                // Identity verified. Proceed to payment flow.
            }
            is OnrampVerifyIdentityResult.Cancelled -> {
                // User canceled. Let them try again.
            }
            is OnrampVerifyIdentityResult.Failed -> {
                // Verification failed. Inspect result.error.
            }
        }
    }
```

## Collect payment

### Register a crypto wallet (Client-side) (Server-side)

You must register a wallet address before you can create a payment token. This validates that the address is valid for the given network. Your back end can call the List ConsumerWallets API to determine whether the customer already has wallets on file.

If the list is empty or the customer wants to add another address, have the client call `registerWalletAddress` with the customer’s chosen address and network. You can reuse a previously registered wallet in future sessions.

#### List ConsumerWallets

```shell
curl "https://api.stripe.com/v1/crypto/customers/{customerId}/crypto_consumer_wallets" \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

#### Register a wallet

```kotlin
when (val result = onrampCoordinator
                    .registerWalletAddress("address", CryptoNetwork.Bitcoin)) {
    is OnrampRegisterWalletAddressResult.Completed -> {
        // Wallet registered. Proceed to collect payment method.
    }
    is OnrampRegisterWalletAddressResult.Failed -> {
        // Registration failed. Inspect result.error and let the user retry.
    }
}
```

### Collect a payment method (Client-side) (Server-side)

You must collect a payment method before a transaction can occur. Your back end can call the List PaymentTokens API to determine which payment methods the user already has. If the list is empty or the customer wants to use a different method, have the client call `collectPaymentMethod` on `OnrampCoordinator.Presenter`.

We support cards, bank accounts, and Google Pay. For card and bank account, `collectPaymentMethod` presents the Stripe wallet UI, which lists existing stored payment methods, lets the user add new ones, and lets the user select one.

#### List PaymentTokens

```shell
curl https://api.stripe.com/v1/crypto/customers/{customerId}/payment_tokens \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

#### Collect a payment method

```kotlin
onrampPresenter.collectPaymentMethod(PaymentMethodSelection.Card())
```

```kotlin
// Handle the result via callbacks.
OnrampCallbacks()
    .collectPaymentCallback { result ->
        when (result) {
            is OnrampCollectPaymentMethodResult.Completed -> {
                // Payment method selected. Use displayData in your UI,
                // then call createCryptoPaymentToken.
            }
            is OnrampCollectPaymentMethodResult.CompletedWithKycInfo -> {
                // Payment method selected and KYC information was available.
            }
            is OnrampCollectPaymentMethodResult.Cancelled -> {
                // User canceled. Let them try again.
            }
            is OnrampCollectPaymentMethodResult.Failed -> {
                // Collection failed. Inspect result.error.
            }
        }
    }
```

After payment method selection succeeds, the callback returns a `PaymentMethodDisplayData` instance with `icon`, `label`, `type`, and `sublabel` properties that you can use in your UI to show the selected payment method.

### Create a payment token (Client-side)

Create a payment token by calling `createCryptoPaymentToken`. Use the returned token when you create the `CryptoOnrampSession`.

```kotlin
when (val result = onrampCoordinator.createCryptoPaymentToken()) {
    is OnrampCreateCryptoPaymentTokenResult.Completed -> {
        // Token created. Pass the token to createOnrampSession.
    }
    is OnrampCreateCryptoPaymentTokenResult.Failed -> {
        // Token creation failed. Inspect result.error.
    }
}
```

### Create a crypto onramp session (Server-side)

From your UI, determine the amount, source currency such as `usd`, destination currency such as `usdc`, and network. Your back end calls the [Create a CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/create.md) API to create a [CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/object.md). The Android SDK doesn’t provide APIs for session creation. Your back end handles this step. The example shows how a client application might call your back end.

#### Client-side

```kotlin
val result = clientBackend.createOnrampSession(
    paymentToken = paymentToken,
    walletAddress = wallet.address,
    authToken = authToken,
    destinationNetwork = wallet.network
)

when (result) {
    is Result.Success -> {
        // Session created. Use result.sessionId for checkout.
    }
    is Result.Failure -> {
        // Creation failed. Show error and let the user retry.
    }
}
```

#### Server-side

```shell
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN" \
  -d "ui_mode=headless" \
  -d "crypto_customer_id=crc_xxx" \
  -d "payment_token=cpt_xxx" \
  -d "source_amount=100" \              # Pass `source_amount` or `destination_amount`, not both.
  -d "source_currency=usd" \
  -d "destination_currency=usdc" \
  -d "destination_network=base" \       # Singular. Pins the transaction to this network.
  -d "destination_networks[]=base" \    # Array. Required when `wallet_address` is set. Must match `destination_network`.
  -d "wallet_address=0x1234567890abcdef1234567890abcdef12345678" \
  -d "customer_ip_address=203.0.113.1"
```

### Perform checkout (Client-side) (Server-side)

Call `performCheckout` on `OnrampCoordinator.Presenter` to run the checkout flow. It presents a UI for required actions, such as `3DS`.

You must implement the `onrampSessionClientSecretProvider` callback as part of `OnrampCallbacks`. The SDK invokes it to retrieve the checkout client secret. Have it call your back end, which calls the onramp session checkout endpoint with the session ID. The response includes the `client_secret`. This callback might be called more than once during a single checkout.

For ACH, the API may indicate that `mandate_data` is missing. Collect acceptance and send it on a later checkout call if required.

#### Client-side

```kotlin
// Configure the client secret provider in your callbacks.
OnrampCallbacks()
    .onrampSessionClientSecretProvider { sessionId ->
        // Return the client secret for the given sessionId
        // from your backend API.
        return getClientSecretForSessionId(sessionId)
    }
```

```kotlin
// Start checkout.
onrampPresenter.performCheckout(onrampSessionId = sessionId)
```

```kotlin
// Handle the result via callbacks.
OnrampCallbacks()
    .checkoutCallback { result ->
        when (result) {
            is OnrampCheckoutResult.Completed -> {
                // Purchase complete. Show success.
            }
            is OnrampCheckoutResult.Cancelled -> {
                // User canceled. Let them try again.
            }
            is OnrampCheckoutResult.Failed -> {
                // Checkout failed. Inspect result.error.
            }
        }
    }
```

#### Server-side

```shell
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions/{sessionId}/checkout \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

When the API returns `200` or `202` but the purchase isn’t complete, the response body includes the [CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions.md) object with `transaction_details.last_error` set. Use that value to determine the next step:

| `last_error`                    | Description                                               | How to handle                                                                                            |
| ------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `action_required`               | The user must complete a payment step, such as 3D Secure. | Run the SDK’s `3DS` handling. After the user completes the step, call checkout again.                    |
| `missing_kyc`                   | KYC verification is required.                             | Have the user complete KYC in the SDK, for example, `attachKycInfo`. Then call checkout again.           |
| `missing_document_verification` | Identity document verification is required.               | Have the user complete verification in the SDK, for example, `verifyIdentity`. Then call checkout again. |
| `charged_with_expired_quote`    | The quote expired.                                        | Refresh the quote on your back end, then call checkout again.                                            |
| `transaction_limit_reached`     | The user exceeded their limit.                            | Display an error message.                                                                                |
| `location_not_supported`        | We don’t support the user’s location.                     | Show that the service isn’t available in their region.                                                   |
| `transaction_failed`            | A generic failure occurred.                               | Display a generic error message.                                                                         |
| `missing_consumer_wallet`       | The wallet address doesn’t exist for the current user.    | Have the user register the wallet, then call checkout again.                                             |

## Troubleshoot the integration

### Configuration error

| Error                                                                                                     | Cause and fix                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `IllegalArgumentException`: `merchantDisplayName` must not be null and `publishableKey` must not be null. | Both `merchantDisplayName` and `publishableKey` are required on `OnrampConfiguration`. Set both before you call `onrampCoordinator.configure(configuration)`.                                                                                                                              |
| `IllegalArgumentException`: Callback must not be null                                                     | All callbacks on `OnrampCallbacks` are required except `googlePayIsReadyCallback`. Set `verifyIdentityCallback`, `verifyKycCallback`, `collectPaymentCallback`, `authorizeCallback`, `checkoutCallback`, and `onrampSessionClientSecretProvider` before you build the `OnrampCoordinator`. |
| `OnrampConfigurationResult.Failed`                                                                        | The `configure` call can fail if the underlying Link SDK fails to initialize. Inspect the `error` property. A common cause is an invalid publishable key.                                                                                                                                  |

### Authentication error

| Error                                                     | Cause and fix                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MissingConsumerSecretException`: Missing consumer secret | The user’s session wasn’t established or expired. Make sure that the user completed authentication through `authorize` or `authenticateUserWithToken` before you call other APIs. This error can come from `registerLinkUser`, `registerWalletAddress`, `attachKycInfo`, `verifyKycInfo`, and `verifyIdentity`. |
| Link authorization error or forced re-authentication      | If an API call returns an authorization error, the SDK automatically clears the cached Link account state. Subsequent calls fail with `MissingConsumerSecretException`. Re-authenticate the user by calling `authorize` again.                                                                                  |

### Payment error

| Error                                                        | Cause and fix                                                                                                                                                                                                                |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MissingCryptoCustomerException`: Missing crypto customer ID | No crypto customer is associated with the current session. A crypto customer ID is created during `authorize` or `registerLinkUser`. Make sure that one of these calls completed before you call `createCryptoPaymentToken`. |
| `MissingPaymentMethodException`: Missing payment method      | Payment method collection appeared to succeed, but we couldn’t resolve the selected method internally. Retry `collectPaymentMethod`.                                                                                         |

### Checkout error

| Error                                        | Cause and fix                                                                                                                                                                                                                                                                         |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PaymentFailedException`: Payment failed     | The underlying `PaymentIntent` reached a terminal failure state, such as a declined card, processing error, or unresolvable session after process failure. Inspect the error and offer the user an option to retry or select a different payment method.                              |
| `onrampSessionClientSecretProvider` failures | This callback might be called more than once during a single checkout, initially and again after handling a required next action such as `3DS`. Make sure that your back end can handle repeated calls for the same session ID. If this callback results in an error, checkout fails. |

### Identity and KYC error

| Error                                                             | Cause and fix                                                                                                                                                                      |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `OnrampVerifyIdentityResult.Failed` with “No ephemeral key found” | The server responded without an ephemeral key. This usually indicates a back-end configuration issue. Ensure that the user’s account is properly set up for identity verification. |
| `OnrampVerifyKycInfoResult.UpdateAddress`                         | This isn’t an error. The user indicated that their address needs updating. Show your address form, then call `onrampPresenter.verifyKycInfo(updatedAddress)` again.                |

### General guidance

- All `Failed` result types include an `error: Throwable` property. Log or inspect it for detailed diagnostics.
- Only one `OnrampCoordinator` instance can be active at a time. Creating multiple instances can lead to undefined behavior.
- Always call `logOut()` when the user logs out of your app to clean up SDK state and avoid stale session issues.
- When you use a test mode publishable key that contains `test`, the SDK operates against the Stripe test environment. No real transactions are processed, and no actual identity verification occurs.

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide?platform=ios.

This guide explains how to build your integration with the iOS Crypto Onramp SDK. Use it when you need full control over the onramp flow, want to understand each API, or want to customize the flow for your app.

## Before you begin

- The Embedded Components onramp is only available to users in the US (excluding New York).
- The Embedded Components API is in private preview. No API calls succeed until onboarding is complete, including in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes). To request access:
  1. [Submit your application](https://docs.stripe.com/crypto/onramp.md#submit-your-application).
  1. [Sign up to join the waitlist](https://docs.stripe.com/crypto/onramp.md#sign-up).
  1. Work with your Stripe account executive or solutions architect to complete onboarding before you start your integration. This includes, but isn’t limited to:
     - Confirm that your account is enrolled in the required feature gates for the Embedded Components onramp APIs and Link OAuth APIs.
     - Enable Link as a payment method in your [Dashboard](https://dashboard.stripe.com/settings/payment_methods).
     - Obtain your OAuth client ID and client secret. Stripe provisions these credentials, and you need them for the [authentication flow](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#authentication).

     - Confirm that your app is registered as a trusted application. We require this before you can use the SDK, including for simulator testing.

- After onboarding is complete, obtain your secret key and [publishable API key](https://docs.stripe.com/keys.md#obtain-api-keys) from the [API keys page](https://dashboard.stripe.com/apikeys).

## Configure the mobile SDK

### Add the onramp dependency (Client-side)

The [Stripe iOS SDK](https://github.com/stripe/stripe-ios) is open source and [fully documented](https://stripe.dev/stripe-ios/index.html). It supports apps that run iOS 13 or later. Add the `StripeCryptoOnramp` product to your app with your package manager.

#### Swift Package Manager

1. In Xcode, select **File** > **Add Package Dependencies…** and enter **https://github.com/stripe/stripe-ios-spm** as the repository URL.
1. Select the latest version number from the [releases page](https://github.com/stripe/stripe-ios/releases).
1. Add the `StripeCryptoOnramp` product to the [target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

#### CocoaPods

1. If you haven’t already, install the latest version of [CocoaPods](https://guides.cocoapods.org/using/getting-started.html).
1. If you don’t have an existing [Podfile](https://guides.cocoapods.org/syntax/podfile.html), run the following command to create one:

```shell
pod init
```

1. Add this line to your `Podfile`:

```ruby
pod 'StripeCryptoOnramp'
```

1. Run the following command:

```shell
pod install
```

1. Open your project in Xcode with the `.xcworkspace` file instead of the `.xcodeproj` file.
1. To update to the latest version of the SDK later, run:

```shell
pod update StripeCryptoOnramp
```

#### Carthage

1. If you haven’t already, install the latest version of [Carthage](https://github.com/Carthage/Carthage#installing-carthage).
1. Add this line to your `Cartfile`:

```text
github "stripe/stripe-ios"
```

1. Follow the [Carthage installation instructions](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos). Make sure that you embed [all required frameworks](https://github.com/stripe/stripe-ios/tree/master/StripeCryptoOnramp#manual-linking).
1. To update to the latest version of the SDK later, run:

```shell
carthage update stripe-ios --platform ios
```

#### Manual framework

1. Go to the [GitHub releases page](https://github.com/stripe/stripe-ios/releases/latest) and download and unzip `Stripe.xcframework.zip`.
1. Drag `StripeCryptoOnramp.xcframework` to the **Embedded Binaries** section of the **General** settings in your Xcode project. Make sure that you select **Copy items if needed**.
1. Repeat step 2 for all required frameworks listed [here](https://github.com/stripe/stripe-ios/blob/master/StripeCryptoOnramp/README.md#manual-linking).
1. To update to the latest version of the SDK later, repeat steps 1–3.

### Opt in to experimental APIs (Client-side)

The SDK is in private preview. You must opt in with the `@_spi(CryptoOnrampAlpha)` attribute. Mark the `StripeCryptoOnramp` import like this:

```swift
@_spi(CryptoOnrampAlpha) import StripeCryptoOnramp
```

### Configure the SDK (Client-side)

Before you call any onramp APIs, set your publishable key and create a `CryptoOnrampCoordinator` instance. You can also create a `LinkAppearance` instance to customize Stripe-provided UI elements such as one-time passcode entry, payment method selection, and identity verification.

Only one `CryptoOnrampCoordinator` instance can be active at a time because the SDK uses shared internal state.

```swift
STPAPIClient.shared.publishableKey = "pk_test_123"
```

```swift
let appearance = LinkAppearance(
    colors: .init(primary: .systemBlue, selectedBorder: .label),
    primaryButton: .init(cornerRadius: 16, height: 56),
    style: .alwaysDark
)
```

```swift
Task {
    do {
        self.coordinator = try await CryptoOnrampCoordinator.create(appearance: appearance)
        // Coordinator successfully configured.
    } catch {
        // Handle thrown errors.
    }
}
```

## Authenticate the customer

### Check for a Link account (Client-side)

The customer must have a [Link](https://link.com) account to use the onramp APIs. Use `hasLinkAccount(with:)` to determine whether the customer’s email is associated with an existing Link account.

- If the customer has an account, go to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).
- If they don’t have an account, [register a new Link customer](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-register-a-new-link-customer-if-needed), then go to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).

```swift
do {
    if try await coordinator.hasLinkAccount(with: email) {
        // The customer has an account. Proceed to authorization.
    } else {
        // Register the customer first.
    }
} catch {
    // Handle thrown errors.
}
```

### Register a new Link customer if needed (Client-side)

If the customer doesn’t have a Link account, use `registerLinkUser` to create one with information that you collect in your UI. After account creation succeeds, go to [Authorize](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-authorize).

```swift
do {
    try await coordinator.registerLinkUser(
        email: email,
        fullName: fullName,
        phone: phoneNumber,
        country: country
    )
    // The customer is registered. Proceed to authorization.
} catch {
    // Handle thrown errors.
}
```

### Authorize (Client-side) (Server-side)

The primary authentication method uses two-factor authorization.

#### Create a LinkAuthIntent

A `LinkAuthIntent` tracks the scopes of the OAuth requests and the status of customer consent. Your backend calls the Create a LinkAuthIntent API with your `OAUTH_CLIENT_ID` and the onramp OAuth scopes, receives the `authIntentId`, and sends it to the client.

#### Client-side

```swift
// createAuthIntent is a function you implement to call your backend.
let response = try await clientBackend.createAuthIntent(oauthScopes: scopes)
let authIntentId = response.authIntentId
```

#### Server-side

```shell
curl -X POST https://login.link.com/v1/link_auth_intent \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "oauth_client_id": "$OAUTH_CLIENT_ID", "oauth_scopes": "kyc.status:read,crypto:ramp,auth.persist_login:read"}'
```

#### Collect customer consent

Call `authorize(linkAuthIntentId:from:)` on `CryptoOnrampCoordinator` with the `authIntentId` to complete consent. This presents the OTP dialog so the customer can authorize the request.

```swift
do {
    let authResult = try await coordinator.authorize(
        linkAuthIntentId: authIntentId,
        from: presentingViewController
    )
    switch authResult {
    case .denied, .canceled:
        // The customer denied or canceled the authentication flow.
    case let .consented(customerId):
        // The customer successfully authenticated.
        // Proceed to KYC, identity verification, or payment.
        // Store authIntent.token to enable Seamless Sign-In in future sessions.
    }
} catch {
    // Handle thrown errors.
}
```

#### Request access tokens

If the result is `.consented`, your back end calls the Retrieve Access Tokens API to request access tokens. Store the access token and use it in all subsequent onramp API requests, for example, in the `Stripe-OAuth-Token` header.

```shell
# Request
curl -X POST https://login.link.com/v1/link_auth_intent/{authIntentId}/tokens \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY"

# Response
{
  "access_token": "liwltoken_xxx",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh": {
    "refresh_token": "liwlrefresh_xxx",
    "expires_in": 7776000
  }
}
```

### Use Seamless Sign-In for a returning customer (Client-side) (Server-side)

To reduce friction for a returning customer, you can skip the OTP dialog by storing the `LinkAuthIntent` token after a successful `authorize` call and exchanging it for a `linkAuthTokenClientSecret` (LATCS) through your back end in the next session. Pass the LATCS to `authenticateUserWithToken(_:)` to sign in without customer interaction.

If authentication fails, for example because the token expired, clear the stored token and fall back to the standard `hasLinkAccount` and `authorize` flow.

```swift
do {
    let result = try await clientBackend.createLinkAuthToken(storedLAIToken)
    let latcs = result.linkAuthTokenClientSecret
    try await coordinator.authenticateUserWithToken(latcs)
    // The customer successfully authenticated.
} catch {
    // Seamless Sign-In failed. Clear stored tokens and fall back to authorize.
}
```

### Log out (Client-side)

Call `logOut()` when the customer logs out of your app to clear all SDK state, including authorization, the selected payment method, and the crypto payment token. Also clear any locally stored tokens that you use for seamless sign-in.

```swift
do {
    try await coordinator.logOut()
    // The customer successfully logged out.
} catch {
    // Handle thrown errors.
}
```

### View an end-to-end authentication example

The following example shows how to use the authentication APIs together in a complete authentication lifecycle, including seamless sign-in, new and existing customer handling, OTP authorization, and logout.

```swift
@_spi(CryptoOnrampAlpha) import StripeCryptoOnramp
import UIKit

final class OnrampAuthExample {

    private let coordinator: CryptoOnrampCoordinator
    private let backend: MerchantBackend
    private let tokenStore: SeamlessTokenStore

    init(
        coordinator: CryptoOnrampCoordinator,
        backend: MerchantBackend,
        tokenStore: SeamlessTokenStore
    ) {
        self.coordinator = coordinator
        self.backend = backend
        self.tokenStore = tokenStore
    }

    // Call when the customer starts an onramp session.
    func authenticateUserForOnramp() async throws {
        // 1) Try Seamless Sign-In first. This is optional and skips OTP for a returning customer.
        if let storedLAIToken = tokenStore.load() {
            do {
                let latcs = try await backend.createLinkAuthTokenClientSecret(
                    fromStoredLAIToken: storedLAIToken
                )
                try await coordinator.authenticateUserWithToken(latcs)
                return
            } catch {
                // Tokens can expire. Clear and fall back to the standard flow.
                tokenStore.clear()
            }
        }

        // 2) Collect email in your own UI.
        let email = try await promptForEmailFromYourUI()

        // 3) Check for an existing Link account.
        let hasLinkAccount = try await coordinator.hasLinkAccount(with: email)

        if !hasLinkAccount {
            // 4) Collect details and register the customer.
            let reg = try await promptForRegistrationInfoFromYourUI(prefilledEmail: email)
            try await coordinator.registerLinkUser(
                email: reg.email,
                fullName: reg.fullName,
                phone: reg.phoneE164,
                country: reg.country
            )
        }

        // 5) Create a LinkAuthIntent on your backend.
        let authIntent = try await backend.createLinkAuthIntent(
            oauthScopes: Scopes.requiredScopes
        )

        // 6) Present the OTP and consent UI.
        let presentingVC = try presentingViewControllerForOTP()
        let authResult = try await coordinator.authorize(
            linkAuthIntentId: authIntent.authIntentId,
            from: presentingVC
        )

        switch authResult {
        case .consented:
            // Store the token to enable Seamless Sign-In in future sessions.
            tokenStore.save(authIntent.token)
        case .denied:
            throw AuthFlowError.authorizationDenied
        case .canceled:
            throw AuthFlowError.authorizationCanceled
        @unknown default:
            throw AuthFlowError.unknownError
        }
    }

    // Call when the customer logs out of your app.
    func logOutUserFromApp() async {
        do {
            try await coordinator.logOut()
        } catch {
            // Continue with your own logout flow.
        }
        tokenStore.clear()
    }

    // MARK: - Placeholder UI hooks (replace with your app's UI)

    private func promptForEmailFromYourUI() async throws -> String {
        return "user@example.com"
    }

    private func promptForRegistrationInfoFromYourUI(
        prefilledEmail: String
    ) async throws -> RegistrationInput {
        RegistrationInput(
            email: prefilledEmail,
            fullName: "Jane Doe",
            phoneE164: "+12125551234",
            country: "US"
        )
    }

    private func presentingViewControllerForOTP() throws -> UIViewController {
        guard let vc = UIApplication.shared.connectedScenes
            .compactMap({ \$0 as? UIWindowScene })
            .flatMap(\.windows)
            .first(where: \.isKeyWindow)?
            .rootViewController else {
            throw AuthFlowError.noPresentingViewController
        }
        return vc
    }
}

// MARK: - Supporting types

struct RegistrationInput {
    let email: String
    let fullName: String?
    let phoneE164: String
    let country: String
}

protocol MerchantBackend {
    func createLinkAuthIntent(oauthScopes: [Scopes]) async throws -> CreateLinkAuthIntentResponse
    func createLinkAuthTokenClientSecret(fromStoredLAIToken token: String) async throws -> String
}

struct CreateLinkAuthIntentResponse {
    let authIntentId: String
    let token: String
}

protocol SeamlessTokenStore {
    func load() -> String?
    func save(_ token: String)
    func clear()
}

enum AuthFlowError: Error {
    case authorizationDenied
    case authorizationCanceled
    case noPresentingViewController
    case unknownError
}

enum Scopes: String {
    static let requiredScopes: [Scopes] = [.cryptoRamp, .kycStatusRead, .authPersistLoginRead]

    case cryptoRamp = "crypto:ramp"
    case kycStatusRead = "kyc.status:read"
    case authPersistLoginRead = "auth.persist_login:read"
}
```

## Verify identity

For details about KYC tiers and identity requirements, see the [KYC integration guide](https://docs.stripe.com/crypto/onramp/kyc-integration-guide.md).

### Check whether KYC collection is needed (Server-side)

Your back end calls the Retrieve a CryptoCustomer API with the `customerId`. Inspect the `verifications` array in the response. If it includes an entry with type `kyc_verified` and status `not_started`, go to [Collect KYC](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#step-collect-kyc-if-needed).

```shell
curl https://api.stripe.com/v1/crypto/customers/{customerId} \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

### Collect KYC if needed (Client-side)

If the customer needs KYC verification, call `attachKYCInfo(info:)` to collect and submit KYC data. Present your own UI to collect this information.

```swift
let kycInfo = KycInfo(
    firstName: firstName,
    lastName: lastName,
    idNumber: idNumber,
    address: address,
    dateOfBirth: dateOfBirth
)

do {
    try await coordinator.attachKYCInfo(info: kycInfo)
    // KYC attached. Proceed to identity verification if needed, or to payment.
} catch {
    // Handle thrown errors.
}
```

### Verify KYC if needed (Client-side)

When a customer already has KYC information on file, use `verifyKYCInfo(updatedAddress:from:)` to present a Stripe-provided screen where the customer can confirm their existing information. If the customer needs to update their address, call `verifyKYCInfo` again with the updated address.

```swift
do {
    let result = try await coordinator.verifyKYCInfo(
        updatedAddress: nil,
        from: presentingViewController
    )
    switch result {
    case .confirmed:
        // KYC verified. Proceed to identity verification or payment.
    case .updateAddress:
        // The customer wants to update their address.
        // Show your address form, then call verifyKYCInfo(updatedAddress:from:) again.
    case .canceled:
        // The customer dismissed the flow without confirming.
    }
} catch {
    // Handle thrown errors.
}
```

### Verify identity if needed (Client-side)

Some customers must verify their identity before they can complete checkout. When required, call `verifyIdentity(from:)` to present a Stripe-hosted flow where the customer uploads an identity document and a selfie.

Verification is asynchronous. After the customer completes the flow, your back end can call the Retrieve a CryptoCustomer API and inspect the `verifications` array to check the result.

```swift
do {
    let result = try await coordinator.verifyIdentity(from: presentingViewController)
    switch result {
    case .completed:
        // The customer completed identity verification. Proceed to payment.
    case .canceled:
        // The customer canceled the identity verification flow.
    }
} catch {
    // Handle thrown errors.
}
```

## Collect payment

### Register a crypto wallet (Client-side) (Server-side)

You must register a wallet address before you can create a payment token. This validates that the address is valid for the given network. Your back end can call the List ConsumerWallets API to determine whether the customer already has wallets on file.

If the list is empty or the customer wants to add another address, have the client call `registerWalletAddress(walletAddress:network:)` with the customer’s chosen address and network. You can reuse a previously registered wallet in future sessions.

#### List ConsumerWallets

```shell
curl "https://api.stripe.com/v1/crypto/customers/{customerId}/crypto_consumer_wallets" \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

#### Register a wallet

```swift
do {
    try await coordinator.registerWalletAddress(
        walletAddress: "bc1qztnc…",
        network: .bitcoin
    )
    // Wallet registered. Proceed to collect a payment method.
} catch {
    // Handle thrown errors.
}
```

### Collect a payment method (Client-side) (Server-side)

You must collect a payment method before a transaction can occur. Your back end can call the List PaymentTokens API to determine which payment methods the customer already has. If the list is empty or the customer wants to use a different method, have the client call `collectPaymentMethod(type:from:)` on `CryptoOnrampCoordinator`.

We support cards, bank accounts, and Apple Pay. For card and bank account, `collectPaymentMethod` presents the Stripe wallet UI, which lists existing stored payment methods, lets the customer add new ones, and lets the customer select one. After a successful selection, it returns a `PaymentMethodDisplayData` instance with `paymentMethodType`, `icon`, `label`, and `sublabel` properties that you can use in your UI.

#### List PaymentTokens

```shell
curl https://api.stripe.com/v1/crypto/customers/{customerId}/payment_tokens \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

#### Collect a payment method

```swift
do {
    let type = PaymentMethodType.card // or PaymentMethodType.bankAccount
    if let displayData = try await coordinator.collectPaymentMethod(
        type: type,
        from: presentingViewController
    ) {
        // Payment method selected. Optionally use displayData in your UI.
    } else {
        // The customer canceled payment method selection.
    }
} catch {
    // Handle thrown errors.
}
```

#### Apple Pay

To offer Apple Pay, check whether the device supports it with [`StripeAPI.deviceSupportsApplePay()`](<https://stripe.dev/stripe-ios/stripe/documentation/stripe/stripeapi/devicesupportsapplepay()>) before you show the button. For example, in a SwiftUI view:

```swift
if StripeAPI.deviceSupportsApplePay() {
    PayWithApplePayButton(.plain) {
        // Proceed with Apple Pay collection.
    }
}
```

For `PaymentMethodType.applePay`, you must supply a [`PKPaymentRequest`](https://developer.apple.com/documentation/passkit/pkpaymentrequest). You can use the `StripeCore` framework to generate one. The following example creates a payment request with a pending amount because fees aren’t determined until checkout:

```swift
let request = StripeAPI.paymentRequest(
    withMerchantIdentifier: "my_merchant_id",
    country: "US",
    currency: "USD"
)

request.paymentSummaryItems = [
    PKPaymentSummaryItem(
        label: "My Company",
        amount: .zero,
        type: .pending
    )
]
```

When you have the `PKPaymentRequest`, call `collectPaymentMethod` with `PaymentMethodType.applePay` when the customer taps **Apple Pay**:

```swift
do {
    let type = PaymentMethodType.applePay(paymentRequest: request)
    if let displayData = try await coordinator.collectPaymentMethod(
        type: type,
        from: presentingViewController
    ) {
        // Apple Pay payment method selected.
    } else {
        // The customer canceled Apple Pay.
    }
} catch {
    // Handle thrown errors.
}
```

The `CryptoOnrampCoordinator` instance tracks the most recently selected payment method and uses it in the next transaction.

### Create a payment token (Client-side)

Create a payment token for the selected payment method by calling `createCryptoPaymentToken()`. Use the returned token when you create the `CryptoOnrampSession`.

```swift
do {
    let token = try await coordinator.createCryptoPaymentToken()
    // Payment token created. Proceed to session creation and checkout.
} catch {
    // Handle thrown errors.
}
```

### Create a crypto onramp session (Server-side)

From your UI, determine the amount, source currency such as `usd`, destination currency such as `usdc`, and network. Your back end calls the [Create a CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions/create.md) API. The iOS SDK doesn’t provide APIs for session creation. Your back end handles this step. The following example shows how a client application might call your back end.

#### Client-side

```swift
let request = CreateOnrampSessionRequest(
    paymentToken: paymentToken,
    sourceAmount: 100.0,
    sourceCurrency: "usd",
    destinationCurrency: "usdc",
    destinationNetwork: wallet.network,
    walletAddress: wallet.walletAddress
)
do {
    let sessionResponse = try await clientBackend.createOnrampSession(request: request)
    // Session created. Use sessionResponse.sessionId for checkout.
} catch {
    // Handle thrown errors.
}
```

#### Server-side

```shell
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN" \
  -d "ui_mode=headless" \
  -d "crypto_customer_id=crc_xxx" \
  -d "payment_token=cpt_xxx" \
  -d "source_amount=100" \
  -d "source_currency=usd" \
  -d "destination_currency=usdc" \
  -d "destination_network=base" \
  -d "destination_networks[]=base" \
  -d "wallet_address=0x1234567890abcdef1234567890abcdef12345678" \
  -d "customer_ip_address=203.0.113.1"
```

Pass `source_amount` or `destination_amount`, not both. Use the singular `destination_network` to pin the transaction to a network. When you set `wallet_address`, you must also set `destination_networks[]`, and its value must match `destination_network`.

### Perform checkout (Client-side) (Server-side)

To perform checkout, your view controller must conform to [`STPAuthenticationContext`](https://stripe.dev/stripe-ios/stripe/documentation/stripe/stpauthenticationcontext) so the SDK can present authentication challenges:

```swift
extension MyCheckoutViewController: STPAuthenticationContext {
    func authenticationPresentingViewController() -> UIViewController {
        self
    }
}
```

Call `performCheckout(onrampSessionId:authenticationContext:clientSecretProvider:)` with the session ID and a closure that retrieves the checkout client secret from your back end. The closure might be called more than once during a single checkout, for example, after handling a 3D Secure challenge.

For ACH, the API may indicate that `mandate_data` is missing. Collect acceptance and send it on a later checkout call if required.

#### Client-side

```swift
do {
    let checkoutResult = try await coordinator.performCheckout(
        onrampSessionId: sessionResponse.sessionId,
        authenticationContext: presentingViewController
    ) { onrampSessionId in
        let result = try await APIClient.shared.checkout(onrampSessionId: onrampSessionId)
        return result.clientSecret
    }
    switch checkoutResult {
    case .completed:
        // Checkout completed successfully.
    case .canceled:
        // Checkout canceled during an authentication challenge.
    }
} catch {
    // Handle thrown errors.
}
```

#### Server-side

```shell
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions/{sessionId}/checkout \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Stripe-OAuth-Token: $ACCESS_TOKEN"
```

When the API returns `200` or `202` but the purchase isn’t complete, the response body includes the [CryptoOnrampSession](https://docs.stripe.com/api/crypto/onramp_sessions.md) object with `transaction_details.last_error` set. Use that value to determine the next step:

| `last_error`                    | Description                                                   | How to handle                                                                                                |
| ------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `action_required`               | The customer must complete a payment step, such as 3D Secure. | Run the SDK’s 3DS handling. After the customer completes the step, call checkout again.                      |
| `missing_kyc`                   | KYC verification is required.                                 | Have the customer complete KYC in the SDK, for example, `attachKYCInfo`. Then call checkout again.           |
| `missing_document_verification` | Identity document verification is required.                   | Have the customer complete verification in the SDK, for example, `verifyIdentity`. Then call checkout again. |
| `charged_with_expired_quote`    | The quote expired.                                            | Refresh the quote on your back end, then call checkout again.                                                |
| `transaction_limit_reached`     | The customer exceeded their limit.                            | Display an error message.                                                                                    |
| `location_not_supported`        | We don’t support the customer’s location.                     | Show that the service isn’t available in their region.                                                       |
| `transaction_failed`            | A generic failure occurred.                                   | Display a generic error message.                                                                             |
| `missing_consumer_wallet`       | The wallet address doesn’t exist for the current customer.    | Have the customer register the wallet, then call checkout again.                                             |

## Troubleshoot the integration

### Configuration error

| Error                                              | Cause and fix                                                                                                                                                                             |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CryptoOnrampCoordinator.create()` throws an error | The `create()` factory method can fail if the underlying Link SDK fails to initialize. A common cause is an invalid publishable key set on `STPAPIClient`. Inspect the error for details. |

### Authentication error

| Error                                                      | Cause and fix                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LinkController.IntegrationError.noActiveLinkConsumer`     | The customer’s session wasn’t established or expired. Make sure that they completed authentication through `authorize` or `authenticateUserWithToken` before you call other APIs. This error can come from `authenticateUserWithToken`, `registerWalletAddress`, `attachKYCInfo`, `verifyKYCInfo`, `verifyIdentity`, `collectPaymentMethod`, and `createCryptoPaymentToken`. Re-authenticate the customer by calling `authorize` again. |
| `CryptoOnrampCoordinator.Error.seamlessSignInTokenInvalid` | `authenticateUserWithToken` throws this error when the provided token expired, was already used, or was revoked. Fall back to `authorize` to sign in the customer manually and clear any stored tokens.                                                                                                                                                                                                                                 |

### Registration error

| Error                                                    | Cause and fix                                                                                                                                                                                                                            |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CryptoOnrampCoordinator.Error.linkAccountAlreadyExists` | `registerLinkUser` throws this error if the email is already associated with an existing Link account. Use `hasLinkAccount(with:)` to check before you attempt registration, or direct the customer to sign in with `authorize` instead. |
| `CryptoOnrampCoordinator.Error.invalidPhoneFormat`       | `registerLinkUser` throws this error if the phone number isn’t in E.164 format, for example, `+12125551234`. Validate the format before you call this API.                                                                               |

### Payment error

| Error                                                        | Cause and fix                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CryptoOnrampCoordinator.Error.missingCryptoCustomerID`      | `createCryptoPaymentToken` throws this error. A crypto customer ID is created during `authorize`, `authenticateUserWithToken`, or `registerLinkUser`. Make sure that one of these steps completed before you try to create a payment token.                                                                                                                           |
| `CryptoOnrampCoordinator.Error.invalidSelectedPaymentSource` | `createCryptoPaymentToken` throws this error if no payment method has been collected. `collectPaymentMethod` can also throw it if the selected method can’t be resolved internally. Make sure that `collectPaymentMethod` succeeded before you call `createCryptoPaymentToken`. If the error occurs during payment collection, retry the `collectPaymentMethod` call. |
| `CryptoOnrampCoordinator.Error.linkAccountNotVerified`       | `collectPaymentMethod` throws this error for Link payment types (`.card`, `.bankAccount`) when the Link account session isn’t in a verified state. Make sure that the customer’s authentication and verification flow completed before you collect a payment method.                                                                                                  |

### Checkout error

| Error                                | Cause and fix                                                                                                                                                                                                                           |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CheckoutError.paymentFailed`        | The underlying `PaymentIntent` reached a terminal failure state, for example, a declined card, processing error, or failed 3D Secure. Inspect the error and offer the customer an option to retry or select a different payment method. |
| `CheckoutError.missingPaymentMethod` | The `PaymentIntent` doesn’t have an associated payment method. Make sure that a payment method was collected successfully before you initiate checkout.                                                                                 |
| `CheckoutError.unexpectedError`      | A catch-all error for unexpected states during checkout. Log the surrounding context and retry the checkout.                                                                                                                            |

### Identity and KYC error

| Error                                               | Cause and fix                                                                                                                                                                                                                     |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CryptoOnrampCoordinator.Error.missingEphemeralKey` | `verifyIdentity` throws this error when the server responds without an ephemeral key. This usually indicates a back-end configuration issue. Make sure that the customer’s account is set up correctly for identity verification. |
| `VerifyKYCResult.updateAddress`                     | This isn’t an error. When `verifyKYCInfo` returns `.updateAddress`, show your own address form and call `verifyKYCInfo(updatedAddress:from:)` again with the new address.                                                         |

### General guidance

- All errors thrown by `CryptoOnrampCoordinator` APIs conform to `LocalizedError`. Use the `localizedDescription` property for detailed diagnostics.
- Only one `CryptoOnrampCoordinator` instance can be active at a time. Creating multiple instances can lead to undefined behavior.
- Always call `logOut()` when the customer logs out of your app to clean up SDK state and avoid stale session issues.
- When you use a test mode publishable key that contains `test`, the SDK operates against the Stripe test environment. No real transactions are processed, and no actual identity verification occurs.

## Supported networks and currencies

### Livemode

| Currency                      | Network               | Address                                                                            |
| ----------------------------- | --------------------- | ---------------------------------------------------------------------------------- |
| USDC (`usdc`)                 | Solana (`solana`)     | EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v                                       |
| USDC (`usdc`)                 | Base (`base`)         | 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913                                         |
| USDC (`usdc`)                 | Sui (`sui`)           | 0xdba34672e30cb065b1f93e3ab55318768fd6fef66c15942c9f7cb846e2f900e7::usdc::USDC     |
| USDC.e (`usdc`)               | Tempo (`tempo`)       | 0x20c000000000000000000000b9537d11c60e8b50                                         |
| USDC (`usdc`)                 | Ethereum (`ethereum`) | 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48                                         |
| USDB (`usdb`)                 | Solana (`solana`)     | ENL66PGy8d8j5KNqLtCcg4uidDUac5ibt45wbjH9REzB                                       |
| USDsui (`usdsui`)             | Sui (`sui`)           | 0x44f838219cf67b058f3b37907b655f226153c18e33dfcd0da559a844fea9b1c1::usdsui::USDSUI |
| USDC (`usdc`)                 | Arbitrum (`arbitrum`) | 0xaf88d065e77c8cC2239327C5EDb3A432268e5831                                         |
| USDT (`usdt`)                 | Ethereum (`ethereum`) | 0xdac17f958d2ee523a2206206994597c13d831ec7                                         |
| Phantom Cash (`phantom_cash`) | Solana (`solana`)     | CASHx9KJUStyftLFWGvEVf59SGeG9sh5FfcnZMVPCASH                                       |

### Sandbox (test mode)

| Currency      | Network               |
| ------------- | --------------------- |
| USDC (`usdc`) | Solana (`solana`)     |
| USDC (`usdc`) | Ethereum (`ethereum`) |
| USDC (`usdc`) | Base (`base`)         |

## Testing

> You can test your integration in two ways, in a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) using test API keys, or in _live mode_ (Use this mode when you’re ready to launch your app. Card networks or payment providers process payments) using live API keys. Both require your app to be registered as a trusted application with Stripe before any SDK calls succeed, including on a simulator. The OAuth client ID and client secret are the same for both sandboxes and live mode.

### Sandbox testing

Use a _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) to build and verify your integration without real charges or real KYC. Use your `sk_test_...` secret key and `pk_test_...` publishable key.

If you’re testing on an Android emulator, use a system image that includes Google APIs or Google Play to prevent SDK calls from failing because of app attestation errors.

#### Test values

Use the following values when testing each step of the flow in _sandbox_ (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes):

| Step           | Field              | Test value                                            |
| -------------- | ------------------ | ----------------------------------------------------- |
| Authentication | SMS / OTP code     | `000000`                                              |
| KYC            | Name               | `John Verified`                                       |
| KYC            | ID Number (SSN)    | `000000000`                                           |
| KYC            | Address line 1     | `address_full_match`                                  |
| KYC            | State              | Two-letter code (for example, `WA`, not `Washington`) |
| Payment        | Credit card number | `4242 4242 4242 4242`                                 |

#### Identity verification

The identity verification step presents a testmode UI that lets you select the verification outcome directly, without uploading a real document or selfie. This lets you test all verification outcomes (success, failure, and so on) without manual review delays.

### Live mode testing

Live mode testing validates production mode and has stricter requirements than sandbox testing.

#### Requirements

- **Live API keys**: Use your `sk_live_...` secret key and `pk_live_...` publishable key. Test keys don’t work in live mode.
- **Real card charges**: Live mode transactions charge a real payment method. Test card numbers don’t work.
- **Real KYC**: Users must complete real identity verification. Sandbox test values don’t apply in live mode.

- **Physical device**: The SDK requires a physical iOS or Android device. Live mode doesn’t support simulators or emulators. On iOS, you can run your app from Xcode on a physical device or distribute it through [TestFlight](https://developer.apple.com/testflight/). When running from Xcode, set the `com.apple.developer.devicecheck.appattest-environment` entitlement to `production`. If you previously ran with the `development` environment, delete and reinstall the app to clear any cached states.

## LinkAuthIntent APIs

### Create a LinkAuthIntent

Creates a `LinkAuthIntent` to start a [Log in with Link](https://link.com/) flow. Send the OAuth client id and scopes you need. The API returns an intent id and expiration.

To obtain your `OAUTH_CLIENT_ID`, contact your Stripe account executive or solutions architect. Stripe provisions the credential as part of your onboarding.

OAuth scopes used when creating a `LinkAuthIntent`:

| Scope (string)            | Description                                                                |
| ------------------------- | -------------------------------------------------------------------------- |
| `kyc.status:read`         | Read the customer’s KYC verification status.                               |
| `crypto:ramp`             | Add crypto wallets to deposit from the customer’s account on their behalf. |
| `auth.persist_login:read` | Allow use of a persisted token for seamless sign-in. (For Android and iOS) |

```shell
curl -X POST https://login.link.com/v1/link_auth_intent \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "oauth_client_id": "$OAUTH_CLIENT_ID", "oauth_scopes": "kyc.status:read,crypto:ramp"}'
```

```json
// Response
{
  "id": "lai_xxxx",
  "expires_at": 1756238966
}
```

**Parameters**

| Parameter               | Type                | Description                                                                                                                                     |
| ----------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `email`                 | string (required)   | The user’s email for looking up an existing Link customer. Provide either `email` or `hashed_email`, not both.                                  |
| `hashed_email`          | string (required\*) | A SHA256 hash of the plain text email for privacy-sensitive flows. Provide either `email` or `hashed_email`, not both.                          |
| `oauth_client_id`       | string (required)   | Your OAuth client id (for example, from Link). Identifies your application in the OAuth flow.                                                   |
| `oauth_scopes`          | string (required)   | Comma-separated list of OAuth scopes (for example, `kyc.status:read,crypto:ramp`). Defines the permissions you’re requesting.                   |
| `data_sharing_merchant` | string (optional)   | When set, the recipient business ID for data-sharing (for example, crypto onramp). Must be a valid business ID enabled to receive OAuth tokens. |

**Returns**

| Field        | Type    | Description                                                          |
| ------------ | ------- | -------------------------------------------------------------------- |
| `id`         | string  | Unique identifier for the `LinkAuthIntent` (for example, `lai_xxx`). |
| `expires_at` | integer | Unix timestamp when the intent expires.                              |

**Errors**

| HTTP status | Cause                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------ |
| 400         | Missing or invalid request body.                                                                 |
| 403         | The CreateLinkAuthIntent isn’t enabled for the business or the API key is invalid or missing.    |
| 404         | Can’t find the OAuth client for authIntentId, or the provided email has no active Link customer. |
| 409         | The Link customer previously revoked the connection with this partner.                           |

### Retrieve access tokens

Retrieving access tokens exchanges a consented `LinkAuthIntent` for an OAuth access token. Call this after the user completes authorization. Use the access token (for example, in the `Stripe-OAuth-Token` header) in subsequent onramp API requests for that user.

```shell
curl -X POST https://login.link.com/v1/link_auth_intent/{authIntentId}/tokens \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY"
```

```json
// Response
{
  "access_token": "liwltoken_xxx",
  "expires_in": 3600,
  "token_type": "Bearer",
  "refresh": {
    "refresh_token": "liwlrefresh_xxx",
    "expires_in": 7776000
  }
}
```

**Parameters**

| Parameter | Type              | Description                                       |
| --------- | ----------------- | ------------------------------------------------- |
| `id`      | string (required) | The Link Auth Intent id (for example, `lai_xxx`). |

**Returns**

| Field                   | Type              | Description                                                                                                                                                                                                                                       |
| ----------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`          | string            | OAuth access token. Send it on subsequent API requests for this user (for example, in the `Stripe-OAuth-Token` header).                                                                                                                           |
| `token_type`            | string            | Token type. Always `Bearer`.                                                                                                                                                                                                                      |
| `expires_in`            | integer           | Seconds until the access token expires.                                                                                                                                                                                                           |
| `refresh`               | object (optional) | Present when a refresh token was issued. Use it to obtain a new access token when the current one expires. See [Refresh an Access Token](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#refresh-an-access-token). |
| `refresh.refresh_token` | string            | OAuth refresh token. Store it securely and use it to obtain new access tokens. See [Refresh an Access Token](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#refresh-an-access-token).                             |
| `refresh.expires_in`    | integer           | Seconds until the refresh token expires.                                                                                                                                                                                                          |

**Errors**

| HTTP status | Cause                                                                                  |
| ----------- | -------------------------------------------------------------------------------------- |
| 403         | Feature not available.                                                                 |
| 403         | `LinkAuthIntent` hasn’t been consented by the user.                                    |
| 403         | Invalid or missing API key.                                                            |
| 404         | `LinkAuthIntent` not found (an invalid id, or the intent belongs to another business). |

### Refresh an access token

Exchanges a refresh token for a new access token. When your access token expires, use the refresh token you received from [Retrieve Access Tokens](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md#retrieve-access-tokens) API to obtain a new access token without requiring the user to re-authorize.

To obtain your `OAUTH_CLIENT_SECRET`, contact your Stripe account executive or solutions architect. Stripe provisions the credential as part of your onboarding.

```shell
curl -X POST https://login.link.com/auth/token \
  -H "Authorization: Bearer $STRIPE_SECRET_KEY" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=$REFRESH_TOKEN" \
  -d "client_id=$OAUTH_CLIENT_ID" \
  -d "client_secret=$OAUTH_CLIENT_SECRET"
```

```json
// Response
{
  "access_token": "liwltoken_xxx",
  "refresh_token": "liwlrefresh_xxx",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "kyc.status:read crypto:ramp"
}
```

**Parameters**

| Parameter       | Type              | Description                                                                |
| --------------- | ----------------- | -------------------------------------------------------------------------- |
| `grant_type`    | string (required) | Must be `refresh_token`.                                                   |
| `refresh_token` | string (required) | The refresh token previously obtained from the Retrieve Access Tokens API. |
| `client_id`     | string (required) | Your OAuth client ID provided by Link.                                     |
| `client_secret` | string (required) | Your OAuth client secret provided by Link.                                 |

**Returns**

| Field                   | Type              | Description                                                                                                                                       |
| ----------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `token_type`            | string            | Token type. Always `Bearer`.                                                                                                                      |
| `access_token`          | string            | OAuth access token. Expires in 1 hour. Send it on subsequent API requests (for example, in the `Stripe-OAuth-Token` header).                      |
| `expires_in`            | integer           | TTL in seconds (3600, that is, 1 hour).                                                                                                           |
| `refresh`               | object (optional) | Present when a new refresh token was issued. A new refresh token is returned each time you use the old one. Store it for future refresh requests. |
| `refresh.refresh_token` | string            | An OAuth refresh token. Store it securely for obtaining new access tokens when the current one expires.                                           |
| `refresh.expires_in`    | integer           | Seconds until the refresh token expires.                                                                                                          |
| `scope`                 | string            | The OAuth scopes granted.                                                                                                                         |
