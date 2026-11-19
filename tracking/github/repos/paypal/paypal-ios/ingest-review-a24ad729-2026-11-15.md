# PayPal iOS 3.2.0 Full Additive Ingest Review

## Authorization and Identity

- User approved full additive ingestion including the ten-file exact-SHA supplement, preserving all prior history, then explicitly approved focused reading.
- Item: `github-a24ad729631b9a2aa48d`; package: `paypal-ios@3.2.0`; exact SHA: `7eb8f7b7f9162e8f8114abae7f5dba9b525eae64`.
- Prior: `paypal-ios@3.1.1`, SHA `de98414f5cf74dc3db2239a4828b4760ef391d20`.
- Supplement manifest: `raw/github/paypal/paypal-ios/supplements/2026-11-15-7eb8f7b-763917b6/manifest.json`.
- Canonical linked attachment: `tracking/github/repos/paypal/paypal-ios/evidence-attachments/github-a24ad729631b9a2aa48d/attachment.json`.

## Reading and Grounding

- Completed: cumulative source/changelog read; changed retained source, new changelog entries, all ten supplemental files, affected prior code, release notes/comparison and relevant dependencies read. The full-mode expanded reading set is respected with the explicitly approved exception, not silently reduced to delta.
- Completed: all 334 prior/current/supplement file sizes, SHA-256 hashes and Git blob IDs verified; 144 common files unchanged. Current base capsule has 162 files / 382,507 bytes; supplement ten files / 24,339 bytes. Older upstream CHANGELOG history from 3.1.1 downward is byte-identical. Packet snapshot/markdown and comparison markdown/patch hashes pass; attachment verifier passes.
- Shared wiki context read by relevant section under approval; no claim to have read all shared logs or the entire upstream repository. Later main guides were not collected or used.
- Five located verbatim excerpts were extracted before edits and retained in the source's 3.2.0 Grounding excerpts section: VenmoClient async start (80), return handler (119), universal-links-only false (167); AnalyticsService event snapshot (83); AnalyticsEventData venmo_installed key (56).

## Workflow and Findings

1. Raw read/grounding completed before wiki edits.
2. Concept audit completed first: existing iOS SDK, Checkout and Vault concepts cover the new flow; updated those rather than creating duplicate concepts.
3. Added a version-qualified full additive source section, prepended snapshot/supplement references and updated package status. Existing version sections retained; the old generic no-native-Venmo statement explicitly qualified to its historical 2.0.1 evidence.
4. Company summary/reverse catalog updated; no new source, source_count remains 177.
5. Concept synchronization completed with source links and reciprocal request-contract contradiction warning.
6. No cross-company comparison warranted: this source does not substantively compare companies. Android lifecycle mentioned only as an API-boundary distinction, not assumed parity.
7. Contradiction check: unused request options/web-session comment flagged in source and concept. Old absence findings are version-qualified, not erased. Prior action-validation, licensing, vault and return cautions preserved.
8. Provider catalog updated; no root catalog change needed for an existing provider source.
9. Provider log and concise root log updated.
10. Scoped validation completed: seven typed wiki pages pass validate_wiki.py; catalog entries are unique, all new root-relative source/changelog evidence links exist, five located quotes are exact, historical source/changelog sections and raw-reference lists pass preservation checks, and git diff --check passes. Root log/provider catalog lack frontmatter by existing convention and are checked separately rather than reformatted. Global GitHub validation reports the same 13 unrelated historical structural errors, none for this repository; global validation is not clean. Lifecycle close follows separately.

The new separate VenmoPayments module uses OS HTTPS handling and a retained client. Successful opening is not callback/async completion; a return is required and absent returns have no automatic timeout/cancellation. One pending callback, missing origin/order binding and unused request options are recorded. Merchant validation and separate server authorization/capture remain required. The demo is illustrative, not production state verification. No Venmo vault/account-enablement claim follows.

Shared analytics copies event-time state, renames app_switch_url to url and adds venmo_installed. PayPal launch/return URL assignments are not evidence that Venmo populates the same URL field. MainActor/Sendable changes are not verified compiler or runtime results. Privacy metadata is not compliance proof.

No build/test, dependency/device/browser/payment execution, registry expansion, later-main-guide collection, commit or push is authorized or performed by this ingest.

## Lifecycle Close

`complete-ingest` succeeded. Item is `ingested` with approved mode `full` and its validated evidence attachment retained. Generated index records accepted `paypal-ios@3.2.0`, queue state ingested, next action wait and next due date 2026-11-22. No pending work items remain. Last wiki ingest date is 2026-11-15. The global validator result above remains a known unrelated baseline, not a global clean claim. Next gate: report findings and await scoped commit/push approval.
