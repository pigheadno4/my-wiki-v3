---
title: "Braintree Marketplace: Updating Sub-merchants (Node.js)"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/braintree-marketplace/update/node"
raw_files:
  - "braintree/docs/guides/braintree-marketplace/update/node-2026-09-16.md"
tags: [braintree, marketplace, node-js, sub-merchants, merchant-accounts, updates]
---

## Overview

This collected Braintree Marketplace guide documents the Node.js route for updating an existing sub-merchant through `gateway.merchantAccount.update()`. The call identifies the sub-merchant account and supplies only the attributes to change; omitted attributes remain unchanged.

## Key takeaways

- The update requires the merchant account ID together with the changed attributes. If the merchant account cannot be found, the guide routes the failure to Braintree's Node.js `notFoundError`.
- The guide groups updateable sub-merchant details under `individual`, `business`, and `funding`. Every sub-merchant must retain individual details; business details apply to a registered business and are optional in addition to those individual details. The funding section controls where Braintree disburses settled funds.
- Successful individual and funding examples return only the last four digits of the SSN and bank account number, respectively, because those fields contain sensitive data.

> [!warning] Availability and lifecycle boundary
> The page directs new merchants seeking a marketplace solution to Braintree Sales. This collected guide does not establish current Marketplace availability, eligibility, approval, activation, validation outcomes, or when an update affects later processing or disbursement. A successful update response is not evidence that settled funds were disbursed.

## Detail locators

- New-merchant Marketplace availability route: `# Updating Sub-merchants > AVAILABILITY`, lines 17-18.
- Required merchant-account identifier, changed-attribute input and unchanged omitted attributes: `# Updating Sub-merchants`, lines 20-21.
- Node.js update invocation and callback success check: `# Updating Sub-merchants > ### Node`, lines 22-31.
- Missing-account error route and the three update categories: `# Updating Sub-merchants`, lines 33-38.
- Required individual details and the individual-update example: `## Individual details`, lines 41-67.
- SSN output masking after success: `## Individual details`, lines 68-69.
- Registered-business qualification, optional business details and required-individual relationship: `## Business details`, lines 70-93.
- Funding purpose and update example: `## Funding details`, lines 94-113.
- Bank-account-number output masking after success: `## Funding details`, lines 114-115.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- General Node.js merchant-account update reference: [[source-braintree-merchant-account-update-node]]

## Raw Sources

- [[raw/braintree/docs/guides/braintree-marketplace/update/node-2026-09-16|Braintree Marketplace Node.js sub-merchant update guide]] - complete collected page covering update identity, unchanged omitted attributes, update categories, availability, missing-account and sensitive-output boundaries
