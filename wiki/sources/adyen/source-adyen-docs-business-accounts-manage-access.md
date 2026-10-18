---
title: "Adyen Business accounts Customer Area and API access"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/manage-access"
raw_files:
  - "adyen/docs/business-accounts/manage-access/2026-09-15.md"
tags: [adyen, business-accounts, platforms, access, roles, api-credentials]
---

## Overview

This Business accounts access guide (last modified 2023-07-20; captured 2026-09-15) describes balance-platform Customer Area users and separate API credential roles. It says Adyen creates an admin user on signup, which becomes active after email verification. The page lists management affordances for accounts, transfers, credentials and webhooks, but listing a role or a TEST Customer Area link does not prove a platform's live account, a user's assigned permission, API acceptance or any executed transfer. See [[adyen]], [[adyen-business-accounts]] and [[adyen-platforms]].

## Key takeaways

- **Human Customer Area access:** The admin user can create team accounts and assign action-specific roles. The guide says all Adyen account users must set up MFA or SSO. For viewing Business accounts, Balance platform base role permits viewing transfers, account holders, balance accounts and Business accounts. View payment instrument PII is an additional role for viewing an Adyen-issued bank account IBAN belonging to a sole proprietorship, and requires the base role. The PII role is narrower than general account viewing, and neither role alone proves a specific user's authorization or ownership of an account.
- **API credential boundary:** The guide distinguishes a web-services API credential from a legal-entity-management API credential. Web-service roles determine API requests possible with that credential; Customer Area human roles are not interchangeable with these credentials. Balance Platform BCL role covers creation/update/deletion of configuration resources. BCL PCI requires BCL and permits unmasking PAN/CVV/CVC only in the described POST paymentInstruments response; Bank SCA Webservice Role manages SCA devices. These are stated capability scopes, not evidence of a successful resource mutation or access to card data.
- **Transfer roles and version:** The Bank Transfer Initiation Webservice role can initiate transfers only for Transfers API v1 in this snapshot. TransferService Webservice Initiate covers initiation, and TransferService Webservice Retrieve covers viewing initiated transfers. A role description is not a transfer request, booking, payout or beneficiary bank receipt.

## Detail locators

- Admin activation and Customer Area functions: pinned raw lines 15–31.
- Team users, MFA/SSO and Business-account/sole-proprietor PII roles: pinned raw lines 33–48.
- Separate web-services and legal-entity credentials: pinned raw lines 50–59.
- Configuration/PCI/SCA roles and transfer roles with v1 qualification: pinned raw lines 61–83.

## Related

- [[adyen-business-accounts]] — main Business accounts concept and reciprocal source route.
- [[adyen-platforms]] — balance-platform access context.

## Raw Sources

- [[raw/adyen/docs/business-accounts/manage-access/2026-09-15|Adyen Business accounts manage-access guide, captured 2026-09-15]]
