# Adyen C63 API Explorer recovery preparation

Status: **AWAITING COLLECTION APPROVAL — no ingestion-ready manifest**. Prepared 2026-11-02.

C62 committed and pushed as `943e71a244ec9bcadbf11b6ce906b7a95bf2daad`; origin/main exact SHA verified. Current Adyen source count: **2,899 = 2,547 General Docs + 336 API Explorer + 16 GitHub**.

## Verified local readiness

All **336 collected complete-body API Explorer pages are ingested**. Of 363 local API Explorer raw snapshots, the only 27 unreferenced snapshots are title-only stubs. Every stub was re-screened and hash-pinned in [recovery-proposal.json](recovery-proposal.json). Their exclusion remains in force. No eligible source units exist for another ingestion round, so no empty or placeholder ingestion manifest, dispatch contract, runtime, candidates or source pages were created.

The captured Checkout v72 overview also lists ten operations with no page-level raw evidence (already recorded during C56). These are **collection gaps**, not uningested raw pages; path metadata supplies no behavioral evidence. This readiness check is local and does not claim current upstream availability or complete upstream coverage.

## Proposed bounded recovery before C63 ingestion

The concrete proposed scope is **37 gap items**: retry the 27 exact official Markdown URLs recorded for title-only stubs, and resolve the official page-level documentation URLs for the ten Checkout method/path references below before fetching those resolved pages. Ten method/path identifiers are not ten already-verified documentation URLs. Use official Adyen documentation only, preserve URL/path case and the documented duplicate-prefix fixup; no SDK/spec/repository expansion or other API families.

- `GET /paymentLinks/{linkId}`
- `PATCH /paymentLinks/{linkId}`
- `POST /payments/{paymentPspReference}/amountUpdates`
- `POST /payments/{paymentPspReference}/cancels`
- `POST /payments/{paymentPspReference}/captures`
- `POST /payments/{paymentPspReference}/refunds`
- `POST /payments/{paymentPspReference}/reversals`
- `GET /sessions/{sessionId}`
- `PATCH /sessions/{sessionId}`
- `DELETE /storedPaymentMethods/{storedPaymentMethodId}`

Collection approval would authorize only this bounded recovery: fetch/stage the resolved official Markdown references, retain status/error and response provenance, compare against existing immutable raw, and write new dated snapshots for recovered complete bodies without overwriting September evidence. Repeated title-only responses remain excluded. Record unresolved or unavailable documentation URLs without inventing schemas, request fields or operation outcomes. Do not refresh the entire corpus, change code/rules/validators, operate provider/account/device/payment systems, or ingest recovered content during collection.

After all recovery attempts finish, report exact complete-body successes/failures and new raw hashes. Then prepare a **new exact C63 ingestion manifest** containing only recovered complete-body evidence, fixed questions and three distinct preselected full-read audits where campaign size permits. Follow the existing provider-specific review and promotion rules; any smaller scope requiring a policy exception must be presented explicitly. Request separate ingestion approval for that manifest. No automatic ingestion from collection approval.

This proposal is uncommitted and unpushed. C62 publication is complete; C63 collection and ingestion have not started. [Readiness evidence](readiness-validation.json).

User approved this bounded recovery collection on 2026-11-02. Collection is active; ingestion and publication remain unapproved. Preparation statements above retain their historical meaning.
