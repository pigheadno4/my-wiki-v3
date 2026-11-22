---
title: "Stripe — Orchestration: Route Payments to Multiple Processors"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/orchestration/route-payments"
raw_files:
  - "stripe-payments-orchestration-route-payments-2026-11-07.md"
  - "stripe-orchestration-route-payments-2026.md"
tags: [stripe, orchestration, multi-processor, routing, payment-record, webhooks, private-preview]
---

## Summary

[[stripe]]’s May 11 and November 7, 2026 guides show how to use [[stripe-orchestration]] to select a payment processor using Dashboard rules. Rules can match card country, amount, currency and other conditions and configure one optional cross-processor retry. Both guides identify private preview and representative-led onboarding. November adds an email-based access request. Onboarding checks that the destination processor and Stripe integration are supported and requires entering the destination processor’s API keys in the Dashboard. See May lines 8-20 and November lines 9-33.

November explicitly says Link credentials cannot transfer between processors, so Link transactions bypass routing rules and Stripe processes them regardless of configuration. The May product overview already lists Link as excluded from routing feature support. Apple Pay and Google Pay have a separate routing guide for supported configurations. See [[source-stripe-orchestration]] and [[source-stripe-orchestration-wallet-payments]].

## Sandbox and Server Integration

1. Select the sandbox in the Dashboard account picker, add test rules, then activate them. The November examples use the selected sandbox’s API key. See November lines 39-54.
2. Set `payments_orchestration[enabled]=true` when the server creates a PaymentIntent. Billing, Checkout Sessions, Payment Links and Dashboard payments automatically create PaymentIntents. Contact a Stripe representative to configure those PaymentIntents to use Orchestration.
3. Verify a test payment under **Processor** or **Recent activity** in Dashboard. Alternatively, use the PaymentIntent’s `payment_record` ID to retrieve the record through the API or inspect it in Workbench and read `processor_details`. See November lines 69-112.
4. After sandbox testing, configure and activate live rules on the onboarded integration. A successful sandbox test establishes test routing for that setup. See [[source-stripe-orchestration-rules]] and November lines 208-220.

The guides exclude the Setup Intents API and flexible acquiring features on other processors. For transactions involving a 3D Secure request, supply the Acquirer BIN for the destination processor.

## Execution History, Reporting and Payment Outcome

The Payment Record provides execution history for payments with Orchestration enabled. The example retains the same `payment_record` ID throughout the PaymentIntent lifecycle and generates an attempt record each time the PaymentIntent is confirmed. The November diagram shows the Payment Record’s `latest_payment_attempt_record` link. See [[source-stripe-payment-records]] and November lines 84-119, 121-155 and 178-206.

For external routing, Stripe creates Payment Records and Payment Attempt Records in place of Charges. The example sets `latest_charge` to `null`. If internal reporting or reconciliation relies on Charges, the guides direct you to use Payment Attempt Records across **all Stripe volume**. External payments lack Stripe Balance Transactions because their funds do not move through the Stripe account.

When another processor handles a card payment, Stripe reports `processing` and sends `payment_intent.processing`, which can support a temporary inventory hold. After the processor reports capture, Stripe transitions the PaymentIntent to `succeeded` and sends `payment_intent.succeeded`. Existing handlers that fulfill from the latter event need no change according to both guides. A return URL, processor selection, processor-reported capture and Stripe-account settlement identify different stages.

Dashboard analytics can take up to two days to populate. For externally processed payments, the Dashboard lacks balance summary and activity reports, dispute status and receipts. See November lines 212-220.

## Error Prevention and Retry Eligibility

Onboarding opt-in enables error prevention. If a selected main or retry processor cannot support a required feature, Orchestration attempts the payment on Stripe instead of returning the unsupported-feature error. If Stripe is the main processor and the payment fails there, Stripe evaluates whether the configured retry processor can handle the payment and skips the retry if it cannot. The November feature-support guide says failover from Stripe ignores error protection to avoid a duplicate Stripe attempt. Other retry conditions still apply, including unsuccessful 3DS and features the retry processor cannot handle. See May lines 171-175, November lines 222-226, [[source-stripe-orchestration-feature-support]] and [[source-stripe-orchestration-retries]].

## Dated API Examples

The May 11 guide uses Node.js for two PaymentIntent-create samples with `payment_method_types: ["card"]` and for Payment Record retrieval. The November 7 guide uses cURL and the two PaymentIntent examples include `return_url` and omit the explicit card list. The changed samples leave the reason, the request API version and any universal return-URL requirement unstated. The sandbox button label changes from **Add rules** to **Add test rules**. Text diagrams expose existing object and webhook links in the same illustrated flow. The two create arrows identify a single illustrated PaymentIntent flow, and its `2025-01-27` value is the sample webhook event version.

The separate removal changelog’s REST links and table identify the affected PaymentIntent Create endpoint as `2026-09-30.endive`. It documents HTTP 400 (`payment_method_types_no_longer_supported`) when sending the older writable request parameter at that endpoint. The response property remains computed and read-only. The same changelog’s Impact paragraph separately names `2026-08-26.preview`. Check the versioned endpoint before reusing the May samples. See May lines 38-52, 61-75 and 128-134 and November lines 56-65, 73-82 and 178-185.

## Related Pages

- [[stripe-orchestration]] — routing, product constraints and related guides.
- [[source-stripe-orchestration]] — product and processor overview.
- [[source-stripe-orchestration-rules]] — conditions, actions and rule lifecycle.
- [[source-stripe-orchestration-retries]] — eligibility, 3DS and retry outcomes.

## Raw Sources

- [[raw/stripe-payments-orchestration-route-payments-2026-11-07|Stripe’s November 7, 2026 routing implementation guide]]
- [[raw/stripe-orchestration-route-payments-2026|Stripe’s May 11, 2026 routing implementation guide]]

## Related raw API references

- [[raw/stripe-changelog-endive-2026-09-30-removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents-2026-11-07|Endive PaymentIntent and SetupIntent request-parameter changelog]] — November 7, 2026 capture, lines 5-36.
