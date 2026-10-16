---
title: "Adyen Platforms account-holder status"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/account-holder-status"
raw_files:
  - "adyen/docs/platforms/account-holder-status/2026-09-15.md"
tags: [adyen, platforms, account-holders, status, capabilities, splits]
---

## Overview

Adyen's Platforms account-holder status guide distinguishes an account holder's overall standing from the status of related balance accounts/payment instruments and the capabilities affected by a status reason. It describes platform- and Adyen-initiated changes and post-settlement split routing. These are documented state rules, not proof that a specific account holder was verified, a capability is enabled, a payment settled or a payout arrived.

## Key takeaways

- After onboarding and verification, the page says an account holder's status is set to **active**; the platform can update it to **suspended** or **closed** with Configuration API as the relationship changes. The status table calls active the initial status for account holders and balance accounts. **Suspended** temporarily disables the resource and blocks payouts; **closed** permanently disables it and all capabilities and is not editable. **Inactive** is listed only for newly created payment instruments. Do not treat active status alone as a complete verification or capability-approval record.
- Adyen may independently suspend or close an account holder for risk, fraud or terms reasons. Customer Area shows an Adyen status reason and `balancePlatform.accountHolder.updated` webhooks can deliver updates. **Only Adyen can reverse an Adyen-initiated suspension.** Adyen suspension propagates to related balance accounts; Adyen closure closes related balance accounts and payment instruments. Depending on reason, inheritance can extend to account holders sharing the same legal entity, so the exact status reason and resource scope matter.
- The reason tables are general guidelines, not fixed universal behavior: suspected fraud blocks payouts at account-holder level; suspected risk or terms can block payouts alone or payouts and pay-ins, potentially at legal-entity level. Closed fraud/risk/terms reasons disallow all capabilities, with inheritance varying by reason. Account-holder status, each capability's allowed/enabled state and verification status remain separate checks.
- The guide says payment processing is not **directly** affected by account-holder status because split instructions direct funds **after settlement**. For a suspended account holder with pay-ins still allowed, the split settles into that holder's balance account; if pay-ins are also blocked, or the holder is closed, the split is described as settling into the liable account holder's **Reserved Incorrect Splits Account**. This conditional routing is not assurance that any individual authorization, capture, settlement or payout succeeded.
- This page links to a separate Manage account holders guide for the actual suspend, reactivate and close procedure. It supplies no credential-role list or fixed time for status propagation; use the observed Customer Area reason, webhook and related capability states for an actual case.

## Detail locators

- Opening and `## Status definitions` — account-holder versus balance-account/payment-instrument objects; active, suspended, closed and payment-instrument-only inactive values; Configuration API navigation.
- `## Adyen-initiated status updates` / `### Status inheritance` — Customer Area reason/webhook route, Adyen-only reversal, related balance-account/payment-instrument and legal-entity effects.
- `### Status reasons` — case-qualified suspended/closed reason tables, payouts versus pay-ins and inheritance-level distinctions.
- `## Payment processing` — settlement-time split routing for suspended with/without blocked pay-ins and closed holders; distinct from payment authorization or bank receipt.

## Related

- Company: [[adyen]]
- Platforms concept: [[adyen-platforms]]
- Separate capability/verification state: [[source-adyen-docs-platforms-verification-overview-capabilities]]

## Raw Sources

- [[raw/adyen/docs/platforms/account-holder-status/2026-09-15|2026-09-15 Platforms account-holder status guide]]
