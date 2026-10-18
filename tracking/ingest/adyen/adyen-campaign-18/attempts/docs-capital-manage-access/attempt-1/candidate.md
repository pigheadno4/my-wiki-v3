---
title: "Manage access for your Capital team | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/manage-access"
raw_files:
  - "adyen/docs/capital/manage-access/2026-09-15.md"
tags: [adyen, capital, platforms, access, credentials, roles]
---

## Overview

This [[adyen]] Capital access guide, last modified 2023-07-20 and captured 2026-09-15, describes Customer Area user roles separately from web-service API credential roles for managing a balance-platform Capital integration. It lists common roles, not an exhaustive permission matrix or evidence that any live user or credential holds them. See [[adyen-capital]].

## Key takeaways

- The page says Adyen creates a platform admin user at signup, sends a verification email and activates that user after verification. In Customer Area, an admin can manage integration resources, team access, API credentials, webhooks and Capital-offering information. The page describes the admin as holding integration-management permissions and able to grant team members roles. These are documented setup semantics, not proof that a particular user is active or authorized. [Raw: lines 19–37]
- Customer Area users must set up MFA or SSO. The **Capital base role** is specifically described as allowing a user to view Capital grants and grant details in Customer Area; it is not stated as an API credential role or general grant-initiation authority. [Raw: lines 35–49]
- API requests require appropriate credentials. The described balance-platform setup includes separate web-service and legal-entity-management credentials. Web-service roles govern which requests a credential can perform; the page's tables are labeled the **most frequently used** roles, so they should not be treated as all possible roles or as automatic grants of access. [Raw: lines 51–68]
- For balance-platform configuration, **Balance Platform BCL role** is described for creating, updating and deleting resources such as account holders, balance accounts and transfer instruments. **Balance Platform BCL PCI role** permits unmasking/viewing PAN and CVV/CVC in the specified `POST /paymentInstruments` response and also requires BCL. This is sensitive card-data access tied to that response and role combination, not a generic Capital role. [Raw: lines 66–74]
- For Capital API credential roles, **Balance Platform Capital Configuration Role** is described for viewing grant-offer and grant-account details, and **Balance Platform Capital Grant Initiation Role** for configuring grants. The page does not establish the exact live credential assignments, current API access, user capability, offer acceptance, disbursement, repayment or any financing outcome. [Raw: lines 75–82]

## Detail locators

- Admin creation/verification and Customer Area functions: raw lines 19–31.
- User permissions, MFA/SSO and Capital base role: raw lines 33–49.
- Web-service versus legal-entity credentials and role-scoped requests: raw lines 51–64.
- BCL, conditional PCI card-data access and Capital credential role descriptions: raw lines 66–82.

## Related

- [[adyen-capital]] — Capital product and access context
- [[adyen-platforms]] — balance-platform context
- [Manage users](https://docs.adyen.com/account/users) — related Customer Area administration
- [Balance Platform API credentials](https://docs.adyen.com/platforms/manage-access/api-credentials-web-service/) — linked credential guide
- [MFA](https://docs.adyen.com/account/multifactor-authentication/) — related account security
- [SSO](https://docs.adyen.com/account/single-sign-on) — related account security

## Raw Sources

- [[raw/adyen/docs/capital/manage-access/2026-09-15|Adyen Capital manage access — collected 2026-09-15]]
