---
title: "Stripe Orchestration"
type: concept
category: technology
tags: [stripe, orchestration, multi-processor, routing, retries, payment-routing, private-preview]
---

## Overview

Stripe Orchestration is a private-preview layer for routing card payments across supported processors. The November 2026 overview adds an email request form. Requesting access, representative-led onboarding, testing rules in a sandbox, and activating rules in the live account are separate steps. Third parties remain the processors for payments routed to them, with fees and liability under their own terms. See [[source-stripe-orchestration]].

## Features

- **Multi-processor routing**: Route via PaymentIntents integration or auto-route from Billing, Checkout, Payment Links, or Dashboard
- **Retry on different processor**: Configure rules to automatically retry failed payments with alternative processors
- **Performance monitoring**: Analyze payment performance across processors
- **Post-transaction flows**: Refunds via Stripe Dashboard/Refunds API; third-party processors manage their own refunds
- **Sandbox rule testing**: Test routing rules before live activation

## Supported Products

Cards only via: Payments, Billing, Dashboard payments.

## Supported Processors and Feature Matrix

Three processors currently supported: **Adyen**, **Braintree**, **Worldpay WPG**.

| Feature | Adyen | Braintree | Worldpay WPG |
| --- | --- | --- | --- |
| Auto/manual capture, refunds, 3DS, statement descriptors, wallets, recurring | ✓ | ✓ | ✓ |
| Network tokens | ✓ | ✓ | ✗ |
| Processor account overrides (November 7, 2026 matrix) | ✓ | ✗ | ✓ |

Key exceptions: multicapture unsupported; `statement_descriptor_suffix_kanji` unsupported; `statement_descriptor_suffix_kana` Adyen only; 3DS + Apple Pay/Google Pay DPAN unsupported; Google Pay FPAN unsupported on Adyen.

Unsupported processor features return HTTP 400 `orchestration_unsupported` by default, naming the first unsupported feature. An onboarding opt-in for error protection can trigger a Stripe fallback attempt. See [[source-stripe-orchestration-feature-support]].

## Explicitly Not Supported

The November 7, 2026 overview excludes non-card payments, Link, Capital, Connect, Terminal, Organizations, disputes and settlement-related activity. The November routing guide explains that Link credentials cannot transfer between processors. Stripe processes Link outside the configured routing rules. Apple Pay and Google Pay have separate wallet and processor conditions.

The May 11 overview also lists Radar for third-party routed payments and Sigma as exclusions. November omits both names, leaving their support undetermined. The separate retry guide says a Stripe-main payment blocked by Stripe, for example through Radar, is treated as a decline and can be retried on the selected processor under documented conditions. See [[source-stripe-orchestration]] and [[source-stripe-orchestration-retries]].

## Rule Conditions (7)

| Condition | Notes |
| --- | --- |
| Amount | Must also specify currency |
| BIN | First 6 or 8 digits of card |
| Card country | Card issuing country |
| Card issuer | Issuing financial institution |
| Card type | credit / debit / prepaid |
| Currency | Presentment currency |
| Metadata | PaymentIntent metadata fields |

Conditions are evaluated left to right and the first match wins. Choose a main processor and an optional retry processor for matching actions and for the separately configured no-match action. In the November rules guide, a supported processor action can override onboarding account logic with a configured account of that processor. Main and retry account selections are independent. Unset selections use the onboarding logic. The November matrix supports this override for Adyen and Worldpay WPG and marks it unsupported for Braintree. See [[source-stripe-orchestration-rules]] and [[source-stripe-orchestration-feature-support]].

**Rule lifecycle.** Save drafts without changing active routing. In a sandbox, create and activate test rules, then verify the test result. Recreate the rules in live mode before choosing **Activate rules** for live payments. The November guide scopes the limit to one active set per sandbox and one in live mode. Activation replaces the active set in that environment and a deactivated set can be reactivated. Active rules are read-only. Use **Duplicate test rules** or **Duplicate rules**, confirm, then edit the duplicate. Use **Deactivate test rules** or **Deactivate rules** and confirm when removing the active set. Payments in that environment route to Stripe when it has no active set. See [[source-stripe-orchestration-rules]].

## Cross-Processor Retry Behavior

Configure a retry processor in each rule's Action. Key edge cases:

| Scenario | Behavior |
| --- | --- |
| 3DS on the first main-processor attempt, with failed authentication or a failed payment after successful authentication | Skip the cross-processor retry and send `payment_intent.payment_failed`. |
| The configured retry processor lacks a required feature, such as Connect `on_behalf_of` | Skip the incompatible processor. A compatible configured processor can receive an otherwise eligible retry. Evaluate opt-in error protection and the original-Stripe failover exception separately. See [[source-stripe-orchestration-retries#Unsupported-feature validation and error protection|retry and fallback scope]]. |
| Stripe Radar blocks transaction (main = Stripe) | Treated as decline → **retried on retry processor** |
| Adaptive Acceptance + Stripe is main processor | Stripe may internally retry before cross-processor retry triggers |
| Stripe is retry processor + Adaptive Acceptance enabled | Potentially 2 retries (1 cross-processor + 1 Adaptive Acceptance) |

## API Integration

Enable on PaymentIntent: `payments_orchestration: { enabled: true }`. Routing rules configured in the Dashboard apply.

For Billing, Checkout Sessions, Payment Links, and Dashboard payments (which auto-create PaymentIntents), contact Stripe representative to enable Orchestration.

## New API Objects (Breaking Change)

For payments with Orchestration enabled, the Payment Record contains execution history. The guide’s example keeps `payment_record` stable through the PaymentIntent lifecycle and generates a new attempt record at confirmation. For payments routed to third-party processors, Stripe creates **Payment Records** and **Payment Attempt Records** instead of Charges. Retrieve using the Payment Record ID:

```js
stripe.paymentRecords.retrieve('{{PAYMENT_RECORD_ID}}')
```

`latest_charge: null` in the PaymentIntent when routed to a third party.

## Reporting and Webhook Changes

**Reporting breaks**:

- Third-party routed payments have no Stripe Charges. If reporting or reconciliation relies on Charges, use Payment Attempt Records across all Stripe volume.
- No Balance Transactions for third-party volume (funds don't flow through Stripe)

**Webhook changes** for third-party routed payments:

- New `processing` status + `payment_intent.processing` event (useful for inventory holds)
- After the external processor reports capture, Stripe transitions the PaymentIntent to `succeeded` and sends `payment_intent.succeeded`. Existing fulfillment handlers based on that event need no change according to the routing guide.

## Integration Limitations

- Setup Intents API: not supported
- Flexible acquiring features: not available on other processors
- 3DS: must provide Acquirer BIN for destination processor
- Dashboard: no balance summary, dispute status, or receipts for third-party; data up to 2 days lag

## Error Prevention Mode

When onboarding error protection is enabled, Orchestration can try Stripe if the selected main or retry processor lacks a required feature. If Stripe was already tried, failover ignores error protection to avoid a duplicate Stripe attempt. An otherwise eligible payment can still use a compatible configured retry processor. When Stripe was main and its attempt fails, Orchestration checks whether the selected retry processor can handle the payment and skips it if incompatible. An attempted Stripe fallback can also fail. Without applicable fallback, unsupported-feature request validation can return HTTP 400 `orchestration_unsupported` and name the first unsupported feature. See [[source-stripe-orchestration-feature-support]], [[source-stripe-orchestration-route-payments]] and [[source-stripe-orchestration-retries]].

## Wallet Payments (Apple Pay / Google Pay)

The November [[source-stripe-orchestration-feature-support|feature matrix]] lists Apple Pay and Google Pay on Adyen, Braintree and Worldpay WPG, subject to wallet-token and processor limits. 3DS is unsupported for Apple Pay or Google Pay DPANs, and Adyen does not support Google Pay FPAN. To attempt a charge with a saved mobile-wallet method, pass `off_session=true` during PaymentIntent confirmation. When the customer is present at checkout, re-prompt through the applicable wallet integration. See [[source-stripe-orchestration-wallet-payments]] for processor setup and sandbox test routing.

## Relationship to Other Products

- [[stripe-vault-and-forward]]: Forwards card data (PANs) to external processors. Orchestration routes *transactions*; Vault and Forward routes *card data*. Complementary.
- [[stripe-off-session-payments]] and [[source-stripe-off-session-payments-api]] describe a separate API for off-session payments. Its November routing companion documents card-only opt-in to Orchestration with access to both private previews, an onboarded processor, and an active routing configuration. It excludes Connect, raw card data, and Smart Retries for this combined path. An optional routing-rule retry processor is a separate control.

## Sources

- [[source-stripe-orchestration]] — May and November 2026 overview: private-preview request, processor responsibilities and refunds, dated Radar and Sigma exclusions, and the distinct Link, wallet, and Off-Session Payments routes
- [[source-stripe-orchestration-route-payments]] — May and November 2026 implementation guides for private-preview onboarding, sandbox rules, Payment Records, capture webhooks and error prevention.
- [[source-stripe-orchestration-rules]] — rule conditions (7), execution order, rule lifecycle
- [[source-stripe-orchestration-retries]] — private-preview rule setup, first-attempt 3DS, incompatible processor skips, Stripe-main blocks and Adaptive Acceptance ordering
- [[source-stripe-orchestration-feature-support]] — feature matrix (Adyen/Braintree/Worldpay WPG), error code orchestration_unsupported, error protection opt-in
- [[source-stripe-orchestration-wallet-payments]] — Apple Pay and Google Pay routing, processor and token limits, saved versus customer-present attempts, and November private-preview request context
