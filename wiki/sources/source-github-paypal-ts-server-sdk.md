---
title: "GitHub: paypal/PayPal-TypeScript-Server-SDK"
type: source
date_ingested: 2026-04-16
original_format: github-repo
raw_files:
  - "github-paypal-ts-server-sdk.md"
tags: [paypal, typescript, server-sdk, orders, payments, vault, subscriptions, oauth]
---

## Summary

PayPal's official TypeScript server-side SDK (`@paypal/paypal-server-sdk`). Wraps 5 PayPal REST API controllers with typed interfaces, auto-handles OAuth2 token management, and supports 3 client initialization patterns. v2.3.0.

## Install

```bash
npm install @paypal/paypal-server-sdk@2.3.0
```

## Client Initialization

Three patterns supported:

### Code-based
```ts
import { Client, Environment, LogLevel } from '@paypal/paypal-server-sdk';

const client = new Client({
  clientCredentialsAuthCredentials: {
    oAuthClientId: 'OAuthClientId',
    oAuthClientSecret: 'OAuthClientSecret'
  },
  environment: Environment.Sandbox, // or Environment.Production
  timeout: 0,
  logging: {
    logLevel: LogLevel.Info,
    logRequest: { logBody: true },
    logResponse: { logHeaders: true }
  }
});
```

### Config-file based
```ts
const client = Client.fromJsonConfig(fileContent); // reads config.json
```

### Environment-variable based
```ts
// reads from .env file
```

## Controllers (5)

| Controller | API | Key methods |
| --- | --- | --- |
| `OrdersController` | Orders v2 | createOrder, getOrder, patchOrder, confirmOrder, authorizeOrder, captureOrder, createOrderTracking, updateOrderTracking |
| `PaymentsController` | Payments v2 | getAuthorizedPayment, reauthorizeOrder, voidPayment, captureAuthorizedPayment, getRefund, refundCapturedPayment, getCapturedPayment |
| `VaultController` | Payment Tokens v3 | createSetupToken, getSetupToken, createPaymentToken, getPaymentToken, listCustomerPaymentTokens, deletePaymentToken |
| `SubscriptionsController` | Subscriptions v1 | Full products/plans/subscriptions lifecycle |
| `TransactionSearchController` | Transaction Search v1 | listTransactions |

## Key Patterns

```ts
// Create order
const ordersController = new OrdersController(client);
const response = await ordersController.createOrder({
  body: {
    intent: CheckoutPaymentIntent.Capture,
    purchaseUnits: [{ amount: { currencyCode: 'USD', value: '10.00' } }]
  },
  prefer: 'return=representation'
});
const order = response.result;
```

All methods return `Promise<ApiResponse<T>>` — result is in `.result`.

## Notable Header Parameters

All controller methods accept optional headers:
- `paypalRequestId` — idempotency key (required for single-step creates with payment source)
- `paypalPartnerAttributionId` — BN code for partner attribution
- `paypalClientMetadataId` — fraud protection metadata ID
- `paypalAuthAssertion` — JWT for marketplace/partner flows
- `paypalMockResponse` — negative testing in sandbox
- `prefer` — `return=minimal` (default) or `return=representation`

## Related Pages

- [[paypal]] — company page
- [[paypal-vault]] — Vault/Payment Tokens concept
- [[paypal-payouts]] — Payouts (not yet in this SDK)
- [[source-github-paypal-rest-api-specs]] — OpenAPI specs for same APIs

## Raw Sources

- [[github-paypal-ts-server-sdk]] — stub file pointing to detail directory
