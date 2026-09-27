---
title: "Braintree Data Migration"
type: concept
category: technology
tags: [braintree, data-migration, vault, payment-methods]
---

## Overview

The collected Braintree guides describe two distinct gateway-migration routes: importing customer and payment-method data from another processor into Braintree, and exporting Vault customer and saved-card data to another payment gateway. Both are bounded migrations, not periodic backup or failover services. [[source-braintree-get-started-data-migration-imports]] [[source-braintree-get-started-data-migration-exports]]

## Retrieval routes

- [[source-braintree-get-started-data-migration-overview]] - orientation route for import versus export, fee and timeline qualifications, non-migratable subscription and transaction data, ACH legal terms, and Apple Pay and Google Pay export exclusions; use the linked import and export guides for process detail.
- [[source-braintree-get-started-data-migration-public-key]] - Braintree's public-key route for encrypting every file sent with customer data during migration; obtain operational key material from the current official guide rather than copying it into the wiki.
- [[source-braintree-get-started-data-migration-imports]] - inbound import prerequisites, preferred secure transfer, identifier mapping, payment-method-specific conditions and the two-import limit; consult its raw locators for field details.
- [[source-braintree-get-started-data-migration-exports]] - outbound Vault export, receiving-gateway PCI attestation and public key, encrypted transfer, export selection and the two-export limit; consult its raw locators for the fixed CSV format.

The 2026-09-16 collected pages do not establish current availability or whether a particular processor will participate.

## Sources

- [[source-braintree-get-started-data-migration-imports]] - collected inbound migration guide
- [[source-braintree-get-started-data-migration-exports]] - collected outbound migration guide
