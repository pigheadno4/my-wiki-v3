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

- [[source-adyen-api-explorer-management-latest-post-terminals-terminalid-terminalthemes-unapply]] — 2026-11-07-captured Management API v3 TEST reference for resetting one deployed or boarded Android terminal's theme assignment to a higher-level custom or default theme without deleting the theme; `200` also covers no direct custom assignment.


- [[source-adyen-api-explorer-management-latest-post-stores-storeid-terminalthemes-unapply]] — 2026-11-07-captured Management API v3 TEST store-theme unapply: remove the store assignment without deleting the theme; Android terminals inherit a higher-level/default theme except where individually themed, and `200` does not prove on-device propagation.


- [[source-adyen-api-explorer-management-latest-delete-merchants-merchantid-terminalthemes-id]] — 2026-11-07-captured Management API v3 TEST reference for merchant terminal-theme deletion, including the in-use unapply prerequisite.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-terminalthemes-unapply]] — 2026-11-07-captured Management API v3 TEST merchant terminal-theme unapply; restores company/default fallback subject to store and terminal overrides without deleting the theme.


- [[source-adyen-api-explorer-management-latest-delete-merchants-merchantid-terminalthemes-id-assets]] — 2026-11-07 Management API v3 TEST deletion of one merchant terminal-theme asset by required type/model, with logo-owner edit restriction; 204 deletion does not establish on-device display.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-terminalthemes-id-assets-replace]] — 2026-11-07-captured Management API v3 TEST merchant terminal-theme asset replacement for an existing type/model pair, with model-specific upload constraints and 24-hour CDN URL; replacement response does not prove device application.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-terminalthemes-id-assets]] — 2026-11-07-captured Management API v3 TEST reference for adding a merchant terminal-theme image or video asset by type/model; duplicates require replacement, and creation does not prove device display.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-terminalthemes-id]] — 2026-11-07-captured Management API v3 TEST merchant terminal-theme read, with theme metadata and tokenized asset CDN URLs valid for 24 hours; readback does not establish on-device display.

> [!warning] Contradiction
> This GET reference's access instructions name `Management API - Terminal themes read and write`, while its 403 example names `Management API - Terminal settings read and write`. The capture does not settle the enforced role. [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-terminalthemes-id]]


- [[source-adyen-api-explorer-management-latest-post-companies-companyid-terminalthemes-id-assets]] — 2026-11-07-captured Management API v3 TEST reference for adding a company terminal-theme asset by type/model; duplicates require the replace endpoint, and creation does not prove device display.


> [!warning] Contradiction
> The store terminal-settings PATCH Wi-Fi table labels `eapIntermediateCert` for TLS, while its PEAP request and response examples include it. The capture does not settle when the field is accepted. [[source-adyen-api-explorer-management-latest-patch-stores-storeid-terminalsettings]]


- [[source-adyen-api-explorer-management-latest-patch-stores-storeid-terminalsettings]] — 2026-11-07-captured Management API v3 TEST store terminal-settings PATCH: full containing-object changes and inheritance reset; individual-terminal overrides remain possible, and `200` readback does not prove on-device application.


- [[source-adyen-api-explorer-management-latest-patch-terminals-terminalid-terminalsettings]] — 2026-11-07-captured Management API v3 Test terminal-specific settings PATCH, with full-containing-object update/reset rules, sensitive-setting Advanced role, optional settings readback and device-application boundary.

> [!warning] Contradiction
> This reference describes `eapIntermediateCert` as an EAP TLS field, while its PEAP request and response examples include it. The snapshot does not settle PEAP validation. [[source-adyen-api-explorer-management-latest-patch-terminals-terminalid-terminalsettings]]


- [[source-adyen-api-explorer-management-latest-patch-terminals-terminalid-terminallogos]] — 2026-11-07-captured Management API v3 TEST terminal-logo PATCH; Base64 data updates one terminal logo, while an empty value restores higher-level inheritance.


- [[source-adyen-api-explorer-management-latest-get-terminals-terminalid-terminallogos]] — 2026-11-07-captured Management API v3 TEST read of one terminal's configured logo by terminal ID, with optional Base64 image data and Live rate-limit notice; readback does not prove on-device display or payment readiness.


- [[source-adyen-api-explorer-management-latest-get-terminals-terminalid-terminalsettings]] — 2026-11-07-captured Management API v3 TEST readback of one terminal's configured settings and role-gated sensitive fields; response settings do not prove on-device application or payment readiness.


- [[source-adyen-api-explorer-management-latest-get-stores-storeid-terminalsettings]] — 2026-11-07-captured Management API v3 TEST read of store-level terminal settings by store ID; individual terminal values can differ, sensitive settings need an Advanced role, and readback does not prove device application or payment readiness.


- [[source-adyen-api-explorer-management-latest-get-stores-storeid-terminallogos]] — 2026-11-07-captured Management API v3 TEST GET for a store's model-specific terminal logo; optional Base64 `data` is subject to an individual-terminal override, and readback does not prove on-device display.


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-terminalsettings]] — 2026-11-07-captured Management API `latest` v3 TEST merchant terminal-settings PATCH, with full-containing-object changes, inheritance reset, lower-level overrides and role gates; success does not prove on-device application or payment.

> [!warning] Contradiction
> This source's Wi-Fi schema limits `eapIntermediateCert` to `eap` `tls`, but its illustrative PEAP request and `200` response include that field. The capture does not resolve PEAP acceptance or requirement. [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-terminalsettings]]


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-terminallogos]] — 2026-11-07-captured Management API v3 TEST read of a merchant-account terminal logo by required model; optional Base64 image data remains subject to store or terminal override and does not prove on-device display.


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-stores-reference-terminalsettings]] — 2026-11-07-captured Management API v3 TEST store-reference terminal-settings PATCH; full containing objects, inherited-value resets, terminal overrides, and sensitive-setting role boundary.


- [[source-adyen-api-explorer-management-latest-patch-stores-storeid-terminallogos]] — 2026-11-07-captured Management API v3 TEST PATCH for a store and one terminal model's logo; individual-terminal override and higher-level inheritance apply, while a 200 configuration response does not prove on-device display.


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-stores-reference-terminallogos]] — 2026-11-07-captured Management API v3 TEST reference for updating a store's terminal logo by merchant ID and store reference; empty logo data restores higher-level inheritance.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-stores-reference-terminallogos]] — 2026-11-07-captured Management API v3 Test reference for reading a store-reference terminal logo by model, with optional Base64 data and a 204 no-content success; individual-terminal logos can override the store logo.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-stores-reference-terminalsettings]] — 2026-11-07-captured Management API v3 TEST read of store terminal settings by merchant ID and store reference, with credential roles, lower-level overrides and optional settings readback; this does not prove on-device application or payment readiness.


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-terminallogos]] — 2026-11-07-captured Management API v3 TEST reference for updating one merchant terminal-model logo, including lower-level overrides and empty-value restoration of company inheritance.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-terminalsettings]] — 2026-11-07-captured Management API v3 TEST read of merchant-level terminal settings; store or terminal values can override them, sensitive settings need an Advanced role, and readback does not prove on-device application or payment readiness.


- [[source-adyen-api-explorer-management-latest-patch-companies-companyid-terminallogos]] — 2026-11-05-captured Management API v3 TEST PATCH for one company terminal model's logo; lower-level logos can override it, empty image data restores PSP inheritance, and `200` readback does not prove on-device application.


- [[source-adyen-api-explorer-management-latest-patch-companies-companyid-terminalsettings]] — 2026-11-05-captured Management API v3 TEST company terminal-settings PATCH: lower-level overrides, full-containing-object changes and PSP-inheritance reset rules; 200 does not prove on-device application or payment execution.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminallogos]] — 2026-11-05-captured Management API v3 Test read of a company-level terminal logo by model; optional Base64 `data` is subject to merchant/store/terminal overrides and does not prove on-device display.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-terminalproducts]] — 2026-11-05-captured Management API v3 TEST merchant-account terminal-product catalog read, with required country and ordering role; listing is separate from ordering and device readiness.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminalsettings]] — 2026-11-05-captured Management API v3 TEST read of company terminal settings, with lower-level override scope and an additional Advanced role for sensitive settings; readback does not prove effective on-device configuration or payment readiness.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-terminalorders-orderid-cancel]] — 2026-11-05-captured Management API v3 TEST merchant-path terminal-products-order cancellation, limited to `Placed` orders; `200` describes `Cancelled` order readback, while `204` has no content, and neither proves shipment, refund or device readiness.


- [[source-adyen-api-explorer-management-latest-patch-merchants-merchantid-terminalorders-orderid]] — 2026-11-05-captured Management API v3 TEST PATCH for a merchant terminal products order: Placed-only updates, complete replacement when changing items, and 200 order detail or 204 no-content success; neither establishes shipment or device readiness.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-terminalorders]] — 2026-11-05-captured Management API v3 TEST merchant terminal-order list with status/reference filters, optional order data, and a 204 no-content response; readback does not prove delivery, boarding, or payment readiness.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-terminalorders-orderid]] — 2026-11-05-captured Management API `latest` Test v3 merchant terminal-order read: 200 order details or 204 with no content; optional order status and tracking fields are not delivery or device-readiness proof.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-terminalorders]] — 2026-11-05-captured Management API v3 test merchant terminal-product order reference with 200 representation or 204 no-content success; test calls create no actual test-terminal orders, and a returned order is not shipment, boarding or payment proof.


- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-shippinglocations]] — 2026-11-05-captured Management API v3 TEST merchant shipping-location creation for later terminal orders, requiring Terminal ordering read/write; 200/204 is not order or delivery proof.

> [!warning] Contradiction
> The phone-number table specifies 10–14 digits with an optional `+` prefix, but the request example has spaces and the response example omits them. The capture does not settle acceptance or normalization. [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-shippinglocations]]


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-shippinglocations]] — 2026-11-05-captured Management API v3 TEST merchant shipping-location list for terminal orders, with live rate-limit qualification; readback does not place or deliver an order.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-billingentities]] — 2026-11-05-captured Management API v3 Test, role-gated merchant billing-entity list for later terminal orders; optional `data` or a `204` supplies no order or delivery proof.


- [[source-adyen-api-explorer-management-latest-get-merchants-merchantid-terminalmodels]] — 2026-11-05-captured Management API v3 TEST merchant terminal-model lookup with ordering-read roles and a Live rate-limit notice; optional model-list readback supplies IDs for later queries, not order, inventory or device-readiness proof.


- [[source-adyen-api-explorer-management-latest-post-companies-companyid-terminalorders-orderid-cancel]] — 2026-11-05-captured Management API v3 TEST cancellation of a company-path terminal products order only while `Placed`; a successful response reports `Cancelled`, with Live rate-limit notice and no shipping, refund or device-state proof.

> [!warning] Contradiction
> The response schema calls for two-letter ISO country codes in billing/shipping addresses, but the `200` example uses `"Netherlands"` for both. Treat sample address values as illustrative. [[source-adyen-api-explorer-management-latest-post-companies-companyid-terminalorders-orderid-cancel]]


- [[source-adyen-api-explorer-management-latest-patch-companies-companyid-terminalorders-orderid]] — 2026-11-05-captured Management API v3 TEST PATCH for a company terminal products order: updates are Placed-only, and changing items replaces the entire array; 200 returns order details, not shipment or device-readiness proof.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminalorders-orderid]] — 2026-11-05-captured Management API `latest` Test v3 read of a company terminal-products order, with optional status, tracking, product, billing and shipping details; order readback does not prove delivery or device readiness.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminalorders]] — 2026-11-05-captured Management API v3 TEST company terminal-order list with status/reference filters and optional order data; readback does not prove shipment delivery, device boarding, or payment readiness.


- [[source-adyen-api-explorer-management-latest-post-companies-companyid-terminalorders]] — 2026-11-05-captured Management API v3 test reference for creating a company terminal-product order, with optional request/response fields and a test endpoint that does not create actual test-terminal orders; a returned order is not shipment, boarding or payment proof.


- [[source-adyen-api-explorer-management-latest-post-companies-companyid-shippinglocations]] — 2026-11-05-captured Management API v3 TEST company shipping-location creation for later terminal orders, requiring Terminal ordering read/write; Live rate limits are noted, and location creation is not order or delivery proof.

> [!warning] Contradiction
> This reference describes contact phone numbers as 10–14 digits with an optional `+` prefix, but its request and response examples include spaces. The example does not settle validation. [[source-adyen-api-explorer-management-latest-post-companies-companyid-shippinglocations]]


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-shippinglocations]] — 2026-11-05-captured Management API v3 TEST company and merchant shipping-location list for terminal orders, with live rate-limit qualification; listing does not place or deliver an order.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-billingentities]] — 2026-11-05-captured Management API v3 Test read of company and associated merchant billing entities for terminal ordering; an optional `data` readback supplies possible `billingEntityId` values but does not place an order or prove delivery.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminalproducts]] — 2026-11-05-captured Management API v3 TEST country-specific company terminal-product catalog read, with ordering-role and live rate-limit notes; listing does not place an order or prove device readiness.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminalmodels]] — 2026-11-05-captured Management API v3 TEST company terminal-model lookup with ordering-read roles and a Live rate-limit notice; optional model-list readback supplies IDs for later queries, not order, inventory or device-readiness proof.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminalactions-actionid]] — 2026-11-05-captured Management API v3 TEST GET of one company terminal action by action ID, with action type, reported status, schedule/confirmation times and result fields; live requests have rate limits. Readback is not a new action or payment-readiness proof.


- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminalactions]] — 2026-11-05-captured Management API `latest` Test v3 company terminal-action list; excludes Adyen-scheduled actions, supports type/status filters and pagination, and returns action status rather than device or payment proof.


- [[source-adyen-api-explorer-management-latest-post-terminals-terminalid-reassign]] — 2026-11-05-captured Management API v3 TEST terminal reassignment reference for company, merchant, merchant inventory, or store destinations; merchant assignment requires an explicit inventory flag, and 200 has no device-state readback.


- [[source-adyen-api-explorer-managementnotification-latest-post-terminalsettings-modified]] — 2026-09-15-captured Management notification for completed terminal-settings update request, with optional resource IDs and updater source; the event does not show settings or prove on-device application.


- [[source-adyen-api-explorer-managementnotification-latest-post-terminalboarding-triggered]] — 2026-09-15-captured terminalBoarding.triggered successful-boarding notification contract; webhook acceptance is separate from device configuration or payment readiness.


- [[source-adyen-api-explorer-managementnotification-latest-post-terminalassignment-completed]] — 2026-09-15-captured `ManagementNotification/latest` terminal reassignment-completed event with account, terminal and originating-request IDs, optional store IDs, and `2xx` receiver acceptance separate from device boarding.


- [[source-adyen-api-explorer-managementnotification-latest-overview]] — 2026-09-15-captured Management Webhooks v3 overview listing terminal assignment, boarding-result and settings events alongside other account events; catalog listing is not terminal readiness proof.


- [[source-adyen-api-explorer-postfmapi-latest-post-getterminalsunderaccount]] — 2026-09-15-captured deprecated POS Terminal Management API v1 test-server list for company, merchant and store terminal assignments; in-store means ready to board or boarded, not operational readiness.


- [[source-adyen-api-explorer-postfmapi-latest-post-getterminaldetails]] — 2026-09-15-captured deprecated POS Terminal Management v1 TEST detail lookup for terminal identity and assignment/boarding indicators; fleet fields do not prove payment readiness.


- [[source-adyen-api-explorer-postfmapi-latest-post-getstoresunderaccount]] — 2026-09-15-captured deprecated POS Terminal Management API v1 TEST company/merchant store-list reference with store status and assigned-terminal IDs; it does not prove terminal readiness.


- [[source-adyen-api-explorer-postfmapi-latest-post-findterminal]] — 2026-09-15-captured deprecated POS Terminal Management API v1 TEST assignment lookup for terminal company/merchant/store, with merchant-inventory boarding distinction and 2025 support-stop notice.


- [[source-adyen-api-explorer-postfmapi-latest-post-assignterminals]] — 2026-09-15-captured, deprecated POS Terminal Management API v1 TEST assignment reference for merchant/store/company-inventory moves and per-terminal asynchronous results; use the separate Management API for current fleet automation.


- [[source-adyen-api-explorer-postfmapi-latest-overview]] — 2026-09-15-captured deprecated POS Terminal Management API v1 catalog for terminal/store lookup and assignment, with legacy authentication, endpoint/version details and Management API migration direction.


- [[source-adyen-api-explorer-management-latest-post-terminals-scheduleactions]] — 2026-09-15-captured Management API v3 TEST terminal-action scheduling reference for one action, at most 100 terminal IDs, store-assignment condition and per-terminal scheduling result; `totalScheduled` is not device-execution proof.


- [[source-adyen-api-explorer-management-latest-get-terminals]] — 2026-09-15-captured Management API v3 test-server `GET /terminals` contract for role-gated fleet listing, filters, pages and assignment states; inventory data does not prove live readiness.


- [[source-adyen-docs-point-of-sale-firmware-release-notes]] — 2026-09-15 snapshot of physical-terminal software and separate mobile SDK/Payments-app release histories, with version/model availability, LTS and breaking-change locators; no installed-version or transaction proof.


- [[source-adyen-docs-industries-peak-season-in-person-payments]] — 2026-09-15 Adyen peak-season in-person planning guide for method testing, fleet/software preparation, outage options and cloud endpoint checks; terminal version/freeze details are 2025-season guidance with an inconsistent date range.


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
