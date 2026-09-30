---
title: "Braintree Marketplace Funding"
type: source
date_ingested: 2026-09-30
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/braintree-marketplace/funding"
raw_files:
  - "braintree/articles/guides/braintree-marketplace/funding-2026-09-16.md"
tags: [braintree, marketplace, funding, sub-merchants, disbursements, escrow]
---

## Overview

This collected Braintree Marketplace article describes funding routes for a master merchant and its sub-merchants after a transaction settles. It covers expected disbursement timing, escrow and funding-destination conditions, statement descriptors, and failure notification, but it does not prove that an individual bank deposit arrived or that Marketplace or any funding destination is currently available to a particular merchant.

## Key takeaways

- The article says settled Marketplace transactions should be disbursed to the master merchant's bank account and the sub-merchant's funding source within 1-3 business days unless the funds are held in escrow. It also says each party receives at most one deposit per day regardless of transaction count; these statements are not confirmation of any individual deposit.
- Escrow applies to the entire transaction, including service fees. A master merchant that needs partial disbursements, such as one part immediately and another upon delivery, must create separate transactions.
- The bank-account route uses details collected during onboarding and accepts only checking accounts; savings, deposit-only, and prepaid debit accounts are not accepted. The article also explains master-merchant and sub-merchant statement descriptors, with exact formats in the raw page.
- Venmo funding destinations are stated as no longer supported for new merchants. For the legacy flow described, an unmatched recipient had 30 days to create an account; otherwise the recipient would not receive funds, Braintree says no disbursement-exception webhook was sent for that case, and manual follow-up was required.
- Disbursement-exception webhooks report failed sub-merchant disbursements. The article calls these webhooks the only way a merchant will be notified of sub-merchant disbursement problems and says integrating them into the Marketplace workflow is vital. Banks and Venmo do not send confirmation of successful disbursements, so absence of this webhook is not proof that funds reached a bank or Venmo account.

> [!warning] Availability and funding evidence boundary
> New merchants seeking a marketplace solution are directed to Braintree Sales, and Venmo funding destinations are expressly unavailable to new merchants in this snapshot. Expected timing, descriptors, and failure-only webhooks do not establish current support, merchant eligibility, settlement of a particular transaction, or arrival of an individual deposit.

## Detail locators

- New-merchant Marketplace Sales route: opening `AVAILABILITY`, lines 17-18.
- Expected post-settlement timing, daily deposit maximum, and master-merchant descriptor: `## Master merchant funding`, lines 23-31.
- Whole-transaction escrow requirement and separate-transaction rule for partial disbursements: `## Sub-merchant funding > IMPORTANT`, lines 34-38.
- Bank onboarding route, checking-account-only condition, and sub-merchant descriptor construction: `### To a bank account`, lines 43-57.
- New-merchant Venmo unavailability, legacy matching/invitation flow, 30-day deadline, and missing-webhook exception: `### To a Venmo account`, lines 60-74.
- Venmo message and payment-ID details: `#### Venmo funding descriptor`, lines 79-85.
- Failure-only notification boundary and exception-code inventory: `### Disbursement exception webhook`, lines 88-99.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-marketplace]]
- Webhook context: [[braintree-webhooks]]

## Related raw API references

- [[raw/braintree/docs/guides/braintree-marketplace/onboarding/node-2026-09-16|Braintree Marketplace onboarding guide - Node.js]] - unread navigation-only route for collecting sub-merchant funding details; no onboarding behavior is imported here
- [[raw/braintree/docs/reference/general/webhooks/disbursement/node-2026-09-16|Braintree disbursement webhook reference - Node.js]] - unread navigation-only event reference; no additional trigger or payload behavior is imported here

## Raw Sources

- [[raw/braintree/articles/guides/braintree-marketplace/funding-2026-09-16|Braintree Marketplace funding article]] - complete collected article covering master/sub-merchant post-settlement funding, escrow, bank and legacy Venmo routes, descriptors, and failure-only notification boundaries
