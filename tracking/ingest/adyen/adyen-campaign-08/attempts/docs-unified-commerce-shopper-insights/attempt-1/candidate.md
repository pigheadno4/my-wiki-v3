---
title: "Adyen Unified Commerce shopper insights overview"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/shopper-insights"
raw_files:
  - "adyen/docs/unified-commerce/shopper-insights/2026-09-15.md"
tags: [adyen, unified-commerce, shopper-insights, payments-data, privacy]
---

## Overview

Adyen's Shopper Insights overview, last modified 2021-07-06 and captured 2026-09-15, presents using identifiers in payment data to analyze shopper trends across sales channels and regions. It describes a merchant collecting payment data from webhooks and combining it with the merchant's database for its own analysis. This is a [[adyen-unified-commerce]] data-use proposition, not proof that Adyen automatically creates a verified person-level profile, that a specific identifier links every channel, or that a payment succeeded.

## Key takeaways

- **Cross-channel analysis is framed as a use case.** The page says Adyen processes payment data from sales channels on one platform and describes connected data across channels and regions, one common database, merchant analysis using webhook data, and resulting business decisions such as store placement or marketing campaigns. It does not give an implementation contract or a completed merchant warehouse.
- **Privacy comes before storing data.** The page tells merchants to consider privacy regulations in operating countries/regions, consult legal counsel or an accredited third party, and ask customers for explicit permission to store their data while explaining its use. It mentions website terms or terminal interaction as possible permission touchpoints; neither route alone is shown to satisfy a merchant's legal duties.
- **Adyen-stored data has a separate deletion route.** If a customer requests removal, the page points to Adyen's Data Protection API for customer-related data stored with Adyen and cites GDPR right to erasure. This does not itself remove merchant-held database, warehouse or webhook copies; those handling steps are outside this overview.
- The linked Collect data guide is the place to verify concrete identifier fields and collection mechanics. This overview does not define card alias, PAR, token, shopper reference or contact-detail matching semantics, and does not establish current region, scheme, merchant-account or product eligibility.

## Detail locators

- Raw `# Shopper insights` (lines 15–35): provider proposition, connected channels/regions, common database and webhook-plus-merchant-database analysis examples.
- Raw `## Data privacy` (lines 37–44): pre-storage privacy review, explicit customer permission and stated-purpose notice, possible interaction surfaces, and Adyen Data Protection API deletion route.
- Raw `## Next steps` (lines 46–50): Collect data child guide for identifier details; navigation only until that guide is read.

## Related

- [[adyen-unified-commerce]] — cross-channel merchant proposition and child routes.
- [[source-adyen-docs-unified-commerce-collect-data]] — separately reviewed identifier collection mechanisms and field scope.
- [[adyen-pos-shopper-engagement]] — terminal interaction route, not consent proof by itself.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/shopper-insights/2026-09-15|Shopper insights, fetched 2026-09-15]]
