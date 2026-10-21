---
title: "Adyen Marketplaces account-holder status"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/account-holder-status"
raw_files:
  - "adyen/docs/marketplaces/account-holder-status/2026-09-15.md"
tags: [adyen, marketplaces, platforms, account-holders, status, splits]
---

## Overview

This 2026-09-15 Marketplace guide describes an account holder's overall standing, Adyen-initiated status inheritance, and how payment split destinations are handled after settlement. It belongs to the modern [[adyen-platforms]] route from [[adyen]], not the legacy Classic Platforms model. These documented state and routing rules do not prove a particular user's verification, capability grant, settlement or payout.

## Key takeaways

- The page says account holders become **active** after onboarding and verification, and the status table calls active the initial account-holder/balance-account status. The platform can use Configuration API to move an account holder to **suspended** or **closed**. Suspension temporarily disables the resource and blocks payouts; closed permanently disables it and all capabilities and is not editable. **Inactive** applies only to a newly created payment instrument. See raw lines 19–38.
- Adyen can independently suspend or close for suspected or confirmed risk, fraud or terms issues. Customer Area can show the Adyen status reason and `balancePlatform.accountHolder.updated` webhooks deliver updates. Only Adyen can reverse an Adyen-initiated suspension. Adyen suspension also suspends related balance accounts; Adyen closure closes related balance accounts and payment instruments. Depending on the reason, capability effects can extend to all account holders sharing the legal entity. See raw lines 40–58.
- The reason tables are **general guidelines** and explicitly allow case-specific differences. Suspected fraud lists payout blocks at account-holder level; suspected risk or terms can block payouts alone or both pay-ins and payouts and may inherit at legal-entity level. Closure disallows all capabilities, with inheritance varying by reason. Consult the actual reason and capability state for a particular case. See raw lines 60–85.
- Split instructions direct funds after settlement, so the guide says payment processing is not directly impacted by account-holder status. A split to a suspended holder settles to that holder's balance account if pay-ins are not also blocked. If the suspended holder's pay-in capability is blocked, or the holder is closed, the split instead settles to the liable account holder's **Reserved Incorrect Splits Account**. These are conditional routing descriptions, not proof of authorization, settlement or payout in a specific payment. See raw lines 87–93.

## Detail locators

- Account-holder, balance-account and payment-instrument statuses: raw lines 19–38.
- Adyen-initiated update, reason notification and status inheritance: raw lines 40–58.
- Reason/capability/inheritance guideline tables: raw lines 60–85.
- Post-settlement split routing for suspended versus closed holders: raw lines 87–93.

## Related

- [[adyen]] — provider profile.
- [[adyen-platforms]] — modern Platforms and Marketplaces route.
- [[source-adyen-docs-marketplaces-manage-account-holders]] — separate suspension, reactivation and closure procedure.
- [[source-adyen-docs-platforms-account-holder-status]] — distinct Platforms URL with closely related status guidance.
- [[adyen-classic-platforms]] — legacy Classic Platforms resource model.

## Raw Sources

- [[raw/adyen/docs/marketplaces/account-holder-status/2026-09-15|Account holder status — pinned 2026-09-15 raw snapshot]]
