---
title: "Braintree AU Transaction Descriptors"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/au/transactions/descriptors"
raw_files:
  - "braintree/articles/au/transactions/descriptors-2026-09-16.md"
tags: [braintree, au, transactions, descriptors, bank-statements]
---

## Overview

This collected Braintree article, filed under its AU documentation path, describes identifying information customers may see on statements for purchases through a merchant's mobile app or website. It distinguishes soft, hard and per-transaction dynamic descriptors, while stating that the customer's bank ultimately determines the exact statement presentation.

## Key takeaways

- The article says the addressed account supports three descriptor types: a soft descriptor after authorization while a charge is pending, a hard descriptor after settlement once the customer's bank finalizes transaction status, and a dynamic descriptor configured and passed with each transaction through the API. This is a statement about the captured page's addressed account, not proof that every Australian account, processor or payment method supports the same behavior.
- Merchant name (trading name) and clearing city and country are listed as required descriptor information. The article says the hard descriptor was automatically configured from application information and routes change requests through Braintree's contact path; exact field constraints remain in the pinned raw.
- The article later labels its location subsection `Clearing city and state` and constrains city and state, despite earlier requiring clearing city and country. The snapshot does not resolve that terminology mismatch, so confirm the account-specific requirement rather than treating country and state as interchangeable.
- PayPal-transaction descriptor updates use the PayPal console instead of the Braintree contact route described for the hard descriptor. Dynamic-descriptor details include a refund default and an Amex Direct-specific asterisk rule; these narrow statements do not establish payment-method eligibility, refund success, authorization, settlement or funding.

> [!warning] Scope and evidence boundaries
> This is a 2026-09-16 snapshot of Braintree's AU documentation path. The page does not name a processor or establish current regional availability, account assignment, processor support, payment-method eligibility or successful payment/refund execution. Do not transfer its rules to sibling processor or account articles. A customer's bank controls the final statement rendering, and the example format is not a guarantee.

## Detail locators

- Descriptor purpose, bank-controlled presentation and example: `# Descriptors`, raw lines 14-18.
- Account-scoped soft, hard and dynamic descriptor meanings: `# Descriptors`, raw lines 20-25.
- Required merchant-name and clearing-location parameters, application-derived hard descriptor and Braintree change route: raw lines 27-33.
- Separate PayPal-console update route: note below `# Descriptors`, raw lines 36-37.
- Hard/soft merchant-name limits and the unresolved country-versus-state terminology: `## Hard and soft descriptor requirements`, raw lines 42-57.
- Refund descriptor default, business-name-only dynamic descriptor scope, detailed character rules, Amex Direct asterisk requirement and registered-trading-name condition: `## Dynamic descriptor requirements`, raw lines 60-76.
- Linked Ruby developer-doc route for passing a per-transaction dynamic descriptor: raw line 78; navigation only, not additional behavioral evidence for this entry.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]
- General descriptor route: [[source-braintree-control-panel-descriptors]]

## Raw Sources

- [[raw/braintree/articles/au/transactions/descriptors-2026-09-16|Braintree AU Transaction Descriptors]] - complete collected article for AU-path descriptor types, configuration, update routes, statement-display qualifications and field requirements
