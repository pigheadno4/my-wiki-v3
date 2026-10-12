# Adyen Campaign 01 results

- Complete: 50/50 approved sources; 100/100 fixed queries pass after corrections.
- Initial independent review: 40/50 (80%). Ten attempt-2 targeted reviews; 50 first full reviews, zero repeated full reviews, zero terminal rejections.
- Query corrections: token location split between Sessions and Payments; third-party 3DS challenge-indicator field-name conflict; JWE EC-certificate/RSA-algorithm example conflict. Independently targeted-verified; original receipts/raw retained.
- Mechanical corrections: six concept category-enum values. Nine coordinator repairs total = three bounded semantic corrections plus six metadata corrections.
- Outputs: 50 website sources; 17 touched concepts (14 new, three existing); Adyen catalog/company total 64 sources = 50 website + 14 GitHub. Existing GitHub history and other tasks' changes preserved.
- Structural close: 50 raw hashes, exact provenance, reciprocal links, unique catalog entries and count PASS. Typed validation: 69 files PASS, then changed-scope checks for metadata/warning/log corrections PASS. No code/rule changes or full unit suite.
- Started 2026-10-10T07:58:25Z; completed 2026-10-11T14:33:16Z. Wall span 30h34m51s includes usage-limit and turn interruptions and is not processing throughput.
- Worker receipt span: 2026-10-10T08:01:54Z to 2026-10-11T14:20:44Z. Review receipt span: 2026-10-10T08:04:26Z to 2026-10-11T14:26:45Z. These stages overlap and include interruption/handoff delay; exact active model time cannot be recovered reliably. Do not sum them or compare them to uninterrupted prior campaigns.
- Optimization opportunities evidenced here: 80% initial pass is substantially better than the early pilots, but raw-internal example conflicts still need explicit warnings. Keep examples as detail locators; don't silently turn them into contracts. Existing category enum can be enforced mechanically during handoff without adding a new review layer; no validator changes were made in this campaign.
- No collection/refresh, API Explorer ingestion, GitHub ingestion, live payment test, commit or push. Next action is scoped commit review, only with approval.

Evidence: `monitor.md`, `jobs.json`, per-attempt receipts/reviews, `query-audit-a.md` through `query-audit-j.md`, correction reports C/H/I, `close-validation.md`, and `recovery-notes.md`.
