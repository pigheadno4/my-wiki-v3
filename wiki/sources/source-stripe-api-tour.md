---
title: "Stripe API Tour"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/payments-api/tour"
raw_files:
  - "stripe-payments-api-tour-2026-11-07.md"
  - "stripe-api-tour-2025.md"
tags: [stripe, payment-intents, payment-methods, charge, checkout, webhooks, events]
---

## Summary

Conceptual tour of how Stripe API objects cooperate across payment integrations, including an illustrative PaymentIntent path and the roles of PaymentMethod, Charge, and Event. This is an object and process overview, not a complete integration-option taxonomy or an exhaustive state-transition contract. The 2026-04-19 and 2026-11-07 same-URL captures both support the central object descriptions.

## Key Takeaways

- Stripe represents balances, subscriptions, payment details, products, and payment processes as API objects. Dashboard and low-code/no-code actions also produce objects.
- A PaymentIntent tracks the intent to collect a payment across states; `requires_payment_method` can indicate another payment method is needed. A PaymentMethod represents credentials, and Setup Intents can save a method for future PaymentIntents.
- **In most cases**, confirming a PaymentIntent creates a Charge representing that particular attempt to move money. The Charge can succeed or fail. If it fails, the payment **can** be retried by confirming the same PaymentIntent, **usually** with new payment details; this tour does not guarantee every confirmation creates a Charge or that any retry succeeds.
- Event objects represent activity, such as a Charge succeeding or failing. Some integrations respond through merchant webhook code; Checkout and Payment Links provide prewritten responses in the tour's description.
- The page links five integration guides: Payment Links, Checkout, Subscriptions, Invoicing, and Payment Intents. It separately describes Stripe Elements as drop-in UI components within integrations, not as a sixth guide.
- The 2026-04-19 capture says integrations using **customer-configured Accounts** should substitute equivalent Accounts v2 references for `Customer` and event references in code examples. The 2026-11-07 capture omits that caveat; its omission does not establish repeal or account-specific applicability. A customer-configured Account is distinct from a merchant Stripe account and from an ordinary Customer object.

## Illustrative PaymentIntent Path

Both captures label the path simplified. The 2026-11-07 text rendering shows `requires_payment_method → requires_confirmation → processing → succeeded`, a retry arrow from `requires_confirmation` to `requires_payment_method`, and a `processing → canceled` branch. The accompanying prose also says processing can yield `succeeded` or return to `requires_payment_method` on failure. These are illustrative branches, not a complete or exact transition graph; consult the linked [PaymentIntent lifecycle guide](https://docs.stripe.com/payments/paymentintents/lifecycle) for precise state rules.

In the example, a customer clicking checkout for a 100 USD cart expresses intent, not a completed purchase. An integration creates a PaymentIntent to track that intent. Payment details can be gathered by merchant code or Stripe, depending on the integration. Confirmation can be handled by merchant code or Stripe's Checkout/Payment Links flow. Stripe then attempts processing. The tour does not document an observed payment outcome.

## Key Objects

| Object | Role in this conceptual tour |
| --- | --- |
| PaymentIntent | Tracks intent to collect a payment and its process status. |
| PaymentMethod | Carries card or other payment credentials. |
| Charge | In most cases, represents a particular attempt after PaymentIntent confirmation; may succeed or fail. |
| SetupIntent | Can save a payment method for future PaymentIntents. |
| Event | Represents activity; integrations may respond through webhooks or prewritten Stripe handling. |
| Customer / customer-configured Account | Customer references require account-model qualification; the older capture identifies Accounts v2 substitution for customer-configured Account integrations. |
| Subscription | Tracks recurring customer charges. |
| Product | Represents a catalog product, including one created in Dashboard. |

## Related Pages

- [[stripe-payment-intents]] — PaymentIntent concept and more detailed routes
- [[stripe]] — Stripe company page
- [[recurring-payments]] — generic recurring payments concept
- [[disputes]] — generic disputes concept
- [PaymentIntent lifecycle guide](https://docs.stripe.com/payments/paymentintents/lifecycle) — linked detailed state reference; content not assessed for this update
- [Accounts v2 customer modeling guide](https://docs.stripe.com/connect/use-accounts-as-customers) — linked in the older capture; content not assessed for this update

## Raw Sources

- [[raw/stripe-payments-api-tour-2026-11-07|2026-11-07 Stripe API Tour capture]] — conceptual objects, illustrative text status diagram, retry and Charge qualifiers
- [[raw/stripe-api-tour-2025|2026-04-19 Stripe API Tour capture]] — earlier conceptual tour and customer-configured Accounts v2 caveat
