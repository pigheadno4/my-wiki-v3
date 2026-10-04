---
title: "Braintree Local Payment Methods Server-Side Implementation — Node.js"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/server-side/node"
raw_files:
  - "braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16.md"
  - "braintree/docs/guides/local-payment-methods/client-side-custom/android/v5-2026-09-16.md"
tags: [braintree, local-payment-methods, node-js, webhooks, transactions]
---

## Overview

This collected Braintree developer guide is the Node.js server-side route for completing a Local Payment Method transaction when the server receives a payment-method nonce from either the returning client or a Local Payment Method webhook. It is a captured documentation snapshot for [[braintree]] and [[braintree-payment-methods]], not evidence of current method availability, merchant or buyer eligibility, environment configuration, successful execution, settlement or funding.

## Key takeaways

- A buyer leaves the merchant checkout to approve the payment through an app, website or bank and may not return after the bank payment succeeds. The server integration must support both documented transaction-creation paths: a nonce sent by the returning client and a nonce contained in the Local Payment Method webhook when the buyer does not return.
- Webhooks are therefore a critical server-side prerequisite. The guide recommends storing the payment ID returned when the payment starts and mapping it to a cart or other identifier, so the webhook's payment ID can locate the pending order.
- If the merchant requires the buyer to return and cannot create the transaction within three hours after invoking checkout, the page says Braintree will automatically refund the money. When no transaction was created, Braintree initiates the refund and sends a `local_payment_reversed` webhook; the page says the buyer should expect the returned funds within two to three days.
- The payment-method nonce is single-use and Local Payment Methods support one-time payments only. The server-side Transaction Sale request must set `submitForSettlement` to `true`; calling Transaction Sale twice for the same Local Payment Method by using both the client nonce and webhook nonce produces the documented validation error. Submission for settlement is not evidence that settlement or merchant funding completed.
- The transaction currency must match the currency set in the client integration. Vaulting payment methods and creating recurring transactions are not supported by this page's Local Payment Methods flow.
- After bank approval, Braintree updates the Payment Context and sends a webhook; if the buyer does not approve, the Payment Context eventually expires. The Node.js page calls the Payment Context GraphQL API an alternative to webhooks, but the fully read Android v5 client guide says merchants must implement Braintree webhooks to accept Local Payment Methods. The snapshots do not explain whether the GraphQL route replaces every webhook responsibility, so do not treat it as a blanket webhook exemption.

## Evidence boundaries

> [!warning] Payment lifecycle
> Keep bank approval or processing, a completed webhook notification, receipt of a nonce, Transaction Sale creation, submission for settlement, settlement and funding as distinct evidence points. The page's examples create a transaction and request settlement submission; they do not prove completed settlement or funding.

> [!warning] Nonce and duplicate handling
> The client-return nonce and webhook nonce are alternative inputs for the same Local Payment Method transaction path. Do not interpret them as permission to create two sales: the page says a second Transaction Sale call for the same Local Payment Method results in a validation error.

> [!warning] Method, timing and environment scope
> This server-side page does not classify every Local Payment Method as instant or non-instant, and its three-hour auto-refund condition applies to the described no-return/no-transaction case. The captured Node.js examples do not identify an executed Sandbox or Production environment and do not establish current method availability or eligibility.

> [!warning] Webhook versus GraphQL scope
> The Node.js page's closing GraphQL-alternative note is unresolved against both its own statement that webhooks are critical and the Android v5 guide's mandatory-webhook statement. These snapshots do not establish that Payment Context GraphQL replaces the completion, reversal or other notification responsibilities documented for this flow.

## Detail locators

- Unsupported vaulting and recurring transactions: `# Server-Side Implementation`, lines 17–18.
- Buyer redirect, possible non-return after bank processing, webhook transaction route, three-hour auto-refund and `local_payment_reversed` notification: `## Local Payment Method webhooks`, lines 23–31.
- Webhook prerequisite and completed-notification example payload: `### Configure webhooks`, lines 34–48.
- Payment-ID storage and pending-order correlation: `### Configure webhooks`, lines 50–53.
- Required returning-client and webhook nonce paths: `## Creating transactions`, lines 54–59.
- Single-use, one-time scope and required `submit_for_settlement`: `## Creating transactions`, lines 61–62.
- Optional `order_id` and `descriptor_name` fields plus callback and Promise Transaction Sale examples: `### Optional fields` through `### Promise`, lines 63–114.
- Duplicate Transaction Sale validation error: `## Creating transactions`, lines 116–117.
- Client/server currency match: `## Currency support`, lines 120–123.
- Payment Context approval update, webhook, expiry and GraphQL-alternative note: `## Payment Contexts`, lines 124–130.
- Android v5 mandatory-webhook statement: supporting raw `### Invoke payment flow`, lines 211–212.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Server integration route: [[braintree-server-sdk]]
- Notification route: [[braintree-webhooks]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following collected pages were not used as factual authority for this source entry; they are exact-file navigation for follow-on implementation work:

- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]]
- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Node.js Local Payment Method webhook reference]]
- [[raw/braintree/docs/reference/general/validation-errors/all/node-2026-09-16|Node.js validation-error reference]]
- [[raw/braintree/graphql/integration_guides/local_payment_contexts-2026-09-16|Local Payment Contexts GraphQL integration guide]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Braintree Local Payment Methods Server-Side Implementation — Node.js (captured 2026-09-16)]] - complete primary page covering the client-return and webhook nonce paths, transaction creation, refund and reversal handling, one-time settlement submission, duplicate-sale validation, currency matching and Payment Context transitions
- [[raw/braintree/docs/guides/local-payment-methods/client-side-custom/android/v5-2026-09-16|Braintree Local Payment Methods Client-Side Implementation — Android v5 (captured 2026-09-16)]] - fully read supporting authority for the mandatory-webhook statement that qualifies the Node.js page's unresolved GraphQL-alternative note
