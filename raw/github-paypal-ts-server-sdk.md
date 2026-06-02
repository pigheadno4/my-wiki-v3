<!-- Repo: https://github.com/paypal/PayPal-TypeScript-Server-SDK -->
<!-- Commit SHA: ff27fa8e18cccad1daf180fe98d3cf0ed5ed3c5b -->
<!-- Date reviewed: 2026-04-16 -->
<!-- Detail directory: raw/github-paypal-ts-server-sdk/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-ts-server-sdk/README.md
  raw/github-paypal-ts-server-sdk/doc/client.md
  raw/github-paypal-ts-server-sdk/doc/auth/oauth-2-client-credentials-grant.md
  raw/github-paypal-ts-server-sdk/doc/controllers/orders.md
  raw/github-paypal-ts-server-sdk/doc/controllers/payments.md
  raw/github-paypal-ts-server-sdk/doc/controllers/vault.md
  raw/github-paypal-ts-server-sdk/doc/controllers/subscriptions.md
  raw/github-paypal-ts-server-sdk/doc/controllers/transaction-search.md
  raw/github-paypal-ts-server-sdk/src/client.ts
  raw/github-paypal-ts-server-sdk/src/configuration.ts
  raw/github-paypal-ts-server-sdk/src/index.ts
  raw/github-paypal-ts-server-sdk/src/controllers/ordersController.ts
  raw/github-paypal-ts-server-sdk/src/controllers/paymentsController.ts
  raw/github-paypal-ts-server-sdk/src/controllers/vaultController.ts
  raw/github-paypal-ts-server-sdk/src/controllers/subscriptionsController.ts
  raw/github-paypal-ts-server-sdk/src/controllers/transactionSearchController.ts
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/github-paypal-ts-server-sdk/ preserving their repo-relative paths -->

# PayPal TypeScript Server SDK

GitHub: https://github.com/paypal/PayPal-TypeScript-Server-SDK
npm: `@paypal/paypal-server-sdk@2.3.0`
Note: Currently covers 5 controllers only — more endpoints planned

## What each file covers

| File | What to find there |
| --- | --- |
| `raw/github-paypal-ts-server-sdk/README.md` | Setup, 3 init patterns (code/config/env), environment enum, full usage examples for all controllers |
| `raw/github-paypal-ts-server-sdk/doc/client.md` | Client config reference: all parameters, timeout, logging, httpClientOptions |
| `raw/github-paypal-ts-server-sdk/doc/auth/oauth-2-client-credentials-grant.md` | OAuth2 client credentials setup and token management |
| `raw/github-paypal-ts-server-sdk/doc/controllers/orders.md` | Orders: 8 methods (create, get, patch, confirm, authorize, capture, create/update tracking) with full signatures and examples |
| `raw/github-paypal-ts-server-sdk/doc/controllers/payments.md` | Payments: authorize/reauthorize/void/capture, refund, show details |
| `raw/github-paypal-ts-server-sdk/doc/controllers/vault.md` | Vault/Payment Tokens: setup tokens, payment tokens, customer management |
| `raw/github-paypal-ts-server-sdk/doc/controllers/subscriptions.md` | Subscriptions: products, plans, subscriptions full lifecycle |
| `raw/github-paypal-ts-server-sdk/doc/controllers/transaction-search.md` | Transaction search with filters |
| `raw/github-paypal-ts-server-sdk/src/client.ts` | Client class implementation |
| `raw/github-paypal-ts-server-sdk/src/configuration.ts` | Configuration types and defaults |
| `raw/github-paypal-ts-server-sdk/src/index.ts` | All package exports |
| `raw/github-paypal-ts-server-sdk/src/controllers/ordersController.ts` | Orders controller TypeScript implementation |
| `raw/github-paypal-ts-server-sdk/src/controllers/paymentsController.ts` | Payments controller TypeScript implementation |
| `raw/github-paypal-ts-server-sdk/src/controllers/vaultController.ts` | Vault controller TypeScript implementation |
| `raw/github-paypal-ts-server-sdk/src/controllers/subscriptionsController.ts` | Subscriptions controller TypeScript implementation |
| `raw/github-paypal-ts-server-sdk/src/controllers/transactionSearchController.ts` | Transaction search controller TypeScript implementation |
