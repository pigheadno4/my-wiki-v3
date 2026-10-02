---
title: "GitHub: paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration"
type: source
date_ingested: 2026-08-17
date_updated: 2026-10-02
original_format: github-repo
raw_files:
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-10-02-06bc2de/manifest.json"
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-10-02-06bc2de-9592883c/manifest.json"
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/manifest.json"
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-08-16-f1c7123-dd2b315d/manifest.json"
tags: [paypal, braintree, web-sdk-v6, checkout, vault, billing-agreements, pay-later, messages, react, node-js, sample-app, github-repository]
---

## Overview

`paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration` is a runnable PayPal Checkout v6 sample specifically for Braintree merchants. This cumulative page preserves the first baseline, `main@f1c7123`, at exact SHA `f1c712374f674ce6f0b2683f105871dcb969d2d7`, and adds the returning-buyer sample at `main@06bc2de`, exact SHA `06bc2de96264a29f33ff7b6eb0d566c1cd162b0a`. The Browser Architecture through Venmo Boundary sections below retain baseline-qualified findings; the new commit section records subsequent changes.

Repository: <https://github.com/paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration>

## Evidence Boundary

- The first immutable snapshot retains 64 policy-selected files totaling 130,398 bytes. One test file totaling 1,151 bytes was excluded.
- A linked exact-SHA supplement retains React `index.html`, React `utils.ts`, and Node `.nvmrc`, closing dependencies discovered during packet review.
- The code demonstrates sample integration contracts at one commit. It does not prove production readiness, merchant enablement, regional availability, buyer eligibility, or behavior delegated to an uncollected runtime.
- This repository remains independent from `paypal/paypal-js` and `braintree/braintree-web`; their package-qualified histories must not be merged into this commit history.
- The October 2 collection retains 68 files (137,194 bytes) plus an approved two-file saved-payment frontend supplement (10,784 bytes). Additive full ingest used the user's one-item focused-reading exception: changed retained files, supplemental frontend and affected prior/dependency code were read fully; unchanged files and inventories were hash-checked. This is not a whole-repository read or runtime test.

## Grounding Excerpts

> "sample PayPal integrations for Braintree merchants"
>
> `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/README.md:1-3`

> "PayPal and Venmo"
>
> `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/README.md:35-39`

> `planType: "RECURRING"`
>
> `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/client/paypalBillingAgreements/recurring/src/app.js:22-29`

> `if (eligibility.paylater)`
>
> `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/client/paypalOneTimePayments/smartStack/src/app.js:73-86`

> `submitForSettlement: true`
>
> `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/server/node/src/routes/transactionRouteHandler.ts:18-24`

## Merchant Setup

The sample requires Braintree sandbox merchant ID, public key, and private key values. It also instructs the merchant to create a PayPal sandbox business account, link it to the Braintree sandbox account, and enable the Vault and PayPal/Venmo application features.

These instructions establish the intended Braintree-account path. A checked feature box is not evidence that every funding source is implemented in this repository or enabled for a particular merchant.

## Browser Architecture

The static pages load Braintree Web `3.142.0` modules from the Braintree CDN. Each payment example follows the same base sequence:

1. Fetch a browser-safe Braintree client token from `/braintree-api/auth/browser-safe-client-token`.
2. Create `window.braintree.client` with that token.
3. Create `window.braintree.paypalCheckoutV6` from the Braintree client.
4. Call `loadPayPalSDK()` and construct the relevant payment or messaging session.
5. Tokenize approved payment data into a Braintree payment-method nonce.
6. Send the nonce to the merchant's Braintree server integration.

This is a Braintree processing path. It does not use PayPal Orders API create/capture calls directly.

## Demonstrated Payment Flows

### One-time checkout

The basic flow creates a capture-intent one-time session and sends its nonce and amount to the Node transaction route. The line-item variant supplies debit and credit items plus an amount breakdown. The shipping-callback variant changes shipping options and order amounts through `updatePayment()` when the buyer changes address.

The Smart Payment Stack calls `findEligibleMethods()` and conditionally presents Pay Later and PayPal Credit. Pay Later uses eligibility-provided country and product codes; Credit creates a one-time session with `offerCredit: true`. PayPal is presented without the same conditional branch in this sample, but sample rendering is not general eligibility proof.

### Checkout with vault

`createCheckoutWithVaultSession()` combines a `10.00 USD` capture with billing-agreement consent. After tokenization, the sample calls Braintree `transaction.sale()` with `storeInVaultOnSuccess: true` and `submitForSettlement: true`.

### Billing agreements

The basic billing-agreement flow saves a PayPal account without a purchase. Additional examples pass plan metadata for:

- `RECURRING`: a monthly variable-price example with 12 executions;
- `SUBSCRIPTION`: a fixed-price monthly example with product, fee, shipping, tax, and total metadata; and
- `UNSCHEDULED`: an auto-reload-style pay-as-you-go example.

All three tokenize approval to a Braintree nonce and call the sample vault route. The repository demonstrates metadata construction and tokenization, not a complete merchant subscription scheduler or subsequent-charge engine.

### PayPal Messages

The Messages page creates a Braintree v6 Messages instance and renders `<paypal-message>` with amount, buyer-country, and currency attributes. It is promotional content, not a payment session, and it does not generate a nonce.

## React Integration

The React sample declares React `19.2.4`, `@paypal/react-paypal-js@^10.1.0`, and React Router `7.13.1`. Its `BraintreePayPalProvider` is backed by the Braintree CDN scripts loaded in the supplemented HTML entry point.

The retained application demonstrates prebuilt and custom-hook variants for:

- one-time payment;
- checkout with vault; and
- billing-agreement save-without-payment.

Its product and cart state is browser-side demonstration state. Product data comes from the sample server, but cart totals are calculated in React and then posted to the transaction route.

## Node Server

The Node 20 sample declares `braintree@^3.36.0`, Express 5, Zod 4, and TypeScript. It exposes routes for:

- generating a Braintree client token;
- returning a small product catalog;
- creating a transaction sale from a nonce; and
- creating a customer and saving a payment method.

The Braintree gateway is hard-wired to `braintree.Environment.Sandbox`. Transaction sales set `submitForSettlement: true`; checkout-with-vault can additionally set `storeInVaultOnSuccess`.

## Production Limitations

> [!warning] Client-controlled amount
> The transaction route accepts `amount` directly from the request body. Although client comments say production should obtain the final amount from the server, the retained server does not rebuild or validate the amount from its product catalog. Production code must derive the payable amount from trusted server-side cart and pricing data.

> [!warning] Customer identity and server hardening
> The vault-only route creates a new Braintree customer for every request rather than associating the nonce with an authenticated merchant customer. The server also enables unrestricted CORS and returns exception text to clients. Authentication, authorization, customer mapping, bounded CORS, safe error responses, idempotency, and durable transaction state are outside this sample.

The sample does not inspect settlement results before displaying client success text. Merchants must validate Braintree responses and persist authoritative transaction state rather than treating HTTP completion or browser messaging as settlement proof.

## Venmo Boundary

The README tells merchants to enable the PayPal/Venmo application feature, but no retained example constructs a Venmo payment session. The implemented Smart Payment Stack covers PayPal, Pay Later, and PayPal Credit. Therefore this baseline does not establish a working Venmo checkout integration; use independently collected Braintree Web or current product documentation for that question.

## `default-branch@06bc2de` - View/Edit Saved Payment

The October 1 commit adds a static returning-buyer example and changes server token generation and transaction submission. The comparison identifies five actual upstream changes within its selected pathspec; three additional retained paths (React HTML, React utility and Node `.nvmrc`) match the earlier supplement byte-for-byte and are not new behavior. Sixty retained snapshot paths are unchanged.

### Integration sequence

1. Obtain an existing vaulted PayPal account. The basic billing-agreement example now displays `paymentMethod.token` as `vaultId`, plus `customerId`, after vaulting. Its unchanged vault route creates a new customer per request; it is not production customer mapping.
2. The new page accepts either identifier and calls `/braintree-api/auth/browser-safe-client-token`. An explicit nonempty `preferredPaymentMethodToken` wins; otherwise customer lookup selects a default PayPal account or the first account and throws if none exists. With neither identifier, the route retains ordinary client-token generation.
3. The new Node GraphQL helper sends the resolved token as `input.clientToken.paymentMethodId` to the sandbox `createClientToken` mutation. It uses server-side Braintree public/private keys and the `Braintree-Version: 2023-07-03` header. The helper's REST-equivalence comment is not independently verified API guidance.
4. The HTML loads Braintree Web `3.146.0`. `<paypal-saved-payment-methods>` already exists before a fresh Braintree client and `paypalCheckoutV6` adapter call `loadPayPalSDK()`. The edit session uses `10.00 USD`, `intent: "authorize"` and `commit: false`; clicking the element calls `start({ presentationMode: "auto" })`.
5. Approval passes `orderId` and `payerId` to `tokenizePayment()` and stores the returned nonce. A separate Submit Order action sends that nonce if present, otherwise the resolved persistent vaulted token.
6. The sale route now accepts either `paymentMethodNonce` or `paymentMethodToken`, requires exactly one truthy value, and requests `submitForSettlement: true`. The XOR check is not identifier-format or ownership validation. This is a Braintree transaction, not PayPal Orders API capture.

### Source-qualified code fragments

These excerpts illustrate the sample contract, not a production-ready integration. The frontend must be paired with authenticated server-side ownership checks and authoritative payment-result handling.

```javascript
editSavedPaymentSession =
  editPaypalCheckoutV6Instance.createEditSavedPaymentSession({
    amount: ORDER_AMOUNT,
    currency: "USD",
    intent: "authorize",
    commit: false,
    async onApprove(data) {
      const payload = await editPaypalCheckoutV6Instance.tokenizePayment({
        orderId: data.orderId,
        payerId: data.payerId,
      });
      approvedNonce = payload.nonce;
    },
  });
```

The excerpt omits the sample's alert, cancellation and error callbacks. Its later submission chooses the payment source separately:

```javascript
const transactionResult = await completePayment(
  approvedNonce
    ? { paymentMethodNonce: approvedNonce }
    : { paymentMethodToken: vaultConfig.vaultId },
);
```

Frontend evidence: [saved-payment app](../../../../raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-10-02-06bc2de-9592883c/files/client/paypalEditSavedPayment/src/app.js), [HTML and CDN versions](../../../../raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-10-02-06bc2de-9592883c/files/client/paypalEditSavedPayment/src/index.html). Server evidence: [preferred-token GraphQL helper](../../../../raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-10-02-06bc2de/files/server/node/src/braintreeGraphQlClient.ts), [token route](../../../../raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-10-02-06bc2de/files/server/node/src/routes/authRouteHandler.ts), [sale route](../../../../raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-10-02-06bc2de/files/server/node/src/routes/transactionRouteHandler.ts).

### React and repository boundaries

The unchanged React entry still loads Braintree Web `3.142.0`, declares `@paypal/react-paypal-js@^10.1.0`, and uses ordinary client tokens and nonce submission. The new static page is not a React edit wrapper and does not establish an update to `paypal/paypal-js`. The adapter API is independently evidenced in [[source-github-braintree-web]] at `3.146.0`; returning-buyer vault-initiated checkout already existed in the retained `3.143.0` baseline. This commit is not the first evidence of all returning-buyer checkout.

### Production caveats and contradiction

> [!warning] Customer/token ownership
> The retained server wiring does not authenticate ownership of client-supplied customer IDs or preferred vault tokens. Production must resolve permitted saved methods from authenticated server-side identity rather than trust these query parameters. Keep API credentials server-side, derive trusted order amounts, restrict CORS, sanitize errors and debug output, and persist transaction/idempotency state.

> [!warning] Contradiction
> The frontend unconditionally displays "Order successfully captured!" after JSON completion, without checking HTTP status, `transactionResult.success` or transaction state. That message is not proof of authorization, capture or settlement. The same discrepancy is recorded in [[paypal-braintree-integration]]. Tokenization and submission also do not establish a durable change to the default vaulted funding instrument.

Setup clears a prior approved nonce, but cancellation/error callbacks do not. The submit button is disabled during its fetch, not throughout editing, and no teardown or durable edit-result reconciliation is demonstrated. These are static code-review caveats, not reproduced browser failures. No build, wallet session, sandbox payment or eligibility test was executed.

### Update grounding excerpts

- `paymentMethodId: preferredPaymentMethodToken,` - `server/node/src/braintreeGraphQlClient.ts` in the current snapshot.
- `"Provide exactly one of paymentMethodNonce or paymentMethodToken"` - `server/node/src/routes/transactionRouteHandler.ts` in the current snapshot.
- `intent: "authorize",` and `commit: false,` - `client/paypalEditSavedPayment/src/app.js` in the current supplement.
- `: { paymentMethodToken: vaultConfig.vaultId },` - the same supplemented app's submission branch.
- `src="https://js.braintreegateway.com/web/3.146.0/js/client.min.js"` - supplemented `client/paypalEditSavedPayment/src/index.html`.

## Related

- Company: [[paypal]]
- Concept: [[paypal-braintree-integration]]
- Repository history: [[changelog-github-v6-web-sdk-with-braintree-sdk-sample-integration]]
- Independent client SDK evidence: [[source-github-braintree-web]]
- Independent React package evidence: [[source-github-paypal-js]]
- Independent server SDK evidence: [[source-github-braintree-node]]

## Raw Sources

- [Current snapshot manifest](../../../../raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-10-02-06bc2de/manifest.json) - immutable 68-file commit evidence
- [Current frontend supplement manifest](../../../../raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-10-02-06bc2de-9592883c/manifest.json) - two approved exact-SHA saved-payment files
- [Commit comparison](../../../../tracking/github/repos/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/comparisons/default-branch/f1c7123--06bc2de/comparison.md) - selected upstream transition, not a semantic package release
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/manifest.json` - immutable 64-file exact-SHA baseline
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/README.md` - repository purpose and merchant setup
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/client/paypalOneTimePayments/smartStack/src/app.js` - PayPal, Pay Later, and Credit eligibility flow
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/client/paypalBillingAgreements/recurring/src/app.js` - recurring billing-agreement metadata and nonce flow
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/client/paypalCheckoutWithVault/basic/src/app.js` - capture plus vault
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/server/node/src/routes/transactionRouteHandler.ts` - Braintree transaction sale boundary
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/server/node/src/routes/paymentMethodRouteHandler.ts` - sample customer and payment-method creation
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-08-16-f1c7123-dd2b315d/manifest.json` - linked React and Node dependency supplement
