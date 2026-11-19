---
title: "Stripe — Payments for Existing Customers"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/existing-customers"
raw_files:
  - "stripe-payments-existing-customers-2026.md"
tags: [stripe, checkout, saved-payment-methods, existing-customers, allow-redisplay, customer-session, elements, payment-intent]
---

## Overview

Stripe's 2026-11-07 canonical capture identifies charging an existing payment method while the customer is on-session and lists five web variants. It is a variant index, not a full guide. The implementation details below come from the retained 2026-05-11 combined guide and remain dated; the November index does not establish current field behavior, account eligibility, method availability, or a payment result.

## Five dated integration routes

| May 2026 route | Identity and UI boundary | Old raw locator |
| --- | --- | --- |
| Stripe-hosted page | Checkout Session with `customer` or `customer_account`; redirects to hosted Checkout | lines 8-83 |
| Full embedded page | Checkout Session with `ui_mode: 'embedded_page'` and an eligible customer identity; mounts embedded Checkout from its client secret | lines 205-274, 355-450 |
| Elements | Checkout Session with `ui_mode: 'elements'`; Checkout Elements SDK displays the Payment Element and confirms the Session | lines 502-561, 642-699, 796-875 |
| Custom flow | Direct PaymentIntent plus CustomerSession for the same Customer or customer-configured Account, with `payment_method_redisplay: 'enabled'`; uses Payment Element and `stripe.confirmPayment` | lines 896-999, 1119-1138, 1219-1223 |
| Direct API | Lists reusable PaymentMethods for a Customer or customer-configured Account, renders the merchant's own selection UI, then creates and confirms a PaymentIntent for the selected method | lines 1448-1486, 1545-1581 |

The Direct API is the fifth route already present in the May guide, not a new November feature. The May Accounts v2 guidance calls customer-configured Account support generally available for Connect users and public preview for other Stripe users, with a preview API version for preview participants. The Customer route is an alternative. This is dated access guidance, not proof of present account eligibility (old raw lines 32-40, 919-927).

## Redisplay, consent, and Checkout prefill

The May guide says merchants are responsible for applicable consent and must collect consent to save details for the specific future use before rendering past methods to the customer. The payment method's `allow_redisplay` value governs whether it is shown by default. Keep API parameter identities distinct: Checkout Sessions use `saved_payment_method_options.allow_redisplay_filters`; a custom PaymentIntent flow uses CustomerSession `payment_method_allow_redisplay_filters` after enabling `payment_method_redisplay`; Direct API listing uses its `allow_redisplay` query. The allowed values discussed in the guide are `always`, `limited`, and `unspecified`. For Checkout, explicitly specifying filters overrides its default, so include `always` if those methods should remain visible (old raw lines 84-98, 1001-1063, 1454-1527).

The dated **Checkout Session** variants display up to 50 saved cards. Apple Pay and Google Pay are not reused as saved Checkout options; show their UI afresh while that Session is active. Checkout card prefill requires `payment` or `subscription` mode, a saved card with eligible redisplay, and billing details sufficient for the Session's address settings; `setup` mode does not prefill. In payment mode the newest saved card takes priority; in subscription mode the default method takes priority if it is a card, otherwise the newest card. The prefilled method displays for 30 minutes after Checkout Session creation. The guide describes a Checkout saved-card removal option with `payment_method_remove: 'enabled'`. These conditions do not describe CustomerSession or Direct API behavior (old raw lines 12, 90-98, 161-183, 458-480, 506, 772-794).

The May custom Payment Element branch lists `card`, `link`, `us_bank_account`, `acss_debit`, `sepa_debit`, `bacs_debit`, `au_becs_debit`, `nz_bank_account`, `ideal`, `sofort`, and `bancontact` as saved types it can display. This list is scoped to that branch and date (old raw lines 900-915).

## State and outcome boundaries

For the three Checkout Session routes, the May guide names `checkout.session.completed`, `checkout.session.async_payment_succeeded`, and `checkout.session.async_payment_failed`; it directs fulfillment from events instead of the browser return (old raw lines 185-203, 482-500, 876-894). For the custom PaymentIntent route, the return page retrieves the PaymentIntent and distinguishes `succeeded`, `processing`, and `requires_payment_method`; server events include `payment_intent.succeeded`, `payment_intent.processing`, and `payment_intent.payment_failed` (old raw lines 1317-1369, 1434-1446).

The Direct API route lists and displays methods before a server `PaymentIntent` create with the selected method and `confirm: true`. A 402 response means the attempted payment was declined. If the created Intent is `requires_action`, the client calls `handleNextAction`; an actions-handled sample message alone does not establish a succeeded payment. The guide directs post-payment work from PaymentIntent events rather than a client callback (old raw lines 1454-1486, 1545-1616). Neither listing a method nor creating a Checkout Session or Intent proves payment completion.

## Related

- [[stripe]] — provider context
- [[stripe-saved-payment-methods]] — saved-method concept and related source routes
- [[stripe-checkout]] — Checkout Sessions context

## Related raw API references

- [[raw/stripe-payments-existing-customers-2026-11-07|Stripe 2026-11-07 existing-customers variant index]] — navigation only for Stripe-hosted page, Full embedded page, Elements, Custom flow, and Direct API; detailed November variant bodies were not pinned here.

## Raw Sources

- [[raw/stripe-payments-existing-customers-2026|Stripe 2026-05-11 combined five-route guide]]
