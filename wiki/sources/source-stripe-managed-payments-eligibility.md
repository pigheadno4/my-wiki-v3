---
title: "Managed Payments Eligibility"
type: source
date_ingested: 2026-04-23
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/managed-payments/eligibility"
raw_files:
  - "stripe-payments-managed-payments-eligibility-2026-11-07.md"
  - "stripe-managed-payments-eligibility-2025.md"
tags: [stripe, managed-payments, merchant-of-record, tax-codes, eligibility, digital-goods, buyer-countries]
---

## Summary

Stripe reviews direct integrations for Managed Payments eligibility based on factors including business type and geography. The November 7, 2026 capture lists 37 merchant business locations and 76 eligible Product tax codes. Each sale through a Checkout Session or Payment Link must meet the product, distribution, and tax-code requirements. Customer coverage and ongoing account requirements apply separately.

## Account Eligibility

Use a direct integration with a business based in a supported location. Connect platforms, Express accounts, and accounts controlled by a platform are excluded. A listed business location or Product tax code alone does not establish Stripe approval.

### Supported business locations

The November 7, 2026 eligibility capture lists 37 entries (raw lines 22–68).

- **North America**: CA, US
- **Europe**: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK
- **Asia Pacific**: AU, HK, JP, SG

The April 23, 2026 eligibility capture lists 38 entries, including Gibraltar (GI, raw lines 21–69). The November list otherwise matches April's. The [[source-stripe-managed-payments-changelog]] separately reports 39 countries, including Australia, at the April 22, 2026 general-availability milestone. The November [[source-stripe-managed-payments-tax-compliance]] capture still includes Gibraltar for cross-border sales to customers there. The eligibility snapshots give no effective date for the listing change or account-specific treatment for Gibraltar.

## Product Eligibility

For each Product sold through a Checkout Session or Payment Link, assign an eligible tax code on the Product in the Dashboard or through the API. Sell directly to customers, hold the necessary distribution rights and licences, and provide a fully automated digital product. Live human intervention such as one-to-one coaching disqualifies the service. If Stripe determines that a product is ineligible, stop using Managed Payments for that product and take responsibility for its indirect tax liability. The guide points to Stripe Tax as a separate option when a product appears ineligible.

Eligible categories include software (IaaS, PaaS, SaaS, and downloads), video games, digital media, self-study and on-demand courses, and electronically supplied business and web services. Physical goods, professional services, and live in-person events are excluded. Some Digital Audio Visual Works rows cover live-event content delivered as digital downloads, streams, or bundles (November raw lines 153–155 and 175–177, April raw lines 149–151 and 172–174). Check the exact code definition, direct sale, distribution rights, and automated delivery together. The general electronically supplied services description for `txcd_10000000` mentions minimal human involvement (line 108 in both captures). The fully automated Managed Payments requirement still applies.

### Exact eligible tax codes

Use the enumerated dated tables for code lookup: November 7 raw lines 104–183 (76 rows) and April 23 raw lines 104–180 (73 rows). The SaaS rows, for example, are `txcd_10103000`, `txcd_10103001`, `txcd_10103100`, and `txcd_10103101`. The personal and business distinctions on applicable codes matter for US sales.

November includes these four AIaaS rows (raw lines 117–120), which the November [[source-stripe-managed-payments-changelog]] capture dates to June 2, 2026.

| Tax code | AIaaS delivery and use |
| --- | --- |
| `txcd_10105001` | Cloud-based, personal use |
| `txcd_10105002` | Cloud-based, business use |
| `txcd_10105003` | Cloud-based and downloaded, personal use |
| `txcd_10105004` | Cloud-based and downloaded, business use |

April includes Website Advertising `txcd_10701000` (raw line 166) and November omits it. Website Hosting `txcd_10701100` remains in the November table. The April changelog capture listed Website Advertising in its September 22, 2025 one-time and in-app payment entry. The November changelog capture omits it from that entry. These omissions give no effective removal date, replacement code, or treatment of existing products or invoices.

November explicitly excludes data brokering from the four following information-service code definitions (raw lines 171–174). It also drops “of any kind” from the electronically delivered definitions.

| Tax code | Information service |
| --- | --- |
| `txcd_10701400` | Via website, business use |
| `txcd_10701401` | Via website, personal use |
| `txcd_10701410` | Electronically delivered, business use |
| `txcd_10701411` | Electronically delivered, personal use |

## Customer Coverage

Both captures describe coverage in more than 195 customer countries and territories. The nine listed restrictions are Ascension Island, China, Cuba, Iran, Kosovo, North Korea, Russia, Syria, and Tristan da Cunha. This customer coverage is distinct from merchant business locations and product eligibility.

## Ongoing Performance Requirements

Maintain a low historical dispute rate and have no prior risk issues. Stripe can issue refunds within 60 days of purchase in certain cases, including to help reduce chargebacks. Stripe applies regional cooling-off periods and other applicable consumer protection requirements.

## Related Pages

- [[stripe]] — Stripe and its Managed Payments documentation
- [[stripe-managed-payments]] — account and product eligibility, integrations, and operating requirements
- [[source-stripe-managed-payments-overview]] — integration paths and feature comparison
- [[source-stripe-managed-payments-changelog]] — dated availability and eligible-code milestones
- [[source-stripe-managed-payments-tax-compliance]] — customer tax coverage and merchant responsibilities

## Raw Sources

- [[raw/stripe-payments-managed-payments-eligibility-2026-11-07]] — full eligibility capture, November 7, 2026
- [[raw/stripe-managed-payments-eligibility-2025]] — full eligibility capture, April 23, 2026
