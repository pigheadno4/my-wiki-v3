---
title: "Adyen transaction batch files through SFTP"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files"
raw_files:
  - "adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/2026-09-15.md"
tags: [adyen, batch-processing, sftp, pgp, file-transfer]
---

## Overview

This 2026-09-15 Adyen guide explains preparing and transferring **transaction batch files through SFTP** for bulk processing. It gives refunds and failed-capture retries as examples, not as automatic safe-retry instructions. The page metadata says last modified in 2020. SFTP transport, PGP protection, acknowledgment of rejection, and individual payment/modification outcomes are distinct; this guide does not prove that an uploaded request succeeded financially.

## Key takeaways

- The guide says a batch file holds one request type per merchant account and directs separate files for request types such as authorization, refund and capture. It also says Support can enable modifications for multiple merchant accounts. The parent [[source-adyen-docs-development-resources-batch-processing]] table states one request type and one merchant account per SFTP file; this page does not explain how a Support-enabled multi-account modification case changes file composition. Preserve that unresolved qualification.
- Adyen requires a secure SFTP channel and PGP data encryption. To provision an SFTP directory, the merchant sends Support its Customer Area company account, external upload-server IPs, an RSA SSH public key (2048 or 4096 bits), and technical contact details; Support responds when access is ready. The page lists distinct test and live hosts, ports, usernames and allowlist IPs. These are dated connection details to verify before actual use. See `SFTP configuration` and `Connecting to the SFTP server`.
- Encrypt each batch input file with Adyen's PGP key before upload. The page says Adyen signs the batch result file with its PGP key; registering the merchant's PGP public key is an optional extra so Adyen encrypts result files for that merchant. Registering it requires **Batch Files** as the key purpose. See `PGP encryption`.
- The troubleshooting section says a rejected file can yield a batch acknowledgment file with rejection details. It names decryption/signature or unconfigured-key issues, missing response-encryption public key, and an unencrypted file containing live card numbers as possible causes. A transport connection or acknowledgment is not a per-record financial result; result files and relevant later outcome signals must be assessed separately. See `PGP troubleshooting`.

## Detail locators

- `SFTP configuration`, lines 29–38: exact Support provisioning inputs and SSH key-size requirement.
- `Connecting to the SFTP server`, lines 40–54: test/live hosts, ports, Support-provided user formats and IP allowlists.
- `PGP encryption`, lines 56–69: input encryption, Adyen result signing, optional merchant-key result encryption and Customer Area key route.
- `PGP troubleshooting`, lines 71–78: acknowledgment-file link and file-level rejection examples; no per-transaction success semantics.

## Related

- [[adyen]]
- [[adyen-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing]]
- [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-acknowledgement-file]]

## Raw Sources

- [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/2026-09-15|Adyen SFTP batch-file guide, 2026-09-15 snapshot]]
