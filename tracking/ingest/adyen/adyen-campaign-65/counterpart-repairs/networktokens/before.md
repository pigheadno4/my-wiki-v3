---
title: "Adyen Issuing: Manage network tokens"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/manage-network-tokens"
raw_files:
  - "adyen/docs/issuing/manage-network-tokens/2026-09-15.md"
tags: [adyen, issuing, network-tokens, digital-wallets]
---

## Overview

This 2026-09-15 snapshot of an Adyen Issuing guide covers network tokens created by Visa or Mastercard when a cardholder adds an Adyen-issued card to a digital wallet. A token is a PAN alternative for a particular card-device-wallet pairing; Adyen describes managing its status separately from the card. This is Issuing card-token management, not merchant checkout tokenization. [[adyen-issuing]]

## Key takeaways

- An Issuing-supporting integration and a Configuration API credential with the stated account-scoped NetworkTokens read/patch role are prerequisites in this guide. The sample requests use the test Balance Platform API host.
- List a payment instrument's tokens with GET `/paymentInstruments/{id}/networkTokens`, including all statuses; retrieve a single token with the documented GET `/networkTokens/{networkTokenId}` operation. The single-token curl sample instead uses a nested `/paymentInstruments/{id}/networkTokens/{networkTokenId}` path. Verify the intended API route before implementation.
- The guide lists inactive → active after phone-call authentication, active → suspended, suspended → active, and active/suspended → closed. PATCH requests supply `status`; closed is final. HTTP 202 means accepted for asynchronous processing, with webhooks supplying the final result, not a completed status change. The PATCH operation label and sample curl likewise show different URL shapes.
- To limit usage, the guide illustrates POST `/transactionRules` for a card-scoped active-token-count rule and a separate rule blocking token-processed transactions greater than EUR 50. These are example rule configurations, not proof that token provisioning or any transaction was actually blocked.

## Detail locators

- Requirements and account-scoped role: raw lines 29–36. List and single-token operations, response fields and status values: raw lines 38–294. The list's `type` table names `applePay`/`googlePay` at line 192, while the single-token `type` table names `wallet`/`cof` at line 261; do not silently reconcile these differing descriptions.
- Status transitions, final closure, PATCH request and asynchronous result: raw lines 295–334. The operation label at line 306 and sample curl at line 323 have different path shapes.
- Active-token-count rule example: raw lines 340–784, especially `activeNetworkTokens` with `greaterThanOrEqualTo: 1`, payment-instrument scope, `requestType: authorization`, and `hardBlock` at lines 359–383. The document calls this a one-per-card limit; the authorization request type in the example does not by itself establish how provisioning is enforced.
- Token-transaction amount rule: raw lines 785–1319, especially `processingTypes: token`, amount over EUR 50, `hardBlock`, and the test-host sample at lines 801–834. Rule-creation HTTP 200 responses return a rule ID at lines 754 and 1281; they do not demonstrate an evaluated authorization outcome.

## Related

- [[adyen]] — provider context.

- [[adyen-issuing]] — Issuing card-program context.

## Raw Sources

- [[raw/adyen/docs/issuing/manage-network-tokens/2026-09-15|Manage network tokens — 2026-09-15 snapshot]]
