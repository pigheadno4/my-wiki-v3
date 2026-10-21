---
title: "Adyen Marketplace UI component libraries overview"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview"
raw_files:
  - "adyen/docs/marketplaces/components-overview/2026-09-15.md"
tags: [adyen, marketplaces, platforms, ui-components, onboarding, reporting]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace overview maps embeddable UI libraries for before-, during- and after-payment user tasks in [[adyen-platform-components]]. The marketplace needs a UI host and backend API layer. Its server validates the logged-in user and creates a session token containing required user roles; the client initializes a component with that token. The page is an inventory and integration route, not evidence that displayed onboarding, payment, payout, dispute or financing actions completed.

## Key takeaways

- Before payment, the Marketplace page lists **Individual Legal Entity** (personal details, identity documents and status), **Terms of Service** (view/accept, status and signed copies), and **Transfer Instrument** (bank-account entry/change/deletion, verification methods and status). During payment it routes to **Checkout** for ecommerce payment UI. These are descriptions of component interfaces; each child guide owns specific setup, consent, verification and outcome conditions. See raw lines 36–68.
- After payment it lists **Transactions**, **Payouts**, **Reports**, **Disputes**, **Pay by Link**, and **Capital**. The descriptions include transaction export/details, payout and balance views, daily report downloads, dispute actions, payment-link management and business-financing application/repayment views. A display or submitted UI action alone does not establish authorization, settlement, bank receipt, resolved dispute or funded grant. See raw lines 70–106.
- The simplified flow is marketplace user login, server validation plus role-bearing authentication session, client component initialization, then user interaction. The setup sequence is server authentication session, front-end library installation, initialization and appearance customization. The page explicitly says some components need extra conditions; follow their respective integration guides. See raw lines 115–133.
- The page describes components as generally available for users operating in Adyen for Platforms supported countries/regions, while **business financing** components have narrower country/region limits. Minimum listed browsers are Chrome 98, Safari 15.4 and Firefox 94, with current versions recommended. These 2026-09-15 statements do not prove current region, product, role or account eligibility. See raw lines 135–149.
- **Cashout components** and a **Capital components update** for UK sole-proprietor Merchant Cash Advances are in a roadmap labelled **Early Q1 2027**. That is a dated plan, not a currently shipped feature; the existing Capital inventory item is separate from the proposed update. See raw lines 102–113.

## Detail locators

- Marketplace UI/backend suitability and component-library purpose: raw lines 17–34.
- Before, during and after payment inventory and child-guide links: raw lines 36–106.
- Dated cashout and Capital-update roadmap: raw lines 108–113.
- Session-token/server/client flow and setup steps: raw lines 115–133.
- General versus financing availability and browser minimums: raw lines 135–149.
- Before/during/after navigation: raw lines 151–163.

## Related

- [[adyen]] — provider profile.
- [[adyen-platform-components]] — canonical UI component-suite concept.
- [[adyen-platforms]] — parent platform context.
- [[source-adyen-docs-platforms-components-overview]] — separate Platforms URL and related inventory; Marketplace route additionally lists Individual Legal Entity and Terms of Service before-payment components.
- [[source-adyen-docs-marketplaces-onboard-users-components]] — narrower onboarding-component overview.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/2026-09-15|Marketplace UI component libraries overview — pinned 2026-09-15 raw snapshot]]
