---
title: "Adyen Balance Platform API v2: POST /paymentInstruments/{id}/networkTokenActivationData"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments/(id)/networkTokenActivationData"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/(id)/networkTokenActivationData/2026-11-02.md"
tags: [adyen, balance-platform, issuing, network-tokens, digital-wallets, api]
---

## Overview

This 2026-11-02 Balance Platform API v2 reference describes `POST /paymentInstruments/{id}/networkTokenActivationData`, which creates network-token provisioning data for adding a user's payment instrument to a digital wallet. The page shows only the TEST server `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is a documentation route and does not verify current live availability. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

> [!warning] Contradiction
> The request-body table marks `sdkOutput` as `No` under Required, while the same row says `sdkOutput` is required to create network-token provisioning data (pinned raw line 23). The table's property flag and the described flow disagree; this capture does not show whether omitting the field succeeds or fails.

- The required **path** `id` identifies the payment instrument. The request-body table marks `sdkOutput` as **not required**, but its description explicitly says this SDK-generated block is **required to create** network-token provisioning data. The page does not separately state whether the whole body is required, show a request JSON example, or define an idempotency contract. Preserve the table/prose tension instead of treating the table's `No` as permission to omit it in the described flow.
- A 200 response has an `sdkInput` string marked optional in the response table. Its description says this activation-data block is required to initialize Adyen's network-token provisioning SDK. Response-field optionality and the downstream SDK prerequisite are different claims; the page gives no 200 example to show actual presence.
- Creating or returning provisioning data is a step toward adding an instrument to a wallet. This reference does not report a created or active network token, completed wallet provisioning, cardholder authentication, a payment authorization, capture or settlement. Use separate token-status and wallet-flow sources for those outcomes.
- The listed errors are 400, 401 (authentication required), 403 (insufficient permissions), 422 (validation), and 500. The 422 and 500 examples describe changing or creating payment instruments, not provisioning-data-specific failures; treat them as generic examples. No retry, reversal or asynchronous outcome contract is stated here.

## Detail locators

- Purpose, TEST server, path ID, `sdkOutput` table/prose condition: pinned raw lines 5–23.
- 200 response and `sdkInput` downstream use: pinned raw lines 25–33.
- Error schemas and illustrative error bodies: pinned raw lines 36–202.

## Related

- [[adyen-issuing]] — Issuing and network-token context.
- [[source-adyen-docs-issuing-tokens-digital-wallet]] — separate wallet provisioning lifecycle guide.
- [[source-adyen-api-explorer-balanceplatform-latest-get-paymentinstruments-id-networktokens]] — separate network-token list route.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstruments/(id)/networkTokenActivationData/2026-11-02|Network-token provisioning data POST snapshot]]