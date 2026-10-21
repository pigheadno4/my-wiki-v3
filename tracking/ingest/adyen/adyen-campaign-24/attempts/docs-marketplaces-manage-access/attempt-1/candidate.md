---
title: "Adyen Marketplaces: manage team access"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/manage-access"
raw_files:
  - "adyen/docs/marketplaces/manage-access/2026-09-15.md"
tags: [adyen, marketplaces, platforms, customer-area, user-roles, api-credentials]
---

## Overview

This 2023-modified Marketplace access overview, captured 2026-09-15, introduces the Customer Area and initial admin user for managing a [[adyen-platforms]] marketplace integration from [[adyen]]. Adyen creates the admin user after signup; email verification activates that Customer Area user. The page routes to separate user, role and Balance Platform API-credential guides. It does not establish operation-specific grants, live-account access or successful API requests.

## Key takeaways

- The initial marketplace admin user receives an email to verify the account; completing that verification activates the user. The Customer Area is an online dashboard for managing the marketplace integration. Its snapshot link points to a test Customer Area domain. See raw lines 19–25.
- The dashboard routes to company/merchant/account-holder/balance-account resources; payments, payment methods and transfers; separate payments, balance-platform and financial-product API credentials; webhooks and reconciliation reports; and optional financial products such as Issuing and Capital. These are navigation capabilities, not proof that every product or permission is active for a particular account. See raw lines 25–32.
- The admin can create team Customer Area users and assign roles to control each user's permissions. This Customer Area user/role model is distinct from API credentials used to authenticate programmatic requests. Exact role powers, keys, scopes and environment-specific authorization belong to the linked child guides and actual configuration. See raw lines 34–38 and 40–52.

## Detail locators

- Initial admin creation and email-verification activation: raw lines 15–19.
- Customer Area resource, payment, credential, webhook, report and product routes: raw lines 21–32.
- Team-user creation, role assignment and child guide links: raw lines 34–52.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — modern Platforms and Marketplaces route.
- [[adyen-customer-area-iam]] — Customer Area user and role concepts.
- [[source-adyen-docs-marketplaces-manage-access-api-credentials-web-service]] — separate Balance Platform API-credential creation and lifecycle guide.
- [[source-adyen-docs-platforms-manage-access]] — separate Platforms URL with closely related access overview.
- [[adyen-classic-platforms]] — legacy Classic Platforms, a distinct integration model.

## Raw Sources

- [[raw/adyen/docs/marketplaces/manage-access/2026-09-15|Manage access for your team — pinned 2026-09-15 raw snapshot]]
