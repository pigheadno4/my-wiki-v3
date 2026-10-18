---
title: "Adyen Platforms manage split configuration profiles"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/automatic-split-configuration/manage-split-configurations"
raw_files:
  - "adyen/docs/platforms/automatic-split-configuration/manage-split-configurations/2026-09-15.md"
tags: [adyen, platforms, automatic-splits, split-configurations, management]
---

## Overview

This 2026-09-15 Adyen for Platforms hub explains the scope and capture-time effect of managing automatic split-configuration profiles linked to a user's store. It routes detailed Customer Area and Management API procedures to separate guides. A linked profile supplies the highest-priority matching rule's split instructions for payments unless a capture request supplies transaction-specific split instructions. See [[adyen]], [[adyen-platforms]] and [[adyen-automatic-split-configuration]].

## Key takeaways

- **Management methods:** The page says rules can be added or removed and existing rule conditions or split instructions changed in Customer Area or with the Management API. Changing a profile description and setting a card-region condition are Management API-only on this page. It does not specify roles, API payloads, exact rule-deletion constraints or other effects; use the linked method guides for those details.
- **Capture timing and precedence:** Adyen checks the profile when capturing a payment. If the profile is updated after authorization but before capture, the updated profile applies to that capture. Transaction-specific split instructions in the capture request override the profile. Treat a pre-capture configuration change as potentially affecting already-authorized payments; an authorization-time view alone is not a reliable prediction of their capture split.
- **Evidence boundary:** This hub states configuration behavior, not that a profile is actually linked or a specific rule matched, capture occurred, money was booked, or a payout completed. It does not state that profile or rule edits are irreversible or that a delete has a specific fallback outcome.

## Detail locators

- Purpose, store-linked profile and highest-priority rule: pinned raw lines 15-19.
- Customer Area versus Management API operations and API-only fields: pinned raw line 21.
- Capture-time reevaluation and transaction-specific override: pinned raw line 23.
- Separate method-guide routes: pinned raw lines 25-33.

## Related

- [[adyen-automatic-split-configuration]] — main concept and reciprocal source route.
- [[source-adyen-docs-platforms-automatic-split-configuration]] — profile-rule hierarchy and fallback overview.
- [[source-adyen-docs-platforms-automatic-split-configuration-manage-split-configurations-customer-area]] — detailed Customer Area management route.

## Related raw API references

- [[raw/adyen/docs/platforms/automatic-split-configuration/manage-split-configurations/api/2026-09-15|Management API profile-management guide]] — separate method detail; not evidence for this entry.

## Raw Sources

- [[raw/adyen/docs/platforms/automatic-split-configuration/manage-split-configurations/2026-09-15|Adyen Manage split configuration profiles, captured 2026-09-15]]
