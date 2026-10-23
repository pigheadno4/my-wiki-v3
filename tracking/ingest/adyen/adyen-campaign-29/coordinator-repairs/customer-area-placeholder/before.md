---
title: "Adyen unified Customer Area migration from Balance Platform Customer Area"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/about-our-customer-area"
raw_files:
  - "adyen/docs/about-our-customer-area/2026-09-15.md"
tags: [adyen, customer-area, balance-platform, migration, user-access]
---

## Overview

This 2026-09-15-captured [[adyen]] migration guide describes replacing Balance Platform Customer Area (BPCA) with unified Customer Area for Issuing and Financial Products journeys. It says transition starts in Q3 2025, gives a February 28, 2026 BPCA-access deadline, and describes staged TEST/LIVE user setup and navigation/role changes. Its timeline is expressly indicative and subject to change; this snapshot does not prove the transition's present completion or an individual user's access. See [[adyen-customer-area-iam]].

## Key takeaways

- **User setup and dated stages:** Users without a Customer Area account are prompted from BPCA to create a password and register MFA separately for TEST and LIVE; existing Customer Area account holders need no setup but may need an admin to assign missing feature roles. The page lists TEST setup from September 1, 2025, LIVE setup from September 8, new-user creation disabled in both BPCA environments on October 9, and BPCA access ending in February 2026. It also says existing Customer Area users and BPCA users with duplicate emails are unaffected. These are the page's dated plans, not observed live-state checks. See pinned raw lines 37–107.
- **Account and menu scope:** Customer Area access is at company-account or merchant-account level, with users managed there. The navigation table moves transfers, issuing functions, API credentials/webhooks and Balance Platform reports into different Customer Area sections; `Score > Risk rules` is `TBD` in the table. Stage 2 says users have the same functionality 'as described in Stage 2', a self-reference, so use the specific menu/role rows rather than inferring a complete feature parity guarantee. See pinned raw lines 83–90 and 109–141.
- **Roles and copy access:** The guide maps BPCA roles to Customer Area role bundles. Users with the Balance platform admin role should have full company-account access when the merchant accounts available to them after transition include all merchant accounts in the company; a Developer without prior admin permissions initially has merchant-level API credentials/webhooks only, requiring admin action for company-level access. An admin with Merchant admin or Merchant user management may copy a user's missing merchant-account access and roles, but can assign only roles/accounts the admin themselves can access; users already holding company-level access skip the merchant-account selection. The copy flow has a review/Confirm step. See pinned raw lines 157–196.
- **Login, links and API boundary:** New password/MFA setup applies separately to TEST and LIVE. A setup verification email is described as once-sendable, with a two-week expiration and admin reissue path. BPCA deep links stop working after deprecation; Customer Area links must select a merchant account belonging to the balance platform that created the target entity, and the page gives distinct TEST/LIVE URL examples. It says API integrations remain functional and unchanged, which concerns the UI migration and does not itself grant API credentials, role access, or payment/funds-movement authority. See pinned raw lines 143–155 and 198–240.

## Detail locators

- Migration rationale and staged TEST/LIVE timeline with subject-to-change caveat: pinned raw lines 15–107.
- Account-level access and navigation changes: pinned raw lines 109–141.
- Verification, mapped roles and scoped copy-access steps: pinned raw lines 143–196.
- Data, downtime, API and deep-link statements plus partner-user route: pinned raw lines 198–252.

## Related

- [[adyen-customer-area-iam]] — Customer Area user and role context.
- [[source-adyen-docs-account-users]] — separate user-management rules.
- [[source-adyen-docs-account-users-partner-users]] — third-party integrator access route.

## Raw Sources

- [[raw/adyen/docs/about-our-customer-area/2026-09-15|Unified Customer Area migration guide, captured 2026-09-15]]
