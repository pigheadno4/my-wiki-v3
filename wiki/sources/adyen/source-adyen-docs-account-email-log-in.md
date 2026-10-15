---
title: "Email login | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/email-log-in"
raw_files:
  - "adyen/docs/account/email-log-in/2026-09-15.md"
tags: [adyen, customer-area, email-login, user-migration, iam]
---

## Overview

This 2026-09-15 [[adyen]] guide explains administrator-managed migration of **existing Customer Area users** to email-address login. The documented requirement is the **Merchant admin** Customer Area role. Test and live Customer Areas must be migrated separately, and finishing migration changes how that user logs in to the corresponding environment. This is Customer Area user authentication guidance under [[adyen-customer-area-iam]], not an API credential or account-permission migration.

## Key takeaways

- A user's email must be unique for migration because it becomes the username. The **Requires review** reasons distinguish an email shared by more than one Customer Area account from an email already used by a separate email-login user in the same organization; the latter prevents an SSO user and email-login user sharing that address. The guide gives a duplicate-email change and verification route, and a Support route when the other account or organization is unknown. See raw lines 43–69.
- Administrators can check **Requires review**, **Ready to migrate**, and **Pending migration** statuses and start an individual or bulk migration. Starting an individual migration sends the user a completion email; starting bulk migration does not send that start email, so Adyen recommends notifying affected users. On next login, a bulk-migrated user completes migration with previous credentials; while pending, they cannot access Customer Area until completion. After completion, prior credentials no longer grant Customer Area access. See raw lines 71–100.
- Cancellation is allowed only while the user has not completed migration. A canceled migration can be started again; the guide covers individual and bulk cancellation paths and different user-notification behavior. See raw lines 102–126.
- This page neither configures MFA or SSO nor describes password recovery, role grants, changed account scope, or a merchant's actual login state. Follow its separate SSO and user-role guides for those topics.

## Detail locators

- **Purpose, Merchant admin prerequisite, separate test/live scope:** raw lines 15–31.
- **Migration management and review/ready/pending statuses:** raw lines 29–57.
- **Duplicate address, same-organization SSO/email collision and verification:** raw lines 47–69.
- **Individual versus bulk start, user communications and pending/completed access:** raw lines 71–100.
- **Unfinished-only cancellation and restart:** raw lines 102–126.

## Related

- [[adyen]]
- [[adyen-customer-area-iam]]
- [[source-adyen-docs-account-users]] — user roles and account access
- [[source-adyen-docs-account-single-sign-on-migrate-users-to-sso]] — separate SSO migration route

## Raw Sources

- [[raw/adyen/docs/account/email-log-in/2026-09-15|Adyen email login — collected 2026-09-15]]
