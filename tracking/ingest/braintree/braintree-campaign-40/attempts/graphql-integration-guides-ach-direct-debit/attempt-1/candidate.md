---
title: "Braintree GraphQL ACH Direct Debit Integration Guide"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/graphql/integration_guides/ach_direct_debit"
raw_files:
  - "braintree/graphql/integration_guides/ach_direct_debit-2026-09-16.md"
tags: [braintree, graphql, ach, direct-debit, bank-accounts]
---

## Overview

This 2026-09-16 Braintree website snapshot is a GraphQL integration guide for US-network ACH Direct Debit. It routes the documented `tokenizeUsBankAccount`, `vaultUsBankAccount`, `verifyUsBankAccount`, `confirmMicroTransferAmounts` and `chargeUsBankAccount` flow, plus a limited-beta Instant Verification path. The guide is separate from the JavaScript v3 client SDK implementation and the versioned GitHub GraphQL schema history; it is not proof of current merchant eligibility, production enablement, deployment, bank-account ownership, successful verification, charge settlement or funding.

## Key takeaways

- The page says ACH Direct Debit client-side collection uses JavaScript v3 and is not available in Drop-in UI. Its GraphQL flow is organized around tokenizing, vaulting, verifying and transacting; linked SDK and API-reference pages remain separate authority.
- `tokenizeUsBankAccount` exchanges supplied bank details for a single-use payment-method ID. Tokenization alone does not verify the account and the resulting method is not transactable. `vaultUsBankAccount` exchanges that single-use ID for a multi-use method; when a verification method is supplied it can initiate verification in the same step, and the page says the vaulted method becomes transactable only after successful verification.
- The verification routes described are network check, micro-transfers and independent check. For micro-transfers, the merchant collects the two amounts in its own UI and submits them with `confirmMicroTransferAmounts`; even after amount confirmation, the guide requires status lookup because the account may be ready, still waiting for the verification transfers to settle, or later report verification-settlement failure. Verification requests can be retried with the same or a different method.
- Instant Verification is labeled limited beta for pilot merchants. The captured flow generates a client token and verification JWT server-side, redirects the customer through an open-banking experience, handles a returned tokenized account, and then vaults it with `INSTANT_VERIFICATION_ACCOUNT_VALIDATION`. A non-default merchant account ID used for the client token must match the later transaction's merchant account ID.
- The page requires customer mandate or proof of authorization for all ACH transactions and directs the merchant to retrieve bank details, show the applicable authorization language and pass the mandate text on `vaultUsBankAccount` or `chargeUsBankAccount`. For a verified multi-use method, `chargeUsBankAccount` creates the transaction; the page recommends including collected client device data in `riskData` to help reduce declines. Each single-use payment-method ID can be vaulted only once.

## Material warnings

> [!warning] Unresolved `verificationMethod` contradiction
> The vaulting section says a bank account can be vaulted without specifying a verification method, while the Common errors section says omission produces a non-null validation error. The same vaulting section says merchants performing their own verification should set `INDEPENDENT_CHECK`. This snapshot does not resolve which input shape is accepted for a particular account or API contract, so preserve both statements and verify against the applicable GraphQL schema and environment.

> [!warning] Example state is not a runtime guarantee
> The transaction prose says the multi-use payment method can be charged once verified, but the displayed `chargeUsBankAccount` response has `paymentMethodSnapshot.verified: false`. Treat the example as captured documentation, not proof that an unverified account is chargeable or that a charge, settlement or funding event occurred.

> [!warning] Verification settlement is not transaction settlement
> The status-search discussion concerns micro-transfer verification and whether those verification transfers have settled. It does not document the lifecycle or finality of an ACH charge. Use the dedicated ACH payment-method guide for delayed charge settlement, returns and disputes rather than transferring those facts into this GraphQL operation guide.

## Detail locators

- Client-side JavaScript v3 availability, Drop-in exclusion and four-stage flow: raw lines 14-31.
- Tokenization definition, non-verification consequence, `tokenizeUsBankAccount` request and response shapes: `## Tokenizing`, raw lines 34-124.
- Single-use-to-multi-use exchange, vault-plus-verification behavior and `vaultUsBankAccount` example: `## Vaulting`, raw lines 126-215.
- Vault-without-verification wording and `INDEPENDENT_CHECK`: `### Vaulting without verification`, raw lines 217-219.
- Network-check, micro-transfer and independent-check identities; `verifyUsBankAccount` and `confirmMicroTransferAmounts` examples: `## Verifying`, raw lines 222-371.
- Pilot-only Instant Verification, server-generated client token, merchant-account match, JWT/redirect flow and returned payment-method handling: `### Verifying with Instant verification`, raw lines 373-649.
- Mandate prerequisite, bank-detail lookup and mandate-text handoff to vault or charge: `#### Retrieve Bank Details for ACH Mandate`, raw lines 651-708.
- Verification response inspection, micro-transfer verification-state lookup and retry route: raw lines 710-775.
- Verified multi-use-method charge route, device-data recommendation and displayed example state: `## Creating Transactions`, raw lines 778-850.
- Single-use vault-once limit and conflicting omitted-`verificationMethod` error: `## Common errors`, raw lines 852-912.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Payment-method lifecycle and return context: [[source-braintree-payment-methods-ach]]

## Related raw API references

The guide links to JavaScript v3 client setup, ACH authorization language, GraphQL reference/explorer entries and fraud-device-data guidance. Those linked targets were not read for this entry and are navigation only; they do not establish SDK behavior, an exact schema version, account enablement or successful execution.

## Raw Sources

- [[raw/braintree/graphql/integration_guides/ach_direct_debit-2026-09-16|Braintree GraphQL ACH Direct Debit integration guide]] - complete collected page covering tokenization, vaulting, verification, pilot Instant Verification, mandate handling, charge creation and common errors
