# Braintree C31 timing and bounded optimization opportunities

Twenty sources approved, first pass 14/20 (70% versus C30 60%), twenty initial full reviews plus six targeted reviews, zero repeated full reviews. Queries 40/40; typed validation 24/24. Operational runtime **44m21s**, versus C30 **24m09s** for ten pages. Average **2m13.1s/page** versus **2m24.9s/page**, about **8.2% faster per page**, not a major speedup. No thread-limit failure occurred; the five rolling child slots were shared across workers, reviewers and auditors.

Primary raw lines were 1,827 versus C30 2,197 (-16.8%) despite twice as many pages. Source words were 13,662 versus 6,960 (+96.3%); average source words 683 versus 696. The workload has sparse applicability/configuration pages but more cross-document conflicts, so this is not a controlled capacity-only comparison. Primary-line count excludes supporting full reads and instruction/navigation/receipt/report work.

| Observed milestone | UTC | Elapsed from 01:45:19 |
| --- | --- | --- |
| First five worker handoffs complete | 01:49:01 | 3m42s |
| All twenty initial worker handoffs complete | 02:17:57 | 32m38s |
| Last independent review handoff | 02:21:25 | 36m06s |
| Final promotion and source catalogs observed complete by | 02:22:26 | 37m07s |
| Shared logs observed complete by | 02:23:07 | 37m48s |
| Last query report analysis ended | 02:28:28 | 43m09s |
| Last query report received and inspected by | 02:29:17 | 43m58s |
| Mechanical validation and runtime close | 02:29:40 | **44m21s** |

Windows overlap and cannot be added. Initial worker completion improved per page (32m38s/20 versus C30 18m23s/10), but mandatory first reviews, corrections and ten query-auditor handoffs remain substantial. Query auditing overlapped remaining promotions, yet its last report arrived almost seven minutes after source catalogs were ready. Once that last report was inspected, close took 23 seconds. Further closure tests are not indicated.

Six bounded first-review corrections:

- Android custom client: retain its mandatory-webhook wording versus the Node Payment Context GraphQL alternative, without treating the alternative as universal replacement.
- iOS custom client: preserve the captured undefined start argument/omitted result body, supporting onboarding authority, method-currency tension and qualified server-notification alternatives.
- Boleto: retain GraphQL Requirements versus supported-list omission and family EUR versus BRL evidence tension.
- Trustly: retain family EUR/customer-confirmation funding wording versus method currency and post-settlement association.
- OXXO: supply the fully read supporting article's declared raw provenance/locator for an already retained currency warning.
- Alipay: retain the family EUR statement versus eight currency codes/CNY maximum and declare fully read supporting provenance.

These are actual authority/qualification/provenance issues, not requests to reproduce full schemas. A reviewer also initially misapplied supporting-provenance requirements on the iOS correction; the same reviewer corrected that false blocker before runtime acceptance, with no new attempt. A context restoration and shell-quoting correction added coordinator handling time; neither changed source evidence nor introduced infrastructure. A generated shared-catalog patch had duplicate target operations and was regrouped before any partial catalog write.

Small next-campaign suggestions, requiring approval rather than retrospective policy changes:

- Put already discovered **family-level conflicts** into concise provider/scope notes for relevant jobs (EUR-presentment, webhook/GraphQL alternatives, method support-list tension). Workers still fully read their primary and any factual supporting authority; notes flag risk, not substitute evidence. This may prevent repeated rediscovery in first reviews without a registry or new classifier.
- For another twenty-page campaign, consider **five query groups of four pages/eight questions**, retaining the same forty questions and full selected evidence reads. This halves auditor startups/handoffs and duplicated general-rule/index reading; rolling overlap and the five-slot ceiling remain. It does not batch worker ingestion or waive review.
- Draft sparse/configuration entries without repeating the same snapshot/execution caveat in Overview, takeaways and multiple warning blocks. Preserve one clear material warning plus exact locators. Do not rewrite these accepted sources merely to shorten them and do not impose a hard word cap.

Keep the existing pipeline and one campaign close. Do not add monitoring fields, test layers, worktrees or another model role. Twenty-page scope amortized close cost only modestly; increased page count alone is not a demonstrated solution to total latency.

Final reports/status observed written by 02:31:15 UTC: post-close documentation 1m35s; initialization-to-report-ready 45m56s. Final chat follows this milestone. No C31 commit, push or next campaign execution is authorized by this report.
