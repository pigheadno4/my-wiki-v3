# Adyen C01 recovery notes

- Campaign started 2026-10-10T07:58:25Z. Execution was interrupted by account usage limits, then resumed on 2026-10-11; a later turn interruption also stopped unfinished child tasks.
- Accepted completed external artifacts before redispatching. Approved jobs were not redrafted. Existing pending attempt orders were reused for interrupted first reviews/workers; recovery child names differ from original persisted assignment labels.
- No usage-reset credits were consumed and no model/backend fallback was introduced. The approved Sol medium worker / Sol high reviewer settings were retained.
- Query audit C identified one retained-claim ambiguity in token payments. Coordinator applied the auditor's exact bounded replacement separating `/sessions` shopper context and client-side stored-method selection from `/payments`' explicit token field. The unchanged-hash context check is retained in `query-audit-c-correction.md`; original approved receipt remains historical evidence, not silently rewritten.
- Filesystem timestamps include interruptions and artifact-receipt delay. Campaign wall time is not uninterrupted processing time; do not present it as a throughput benchmark or infer exact model stage duration from receipt times.
- No raw files, GitHub evidence, collector, scheduler, validator or rule schemas were changed. Other sessions' dirty changes were preserved. Commit and push require separate approval.
