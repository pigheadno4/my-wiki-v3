---
title: "Braintree Marketplace Onboarding (Node.js)"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/onboarding/node"
raw_files:
  - "braintree/docs/guides/braintree-marketplace/onboarding/node-2026-09-16.md"
tags: [braintree, marketplace, node-js, sub-merchants, onboarding, merchant-accounts]
---

## Overview

This collected Braintree Marketplace guide is the Node.js route for a master merchant onboarding a sub-merchant by creating a merchant account and then confirming its creation. It identifies the information categories and account relationships needed for that flow, bank-funding and terms-acceptance conditions, and the pending-result route; it does not establish current Marketplace availability or automatic approval, activation, funding, or transaction eligibility.

## Key takeaways

- The page says a master merchant must onboard each sub-merchant by creating a merchant account on the sub-merchant's behalf and confirming that creation. New merchants seeking a marketplace solution are directed to Braintree Sales.
- Individual information is always required for sub-merchant creation. A registered company also requires a business section with its legal name, tax ID and address, while the sub-merchant still remains tied to an individual.
- For bank disbursement, the guide requires a bank funding destination plus checking-account and routing details and says those bank fields must not be sent for another destination. It also states that Venmo funding destinations are no longer supported for new merchants.
- Braintree says it does not verify the bank account details. If final disbursement fails because the details are wrong, a disbursement-exception webhook is sent and the funds are held until the details are updated.
- A valid create call can return the sub-merchant in `pending` status. The guide routes status handling and webhooks to the later confirmation step; the displayed result is not evidence that onboarding has completed successfully.

## Evidence boundaries

> [!warning] Availability and completion are separate
> The collected page directs new merchants seeking a marketplace solution to Sales. Its Node.js creation flow and `pending` example do not prove current product availability, merchant eligibility, approval, activation, funding readiness, or completed onboarding.

> [!warning] Environment and funding conditions
> The guide says to replace the sandbox master merchant account ID when moving to production. It also says Braintree does not verify bank details and may hold funds after a disbursement exception until those details are updated.

## Detail locators

- New-merchant Sales route and master-merchant create-then-confirm sequence: opening `**AVAILABILITY**` and introductory paragraph, lines 17-24.
- Callback and Promise Node.js creation examples: `## Full example`, lines 25-115.
- Individual-always-required and registered-business conditions: `## Parameters > ### Individual parameters` through `### Business parameters`, lines 120-149.
- Bank-destination fields, checking-account condition, unsupported new-merchant Venmo destination, and unverified-bank-details warning: `### Funding parameters`, lines 152-187.
- Sub-merchant terms acceptance and required website terms route: `### Terms of service accepted parameter`, lines 190-200.
- Master-account nesting, service-fee destination, environment lookup, and production-ID warning: `### Master merchant account ID parameter`, lines 201-220.
- Optional requested ID and gateway-generated fallback: `### ID parameter`, lines 223-233.
- Pending result and status/webhook confirmation route: `## Result handling`, lines 234-253.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- Node gateway context: [[braintree-server-sdk]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-marketplace/confirmation/node-2026-09-16|Braintree Marketplace confirmation guide - Node.js]] - unread navigation-only route for confirming sub-merchant creation; no confirmation behavior is imported here
- [[raw/braintree/docs/reference/request/merchant-account/create/node-2026-09-16|Braintree Merchant Account Create reference - Node.js]] - unread navigation-only field reference; no additional field behavior is imported here
- [[raw/braintree/docs/reference/general/webhooks/disbursement/node-2026-09-16|Braintree disbursement webhook reference - Node.js]] - unread navigation-only webhook route; no additional event or payload behavior is imported here

## Raw Sources

- [[raw/braintree/docs/guides/braintree-marketplace/onboarding/node-2026-09-16|Braintree Marketplace onboarding guide - Node.js]] - complete collected guide covering the master/sub-merchant onboarding sequence, conditional information categories, funding and terms conditions, environment warning, and pending result route
