---
title: "Adyen for Platforms UI component libraries overview"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/components-overview"
raw_files:
  - "adyen/docs/platforms/components-overview/2026-09-15.md"
tags: [adyen, platforms, ui-components, onboarding, reporting]
---

## Overview

This 2026-09-15 Adyen for Platforms page inventories embeddable UI component libraries for tasks before, during, and after payment. The platform supplies a UI host and backend API layer; its server validates the logged-in user and creates a role-bearing authentication session token, and the client initializes a component with that token. The overview is an integration map, not proof that a component's displayed action or underlying financial operation completed.

## Key takeaways

- The listed current routes are Transfer Instrument before payment; Checkout during payment; and Transactions, Payouts, Reports, Disputes, Pay by Link, and Capital after payment. Their descriptions include bank-account management and verification display, ecommerce checkout, transaction/payout/report views, dispute response, payment-link management, and Capital application/repayment views. These are library capabilities and links to dedicated guides; the overview does not define each task's role, eligibility, API version, or event outcome.
- The simplified integration sequence is user login, server validation and authentication session creation with required user roles, then client-side component initialization and user interaction. Setup steps are server authentication session, front-end library installation, initialization, and optional appearance customization. Some components need additional conditions in their own guides. A rendered component or session token is not evidence of approval, authorized payment, booked transfer, dispute resolution, or financing grant.
- General availability is described for users in countries and regions supported by Adyen for Platforms, while business-financing components have a narrower country/region list. This dated page does not establish current product eligibility for a particular user. It lists minimum browsers as Chrome 98, Safari 15.4, and Firefox 94 and recommends current versions for security.
- Cashout components and a Capital components update for UK sole-proprietor Merchant Cash Advances appear under a roadmap labeled early Q1 2027. That timing is a plan in this snapshot, not evidence that either feature is available. The existing Capital component in the current list is a separate inventory item.
- After-payment labels such as Transactions, Payouts, and Reports identify display and workflow interfaces. They do not alone prove payout initiation, booked funds, bank receipt, or report reconciliation; follow the respective child documentation and operation evidence.

## Detail locators

- `# Build your interface with UI component libraries`: platform UI/backend suitability and component purpose.
- `## Available components`: before/during/after inventory with child guides.
- `## Roadmap`: dated cashout and Capital update plans.
- `## How it works`: server role-bearing session token and client initialization sequence.
- `## Supported countries/regions` and `## Supported browsers`: general versus financing availability and browser minimums.

## Related

- [[adyen-platform-components]] — main component-suite concept and source route.
- [[adyen-platforms]] — parent Platforms context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/components-overview/2026-09-15|Adyen Platforms components overview (fetched 2026-09-15)]]
