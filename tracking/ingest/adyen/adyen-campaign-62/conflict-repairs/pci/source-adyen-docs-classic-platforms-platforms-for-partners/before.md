---
title: "Adyen Classic partner platform requirements"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/platforms-for-partners"
raw_files:
  - "adyen/docs/classic-platforms/platforms-for-partners/2026-09-15.md"
tags: [adyen, classic-platforms, partners, ecommerce, stores, pci]
---

## Overview

This 2023-modified Classic guide, captured 2026-09-15, applies **only** to a partner arrangement for Adyen for Platforms. Unlike the ordinary platform model, the partner platform cannot process payments on behalf of its sub-merchants; Adyen establishes a direct sub-merchant relationship with card schemes. The platform onboards each sub-merchant, collects ecommerce SAQ A evidence, creates a store, and routes payments through that store. Integrations built after 2022-08-01 are directed to a separate newer guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- For ecommerce, each sub-merchant needs SAQ A and an online store to establish the direct scheme connection. POS sub-merchants also need stores but the guide says they do **not** complete SAQ A because the POS terminals establish the card-network connection and PCI requirements (raw lines 19–30). The platform must arrange store creation with Adyen Support, supplying countries, currencies, MCCs and payment methods (raw lines 40–56). This dated source does not independently establish current PCI compliance.
- Create the Classic account holder first and collect website address and phone for later store details. Before adding an ecommerce store, make sure the sub-merchant completed SAQ A and passed KYC verification (raw lines 58–71, 146–152). HOP includes SAQ A automatically; a custom onboarding flow must request `/getPciQuestionnaireUrl` and use the result to send the holder to the questionnaire (raw lines 73–100).
- The custom SAQ A URL is one-time and must be used within 15 seconds; successful redirect starts a 30-minute session. A late redirect or reload returns HTTP 401 and requires another URL. Verification status arrives through `ACCOUNT_HOLDER_VERIFICATION`, including the shown `PCI_VERIFICATION` example; verify successful SAQ A provision and KYC before continuing (raw lines 98–144). The prose calls the response field `redirectURL` but its JSON example uses `redirectUrl`; confirm the API spelling before parsing (raw lines 98–112).
- Subscribe to `ACCOUNT_HOLDER_STORE_STATUS_CHANGE`, add `storeDetails` using Classic `/updateAccountHolder`, including address, phone, merchant account, MCC, store name/reference, web address and `shopperInteraction: Ecommerce` (raw lines 146–204). The example response is `Pending`; wait for a status-change webhook with new status `Active` **before any payment processing** (raw lines 206–243).
- If a sub-merchant takes payments from its own domain, add that domain to allowed origins (raw lines 265–267). Route `/payments` with the appropriate sub-merchant `store` ID; a payment can split funds across multiple account holders, but can be processed through only **one** store (raw lines 269–279). The test `/payments` body with three splits is an example, not proof of authorization, booking, payout or bank receipt (raw lines 281–330).

## Detail locators

- Partner-only identity, direct scheme relationship, ecommerce/POS SAQ A distinction and five-step sequence: raw lines 19–38. Support configuration and account-holder prerequisites: raw lines 40–71.
- Hosted versus custom questionnaire, one-time URL/session/401, webhook and casing mismatch: raw lines 73–144. Store create fields, Pending response and Active webhook gate: raw lines 146–263. Allowed origins, single-store routing and example splits: raw lines 265–330.

## Related

- [[adyen-classic-platforms]] — older account-holder/account model; partner terms here are narrower.
- [[source-adyen-docs-classic-platforms-platforms-for-pos]] — separate POS-store path and SAQ A distinction.
- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page]] — hosted onboarding route.
- [[adyen-platforms]] — newer balance-platform model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/platforms-for-partners/2026-09-15|Classic partner platform requirements, captured 2026-09-15]]
