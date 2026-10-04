---
title: "Braintree Wells Flat Change Your Bank Account"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/wells-flat/change-your-bank-account"
raw_files:
  - "braintree/articles/wells-flat/change-your-bank-account-2026-09-16.md"
tags: [braintree, wells-flat, bank-account, disbursements, control-panel, united-states]
---

## Overview

This collected [[braintree]] Wells Flat article describes the business checking account associated with a merchant account, the Control Panel route for viewing limited account details, and a documented request flow for changing that account with supporting documentation. It says settled transactions disburse to the account supplied during the original application according to a separate settlement-and-funding timeline; that statement is not proof that any particular transaction settled or deposit arrived.

The article belongs to the captured Wells Flat account scope and does not describe a pricing model or fee rate. Its US-account and document conditions must not be transferred to Wells IC, another processor or account configuration, or treated as independent current bank policy or proof of current merchant eligibility.

## Key takeaways

- The Control Panel path is **Business** → **Merchant Accounts** → **View** for the selected account. The resulting Disbursement Bank Account page shows the routing number and the last four digits of the associated bank account. Access is limited to users whose role permissions include that merchant account; an account admin can edit the user's merchant-account inclusion.
- To request a bank-account update, the page directs the user to the Disbursement Bank Account page, then **Change**, and requires supporting documentation for the new account. This is a documented UI procedure; the article does not establish whether an API route exists or does not exist, and submitting documents is not evidence that a change was approved or completed.
- Screenshots of an online-banking profile are not accepted. A voided check must carry the business DBA or legal name, any displayed address must match the business address on file, and starter checks, temporary checks, and sample-check screenshots are invalid.
- Alternatively, a bank letter must be on bank letterhead; name the bank and the matching DBA or legal business account holder; include the ABA/routing and account numbers; be signed by a bank representative; have a clearly stated issue date within the prior six months; and not be a direct-deposit form.
- The submitted account must be a US-based business checking account. The page rejects savings, deposit-only, and prepaid debit accounts.

> [!warning] Wells Flat and snapshot scope
> Apply these account and document conditions only to the captured Braintree Wells Flat article. Do not transfer them to Wells IC or another account or pricing configuration, and do not present them as independent or current Wells Fargo policy, current regional or merchant eligibility, or confirmation that a requested change succeeded.

## Detail locators

- Original-application account and settled-transaction disbursement statement: opening paragraph, raw line 16.
- Control Panel viewing steps: `## Viewing your bank account`, raw lines 21–28.
- Displayed routing number and last four account digits: `## Viewing your bank account`, raw line 30.
- Merchant-account role-permission condition and account-admin route: first `NOTE`, raw lines 33–34.
- **Change** action and supporting-document upload: `## Updating your bank account`, raw line 41.
- Online-banking-profile screenshot rejection: second `NOTE`, raw lines 44–45.
- Voided-check requirements and invalid check forms: `### Voided check`, raw lines 52–57.
- Bank-letter content, signature, recency, and direct-deposit-form exclusion: `### Bank letter`, raw lines 60–69.
- US-based business-checking requirement and rejected account types: final `NOTE`, raw lines 72–73.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-platform]]
- Administration concept: [[braintree-control-panel]]

## Related raw documentation

- [[raw/braintree/articles/wells-flat/transactions/settlement-funding-timeline-2026-09-16|Braintree Wells Flat settlement and funding timeline]] - unread navigation-only destination linked for disbursement timing; not used as factual evidence here
- [[raw/braintree/articles/control-panel/users-roles/managing-users-roles-2026-09-16|Braintree managing users and roles article]] - unread navigation-only destination linked for editing merchant-account permissions; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/wells-flat/change-your-bank-account-2026-09-16|Braintree Wells Flat Change Your Bank Account article]] - complete collected snapshot covering disbursement-account viewing, permission-gated access, the documented change request, supporting-document conditions, and rejected account types
