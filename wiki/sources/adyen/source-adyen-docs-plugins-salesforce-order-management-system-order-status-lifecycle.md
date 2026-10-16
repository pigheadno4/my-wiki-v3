---
title: "Adyen Salesforce OMS order-status lifecycle"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-order-management-system/order-status-lifecycle"
raw_files:
  - "adyen/docs/plugins/salesforce-order-management-system/order-status-lifecycle/2026-09-15.md"
tags: [adyen, salesforce-oms, salesforce-commerce-cloud, order-status, authorization, capture]
---

## Overview

This Adyen page introduces the Salesforce Commerce Cloud (SFCC) and Salesforce Order Management System (OMS) order-status lifecycle as a synchronization and troubleshooting topic. Its **text** distinguishes SALE and AUTH payment flows; the detailed status diagram is linked as an SVG in the raw page and is not transcribed in this snapshot. Do not derive a specific Salesforce status transition or Adyen financial outcome from the text alone.

## Key takeaways

- In the **SALE flow**, capture follows authorization directly. In the **AUTH flow**, authorization and capture are separate steps. This is a flow distinction, not proof that either operation succeeded for an individual order.
- For alternative payment methods such as local methods, the page says both flows are available and configurable in Adyen Customer Area. Card methods follow AUTH by default. The page does not say that cards cannot use another configuration, nor does it specify a method-by-method eligibility matrix.
- The page directs readers to a diagram to learn order statuses, troubleshoot and test SFCC–OMS synchronization. The retained Markdown has only an SVG image reference, with no text list of order statuses, transition conditions or webhook mapping. Use the diagram/related integration guides for that detail after independently reading them.
- This 2023-modified page, captured 2026-09-15, gives no role, version, credential or merchant-account requirements; no refund or authorization-reversal transition is defined here. An OMS status or configured flow does not establish capture, refund, reversal, settlement, payout or bank receipt.

## Detail locators

- Opening paragraphs, lines 17-26 — SFCC/OMS synchronization purpose and SALE/AUTH definitions, APM configuration and card default.
- SVG reference at line 28 — visual order-status diagram; this raw Markdown does not expose the diagram's status labels as text.
- `## See also` — separate SFCC and OMS integration routes, not independently read behavioral evidence for this source.

## Related

- Company: [[adyen]]
- OMS integration concept: [[adyen-salesforce-order-management-system]]
- Separate storefront concept: [[adyen-salesforce-commerce-cloud]]

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-order-management-system/order-status-lifecycle/2026-09-15|2026-09-15 SFCC/OMS order-status lifecycle page]]
