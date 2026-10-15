---
title: "Adyen PGP encryption for sensitive files"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/security/sensitive-data/pgp-encryption"
raw_files:
  - "adyen/docs/development-resources/security/sensitive-data/pgp-encryption/2026-09-15.md"
tags: [adyen, pgp, encryption, file-security, key-management]
---

## Overview

This [[adyen]] guide describes generating a PGP key pair and registering its **public** key in the Customer Area so Adyen can encrypt files matching a selected purpose. The captured page lists batch-processing files, optionally encrypted reports, and sensitive-card-data files such as migration and Account Updater result files. It is a file-protection and key-management route through [[adyen-pgp-file-encryption]], distinct from card-payload JWE encryption and SFTP transport security.

## Key takeaways

- A payments integration with Adyen is the stated prerequisite. The page limits **merchant-account** registrations to encrypted reports and Account Updater; the Customer Area registration step names their purposes as **Reports** and **AccountUpdater**. The batch-files example is therefore not a general merchant-account permission. See **Requirements** and **2. Register the PGP key with Adyen**, raw lines 34–42 and 110–136.
- The GnuPG walkthrough generates a key pair, exports the armored **public** key, and uploads that public key with a selected **Purpose**. It explicitly says not to upload the private key. Files matching that purpose are then encrypted with the registered key. See raw lines 56–108 and 127–136.
- An expired registered key can impair transaction processing or decryption of important information. The merchant is responsible for keeping registered keys valid and current. The captured page describes a notice two weeks before expiry and recommends generating and registering a new key; alternatively it describes extending the existing key expiry and registering the updated public key. See **Handle an expiring PGP key**, raw lines 138–147, and **Update PGP key expiry**, lines 149–211.
- The opening notes that PGP keys can sign, encrypt, and decrypt. This guide's operational sequence concerns public-key registration for **file encryption**; it does not specify a signing or signature-verification flow. The snapshot also does not provide a key-fingerprint verification procedure, a rotation overlap guarantee, or distinct test/live registration rules.

## Detail locators

- File-use examples and generate/register sequence: **PGP encryption**, raw lines 15–32.
- Merchant-account limitation and notification subscription: **Requirements**, raw lines 34–42.
- GnuPG installation and key-generation commands, key size and expiry recommendations, armored export: **GnuPG command line tools** and **1. Generate a new PGP key**, raw lines 44–108.
- Customer Area account selection, registered-key display, purpose selection, public-key warning and upload: **2. Register the PGP key with Adyen**, raw lines 110–136.
- Expiry impact, notice, replacement or expiry extension, and re-registration: **Handle an expiring PGP key** and **Update PGP key expiry**, raw lines 138–211.

## Related

- Company: [[adyen]]
- Concept: [[adyen-pgp-file-encryption]]
- Adjacent account-update route: [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/development-resources/security/sensitive-data/pgp-encryption/2026-09-15|Adyen PGP encryption guide]] — full pinned 2026-09-15 snapshot; page metadata says last modified 2023-08-29
