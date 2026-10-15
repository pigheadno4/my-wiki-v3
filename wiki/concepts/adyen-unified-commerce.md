---
title: "Adyen Unified Commerce"
type: concept
category: technology
tags: [adyen, unified-commerce, omnichannel, payments-data, merchant]
---

## Definition

Adyen's Unified Commerce overview presents a merchant-facing omnichannel offering for viewing payments data across online, in-app and in-person shopper journeys and connected customer-facing/back-end systems. It groups its proposition into Insights, Experiences and Engagement. This provider concept owns the cross-channel overview; POS loyalty, specific shopper-insight mechanisms, and individual payment integrations require their own source routes.

## Evidence boundary

The 2026-09-15 snapshot is an overview with a 2021 last-modified date. It does not define an API, shopper identity-matching rule, privacy/consent implementation, payment or payout object, seller/payee/merchant-of-record allocation, settlement flow, or proof of a merchant's actual unified customer view. Its regional table and UK/UAE qualifications are dated and require current eligibility checks. Treat linked Insights, Experiences, Engagement and use-case pages as navigation until independently reviewed.

## Sources

- [[source-adyen-docs-unified-commerce-retail-use-cases-endless-aisle]] — 2026-09-15 endless-aisle landing page defining in-store ecommerce orders and routing to ship-home and later store-pickup guides; scenario mechanics remain in child sources.


- [[source-adyen-docs-unified-commerce-retail-use-cases-click-and-collect]] — 2026-09-15 retail landing page defining click and collect and routing reserve/try, buy/pickup with changes, and assistant-pickup variants; scenario labels alone do not establish payment or settlement behavior.


- [[source-adyen-docs-unified-commerce-pay-by-link-ios-app]] — iOS merchant app guide for role-gated link creation and app-created link management, with an iOS-specific BNPL exclusion and test/live account selection (2026-09-15 snapshot).


- [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links]] — 2024-modified, 2026-09-15-captured creation-channel overview for Pay by Link, 24-hour/70-day/five-attempt expiry, reuse and account capture settings; BNPL channel conflict remains qualified.


- [[source-adyen-docs-unified-commerce-retail-use-cases-mixed-baskets-accounts]] — 2026-09-15 mixed-basket account-structure guide comparing one full-basket authorization with partial captures against three two-request account/store options and their payment-method and reconciliation consequences; legal entity, MOR and settlement are not specified.


- [[source-adyen-docs-unified-commerce-pay-by-link-settings]] — 2026-09-15 Customer Area Pay by Link settings guide for authorized roles, configured currency/reuse/validity choices, optional shopper data, and immediately applied settings.


- [[source-adyen-docs-unified-commerce-pay-by-link-supported-payment-methods]] — 2026-09-15 Pay by Link Customer Area/API method matrix requiring merchant-account addition, with wallet prerequisites, ACH Direct Debit warning, and unresolved BNPL conflict against the Customer Area creation guide (page metadata last modified 2024-06-11).


- [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-customer-area]] — 2026-09-15 Customer Area Pay by Link guide for user roles, configured link creation, Adyen-hosted shopper form, payment-status and manual-capture distinctions, expiry, and shopper-data limits.


- [[source-adyen-docs-unified-commerce-retail-use-cases-click-and-collect-c-and-c-assistant-pickup]] — 2026-09-15 assistant-pickup click-and-collect guide for zero-amount link/card-identifier matching and later capture of the shopper's separate online authorization; requires linked ecommerce/POS merchant systems.


- [[source-adyen-docs-unified-commerce-retail-use-cases-click-and-collect-c-and-c-try-then-buy]] — 2026-09-15 Adyen Docs reserve-online/try-in-store guide for uncaptured Checkout authorization, purchase-time capture, conditional adjustment or extra POS payment, and permission-bound card/profile lookup.


- [[source-adyen-docs-unified-commerce-retail-use-cases-endless-aisle-e-a-ship-home]] — 2026-09-15 Endless Aisle ship-home guide for terminal authorization, shipment-linked manual and partial captures, mixed baskets, delivery lookup, and store/warehouse return routes.


- [[source-adyen-docs-unified-commerce-retail-use-cases-click-and-collect-c-and-c-add-return]] — 2026-09-15 click-and-collect guide for online-paid orders with pickup identification, referenced returns, and separate in-store add-on payment; requires linked merchant order/inventory systems.


- [[source-adyen-docs-unified-commerce-retail-use-cases-endless-aisle-e-a-store-pickup]] — 2026-09-15 Adyen Docs implementation guide for in-store terminal authorization of online items, pickup-time manual capture, qualified mixed baskets, card-based order lookup and returns.


- [[source-adyen-docs-unified-commerce-pay-by-link]] — 2026-09-15 Pay by Link webpage overview: Adyen-hosted payment page, supplemental online-shop role, three-month link removal and live terms URL prerequisite.


- [[source-adyen-docs-unified-commerce-retail-use-cases]] — 2026-09-15 Adyen Docs retail hub defining click and collect/endless aisle and routing to scenario and mixed-basket account-structure guides; overview only.


- [[source-adyen-docs-unified-commerce-shopper-insights]] — 2021-modified, 2026-09-15-captured overview of cross-channel shopper-data analysis, merchant webhook/database use and pre-storage permission/deletion boundaries; identifier mechanics remain in Collect data.


- [[source-adyen-docs-unified-commerce-mail-order-telephone-order]] — MOTO overview (2024 last-modified; 2026-09-15 capture) defining remote card-not-present transactions, Customer Area/API/terminal routes, and source-qualified fraud/chargeback warning.


- [[source-adyen-docs-unified-commerce-loyalty-program]] — 2026-09-15 Shopper loyalty overview for merchant-managed cross-channel profiles, API-response identifier lookup, illustrative benefits and consent/privacy guidance.


- [[source-adyen-docs-unified-commerce-mail-order-telephone-order-customer-area]] — 2026-09-15 Customer Area Virtual Terminal MOTO guide for staff role, merchant/store selection, form submission, Standard/`AUTHORISATION` webhook test and SAQ C-VT live preparation; separate from Checkout API and POS-terminal MOTO.


- [[source-adyen-docs-unified-commerce-shopper-engagement]] — Unified Commerce engagement overview (2021 last-modified; 2026-09-15 capture) for terminal interaction, loyalty, digital receipts, donation/localization routes and privacy guidance.


- [[source-adyen-docs-unified-commerce-shopper-experiences]] — 2026-09-15 Adyen Docs overview of order/product/payment journey separation and illustrative endless-aisle, link-payment, return, mobile and in-store experiences.


- [[source-adyen-docs-unified-commerce-endless-aisle]] — 2026-09-15 captured endless-aisle guide for in-store ecommerce orders, three Terminal API device setups versus tablet Pay by Link, and physical-store legal-entity assignment for terminal payments.


- [[source-adyen-docs-unified-commerce-terminal-interaction]] — 2026-09-15 Unified Commerce terminal-interaction overview for POS-directed Input/Display requests, merchant processing of responses and scoped privacy guidance.


- [[source-adyen-docs-unified-commerce-collect-data]] — 2026-09-15 captured data-collection guide for merchant-side cross-channel identifier analysis via configured Standard webhooks or differently formatted Terminal API responses, with alias/PAR/reference/token and privacy boundaries.


- [[source-adyen-docs-unified-commerce-loyalty-program-recognize-customers]] — 2026-09-15 Adyen Docs cross-channel returning-customer guide for merchant email/profile lookup, POS card alias and conditional shopper reference, saved-card token and separate payment flows.


- [[source-adyen-docs-unified-commerce-digital-receipts]] — 2026-09-15 in-person digital-receipt guide for terminal card recognition and receipt-channel input, Terminal API receipt data, and merchant CRM/email delivery.


- [[source-adyen-docs-unified-commerce-loyalty-program-create-profiles]] — 2026-09-15 cross-channel merchant-CRM guide for consented online/POS profile creation, distinct card alias, shopper reference and saved-method token roles, and conditional identifier enablement.


- [[source-adyen-docs-unified-commerce-mail-order-telephone-order-api-request]] — 2026-09-15 Checkout Sessions/Web Drop-in MOTO guide for agent-entered card data, required roles, asynchronous AUTHORISATION outcome and SAQ C-VT go-live steps; table/example `Moto` versus `MOTO` remains unresolved.


- [[source-adyen-docs-unified-commerce-loyalty-program-payment-linked-loyalty]] — 2026-09-15 captured cross-channel loyalty tutorial for merchant-owned profiles, online shopper-email/reference lookup, POS card alias recognition, terminal prompts and later webhook updates.


- [[source-adyen-docs-unified-commerce-referenced-refunds]] — Cross-channel referenced-refund guide (2022 last-modified; 2026-09-15 capture) for original-payment PSP references, company-level enablement, Terminal API or Checkout refund paths and asynchronous webhook outcomes.


- [[source-adyen-docs-unified-commerce]] — Adyen Omnichannel overview captured 2026-09-15 for Unified Commerce's merchant proposition, three pillars, regional table and child-guide routes.
