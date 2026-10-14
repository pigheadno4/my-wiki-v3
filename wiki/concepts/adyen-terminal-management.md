---
title: "Adyen Terminal Management"
type: concept
category: technology
tags: [adyen, point-of-sale, management-api, terminal-management]
---

## Definition

Adyen terminal management uses Management API or the Customer Area to administer the physical terminal fleet. The 2026-09-15 overview routes API automation for ordering, assigning devices to stores, configuring features, and scheduling terminal actions; store staff board a configured terminal after delivery to its assigned store. This administration is distinct from [[adyen-terminal-api]] payment messaging and from [[adyen-pos-store-management]] store creation and payment-method settings.

## Operational boundary

Management API requests need an API credential, API key, and operation-specific roles. A cloud Terminal API integration may reuse its API key, subject to those roles. Live terminal-management and store endpoints have group-based rate limits; the snapshot's figures are indicative and can change. This overview does not establish current account eligibility, a device's boarding or configuration state, successful actions, or payment execution. Consult the linked task guides and current API contract before acting.

## Sources

- [[source-adyen-docs-point-of-sale-menu-access]] — Adyen 2026-09-15 terminal menu/passcode guide for Customer Area and Management API roles, setting inheritance, unattended Android screen-lock caution, and maintenance/restart timing.


- [[source-adyen-docs-point-of-sale-managing-terminals-customize-terminals]] — Adyen Customer Area terminal-customization overview captured 2026-09-15, routing display, receipt, feature, and setting-level topics to detailed guides.


- [[source-adyen-docs-point-of-sale-managing-terminals-assign-terminals]] — Adyen Customer Area assignment guide (2024-08-19 modified; 2026-09-15 capture) for inventory-to-store and CSV assignment, old-store configuration timing, and reboarding.


- [[source-adyen-docs-point-of-sale-release-updating-manual-deployment]] — 2026-09-15 Customer Area guide for manually scheduling LTS terminal-software pilots and fleet batches, distinguishing plan approval, per-device status, and newly boarded default versions.


- [[source-adyen-docs-point-of-sale-managing-terminals-board-terminal]] — Adyen physical terminal boarding guide captured 2026-09-15 for assignment-before-boarding, manual versus eligible OTP flow, payment-method/software/role gates and old-store reassignment risk.


- [[source-adyen-docs-point-of-sale-managing-terminals-maintain-performance]] — 2026-09-15 Adyen Terminal API/standalone maintenance guide for scheduled calls, restart-hour reboots, configuration/software application, exceptions and power/network prerequisites; timing is snapshot-qualified.


- [[source-adyen-docs-point-of-sale-release-updating]] — 2026-09-15 Adyen terminal-software update strategy for automatic monitored rollout, Adyen-approved manual LTS releases, and beta participation across Terminal API and standalone terminals; planned dates are snapshot-only and the page does not prove a device's installed version.


- [[source-adyen-docs-point-of-sale-automating-terminal-management-configure-terminals-api]] — 2026-09-15 Management API guide to terminal settings and logos across company, merchant, store, and terminal levels; consult for inheritance, PATCH removal, roles, and configuration timing.


- [[source-adyen-docs-point-of-sale-managing-terminals-order-terminals]] — 2026-09-15 Adyen Customer Area guide for terminal sales, returns, TRS replacements, hardware kits, cancellation, and logistical updates.


- [[source-adyen-docs-point-of-sale-managing-terminals]] — 2026-09-15 Adyen terminal-fleet navigation overview for ordering, store assignment before boarding, inspection cadence, operational topics and API-administration routes; detailed procedures and current eligibility require separate evidence.


- [[source-adyen-docs-point-of-sale-automating-terminal-management-assign-terminals-api]] — 2026-09-15 Adyen Management API guide for terminal reassignment, account/inventory states, boarding boundary, required roles, asynchronous response, and assignment-complete webhook.


- [[source-adyen-docs-point-of-sale-automating-terminal-management-order-terminals-api]] — 2026-09-15 Management API guide to company/merchant terminal and accessory orders, prerequisite IDs, live-only creation, and Placed-only order changes.


- [[source-adyen-docs-point-of-sale-automating-terminal-management]] — unversioned Adyen POS Management API overview captured 2026-09-15 for fleet tasks, credential roles, live rate-limit groups, and detailed task routes.
