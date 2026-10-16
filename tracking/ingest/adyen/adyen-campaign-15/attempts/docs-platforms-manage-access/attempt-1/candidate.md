---
title: "Adyen for Platforms Customer Area team access"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-access"
raw_files:
  - "adyen/docs/platforms/manage-access/2026-09-15.md"
tags: [adyen, platforms, customer-area, user-roles, api-credentials]
---

## Overview

This Adyen for Platforms access overview (last modified 2023-07-20, captured 2026-09-15) introduces the **Customer Area** for platform integration administration and the initial **admin user**. Adyen creates that user on signup; email verification activates it. The admin can create team users and assign Customer Area roles to control their permissions. The page routes to separate user, role and Balance Platform API-credential guides; it does not enumerate operation-specific roles or prove a particular account, credential, test/live environment or product is active.

## Key takeaways

- The Customer Area is described as the platform dashboard for company/merchant/account-holder/balance-account resources, payments, methods, transfers, webhooks, reports and optional financial products such as Issuing and Capital. These are navigation areas, not a statement that every merchant account has access to every operation or product.
- The initial admin user's email verification is a **Customer Area user activation** step. Team members receive individual Customer Area accounts and role-assigned permissions. An admin user does not by itself establish a balance-platform API credential, endpoint authorization or successful API request.
- The page distinguishes API-credential categories for **payments**, **balance platform**, and **financial products**. It links specifically to a separate web-service credential guide for Balance Platform API requests. Exact API keys, scopes, environment and operation-level role requirements belong to those child references and the actual account configuration.
- The linked Customer Area URL in this snapshot is a test-domain example. The page does not set a universal test-to-live migration procedure or assert that test permissions/credentials carry over to live.

## Detail locators

- Raw lines 15–19: platform signup, admin-user creation and email-verification activation.
- Raw lines 21–32, `Customer Area`: dashboard resource, payment, credential, webhook, report and financial-product routes.
- Raw lines 34–38, `User management`: admin permissions, team users and assigned Customer Area roles.
- Raw lines 40–52, `Next steps`: separate manage-users, user-roles and Balance Platform API-credential guides.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform resource and account context.
- [[adyen-customer-area-iam]] — distinct Customer Area user-role management concepts.

## Raw Sources

- [[raw/adyen/docs/platforms/manage-access/2026-09-15|Platforms manage access, fetched 2026-09-15]]
