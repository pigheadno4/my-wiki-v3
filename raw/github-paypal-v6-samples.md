<!-- Repo: https://github.com/paypal-examples/v6-web-sdk-sample-integration -->
<!-- Commit SHA: dd9ef8a53c71d9d2107ad94c23b73b62f9811258 -->
<!-- Date reviewed: 2026-04-17 -->
<!-- Detail directory: raw/github-paypal-v6-samples/ -->
<!-- Files saved (read directly from these paths):
  raw/github-paypal-v6-samples/README.md
  raw/github-paypal-v6-samples/server/node/README.md
  raw/github-paypal-v6-samples/server/node/src/server.ts
  raw/github-paypal-v6-samples/server/node/src/paypalServerSdkClient.ts
  raw/github-paypal-v6-samples/server/node/src/routes/ordersRouteHandler.ts
  raw/github-paypal-v6-samples/server/node/src/routes/vaultRouteHandler.ts
  raw/github-paypal-v6-samples/server/node/src/routes/authRouteHandler.ts
  raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/recommended/app.js
  raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/redirect/app.js
  raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/directAppSwitch/app.js
  raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/hydrateEligibleMethods/app.js
  raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/merchantAsyncValidation/app.js
  raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/paymentHandler/app.js
  raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/sandboxedIframe/src/merchant-example/app.js
  raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/typescript/src/app.ts
  raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePaymentWithVault/html/src/recommended/app.js
  raw/github-paypal-v6-samples/client/components/paypalPayments/savePayment/html/src/app.js
  raw/github-paypal-v6-samples/client/components/cardFields/oneTimePayment/html/src/recommended/app.js
  raw/github-paypal-v6-samples/client/components/cardFields/oneTimePayment/html/src/advanced/threeDSecure/app.js
  raw/github-paypal-v6-samples/client/components/cardFields/savePayment/html/src/app.js
  raw/github-paypal-v6-samples/client/components/venmoPayments/oneTimePayment/html/src/app.js
  raw/github-paypal-v6-samples/client/components/googlepayPayments/oneTimePayment/html/src/app.js
  raw/github-paypal-v6-samples/client/components/applepayPayments/html/src/app.js
  raw/github-paypal-v6-samples/client/components/paypalGuestPayments/html/src/recommended/app.js
  raw/github-paypal-v6-samples/client/components/paypalGuestPayments/html/src/onload/app.js
  raw/github-paypal-v6-samples/client/components/paypalGuestPayments/html/src/shipping/app.js
  raw/github-paypal-v6-samples/client/components/paypalSubscriptions/html/src/recommended/app.js
  raw/github-paypal-v6-samples/client/components/paypalMessages/html/src/recommended/app.js
  raw/github-paypal-v6-samples/client/components/paypalMessages/html/src/advanced/app.js
  raw/github-paypal-v6-samples/client/components/bankAchPayments/oneTimePayment/html/src/recommended/app.js
  raw/github-paypal-v6-samples/client/components/sepaPayments/html/src/app.js
  raw/github-paypal-v6-samples/client/components/bancontactPayments/html/src/app.js
  raw/github-paypal-v6-samples/client/components/blikPayments/html/src/app.js
  raw/github-paypal-v6-samples/client/components/epsPayments/html/src/app.js
  raw/github-paypal-v6-samples/client/components/idealPayments/html/src/app.js
  raw/github-paypal-v6-samples/client/components/p24Payments/html/src/app.js
-->
<!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from https://github.com/paypal-examples/v6-web-sdk-sample-integration at commit dd9ef8a53c71d9d2107ad94c23b73b62f9811258, then save any newly discovered files into raw/github-paypal-v6-samples/ preserving their repo-relative paths -->

# paypal-examples/v6-web-sdk-sample-integration

Full working sample integration for PayPal JavaScript SDK v6. Node.js/Express backend + vanilla JS/HTML frontend. Covers all major payment components.

## What each file covers

| File | What to find there |
| ---- | ------------------ |
| `raw/github-paypal-v6-samples/README.md` | Top-level setup: install, env vars, start commands |
| `raw/github-paypal-v6-samples/server/node/README.md` | Server-specific setup and API endpoint docs |
| `raw/github-paypal-v6-samples/server/node/src/server.ts` | Express app: middleware, route mounting, port |
| `raw/github-paypal-v6-samples/server/node/src/paypalServerSdkClient.ts` | PayPal server SDK client init with credentials |
| `raw/github-paypal-v6-samples/server/node/src/routes/ordersRouteHandler.ts` | Create order, capture order endpoints |
| `raw/github-paypal-v6-samples/server/node/src/routes/vaultRouteHandler.ts` | Setup token + payment token endpoints |
| `raw/github-paypal-v6-samples/server/node/src/routes/authRouteHandler.ts` | Browser-safe client token endpoint |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/recommended/app.js` | Standard PayPal one-time payment (recommended pattern) |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/redirect/app.js` | PayPal payment with redirect presentation mode |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/directAppSwitch/app.js` | Direct app switch for mobile PayPal app |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/hydrateEligibleMethods/app.js` | Server-side eligibility hydration pattern |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/merchantAsyncValidation/app.js` | Async merchant validation before checkout |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/paymentHandler/app.js` | Custom payment handler pattern |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/html/src/advanced/sandboxedIframe/src/merchant-example/app.js` | PayPal in sandboxed iframe |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePayment/typescript/src/app.ts` | TypeScript variant of standard PayPal payment |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/oneTimePaymentWithVault/html/src/recommended/app.js` | PayPal one-time payment + vault save |
| `raw/github-paypal-v6-samples/client/components/paypalPayments/savePayment/html/src/app.js` | Save PayPal without purchase (VAULT_WITHOUT_PAYMENT) |
| `raw/github-paypal-v6-samples/client/components/cardFields/oneTimePayment/html/src/recommended/app.js` | Card Fields standard one-time payment |
| `raw/github-paypal-v6-samples/client/components/cardFields/oneTimePayment/html/src/advanced/threeDSecure/app.js` | Card Fields with 3DS verification |
| `raw/github-paypal-v6-samples/client/components/cardFields/savePayment/html/src/app.js` | Card Fields save/vault without purchase |
| `raw/github-paypal-v6-samples/client/components/venmoPayments/oneTimePayment/html/src/app.js` | Venmo one-time payment |
| `raw/github-paypal-v6-samples/client/components/googlepayPayments/oneTimePayment/html/src/app.js` | Google Pay via SDK v6 |
| `raw/github-paypal-v6-samples/client/components/applepayPayments/html/src/app.js` | Apple Pay via SDK v6 |
| `raw/github-paypal-v6-samples/client/components/paypalGuestPayments/html/src/recommended/app.js` | Guest checkout (card without PayPal account) — standard |
| `raw/github-paypal-v6-samples/client/components/paypalGuestPayments/html/src/onload/app.js` | Guest checkout — auto-start on page load |
| `raw/github-paypal-v6-samples/client/components/paypalGuestPayments/html/src/shipping/app.js` | Guest checkout with shipping callbacks |
| `raw/github-paypal-v6-samples/client/components/paypalSubscriptions/html/src/recommended/app.js` | PayPal subscriptions |
| `raw/github-paypal-v6-samples/client/components/paypalMessages/html/src/recommended/app.js` | Pay Later messaging (recommended) |
| `raw/github-paypal-v6-samples/client/components/paypalMessages/html/src/advanced/app.js` | Pay Later messaging (advanced/custom) |
| `raw/github-paypal-v6-samples/client/components/bankAchPayments/oneTimePayment/html/src/recommended/app.js` | ACH bank payment (US) |
| `raw/github-paypal-v6-samples/client/components/sepaPayments/html/src/app.js` | SEPA direct debit (EU) |
| `raw/github-paypal-v6-samples/client/components/bancontactPayments/html/src/app.js` | Bancontact (Belgium) |
| `raw/github-paypal-v6-samples/client/components/blikPayments/html/src/app.js` | BLIK (Poland) |
| `raw/github-paypal-v6-samples/client/components/epsPayments/html/src/app.js` | EPS (Austria) |
| `raw/github-paypal-v6-samples/client/components/idealPayments/html/src/app.js` | iDEAL (Netherlands) |
| `raw/github-paypal-v6-samples/client/components/p24Payments/html/src/app.js` | Przelewy24 (Poland) |
