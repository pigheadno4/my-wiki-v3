---
title: "Adyen Marketplace balance-account top-ups"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/top-up-balance-account"
raw_files:
  - "adyen/docs/marketplaces/top-up-balance-account/2026-09-15.md"
tags: [adyen, marketplaces, platforms, top-ups, balance-accounts]
---

## Overview

This 2026-09-15 Marketplace orientation page defines a **balance-account top-up** as an incoming transfer from an **external source** that increases a user's balance account; a marketplace can also top up its liable balance account. This differs from internal movement between existing balance accounts. It routes to scheduled, on-demand and webhook guides, which own the funding method, eligibility and outcome details. [[adyen]] [[adyen-platforms]]

## Key takeaways

- User-account funds usually come from customer payments; top-up funding is a separate external inflow. The page suggests covering negative balances after refunds/chargebacks or maintaining funds for a planned transfer as use cases. They do not mean a particular top-up or later transfer has completed (raw lines 19–28).
- **Scheduled** top-ups use a configured schedule based on timing and amount. **On-demand** top-ups are manually initiated as needed, with or without a scheduled arrangement. Once initiated, the page says Adyen triggers an incoming external transfer to pull from the specified source; initiation is distinct from booked credit and available balance (raw lines 30–37).
- The page title/description mentions a pull sweep and verified transfer instrument, but the body covers both scheduled and on-demand paths without detailing their respective source or method rules. Follow the child guides for verified-instrument, role, region, capability, fee, retry and status conditions; do not generalize the scheduled direct-debit description to every on-demand top-up (raw lines 6–7, 17, 30–51).
- The webhook next step is the route for top-up status updates. This orientation supplies no evidence that an external debit cleared, the balance account was credited, negative balance was cured, or an outgoing payout reached a bank (raw lines 37–51).

## Detail locators

- Top-up definition, user and liable account scope, suggested uses: raw lines 17–28.
- Scheduled/on-demand distinction, initiation language and child guide/webhook routes: lines 30–51.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern Marketplace/platform context.
- [[source-adyen-docs-marketplaces-top-up-balance-account-scheduled-top-ups]] — scheduled pull-sweep conditions.
- [[source-adyen-docs-marketplaces-top-up-balance-account-on-demand-top-ups]] — on-demand payment funding.
- [[source-adyen-docs-marketplaces-top-up-balance-account-top-up-webhooks]] — credit and fee event evidence.
- [[source-adyen-docs-platforms-top-up-balance-account]] — separate Platforms-path overview.

## Raw Sources

- [[raw/adyen/docs/marketplaces/top-up-balance-account/2026-09-15|Marketplace balance-account top-ups — 2026-09-15 snapshot]]
