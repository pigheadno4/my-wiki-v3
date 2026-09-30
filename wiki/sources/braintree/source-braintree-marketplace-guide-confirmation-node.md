---
title: "Braintree Marketplace: Confirming Sub-merchant Onboarding (Node.js)"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/confirmation/node"
raw_files:
  - "braintree/docs/guides/braintree-marketplace/confirmation/node-2026-09-16.md"
tags: [braintree, marketplace, node-js, sub-merchants, onboarding, webhooks]
---

## Overview

This collected Braintree Marketplace Node.js guide documents the confirmation step for a sub-merchant account after the sub-merchant's information has been verified with third-party services. It distinguishes approved and declined webhook paths and routes readers to webhook setup, parsing, and validation-error details; it does not document account creation or a complete onboarding workflow.

## Key takeaways

- New merchants seeking a marketplace solution are directed to Braintree Sales. This collected snapshot does not establish current Marketplace availability or merchant eligibility.
- The confirmation webhook is triggered after the sub-merchant's information has been verified with several third-party services. The merchant must have a webhook endpoint configured, and the Node examples parse the `bt_signature` and `bt_payload` parameters received in the webhook POST request.
- For approval, the Node example checks `SubMerchantAccountApproved` and shows the returned merchant account with `active` status, its ID, and its master merchant account. The guide says transactions can begin on the sub-merchant account once successful onboarding has been confirmed.
- For decline, the Node example checks `SubMerchantAccountDeclined` and exposes a message and errors. The guide says the webhook contains validation errors explaining the decline, gives several possible reason categories, and directs the merchant to gather more information and contact Customer Success with the sub-merchant's first and last name.

> [!warning] Confirmation is not account creation or complete onboarding proof
> This page covers the post-verification approval-or-decline webhook step. It does not create the merchant account, define the full verification process or decision timing, or establish that a collected notification alone proves every onboarding, funding, processing, or current-availability requirement has been satisfied.

## Detail locators

- New-merchant Marketplace availability route: `# Confirming Sub-merchant Onboarding > AVAILABILITY`, lines 17-18.
- Confirmation purpose, post-verification trigger and webhook-configuration prerequisite: `# Confirming Sub-merchant Onboarding`, lines 20-24.
- Webhook POST parameters and parsing route: `# Confirming Sub-merchant Onboarding > NOTE`, lines 25-26.
- Approved notification kind, returned account state and IDs, and transaction boundary: `## Sub-merchant approved > ### Node`, lines 31-43.
- Declined notification kind, message, errors and reason categories: `## Sub-merchant declined > ### Node`, lines 46-60.
- Validation-error route and follow-up instruction: `## Sub-merchant declined`, lines 62-64.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- Webhook integration context: [[braintree-webhooks]]
- Separate event-kind and payload reference: [[source-braintree-webhooks-sub-merchant-account-node]]

## Related raw API references

- [[raw/braintree/docs/guides/webhooks/overview-2026-09-16|Braintree webhook overview]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/guides/webhooks/parse/node-2026-09-16|Braintree Node.js webhook parsing guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/docs/reference/general/validation-errors/all/node-2026-09-16|Braintree Node.js validation-error reference]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/braintree-marketplace/confirmation/node-2026-09-16|Braintree Marketplace sub-merchant onboarding confirmation guide for Node.js]] - complete collected page covering the post-verification approval and decline webhook paths, returned state examples, validation-error routing, and follow-up boundary
