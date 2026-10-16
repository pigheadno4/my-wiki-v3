---
title: "Adyen platform account-holder risk management"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/manage-account-holder-risk"
raw_files:
  - "adyen/docs/platforms/manage-account-holder-risk/2026-09-15.md"
tags: [adyen, platforms, score, account-holder-risk, payouts]
---

## Overview

This Adyen for Platforms **Score** guide describes reviewing account-holder risk cases and configuring rules or actions in Customer Area after signals of possible fraud or other unusual activity. The snapshot was captured 2026-09-15 despite 2020-12-22 last-modified metadata; it also describes an October 2026 planned Score enablement, so availability must be checked for the actual platform. A risk score, flag, review label or example webhook is not proof of fraud, KYC verification, capability approval, payout execution or funds receipt.

## Key takeaways

- **Roles and availability:** `Merchant Marketplace Risk` is listed for reviewing cases and direct actions; `Merchant Marketplace Risk Admin` for risk rules and automated actions. The page says Score is default for platforms created after October 2024 and describes an October 31, 2026 enablement for all Adyen for Platforms merchants. That dated future rollout statement does not prove a given platform's current access.
- **Rules and automatic effects:** a rule can affect risk score at a selected level or trigger `None`, `Bump KYC tier`, or `Disable payouts`. Its automated-actions log helps operators review what happened and whether to unblock or retain a block. Disabling payouts is an operational control; neither rule configuration nor a log entry proves a payout occurred or that an account's verification status changed in a specified way.
- **Case review and direct effects:** flagged signals create open cases; the dashboard shows open/reviewed/suspicious queues, linked users and risk context including processed volume and overall score. A reviewer may mark a case Reviewed or Suspicious, block/re-enable payouts, suspend an account, add confirmed-fraud KYC values to a high-risk list, or trust linked accounts. These are different actions; moving a case queue is not the same as changing payout capability or establishing fraud.
- **False positives and permanent exclusions:** an irrelevant signal can be muted for a week, month, year or indefinitely. A KYC value can be excluded from linked-account identity matching when irrelevant, but the guide says this exclusion **cannot be undone and is permanent**. High-risk lists may hold email, phone, personal data, bank account, address or tax ID attributes; the direct-action text limits adding high-risk KYC values to **confirmed fraudulent users**.
- **Webhook setup and identity:** `balancePlatform.score.triggered` is optional and needs a server receiving/accepting webhooks, Configuration webhook subscription and Adyen-contact enablement. In the example, `data.id` identifies a **score calculation/recalculation** and changes each time; it is not the account-holder ID shown separately in `data.accountHolder.id`. The example test payload, score and `automatedActions` are illustrative, not live action proof.

## Detail locators

- Raw lines 15–29: Score purpose, two Customer Area roles, optional risk-signal webhooks and dated rollout language.
- Raw lines 31–62: rule creation, risk-score impact, `Bump KYC tier`/`Disable payouts` choices and automated action log.
- Raw lines 64–99: case queues, dashboard content and direct actions with confirmed-fraud qualifier.
- Raw lines 100–126: signal muting and permanent exclusion of KYC values from linked identities.
- Raw lines 128–166: high-risk-list attributes/manual or CSV additions and conditional webhook enablement.
- Raw lines 168–204: sample `balancePlatform.score.triggered` payload and score-calculation versus account-holder identifiers.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform account-holder, verification and payout boundaries.
- [[adyen-risk-management]] — broader Adyen risk-management concepts, distinct from this platform Score case workflow.

## Raw Sources

- [[raw/adyen/docs/platforms/manage-account-holder-risk/2026-09-15|Account-holder risk management, fetched 2026-09-15]]
