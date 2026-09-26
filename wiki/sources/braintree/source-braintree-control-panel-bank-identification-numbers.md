---
title: "Braintree Control Panel Bank Identification Numbers"
type: source
date_ingested: 2026-09-23
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/transactions/bank-identification-numbers"
raw_files:
  - "braintree/articles/control-panel/transactions/bank-identification-numbers-2026-09-16.md"
tags: [braintree, control-panel, transactions, bin, iin, pci-dss]
---

## Overview

This collected Braintree article explains how bank identification numbers (BINs), also called issuer identification numbers (IINs), can be used for transaction analysis and found through Control Panel transaction search, CSV exports, or a linked transaction-search API route. It also records Braintree's treatment of the 8-digit issuer-BIN expansion and payment-card-data handling; these dated statements are evidence from the collected page, not confirmation of current feature support or PCI requirements.

## Key takeaways

- The article defines a BIN/IIN as the first six digits of a debit or credit card and presents BIN lookup as a way to investigate purchase and decline patterns, including customer location and card-type trends.
- For one transaction, the documented Control Panel route is Transaction Search, where the BIN appears as the first six digits in the Payment Information column. For comparisons across transactions, the article directs readers to download the search results as CSV and use its First Six of Credit Card column.
- The article also links transaction-ID search through the API and says its response includes the BIN as a parameter. It does not name an SDK, method, response-object path, or current availability on this page, so those details remain with the linked API authority.
- Although the page discusses the April 2022 move to 8-digit issuer BINs and says Braintree processes them, its BIN data-availability section says the existing APIs, GraphQL integrations, console search, and BIN reports continue to expose six-digit BINs. Do not infer that these surfaces return the full 8-digit issuer BIN.
- The page says viewing and storing BINs does not compromise or change PCI compliance requirements. Its 8-digit-expansion section separately cites PCI DSS v3.2.1 requirement 3.3 for displayed-PAN masking and warns that merchants relying only on truncation for data-at-rest protection need another acceptable protection method.

## Detail locators

- BIN/IIN definition and described business-analysis uses: `# Bank Identification Numbers`, lines 16-18.
- Page-level PCI qualification for viewing and storing BINs: `# Bank Identification Numbers`, line 20.
- Dated 8-digit BIN notice and no-action qualification when an integration does not use BINs: `# Bank Identification Numbers > NOTE`, lines 23-24.
- Control Panel transaction-search route and displayed result location: `## Finding BINs in the gateway`, lines 29-37.
- Multi-transaction CSV route and column name: `## Finding BINs in the gateway`, line 39.
- API transaction-ID search route and response-level BIN statement: `## Finding BINs in the gateway`, line 41.
- Collected 8-digit processing/readiness statement: `## 8-Digit BIN expansion readiness`, line 46.
- Six-digit output boundary across APIs, GraphQL, console search, and BIN reports: `### BIN data availability`, line 61.
- Displayed-PAN masking, data-at-rest protection, and cited PCI version: `### Payment Card Industry Data Security Standards (e.g. PCI, DSS) and BIN Expansion`, lines 64-78.

## Evidence limitations

> [!warning] Dated support and PCI evidence
> The raw is a 2026-09-16 collection of a page whose 8-digit-transition language is framed around April 2022 and whose PCI footnote names PCI DSS v3.2.1. Use the page to retrieve Braintree's collected BIN lookup and output boundaries, but verify current Braintree behavior and current PCI DSS obligations with the applicable authorities before implementation or compliance decisions. In particular, the page does not establish that exposing or storing the first eight PAN digits has the same treatment as the six-digit BIN visibility it documents.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Related raw API references

- [[raw/braintree/docs/reference/request/transaction/search/node-2026-09-16|Braintree Node.js transaction-search reference]] - navigation-only implementation authority linked by topic; not used as factual evidence here
- [[raw/braintree/articles/control-panel/reporting/decline-analysis-2026-09-16|Braintree decline-analysis article]] - navigation-only analysis route; not used as factual evidence here
- [[raw/braintree/articles/risk-and-security/compliance/pci-compliance-2026-09-16|Braintree PCI-compliance article]] - navigation-only compliance route; not used as factual evidence here

## Raw Sources

- [[raw/braintree/articles/control-panel/transactions/bank-identification-numbers-2026-09-16|Braintree Control Panel Bank Identification Numbers]] - complete collected article covering BIN/IIN purpose, Control Panel and CSV lookup, the linked API route, 8-digit expansion, six-digit output boundaries, and PCI qualifications
