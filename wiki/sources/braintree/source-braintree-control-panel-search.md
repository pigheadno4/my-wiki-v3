---
title: "Braintree Control Panel Search"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/control-panel/search"
raw_files:
  - "braintree/articles/control-panel/search-2026-09-16.md"
tags: [braintree, control-panel, search, transactions, vault, subscriptions, reporting]
---

## Overview

This collected Braintree article documents search in the Control Panel. It distinguishes a quick basic search for specific transactions and Vault records from advanced searches for transactions, verifications, Vault customers and subscriptions; it is not documentation for an SDK or API search operation.

## Key takeaways

- The basic search bar is the limited, quick route for locating specific transactions and Vault records. Its searchable categories include customer, payment-method, cardholder, transaction, order and custom-field values; custom-field API and display names are not searchable.
- Basic search returns only transactions or Vault records made in the preceding 60 days. Newly created transactions or customers can take time to appear, and the page warns that searches within 30 minutes of creation may miss them.
- Advanced search is divided into Transactions, Verifications, Vault and Subscriptions. Transaction search supports filtered transaction-history searches and CSV-based custom reporting; when searching by gateway user, subscriptions are excluded from the results.
- Verification search is limited to 40,000 records. Vault search exposes only the last 10 transactions performed with a customer record and directs readers to transaction search for all associated activity. Subscription search provides an activity overview and links an individual subscription ID to its history.
- Search-result downloads are CSV files. The collected page caps transaction-search downloads at 500,000 records and subscription, Vault and verification downloads at 40,000 records, requiring narrower criteria above those limits. It says download history remains available in the Control Panel for at least 24 hours.

## Detail locators

- Basic versus advanced search purpose: `# Search`, lines 16-20.
- Basic-search location, object scope and searchable categories: `## Basic search bar`, lines 25-52.
- Basic-search 60-day window and creation-indexing delay: `## Basic search bar`, lines 55-56.
- Advanced-search purpose and four search areas: `## Advanced search options`, lines 61-69.
- Transaction filters, gateway-user subscription exclusion and CSV reporting purpose: `### Transactions`, lines 74-87.
- Verification criteria, 40,000-record search limit and Control Panel route: `### Verifications`, lines 98-119.
- Vault-search criteria, Control Panel route and last-10-transactions boundary: `### Vault`, lines 122-140.
- Subscription overview and individual-history route: `### Subscriptions`, lines 143-154.
- CSV download, per-search download caps and at-least-24-hour history: `## Downloading results`, lines 157-163.
- Account-setup qualification for some downloaded transaction columns: `## Downloading results`, line 167.

## Evidence boundary

> [!warning] Collected Control Panel behavior, not API behavior or permission authority
> This article instructs a user to log in before advanced searches but names no required Control Panel role or permission. It does not establish equivalent SDK/API search behavior or current product support. Treat the 60-day basic-search window, creation-indexing delay, result/download limits and download-history duration as claims from the 2026-09-16 collected snapshot.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/control-panel/search-2026-09-16|Braintree Control Panel Search]] - complete collected article covering basic and advanced search purposes, object-specific result boundaries, date and indexing qualifications, CSV downloads and the absence of a named permission requirement
