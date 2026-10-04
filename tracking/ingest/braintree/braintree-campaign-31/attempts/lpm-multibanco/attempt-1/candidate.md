---
title: "Braintree Multibanco Local Payment Method"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/multibanco"
raw_files:
  - "braintree/docs/guides/local-payment-methods/multibanco-2026-09-16.md"
tags: [braintree, local-payment-methods, multibanco, portugal, graphql, webhooks]
---

## Overview

This collected, unversioned Braintree guide describes Multibanco as a voucher-based Local Payment Method created online and paid later at an ATM with a debit card or through online banking. It is a retrieval route for the method's limited-release applicability, linked-PayPal prerequisite, non-instant no-capture lifecycle, server-side GraphQL route, sandbox simulation and required outcome webhooks. The 2026-09-16 snapshot does not establish current availability, merchant enablement, buyer eligibility or a completed live payment.

## Key takeaways

- The guide marks Multibanco as a limited release for pilot merchants in Braintree-supported merchant countries except Brazil, Japan and Russia, and limits customers to buyers in Portugal. Those captured conditions are snapshot applicability, not proof that a particular merchant or buyer is eligible.
- Processing requires a valid PayPal business account that has been created, verified and linked in the Braintree Control Panel. The page directs the server side to GraphQL to create a local payment transaction, but it names no client platform, SDK or version and does not document a client token, nonce or other initiation-response contract.
- Multibanco is non-instant: the guide says a buyer has up to seven days to pay the voucher. There is no merchant capture call; Braintree says it associates a transaction after receiving confirmation that the voucher was paid. Creation or access to an approval URL therefore must not be presented as completed payment.
- A webhook integration is required. The guide says webhooks confirm a successful payment or notify that a voucher expired, and it shows `local_payment_funded` and `local_payment_expired` example payloads. The funded example's `status: settled` is example content, not evidence that a specific payment settled or that merchant funding completed.
- In Sandbox, the approval URL opens a modal that can simulate successful, expired or unapproved outcomes. The page says the successful simulation sends a webhook after two to three minutes and updates the payment context with an associated transaction; this is Sandbox-only simulated behavior, not Production execution evidence or a general delivery-time guarantee.

## Evidence boundaries

> [!warning] Pilot, country and snapshot scope
> Limited-release wording and the captured seller/buyer geography do not prove current program availability, account enablement or individual buyer eligibility. Recheck live and account-specific conditions before relying on this route.

> [!warning] Non-instant lifecycle and outcome
> Keep transaction creation, an approval URL, voucher payment, Braintree's confirmation, transaction association, webhook delivery, example transaction status and merchant funding as distinct evidence points. This page says there is no capture call and does not establish that initiation or approval completes payment.

> [!warning] Platform, token and environment scope
> The page names server-side GraphQL but no client SDK, platform or version, and it does not specify a token or nonce handoff. Its modal and two-to-three-minute webhook timing are explicitly Sandbox simulation behavior; neither the simulation nor the example webhook proves Production execution, settlement of a particular payment or merchant funding.

## Detail locators

- Limited-release merchant and Portugal-buyer applicability: `### Configuration`, lines 17-21.
- Voucher identity, ATM or online-banking payment and seven-day non-instant window: `### Configuration`, line 23.
- Created, verified and linked PayPal business-account prerequisite: `### Configuration`, line 26.
- No-capture transition and Braintree transaction association after voucher-payment confirmation: `### Capturing Non-Instant Transaction`, lines 29-31.
- Sandbox approval-modal outcomes, successful-simulation timing and payment-context update: note under `### Capturing Non-Instant Transaction`, lines 34-35.
- Server-side GraphQL transaction-creation route: `### Server Side with GraphQL`, lines 38-42.
- Required successful-payment and expired-voucher webhooks: `### Configure webhooks`, lines 45-47.
- Funded and expired webhook example fields: `### Configure webhooks`, lines 49-76; exact notification-content route: line 77.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]
- Notification concept: [[braintree-webhooks]]

## Related raw API references

The following collected pages were not used as factual authority for this source entry; they are exact-file navigation for follow-on setup and implementation work:

- [[raw/braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16|PayPal setup guide]]
- [[raw/braintree/graphql/integration_guides/non_instant_local_payments-2026-09-16|GraphQL non-instant local payments guide]]
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]]
- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Node.js Local Payment Method webhook reference]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/multibanco-2026-09-16|Braintree Multibanco guide]] - complete collected page covering pilot applicability, payment timing, PayPal setup, no-capture behavior, GraphQL routing, Sandbox simulation and webhook outcomes
