---
title: "Braintree Data Migration Imports"
type: source
date_ingested: 2026-09-27
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/get-started/data-migration/imports"
raw_files:
  - "braintree/articles/get-started/data-migration/imports-2026-09-16.md"
tags: [braintree, data-migration, imports, vault, payment-methods]
---

## Overview

This collected Braintree article documents a managed process for importing customers and payment methods from another processor into the Braintree gateway. It covers the export and secure-transfer prerequisites, Braintree's preferred PGP-and-SFTP transfer flow, identifier mapping, supported data categories, and consequential import limits; it is not an export procedure, backup service, failover mechanism, or guarantee that imported wallet payment methods will transact successfully.

## Key takeaways

- The page limits a migration to no more than two imports: one bulk import and one import for customers created during the processing switch. Braintree says it will not perform periodic imports for backup or failover, leaving that responsibility to the merchant.
- To begin, the merchant must request a data export from its current or former processor and ask that processor to transfer the data to Braintree over a secure connection. Braintree describes a preferred process in which it obtains the processor's PGP public key, sends encrypted SFTP credentials, receives data encrypted with Braintree's public key, and performs the import. Encryption with Braintree's public key is stated as required before transmission.
- After completion, Braintree says it provides a logfile containing the customer IDs and payment-method tokens created in the gateway. For mapping, Braintree can generate those identifiers or use supplied values; supplied identifiers should be checked against existing Vault customers to prevent collisions.
- CSV with UTF-8 encoding is preferred, and other formats may delay the import. Detailed credit-card, optional customer and billing-address, custom-field, wallet, and US ACH fields remain in the raw locators below rather than being duplicated here.
- The page documents imports for credit cards, PayPal Billing Agreements, Apple Pay cards, Google Pay cards and network tokens, and US ACH. Payment-method-specific conditions matter: the PayPal Business Account used for the billing agreements must match the account linked to the Braintree gateway; Apple Pay and Google Pay data require processor-separated files; and the issuer ultimately determines transaction success for imported Apple Pay and Google Pay methods, which may need to be re-added after consistent declines.

> [!warning] Collected import boundaries
> Treat the two-import cap, required public-key encryption, collision check, account-match requirement, separate wallet files, and issuer-controlled wallet transaction outcomes as material boundaries of this collected page. The 2026-09-16 snapshot does not establish current import availability, processor participation, timing, acceptance, transaction success, backup coverage, or failover coverage.

## Detail locators

- Two-import maximum and no periodic backup or failover imports: `# Imports > **NOTE**`, lines 17-18.
- Import purpose and export/secure-transfer prerequisites: `# Imports`, line 22.
- Preferred PGP, credential, SFTP and import process plus output logfile: `## Data transfer process`, lines 25-35.
- Required encryption with Braintree's public key: `## Data transfer process > **IMPORTANT**`, lines 38-39.
- Preferred CSV/UTF-8 format and delay qualification: `## Data format`, lines 44-46.
- Identifier generation or reuse and collision check: `## Mapping the data`, lines 49-55.
- Credit-card minimum and optional data categories: `## Required credit card fields` through `## Optional fields`, lines 60-151.
- Vault custom-field mapping route: `## Custom fields`, lines 154-156.
- PayPal Billing Agreement inputs and Business Account match: `## Importing PayPal Billing Agreements`, lines 159-165.
- Apple Pay separate-file, field-category and issuer-success boundaries: `## Importing Apple Pay cards`, lines 170-181.
- Google Pay separate-file, card/network-token category and issuer-success boundaries: `## Importing Google Pay Cards and Google Pay Network Tokens`, lines 188-215.
- US ACH input categories and ownership-type mapping: `## Importing US ACH` through `## Required Fields:`, lines 222-263.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-data-migration]]

## Related raw API references

- [[raw/braintree/articles/get-started/data-migration/public-key-2026-09-16|Braintree data-migration public-key guide]] - navigation only; not read as factual evidence for this source
- [[raw/braintree/articles/control-panel/custom-fields-2026-09-16|Braintree Control Panel custom-fields article]] - navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/articles/get-started/data-migration/imports-2026-09-16|Braintree Data Migration Imports article]] - complete collected page covering import purpose, prerequisites, preferred transfer process, mapping, supported data categories, and consequential limits
