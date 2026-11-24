---
title: "Stripe — Migrate Basic Card Integration (Handle Auth)"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/payment-intents/upgrade-to-handle-actions
raw_files:
  - "stripe-payments-payment-intents-upgrade-to-handle-actions-2026-11-07.md"
  - "stripe-migrate-basic-card-integration-2026.md"
tags: [stripe, payment-intent, authentication, handle-card-action, confirmation-method, migration, legacy]
---

## Summary

The May 11 and November 7, 2026 [[stripe|Stripe]] guides upgrade the [[source-stripe-payments-without-auth|basic card integration]] to handle an issuer's request for payment authentication. They describe the manual confirmation flow and its client modal and server steps. Merchant, bank and geographic eligibility remain separate.

## Manual confirmation flow

1. The server removes `error_on_requires_action` and creates and confirms the PaymentIntent using `confirm=true` and `confirmation_method=manual`. When the issuer requests authentication, the PaymentIntent can enter `requires_action`.
2. Inspect the PaymentIntent's `status` and `next_action`. The May Express example returns `requiresAction` and the PaymentIntent client secret for the client to act. It handles `succeeded` as the payment-success branch.
3. The browser calls `stripe.handleCardAction(clientSecret)` to let the customer perform the required action. The successful action returns the PaymentIntent in `requires_confirmation`. If there is a client error, display it.
4. The client returns the same PaymentIntent ID to the server. The server uses its secret key to re-confirm that PaymentIntent within one hour. If the server misses the window, the attempt fails and returns to `requires_payment_method`. Verify `succeeded` before fulfillment in this guide's flow. Authentication completion leaves the payment awaiting server confirmation.

Both guides describe reusing the same merchant endpoint. May shows a full Express `/pay` branch that creates an Intent from `payment_method_id` or re-confirms from `payment_intent_id`. November keeps the client call to `/pay` and illustrates a cURL call to the PaymentIntent confirm endpoint. The November [[raw/stripe-api-payment-intents-confirm-2026-11-07|Confirm API reference]] describes the separate automatic confirmation flow, where client-handled actions require no further confirmation. See May lines 19–120 and 124–161, November lines 18–91, and the Confirm API at lines 7–17.

## Dated request and server examples

- **May 11, 2026.** The Node examples use `payment_method_types: ["card"]`. The fuller Express examples set `use_stripe_sdk: true` and include `generateResponse`, the creation and reconfirmation branches, and error handling. The first short create snippet omits `use_stripe_sdk`.
- **November 7, 2026.** The cURL create example uses `allowed_payment_method_types[]=card` without an explicit API version header. It omits `use_stripe_sdk` and replaces the full server response example with guidance to inspect status and next action. The separate November [[raw/stripe-api-payment-intents-create-2026-11-07|Create API reference]] (lines 708–709) and [[raw/stripe-api-payment-intents-confirm-2026-11-07|Confirm API reference]] (lines 659–660) document `use_stripe_sdk` as optional and say to set it to `true` when confirming server-side and handling next actions with Stripe.js, iOS or Android SDKs.

The [[raw/stripe-changelog-dahlia-2026-07-29-allowed-payment-method-types-parameter-2026-11-07|2026-07-29.dahlia changelog]] says `allowed_payment_method_types` filters out incompatible requested types instead of returning the earlier incompatible-type error. The response's `payment_method_types` property reports the resulting compatible subset. The allowlist request parameter is mutually exclusive with `payment_method_types`, `excluded_payment_method_types`, `automatic_payment_methods` and `payment_method_configuration`. The [[raw/stripe-changelog-endive-2026-09-30-removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents-2026-11-07|Endive REST changelog]] says the linked `2026-09-30.endive` PaymentIntent Create, Update and Confirm and SetupIntent Create and Update reject a writable `payment_method_types` with HTTP 400 and `payment_method_types_no_longer_supported`, while the response property remains read-only. Its Impact section also mentions `2026-08-26.preview`. The first affected version remains unresolved. The versioned references establish their own contract boundaries. See May lines 26–83 and 124–161 and November lines 27–46 and 81–91 for the examples.

## Sandbox and live authentication

Both guides describe a sandbox modal that can simulate successful or failed authentication and a live modal whose UI the issuer controls. Their test tables list a success card and an insufficient-funds card. Both also say test card `4000002500003155` requires authentication and fails with `authentication_not_handled` in this integration. The [[source-stripe-payments-without-auth|no-authentication guide]] lists that failure for its decline-only flow. The distinct [[raw/stripe-payments-payment-intents-migration-2026-11-07|Payment Intents migration guide]] describes authentication at setup or the first transaction for the same card. The two upgrade-guide tables and the surrounding action-handling instructions leave the fixture outcome in the upgraded flow unresolved. See May lines 163–171, November lines 93–101, and the separate migration guide at lines 181–190.

## Related Pages

- [[stripe]] — provider overview
- [[stripe-payment-intents]] — status, confirmation and versioned request fields
- [[source-stripe-payments-without-auth]] — earlier regional card flow
- [[stripe-3d-secure#Web Display Options|3D Secure web display options]]

## Raw Sources

- [[raw/stripe-payments-payment-intents-upgrade-to-handle-actions-2026-11-07]] — November 7, 2026 full migration guide
- [[raw/stripe-migrate-basic-card-integration-2026]] — May 11, 2026 full migration guide with the earlier Express examples
