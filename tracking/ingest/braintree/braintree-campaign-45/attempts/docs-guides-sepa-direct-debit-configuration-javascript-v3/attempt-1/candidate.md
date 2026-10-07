---
title: "Braintree SEPA Direct Debit Configuration — JavaScript v3"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/sepa-direct-debit/configuration/javascript/v3"
raw_files:
  - "braintree/docs/guides/sepa-direct-debit/configuration/javascript/v3-2026-09-16.md"
tags: [braintree, sepa, direct-debit, javascript, configuration, client-token, webhooks]
---

## Overview

This collected [[braintree]] page is the JavaScript v3-routed configuration checklist for accepting SEPA Direct Debit. It maps a valid linked PayPal Business Account, server-generated client authorization, client integration, server-side transaction creation, webhook configuration and a successfully processed transaction in either Sandbox or Production. It is a responsibility and readiness route for [[braintree-payment-methods]], not proof that an account is enabled or a debit ran successfully.

## Key takeaways

- Before accepting SEPA Direct Debit, the checklist says the merchant must create, verify and link a valid PayPal Business Account in the Braintree Control Panel. This page states the prerequisite but does not establish that a particular merchant account has completed it.
- The merchant server generates a client token, and the client uses that token to initialize its components. Client integration is a separate checklist step from server-side SEPA Direct Debit transaction creation and Braintree webhook configuration.
- The body says the SEPA Direct Debit integration was introduced in JavaScript SDK v3, iOS SDK v5 and Android SDK v4. On this JavaScript v3 route, that is generation-level introduction history, not an exact JavaScript package floor, current-support proof or authority for native SDK implementation details.
- The final checklist item calls for successfully processing a SEPA Direct Debit transaction in Sandbox or Production. The environment wording is disjunctive; this captured instruction is not evidence of success in either environment, and success in one is not stated to prove readiness in the other.

## Evidence boundaries

> [!warning] Configuration snapshot, not runtime proof
> This is a Braintree website-documentation snapshot captured on 2026-09-16. It does not establish current product or SDK support, merchant eligibility, account or environment enablement, exact package or commit-qualified GitHub behavior, webhook delivery, transaction success, settlement or funding.

## Detail locators

- Checklist purpose: `# Configuration`, raw line 16.
- PayPal Business Account creation, verification, Control Panel linking and validity condition: `# Configuration`, raw line 17.
- Server-side client-token generation and client component initialization: `# Configuration`, raw lines 18-19.
- Client integration and SDK-generation introduction history: `# Configuration`, raw lines 22-23.
- Server transaction creation, webhook configuration and Sandbox-or-Production success item: `# Configuration`, raw lines 26-28.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- JavaScript client implementation route: [[source-braintree-docs-guides-sepa-direct-debit-client-side-javascript-v3]]
- SEPA lifecycle and mandate overview: [[source-braintree-docs-guides-sepa-direct-debit-overview]]

## Related raw API references

The following collected pages were not used as factual authority for this source entry; they are exact-file navigation for follow-on setup and lifecycle work:

- [[raw/braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16|PayPal Business Account setup guide]]
- [[raw/braintree/docs/guides/sepa-direct-debit/client-side/javascript/v3-2026-09-16|SEPA Direct Debit client-side guide — JavaScript v3]]
- [[raw/braintree/docs/guides/sepa-direct-debit/server-side/node-2026-09-16|SEPA Direct Debit server-side guide — Node.js route]]
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]]
- [[raw/braintree/docs/guides/sepa-direct-debit/testing-go-live/node-2026-09-16|SEPA Direct Debit testing and go-live guide — Node.js route]]

## Raw Sources

- [[raw/braintree/docs/guides/sepa-direct-debit/configuration/javascript/v3-2026-09-16|Braintree SEPA Direct Debit Configuration — JavaScript v3 (captured 2026-09-16)]] - complete collected page covering the account prerequisite, client-token role, client/server responsibility split, webhook route and environment-qualified success item
