---
title: "Adyen Mirakl connector overview"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/mirakl"
raw_files:
  - "adyen/docs/plugins/mirakl/2026-09-15.md"
tags: [adyen, mirakl, marketplace, seller-onboarding, payouts]
---

## Overview

This 2019-08-15-last-modified, 2026-09-15-captured overview describes Adyen's **Mirakl Marketplace connector** with Adyen for Platforms. It frames seller onboarding/KYC, account-data synchronization, commission and subscription-fee collection, balance reporting, and domestic seller payouts. It is a product and integration route, not a record of merchant eligibility, a live deployment or completed money movement. See [[adyen-mirakl]] and [[adyen]].

> [!warning] Source scope and commission phase
> This older overview broadly describes splitting pay-in funds to collect marketplace commission. The separately reviewed Seller payouts guide says the connector transfers commission and subscription fees to the liable balance account after a successful seller payout, so `type: Commission` is not required in that pay-in split request for this connector flow. Preserve the distinct source and processing-phase scopes; do not infer a universal commission-splitting rule from the overview. [[source-adyen-docs-plugins-mirakl-payouts]]

## Key takeaways

- **Connector scope versus pay-in:** The overview says hosted onboarding collects seller information for Adyen verification, then the connector can collect funds from sellers and support domestic payouts. It explicitly says the connector **does not manage pay-in**: the marketplace must implement payment, refund and chargeback flows separately. Do not infer those flows from the feature list or child links.
- **Required payment/split architecture:** It requires an ecommerce system that processes payments on behalf of sellers and splits funds among multiple balance accounts, sending sellers' portions to their accounts while collecting marketplace commission. The page does not identify the legal merchant of record, seller contracting party, payee for a particular purchase, or precise settlement obligation; those depend on the actual platform arrangement.
- **Capabilities are qualified:** Feature bullets mention Adyen Hosted Onboarding/KYC, Transfers API balance control for commissions and Mirakl subscription fees, domestic seller payouts, synchronized account data and Balance Platform reporting. The page does not give supported countries, account eligibility, transfer/payout timing, fee calculation, report schema or proof that KYC passed or a payout reached a bank.
- **Preparation and exceptions:** Its get-started route calls for an Adyen for Platforms test account and API credentials while live credentials are pending, then connector setup, seller onboarding, separately implemented payment flows, payouts/commissions, reconciliation and testing. Contact the Adyen point of contact if Mirakl's “Issue invoices even if payable balance is negative” feature is enabled or when migrating from another connector. The linked child guides contain operational details that this overview does not establish.

## Detail locators

- Lines 15–23: connector identity and Adyen for Platforms/KYC/payout framing.
- `## Features`, lines 25–32: hosted onboarding, Transfers API, domestic payouts, account synchronization and reporting claims.
- `## How it works`, lines 34–40: onboarding sequence and categorical pay-in exclusion.
- `## Requirements`, lines 42–49: ecommerce payment/split prerequisite and Adyen-contact conditions.
- `## Get started`, lines 51–68: test-account/API-credential preparation and child-guide navigation.

## Related

- [[adyen-mirakl]] — Mirakl connector ownership and pay-in boundary.
- [[adyen]] — provider profile.
- [[adyen-payouts]] — separate provider payout concept; this overview concerns marketplace seller balances rather than legacy Online payouts.
- [[source-adyen-docs-plugins-mirakl-set-up-the-connector]] — connector setup route.
- [[source-adyen-docs-plugins-mirakl-set-up-payment-flows]] — separately implemented pay-in route.
- [[source-adyen-docs-plugins-mirakl-payouts]] — seller payout and commission route.

## Raw Sources

- [[raw/adyen/docs/plugins/mirakl/2026-09-15|Mirakl connector overview, captured 2026-09-15]]
