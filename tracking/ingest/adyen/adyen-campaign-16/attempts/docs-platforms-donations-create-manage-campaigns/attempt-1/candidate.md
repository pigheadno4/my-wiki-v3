---
title: "Create and manage Adyen Giving campaigns for platform account holders"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/donations/create-manage-campaigns"
raw_files:
  - "adyen/docs/platforms/donations/create-manage-campaigns/2026-09-15.md"
tags: [adyen, platforms, giving, donations, campaigns]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes how a platform sets up and manages Giving campaigns for its account holders in Customer Area or through the Management API, and how it may build its own UI for user self-service. A campaign links participating account holders and their channel-specific stores to an onboarded nonprofit cause, for online payments, in-person payments, or both. It covers campaign configuration and lifecycle; the linked online and in-person guides cover shopper payment and donation handling. See [[adyen-giving]] and [[adyen-platforms]]. A created or active campaign does not prove that any shopper donated or that funds settled.

## Key takeaways

- Scope is Adyen for Platforms with a platform model. The documented online route is API-only on Checkout API v67 or later; the in-person route is Terminal API or Standalone with terminal software v1.109 or later, with some terminals/features requiring v1.110 or later. Management API campaign requests need the “Management API - Campaign Management read and write” API-credential role; Customer Area viewing uses “Donation campaigns viewer” and creating, starting, editing or ending uses “Donation campaigns manager.” An onboarded or pre-approved nonprofit, supported region/currency/payment method and applicable terminal model are prerequisites. The campaign is capped at 400 account holders; a store can be in only one active campaign at a time.
- The platform selects an available nonprofit and cause for the account holders, then configures account-holder IDs and stores per sales channel. API creation uses the selected cause ID, campaign name and platform-required account-holder IDs; the channel objects identify eligible stores and donation type. Stores must match the channel and at least one included account holder. The pinned field tables specify required/conditional settings and minor-unit fixed amounts. Creation returns a campaign ID and initially `inactive` status; it does not activate the campaign.
- Online campaigns can offer fixed amounts or round-up; pre-checkout donation presentation requires the API-only integration and is implemented in the online payment flow, not as a campaign setting. In-person campaigns can offer fixed amounts, round-up or a combination, and choose one-step or two-step card presentation. Both in-person choices remain separate payment and donation transactions. The terminal does not prompt after gift-card payment, and a donation cannot complete offline even when the underlying payment proceeds offline.
- Management API listing is per account holder and may filter `inactive`, `active` or `ended` campaigns. Editing is allowed for inactive or active campaigns; adding an account holder requires compatibility with the nonprofit cause by legal-entity country and industry, and PATCH arrays must contain all entries to retain. Online edits take effect right away; in-person terminals receive them on their next maintenance call, usually overnight. Status cannot be patched directly.
- Activating `inactive` to `active` and ending `active` to `ended` are one-way transitions: the guide does not allow reverting active to inactive or reactivating an ended campaign. Only an inactive, never-started campaign may be permanently deleted. A successful status response reports campaign state, not donation or payment outcome; the separate payment/donation guides and their outcome evidence are required for those claims.

## Detail locators

- Scope, integration/role/nonprofit prerequisites, eligibility, 400-account-holder and one-active-campaign-per-store limits: pinned raw lines 15–42.
- Online and in-person interaction flows, terminal and offline behavior, and donation-type choices: pinned raw lines 44–106.
- Customer Area account-holder, nonprofit, channel, store, currency and initial-status sequence: pinned raw lines 114–161.
- API nonprofit/cause lookup and creation schema, field requirements, minor-unit amounts, test example and inactive result: pinned raw lines 163–400; use field tables at lines 270–295, not the sample response as a universal guarantee.
- Customer Area lifecycle and terminal edit propagation: pinned raw lines 402–419; account-holder list/status lookup: lines 430–452.
- Compatibility precheck, PATCH array replacement and status restriction: pinned raw lines 572–586; status transitions, repeat-status response and 422 failures: lines 666–691; irreversible deletion restriction: lines 693–711.

## Related

- [[adyen]]
- [[adyen-giving]]
- [[adyen-platforms]]
- [[adyen-index]]

## Raw Sources

- [[raw/adyen/docs/platforms/donations/create-manage-campaigns/2026-09-15|Platform Giving campaign management snapshot (2026-09-15)]]
