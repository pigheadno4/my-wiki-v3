---
title: "Braintree Disputes Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/disputes/overview"
raw_files:
  - "braintree/docs/guides/disputes/overview-2026-09-16.md"
tags: [braintree, disputes, chargebacks, api]
---

## Overview

This unversioned Braintree webpage, captured 2026-09-16, introduces API-based dispute management for merchants whose account setup already permits dispute access in the Braintree Control Panel. It outlines the merchant's accept-or-respond decision and the response handoff to the cardholder's bank.

## Key takeaways

- API dispute management is available only to merchants who can access disputes in the Braintree Control Panel; account setup determines whether this route is available.
- The page frames chargebacks, retrievals, and pre-arbitrations as items the merchant must review and either accept or answer with evidence. Its stated API scope includes finding or searching disputes, checking status, submitting evidence, and accepting a dispute.
- In the basic flow, the cardholder starts a dispute with their bank and a dispute is created for the merchant account that processed the transaction. Acceptance ends the merchant flow; a response instead adds text or file evidence and finalizes the dispute so Braintree can send the response to the bank for review.
- Merchants who currently use another chargeback-response process cannot use this API route. Braintree warns that implementing API dispute management for an unsupported account setup can cause the merchant to miss an opportunity to recover funds from illegitimate chargebacks.
- This captured page documents the stated route and conditions; it does not establish current merchant eligibility, successful API execution, evidence acceptance, a bank decision, settlement, or recovered funds.

## Detail locators

- Control Panel dispute-access prerequisite: `# Overview > AVAILABILITY`, lines 16-17.
- Merchant responsibility, account-setup qualification, Control Panel/API relationship, and action inventory: opening overview paragraph and list, lines 19-25.
- Cardholder initiation, dispute creation, accept-or-respond decision, text/file evidence, finalization, and bank-review handoff: `## Dispute management flow`, lines 30-40.
- Account-dependent API availability and alternate-process exclusion: `## Availability`, lines 47-54.
- Consequence warning for implementing the API route on an unsupported account setup: `## Availability > IMPORTANT`, lines 56-57.

## Related

- Company: [[braintree]]
- Main concept: [[disputes]]
- Detailed API workflow: [[source-braintree-docs-guides-disputes-managing]]

## Related raw API references

- The support-article route and next-page route to Managing Disputes via the API are navigation in the captured overview; they were not read as evidence for this source.

## Raw Sources

- [[raw/braintree/docs/guides/disputes/overview-2026-09-16|Braintree Disputes Overview]] - complete captured webpage covering account-qualified API availability, the accept-or-respond flow, evidence finalization, and the unsupported-account warning
