---
title: "Stripe — Orchestration: Manage Rules"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/orchestration/rules"
raw_files:
  - "stripe-payments-orchestration-rules-2026-11-07.md"
  - "stripe-orchestration-rules-2026.md"
tags: [stripe, orchestration, rules, routing, multi-processor, private-preview]
---

## Summary

The May 11 and November 7, 2026 guides describe Stripe Orchestration as a private-preview feature for configuring routing rules in **Payments > Orchestration** in Dashboard. November adds an [email request for preview access](https://docs.stripe.com/payments/orchestration/rules.md#orchestration_preview), account overrides for supported processors and explicit sandbox and live rule controls. The registration example requests access through the documentation. Destination-processor support, Stripe account onboarding and integration eligibility are separate prerequisites. See [[source-stripe-orchestration-route-payments]].

## Rule Conditions

| Condition | Notes |
| --- | --- |
| Amount | Specify both amount and currency |
| BIN | First 6 or 8 card digits |
| Card country | Card's issuing country |
| Card issuer | Issuing financial institution |
| Card type | Credit, debit or prepaid |
| Currency | Supported presentment currency |
| Metadata | Request metadata, such as order details attached to a PaymentIntent |

## Execution Model

Stripe evaluates conditions left to right and applies the first matching action. Use the condition's overflow menu to move it left or right. Set a main processor and, optionally, a retry processor for a matching action. Configure the main and optional retry processors for the no-match action separately. With no active rules in the relevant environment, payments route to Stripe.

## Override Processor Account Logic

By default, Stripe uses the processor account logic configured during onboarding. In the November Dashboard flow, select a supported processor in the main or retry action, choose **Override processor account** under **Processor account logic**, and select an already configured account under **Processor account**. The selector shows accounts for the selected processor. Set accounts independently for the main and retry actions. Leaving either selection unset preserves the processor account logic from onboarding for that action. Contact your Stripe representative if the needed account is unavailable.

The November feature matrix supports processor account overrides for Adyen and Worldpay WPG and lists them as unsupported for Braintree. See [[source-stripe-orchestration-feature-support]]. An account override selects among the accounts of a chosen processor. The retry action governs whether a failed payment can be attempted on another processor. Error protection is a separate onboarding opt-in that can route a payment to Stripe when the chosen processor lacks a requested feature. Each mechanism has its own trigger, as do the no-match action and the no-active-rules fallback.

## Rule Lifecycle by Environment

- **Draft.** Choose **Save changes** to keep an editable draft. Drafts take effect only after activation.
- **Sandbox.** Open or create a sandbox, create the rules there and choose **Activate test rules**. Verify the routing behavior in that sandbox before proceeding. Sandbox rules affect only that sandbox.
- **Live.** After the test produces expected results, switch to live mode, recreate the rules and choose **Activate rules**.
- **Replace or reactivate.** Stripe allows one active set per sandbox and one in live mode. Activation replaces the current active set in the same environment. A deactivated set can be reactivated later.
- **Duplicate.** Active sets are read-only. From the set's overflow menu, select **Duplicate test rules** in the sandbox or **Duplicate rules** in live mode. Confirm in the dialog and edit the resulting draft.
- **Deactivate.** In the active set's overflow menu, choose **Deactivate test rules** or **Deactivate rules** for that environment, and confirm in the dialog. When no active set remains there, payments route to Stripe.

The May rules guide recommended sandbox testing and described generic **Activate rules**, **Duplicate rules** and **Deactivate rules** labels. The separate May routing guide already showed **Activate test rules**. The November rules capture provides explicit per-environment instructions.

## Payment Enablement and Test Evidence

Activating a Dashboard ruleset configures routing in that environment. A directly created server-side PaymentIntent includes `payments_orchestration[enabled]=true` to opt in. Contact a Stripe representative for the documented enablement route for PaymentIntents automatically created by Billing, Checkout Sessions, Payment Links or Dashboard payments. Link transactions are excluded from routing rules and always process on Stripe because Link credentials cannot be transferred between processors. See [[source-stripe-orchestration-route-payments]].

The November routing guide uses test cards to verify which processor handled a sandbox payment. On the Dashboard payment details page, **Processor** shows the routed processor and **Recent activity** shows the processor and the rules that routed it. The Payment Record from the PaymentIntent exposes processor-level history through `processor_details.type`. These views establish which processor the test routed to. They leave the specific processor account, actual override execution, retry success, live payment and settlement unverified.

## Related Pages

- [[stripe-orchestration]] — product concept and routing boundaries
- [[source-stripe-orchestration-route-payments]] — PaymentIntent enablement and sandbox verification
- [[source-stripe-orchestration-feature-support]] — dated processor account compatibility and error protection
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-payments-orchestration-rules-2026-11-07|November 7, 2026 Manage rules guide]] — full capture with account selection and environment controls
- [[raw/stripe-orchestration-rules-2026|May 11, 2026 Manage rules guide]] — verbatim historical capture, 58 numbered lines
