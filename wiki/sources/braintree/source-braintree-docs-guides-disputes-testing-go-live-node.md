---
title: "Braintree Dispute Testing and Go Live (Node.js webpage)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/disputes/testing-go-live/node"
raw_files:
  - "braintree/docs/guides/disputes/testing-go-live/node-2026-09-16.md"
tags: [braintree, disputes, testing, sandbox, node-js]
---

## Overview

This unversioned Braintree Node.js webpage, captured 2026-09-16, explains how a merchant with Braintree Control Panel dispute access can create instantly disputed sale transactions in the sandbox and simulate `won` or `lost` statuses by finalizing specific text evidence. It is sandbox test guidance, not proof of a real dispute outcome or an exact Node SDK/package-version contract.

## Key takeaways

- Managing disputes through the API is available only to merchants who can access disputes in the Braintree Control Panel. Braintree strongly recommends testing dispute workflows in the sandbox before production use.
- The central test action is to create a sandbox sale with the listed test card. The page says the result is a settled sale transaction with an `open` dispute; the same route can exercise email notification, a configured Dispute Opened webhook, lookup, and response flows. Exact card, amount, reason-code, callback and Promise examples remain in the raw locators below.
- Some sandbox transaction amounts select specific dispute reason-code behavior. Those values are test fixtures, not production card-network rules. Separate Venmo and linked-PayPal-sandbox routes are navigation only on this page and do not make it direct PayPal Disputes API authority.
- For a sandbox dispute, adding the exact text `compelling_evidence` and then finalizing simulates a `won` status; adding `losing_evidence` and then finalizing simulates a `lost` status. These deterministic sandbox transitions do not establish evidence acceptance, bank/card-network adjudication, returned funds, or the outcome of a real dispute.
- This page does not state the production reply-by deadline. Use [[source-braintree-docs-guides-disputes-managing]] for the deadline-bound production response and evidence-finalization workflow; access, timely submission and a successful API call still do not guarantee a win.

## Detail locators

- Control Panel dispute-access condition and recommendation to test in sandbox before production: `# Testing and Go Live > AVAILABILITY`, lines 17-20.
- Sandbox test card, settled-sale and `open`-dispute behavior, plus amount-specific qualification: opening test section, lines 22-28.
- Email, configured webhook, lookup and evidence-response test coverage: opening test section, lines 30-36.
- Amount-to-reason-code test fixtures: `##### Creating test disputes that require compelling evidence`, lines 39-49.
- Enabled Venmo and linked-PayPal-sandbox navigation: `### Creating test Venmo disputes` and `### Creating test PayPal disputes`, lines 51-57.
- Transaction Sale action and callback/Promise examples: `## Creating a disputed test transaction`, lines 60-97.
- Sandbox `compelling_evidence` finalization and simulated `won` transition: `## Simulating a won dispute`, lines 101-125.
- Sandbox `losing_evidence` finalization and simulated `lost` transition: `## Simulating a lost dispute`, lines 130-154.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Production dispute handling: [[source-braintree-docs-guides-disputes-managing]]

## Related raw API references

- Transaction Sale, Dispute Add Text Evidence, dispute response reason codes, dispute management, Venmo testing and PayPal testing are linked navigation targets in the captured page; they were not used here as independent behavioral evidence.

## Raw Sources

- [[raw/braintree/docs/guides/disputes/testing-go-live/node-2026-09-16|Braintree Dispute Testing and Go Live (Node route)]] - complete captured webpage covering sandbox disputed-sale creation, test notifications and lookup, amount-specific reason fixtures, and evidence-finalization simulations for `won` and `lost` statuses
