# Fixed query check — api-explorer-balanceplatform-latest-delete-scaassociations

Pinned source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-delete-scaassociations.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/scaAssociations
Pinned raw: `raw/adyen/api-explorer/balanceplatform/latest/delete/scaAssociations/2026-09-15.md` (SHA-256 `495f918f199668e43b2a50e086c316c9f79933359f8aabf4659063c605f945f0`).

## Q1
For `balanceplatform/latest/delete/scaAssociations`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** The captured Balance Platform API Explorer page documents `DELETE /scaAssociations` to delete one or more SCA associations for a device (raw lines 5–7). It lists TEST `/bcl/v2` as its server (9–10). The header table calls `WWW-Authenticate` required for SCA authentication (14–17). The body table marks `entityId`, `entityType` and `scaDeviceIds` required; `entityType` permits accountHolder, legalEntity or paymentInstrument, and the IDs select associated devices to remove (20–25). Its example selects an accountHolder and one ID (27–38); that example is not a size or type restriction. The page documents 403 insufficient permissions but no particular credential role (64–65). Its described deletion target is the association, not the registered device itself.

## Q2
What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 204 is labeled successful association deletion (39–42); 401 means authentication required, 403 insufficient permissions, and 500 server processing failure (45–46, 64–65, 83–84). Optional error-body fields, with required children only inside `invalidFields` entries, are listed at 48–61, 67–80 and 86–99. The snapshot gives no separate device deregistration, approval or post-delete verification, propagation time, idempotency contract, or financial status. Its `latest` URL and TEST v2 server are a dated 2026-09-15 snapshot, not current live availability or proof that a deletion or funds action occurred (1–10, 39–42).
