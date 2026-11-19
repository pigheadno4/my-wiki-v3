---
title: "Stripe: Set Up Future BLIK Recurring Payments"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: https://docs.stripe.com/payments/blik/set-up-payment
raw_files:
  - "stripe-blik-set-up-payment-2025.md"
tags: [stripe, blik, poland, pln, recurring, setup-intents, mandates, off-session]
---

## Summary

The May 3, 2026 detailed guide describes saving a customer's BLIK PaymentMethod for recurring use through mandate authorization **without an initial payment**. It covers Checkout setup mode, Elements with a SetupIntent, and Direct API setup. The November 7, 2026 capture at the same canonical URL states that purpose and lists those three variant links only; it does not revalidate their current steps, bank support, limits, or outcomes. [May raw lines 4-16, 113-157, 532-623; November raw lines 5-15]

## May 2026 setup prerequisites and paths

**Consent and bank support.** Before collecting a BLIK code, present recurring mandate terms including price, charge cycle, end date and a terms-and-conditions link; the customer must understand and agree. The May guide says not every Polish bank supports BLIK recurring, and names `recurring_not_supported_by_bank` for an unsupported-bank decline. This is dated guide wording, not a live eligibility check. Its sandbox table instead uses `payment_method_provider_decline` with a `recurring_not_supported@` email pattern; the simulation's failure code and email trigger are distinct from the guide's opening decline-code statement. [May raw lines 8-14, 74-82]

**Checkout.** On the server, create a Checkout Session in `setup` mode with `blik` and a Customer. The customer enters a BLIK code and approves the mandate in their banking app; after the Session completes, the guide says a reusable BLIK PaymentMethod is attached to that Customer. A setup Session is not an initial payment. [May raw lines 16-37]

**Elements.** Create or retrieve a Customer, then create a server-side SetupIntent with that Customer, `payment_method_types: ["blik"]`, and `usage: "off_session"`. Pass the **SetupIntent** client secret to the client Payment Element and call `stripe.confirmSetup` with a `return_url`. The May HTML/JS example uses Stripe.js `dahlia`; this version-specific example is not updated by the November index. After valid confirmation, the SetupIntent is `requires_action` with `next_action.blik_authorize`, and the customer has 60 seconds to approve in the banking app. Use `setup_intent.succeeded` or `setup_intent.setup_failed` for setup outcome, and `mandate.updated` for later mandate status. The May prose at lines 160-162 and its React link at lines 316-318 call this a PaymentIntent client secret, but the surrounding create and confirm steps are for a SetupIntent; do not substitute a PaymentIntent identity. [May raw lines 130-162, 243-250, 316-318, 372-456]

**Direct API.** The May server-side SetupIntent example includes the Customer, `blik`, BLIK code and `usage: "off_session"`, then confirms the SetupIntent. This variant explicitly requires `mandate_data.customer_acceptance` of type `online`, including the customer's IP address and user agent. A `requires_action` response with `blik_authorize` means banking-app mandate approval is still pending; the customer has 60 seconds. The guide uses `setup_intent.succeeded`, `setup_intent.setup_failed`, and `mandate.updated` webhooks to distinguish approval, failure, and mandate-status change. The online acceptance fields are stated for this Direct API path, not as a blanket requirement of the other variants. [May raw lines 549-623]

**Setup redirect qualification.** The May Elements `confirmSetup` description supplies a `return_url` and says BLIK may visit an intermediate authorization site before that return. This setup flow should not inherit a blanket “no redirect” statement from the separate one-time BLIK payment path. The November index does not settle present-day navigation inside a variant. [May raw lines 372-399; November raw lines 9-15]

## Later recurring charges and test boundaries

A completed setup saves a Customer-linked PaymentMethod; charging later is a separate server-side PaymentIntent with the saved Customer and PaymentMethod IDs and `off_session: true`. Its `blik_authorize` next action is bank validation against the mandate, not proof the payment succeeded. The May guide requires `payment_intent.succeeded` and `payment_intent.payment_failed` webhooks for final payment status; bank decline returns the PaymentIntent to `requires_payment_method`. The stated PLN-only and 2000 PLN maximum apply to **each later off-session recurring payment**. [May raw lines 39-72, 458-491, 625-658]

The May sandbox email patterns simulate unsupported banks, mandate rejection or timeout, later mandate inactivation, and off-session declines. The timing and outcomes in those patterns are sandbox examples, not proof of a live bank's support or a completed charge. [May raw lines 74-111, 660-697]

## Related

- [[stripe]] — Stripe company context.
- [[stripe-blik]] — BLIK concept and flow-specific source routes.

## Raw Sources

- [[raw/stripe-blik-set-up-payment-2025|May 3, 2026 detailed BLIK recurring setup guide]] — historical factual capture with Checkout, Elements and Direct API content; filename follows its earlier convention.

## Related raw API references

- [[raw/stripe-payments-blik-set-up-payment-2026-11-07|November 7, 2026 BLIK setup variant index]] — navigation-only capture linking Checkout, Elements and Direct API variants; their current content was not fetched here.
