---
title: "Braintree In-Person Testing Your Integration"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/testing-your-integration"
raw_files:
  - "braintree/in-person/guides/testing-your-integration-2026-09-16.md"
tags: [braintree, in-person, sandbox, testing, card-reader]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes Sandbox-only testing for a Braintree In-Person integration. It recommends end-to-end checks from the POS UI through reader API calls and test-card payment to Control Panel inspection, including unhappy paths, and provides routes for simulated context, payment and processor responses plus an integration-readiness questionnaire. The page is testing guidance and simulation documentation, not evidence of current product or reader availability, account or hardware eligibility, physical device behavior, production readiness, or any actual payment, settlement or funding outcome.

## Key takeaways

- The guide recommends testing the integration end to end in Sandbox before production: start at the POS UI, invoke calls to the Braintree card reader, complete payment with test cards, inspect the Braintree Control Panel, and exercise unhappy-path flows. This is the page's recommended test scope, not proof that a particular integration completed it.
- Sandbox and Production are entirely separate. The snapshot says contexts, locations and transactions created in Sandbox do not transfer to Production; login information, merchant ID and API keys also differ. The page explicitly limits all of its content to Sandbox.
- For Sandbox in-store transactions, specified request amounts simulate the listed Context Status and Payment Status combinations. A separate processor-response procedure says to use a linked decline-code value as the request amount to simulate that response. The exact amount/status matrix and raw procedure remain at the locators below.
- The Braintree Sandbox does not allow testing digital wallets on Braintree dev kit readers. The page additionally states that these payment methods behave like contactless cards from API and UX/UI perspectives; because the same page says they cannot be tested on those dev-kit readers, this statement is documentation guidance rather than observed wallet or device-test proof.
- The readiness questionnaire asks teams to test business-relevant use cases and checks sale/refund idempotency, Merchant Account ID use, timeout logic, error and unhappy-path handling, EMV receipt-data parsing, and logging of `requestId` and other response data. It then suggests arranging a demo and code review with a PayPal Solutions Engineer or Integration Engineer. These questions and a suggested review do not certify production readiness.

## Material warnings

> [!warning] Sandbox isolation and scope
> Nothing created in Sandbox transfers to Production, and credentials and merchant identifiers differ between the environments. The page is explicitly Sandbox-only; simulated statuses and responses cannot establish Production configuration, reader behavior, authorization, settlement or funding.

> [!warning] Digital-wallet testing limitation
> The captured page says digital wallets cannot be tested on Braintree dev kit readers in Sandbox. Its claim that wallet behavior matches contactless cards from API and UX/UI perspectives should not be converted into device-test evidence, current hardware compatibility, availability, or successful wallet-payment proof.

## Detail locators

- Recommended end-to-end POS, reader, test-card, Control Panel and unhappy-path scope: `### Testing Best Practices`, line 19.
- Amount-driven scenario simulation, Sandbox/Production separation, non-transfer rule, differing account values and Sandbox-only scope: `### Testing Best Practices`, lines 23-26.
- Dev-kit reader digital-wallet testing limitation and the page's contactless-card comparison: `### Testing with Digital Wallets`, lines 29-31.
- Simulated Context Status and Payment Status purpose plus exact amount/status matrix: `### Transaction amounts`, lines 34-45.
- Raw processor-response-code purpose and code-as-request-amount simulation procedure: `### Simulating Processor Responses`, lines 48-53.
- Business-use-case scope, readiness framing, idempotency, Merchant Account ID, timeout, error handling, EMV receipt data, request logging, and suggested engineering review: `### Integration Readiness Questionnaire`, lines 56-60.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/articles/get-started/try-it-out-2026-09-16|Try It Out]] - unread Sandbox and Production detail navigation
- [[raw/braintree/articles/control-panel/transactions/declines-2026-09-16|Authorization Decline Codes]] - unread processor-response-code navigation
- [[raw/braintree/in-person/guides/making-a-transaction-2026-09-16|Making a Transaction]] - unread idempotency, Merchant Account ID, timeout and EMV receipt-data navigation
- [[raw/braintree/in-person/guides/graphql-error-handling-2026-09-16|GraphQL Error Handling]] - unread error-handling and request-logging navigation
- [[raw/braintree/in-person/guides/reporting-and-reconciliation-2026-09-16|Reporting and Reconciliation]] - unread follow-on navigation
- [[raw/braintree/in-person/guides/ready-for-launch-2026-09-16|Ready for Launch]] - unread production-readiness navigation

## Raw Sources

- [[raw/braintree/in-person/guides/testing-your-integration-2026-09-16|Braintree In-Person Testing Your Integration]] - complete collected Sandbox testing guide, simulation tables and readiness questionnaire
