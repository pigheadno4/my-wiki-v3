---
title: "Adyen Salesforce OMS Order on Behalf Of setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-order-management-system/set-up-oobo"
raw_files:
  - "adyen/docs/plugins/salesforce-order-management-system/set-up-oobo/2026-09-15.md"
tags: [adyen, salesforce-oms, oobo, pay-by-link, order-entry]
---

## Overview

This 2024-10-09-last-modified, 2026-09-15-captured guide describes **Order on Behalf Of (OOBO)** in the Adyen Salesforce Order Management System package: a customer-service employee places a Salesforce order using a card entry route or creates an Adyen Pay by Link for shopper payment. It covers required SFCC/OMS connections, roles and configuration, then a link-management and diagnostic route. A Salesforce account/order, generated link, Adyen payment and capture are distinct states. See [[adyen-salesforce-order-management-system]] and [[adyen]].

## Key takeaways

- **Platform and role prerequisites:** The page requires an Adyen SFCC cartridge for SFRA or SiteGenesis, Adyen OMS package, a functioning OMS Org connected to SFCC, Standard webhooks and a Web Service user with the API PCI Payments role. Pay by Link additionally calls for Merchant admin or Pay by Link Settings in Customer Area, employee External Credential assignment and the page's separate Salesforce permission/setup steps. These are role and connection requirements, not evidence they are granted in a particular Org.
- **Two routes, with a version gate:** The card path follows Salesforce OOBO and External Payments Package setup; the guide lists cartridge-supported credit cards. OOBO with Pay by Link is described for OMS package **v3.2.0+**, with iDEAL, Apple Pay, PayPal and supported cards listed for the snapshot. An existing v3.1.0-or-earlier integration moving to v3.2.0 for Pay by Link must update webhook configuration to receive payment-status events. A card path's phrase “do not require additional verification” does not establish a universal authentication exemption or card acceptance.
- **Pay by Link order transition:** The employee needs a Salesforce shopper account with contact email and matching store/account currency, selects store/product and delivery details, then **Submit Order** creates an order and generates a payment link. The merchant must build its own sharing logic. This order/link generation is not shopper completion, authorization, capture, settlement or bank receipt. The page does not define a capture policy for these OOBO paths.
- **Identity and configuration:** The guide provisions the Cart and Checkout Data connection, matches WebStore identity and locale to SFCC, identifies the Adyen Payment Gateway ID and creates a `StoreIntegratedService` joining those IDs. Pay by Link adds custom metadata for expiry duration (default 24 hours), return URL and theme, plus Order Summary page layout. `Expire` invalidates **all** links on the order; `Regenerate` invalidates all existing links and creates a new one, so these actions change shopper-accessible links.
- **Security and troubleshooting:** The guide's 403 diagnostic points to the API PCI Payments role; a disabled-user message points to Salesforce Order Management Operations Manager permission. These are conditional remedies, not proof of the only possible cause. Preserve credential access and verify actual Salesforce/Adyen permissions and webhook configuration for the installed version.

## Detail locators

- Lines 15–21: OOBO identity and card versus hosted Pay by Link choices.
- `## Requirements`, lines 23–35: SFCC/OMS, API/Customer Area roles, Standard webhooks, v3.2.0+ link gate and connected Org.
- Lines 37–57: listed payment methods and card OOBO setup navigation.
- Lines 59–98: Pay by Link flow, order/link creation, own sharing logic, setup and v3.2.0 webhook migration.
- Lines 100–146: Cart and Checkout connection, WebStore/Payment Gateway identification, `StoreIntegratedService`, employee External Credential.
- Lines 148–202: link metadata, default expiry, Order Summary layout and expire/regenerate effects.
- Lines 204–234: conditional locale, permission, tenant, delivery, gateway and API-role troubleshooting.

## Related

- [[adyen-salesforce-order-management-system]] — OMS package concept and OOBO route.
- [[adyen-salesforce-commerce-cloud]] — separate storefront cartridge prerequisite.
- [[source-adyen-docs-plugins-salesforce-order-management-system]] — OMS package overview.
- [[source-adyen-docs-plugins-salesforce-order-management-system-install-and-set-up-the-package-manual-setup]] — manual OMS credential and webhook setup route.
- [[source-adyen-docs-unified-commerce-pay-by-link]] — hosted link concept and payment lifecycle boundary.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-order-management-system/set-up-oobo/2026-09-15|Salesforce OMS OOBO setup, captured 2026-09-15]]
