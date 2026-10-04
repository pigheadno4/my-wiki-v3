---
title: "Braintree Wells IC Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-ic/change-your-bank-account"
raw_files:
  - "braintree/articles/wells-ic/change-your-bank-account-2026-09-16.md"
tags: [braintree, wells-ic, bank-account, disbursement, control-panel]
---

## Overview

This collected Braintree-hosted Wells IC article documents how a merchant views and requests a change to the bank account associated with a selected merchant account. It says settled transactions disburse to the checking account supplied during the original application; that statement describes the documented payout route, not proof that an individual transaction settled or that a deposit arrived.

The article is scoped to the captured Braintree Wells IC route. It does not state fee amounts, does not establish that its procedure applies to Wells Flat, and is not current independent Wells Fargo policy. Its stated regional account condition is that a submitted replacement be a US-based business checking account. The documented Control Panel procedure does not establish whether an API route exists.

## Key takeaways

- In the Control Panel, the merchant can select a merchant account and view its disbursement bank account's routing number and last four account-number digits. The user can access that page only when the merchant account is included in the user's role permissions; otherwise, an account admin must add it.
- To request a change, the page directs the merchant to the Disbursement Bank Account page, then **Change**, and requires supporting documentation for the new account. Screenshots of an online-banking profile are not accepted.
- A voided check must name the account holder using the business DBA or legal name; if it lists an address, the address must match the business address on file. Starter checks, temporary checks and screenshots of sample checks are invalid.
- A bank letter must be on bank letterhead; name the bank and account holder; include the ABA/routing number and account number; be signed by a bank representative; carry a clearly stated issue date within the prior six months; and not be a direct-deposit form.
- The submitted account must be a US-based business checking account. The page rejects savings, deposit-only and prepaid debit accounts.

> [!warning] Wells IC and execution scope
> Apply this captured procedure only to the Braintree Wells IC context documented by the page. Do not transfer it to Wells Flat or treat it as current independent Wells Fargo policy. The snapshot does not prove current merchant eligibility, acceptance or completion of an account-change request, settlement of a transaction, or arrival of a deposit.

## Detail locators

- Original-application checking account and settled-transaction disbursement route: opening paragraph, raw line 16.
- Control Panel viewing steps, displayed bank details and role-permission prerequisite: `## Viewing your bank account`, raw lines 19-34.
- Change action, supporting-document upload and online-banking screenshot rejection: `## Updating your bank account`, raw lines 39-45.
- Voided-check requirements and rejected check forms: `### Voided check`, raw lines 52-58.
- Bank-letter content, signature, recency and direct-deposit-form exclusion: `### Bank letter`, raw lines 60-69.
- US-based business-checking requirement and rejected account types: final `NOTE`, raw lines 72-73.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Administration concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/articles/wells-ic/transactions/settlement-funding-timeline-2026-09-16|Braintree Wells IC settlement and funding timeline]] - unread navigation-only destination linked for payout timing; not used as factual evidence here
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree Control Panel managing users and roles]] - unread navigation-only destination linked for role administration; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/wells-ic/change-your-bank-account-2026-09-16|Braintree Wells IC Change Your Bank Account article]] - complete collected page covering the role-scoped disbursement-account view, change request, supporting-document conditions and US business-checking requirement
