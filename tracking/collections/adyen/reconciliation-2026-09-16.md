# Adyen raw collection reconciliation — 2026-09-16

Scope: documentation raw only. No ingestion or GitHub evidence changes. No new network requests during this audit.

## Counts

- Original collection target count: 2,913 (2,550 docs + 363 API Explorer).
- Local snapshots: 2,912, representing 2,911 distinct Source URLs.
- General documentation: 2,549 snapshots; API Explorer: 363 snapshots.
- One URL (`about-our-customer-area.md`) has two dated versions.
- September 16 targeted retry: 6 attempted, 4 recovered, 2 still failed.
- Body screen: 27 API Explorer snapshots contain only a single title line. These are preserved responses, **not complete documentation** and **not ingest-ready**.
- Therefore 2,884 distinct URLs have bodies beyond the detected title-only stubs. This mechanical screen is not full semantic validation of those pages.
- Unresolved quality/collection items: 27 title-only responses plus 2 fetch failures. Do not report complete corpus coverage.

## Verified locally

- All 2,908 migrated snapshots match the SHA-256 recorded in `raw-layout-migration-2026-09-15.json`.
- All 4 retry successes match their recorded SHA-256 and Source URL metadata.
- Every raw destination matches the recorded Source URL and collection date.
- Both collection manifests' raw wikilinks resolve. Migration entries plus retry successes account for every local Adyen documentation snapshot.
- The dated original manifests and retry results retain their historical outcomes. This report qualifies the older download-success counts rather than rewriting history.
- Retry `candidate-*.md` files are duplicate staging copies and are intentionally excluded from the data commit; canonical raw and result hashes are retained.

## Fetch failures retained

- `https://docs.adyen.com/payment-methods/boleto-bancario/android-component.md` — read timeout on September 16 retry.
- `https://docs.adyen.com/scripts/docs-mirror.md` — HTTP 404 on September 16 retry.

## Title-only API responses — exclude from ingestion pending resolution

- `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_FUNDS_BELOW_THRESHOLD/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_HOLDER_CREATED/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_HOLDER_PAYOUT/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_HOLDER_STATUS_CHANGE/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_HOLDER_STORE_STATUS_CHANGE/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_HOLDER_UPCOMING_DEADLINE/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_HOLDER_UPDATED/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/ACCOUNT_HOLDER_VERIFICATION/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/COMPENSATE_NEGATIVE_BALANCE/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/DIRECT_DEBIT_INITIATED/2026-09-15.md`
- `raw/adyen/api-explorer/Notification/latest/post/REFUND_FUNDS_TRANSFER/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/ACH_NOTIFICATION_OF_CHANGE/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/CANCEL_OR_REFUND/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/DISPUTE_DEFENSE_PERIOD_ENDED/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/ISSUER_RESPONSE_TIMEFRAME_EXPIRED/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/MANUAL_REVIEW_ACCEPT/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/MANUAL_REVIEW_REJECT/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/NOTIFICATION_OF_CHARGEBACK/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/NOTIFICATION_OF_FRAUD/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/PREARBITRATION_ISSUER_WITHDRAWN/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/REFUND_NOT_CLEARED/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/REFUND_WITH_DATA/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/REQUEST_FOR_INFORMATION/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/SCHEME_ARBITRATION_LOST/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/SCHEME_ARBITRATION_WON/2026-09-15.md`
- `raw/adyen/api-explorer/Webhooks/latest/post/VOID_PENDING_REFUND/2026-09-15.md`

## Evidence records

- [September 14 manifest](../../../scripts/manifests/adyen-2026-09-14.md)
- [September 15 manifest](../../../scripts/manifests/adyen-2026-09-15.md)
- [Migration mapping](raw-layout-migration-2026-09-15.json)
- [Retry summary](retry-2026-09-16T135143Z/summary.json)
- [Retry page results](retry-2026-09-16T135143Z/results.jsonl)
