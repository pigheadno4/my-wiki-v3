---
title: "Stripe PaymentIntents and SetupIntents Lifecycle"
type: source
date_ingested: 2026-04-19
date_updated: 2026-11-22
original_format: webpage
raw_files:
  - "stripe-payments-paymentintents-lifecycle-2026-11-07.md"
  - "stripe-payments-setup-intents-2026-11-07.md"
  - "stripe-payments-payment-intents-2026-11-07.md"
  - "stripe-payments-payment-intents-asynchronous-capture-2026-11-07.md"
  - "stripe-payment-setup-intents-2025.md"
  - "stripe-payment-intents-api-2025.md"
  - "stripe-payment-status-updates-2025.md"
  - "stripe-async-capture-2025.md"
  - "stripe-setup-intents-api-2025.md"
tags: [stripe, payment-intents, setup-intents, lifecycle, 3ds, checkout-sessions]
---

## Summary

This combined [[stripe|Stripe]] reference brings together the Payment Intents implementation guide, asynchronous capture, the April and November Intent lifecycle and Setup Intents API guides, and a separate April guide for status monitoring. A PaymentIntent tracks an attempt to collect payment. Confirmation can require further action, delayed processing, or a separate capture. A SetupIntent prepares payment credentials for future use without an initial charge.

## Payment Intents API implementation guide

The 2026-04-19 and 2026-11-07 captures of [The Payment Intents API](https://docs.stripe.com/payments/payment-intents) describe the same core integration. Create a PaymentIntent on your server once you know the amount and currency. Associate its ID with the cart or customer session so interrupted checkouts can reuse the Intent, and update the amount when appropriate. Use a cart- or session-based idempotency key when creating the Intent to prevent duplicate Intent creation for that purchase. Multiple attempts can create multiple associated Charge objects. The separate November Payment Intents API reference scopes the at-most-one-successful-Charge rule to a single PaymentIntent (`raw/stripe-api-payment-intents-2026-11-07.md`, lines 80–85).

### Client secret delivery and outcome

The server creates or retrieves the Intent and gives only the customer its Intent-scoped client secret, through a TLS-protected endpoint for a single-page app or a rendered checkout form. Keep the merchant secret API key and full PaymentIntent object server-side. The Intent secret can complete payment for the amount on the Intent. Keep it out of logs and merchant-built URLs. The separate [[source-stripe-payment-intents-quickstart|April Stripe.js quickstart]] describes a provider-appended return query for retrieving status and displaying a message. It gives no authority for fulfillment or permission to log the secret.

Confirming the Intent attempts payment. Monitor verified server webhook events for success or failure and use them for fulfillment. The April status guide shows signature verification, `last_payment_error.message` for failure, `latest_charge` for the latest attempt, and `next_action` when an advanced integration handles required action directly. It distinguishes `payment_intent.processing`, `payment_intent.succeeded`, `payment_intent.amount_capturable_updated`, and `payment_intent.payment_failed`. It recommends webhooks over polling and shows local forwarding with the Stripe CLI.

### Checkout Sessions and Payment Intents

Both implementation-guide captures recommend Checkout Sessions with the Payment Element for most integrations and describe Adaptive Pricing as a Checkout Sessions feature. Their Checkout examples use the Checkout **Session** client secret for `ui_mode: 'elements'`. The React example uses `CheckoutElementsProvider` from `@stripe/react-stripe-js/checkout` and `checkout.confirm`. The HTML example uses `stripe.initCheckoutElementsSdk`, mounts a Payment Element, and confirms through actions returned by `loadActions()`. The lower-level Payment Intents path instead initializes Stripe.js Elements with the **PaymentIntent** client secret and uses the Intent flow's client confirmation. See [[stripe-checkout]] for exact SDK versions and [[source-stripe-checkout-sessions]] for the separate captured overview, whose examples retain `ui_mode: 'custom'`.

### Descriptor and metadata boundaries

Both guide captures' descriptor introductions suggest `statement_descriptor` for a different per-card description. Their explicit note and examples instead use `statement_descriptor_suffix` for card charges and `statement_descriptor` for non-card charges. The November Create reference confirms the non-card parameter errors on card charges (`raw/stripe-api-payment-intents-create-2026-11-07.md`, lines 690–700). For a dynamic card descriptor, the account prefix, asterisk and space separator, and suffix count toward the combined 22-character limit.

The April descriptor and metadata examples explicitly submit `payment_method_types` on PaymentIntent Create. The November cURL examples omit it without stating an API version or a reason. The separate November-captured Endive changelog documents HTTP 400 with `payment_method_types_no_longer_supported` on the linked `2026-09-30.endive` Create endpoint while retaining the read-only object property. Its Impact section also names `2026-08-26.preview`, leaving the first affected version unresolved. See [[stripe-payment-intents#Server SDK 23.0.0 Endive Boundary|the separate exact-version server SDK boundary]].

Use non-sensitive reference values such as an order ID in metadata. The PaymentIntent copies its metadata to a Charge at Charge creation. Later edits on the Intent leave earlier Charges unchanged. Keep sensitive data, including personally identifiable information and card details, out of metadata and description. The guides separately discuss custom Radar metadata rules. April names **Radar for Fraud Teams**, and November names **Radar Plus**. The names are dated guide wording and leave plan equivalence and eligibility unresolved.

### Dated implementation changes

November uses cURL in place of some Node examples and Ruby/ERB in place of the Express/Handlebars client-secret examples. It changes quickstart navigation and adds a lifecycle link. The sandbox aside in the November implementation and lifecycle guides is separate tooling guidance. It describes a help invocation as provisioning, while the separate November CLI reference documents logged-out provisioning through the create operation with an email or Git identity and seven-day expiry, and a Dashboard management path for logged-in users. Provisioning by help invocation is unverified.

## Lifecycle and cancellation

The 2026-04-19 and 2026-11-07 captures of [How Payment Intents and Setup Intents work](https://docs.stripe.com/payments/paymentintents/lifecycle) use “immediate charge” to describe the PaymentIntent's purpose. Creation establishes an attempt. Confirmation and authorization can lead to different states before collection completes. The November guide presents the two Intent lifecycles side by side and links to the [Dashboard-to-PaymentIntent status mapping](https://docs.stripe.com/payments/payment-intents/verifying-status.md#payment-status-mapping). The April guide explicitly describes typical card processing as quicker and outside `processing`, while the November guide describes the asynchronous branch.

| State | PaymentIntent | SetupIntent |
| --- | --- | --- |
| `requires_payment_method` | Needs a method, including after a failed attempt | Needs a method, including after failed setup |
| `requires_confirmation` | Ready to confirm | Ready to confirm |
| `requires_action` | Needs additional action, such as 3DS | Needs additional action, such as 3DS |
| `processing` | Can await a delayed payment outcome | Setup is still processing |
| `requires_capture` | Separate authorization has made funds available for capture. Attempting capture can lead to processing or success. | Payment capture is outside the setup flow |
| `succeeded` | Payment flow completed. See asynchronous capture for deferred fields. | Setup completed for future use without charging |
| `canceled` | No further payment attempts on that Intent | No further setup attempts on that Intent |

Versions before 2019-02-11 use `requires_source` and `requires_source_action` for the corresponding statuses. Excessive PaymentIntent confirmations can cause automatic cancellation.

Both lifecycle captures describe **PaymentIntent cancellation** before `processing` or `succeeded`, with a limited and variable exception during `processing` for ACH, ACSS, AU BECS, BACS, NZ BECS, and SEPA. An attempt during that window can fail. Canceling a PaymentIntent irreversibly prevents future payment attempts on it and releases any held funds. The separate November PaymentIntent Cancel API reference lists eligible states and allows direct cancellation of a Checkout Session’s PaymentIntent only in `requires_capture`. Otherwise follow the Session expiration path where applicable. Its request example specifies `2026-10-28.endive` (`raw/stripe-api-payment-intents-cancel-2026-11-07.md`, lines 7–25).

Both lifecycle captures describe **SetupIntent cancellation** before `processing` or `succeeded`. It irreversibly prevents future setup attempts on that SetupIntent. The limited bank-debit processing exception and held-funds rule above apply to PaymentIntents.

## Saving a payment method

The April 19 and November 7, 2026 captures of [The Setup Intents API](https://docs.stripe.com/payments/setup-intents) describe saving credentials for future use without an initial charge. Stripe updates the SetupIntent through any required customer authentication or bank validation. Set `SetupIntent.usage` to `on_session` for customer-present-only use or `off_session` for off-session or mixed use. Omission defaults to `off_session`. `PaymentIntent.setup_future_usage` describes intended reuse when saving during a payment in the separate implementation guide.

For future customer-facing display, obtain explicit consent and use `allow_redisplay` to distinguish methods saved for offline use from methods eligible to appear in checkout. For off-session charging, obtain an upfront agreement or mandate with opt-in terms that cover permission to initiate a payment or series of payments, anticipated frequency, and how the amount is determined. Consent and mandates remain separate from issuer authentication and Stripe's intended-use optimization.

`off_session` can move card authentication into setup and reduce friction later. Properly saved off-session card payments under an agreement can qualify as merchant-initiated transactions, with any SCA exemption conditional. Issuers can still decline or require later authentication. If an off-session card payment requires authentication, bring the customer back online to complete that payment.

## Asynchronous capture

The 2026-04-19 and 2026-11-07 captures of [Asynchronous capture](https://docs.stripe.com/payments/payment-intents/asynchronous-capture) describe faster confirmation by finishing capture in the background. April's opening describes setting `capture_method=automatic_async` when confirming. Its opt-in text and Node example place it on PaymentIntent creation with `confirm=true`. November uses the same placement in a form-encoded `POST /v1/payment_intents` create-and-confirm example. Those examples establish the create request. The standalone confirm endpoint's schema is outside their scope. November's example `return_url` and omission of the earlier card array alone establish no new request requirement.

Both guides call `automatic_async` the default in the API version they describe as latest. The separate 2024-04-10 creation-default changelog documents the default when omitted and links a 2024-06-20 API reference. The async guide's **2022-11-15 or later** qualifier applies to the pictured PaymentIntent response and webhook `latest_charge` shape. It does not date the creation default.

A `succeeded` PaymentIntent and `captured: true` Charge can coexist with a null Charge `balance_transaction`. The initial attached Charge in the API response and the `charge.succeeded` and `payment_intent.succeeded` events can lack that data. November explicitly requires handling this case even when expanding `balance_transaction` directly or `latest_charge.balance_transaction`. Applicable Connect `application_fee` and `transfer` fields can also be deferred. The `charge.updated` example annotates those two fields for destination charges.

| Deferred data | Documented event |
| --- | --- |
| Charge `balance_transaction` | `charge.updated` |
| Applicable Connect application fee | `application_fee.created` |
| Applicable Connect transfer | `transfer.created` |

April's link text says `charge.updated` but links to `charge.created`. November corrects the destination to `charge.updated`. Both captures state a one-hour SLA for `charge.updated` after successful confirmation. The SLA covers that event only. The background capture, payment outcome, ledger field availability, settlement, and payout are separate. Manual capture and delayed payment-method processing have their own states.

## Detail Locators

- November implementation raw lines 22–107 and April lines 19–131 cover server creation, reuse, idempotency, scope of client-secret delivery, and server outcomes.
- November implementation raw lines 109–171 and April lines 133–211 cover future use, descriptors, and metadata lifecycle.
- November asynchronous capture raw lines 9–36 cover creation and handling absent expanded data. Lines 38–76 and 78–108 cover the displayed response version, deferred fields, and event guidance. April lines 8–28, 30–66, and 68–97 preserve the earlier samples and event link.
- November lifecycle raw lines 13–35 cover payment versus setup, authentication, the Dashboard status mapping route, version aliases, and object-specific states and cancellation. April lifecycle raw lines 10–86 cover the same Intent lifecycles in separate sections.
- April Setup Intents API raw lines 28–68 cover consent, agreements, and `usage`. April status-monitoring raw lines 62–166 cover webhook and next-action examples.

- The separate Setup Intents API guide covers no-charge setup in April raw lines 8–26 and November lines 9–27, consent and agreements in April lines 28–50 and November lines 29–51, and intended use, defaults and recovery in April lines 52–68 and November lines 53–69. The Node.js and cURL server creation examples are in April lines 70–78 and November lines 71–75.

## Related Pages

- [[stripe]] — Stripe company page
- [[stripe-payment-intents]] — PaymentIntents concept and version boundaries
- [[stripe-checkout]] — Checkout Sessions and client SDK distinctions
- [[stripe-radar]] — Radar rules and metadata
- [[source-stripe-api-tour]] — Stripe API tour overview

## Raw Sources

- [[raw/stripe-payments-paymentintents-lifecycle-2026-11-07|2026-11-07 Payment Intents and Setup Intents lifecycle guide]]
- [[raw/stripe-payments-setup-intents-2026-11-07|2026-11-07 Setup Intents API guide]]
- [[raw/stripe-payments-payment-intents-2026-11-07|2026-11-07 Payment Intents implementation guide]]
- [[raw/stripe-payments-payment-intents-asynchronous-capture-2026-11-07|2026-11-07 Asynchronous capture guide]]
- [[raw/stripe-payment-setup-intents-2025|2026-04-19 Payment Intents and Setup Intents lifecycle guide]]
- [[raw/stripe-setup-intents-api-2025|2026-04-19 Setup Intents API guide]]
- [[raw/stripe-async-capture-2025|2026-04-19 Asynchronous capture guide]]
- [[raw/stripe-payment-status-updates-2025|2026-04-19 payment status monitoring guide]]
- [[raw/stripe-payment-intents-api-2025|2026-04-19 Payment Intents implementation guide]]
