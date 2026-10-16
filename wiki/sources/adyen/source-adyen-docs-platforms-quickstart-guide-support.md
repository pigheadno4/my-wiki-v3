---
title: "Adyen for Platforms support quickstart"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/quickstart-guide/support"
raw_files:
  - "adyen/docs/platforms/quickstart-guide/support/2026-09-15.md"
tags: [adyen, platforms, support, onboarding, payouts, escalation]
---

## Overview

This Adyen for Platforms quickstart assigns **user-facing support** to the platform business. Adyen Support serves the business, not its platform users directly. The page suggests support categories, an illustrative tiered team, Customer Area tickets, urgent account-manager escalation, and KYC/payout troubleshooting routes. It does not promise a response time, resolution, verified capability, payment result or payout delivery.

## Key takeaways

- Platform support should handle user questions about onboarding/KYC, finance/payouts and technical integration issues. The SaaS first-/second-/third-line structure is explicitly an **example**: platform first line answers general questions and does not contact Adyen; a specialized second line may contact Adyen; a payment-issue third line handles Adyen escalations. It is not a required organizational chart or transfer of the user relationship to Adyen.
- Adyen suggests proactive communications from account-holder status/capability webhooks and reports. A webhook can inform users that a status or capability changed; a report can help explain fund status and payout amounts. Neither communication is independent proof that verification succeeded, a capability is usable, or a bank received funds. Notification center messages are limited by the Customer Area user's merchant-account access; system messages and service status are incident-information routes.
- Teams submit ordinary support tickets through Customer Area **? > Submit a ticket**, choose a category and provide required subject and issue description; merchant account, copy recipient and attachments are listed fields/options. The page asks for product and detailed context; its template includes TEST/LIVE environment and relevant Transfer, Account Holder or Balance Account IDs in text form. It does not state which Customer Area role grants ticket access, nor a ticket response SLA.
- For urgent problems the page names the **Adyen Account manager** as primary escalation path, with examples of widespread missed payouts, critical transaction/payout flow outage or inaccessible hosted onboarding. A ticket, account-manager contact, notification or service-status page is a route for investigation, not a resolution guarantee.
- KYC FAQ says a `Pending` verification status means review and gives a **typical** 24–48-hour timeframe; contact Adyen Support for clarification after 48 hours, without interpreting that as a guaranteed deadline. Suspended or closed account holders are expected to have payout capabilities blocked; the FAQ advises checking status reasons, verification webhooks/errors and KYC documents before escalation. Its suggestion that a platform may patch a non-Adyen-suspended account holder active does not establish verification approval or a successful payout.
- Finance FAQ distinguishes booked payments from value-date funding when explaining payout amount differences, points to Balance Platform Accounting Report for expected amount, and describes sweeps, on-demand routes and payout-failure reason codes. These are support investigation routes and do not establish a particular payout, bank receipt or universal payout timing.

## Detail locators

- Opening and `## Support Categories` — platform versus Adyen support responsibility and user question categories.
- `## Proactive Support` / `## Tiered Support` — webhook/report communication suggestions and illustrative first-/second-/third-line structure.
- `## Contact Adyen Support` / `### Email Template` — Customer Area ticket steps, required fields and product/environment/ID context.
- `## Adyen Communication Channels` / `## Escalation Paths` — notification access, system/service-status routes and urgent account-manager escalation examples.
- `## KYC & Onboarding` FAQ — pending timing, payout capability blocks, status/webhook/document diagnosis and escalation boundary.
- `## Finance & Payouts` FAQ — value-date versus booking explanation, report/sweep/on-demand navigation and payout failure categories.

## Related

- Company: [[adyen]]
- Platforms concept: [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/platforms/quickstart-guide/support/2026-09-15|2026-09-15 Platforms support quickstart]]
