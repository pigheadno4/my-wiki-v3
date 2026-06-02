<!-- Source URL: https://docs.stripe.com/payments/machine/mpp -->
<!-- Fetched: 2026-05-12 -->
<!-- Note: Content formatted from structured UI quickstart (not raw markdown paste) -->
<!-- Backend: Node.js / Python -->

# MPP payment endpoint builder

Learn how to build and deploy a server that accepts both crypto and shared payment token (SPT) payments using the Machine Payments Protocol (MPP).

## Step 1: Set up your server

### Install the Stripe Node library

```bash
npm install --save stripe
```

### Initialize Stripe

Set up the Stripe client with your secret key, and set the API version to `2026-03-04.preview`. The client processes payment for both crypto and SPT payment methods.

Make sure you have crypto payins enabled for your Stripe account.

## Step 2: Create payment flows

### Create the PaymentIntent handler

Create a function that determines where to send crypto payments. Either extract the address from an existing payment header for retries or verification, or create a new PaymentIntent to generate a new deposit address.

When you create a PaymentIntent with the crypto payment method and deposit mode, specify the networks you want to support using `deposit_options`. Stripe returns deposit addresses for the requested networks. The function extracts the Tempo network address that clients use to send stablecoins.

## Step 3: Test your endpoints

## Full server code (Node.js / TypeScript)

```typescript
import crypto from 'crypto'
import { Hono } from 'hono'
import { config } from 'dotenv'
import { serve } from '@hono/node-server'
import { Mppx, tempo, stripe as mppxStripe } from 'mppx/server'
import { Credential } from 'mppx'
import Stripe from 'stripe'
import NodeCache from 'node-cache'
config()

// Stripe handles payment processing for both crypto and SPT methods
if (!process.env.STRIPE_SECRET_KEY) {
  console.error("STRIPE_SECRET_KEY environment variable is required");
  process.exit(1);
}

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
  apiVersion: "2026-03-04.preview" as any,
  appInfo: {
    name: "stripe-samples/machine-payments",
    url: "https://github.com/stripe-samples/machine-payments",
    version: "1.0.0",
  },
});

// Secret used to secure payment challenges
// https://mpp.dev/protocol/challenges#challenge-binding
const mppSecretKey = crypto.randomBytes(32).toString('base64');

// In-memory cache for deposit addresses (TTL: 5 minutes)
// NOTE: For production, use a distributed cache like Redis instead of node-cache
const paymentCache = new NodeCache({ stdTTL: 300, checkperiod: 60 });

// This function determines where crypto payments should be sent. It either:
// 1. Extracts the address from an existing payment header (for retry/verification), or
// 2. Creates a new Stripe PaymentIntent to generate a fresh deposit address.
async function createPayToAddress(request: Request): Promise<string> {
  const authHeader = request.headers.get('authorization')

  if (authHeader && Credential.extractPaymentScheme(authHeader)) {
    const credential = Credential.fromRequest(request)
    const toAddress = credential.challenge.request.recipient as `0x${string}`
    if (!paymentCache.has(toAddress)) {
      throw new Error('Invalid payTo address: not found in server cache')
    }
    return toAddress
  }

  // Create a new PaymentIntent to get a fresh crypto deposit address
  const decimals = 6; // USDC has 6 decimals
  const amountInCents = Number(1000000) / Math.pow(10, decimals - 2);

  const paymentIntent = await stripe.paymentIntents.create({
    amount: amountInCents,
    currency: "usd",
    payment_method_types: ["crypto"],
    payment_method_data: {
      type: "crypto",
    },
    payment_method_options: {
      crypto: {
        mode: "deposit",
        deposit_options: { networks: ["tempo"] },
      } as any,
    },
    confirm: true,
  });

  if (
    !paymentIntent.next_action ||
    !("crypto_display_details" in paymentIntent.next_action)
  ) {
    throw new Error(
      "PaymentIntent did not return expected crypto deposit details",
    );
  }

  // Extract the Tempo network deposit address from the PaymentIntent
  const depositDetails = paymentIntent.next_action
    .crypto_display_details as any;
  const payToAddress = depositDetails.deposit_addresses["tempo"]
    .address as string;

  console.log(
    `Created PaymentIntent ${paymentIntent.id} for $${(
      amountInCents / 100
    ).toFixed(2)} -> ${payToAddress}`,
  );

  paymentCache.set(payToAddress, true);
  return payToAddress;
}

// Create Mppx instance for SPT payments (cards and Link)
const mppxSpt = Mppx.create({
  methods: [
    mppxStripe.charge({
      networkId: 'internal',
      paymentMethodTypes: ['card', 'link'],
      secretKey: process.env.STRIPE_SECRET_KEY,
    }),
  ],
  secretKey: mppSecretKey
});

const PATH_USD = '0x20c0000000000000000000000000000000000000';

const app = new Hono()

// GET /crypto/paid - Accept crypto payments on Tempo
app.get('/crypto/paid', async (c) => {
  const request = c.req.raw

  const recipientAddress = await createPayToAddress(request)
  const mppxCrypto = Mppx.create({
    methods: [
      tempo.charge({
        currency: PATH_USD,
        recipient: recipientAddress,
        testnet: true,
      }),
    ],
    secretKey: mppSecretKey,
  })

  const response = await mppxCrypto.charge({ amount: '1' })(request)

  if (response.status === 402) {
    return response.challenge
  }

  return response.withReceipt(
    Response.json({
      data: 'Premium content delivered via crypto!',
      timestamp: new Date().toISOString(),
    })
  )
})

// GET /spt/paid - Accept SPT payments (cards and Link)
app.get('/spt/paid', async (c) => {
  const request = c.req.raw

  const result = await mppxSpt.charge({
    amount: '1',
    currency: 'usd',
  })(request);

  if (result.status === 402) {
    return result.challenge
  }

  return result.withReceipt(
    Response.json({
      data: 'Premium content delivered via SPT!',
      timestamp: new Date().toISOString(),
    })
  )
})

serve({
  fetch: app.fetch,
  port: 4242,
});

console.log(`Server listening at http://localhost:4242`);
console.log(`Crypto endpoint: http://localhost:4242/crypto/paid`);
console.log(`SPT endpoint: http://localhost:4242/spt/paid`);
```
