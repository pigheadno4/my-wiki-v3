# Braintree C29 five-slot timing comparison

## Outcome

Ten approved sources; first pass 8/10; ten full plus two targeted reviews; no full retry. Fixed query audit 20/20, typed validation 16/16, zero automatic formatting or canonical source/concept repairs. Five shared child slots ran successfully with immediate worker/reviewer replacement and no batch barrier or thread-limit failure.

| Observed stage | UTC milestone | Elapsed from initialization |
| --- | --- | --- |
| Initialization | 15:14:02 | 0 |
| First five long-page worker handoffs complete | 15:20:29 | 6m27s |
| All ten initial worker handoffs complete | 15:29:19 | 15m17s |
| Last independent review handoff | 15:33:13 | 19m11s |
| Final approved source promotion observed | 15:33:28 | 19m26s |
| Shared catalog aggregation | 15:34:15 | 20m13s |
| Last fixed query handoff | 15:35:13 | 21m11s |
| Mechanical checks and runtime close | 15:36:20 | **22m18s** |

Workers, reviews, bounded corrections, promotions and queries overlap; these elapsed milestones are not additive stage costs. Final review handoff to final promotion was 15s. Last query handoff to close was 1m07s. Final report/status writing occurs after runtime close and is excluded from that duration; initialization-to-user-handoff is therefore slightly longer.

Final reports/status were observed written by 15:37:52 UTC: post-close documentation 1m32s, initialization-to-report-ready 23m50s. The final chat response follows this milestone; it is not included in runtime closure.

## Comparison with C28

| Metric | C28 | C29 |
| --- | ---: | ---: |
| Approved pages | 10 | 10 |
| Nominal shared child budget | 3 | 5 |
| Primary raw file lines | 1,586 | 2,130 |
| Source words | 5,863 | 5,957 |
| First-pass approvals | 9/10 | 8/10 |
| Full / targeted reviews | 10 / 1 | 10 / 2 |
| Query answers passed | 20/20 | 20/20 |
| Initialization → last review handoff | 32m58s | 19m11s |
| Runtime close | 38m07s | **22m18s** |
| Last query handoff → close | 3m00s | 1m07s |

Observed runtime saving: **15m49s (41.5%)**. C29 had 34.3% more raw lines, 1.6% more source words and one additional targeted correction. This is encouraging throughput evidence, not a controlled capacity-only A/B: topics differ and C28 lost capacity after a coordinator timing-only follow-up reactivated a completed thread. C29 avoided that handoff mistake and shortened coordinator close work as well as increasing the shared budget.

## Remaining small opportunities

- Keep five shared rolling slots for the next separately approved comparable campaign; do not increase again or add a scheduler merely from this single result.
- First-pass weakness was one duplicated material-warning omission, not formatting or broad misunderstanding. Keep the existing bounded subject/condition/action check focused on explicitly stated consequences; no new provider invariant or memory subsystem is necessary.
- Query report writing still followed reported analysis end by 35–74s (A 59s, B 68s, C 74s, D/E 35s); the sparse upgrade review's decision-to-validated-artifact interval was 38s. These are observed handoff windows, not instrumented pure writing costs. Broad advanced-options questions led A/B to enumerate many details. Future approved questions can target one consequential boundary plus navigation, and reports can give compact answers/locators rather than retell option inventories. Preserve full raw reads and evidence quality.
- One generated promotion patch initially repeated the same concept target in two operations; apply_patch rejected it without changing files. Grouping updates by target resolved it. A catalog label was narrowed before validation to avoid implying the sparse upgrade raw provides an alternative procedure. Neither changed approved source facts or consumed a worker/reviewer retry.
- Existing candidate/hash/link/catalog/count checks completed once. Preserve recursive GitHub-aware enumeration and separate evidence/navigation; no further validation layer is indicated.

No commit, push, collection, GitHub task or next campaign is authorized by this report.
