---
title: "Adyen Issuing team access in Customer Area"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-access"
raw_files:
  - "adyen/docs/issuing/manage-access/2026-09-15.md"
tags: [adyen, issuing, customer-area, access, roles]
---

## Overview

This 2026-09-15 Issuing page introduces Customer Area access for a team: initial admin-user activation, dashboard functions, and role-based permissions. It links to separate user, role and API-credential guides for procedures. See [[adyen-issuing]] and [[adyen]].

## Key takeaways

- Adyen says it automatically creates a platform admin user when a customer signs up. That user receives an email for account verification and becomes active when verification is completed (raw line 19).
- Customer Area is described as a dashboard for an Issuing integration. The page lists viewing payments and account-holder/legal-entity/balance-account/card resources, controlling transaction rules, configuring webhooks, changing card status, reports, and managing organization users and API credentials (raw lines 21–32). The individual linked guides govern those actions.
- The user-management paragraph says access to specific Customer Area sections and functions is controlled by assigned roles (raw lines 34–36). **Terminology caveat:** it also says to create “web service users” for people in the organization. The linked [[source-adyen-docs-issuing-manage-access-api-credentials-web-service]] guide instead describes web-service users as credentials for authenticating API requests (that guide's raw lines 19–25, 42–52). These captured statements do not resolve which user type should be created for interactive human login; consult the dedicated user and role guidance rather than treating this sentence as a complete procedure.

## Detail locators

- Initial admin creation, verification email and activation: raw line 19.
- Customer Area inventory and links to the relevant operation guides: raw lines 21–32.
- Roles and links to user, user-role and API-credential guidance: raw lines 34–48. The present page does not specify the detailed role matrix, API credential permissions or separate test/live access behavior.

## Related

- [[adyen-issuing]] — Issuing concept.
- [[source-adyen-docs-issuing-manage-access-api-credentials-web-service]] — API credential types and lifecycle; clarifies the “web service user” terminology conflict.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-access/2026-09-15|Adyen Issuing manage access, captured 2026-09-15]]
