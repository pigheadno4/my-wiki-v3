<!-- Source URL: https://docs.stripe.com/payments/machine/x402 -->
<!-- Fetched: 2026-05-12 -->

# x402 payments

Use x402 for machine-to-machine payments.

[x402](https://x402.org) is a protocol for internet payments. When a client requests a paid resource, your server returns an HTTP 402 response with payment details. The client pays, then retries the request with an authorization. Stripe handles deposit addresses and automatically _captures_ (Another way to say that you receive payment for a charge is to say that you "capture" the charge. Capturing the charge is often asynchronous and takes place after authorization. The capture is what transfers the money from the customer to you) the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) when funds settle on-chain.

You can find the app’s [complete source code](https://github.com/stripe-samples/machine-payments) on GitHub.

## Before you begin

Machine payments must be enabled for your account.

> Your customers can use stablecoins as payment globally, but only US businesses can accept stablecoin payments.

To start accepting stablecoin payments:

1. Make sure you’ve [set up your Stripe account](https://docs.stripe.com/get-started/account/set-up.md).
1. Go to your [Payment methods](https://dashboard.stripe.com/settings/payment_methods) settings in the Dashboard and request the **Stablecoins and Crypto** payment method. If you only want to accept stablecoin or crypto payments for [machine payments](https://docs.stripe.com/payments/machine.md), we recommend creating a separate [payment method configuration](https://docs.stripe.com/payments/payment-method-configurations.md) dedicated to machine payments.
1. Stripe reviews your access request and contact you for more details if necessary. The payment method appears as **Pending** while we review your request.
1. After we approve your request, **Stablecoins and Crypto** becomes active in the Dashboard.

## Payment lifecycle

In this guide, you build the server. Your server indicates that payment is required and returns the content after successful payment. You interact with Stripe and a facilitator to complete the payment.
A diagram showing the x402 payment flow between client, server, Stripe, and facilitator (See full diagram at https://docs.stripe.com/payments/machine/x402)

## Create your endpoint

Add payment middleware to your endpoint to require payment.

This example requires 0.01 USD, paid in USDC, per request to `/paid`.

#### Node.js

```node
import { paymentMiddleware } from "@x402/hono";
import { x402ResourceServer, HTTPFacilitatorClient } from "@x402/core/server";
import { ExactEvmScheme } from "@x402/evm/exact/server";

app.use(
  paymentMiddleware(
    {
      "GET /paid": {
        accepts: [
          {
            scheme: "exact",
            price: "$0.01",
            network: "eip155:84532",
            payTo: createPayToAddress,
          },
        ],
        description: "Data retrieval endpoint",
        mimeType: "application/json",
      },
    },
    new x402ResourceServer(facilitatorClient).register(
      "eip155:84532",
      new ExactEvmScheme(),
    ),
  ),
);
```

## Create a PaymentIntent

To process payments, create a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) that accepts the `crypto` _payment method_ (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs). Use the `payTo` method from earlier.

> #### API version
>
> This feature requires the `2026-03-04.preview` API version. Set the `Stripe-Version` header to `2026-03-04.preview` when initializing your Stripe client.

#### Node.js

```node
import Stripe from "stripe";
import NodeCache from "node-cache";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
  apiVersion: "2026-03-04.preview",
});

// In-memory cache for deposit addresses (TTL: 5 minutes)
// NOTE: For production, use a distributed cache like Redis instead of node-cache
const paymentCache = new NodeCache({ stdTTL: 300, checkperiod: 60 });

async function createPayToAddress(context) {
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
  const depositDetails = paymentIntent.next_action.crypto_display_details;
  const payToAddress = depositDetails.deposit_addresses["base"].address;

  console.log(
    `Created PaymentIntent ${paymentIntent.id} for $${(
      amountInCents / 100
    ).toFixed(2)} -> ${payToAddress}`,
  );

  paymentCache.set(payToAddress, true);
  return payToAddress;
}
```

This function returns a crypto deposit address that the client receives and uses for payment.

The [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) response includes deposit addresses with `supported_tokens`, which lists the accepted tokens and their contract addresses for each network:

```json
{
  "id": "pi_123",
  "amount": 5000,
  "currency": "usd",
  "status": "requires_action",
  "next_action": {
    "type": "crypto_display_details",
    "crypto_display_details": {
      "deposit_addresses": {
        "base": {
          "address": "0xbase_address",
          "supported_tokens": [
            {
              "token_currency": "usdc",
              "token_contract_address": "0x…"
            }
          ]
        }
      }
    }
  }
}
```

> #### Crypto PaymentIntents
>
> For more details on how crypto PaymentIntents work, including deposit addresses, payment lifecycle, and supported networks, see the [deposit mode integration guide](https://docs.stripe.com/payments/deposit-mode-stablecoin-payments.md).

## Test your endpoint

Make a request to your server without an eligible client to confirm it returns a `402` status code.

```bash
curl http://localhost:3000/paid
```

You see a `402` status code.

Next, make a request with an eligible client. Use Stripe’s [purl](https://github.com/stripe/purl) to test in the command line.

```bash
purl http://localhost:3000/paid
```

> #### Sandboxes and testnet
>
> [PaymentIntents](https://docs.stripe.com/api/payment_intents/object.md) that you create in a [sandbox](https://docs.stripe.com/sandboxes.md) don’t monitor crypto testnets, so we can’t automatically detect testnet transactions that you send. To test sandbox `PaymentIntents`, use the [test helper endpoint](https://docs.stripe.com/api/payment_intents/simulate_crypto_deposit.md?api-version=2026-03-04.preview) to simulate crypto deposits. [Learn more about testing your integration](https://docs.stripe.com/payments/deposit-mode-stablecoin-payments.md#test-your-integration).

If you connected a wallet, the server returns the content and you can confirm payment. Visit the [Stripe Dashboard Payments](https://dashboard.stripe.com/payments) page to see the transaction.

Alternatively, you can use curl to fetch the latest payments from the Stripe API:

```bash
curl https://api.stripe.com/v1/payment_intents?limit=10 \
  -u <<YOUR_SECRET_KEY>>:
```

## Run mainnet transactions

To run mainnet transactions, integrate with an x402 facilitator that supports mainnet.

See the Coinbase Developer Platform guide to [use the CDP Facilitator](https://docs.cdp.coinbase.com/x402/quickstart-for-sellers#running-on-mainnet).

## Token and network support

`PaymentIntents` with the `crypto` payment method in `mode: deposit` support USDC on the following networks:

| Network | Token | Token contract address                         |
| ------- | ----- | ---------------------------------------------- |
| Tempo   | USDC  | `0x20c000000000000000000000b9537d11c60e8b50`   |
| Base    | USDC  | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`   |
| Solana  | USDC  | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
