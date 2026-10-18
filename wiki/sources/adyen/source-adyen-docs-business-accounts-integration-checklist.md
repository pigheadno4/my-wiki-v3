---
title: "Adyen Business Accounts: Integration and go-live checklist"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/integration-checklist"
raw_files:
  - "adyen/docs/business-accounts/integration-checklist/2026-09-15.md"
tags: [adyen, business-accounts, platforms, integration, go-live]
---

## Overview

This 2023-03-06-modified [[adyen]] checklist sequences Business Accounts integration work on top of an Adyen for Platforms marketplace or platform model. It covers account structure, prerequisite integrations, API credentials, webhooks, additional verification, and separate live setup/tests. It is a dated implementation guide, not evidence that any specific user passed KYC, accepted terms, obtained a live Business Account, or completed a transfer. [[adyen-business-accounts]]

## Key takeaways

- Before building, the guide says to design the implementation with an Adyen implementation manager. Its resource map separates company/merchant accounts, balance platform, account holder, balance account, legal entity, transfer instrument, business line and externally facing `bankAccount` payment instrument. It says a payment instrument generates an account number and one balance account can have one `bankAccount` instrument (raw lines 23–50). Resource names identify model roles; their presence alone does not establish an opened or funded account.
- Complete the relevant Adyen for Platforms marketplace **or** platform integration checklist first (raw lines 52–54). The guide says Business Accounts API calls can use existing marketplace/platform API credentials or newly generated credentials with assigned roles in Customer Area. Its table distinguishes a Balance Platform credential for Configuration/Transfers APIs from a company-scoped credential for Legal Entity Management API (raw lines 56–65). This page does not list a complete current role/permission matrix or country eligibility; consult the linked access and product requirements before live use.
- Configure server webhook endpoints and acknowledgments, configure them in Customer Area, and secure them with HMAC. The page names onboarding-information and account debit/credit events as examples of why webhooks matter (raw lines 67–73). Additional Business Accounts verification checks are required; authentication SDK and Open Banking integrations are marked optional. The linked send/receive and internal-direct-debit guides are separate flow instructions, not executed operations here (raw lines 75–83).
- The test setup is **not automatically replicated** in the live account. The go-live sequence calls for live setup, code updates, live API credentials and endpoints, then end-to-end checks of live API requests, business-account creation with `issueBankAccount`, third-party send/receive with `sendToThirdParty`/`receiveFromThirdParty`, and live webhook receipt/acceptance (raw lines 85–106). A checklist item or TEST configuration does not prove those live checks were performed or a transfer reached a bank.

## Detail locators

- Resource-role map and one bankAccount instrument per balance account: raw lines 36–50.
- Marketplace/platform prerequisite and credential table: raw lines 52–65.
- Webhook setup and optional-versus-required feature links: raw lines 67–83.
- Separate live setup and explicit end-to-end test list: raw lines 85–106.

## Related

- [[adyen-business-accounts]]
- [[source-adyen-docs-business-accounts-get-started]] — design and onboarding route.
- [[source-adyen-docs-business-accounts-account-structure-resources]] — account/resource identities.
- [[source-adyen-docs-business-accounts-verification-overview-capabilities]] — capability-state distinctions.
- [[source-adyen-docs-business-accounts-onboard-users-terms-of-service]] — separate consent process.

## Raw Sources

- [[raw/adyen/docs/business-accounts/integration-checklist/2026-09-15|Captured integration and go-live checklist]]
