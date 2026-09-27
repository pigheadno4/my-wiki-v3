---
title: "Braintree Data Migration Exports"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/data-migration/exports"
raw_files:
  - "braintree/articles/get-started/data-migration/exports-2026-09-16.md"
tags: [braintree, data-migration, vault, exports, pci-dss]
---

## Overview

This collected Braintree guide documents exporting Vault customer and saved-card data when moving to another payment gateway. It routes readers through the receiving gateway's PCI-attestation and public-key prerequisites, encrypted transfer, export selection and fixed file format; the detailed CSV headers remain in the raw page.

## Key takeaways

- Braintree says a migration must use no more than two exports: one for the bulk of customers and one for customers created while processing is switched over. It explicitly does not provide periodic exports for backup or failover.
- Before an export to another gateway, the merchant must provide Braintree an attestation of that gateway's PCI compliance from a qualified provider. Braintree then requests a public encryption key from the receiving service provider, verifies that key, encrypts the sensitive data and transmits it via SFTP, SCP or FTP over SSL; protecting the corresponding private key under PCI DSS remains the receiving provider's responsibility.
- Export selection is either the entire Vault, covering all saved customers and credit cards, or a merchant-supplied list of customer IDs.
- The output is a GPG-encrypted CSV whose format cannot be modified. Each card receives its own row with its customer and address; a customer without cards receives a customer-only row with empty card and address fields.

> [!warning] Migration and backup boundary
> This page documents a bounded gateway-migration export, not a periodic backup or failover service. It does not identify a self-service initiation route, delivery timing, pricing or an eligibility decision, and its 2026-09-16 collection date does not establish current availability.

## Detail locators

- Two-export maximum and no periodic backup/failover exports: `# Exports > NOTE`, lines 17-18.
- PCI attestation, receiving-provider public key, encrypted transfer, private-key responsibility and key verification: `# Exports`, lines 22-26.
- Entire-Vault versus customer-ID selection: `## Export types`, lines 29-35.
- Fixed GPG-encrypted CSV format and row structure: `## Export format`, lines 38-50.
- Complete CSV header names, descriptions and examples: `## Export format > ### File headers`, lines 53-147.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-data-migration]]

## Raw Sources

- [[raw/braintree/articles/get-started/data-migration/exports-2026-09-16|Braintree Data Migration Exports article]] - complete collected page covering outbound Vault migration prerequisites, encrypted transfer, export selection, fixed CSV format and header details
