---
title: "Adyen for Platforms Giving donation campaigns"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/donations"
raw_files:
  - "adyen/docs/platforms/donations/2026-09-15.md"
tags: [adyen, platforms, giving, donations, campaigns]
---

## Overview

This 2026-09-15 Adyen for Platforms Giving overview describes how a platform can offer its users online or point-of-sale donation campaigns for their shoppers. A shopper's donation uses the purchase payment method but is a separate transaction; Adyen says it settles the full donation directly to the nonprofit's bank account and covers its fees. The page explains account-holder campaigns, eligibility and terminal support, then routes to separate setup and channel implementation guides. It does not document an actual donation, settlement or bank receipt. See [[adyen]], [[adyen-platforms]] and [[adyen-giving]].

## Key takeaways

- **Actors and campaign scope:** The platform can manage campaigns for its users in Customer Area or use Management API calls to build user self-service. In this Platforms integration, campaigns are created for account holders. Creation needs a nonprofit, participating account holders, online and/or in-person channels, at least one store for each channel, and donation options such as fixed amounts or round-up. The page caps a campaign set up on behalf of users at 400 participating account holders, and a store can belong to only one active campaign at a time. Account holder, store, shopper and nonprofit have distinct roles; the donation is separate from the purchase.
- **Lifecycle and timing:** A new campaign is inactive; starting it is a separate action. Active campaigns can be edited, but ended campaigns cannot restart and campaigns have no expiry date. Online edits/status changes take effect right away, while in-person terminals take them on their next maintenance call, usually overnight. Do not equate a saved campaign with an active shopper prompt.
- **Eligibility:** Shoppers are asked only where the shopper's region, currency and payment method support Giving. The available pre-approved nonprofit list depends on an account holder's legal-entity country and industry; unapproved nonprofits need onboarding. Supported currencies also vary by nonprofit, and the page's dated method table distinguishes online from in-person one-step and two-step flows. Check the current combination rather than treating the tables as account-specific enablement. The captured region note restricts Singapore fundraising to local nonprofits.
- **Terminal versions and evidence:** The table lists Giving-capable models and feature combinations. It requires terminal software 1.109 or later generally, with some models/features needing 1.110 or later; combined round-up plus fixed amounts in a one-step flow needs 1.124 or later, and the SFO1 one-step row says 1.125 or later. These are dated documented support conditions, not proof that a device is updated or a campaign is running. Follow the separate online or in-person implementation guides and donation insights/reporting route for detailed processing and outcome checks.

## Detail locators

- Separate donation, full nonprofit settlement claim and platform/user management routes: pinned raw lines 15-31.
- Campaign inputs, 400-account-holder maximum, store exclusivity and irreversible end: pinned raw lines 33-47.
- Nonprofit compatibility/onboarding, supported regions/currencies and Singapore note: pinned raw lines 49-76.
- Payment-method/channel support table: pinned raw lines 78-100.
- Terminal model/feature/version matrix and next-step routes: pinned raw lines 102-142.

## Related

- [[adyen-giving]] — main Giving concept and reciprocal source route.
- [[adyen-platforms]] — platform/user context.
- [[source-adyen-docs-platforms-donations-create-manage-campaigns]] — campaign setup and lifecycle detail.
- [[source-adyen-docs-platforms-online-payments-donations-online]] — separate online implementation route.
- [[source-adyen-docs-point-of-sale-donate]] — related POS Giving route.

## Raw Sources

- [[raw/adyen/docs/platforms/donations/2026-09-15|Adyen Giving donation campaigns, captured 2026-09-15]]
