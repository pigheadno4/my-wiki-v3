---
title: "Stripe — Card Payments Without Bank Authentication"
type: source
date_ingested: 2026-05-11
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/without-card-authentication
raw_files:
  - "stripe-payments-without-card-authentication-2026-11-07.md"
  - "stripe-payments-without-auth-2026.md"
tags: [stripe, payment-intent, card-element, us-canada, error-on-requires-action]
---

## Summary

Stripe's May 11 and November 7, 2026 guides describe synchronous card payments for businesses accepting only cards issued in the US or Canada. Stripe says issuers in those two markets can accept payments without bank authentication. When a bank requires authentication, this integration declines the payment. The merchant server can handle immediate post-payment tasks after observing a successful result in this synchronous flow. Stripe recommends webhooks for its global integration, which handles bank-requested authentication and accommodates additional payment methods.

## Client and server flow

1. Serve the page containing Elements over HTTPS in either the HTML/JavaScript or React variant. For HTML/JavaScript, load Stripe.js directly from `js.stripe.com` without bundling or self-hosting it. Stripe-hosted Elements uses an iframe to collect and send card details to Stripe without exposing the details to merchant code.
2. Use the Card Element and `stripe.createPaymentMethod` in the browser. Send the resulting PaymentMethod ID to the merchant server.
3. Calculate the authoritative amount on the merchant server. Create and confirm the PaymentIntent with that PaymentMethod ID, `confirm=true`, and `error_on_requires_action=true`.
4. Require `succeeded` before fulfilling the order. Invalid card details and insufficient funds can still cause ordinary declines. The authentication-required example returns API error code `authentication_required`, decline code `authentication_not_handled`, and a PaymentIntent in `requires_payment_method`. The November flow diagram simplifies the success branch. See [[source-stripe-migrate-basic-card-integration]] to add handling for bank-requested actions.

The client requirements are in the May capture at lines 35–53 and 148–152, and the November capture at lines 49–67 and 160–164. For the server decision and payment outcomes, see May lines 272–345 and 375–410 and November lines 290–325 and 351–386.

## Dated examples

The May 11 capture shows the Dahlia Stripe.js script, Node.js setup, and an Express handler that checks for `succeeded` and treats other statuses as unexpected. The November 7 capture shows the Endive Stripe.js script, Ruby SDK installation, a cURL creation request, React links with `?ui=elements`, and a text diagram. Both captures document the same success condition and authentication-required outcome. The examples document integration behavior and prerequisites without establishing account eligibility, merchant PCI compliance, or runtime results.

Both captures list the same sandbox cards. Use `4242424242424242` for a successful payment, `4000000000009995` for insufficient funds, and `4000002500003155` for an authentication-required decline with the documented flag set. See May lines 404–410 and November lines 380–386.

## Related Pages

- [[stripe]] — provider overview
- [[stripe-payment-intents]] — PaymentIntent confirmation and outcomes
- [[source-stripe-migrate-basic-card-integration]] — upgrade the server-confirmed card integration to handle bank-requested actions

## Raw Sources

- [[raw/stripe-payments-without-card-authentication-2026-11-07]] — full November 7, 2026 guide, including updated sample references and the same documented flow.
- [[raw/stripe-payments-without-auth-2026]] — full May 11, 2026 guide with the earlier Stripe.js and Node/Express examples.
