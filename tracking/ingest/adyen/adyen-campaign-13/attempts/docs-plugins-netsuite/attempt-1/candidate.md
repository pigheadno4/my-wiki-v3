---
title: "NetSuite | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/netsuite"
raw_files:
  - "adyen/docs/plugins/netsuite/2026-09-15.md"
tags: [adyen, plugins, netsuite, payments, reconciliation]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot is the landing guide for Adyen's NetSuite payments bundle across online, in-app and in-person payments, plus a separate reconciliation bundle. It lists capabilities and routes to setup guides; it does not state a bundle release version, current compatibility matrix, merchant enablement, or a completed payment or bank reconciliation result. [[adyen-plugins]]

## Key takeaways

- Listed payment features include website/mobile credit cards collected through the Card Component, dynamic 3DS2, local payment methods, terminal POS, tokenization, Revenue Protect and Adyen-hosted Pay by Link. These are capability descriptions; the page does not establish that every method or feature is enabled for every merchant, NetSuite configuration, channel or market. Its Card Component statement says reduced PCI DSS requirements, not that PCI duties disappear.
- The reconciliation bundle is described as pulling an Adyen Settlement Detail Report, matching NetSuite transactions using PSP reference and record type, and creating deposits to NetSuite accounts. The page calls this fully automated bank reconciliation, but gives no mapping/error/exception rules or transaction-level verification. A NetSuite deposit record is distinct from a receiving-bank credit.
- Preparation routes through Adyen's get-started guide and test-account creation. After creating the test account, the page instructs enabling Chargeback Management in the NetSuite environment; integration can start on test while a live-account application awaits approval. It then links setup for the test Customer Area, NetSuite Customer Center, Pay by Link, POS and tokenization. The linked guides own credentials, roles, deployment and environment-specific steps.
- The glossary distinguishes a **sales order** commitment (no payment request until goods are shipped or services delivered, then invoice or cash sale), an **invoice** payment request after fulfillment, a **cash sale** for immediate payment at delivery, and a **customer deposit** for advance payment. These NetSuite record descriptions must not be treated as evidence that Adyen authorized, captured, settled or paid out a specific transaction.

## Detail locators

- **Bundle positioning and payment features:** raw lines 15–33.
- **Reconciliation bundle and NetSuite deposit record:** raw lines 35–37.
- **Test/live preparation and linked setup routes:** raw lines 39–54, 74–86.
- **Sales-order, invoice, cash-sale and customer-deposit glossary:** raw lines 56–63.

## Related

- [[adyen]]
- [[adyen-plugins]]
- [[adyen-reporting]] — separate reporting and settlement-detail evidence

## Raw Sources

- [[raw/adyen/docs/plugins/netsuite/2026-09-15|Adyen NetSuite bundle overview — collected 2026-09-15]]
