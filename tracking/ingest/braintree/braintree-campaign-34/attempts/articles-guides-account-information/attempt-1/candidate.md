---
title: "Braintree Updating Account Information"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/account-information"
raw_files:
  - "braintree/articles/guides/account-information-2026-09-16.md"
tags: [braintree, control-panel, account-information, bank-account, authorized-signer, business-documents]
---

## Overview

This collected Braintree guide routes account-information updates across Control Panel user credentials and email, secure business-document upload, disbursement bank-account changes and viewing, authorized-signer-controlled details, and UK VAT registration numbers. The route and prerequisites vary by update type, user role, merchant-account access, Braintree Direct status and region.

## Key takeaways

- Anyone can start a password reset from the sign-in page, while a user with **Manage Users** permission can change passwords and other user details in the Control Panel. Updating a Control Panel user's email requires access to the original email account for confirmation; otherwise the article directs the merchant to create a new user.
- Braintree may request sensitive information or documents for some changes. The page assigns Control Panel upload access to Account Administrators and users with the **Business Management** role permission. Its upload instructions culminate in sending the documents for team follow-up; password-protected documents are unsupported and cause an upload error.
- Bank-change requirements depend partly on local regulations and bank partner. A merchant in the United States can submit a bank-account change request in the Control Panel and must provide supporting documents; a merchant outside the United States is directed to contact Braintree for the required documents and approvals. The submitted account must be a business checking account, not a savings, deposit-only or prepaid debit account.
- Viewing the disbursement account in the Control Panel is documented for Braintree Direct merchants in the US and EU. The selected merchant account must be included in the user's role permissions; the view exposes the routing number and the last four account-number digits.
- Only the account's authorized signer can request access to or changes to sensitive account information. The article distinguishes that signer from the Control Panel Account Admin role and routes signer changes or additions through Braintree support. It separately instructs affected UK businesses to provide a new or changed UK VAT registration number immediately; the exact cases and the article's dated turnover-threshold context remain in the raw.

## Material warnings

> [!warning] Bank account and access restrictions
> The page rejects savings, deposit-only and prepaid debit accounts for the submitted disbursement account. Viewing bank information is limited by the documented Braintree Direct, US/EU and merchant-account role-permission conditions. Sensitive account-detail requests remain controlled by the authorized signer, not merely by the Account Admin role.

> [!warning] Collected guidance boundary
> This is a 2026-09-16 snapshot of an account-administration article. It does not prove current regional eligibility, current document or approval requirements, successful acceptance of an update, or current UK VAT law. Follow the cited support and bank-specific routes for the merchant's account and region.

## Detail locators

- Password reset, Manage Users administration and original-email confirmation: `## Control Panel login credentials`, lines 17-21.
- Sensitive-document purpose, eligible Control Panel roles, upload procedure, file formats and password-protection warning: `## Securely upload business documents`, lines 24-46.
- Partner/local-regulation qualification, US versus non-US bank-change routes, supporting documents and accepted account type: `## Bank account information`, lines 51-61.
- Braintree Direct US/EU viewing scope, Control Panel path, displayed bank details and merchant-account permission: `### Viewing your bank account information`, lines 66-81.
- Authorized-signer consent, protected account details, signer identity and distinction from Account Admin: `## Other types of updates` and `### Authorized signer`, lines 86-109.
- UK VAT registration-number definition, dated turnover-threshold context and submission cases: `### VAT registration number`, lines 114-129.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/guides/account-information-2026-09-16|Braintree Updating Account Information]] - complete collected guide for user credentials, secure document upload, bank-account administration, authorized-signer controls and UK VAT-number updates
