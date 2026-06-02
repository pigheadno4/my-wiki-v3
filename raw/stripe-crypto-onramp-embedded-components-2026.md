<!-- Source URL: https://docs.stripe.com/crypto/onramp/embedded-components -->
<!-- Fetched: 2026-05-11 -->
<!-- Architecture: JavaScript SDK / iOS SDK / Android SDK / React Native SDK -->
<!-- Frontend: HTML / React — Backend: Ruby / Node.js / PHP / Python / Go / .NET / Java -->

# Set up the Embedded Components onramp

This quickstart runs minimal code for the full flow. Use this when you want to get started quickly, or to explore the integration before you start building.

For React Native, the production SDK is `@stripe/stripe-react-native`. For web, use `@stripe/crypto`.

See our sample apps: React Native (Expo) | iOS | Android. Follow the integration guide for step-by-step instructions to build your integration.

## Step 1: Set up the server

### Install the Stripe Node library

```bash
npm install --save stripe
```

### Set the Stripe-Version header

All backend requests to the Stripe API must include the `Stripe-Version` header with the `crypto_onramp_beta=v2` flag:

```text
Stripe-Version: 2026-03-25.dahlia;crypto_onramp_beta=v2
```

### Create a LinkAuthIntent

Add an endpoint that creates a `LinkAuthIntent` with the onramp OAuth scopes described in the integration guide. The client uses the returned `authIntentId` when calling `authenticate()` from the SDK.

### Exchange for access tokens

After the user consents using `authenticate()` on the client, you can exchange the `LinkAuthIntent` for an OAuth access token using the Retrieve Access Tokens API. Store the access token and use it in the `Stripe-OAuth-Token` header for all subsequent crypto API calls from your backend. Don't expose the access token to the client.

### Refresh an expired access token

When the access token expires, call `POST https://login.link.com/auth/token` with `grant_type=refresh_token` and the refresh token from the original token exchange response to obtain a new access token. Pass your `LINK_CLIENT_ID` and `LINK_CLIENT_SECRET` along with the same OAuth scopes used in the original request.

### Retrieve a CryptoCustomer

Add an endpoint that calls the Retrieve a CryptoCustomer API with the `customerId` from the authorize flow. Use the response to check the customer's KYC and verification status so the client can prompt them to complete setup (KYC, identity verification, wallet registration, payment method) before creating an onramp session.

### List ConsumerWallets

Add an endpoint that calls the List ConsumerWallets API. Use it to see whether the user already has wallet addresses on file. If the list is empty, the client calls `registerWalletAddress()` before creating an onramp session.

### List PaymentTokens

Add an endpoint that calls the List PaymentTokens API. Use it to see which payment methods the user already has. If the list is empty, have the client call `collectPaymentMethod()` before creating an onramp session.

### Create a CryptoOnrampSession

Add an endpoint that creates a `CryptoOnrampSession` with `ui_mode: headless`. Pass the `crypto_customer_id` from the authorize flow and `payment_token` from `collectPaymentMethod()` or an existing `payment_token` from List PaymentTokens. Include the amount, currencies, network, and wallet address.

### Refresh an executable quote

Add an endpoint that calls the Refresh a Quote API to refresh a quote for the onramp session. Refresh the quote before it expires. Checkout will return an HTTP 400 response if you checkout with an expired quote.

### Perform checkout

Add an endpoint that calls the Checkout API to confirm and fulfill the onramp session. Your backend returns the `client_secret` so the client SDK can validate and complete any required steps (for example, 3DS) using `performCheckout()`.

## Step 2: Set up the SDK

### Install the SDK

```bash
npm install @stripe/crypto
```

## Step 3: Build the client flow

### Authentication flow

Call your server's `/create-link-auth-intent` endpoint with the user's email. A 404 response means the user doesn't have a Link account — in that case, call `onramp.registerLinkUser(email, phoneNumber, country)` to create one. A successful response returns an `authIntentId` that you use in the next step.

Your server creates a `LinkAuthIntent` and returns the `authIntentId`. Call `authenticate(authIntentId, callback)` to start the authentication flow. The SDK returns an element to mount in your page that displays the authentication UI. We recommend presenting the authentication UI in a modal. When the user completes authentication, the callback fires with `crypto_customer_id`. Store it in your backend and use it for the rest of the flow.

### Identity flow

Check the customer's verification status by calling your server. If KYC is missing, call `submitKycInfo()` with the customer's personal details. If identity verification is required, call `verifyDocuments()`. After each step completes, re-check the customer status to determine the next required action.

### Register a wallet address

Call `registerWalletAddress(walletAddress, network)` to register the user's wallet address for the selected network.

### Payment flow

You can use List PaymentTokens to render a list of customer payment methods. If the customer has no payment method, call `collectPaymentMethod()` to display the payment UI and collect a `cryptoPaymentToken`.

### Checkout

Create a `CryptoOnrampSession` on your server. Then call `performCheckout(sessionId, fetchClientSecret)`, passing a callback that calls your backend's `/checkout/:sessionId` and returns the `client_secret`. If the quote expires, call your server's `/quote/:sessionId` endpoint to refresh the quote.

## Next steps

- **Embedded Components onramp integration guide**: Detailed step-by-step instructions for building the integration.
- **Embedded Components onramp overview**: Learn about the customer flow and integration phases.

## Server code (Node.js)

```javascript
const express = require('express');
const app = express();
// This is a public sample test API key.
// Don't submit any personally identifiable information in requests made with this key.
// Sign in to see your own test API key embedded in code samples.
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
const secretKey = 'sk_test_Ou1w6LVt3zmVipDVJsvMeQsc';
const oauthScopes = process.env.LINK_OAUTH_SCOPES || 'crypto:ramp,kyc.status:read';

app.use(express.json());

app.post('/create-link-auth-intent', async (req, res) => {
  const { email } = req.body;
  const linkRes = await fetch('https://login.link.com/v1/link_auth_intent', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${secretKey}`,
    },
    body: JSON.stringify({
      email,
      oauth_scopes: oauthScopes,
      oauth_client_id: process.env.LINK_OAUTH_CLIENT_ID || 'your_oauth_client_id',
    }),
  });
  const data = await linkRes.json();
  if (data.id) {
    res.json({ authIntentId: data.id });
  } else {
    res.status(linkRes.status).json(data);
  }
});

async function exchangeTokens(authIntentId) {
  const res = await fetch(`https://login.link.com/v1/link_auth_intent/${authIntentId}/tokens`, {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${secretKey}` },
  });
  const data = await res.json();
  if (!data.access_token) throw new Error('Token exchange failed');
  return data.access_token;
}

async function refreshExchangeTokens(refreshToken) {
  const params = new URLSearchParams({
    client_id: process.env.LINK_CLIENT_ID || 'lwlpk_xxxxx',
    client_secret: process.env.LINK_CLIENT_SECRET || 'lwlsk_xxxxx',
    grant_type: 'refresh_token',
    refresh_token: refreshToken,
    scope: oauthScopes,
  });
  const res = await fetch('https://login.link.com/auth/token', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${secretKey}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: params,
  });
  const data = await res.json();
  if (!data.access_token) throw new Error('Token refresh failed');
  return data.access_token;
}

app.get('/crypto/customer/:id', async (req, res) => {
  const oauthToken = await exchangeTokens(req.query.authIntentId);
  const stripeRes = await fetch(`https://api.stripe.com/v1/crypto/customers/${req.params.id}`, {
    headers: {
      'Authorization': `Bearer ${secretKey}`,
      'Stripe-OAuth-Token': oauthToken,
      'Stripe-Version': '2026-03-25.dahlia;crypto_onramp_beta=v2',
    },
  });
  const data = await stripeRes.json();
  res.status(stripeRes.status).json(data);
});

app.get('/crypto/customer/:id/wallets', async (req, res) => {
  const oauthToken = await exchangeTokens(req.query.authIntentId);
  const stripeRes = await fetch(
    `https://api.stripe.com/v1/crypto/customers/${req.params.id}/crypto_consumer_wallets`,
    {
      headers: {
        'Authorization': `Bearer ${secretKey}`,
        'Stripe-OAuth-Token': oauthToken,
        'Stripe-Version': '2026-03-25.dahlia;crypto_onramp_beta=v2',
      },
    }
  );
  const data = await stripeRes.json();
  res.status(stripeRes.status).json(data);
});

app.get('/crypto/customer/:id/payment-tokens', async (req, res) => {
  const oauthToken = await exchangeTokens(req.query.authIntentId);
  const stripeRes = await fetch(
    `https://api.stripe.com/v1/crypto/customers/${req.params.id}/payment_tokens`,
    {
      headers: {
        'Authorization': `Bearer ${secretKey}`,
        'Stripe-OAuth-Token': oauthToken,
        'Stripe-Version': '2026-03-25.dahlia;crypto_onramp_beta=v2',
      },
    }
  );
  const data = await stripeRes.json();
  res.status(stripeRes.status).json(data);
});

app.post('/create-onramp-session', async (req, res) => {
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

  const oauthToken = await exchangeTokens(authIntentId);
  const params = new URLSearchParams({
    ui_mode: 'headless',
    crypto_customer_id,
    payment_token,
    source_amount: String(source_amount),
    source_currency,
    destination_currency,
    'destination_currencies[]': destination_currency,
    destination_network,
    'destination_networks[]': destination_network,
    wallet_address,
    customer_ip_address: req.ip || req.socket.remoteAddress,
  });

  const stripeRes = await fetch('https://api.stripe.com/v1/crypto/onramp_sessions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': `Bearer ${secretKey}`,
      'Stripe-OAuth-Token': oauthToken,
      'Stripe-Version': '2026-03-25.dahlia;crypto_onramp_beta=v2',
    },
    body: params,
  });
  const data = await stripeRes.json();
  if (data.id) {
    res.json({ id: data.id, quote_expires_at: data.quote?.expires_at ?? null });
  } else {
    res.status(stripeRes.status).json(data);
  }
});

app.post('/quote/:sessionId', async (req, res) => {
  const oauthToken = await exchangeTokens(req.body.authIntentId);
  const stripeRes = await fetch(
    `https://api.stripe.com/v1/crypto/onramp_sessions/${req.params.sessionId}/quote`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${secretKey}`,
        'Stripe-OAuth-Token': oauthToken,
        'Stripe-Version': '2026-03-25.dahlia;crypto_onramp_beta=v2',
      },
    }
  );
  const data = await stripeRes.json();
  res.status(stripeRes.status).json(data);
});

app.post('/checkout/:sessionId', async (req, res) => {
  const oauthToken = await exchangeTokens(req.body.authIntentId);
  const params = new URLSearchParams({
    'mandate_data[customer_acceptance][type]': 'online',
    'mandate_data[customer_acceptance][accepted_at]': String(Math.floor(Date.now() / 1000)),
    'mandate_data[customer_acceptance][online][ip_address]': req.ip || req.socket.remoteAddress || '',
    'mandate_data[customer_acceptance][online][user_agent]': req.headers['user-agent'] || '',
  });
  const stripeRes = await fetch(
    `https://api.stripe.com/v1/crypto/onramp_sessions/${req.params.sessionId}/checkout`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': `Bearer ${secretKey}`,
        'Stripe-OAuth-Token': oauthToken,
        'Stripe-Version': '2026-03-25.dahlia;crypto_onramp_beta=v2',
      },
      body: params,
    }
  );
  const data = await stripeRes.json();
  res.status(stripeRes.status).json(data);
});

app.listen(4242, () => console.log('Server running on port 4242'));
```

## Client code (React)

```jsx
import React, { useState, useEffect, useRef } from 'react';
import { loadCryptoOnrampAndInitialize } from '@stripe/crypto';

const SERVER = 'http://localhost:4242';

export default function App() {
  const [onramp, setOnramp] = useState(null);
  const [step, setStep] = useState('auth');
  const [email, setEmail] = useState('');
  const [linkAuthIntentId, setLinkAuthIntentId] = useState(null);
  const [cryptoCustomerId, setCryptoCustomerId] = useState(null);
  const [walletAddress, setWalletAddress] = useState('');
  const [walletNetwork, setWalletNetwork] = useState('base');
  const [cryptoPaymentToken, setCryptoPaymentToken] = useState(null);
  const [amount, setAmount] = useState('100');
  const [authElement, setAuthElement] = useState(null);
  const authRef = useRef(null);
  const paymentRef = useRef(null);

  useEffect(() => {
    loadCryptoOnrampAndInitialize('pk_test_GvF3BSyx8RSXMK5yAFhqEd3H').then(setOnramp);
  }, []);

  useEffect(() => {
    if (authRef.current && authElement) {
      authRef.current.replaceChildren(authElement);
    }
  }, [authElement]);

  async function routeNext(customerId, lai) {
    const [customer, wallets, tokens] = await Promise.all([
      fetch(`${SERVER}/crypto/customer/${customerId}?authIntentId=${encodeURIComponent(lai)}`).then(r => r.json()),
      fetch(`${SERVER}/crypto/customer/${customerId}/wallets?authIntentId=${encodeURIComponent(lai)}`).then(r => r.json()),
      fetch(`${SERVER}/crypto/customer/${customerId}/payment-tokens?authIntentId=${encodeURIComponent(lai)}`).then(r => r.json()),
    ]);
    const verifications = customer.verifications ?? [];
    const kyc = verifications.find(v => v.name === 'kyc_verified');
    const idDoc = verifications.find(v => v.name === 'id_document_verified');
    if (kyc?.status !== 'verified') { setStep('kyc'); return; }
    if (idDoc?.status !== 'verified') { setStep('verify'); return; }
    const walletList = wallets.data ?? [];
    const tokenList = tokens.data ?? [];
    if (walletList.length === 0) { setStep('wallet'); return; }
    if (tokenList.length === 0) { setStep('payment'); return; }
    setCryptoPaymentToken(tokenList[0].id);
    setWalletAddress(walletList[0].address ?? '');
    setStep('checkout');
  }

  async function handleLogin() {
    let res = await fetch(`${SERVER}/create-link-auth-intent`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email }),
    });

    if (res.status === 404) {
      await onramp.registerLinkUser(email, '+18004444444', 'US');
      res = await fetch(`${SERVER}/create-link-auth-intent`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      });
    }
    const { authIntentId } = await res.json();

    setLinkAuthIntentId(authIntentId);
    const element = await onramp.authenticate(authIntentId, async ({ crypto_customer_id }) => {
      setAuthElement(null);
      setCryptoCustomerId(crypto_customer_id);
      await routeNext(crypto_customer_id, authIntentId);
    });
    setAuthElement(element);
  }

  async function handleSubmitKyc() {
    await onramp.submitKycInfo({
      given_name: 'John',
      surname: 'Verified',
      date_of_birth: { day: 1, month: 1, year: 1990 },
      address: { line1: 'address_full_match', city: 'San Francisco', state: 'CA', postal_code: '94111', country: 'US' },
      id_number: { type: 'us_ssn', value: '000000000' },
    });
    await routeNext(cryptoCustomerId, linkAuthIntentId);
  }

  async function handleVerify() {
    await onramp.verifyDocuments();
    await routeNext(cryptoCustomerId, linkAuthIntentId);
  }

  async function handleRegisterWallet() {
    await onramp.registerWalletAddress(walletAddress, walletNetwork);
    await routeNext(cryptoCustomerId, linkAuthIntentId);
  }

  async function handleCollectPayment() {
    const element = await onramp.collectPaymentMethod(
      { payment_method_types: ['card'], wallets: { applePay: 'auto', googlePay: 'auto' } },
      ({ cryptoPaymentToken: token }) => {
        setCryptoPaymentToken(token);
        setStep('checkout');
      },
    );
    paymentRef.current?.replaceChildren(element);
  }

  async function handleCheckout() {
    const session = await fetch(`${SERVER}/create-onramp-session`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        authIntentId: linkAuthIntentId,
        crypto_customer_id: cryptoCustomerId,
        payment_token: cryptoPaymentToken,
        source_amount: parseFloat(amount),
        source_currency: 'usd',
        destination_currency: 'usdc',
        destination_network: walletNetwork || 'base',
        wallet_address: walletAddress,
      }),
    }).then(r => r.json());

    const now = Math.floor(Date.now() / 1000);
    if (!session.quote_expires_at || now >= session.quote_expires_at) {
      await fetch(`${SERVER}/quote/${session.id}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ authIntentId: linkAuthIntentId }),
      });
    }

    await onramp.performCheckout(session.id, async () => {
      const { client_secret } = await fetch(`${SERVER}/checkout/${session.id}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ authIntentId: linkAuthIntentId }),
      }).then(r => r.json());
      return client_secret;
    });
    setStep('complete');
  }

  if (!onramp) return <p>Loading...</p>;

  return (
    <div style={{ maxWidth: '480px', margin: '0 auto', padding: '20px' }}>
      {step === 'auth' && (
        <div>
          <input
            type="email"
            value={email}
            onChange={e => setEmail(e.target.value)}
            placeholder="Email"
            style={{ display: 'block', width: '100%', padding: '8px', marginBottom: '8px' }}
          />
          <button onClick={handleLogin} style={{ padding: '8px 16px' }}>
            Log in with Link
          </button>
          {authElement && <div ref={authRef} style={{ marginTop: '16px' }} />}
        </div>
      )}
      {step === 'kyc' && (
        <button onClick={handleSubmitKyc} style={{ padding: '8px 16px' }}>
          Submit KYC info
        </button>
      )}
      {step === 'verify' && (
        <button onClick={handleVerify} style={{ padding: '8px 16px' }}>
          Verify identity
        </button>
      )}
      {step === 'wallet' && (
        <div>
          <input
            value={walletAddress}
            onChange={e => setWalletAddress(e.target.value)}
            placeholder="Wallet address"
            style={{ display: 'block', width: '100%', padding: '8px', marginBottom: '8px' }}
          />
          <select
            value={walletNetwork}
            onChange={e => setWalletNetwork(e.target.value)}
            style={{ display: 'block', marginBottom: '8px' }}
          >
            <option value="base">Base</option>
            <option value="solana">Solana</option>
          </select>
          <button onClick={handleRegisterWallet} style={{ padding: '8px 16px' }}>
            Register wallet
          </button>
        </div>
      )}
      {step === 'payment' && (
        <div>
          <button onClick={handleCollectPayment} style={{ padding: '8px 16px' }}>
            Add payment method
          </button>
          <div ref={paymentRef} style={{ marginTop: '16px' }} />
        </div>
      )}
      {step === 'checkout' && (
        <div>
          <input
            value={amount}
            onChange={e => setAmount(e.target.value)}
            placeholder="Amount in USD"
            style={{ display: 'block', width: '100%', padding: '8px', marginBottom: '8px' }}
          />
          <button onClick={handleCheckout} style={{ padding: '8px 16px' }}>
            Buy crypto
          </button>
        </div>
      )}
      {step === 'complete' && <p>Transaction complete.</p>}
    </div>
  );
}
```
