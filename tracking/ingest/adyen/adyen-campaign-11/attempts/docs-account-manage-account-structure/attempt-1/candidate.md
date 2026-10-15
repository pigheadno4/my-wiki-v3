---
title: "Adyen manage account structure"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/manage-account-structure"
raw_files:
  - "adyen/docs/account/manage-account-structure/2026-09-15.md"
tags: [adyen, account-structure, merchant-account, account-groups, customer-area]
---

## Overview

This Adyen Customer Area guide explains how to request a new merchant account, request closure of a merchant account, create or edit account groups, and switch between company and merchant account views. It is a 2024-last-modified page captured 2026-09-15. The interface steps and stated lifecycle do not establish that any specific request was approved or a real account changed. See [[adyen]] and [[adyen-account-structure]].

## Key takeaways

- **Request merchant account:** At company-account scope, the user needs both `Merchant admin` and `Merchant additional merchant accounts` user roles. The form asks for a desired account code, ecommerce or POS channel, and initial payment methods before **Submit**. The page says the merchant-account name can later be changed only if no transactions have been processed through it. Submission is a request, not proof of approval or a ready account; payment methods may be added later through a separate guide.
- **Request closure:** A `Merchant admin` user switches to the target merchant account, chooses a requested inactivation month and reason, and selects **Request Closure**. The page says the account becomes inactive on the first day of that month, at which point it no longer processes transactions and Adyen stops charging for it. This is consequential and time-dependent; the button itself is not evidence that closure has completed.
- **After inactivation:** The guide says an inactive account remains accessible for six months **from its last transaction date**, rather than six months from inactivation. During the remaining access period users can view/download reports, defend chargebacks and process refunds. After that period it becomes permanently closed and inaccessible. Its July examples show that post-inactivation access can be shorter than six months.
- **Account groups:** Creating or changing group membership requires the `Manage Merchant Account Groups` user role and company-account access. A user selects merchant accounts and creates a group, or uses **Move to group**, **Remove from group**, or **Create a group from selection**. The page then points to separately granting users access to the new group; creating a group does not itself prove that any user has been granted access.
- **View scope:** The Customer Area account switcher selects company or merchant level. Company-level payment lists show payments for merchant accounts the user can access, while merchant-level lists show only the selected merchant account. This access-filtered UI view is not a legal-entity, merchant-of-record, or payout-ownership determination.

## Detail locators

- Lines 15–24: page's four management routes.
- `## Request a new merchant account`, lines 26–48: both company-account roles, form fields, name-change limit, and request submission.
- `## Delete a merchant account`, lines 50–77: closure role, request, timed inactivation, transaction stop, last-transaction-based access window, and permanent loss of access.
- `## Create an account group`, lines 79–101: group access purpose, role/company prerequisite, group creation, separate user grant.
- `## Edit an account group`, lines 103–127: role/company prerequisite and membership actions.
- `## Switching between accounts`, lines 129–144: access-filtered company versus merchant views.

## Related

- [[adyen-account-structure]] — account hierarchy and reciprocal management source route.
- [[source-adyen-docs-account-account-structure]] — company, merchant, group and optional POS store hierarchy.
- [[adyen-api-access]] — distinct API-credential account scope; this page's roles are Customer Area user roles.

## Raw Sources

- [[raw/adyen/docs/account/manage-account-structure/2026-09-15|Manage account structure, captured 2026-09-15]]
