---
title: "Adyen Capital disbursement configuration management"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/manage-disbursements"
raw_files:
  - "adyen/docs/capital/manage-disbursements/2026-09-15.md"
tags: [adyen, capital, grants, disbursements, repayment]
---

## Overview

This 2026-09-15 Capital guide describes retrieving an existing grant's disbursement records, changing a particular disbursement's scheduled-repayment percentage, and retrieving bank-account details assigned for unscheduled repayment. It assumes a grant has already been disbursed; this page does not create a grant or disbursement. Its example GET/PATCH responses and TEST API URLs are documentation, not evidence of a particular user's funding, a booked repayment, an updated live configuration, a bank payout or final debt balance. See [[adyen]], [[adyen-capital]] and [[adyen-platforms]].

## Key takeaways

- **Prerequisites and limit:** The guide requires a Platforms integration with Capital enabled, Balance Platform API credential with Capital Configuration and Grant Initiation roles, user account-holder getGrantOffers and receiveGrants capabilities, a supported region, prior offer selection/Terms signature and at least one disbursed grant. It says currently only one disbursement per grant is allowed, while multiple disbursements are future work. Unscheduled repayments are available only for users operating in Europe, the UK and the US in this snapshot. These stated prerequisites do not prove any real user has them.
- **Read disbursement record:** GET /grants/{grantId}/disbursements uses the grant ID and returns disbursement records containing a distinct disbursement ID, account-holder ID, receiving balance-account ID, minor-unit amount, fee, balances, repayment basis points and fundsCollections. Keep the grant, disbursement, account holder and receiving balance account identifiers distinct. The illustrative response has negative principal/fee balances; it is a sample, not a live user debt calculation.
- **Change repayment percentage:** PATCH /grants/{grantId}/disbursements/{disbursementId} changes the repayment configuration's basis points for the percentage of incoming net volume deducted toward the grant. The guide lists grantId and disbursementId as path parameters; the repayment request object is shown without a required marker in this page's table, although the example supplies it. Changing this setting affects future repayment configuration, not the original disbursement amount or a new bank transfer. Verify the accepted response and later state for a real user; the example does not prove a configuration was changed.
- **Unscheduled-repayment account:** GET the specific grant/disbursement to inspect fundsCollections, where UnscheduledRepayment carries account identification such as an IBAN that can be shared with the user. This is an account for paying **back** a grant, not proof of where grant proceeds were paid or that an unscheduled repayment was sent or booked. Its availability is region-qualified above.

## Detail locators

- Page purpose, prerequisites, one-disbursement limit and region condition: pinned raw lines 15–38.
- Grant-level disbursement GET, identifiers and sample amount/balances: pinned raw lines 40–110.
- Per-disbursement repayment-configuration PATCH, request table and illustrative response: pinned raw lines 112–191.
- Specific-disbursement GET and unscheduled fundsCollections bank details: pinned raw lines 193–236.

## Related

- [[adyen-capital]] — main Capital concept and reciprocal source route.
- [[adyen-platforms]] — parent Platforms integration.

## Raw Sources

- [[raw/adyen/docs/capital/manage-disbursements/2026-09-15|Adyen manage-disbursements guide, captured 2026-09-15]]
