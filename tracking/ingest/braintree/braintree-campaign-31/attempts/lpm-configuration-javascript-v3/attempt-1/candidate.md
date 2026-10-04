---
title: "Braintree Local Payment Methods Configuration — JavaScript v3"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/configuration/javascript/v3"
raw_files:
  - "braintree/docs/guides/local-payment-methods/configuration/javascript/v3-2026-09-16.md"
tags: [braintree, local-payment-methods, javascript, configuration, client-token, webhooks]
---

## Overview

This collected [[braintree]] page is the JavaScript v3 configuration checklist for Local Payment Methods. It routes a merchant through PayPal Business Account setup, server-generated client authorization, client integration, server-side transaction creation, webhooks, and a successful Sandbox or Production transaction. It is a setup and responsibility map for [[braintree-payment-methods]], not method-specific behavior or evidence that any payment ran successfully.

## Key takeaways

- The page requires a valid PayPal Business Account to be created, verified and linked in the Braintree Control Panel before Local Payment Methods can be processed. Account validity and linking are merchant prerequisites; this snapshot does not prove either for a particular account.
- The merchant server generates a client token, while the client uses that token to initialize its components and integrates Local Payment Methods. The page says the Local Payment Methods integration was introduced in JavaScript SDK v3; its separate iOS v4 and Android v2 statements do not make this JavaScript page evidence for those native implementations.
- The server separately creates the local payment transaction, and the checklist separately requires Braintree webhook configuration. Client initialization or client integration therefore does not establish server transaction creation or notification handling.
- The final checklist item is successful processing in either Sandbox or Production. That instruction is not evidence of a completed test, current production readiness, authorization, settlement or funding, and the page does not say that success in one environment proves success in the other.

## Evidence boundaries

> [!warning] Setup snapshot, not execution proof
> This immutable 2026-09-16 documentation snapshot identifies prerequisites and client/server responsibilities for the JavaScript v3 route. It does not prove current SDK support, method or merchant eligibility, account configuration, environment configuration, webhook delivery, transaction success, settlement or funding.

## Detail locators

- Checklist purpose: `# Configuration`, line 16.
- Valid PayPal Business Account creation, verification and Control Panel linking: `# Configuration`, line 19.
- Server-generated client token and client component initialization: `# Configuration`, lines 20-21.
- Client integration and SDK introduction versions: `# Configuration`, lines 24-25.
- Server-side transaction creation, webhook configuration and Sandbox-or-Production success item: `# Configuration`, lines 28-30.
- Client-side continuation: `Next Page: Client-side`, line 32; navigation only.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following collected pages were not used as factual authority for this source entry; they are exact-file navigation for follow-on setup and lifecycle work:

- [[raw/braintree/articles/guides/payment-methods/paypal/setup-guide-2026-09-16|PayPal setup guide]]
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Node.js Local Payment Methods server-side guide]]
- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhooks overview]]
- [[raw/braintree/docs/guides/local-payment-methods/testing-go-live/node-2026-09-16|Node.js Local Payment Methods testing and go-live guide]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/configuration/javascript/v3-2026-09-16|Braintree Local Payment Methods Configuration — JavaScript v3 (captured 2026-09-16)]] - complete collected page covering the setup checklist, PayPal account prerequisite, client/server responsibility split, webhook route and environment-qualified success item
