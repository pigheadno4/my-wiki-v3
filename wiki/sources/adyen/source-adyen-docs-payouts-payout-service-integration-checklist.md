---
title: "Adyen Payout Service integration and go-live checklist"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/integration-checklist"
raw_files:
  - "adyen/docs/payouts/payout-service/integration-checklist/2026-09-15.md"
tags: [adyen, payouts, payout-service, integration, go-live]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service checklist orders account structure, TEST development, webhooks, payout routes, reporting and separate LIVE setup for an Adyen Payouts integration. It belongs under [[adyen-payouts]], whose Payout Service route is distinct from the legacy Online Payout API. Completing checklist items or getting an HTTP 200 from a read request does not establish a successful payout or bank receipt.

## Key takeaways

- Before development, the page expects API credentials from an Adyen contact and joint implementation design, balance-platform/resource setup, and a settlement model for sales funds into the balance account. Its minimum resource model distinguishes company and merchant accounts, balance platform, legal entity, account holder representing the business, business-funds balance account, and verified bank-account transfer instrument. See raw lines 23–51.
- Build with a Transfers API credential (`ws@BalancePlatform.[YourBalancePlatform]` as shown). The optional server library route is described as a development aid. A TEST GET `/transfers` with date/pagination filters is a credential check; HTTP 200 returns `data` and `_links`, not proof of any transfer's completion. The code blocks name specific library versions and TEST endpoint; some examples are not copy-ready, including malformed Java date-expression punctuation at raw line 105 and a Go sample that sets `CreatedUntil` but omits `CreatedSince` despite the surrounding two-date example (raw lines 77–239). See raw lines 53–239.
- Set up a webhook endpoint and Customer Area webhook configuration, and acknowledge each payout-lifecycle status webhook. HMAC signature verification and automated payout-error fallback are explicitly **recommended**, not stated as absolute requirements. An error reason code can guide the fallback. See raw lines 241–254.
- Payout paths separate third-party bank/card beneficiaries from the company's own verified transfer instrument for sales proceeds; the latter can be scheduled or on demand and may leave a reserve balance. Reports credentials from the Adyen contact are required for programmatic downloads, and reports serve reconciliation. See raw lines 256–276.
- For LIVE, apply for a live account and **replicate TEST setup**, because TEST configuration is not copied to LIVE. Switch to live Balance Platform API credentials and endpoint, then verify a live API request, payout success/error scenarios, and live webhook receipt/acceptance. These are go-live checklist actions, not evidence they occurred for a particular account. See raw lines 278–294.

## Evidence boundary

The page does not provide an account-specific approval, funding, settled-balance, payout booking or bank-credit record. The GET test example and HTTP 200 only validate a read credential path. Treat versioned snippets as examples requiring validation before execution; the raw's Java/Go differences are sample-quality issues, not new API rules.

## Detail locators

- Prerequisites and seven-resource structure: raw lines 27–51.
- TEST credential check and versioned SDK snippets: raw lines 53–239.
- Webhook configuration, security and fallback wording: raw lines 241–254.
- Payout/report routes and TEST-to-LIVE transition: raw lines 256–294.

## Related

- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-get-started]]
- [[source-adyen-docs-payouts-payout-service-getting-paid]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/integration-checklist/2026-09-15|Payout Service integration checklist, 2026-09-15]]
