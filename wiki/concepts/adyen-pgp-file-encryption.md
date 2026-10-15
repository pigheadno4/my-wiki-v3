---
title: "Adyen PGP file encryption"
type: concept
category: technology
tags: [adyen, pgp, file-security, key-management]
---

## Definition

Adyen's PGP file-encryption guide describes merchant generation of a PGP key pair and Customer Area registration of its **public** key for a selected file purpose. Adyen says files matching the selected purpose are encrypted with that registered key. The page covers batch-processing files, optionally encrypted reports, and files with sensitive card data such as payment-data migration and Account Updater results. Merchant-account registration is limited to **Reports** and **AccountUpdater** purposes in the captured guide. Keep the private key private; the guide expressly forbids uploading it. [[source-adyen-docs-development-resources-security-sensitive-data-pgp-encryption]]

## Scope and lifecycle

The captured instructions recommend expiry and replacement before expiry, while allowing extension and re-registration of an existing key. An expired registered key can affect transaction processing or decryption, and the merchant is responsible for keeping it valid. This is a 2023-last-modified page captured in 2026, not proof of current account eligibility, active key state, completed file delivery, successful decryption, signing/verification behavior, transport security, fingerprint validation or test/live equivalence.

## Sources

- [[source-adyen-docs-development-resources-security-sensitive-data-pgp-encryption]] — 2026-09-15 captured Adyen PGP key-generation, purpose-scoped public-key registration and expiry guide.
