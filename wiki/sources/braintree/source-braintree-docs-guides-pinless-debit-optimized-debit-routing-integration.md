---
title: "Braintree PINless Debit Optimized Debit Routing Integration"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/integration"
raw_files:
  - "braintree/docs/guides/pinless-debit/optimized-debit-routing/integration-2026-09-16.md"
tags: [braintree, pinless-debit, optimized-debit-routing, network-transaction-identifier, credential-on-file]
---

## Overview

This unversioned Braintree website integration page describes enabling PINless debit optimized routing and the Network Transaction Identifier (NTI) behavior relevant to stored-credential transactions. It distinguishes merchants using Braintree's Vault from merchants using a third-party vault or payment orchestration provider. [[braintree]] [[braintree-payment-methods]]

## Key takeaways

- The page says enabling PINless debit requires no integration modification, but the merchant must contact PayPal to enable PINless debit routing. It separately says merchants seeking the routed low-cost debit network without waiting for a merchant report must update to one of the listed SDK versions.
- It defines an NTI as a value returned by signature card-brand networks for use with subsequent stored-credential transactions, and says PINless debit networks do not support the Credential on File (CoF) framework or issue network-generated NTIs. A successful PINless-routed authorization therefore may lack a network-generated value in the NTI field.
- The later authorization-response section also says Braintree returns an NTI value for PINless debit transactions, subject to network-specific processing rules and CoF participation. Treat that Braintree-returned value separately from a network-generated NTI: the snapshot does not resolve the exact value semantics or guarantee population for every authorization.
- Merchants vaulting with Braintree require no integration changes under this page. For an external vault, the page says the ODR engine returns an NTI where applicable and in accordance with network CoF mandates, and the merchant must pass the NTI from the original customer-initiated transaction in `previous_network_transaction_id` to link later recurring transactions.
- This snapshot is documentation evidence only; it does not prove current availability, merchant eligibility or enablement, exact installed package/runtime behavior, authorization success, payment execution, settlement or funding.

## Detail locators

- Enablement and report-versus-integration-version distinction: raw lines 17-32.
- NTI definition, network participation and successful-authorization qualification: raw lines 35-43.
- PINless authorization-response wording and network/CoF qualification: raw lines 46-57.
- Braintree Vault versus external-vault integration impact and recurring-link field: raw lines 60-68.
- Authorization-workflow and routed-network code-sample navigation: raw lines 17-18 and 68.

## Related

- [[braintree]]
- [[braintree-payment-methods]]
- [[source-braintree-docs-guides-pinless-debit-optimized-debit-routing-network-response-codes]] - separate supplemental network-response-code reference; its processor response code remains the source of truth

## Raw Sources

- [[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/integration-2026-09-16|Braintree PINless Debit optimized debit routing integration (2026-09-16 snapshot)]]
