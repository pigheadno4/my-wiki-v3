---
title: "Adyen standalone terminal solution"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/standalone"
raw_files:
  - "adyen/docs/point-of-sale/standalone/2026-09-15.md"
tags: [adyen, point-of-sale, standalone-terminals, in-person-payments]
---

## Overview

Adyen's standalone solution initiates in-person payments directly on a payment terminal without a POS app or POS-system integration. The pinned 2026-09-15 webpage describes it as a route without development or integration work, and as a possible fallback when a POS app cannot communicate with integrated terminals. This source is a dated solution overview, not a current terminal, market, account-eligibility, security, or payment-result confirmation. [[adyen]] · [[adyen-standalone-terminals]]

## Key takeaways

- **Scope:** Staff initiate transactions on the standalone terminal itself. This differs from a merchant POS app sending Terminal API messages to an integrated terminal. The page directs implementation and operation questions to its linked build and use guides.
- **Fallback condition:** If a POS app cannot start a transaction on its integrated terminal, the page proposes a standalone terminal with cellular connectivity or offline payments enabled. The particular failure and the selected connectivity/offline path matter; the passage does not promise that any network outage will permit a payment or that an offline payment will later succeed.
- **Printer and listed models:** The page says card-scheme receipt compliance requires the ability to give a printed receipt, so standalone use is limited to terminals with a built-in printer. Its listed models are S1F2, S1F2L, V210, V240m Plus (Brazil), V400c Plus, and V400m. Check current support and country suitability before selection.
- **Supported functions in this snapshot:** The page lists card and NFC-wallet payments; QR-wallet, MKE and MOTO payment routes; tipping; in-progress cancellation; refunds; offline payments; accessibility activation; store-configured surcharge; day/shift totals; and receipt reprinting. Specific procedures and eligibility belong to the linked feature guides and terminal configuration. The overview itself is not proof that each listed method is enabled for a merchant or terminal.
- **Operational limits:** The page excludes shopper recognition and tax-free shopping from this solution and says merchants must manually reconcile POS transactions against sales and returns.

## Detail locators

- **Identity and setup model:** raw lines 15–21, `# Standalone solution`.
- **Fallback and prerequisites:** raw lines 23–25, `## Fallback`; follow the linked cellular-failover or offline-payment guide for their separate conditions.
- **Receipt constraint and models:** raw lines 27–35, `## Compliance and supported terminals`.
- **Feature list and operational exclusions:** raw lines 37–67, `## Supported features`. Linked feature procedures are navigation, not established behavior from this page alone.
- **Build and use routes:** raw lines 69–77, `## Next steps`.

## Related

- [[adyen-standalone-terminals]] — provider concept for the direct-terminal solution and its boundaries
- [[adyen-terminal-api]] — separate POS-app-to-terminal message integration
- [[source-adyen-docs-point-of-sale-what-we-support-solutions]] — broader in-person solution comparison

## Related raw API references

The next-step standalone build and use pages and linked cellular, offline, feature, and terminal-selection guides are routes from this overview; their content was not read for this entry.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/standalone/2026-09-15|Standalone solution, fetched 2026-09-15]]
