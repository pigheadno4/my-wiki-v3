---
title: "Adyen Notification center"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/account/notification-center"
raw_files:
  - "adyen/docs/account/notification-center/2026-09-15.md"
tags: [adyen, customer-area, notifications, service-status, chargebacks]
---

## Overview

This Adyen Customer Area guide explains the **Notification center**, its Email and in-app settings, merchant-account-scoped chargeback notices, and service-status messages. The pinned page was captured 2026-09-15. It describes user-visible notices and subscriptions, not a complete incident feed, payment lifecycle record, or delivery-time guarantee. See [[adyen]] and the proposed [[adyen-notification-center]] concept.

## Key takeaways

- The Notification center lists notices for **merchant accounts the user's account can access**. Each notice links to details or the relevant Customer Area page. An unread item marks the icon with a red dot; selecting a notice marks it read and removes it from the next center list, while **See all notifications** opens a page with all notifications sent to the user. Read/unread is a UI state, not evidence that an underlying issue was resolved.
- Under Notification center settings, the user can enable or disable each notification type separately for **Email** or **Notification center**. Email goes to the address linked to that user. The page refers to user roles only as a See also link; it does not state a particular role prerequisite for viewing the center or changing these toggles.
- Fraud and dispute notices are issued for merchant accounts. For **Chargeback notices**, enabling the type also requires selecting the merchant accounts to receive them for. That subscription controls this user's notices; it is not a financial-outcome or dispute-decision signal.
- **Service status messages** describe Adyen platform status, with scheduled maintenance and downtime as examples. The user can see system messages for merchant accounts they can access; each message specifies its applicable merchant account, and email subscription is optional. The page gives no completeness or timing service-level promise and does not prove a present incident, restoration, or payment outcome.

## Detail locators

- Lines 15–19: page purpose and Customer Area notification configuration route.
- `## Notification center`, lines 21–31: user-access account scope, detail links, unread/read UI behavior, all-notifications page.
- `## Configure notification settings`, lines 33–40: per-type Email and in-app toggles, linked user email address.
- `### Settings for chargeback notifications`, lines 42–44: merchant-account-issued fraud/dispute notices and account selection.
- `## Service status messages`, lines 46–52: maintenance/downtime examples, accessible merchant-account scope, optional email.
- `## See also`, lines 54–57: users and user-roles navigation, with no role rule stated here.

## Related

- [[adyen-notification-center]] — proposed provider concept and reciprocal source route.
- [[adyen-account-structure]] — separate merchant-account hierarchy and access context.
- [[adyen-developer-dashboard]] — separate technical API/webhook activity view.
- [[source-adyen-docs-account-users]] — separately documented Customer Area user management.
- [[source-adyen-docs-account-user-roles]] — separately documented user-role reference.

## Raw Sources

- [[raw/adyen/docs/account/notification-center/2026-09-15|Notification center guide, captured 2026-09-15]]
