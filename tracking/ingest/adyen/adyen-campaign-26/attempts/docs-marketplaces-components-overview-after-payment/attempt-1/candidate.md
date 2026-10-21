---
title: "Adyen Marketplace after-payment components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/after-payment"
raw_files:
  - "adyen/docs/marketplaces/components-overview/after-payment/2026-09-15.md"
tags: [adyen, marketplaces, platforms, ui-components, after-payment]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] page is a navigation hub for post-payment dashboards in [[adyen-platform-components]]. It presents ways users could view transactions and balances, follow payouts to bank accounts, and access business-financing UI under the modern [[adyen-platforms]] model (raw lines 15–21). The brief descriptions are product routes, not proof a marketplace has deployed or enabled them.

## Key takeaways

- The page links six child guides: **Transactions** for account/date filtering, exports and fees/IDs/refund detail; **Payouts** for automatic-payout reports, captured funds, adjustments, net amounts and remaining balances; and **Reports** for filtering/downloading automatically generated daily reports (raw lines 23–39).
- It also links **Disputes** for balance-account views and defense/acceptance with documents; **Pay by Link** for store-branded links, expiry, history and sharing; and **Capital** for financing applications, qualified-grant and terms views, and repayment progress (raw lines 41–57). These are summary claims; each child guide controls its own product, role, region, version, data scope and action restrictions.
- The parent Component libraries route is at raw lines 59–61. This hub does not specify session/authentication setup or establish that a particular user is eligible to perform a financial or dispute action.

## Detail locators

- Hub purpose and marketplace balance/payout framing: raw lines 15–21.
- Transactions, Payouts, Reports child navigation: raw lines 23–39.
- Disputes, Pay by Link, Capital child navigation: raw lines 41–57.

## Evidence boundary

A dashboard view, report download, payout amount, payment-link state, dispute control or Capital progress display is not independent evidence of payment capture, balance booking, beneficiary bank receipt, dispute outcome, financing grant or repayment. Consult the relevant child guide and actual account/event evidence before making those claims.

## Related

- [[adyen-platform-components]] — main component concept.
- [[adyen-platforms]] — current Marketplace/Platforms context.
- [[source-adyen-docs-marketplaces-components-overview-after-payment-disputes-component]] — dispute child guide.
- [[source-adyen-docs-marketplaces-components-overview-after-payment-capital-component]] — financing child guide.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/after-payment/2026-09-15|Pinned Marketplace after-payment component hub, captured 2026-09-15]]
