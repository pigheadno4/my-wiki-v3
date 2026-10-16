---
title: "Adyen Salesforce Order Management System package"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-order-management-system"
raw_files:
  - "adyen/docs/plugins/salesforce-order-management-system/2026-09-15.md"
tags: [adyen, salesforce-oms, order-management, payment-modifications]
---

## Overview

This Adyen Salesforce Order Management System (OMS) package overview (captured 2026-09-15) presents order-fulfillment payment actions that work alongside Salesforce Commerce Cloud payment solutions. OMS is the order-management integration, distinct from the SFCC storefront integrations at [[adyen-salesforce-commerce-cloud]]; the dedicated concept is [[adyen-salesforce-order-management-system]]. The page's 2023-10-13 last-modified metadata precedes a V3 August 2024 release row, so its support table is dated, internally inconsistent metadata rather than current-version proof. It does not document a merchant deployment, successful modification, settlement or bank receipt.

## Key takeaways

- The page describes Salesforce OMS as managing orders, customer records, fulfillment, inventory visibility, payments/invoicing and care, and presents the Adyen OMS package as working with payment solutions provided by Salesforce Commerce Cloud. It does not describe the SFRA or Composable storefront implementation details (raw lines 23–30).
- OMS features listed are full and partial captures at stages of fulfillment; full and partial refund initiation; full void/authorization reversal of authorized payments; and partial cancellation after partial capture, where only the uncaptured remainder is cancelled. These are capability descriptions, not evidence that any request was accepted or money moved (raw lines 31–35).
- Credit-card authorization on a shopper's behalf is tied to the optional Order on Behalf Of (OOBO) feature; OOBO with Pay by Link is listed for payment links. The page links to child setup for those features and to SFCC's supported-method page, but it does not provide an independent OMS method matrix, operator role list, credential scopes, or order-state/result semantics (raw lines 36–43, 65–88).
- The table defines support Levels 1/2/3 as full support, high-priority bug fixes plus security updates, and security updates only. It lists V2 (released October 2023) and V3 (released August 2024) support-until dates. Because page metadata predates the V3 row and the snapshot is dated, verify an applicable current release before using those dates for an upgrade decision (raw lines 45–56).
- The get-started route asks for Adyen live-payment preparation and a test account, then permits sandbox package setup while live credentials are pending; OOBO setup is optional and the SFCC go-live checklist is linked before live use. These are prerequisites/navigation, not proof of account eligibility, installation, successful capture/refund or production readiness (raw lines 58–72).

## Detail locators

- OMS identity and SFCC relationship: raw lines 15–30.
- Capture, refund, cancellation and OOBO/Pay by Link capabilities: raw lines 31–43.
- Dated major-version support table: raw lines 45–56.
- Test-account, sandbox setup and child go-live/upgrade navigation: raw lines 58–88.

## Related

- [[adyen-salesforce-order-management-system]] — distinct OMS concept and source route.
- [[adyen-salesforce-commerce-cloud]] — storefront integrations supplying payment solutions; not an OMS behavior source.
- [[adyen]] — Adyen provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-order-management-system/2026-09-15|Salesforce OMS package overview, captured 2026-09-15]]
