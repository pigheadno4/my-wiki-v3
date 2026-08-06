---
title: "GitHub: paypal-examples/paypal-sdk-server-side-integration"
type: source
date_ingested: 2026-08-05
original_format: github-repo
raw_files:
  - "github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/manifest.json"
tags: [paypal, checkout, orders-api, subscriptions, hosted-fields, server-side, partners, samples, github-repository]
---

## Overview

`paypal-examples/paypal-sdk-server-side-integration` is a historical PayPal client/server sample pinned to commit `5409a3b9c0b6d0049fc3be9386092759fd6a1d5c`, authored and committed on 2023-09-28. It combines browser examples with a Fastify/TypeScript merchant server for Orders, Hosted Fields, shipping changes, and Subscriptions create, activate, and revise flows.

Repository: <https://github.com/paypal-examples/paypal-sdk-server-side-integration>

## Evidence Boundary

- The immutable capsule retains 36 files totaling 101,281 bytes and excludes two tests totaling 4,537 bytes.
- The package declares `@paypal/paypal-js` `^5.1.5`, while the browser examples load JS SDK 5.1.4. This is version-qualified 2023 sample evidence, not current PayPal integration or product-availability guidance.
- Sample presence does not establish merchant eligibility, regional availability, account enablement, certification, or production readiness.
- The sample contains implementation defects. They are documented below and must not be silently normalized into recommended behavior.
- Current integrations should prefer official current documentation and the newer [[source-github-v6-web-sdk-sample-integration]] evidence where applicable.

## Grounding Excerpts

> "replace the client-side code to call your server instead, and then return the order ID created on your server"
>
> `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/docs/update-from-client-side-helpers-to-server-side-for-partners.md:57-65`

> "Keep sensitive data, such as order amount, on the server to prevent tampering by outside actors."
>
> `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/docs/update-from-client-side-helpers-to-server-side-for-partners.md:239-242`

> "The client credentials auth token returned by `/v1/oauth2/token` API endpoint should never be passed to the browser."
>
> `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/docs/update-from-client-side-helpers-to-server-side-for-partners.md:244-254`

> "For 5xx capture errors specifically, implement optional idempotent retry"
>
> `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/src/order/capture-order.ts:44-60`

> "validate the captured amount was as expected before doing anything automated for order fulfillment/delivery"
>
> `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/src/controller/order-controller.ts:165-173`

## Server Architecture and Credentials

The Fastify application exposes configuration, client-token, order, shipping-patch, and subscription routes. PayPal client ID and secret remain in server environment variables. The OAuth helper requests `/v1/oauth2/token`, and both OAuth and client-token responses are cached in process memory using their `expires_in` values as TTLs, without an early-expiry safety margin.

Order amount construction is server-owned: the browser submits SKU and quantity, while the server resolves product name, description, SKU, unit price, and currency from `src/data/products.json`. The capture handler instructs implementers to validate the captured amount before fulfillment and to retain the PayPal transaction ID in merchant records.

## Orders and Partner Integrations

The Buttons example calls the merchant server to create an order, returns its ID to the JS SDK, then calls the merchant server to capture after buyer approval. The server supports `CAPTURE` or `AUTHORIZE` intent through configuration.

The partner migration guide retains two connected-merchant patterns:

- send `PayPal-Partner-Attribution-Id` for partner attribution;
- identify the merchant with `PayPal-Auth-Assertion`, or set the purchase-unit payee merchant ID where appropriate.

The guide propagates the authorization assertion to capture or authorize calls. Credentials and access tokens remain server-side.

Capture generates a UUID `PayPal-Request-Id`. On a 5xx response, the sample waits two seconds and retries once using the same request ID. Create Order does not generate an idempotency key, although the partner guide's migration example includes one.

For `INSTRUMENT_DECLINED`, the Buttons browser example calls `actions.restart()` so the buyer can choose another funding source. Other failures are surfaced to the page.

## Hosted Fields

The Hosted Fields example requests a client token from the merchant server, loads the JS SDK with `components=hosted-fields` and `data-client-token`, and checks `paypal.HostedFields.isEligible()`. The browser renders hosted number, CVV, and expiration fields, calls the merchant server to create an order, submits the fields, and then calls the merchant server to capture.

This older `paypal.HostedFields` evidence should not be treated as the current Card Fields contract. See [[paypal-expanded-checkout]] for current and package-qualified boundaries.

## Shipping Changes

The Buttons example sends the order ID and SDK-provided shipping address to `/patch-order`. The server retrieves the order, calculates shipping from country and state data, constructs JSON Patch operations for shipping, tax, amount breakdown, and total, then patches the PayPal order.

The implementation is useful as a historical orchestration example, but its input schema and amount arithmetic are defective as documented below.

## Subscription Flows

The repository demonstrates three Subscriptions API paths:

- Create: use `PAYPAL_SUBSCRIPTION_PLAN_ID`, default `user_action` to `SUBSCRIBE_NOW`, and return the created subscription to the JS SDK.
- Activate: create with `user_action: CONTINUE`, then call `/v1/billing/subscriptions/{subscriptionId}/activate` after buyer approval.
- Revise: call `/v1/billing/subscriptions/{subscriptionId}/revise` with `PAYPAL_SUBSCRIPTION_PLAN_ID_FOR_REVISE`.

These flows demonstrate endpoint orchestration only. They do not establish complete lifecycle management, retries, webhook handling, cancellation behavior, or current eligibility.

## Retained Defects and Limitations

> [!warning] API base URL override
> `PAYPAL_API_BASE_URL || env === "sandbox" ? sandbox : live` is parsed using JavaScript operator precedence so a nonempty custom override selects the sandbox constant instead of using the supplied URL. This contradicts the `example.env` override guidance.

> [!warning] Order retrieval
> `/get-order` defines `orderID` in the querystring schema but reads `request.body`. Its API helper parses every response once before branching and parses a non-success body a second time; its default error text also says `FAILED_TO_PATCH_ORDER`.

> [!warning] Shipping validation and arithmetic
> `/patch-order` requires only `orderID` even though the handler uses `shippingAddress`. Its amount reducer subtracts `discount` values after multiplying them by 100 while adding all other components without that scaling, which can produce an invalid total.

> [!warning] Subscription validation and revise result
> The create, activate, and revise schemas have empty required lists. Missing plan configuration becomes `String(undefined)`, and missing subscription IDs are passed onward. The revise browser discards the server response, returns the original ID, and displays success after approval.

> [!warning] Retry and typing defects
> Capture reuses its idempotency key but drops `Prefer: return=representation` on retry, despite calling it an identical request. Create Order supplies no generated `PayPal-Request-Id`. `src/order/order.d.ts` also declares a self-referential `HTTPStatusCodeSuccessResponse` alias.

The sample also leaves quantity without a positive minimum and can throw when an unknown SKU is destructured. These limitations reinforce its historical-example boundary.

## Related

- Company: [[paypal]]
- Checkout: [[paypal-checkout]]
- Expanded Checkout: [[paypal-expanded-checkout]]
- Subscriptions: [[paypal-subscriptions]]
- Current v6 sample: [[source-github-v6-web-sdk-sample-integration]]
- Repository history: [[changelog-github-paypal-sdk-server-side-integration]]

## Raw Sources

- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/manifest.json` - immutable exact-SHA baseline
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/docs/update-from-client-side-helpers-to-server-side-for-partners.md` - partner server-side migration, headers, credentials, and security guidance
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/src/controller/order-controller.ts` - order construction, capture handling, shipping patching, and route schemas
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/src/order/capture-order.ts` - capture idempotency and retry implementation
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/public/hosted-fields.html` - historical Hosted Fields browser flow
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/src/controller/subscription-controller.ts` - create, activate, and revise server routes
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/public/subscriptions/subscription-activate-example.html` - `CONTINUE` approval and activation browser flow
- `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/2026-08-04-5409a3b/files/public/subscriptions/subscription-revise-example.html` - plan-revise browser flow and retained response-handling defect
