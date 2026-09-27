---
title: "Braintree Data Migration Public Key"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/data-migration/public-key"
raw_files:
  - "braintree/articles/get-started/data-migration/public-key-2026-09-16.md"
tags: [braintree, data-migration, encryption, public-key]
---

## Overview

This collected Braintree page identifies the public key used to encrypt files sent to Braintree with customer data during a data migration. It is a narrow key-distribution page, not the import or export process, and this retrieval entry intentionally does not reproduce the published key block or its identifiers.

## Key takeaways

- Braintree says all files containing customer data must be encrypted with its public key before they are sent to Braintree.
- The page labels the key for Braintree Data Migrations, classifies it as a public key and identifies RSA as its algorithm.
- The authoritative key text and identifying metadata remain only in the raw evidence and current official page; they are not copied into this source summary.

> [!warning] Snapshot and handling boundary
> This page documents the encryption key's migration role, but it does not document the broader import procedure, transmission route, key-verification procedure, rotation or validity period. The 2026-09-16 collection date does not establish that the collected key is current or suitable for a new migration. Do not obtain operational key material from this summary.

## Detail locators

- Required use of Braintree's public key for every file sent with customer data: `# Braintree Public Key`, line 16.
- Key name, public-key classification and technical metadata: `# Braintree Public Key`, lines 19-25.
- Published PGP public-key text block: `### Text`, lines 28-82; key material is intentionally not reproduced here.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-data-migration]]

## Raw Sources

- [[raw/braintree/articles/get-started/data-migration/public-key-2026-09-16|Braintree Data Migration Public Key article]] - complete collected page covering the migration-encryption purpose, public-key metadata and key block
