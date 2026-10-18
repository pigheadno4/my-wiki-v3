---
title: "Adyen for Platforms terminals quickstart"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/quickstart-guide/terminals"
raw_files:
  - "adyen/docs/platforms/quickstart-guide/terminals/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, terminals, operations]
---

## Overview

This 2026-09-15 Adyen for Platforms quickstart helps a platform choose and operate an in-person payment offering for its users. It compares software and physical terminals, tabletop/mobile/unattended journeys, cloud/local integration, shipping, onboarding, fleet management and terminal-cost reconciliation. It is planning guidance, not evidence that a particular merchant account, user store or device is configured, boarded or processing payments. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Solution and architecture choices:** Software options use an Android or iOS device; the page recommends starting there when suitable, then considering physical terminals for user needs. It describes Mobile SDK Tap to Pay, the Android Payments App and Pay-by-Link as different starting routes; its Pay-by-Link description does not establish a card-present transaction. Select tabletop, mobile or unattended hardware around the user/shopper journey. Cloud integration is the page's general recommendation, while local integration can meet use cases such as offline requirements but needs secure local POS-to-terminal communication. These are recommendations and tradeoffs, not universal eligibility or architecture rules.
- **Hardware logistics and limits:** Physical terminals add procurement, warehousing, returns and support work. The page compares Adyen drop shipping to a user with bulk shipment to a platform warehouse. Orders can be placed in Customer Area or automated with Management API; merchant-account email settings affect Adyen order emails, while couriers may still contact recipients. For warehouse stock, it warns against leaving terminals unused for over six months because low batteries and stale firmware can impede setup, with possible reserve-battery key degradation. Custom packaging is described for platforms shipping at least 1,000 terminals per year, with a request at least three months before planned go-live. Check regional lead times and availability with Adyen.
- **Onboarding and fleet:** The guide recommends supporting early setup operationally and automating later. Customer Area can be used to order/return, assign a terminal to a store, inspect security, board it for payments in a user's store, customize and monitor it. Assignment, boarding and a user's store are distinct steps; this page gives no actual device, account or payment outcome. Terminal Replacement Service is described as a monthly-fee, whole-fleet service, not a per-terminal selection; replacement uses the normal order/return process.
- **Cost trail:** The guide suggests matching the Order Number in an Invoice Report to an order CSV, down to store or terminal. It recommends monthly settlement deduction of terminal costs for Adyen-to-platform billing, and lists platform-to-user sell-through, lease and gift choices plus service-cost treatments. These are commercial options and reconciliation guidance, not proof of a deduction, invoice, settlement or transfer.

## Detail locators

- Hardware/software and Tap to Pay, Payments App, Pay-by-Link choices: pinned raw lines 19-29; use cases and architecture: 31-55.
- Drop shipping, bulk stock, emails, order and shipment processes: pinned raw lines 57-99.
- Packaging threshold, lead time and kit options: pinned raw lines 101-122.
- Terminal onboarding, store assignment, boarding and fleet operations: pinned raw lines 124-149.
- Whole-fleet replacement boundary and order/invoice/settlement examples: pinned raw lines 151-196.

## Related

- [[adyen-platforms]] — main Platforms concept and reciprocal source route.
- [[source-adyen-docs-platforms-manage-stores]] — related store-management route.
- [[source-adyen-docs-point-of-sale-managing-terminals]] — related fleet-management route.
- [[source-adyen-docs-platforms-quickstart-guide-customer-area]] — related Customer Area orientation.

## Raw Sources

- [[raw/adyen/docs/platforms/quickstart-guide/terminals/2026-09-15|Adyen Terminals quickstart, captured 2026-09-15]]
