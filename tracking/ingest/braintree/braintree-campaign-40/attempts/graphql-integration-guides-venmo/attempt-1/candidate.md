---
title: "Braintree GraphQL Venmo Integration Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides/venmo"
raw_files:
  - "braintree/graphql/integration_guides/venmo-2026-09-16.md"
tags: [braintree, graphql, venmo, payment-context, vault, authorization, transactions]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website page is a GraphQL integration guide for Venmo Payment Context creation, Vault storage and deletion, authorization, charging, business-profile selection and partial capture. It documents operation purposes and example request/response shapes; it is not a client-SDK implementation, an exact GraphQL schema baseline, or proof of current availability, account enablement, deployment, authorization, settlement or funding.

## Key takeaways

- `createVenmoPaymentContext` is explicitly intended for API-only merchants; the page sends web and mobile integrations to separate client-side guides. A Payment Context carries information shared among the merchant, Braintree and Venmo/PayPal, including payment intent, whether the method should be vaulted, and flags for selected customer-data collection. The displayed fields and `SANDBOX` response are examples, not a complete schema or evidence of environment parity or successful creation.
- `vaultPaymentMethod` is the documented route for saving a customer's Venmo account for later transactions. The page also shows an after-transaction vaulting option on `chargePaymentMethod` or `chargeVenmoAccount`. Those operations consume a `paymentMethodId`; this guide does not document how that identifier was created or establish SDK nonce equivalence, so use the separate nonce/single-use-method route for that terminology and lifecycle.
- Deleting a vaulted Venmo payment method from the merchant site or app also deletes the customer's Venmo merchant connection, except when duplicate Vault methods remain for the same Venmo account; the connection is removed only after the last duplicate is deleted. Conversely, a customer deleting the merchant connection in Venmo automatically removes the method from the merchant Vault. These are consequential cross-system deletions.
- `authorizeVenmoAccount` targets an eligible Venmo account and returns a transaction payload whose `status` must be inspected. `chargePaymentMethod` is the general transaction route shown with an amount and `paymentMethodId`, and the page directs merchants to submit client-collected device data. The displayed `AUTHORIZED` and `SUBMITTED_FOR_SETTLEMENT` values are illustrative responses, not proof of authorization, settlement or funding.
- `chargeVenmoAccount` is the route shown for selecting a Venmo business profile. The supplied `profileId` should match the profile used during client-side tokenization; omitting it associates the transaction with the default business profile. For physical goods shipped separately, the page also routes multiple partial settlements against one authorization through `partialCaptureTransaction`; the example-free statement does not prove capture or settlement success.

> [!warning] Scope, eligibility and environment boundary
> The snapshot states only that Venmo is available on supported iOS and Android devices and that Payment Context creation is for API-only merchants. It does not establish present compatibility, merchant approval, Venmo-profile setup, customer eligibility, Production enablement or Sandbox-to-Production parity. Use the dedicated Venmo payment-method guide for merchant/customer prerequisites and profile setup, and verify the applicable environment and account separately.

## Detail locators

- Supported-device availability statement and linked compatibility route: `# Venmo`, raw lines 14-19.
- API-only qualification, Payment Context purpose and linked complete input reference: `## Creating a Payment Context`, raw lines 22-28.
- `createVenmoPaymentContext` selection plus illustrative variables and response, including intent, usage, customer-client, environment, expiry, method, profile, amount and address-collection fields: raw lines 30-189.
- Explicit Vault reuse purpose, `vaultPaymentMethod` example and after-transaction vault option: `## Vaulting the Venmo account`, raw lines 191-244.
- Bidirectional merchant-connection/Vault deletion effects and duplicate-method qualification: `## Deleting a Vaulted Payment Method`, raw lines 247-251.
- Eligible-account authorization purpose, status inspection and illustrative `AUTHORIZED` response: `## Authorization`, raw lines 254-309.
- Client-collected device-data instruction, `chargePaymentMethod` amount/method input and illustrative `SUBMITTED_FOR_SETTLEMENT` response: `## Creating transactions`, raw lines 311-370.
- `chargeVenmoAccount`, same-profile tokenization condition, omitted-profile default and example payload: `## Specifying the business profile`, raw lines 372-438.
- Physical-goods multiple-shipment condition and `partialCaptureTransaction` route: `## Settlement`, raw lines 440-445.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Venmo eligibility, setup and payment-method lifecycle route: [[source-braintree-payment-methods-venmo]]
- SDK nonce and GraphQL single-use-method terminology route: [[source-braintree-payment-method-nonces]]

## Related raw API references

The page links to GraphQL reference entries for Payment Context, vault, authorization, charge, business-profile and partial-capture operations, and to separate client-side and Venmo-availability guidance. Those linked targets were not read as raw evidence for this entry and provide navigation only; they do not establish exact schema equivalence, SDK behavior, current eligibility, account enablement, environment availability or successful execution.

## Raw Sources

- [[raw/braintree/graphql/integration_guides/venmo-2026-09-16|Braintree GraphQL Venmo integration guide]] - complete collected page covering Payment Context creation, vaulting and deletion, authorization, transaction creation, business-profile selection and partial capture
