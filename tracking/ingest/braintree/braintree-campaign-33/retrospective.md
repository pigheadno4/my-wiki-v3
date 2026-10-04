# Braintree C33 timing and bounded optimization

Runtime **42m11s**, versus C32 **43m41s**: **1m30s / 3.4% faster**, not a substantial speedup. Twenty sources; first pass 15/20 (75%, versus 80%); twenty initial full reviews plus five targeted reviews, no repeated full review. Queries 40/40 and typed validation 25/25.

Primary volume increased from 2,477 to 3,937 lines (+58.9%). Accepted sources decreased from 12,437 to 11,979 words (-3.7%), average 599 words/page. Content, supporting authority reads and a new concept differ, so this is not a controlled A/B or proof of scheduling causality.

| Observed milestone | UTC | Elapsed from 03:41:36 |
| --- | --- | --- |
| First five worker handoffs complete | 03:48:15 | 6m39s |
| All twenty initial worker handoffs reported complete | 04:14:29 | 32m53s |
| Last independent review completed, reviewer-reported | 04:17:31 | 35m55s |
| Final promotion/company/source catalogs observed ready | 04:19:05 | 37m29s |
| Last query analysis ended, auditor-reported | 04:21:12 | 39m36s |
| Last query report received and inspected by | 04:23:05 | 41m29s |
| Logs, mechanical checks and runtime close | 04:23:47 | **42m11s** |

Windows overlap and must not be added. All initial worker handoffs were 1m08s later than C32, while the last review was 2m19s earlier. Catalog-to-close tail was 4m42s versus 4m22s: the dispatch-order groups started earlier, but did not remove the final query tail. Last query analysis-to-inspection took 1m53s, including report creation and handoff; report prose remains a cost.

Five bounded retries repaired material scope rather than routine completeness: Stripe capture deadline and charge-reconciliation conflict; EBANX Nigeria partial-capture conflict; dLocal pending-result duplicate retries, Turkey decimals conflict and main route; Forward endpoint-name/config lookup and related navigation; tokenization-error example versus response-schema wording. No broad misunderstanding required another full review.

Keep optimization small: use the existing subject/condition/action pass to catch example-versus-contract wording and contradictory feature/country rows while reading. Do not add a new registry or sweep every adjacent page. A concept created mid-campaign can change routing expectations: preserve already approved relevant routes rather than retroactively requiring all prior sources to move, and use the dedicated hub for subsequently assigned jobs. Ordinary malformed or sparse reference content needs one concise gap notice, not repeated absence inventories.

Query reports still averaged roughly fifty lines for eight questions with many repeated negative-outcome caveats. Next separately approved round can emphasize the existing compact-report rule: one shared authority boundary, page-specific material exceptions and direct answers only. No question, full evidence read, first independent review or link check is waived. Avoid new performance infrastructure or a new quality layer.

C33 is complete locally; commit/push and another campaign require explicit approval.
