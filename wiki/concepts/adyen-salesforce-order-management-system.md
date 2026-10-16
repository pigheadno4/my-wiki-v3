---
title: "Adyen Salesforce Order Management System"
type: concept
category: technology
tags: [adyen, salesforce-oms, order-management, captures, refunds]
---

## Definition

The Adyen Salesforce OMS package is an order-management payment integration that works with payment solutions from Salesforce Commerce Cloud. The captured overview lists fulfillment-stage full/partial captures, full/partial refund initiation, void or authorization reversal, and cancellation of only the uncaptured remainder after a partial capture. It also lists optional OOBO credit-card authorization and Pay by Link. This OMS route is separate from the [[adyen-salesforce-commerce-cloud]] storefront cartridge and PWA package.

## Evidence boundary

This is a 2026-09-15 webpage snapshot, not a package audit, merchant setup record or payment-result trace. Its 2023-10-13 last-modified metadata predates the support table's V3 August 2024 release row; the V2/V3 support dates and current compatibility require independent release verification. The overview gives no operator roles, credential scopes, order-state mapping or successful capture/refund/settlement evidence. The linked child guides own installation and OOBO behavior.

## Sources

- [[source-adyen-docs-plugins-salesforce-order-management-system-order-status-lifecycle]] — 2023-modified, 2026-09-15-captured SFCC/OMS order-status lifecycle page distinguishing SALE immediate-capture and AUTH separate-capture flows, with an untranscribed status diagram; no individual payment or financial-outcome proof.


- [[source-adyen-docs-plugins-salesforce-order-management-system-authorization-reversal]] — 2023-modified, 2026-09-15-captured OMS v3.1.0+ Salesforce Authorization Reversal guide for Adyen payment cancellation, version-specific CANCELLATION webhook setup, Available-to-Capture matching and asynchronous outcome checks; order cancellation is separate.


- [[source-adyen-docs-plugins-salesforce-order-management-system-install-and-set-up-the-package]] — 2023-modified, 2026-09-15-captured OMS cartridge/Org prerequisites, v3.3.0+ guided setup, capture-mode duplicate-request safeguards and live HMAC/URL/API-key transition; setup is not runtime proof.


- [[source-adyen-docs-plugins-salesforce-order-management-system-set-up-oobo]] — 2024-modified, 2026-09-15-captured OOBO card/Pay by Link setup guide for Salesforce OMS, with v3.2.0+ link gate, SFCC/OMS roles and connections, order/link creation, webhook migration and link-expiry controls; link generation is not payment or capture proof.


- [[source-adyen-docs-plugins-salesforce-order-management-system-upgrade]] — 2024-modified, 2026-09-15-captured OMS v2→v3 and v1→v3.2.0 upgrade branches for gateway/API-key/HMAC/account routing, v1 data script and post-test old-package uninstall; no deployment or payment outcome proof.


- [[source-adyen-docs-plugins-salesforce-order-management-system-install-and-set-up-the-package-manual-setup]] — 2025-modified, 2026-09-15-captured manual Salesforce OMS setup guide for gateway/credential/webhook permissions, capture-mode safeguards and separate live-credential transition; v3.3.0+ defaults to guided setup and success webhooks can precede later failure.


- [[source-adyen-docs-plugins-salesforce-order-management-system]] — Adyen OMS package overview, captured 2026-09-15, for order/payment modification capabilities, optional OOBO, sandbox start and dated major-version support table.

## Related

- [[adyen-salesforce-commerce-cloud]] — distinct SFCC storefront integration family.
- [[adyen]] — provider page.
