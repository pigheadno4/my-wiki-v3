---
title: "Stripe — Off-Session Payments API"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/off-session-payments"
raw_files:
  - "stripe-payments-off-session-payments-2026-11-07.md"
  - "stripe-off-session-payments-api-2026.md"
tags: [stripe, off-session, recurring, smart-retries, multi-processor, v2-api, payment-method]
---

## Summary

Stripe's November 7, 2026 overview calls the v2 Off-Session Payments API a private preview for initiating recurring or unscheduled payments against saved payment methods. It adds an email access request and registration example. Stripe describes follow-up contact after a request. May 11 linked the preview API reference without the request form.

## Create an off-session payment

The November overview shows a server-side, secret-key-authenticated JSON `POST /v2/payments/off_session_payments`. Its example sends amount value and currency, Customer and saved PaymentMethod IDs, recurring cadence, metadata and `retry_details.retry_strategy` set to `best_available`. The May Node example uses `stripe.v2.payments.offSessionPayments.create` with the same example fields and links the [preview object reference](https://docs.stripe.com/api/v2/payments/off-session-payments/object.md?api-version=preview).

The November overview example uses `2026-04-22.preview`. The separate November integration guide specifies `2026-08-26.preview` for v2 payment requests and uses `2026-10-28.preview` to create a v2 event destination. These are operation-specific instructions and example headers. Compatible versions for a given account require their own evidence. [[raw/stripe-payments-off-session-payments-integrate-with-off-session-payments-2026-11-07|November integration guide]]

## Retry strategy

The `best_available` request value asks Stripe to use an eligible strategy. The companion guide documents three applied response values:

| Response | Strategy |
| --- | --- |
| `smart` | Smart Retries chooses retry times using AI inference |
| `scheduled` | Configured custom retry schedule |
| `heuristic` | Rule-based retries for Direct Debit, where AI-based retries are unavailable |

An OffSessionPayment can enter `pending_retry`. A hard decline such as `authentication_required` prevents automatic retries. A scheduled attempt leaves the future authorization outcome open. [[raw/stripe-payments-off-session-payments-smart-retries-2026-11-07|November Smart Retries guide]]

## Separate Orchestration path

The May overview described multi-processor routing across supported processors. The November overview omits that paragraph. The separate November routing guide documents Off-Session Payments with [[stripe-orchestration|Stripe Orchestration]] and explicitly excludes Smart Retries. This card-only path excludes Connect and requests containing raw card data.

The routing companion requires access to both private previews, an onboarded processor and an active routing configuration. Opt in per payment with `payments_orchestration.enabled`. Active rules choose the processor and may specify a separate retry processor. The optional routing-rule retry processor is distinct from Smart Retries. [[raw/stripe-payments-off-session-payments-orchestration-2026-11-07|November off-session Orchestration guide]]

## Asynchronous attempts and outcomes

Stripe attempts authorization after returning the create response. A server-side v2 event destination, configured separately from existing v1 webhooks, receives payment-state notifications. The subscription, event table and example payload use `v2.payments.off_session_payment.*`. The integration guide's success prose uses the plural `off_session_payments`, while the subscribed and illustrated event is singular.

| Event suffix | Documented state |
| --- | --- |
| `created` | Create request succeeded |
| `attempt_started` | Initial authorization or retry began |
| `attempt_failed` | Authorization attempt failed with retries remaining |
| `failed` | Terminal failure due to exhausted retries or a non-retryable decline |
| `succeeded` | Successful authorization for automatic capture, or the capture endpoint was called for manual capture |

The result of a create request, retry scheduling and setup success are distinct from the authorization and capture events. Settlement and payout are separate from these events. [[raw/stripe-payments-off-session-payments-integrate-with-off-session-payments-2026-11-07|November integration guide]]

## Compatible Payment Collection APIs

| API | Use case |
| --- | --- |
| Checkout Sessions | Prebuilt checkout that can collect and save a payment method with or without an initial payment |
| Payment Intents | Handle the payment step with the final amount supplied by the integration |
| Setup Intents | Save payment details without charging initially, for recurring payments or a later-priced one-time payment |

Passing a saved PaymentMethod to Off-Session Payments initiates a separate payment flow from saving or setting up the instrument.

## Consent and terms

Both captures assign compliance with applicable laws, regulations and network rules to the merchant. The merchant collects explicit opt-in for the stated future use and retains a record of the customer's written agreement. The terms cover permission for the specified payment or series, timing and frequency, how the amount is determined, and a cancellation policy for subscriptions. A checkbox is the guide's example of collecting opt-in.

## Related Pages

- [[stripe-off-session-payments]] — Off-Session Payments concept and documented limits
- [[stripe-saved-payment-methods]] — Saving a payment method for later use
- [[stripe-orchestration]] — Separate processor routing path
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-off-session-payments-2026-11-07]] — 2026-11-07 full webpage capture (73 lines)
- [[raw/stripe-off-session-payments-api-2026]] — 2026-05-11 full webpage capture (63 lines)
