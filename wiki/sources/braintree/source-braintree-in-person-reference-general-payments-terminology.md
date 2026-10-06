---
title: "Braintree In-Person General Payments Terminology"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/reference/general-payments-terminology"
raw_files:
  - "braintree/in-person/reference/general-payments-terminology-2026-09-16.md"
tags: [braintree, in-person, payments-terminology, card-reader, tokenization, offline-payments]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website reference is a glossary for payment-industry, merchant-system, and Braintree In-Person terms used across the provider documentation. It is terminology orientation, not a transaction-lifecycle guide or evidence of current certification, product availability, merchant enablement, API acceptance, authorization, capture, settlement, refund, void, or funding.

## Key takeaways

- The payment-industry section defines terms including PCI Council, E2EE, P2PE, EMV, EMV liability shift, card networks, interchange fees, and US PIN debit gateways. Its statements that the Braintree solution is E2EE and was then undergoing P2PE certification belong to this collected snapshot; they do not establish current certification status.
- The omni-channel section distinguishes the merchant systems around a payment integration: POS/ECR, hotel-oriented PMS, OMS, ERP, call-center applications, and ecommerce front ends. The OMS row says order management can trigger capture, but the page does not define capture behavior or guarantee that an OMS performs it.
- The Braintree section covers reader terminology and describes the GraphQL API as the communication route between merchant software and a Braintree reader. It also distinguishes tokenization, which creates a Braintree reference token for sensitive card or transaction data, from vaulting, which creates a customer record and links customer or transaction data to it.
- The remaining provider-specific rows orient readers to contactless/NFC, QR-code PayPal and Venmo acceptance, digital wallets, Store and Forward, POS-managed offline floor limits, and reader safety stock. These glossary descriptions route to dedicated guides for operational conditions; they do not themselves prove availability, eligibility, successful offline forwarding, or a payment outcome.
- Despite the broad title, this page does not define the transaction operations or states called authorization, capture, sale, settlement, refund, void, reversal, or In-Store Context. Mentions of capture and referenced refunds are examples inside OMS and tokenization rows, not a lifecycle contract. Use the dedicated transaction sources for those meanings and conditions.

## Detail locators

- Glossary purpose: introductory sentence, raw line 16.
- PCI, encryption, EMV, card-network, interchange, and PIN-debit terms: `Payments Industry Terminology`, raw lines 19-29.
- POS/ECR, PMS, OMS, ERP, call-center, and ecommerce-system terms: `Omni-Channel Eco-System Terminology`, raw lines 32-40.
- Reader and GraphQL communication terminology: `Braintree Payments Terminology`, raw lines 43-47.
- Tokenization and vaulting descriptions and example uses: `Braintree Payments Terminology`, raw lines 48-49.
- NFC, QR-code wallets, digital wallets, Store and Forward, offline floor limits, and safety stock: `Braintree Payments Terminology`, raw lines 50-55.
- EMV receipt and GraphQL navigation links: raw line 57; these links are navigation, not additional evidence read for this entry.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/reference/graphql-docs-2026-09-16|GraphQL Docs]] - unread navigation linked by the glossary
- [[raw/braintree/in-person/guides/vaulting-and-customers-2026-09-16|Vaulting and Customers]] - unread navigation linked by the glossary
- [[raw/braintree/in-person/guides/paypal-and-venmo-qrc-2026-09-16|PayPal and Venmo QR Codes]] - unread navigation linked by the glossary
- [[raw/braintree/in-person/guides/offline-transactions-2026-09-16|Offline Transactions]] - unread navigation linked by the glossary
- [[raw/braintree/in-person/about/solution-coverage-2026-09-16|Solution Coverage]] - unread navigation linked by the glossary

## Raw Sources

- [[raw/braintree/in-person/reference/general-payments-terminology-2026-09-16|Braintree In-Person General Payments Terminology (fetched 2026-09-16)]]
