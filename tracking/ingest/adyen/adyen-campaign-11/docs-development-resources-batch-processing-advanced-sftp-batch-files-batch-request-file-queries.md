# Fixed retrieval checks — SFTP batch request file

## Q1 — What is this page for, what is its scope, and what should not be inferred?

It is Adyen's 2026-09-15 SFTP batch request-file reference for common FH, BH, BT and FT records across transaction types. It defines header fields and block/file counters, then says the prepared file can go to the SFTP `in` subfolder for fetch and queueing. It does not define transaction-specific record formats, prove file acceptance, or establish an individual payment/modification outcome. Retrieve through `[[adyen-batch-processing]]` → `[[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file]]` → `[[raw/adyen/docs/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file/2026-09-15]]`; raw lines 16-88. Canonical page: https://docs.adyen.com/development-resources/batch-processing/advanced-sftp-batch-files/batch-request-file.

## Q2 — What is its central format, prerequisites, and warning?

The `FH` table marks positions 1–9 required, including fixed `FH`/`1.0`/`Company`, environment, company account name, filename-matched submission platform and sequence, company-linked API credential username, and one listed file type; `EchoData` at position 10 is optional. `BH` numbers blocks sequentially, `BT` counts line records in a block, and `FT` counts blocks. See raw lines 26-57 and 59-86 for exact field formats, requiredness, allowed values, and units. The prose calls FH a merchant-account identifier but the table calls for a company account; the broader SFTP sources also leave the multi-merchant modification file layout unresolved. The SFTP `in` upload is only a transport/queue step (raw line 88), not an ACK or final financial result. Follow the same concept→source→raw route and the related SFTP/acknowledgment sources.

Counterpart qualification: raw common request-file FH field 9 marks FileType required, whereas the naming guide calls field 9 optional. These statements conflict; the generic placeholder example does not prove blank FileType is accepted. See the reviewed contradiction callout and naming-guide source route.
