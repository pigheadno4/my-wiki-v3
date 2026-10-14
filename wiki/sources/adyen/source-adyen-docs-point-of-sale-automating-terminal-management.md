---
title: "Adyen Docs: Automate the management of your terminals"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/automating-terminal-management"
raw_files:
  - "adyen/docs/point-of-sale/automating-terminal-management/2026-09-15.md"
tags: [adyen, point-of-sale, management-api, terminal-management]
---

## Overview

Adyen's unversioned POS documentation, captured 2026-09-15, introduces Management API automation for ordering, assigning, and configuring payment terminals and scheduling terminal actions. Customer Area is the manual alternative. This is terminal fleet administration, separate from Terminal API payment messages and from store creation or payment-method administration. [[adyen]] · [[adyen-terminal-management]] · [[adyen-pos-store-management]]

## Key takeaways

- The page frames the sequence as API-managed order, assignment, and configuration, followed by store-staff boarding when the configured device reaches its assigned store. It also routes to API scheduling of terminal actions. The linked task guides hold the procedures; this overview alone does not establish that a particular terminal is boarded, ready, or payment-capable.
- Management API requests require an API credential with an API key and task-specific roles. A cloud-communications Terminal API integration may reuse its existing API key, but the required Management API roles still depend on ordering, assignment, feature configuration, or action scheduling.
- Live Management API terminal and store endpoints are rate-limited by endpoint group. Requests beyond a group's window are blocked until the window ends; the snapshot's example response carries `"detail": "too many requests"` with status 500. The listed limits are explicitly indicative and may change; they do not establish a current quota or retry guarantee.

## Detail locators

- **Credential and role matrix:** raw heading “API key and roles” (lines 23–36). The matrix separates Terminal ordering, Stores, Terminal settings (including Advanced), and Terminal actions roles; inspect it for the specific operation.
- **Live endpoint groups:** raw heading “Rate limits in the live environment” (lines 38–58), then “Company endpoints and rate limits” (62–92), “Merchant endpoints and rate limits” (96–124), “Store endpoints and rate limits” (126–142), and “Terminal endpoints and rate limits” (146–161). The tables distinguish company, merchant, store, and terminal paths, with separate 160 and 2000 requests/minute groups. The listed live base URL contains `v{version_number}`; the overview does not select a concrete API version.
- **Task routes:** raw heading “What do you want to do?” (lines 163–187) links the order, assign, configure, and schedule-action guides. These are navigation to detailed procedures, not evidence of a completed order, assignment, configuration, or action.

## Related

- [[adyen-terminal-management]] — Management API terminal-fleet administration
- [[adyen-pos-store-management]] — separate store and payment-method administration
- [[adyen-terminal-api]] — in-person payment messaging boundary
- [[adyen-api-access]] — general credential and role scope

## Related raw API references

The linked order, assignment, configuration, and terminal-action guides and API Explorer endpoints were not read for this entry; use these links as navigation only:

- [[raw/adyen/docs/point-of-sale/automating-terminal-management/order-terminals-api/2026-09-15|Order terminals with API]]
- [[raw/adyen/docs/point-of-sale/automating-terminal-management/assign-terminals-api/2026-09-15|Assign terminals with API]]
- [[raw/adyen/docs/point-of-sale/automating-terminal-management/configure-terminals-api/2026-09-15|Configure terminals with API]]
- [[raw/adyen/docs/point-of-sale/android-terminals/deploy-apps/terminal-actions-api/2026-09-15|Schedule terminal actions with API]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/automating-terminal-management/2026-09-15|Adyen terminal-management overview, fetched 2026-09-15]]
