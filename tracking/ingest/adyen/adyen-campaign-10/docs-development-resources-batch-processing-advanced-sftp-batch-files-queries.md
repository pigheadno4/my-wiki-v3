# Fixed retrieval checks: SFTP transaction batch files

## Q1 — Purpose and scope

**Query:** What is this Adyen advanced SFTP batch guide for, and what does a transfer or acknowledgment not prove?

**Expected answer:** It describes Support-provisioned SFTP transport and PGP protection for transaction batch input files. The page gives refunds and failed-capture retries as examples but does not establish that replaying an unresolved operation is safe. A successful connection, upload, or file acknowledgment is not proof that an individual authorization, capture, refund or payout was processed successfully; the relevant result and later outcome evidence must be checked. The snapshot's metadata says last modified in 2020.

**Raw locators:** `# Submit transaction batch files through SFTP`, lines 15–27; `## PGP encryption`, lines 56–69; `### PGP troubleshooting`, lines 71–78. **Canonical retrieval route:** [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]] → [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/2026-09-15|pinned raw]].

## Q2 — Scope, setup and security prerequisites

**Query:** What file-scope and SFTP/PGP requirements does the guide state, and how should its multi-account sentence be interpreted?

**Expected answer:** It says one request type per merchant account in a batch file and separate files for request types. Support can enable modifications for multiple merchant accounts, but this page does not define how that affects file composition; the parent overview says one type/one merchant account per SFTP file. For SFTP provisioning, send Support the Customer Area company account, external source IPs, 2048- or 4096-bit RSA SSH public key, and technical contacts, then use the environment-specific connection details provided. Encrypt input with Adyen's PGP key; Adyen signs result files, while registering the merchant's PGP public key optionally lets Adyen encrypt those results. A rejection ACK can report decryption/signature/key and unencrypted-live-card-number errors; it is file-level feedback, not final transaction success.

**Raw locators:** opening scope, lines 19–27; `## SFTP configuration`, lines 29–38; `## Connecting to the SFTP server`, lines 40–54; `## PGP encryption`, lines 56–69; `### PGP troubleshooting`, lines 71–78. **Canonical retrieval route:** [[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files]] → [[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/2026-09-15|pinned raw]].
