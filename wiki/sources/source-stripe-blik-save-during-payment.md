---
title: "Stripe: Save BLIK Details During a Payment"
type: source
date_ingested: 2026-05-03
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/blik/save-during-payment"
raw_files:
  - "stripe-blik-save-during-payment-2025.md"
  - "stripe-blik-2025.md"
tags: [stripe, blik, poland, pln, recurring, payment-intents, mandates, off-session]
---

## Summary

The detailed 2026-05-03 guide shows how to save a BLIK PaymentMethod while processing a payment, so a later recurring off-session charge need not collect another BLIK code. The customer approves both the first payment and mandate in their banking app. The separate 2026-05-03 BLIK overview labels recurring support **private preview**, and the save guide warns that not all Polish banks support it. The 2026-11-07 canonical capture is only a purpose sentence and a chooser for Checkout, Elements, and Direct API; it does not verify current feature access or variant behavior.

## Key Details

### Mandate, identity, and limits (2026-05-03 evidence)

- Before collecting the BLIK code, present the recurring mandate terms: price, charge cycle, end date, and a link to terms and conditions. The customer must understand and agree before proceeding. A bank without recurring support can fail with `recurring_not_supported_by_bank` (old save raw lines 8-12).
- The saved PaymentMethod must be associated with a Customer for reuse. The guide uses PLN and caps **each later off-session recurring payment** at 2000 PLN; this is not a general limit on the initial payment. The dated primary BLIK overview says recurring is private preview, not universally available (old save raw lines 50-75, 137-165, 718-736; old BLIK overview lines 18-32).
- BLIK's specific action remains in the banking app, without a browser redirect for BLIK itself. The generic Payment Element `return_url` example discusses redirects for some other methods, including iDEAL; it does not establish a BLIK redirect (old save raw lines 390-419, 607-613, 773-794; old BLIK overview lines 8-10).

### Initial payment and save paths (2026-05-03 guide)

- Checkout creates a Session in `payment` mode for a Customer, with `payment_intent_data.setup_future_usage: "off_session"`. After the customer completes the Session and approves payment plus mandate, a reusable BLIK PaymentMethod attaches to that Customer (old raw lines 18-44).
- Elements creates a PLN BLIK PaymentIntent on the server for a Customer with `setup_future_usage: "off_session"`, gives its client secret to the client, and uses Payment Element plus `stripe.confirmPayment`. The generic example includes `return_url`; inspect the PaymentIntent status rather than equating a return or client callback with success (old raw lines 137-171, 390-419, 488-607).
- Direct API creates and confirms a PLN BLIK PaymentIntent for the Customer with `setup_future_usage: "off_session"`, a BLIK code in `payment_method_options.blik.code`, and `mandate_data.customer_acceptance` of type `online` with `ip_address` and `user_agent`. That explicit `mandate_data` prescription belongs to this Direct API variant; do not apply it blindly to hosted Checkout or Elements (old raw lines 718-770).
- A valid confirmation can produce `requires_action` with `next_action.type: "blik_authorize"`. The customer then has 60 seconds to approve payment and mandate in the banking app. This state is pending authorization, not final success. The Direct API section names `payment_intent.succeeded`, `payment_intent.payment_failed`, and `mandate.updated` webhooks for outcomes or mandate changes (old raw lines 607-613, 773-800).
- The Elements paragraph at old raw line 488 says a “card” is saved, while the BLIK-specific instructions identify a BLIK PaymentMethod and Customer. Treat “card” as an internal template conflict, not as a BLIK storage fact (old raw lines 8, 137-165, 488, 607-631).

### Later off-session payment and sandbox cases (2026-05-03 guide)

- Create a **new** PLN PaymentIntent with the saved BLIK PaymentMethod and Customer IDs, `off_session: true`, and `confirm: true`. The bank validates it against the original mandate; `blik_authorize` is a bank action, and a bank decline can move the Intent to `requires_payment_method`. Listen for `payment_intent.succeeded` and `payment_intent.payment_failed` to determine final payment status. A created or confirmed Intent alone does not establish payment success (old raw lines 46-79, 627-660, 814-847).
- Six recurring-specific sandbox billing-email patterns: `.*recurring_not_supported@.*` and `.*alias_declined@.*` produce provider declines immediately and after about 8 seconds; `.*setup_timeout@.*` produces `mandate.updated` pending-to-inactive after about 60 seconds; `.*alias_unregistered@.*` and `.*alias_expired@.*` produce active-to-inactive mandate updates after about six minutes; `.*recurring_declined@.*` lets setup succeed but declines later off-session attempts. These are test fixtures, not live outcome promises (old raw lines 81-118, 662-699, 849-886).

## Capture boundary

The 2026-11-07 raw lists only Checkout, Elements, and Direct API variant links. The collection diff replaces the May detailed body with those links. None of the linked November variants was captured in this pin, so no substantive change, current bank participation, or present merchant eligibility can be inferred.

## Related

- [[stripe]] — Stripe company route.
- [[stripe-blik]] — BLIK concept and related Stripe source routes.

## Raw Sources

- [[raw/stripe-blik-save-during-payment-2025|2026-05-03 full BLIK save-during-payment guide]] — dated implementation, state, limit, and sandbox evidence; 886 lines.
- [[raw/stripe-blik-2025|2026-05-03 BLIK overview]] — dated private-preview and in-app approval context; 180 lines.

## Related raw API references

- [[raw/stripe-payments-blik-save-during-payment-2026-11-07|2026-11-07 BLIK save variant index]] — navigation-only Checkout, Elements, and Direct API links; no variant behavior inferred.
