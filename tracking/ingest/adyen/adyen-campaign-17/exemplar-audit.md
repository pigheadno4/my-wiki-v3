# C17 coordinator fixed sample audit

Date: 2026-10-18. Coordinator fully read the pinned raw and exact promoted source for each fixed sample.

- Standard: `docs-platforms-managed-payouts`, all 102 raw lines and promoted source. PASS: local country/currency, one schedule per currency, Adyen-contact configuration, settlement-delay boundary, standard/accelerated timing, cutoff/contract ETA and illustrative US limits retained. No guaranteed bank receipt inferred.
- Longest/schema heavy: `docs-platforms-reports-and-fees-balance-platform-accounting-report`, all 437 raw lines and promoted source. PASS: event/status grain, transfer/transaction and PSP identifiers, refund new transfer identity, booking/value dates and CET/CEST distinction, signed Received/Reserved/Balance movements, optional columns and do-not-use scheme fee fields retained. Top-up received/blank Transaction Id versus balance movement example tension preserved. No universal join or bank confirmation algorithm invented.
- Ordinary: `docs-platforms-internal-fund-transfers-on-demand-fund-transfers`, all 946 raw lines and promoted source. PASS: source/target balance accounts, support and access/capability prerequisites, one team review, received/pending versus booked, future date within 30 days and one attempt, failure/cancel boundary, two-sided webhooks retained. Transfer-instrument sentence and timezone default conflicts explicit.

No material partial/fail found; no audit expansion required. These checks validate historical documentation retrieval, not live provider behavior or financial operations.
