---
title: "Adyen Payout Service getting started"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/get-started"
raw_files:
  - "adyen/docs/payouts/payout-service/get-started/2026-09-15.md"
tags: [adyen, payout-service, payouts, transfers-api, onboarding]
---

## Overview

This 2026-09-15-captured [[adyen]] page outlines getting started with **Payout Service**: register interest, design funding and counterparty scope with Adyen, obtain TEST Transfers API and Customer Area access, build/test, then arrange and configure LIVE access. It routes within [[adyen-payouts]] but is a **Transfers API Payout Service** path, distinct from the legacy Payout API described by older online-payout guides. The page does not itself grant access or prove an eligible route, an executed payout or bank receipt.

## Key takeaways

- Contact Adyen to register interest. Adyen then discusses the business model and operating/payout countries, and works with the integrator to decide how payouts are funded, how they are sent and which counterparty types may be paid. Those design choices are use-case specific; this overview does not publish a universal allowed counterparty, region, funding source or legal payee rule. See raw lines 21–56.
- After design, an Adyen contact provides TEST credentials for the **Transfers API** to initiate fund transfers and payouts and Customer Area access for test reporting, account configuration, balance accounts and transfer instruments. Existing Adyen payment processors may already have Customer Area access; payment-processing and balance-platform API credentials have distinct management routes. Configured webhooks provide payout status updates. See raw lines 58–81.
- The documented sequence is build with the test account and credentials, use the integration checklist and implementation resources, test in the TEST environment, then contact Adyen for a LIVE account. The page recommends testing again after live configuration. A completed local/test integration or a “ready to go live” statement here is not provider account approval, transfer booking or beneficiary-bank receipt. See raw lines 83–99.
- **TEST setup and configuration are not replicated to LIVE.** The integrator must reproduce the setup in LIVE, test the LIVE integration, and follow the go-live checklist. This is an environment boundary; do not assume test credentials, webhook endpoints or account settings carry over. See raw lines 101–107.
- The page routes to separate account-structure, integration/go-live checklist and access guides. It does not specify request fields, role grants, funding movement states, retry or return behavior. Use those dedicated guides and actual payout status evidence before claiming a payout outcome. See raw lines 109–113.

## Detail locators

- Payout Service identity and contact requirement: raw lines 17–28.
- Eight-step onboarding sequence, use-case design and funding/counterparty scope: raw lines 30–56.
- TEST Transfers API/Customer Area credentials, dashboards and webhook setup: raw lines 58–81.
- Build, TEST verification and LIVE account request: raw lines 83–99.
- LIVE configuration not copied from TEST, live retest and linked guides: raw lines 101–113.

## Related

- [[adyen]] — provider profile.
- [[adyen-payouts]] — payout concept; legacy Payout API and Payout Service routes must remain distinct.
- [[adyen-platforms]] — balance-platform resource context, not an interchangeable Marketplace account authority.

## Related raw API references

- The raw page links to Transfers API, the Payout Service integration checklist, account structure and access guides. Consult those pages separately for exact roles, request schemas and outcome states.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/get-started/2026-09-15|Adyen Payout Service get-started guide — pinned 2026-09-15 raw snapshot]]
