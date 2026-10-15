---
title: "Adyen Customer Area User Migration to SSO"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/single-sign-on/migrate-users-to-sso"
raw_files:
  - "adyen/docs/account/single-sign-on/migrate-users-to-sso/2026-09-15.md"
tags: [adyen, customer-area, sso, user-migration, identity-access]
---

## Overview

This [[adyen]] account guide describes moving existing **Customer Area users** to an already configured single sign-on (SSO) login. Migration is optional for the administrator, can cover some or all users, and requires each affected user to complete the prompted process before their SSO login becomes the recorded method. It concerns Customer Area user access under [[adyen-customer-area-iam]], not web service API credentials or any payment operation.

## Key takeaways

- **Prerequisites and environment:** SSO must already be set up for the Customer Area company account. The acting administrator needs either the **Merchant admin** or **Merchant user management** role. Test and live Customer Area users must be migrated separately; completion in test only grants test-area SSO access.
- **Email/account constraints:** an SSO user's email becomes their username and must be assigned to only one user. With the same email across multiple company accounts, migration leaves access to only one company account; the guide offers separate email addresses per account or remaining on username/account/password login. `EMAIL_ADDRESS_ALREADY_IN_USE` and `SELECTED_MIGRATION_UNAVAILABLE` are separate review cases: the latter concerns an email-login user elsewhere in the same organization and requires changing that user's login method first. Use the status report and exact raw conditions before selecting users.
- **Start versus completion:** `Ready to migrate` permits a start; `Pending migration` means the administrator started it and the user must complete the steps. Username-login users can be started individually or in bulk; email-login users use a separate user-details route that includes first/last name and selecting SSO. The email and next-login prompt direct the user to complete migration with previous credentials. A bulk-start success popup confirms a start, not user completion or SSO access.
- **Access interruption and credential change:** the source says the user cannot access the Customer Area until they finish the migration; after completion they cannot use their previous credentials. The Users page can show the updated SSO login method. Plan for user readiness and an identity provider (IdP) that works before initiating the change; this snapshot is procedural guidance, not proof that a real user's account was changed or that an IdP authentication succeeds.
- **Recovery boundaries:** an administrator can cancel a migration only before the user completes it, including when the IdP or migration is not working; a canceled migration may be restarted by starting it again. For an **email-login user**, the guide separately says the login method can be changed from SSO back to Email at any time. That post-migration login-method change is distinct from canceling an unfinished migration; the page does not promise an equivalent completed-migration rollback for every username-login case.

## Detail locators

- Optionality, separate test/live migration and multiple-company email limit: raw lines 15–28.
- SSO setup and administrator role alternatives: `## Requirements`, raw lines 30–39.
- Management panel, reports and migration statuses/review conditions: raw lines 41–68.
- Duplicate-email correction and new-address verification: raw lines 70–80.
- Username-login individual/bulk start, old-credential completion and lockout: raw lines 82–124.
- Email-login route, required name fields and change back to Email: raw lines 126–146.
- Incomplete-only cancellation, IdP failure example, restart and individual/bulk paths: raw lines 148–173.

## Related

- [[adyen]] — provider context.
- [[adyen-customer-area-iam]] — Customer Area user identity and access route.
- [[source-adyen-docs-development-resources-security-iam]] — broader RBAC, SSO and MFA guidance.
- [[adyen-api-access]] — separate web service API credential identity and roles.

## Raw Sources

- [[raw/adyen/docs/account/single-sign-on/migrate-users-to-sso/2026-09-15|Adyen Customer Area SSO user migration — collected 2026-09-15]]
