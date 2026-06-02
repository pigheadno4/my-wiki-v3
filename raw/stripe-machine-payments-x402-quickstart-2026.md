<!-- Source URL: https://docs.stripe.com/payments/machine/x402 -->
<!-- Fetched: 2026-05-12 -->
<!-- Note: Content formatted from structured UI quickstart (not raw markdown paste) -->
<!-- Backend: Node.js / Python -->

# x402 payment endpoint builder

Learn how to build and deploy a server endpoint that accepts x402 payments for machine-to-machine transactions.

## Step 1: Set up your server

### Install the Stripe Node library

```bash
npm install --save stripe
```

### Initialize Stripe

Set up the Stripe client with your secret key and set the API version to `2026-03-04.preview`. The client handles payment processing and provides crypto deposit addresses for x402 payments.

Make sure you have crypto payins enabled on your Stripe account.

### Configure the facilitator

The facilitator verifies payment proofs and settles transactions on-chain. For testing, use the x402.org testnet facilitator. In production, you can run your own facilitator or use a trusted third-party service.

## Step 2: Create payment flow

### Create the PaymentIntent handler

Create a function that determines where to send payments. Either extract the address from an existing payment header for retries or verification, or create a new PaymentIntent to generate a new deposit address.

When you create a PaymentIntent with the crypto payment method and deposit mode, specify the networks you want to support using `deposit_options`. Stripe returns deposit addresses for the requested networks. The function extracts the Base network address clients use to send USDC.

### Add payment middleware

Add middleware to protect your endpoint and declare the payment requirements. Configure:

- `scheme`: Set the payment scheme. Use `exact` for exact-amount payments.
- `price`: Set the cost per request, for example, `0.01 USD`.
- `network`: Set the blockchain network, for example, `eip155:84532` for the Base Sepolia testnet.
- `payTo`: Provide a function that returns the deposit address.

### Create your protected endpoint

Define the endpoint that requires payment. The middleware automatically:

1. Returns a `402 Payment Required` response with payment details when the request doesn't include a valid payment.
2. Verifies payment proofs through the facilitator.
3. Allows access after the facilitator confirms the payment.

## Step 3: Test your endpoint

### Test without payment

```bash
curl http://localhost:4242/paid
```

Returns a 402 Payment Required response with x402 payment information, including the deposit address.

### Test with payment

Use Stripe's `purl` tool to test the full payment flow. The tool handles the x402 protocol and completes the payment automatically.

```bash
purl http://localhost:4242/paid
```

If you have a wallet connected with testnet USDC, the server returns the content after successful payment.

## Full server code (Node.js / TypeScript)

```typescript
import Stripe from "stripe";
import { config } from "dotenv";
import { paymentMiddleware, x402ResourceServer } from "@x402/hono";
import { ExactEvmScheme } from "@x402/evm/exact/server";
import { HTTPFacilitatorClient } from "@x402/core/server";
import { Hono } from "hono";
import { serve } from "@hono/node-server";
import NodeCache from 'node-cache';
config();

const app = new Hono();

// Stripe handles payment processing and provides the crypto deposit address.
if (!process.env.STRIPE_SECRET_KEY) {
  console.error("❌ STRIPE_SECRET_KEY environment variable is required");
  process.exit(1);
}

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || "", {
  apiVersion: "2026-03-04.preview" as any,
  appInfo: {
    name: "stripe-samples/machine-payments",
    url: "https://github.com/stripe-samples/machine-payments",
    version: "1.0.0",
  },
});

// The facilitator verifies payment proofs and settles transactions on-chain.
// In this example, we use the x402.org testnet facilitator.
const facilitatorUrl = process.env.FACILITATOR_URL;
if (!facilitatorUrl) {
  console.error("❌ FACILITATOR_URL environment variable is required");
  process.exit(1);
}
const facilitatorClient = new HTTPFacilitatorClient({ url: facilitatorUrl });

// In-memory cache for deposit addresses (TTL: 5 minutes)
// NOTE: For production, use a distributed cache like Redis instead of node-cache
const paymentCache = new NodeCache({ stdTTL: 300, checkperiod: 60 });

// This function determines where payments should be sent. It either:
// 1. Extracts the address from an existing payment header (for retry/verification), or
// 2. Creates a new Stripe PaymentIntent to generate a fresh deposit address.
async function createPayToAddress(context: any): Promise<string> {
  // If a payment header exists, extract the destination address from it
  if (context.paymentHeader) {
    const decoded = JSON.parse(
      Buffer.from(context.paymentHeader, "base64").toString(),
    );
    const toAddress = decoded.payload?.authorization?.to;

    if (toAddress && typeof toAddress === "string") {
      if (!paymentCache.has(toAddress)) {
        throw new Error("Invalid payTo address: not found in server cache");
      }
      return toAddress;
    }

    throw new Error(
      "PaymentIntent did not return expected crypto deposit details",
    );
  }

  // Create a new PaymentIntent to get a fresh crypto deposit address
  const decimals = 6; // USDC has 6 decimals
  const amountInCents = Number(10000) / Math.pow(10, decimals - 2);

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
        deposit_options: {
          networks: ["base"],
        },
      },
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

  // Extract the Base network deposit address from the PaymentIntent
  const depositDetails = paymentIntent.next_action
    .crypto_display_details as any;
  const payToAddress = depositDetails.deposit_addresses["base"]
    .address as string;

  console.log(
    `Created PaymentIntent ${paymentIntent.id} for $${(
      amountInCents / 100
    ).toFixed(2)} -> ${payToAddress}`,
  );

  paymentCache.set(payToAddress, true);
  return payToAddress;
}

// The middleware protects the route and declares the payment requirements.
app.use(
  paymentMiddleware(
    {
      // Define pricing for protected endpoints
      "GET /paid": {
        accepts: [
          {
            scheme: "exact",        // Exact amount payment scheme
            price: "$0.01",         // Cost per request
            network: "eip155:84532", // Base Sepolia testnet
            payTo: createPayToAddress, // Dynamic address resolution
          },
        ],
        description: "Data retrieval endpoint",
        mimeType: "application/json",
      },
    },
    // Register the payment scheme handler for Base Sepolia
    new x402ResourceServer(facilitatorClient).register(
      "eip155:84532",
      new ExactEvmScheme(),
    ),
  ),
);

// This endpoint is only accessible after valid payment is verified.
app.get("/paid", (c) => {
  return c.json({
    foo: "bar",
  });
});

serve({
  fetch: app.fetch,
  port: 4242,
});

console.log(`Server listening at http://localhost:4242`);
```
