# Braintree C32 Extend selection

Status: COMPLETE — twenty approved sources, 16/20 first pass, twenty full plus four targeted reviews, no repeated full review. Five query groups passed 40/40; typed validation passed 26/26. Runtime closed at 2026-10-04T03:24:20Z (43m41s). Catalog 312 = 295 website + 17 GitHub. See quality-audit.md and retrospective.md. No C32 commit or push.

## Scope

Twenty previously unreferenced canonical website raws: nine Extend OAuth and eleven Forward API guides, preserving concrete SDK/version variants. Metadata-only selection; no product capability is inferred from unread raw. All twenty raw paths, URLs and target sources are unique, hashes match and source targets are absent. Baseline 292 sources = 275 website + 17 GitHub; twenty approved new sources would yield 312 = 295 website + 17 GitHub. Primary raw volume 2,477 lines, versus C31 1,827; different topic/length means timing is not a controlled A/B.

Five shared rolling child slots, excluding coordinator, across Sol medium workers, different Sol high initial reviewers and query auditors. Review-first allocation with the existing worker reserve; complete primary reads, 3–5 exact primary quotes, maximum three attempts, bounded targeted corrections and individual approvals. Coordinator alone writes canonical sources, concepts, catalogs, logs and runtime. No worktrees, reviewer waiver, role/model change or new infrastructure.

## Pinned pages

| Job | Primary lines | Exact raw path |
| --- | ---: | --- |
| `extend-forward-api-examples` | 609 | `raw/braintree/docs/guides/extend/forward-api/examples-2026-09-16.md` |
| `extend-forward-api-cryptography` | 211 | `raw/braintree/docs/guides/extend/forward-api/cryptography-2026-09-16.md` |
| `extend-forward-api-hyperwallet` | 172 | `raw/braintree/docs/guides/extend/forward-api/hyperwallet-2026-09-16.md` |
| `extend-oauth-client-side-ios-v7` | 157 | `raw/braintree/docs/guides/extend/oauth/client-side/ios/v7-2026-09-16.md` |
| `extend-oauth-access-tokens-node` | 150 | `raw/braintree/docs/guides/extend/oauth/access-tokens/node-2026-09-16.md` |
| `extend-forward-api-configuration` | 142 | `raw/braintree/docs/guides/extend/forward-api/configuration-2026-09-16.md` |
| `extend-forward-api-tokenization-support` | 130 | `raw/braintree/docs/guides/extend/forward-api/tokenization-support-2026-09-16.md` |
| `extend-forward-api-transformations` | 125 | `raw/braintree/docs/guides/extend/forward-api/transformations-2026-09-16.md` |
| `extend-oauth-client-side-android-v5` | 97 | `raw/braintree/docs/guides/extend/oauth/client-side/android/v5-2026-09-16.md` |
| `extend-oauth-reference` | 90 | `raw/braintree/docs/guides/extend/oauth/reference-2026-09-16.md` |
| `extend-oauth-connect-urls-node` | 86 | `raw/braintree/docs/guides/extend/oauth/connect-urls/node-2026-09-16.md` |
| `extend-forward-api-pgp-key` | 85 | `raw/braintree/docs/guides/extend/forward-api/pgp-key-2026-09-16.md` |
| `extend-forward-api-adyen` | 83 | `raw/braintree/docs/guides/extend/forward-api/adyen-2026-09-16.md` |
| `extend-oauth-client-side-javascript-v3` | 75 | `raw/braintree/docs/guides/extend/oauth/client-side/javascript/v3-2026-09-16.md` |
| `extend-forward-api-braintree-api-forwarding` | 72 | `raw/braintree/docs/guides/extend/forward-api/braintree-api-forwarding-2026-09-16.md` |
| `extend-oauth-configuration` | 52 | `raw/braintree/docs/guides/extend/oauth/configuration-2026-09-16.md` |
| `extend-forward-api-stripe` | 49 | `raw/braintree/docs/guides/extend/forward-api/stripe-2026-09-16.md` |
| `extend-oauth-overview` | 36 | `raw/braintree/docs/guides/extend/oauth/overview-2026-09-16.md` |
| `extend-oauth-shared-vault-node` | 32 | `raw/braintree/docs/guides/extend/oauth/shared-vault/node-2026-09-16.md` |
| `extend-forward-api-worldpay` | 24 | `raw/braintree/docs/guides/extend/forward-api/worldpay-2026-09-16.md` |

## Fixed query coverage — approved five groups

Each of twenty pages retains two questions, forty total:
1. Where is the exact named document type/object/provider example/platform/version source and pinned raw? Navigate root index → Braintree index → relevant concept → source → raw.
2. What central responsibility, transition or documented purpose does this page actually establish, and what material prerequisite/security/availability/authority qualification applies? If sparse or an unsupported notice, answer its actual scope/absence rather than filling it from siblings.

Type emphasis: OAuth overview/configuration/reference/connect/token/shared-vault/client pages distinguish connected-merchant consent, credentials, client/server responsibilities and scope/version. Forward configuration/transformation/cryptography/key/tokenization/example pages distinguish forwarding configuration or data treatment from executing/accepting/settling a payment. Named destination pages answer only the Braintree document's actual scope; no destination PSP-wide capability claim.

Approved groups of four pages/eight questions (all IDs prefixed `extend-`):
- A: oauth-overview; oauth-configuration; oauth-reference; oauth-connect-urls-node.
- B: oauth-access-tokens-node; oauth-shared-vault-node; oauth-client-side-javascript-v3; oauth-client-side-android-v5.
- C: oauth-client-side-ios-v7; forward-api-configuration; forward-api-braintree-api-forwarding; forward-api-examples.
- D: forward-api-transformations; forward-api-cryptography; forward-api-pgp-key; forward-api-tokenization-support.
- E: forward-api-adyen; forward-api-hyperwallet; forward-api-stripe; forward-api-worldpay.

This only halves auditor starts/handoffs from C31's ten groups. It does not reduce questions, complete evidence reads, gap sweeps, link checks, initial reviews or per-source worker isolation. Groups overlap promotion only after all four relevant routes are ready; each auditor occupies one of the same five slots. Three manifest audit IDs remain exemplars, not another semantic audit layer.

## Coordinator-supplied role notes

Read CLAUDE.md, rules/ingest.md, rules/psp/braintree-ingest.md and adopted rules/psp/metronome-ingest.md. Workers/reviewers start with rules/ingest-roles.md plus trusted attempt input and these concise notes; auditors retain CLAUDE/query rules reading.

Start root index → braintree-index → payment-platform/auth or another relevant concept selected by full-read audit. Do not automatically merge Extend OAuth with Braintree Auth solely because both use OAuth. Existing source owners remain separate. A genuine Forward API concept gap may justify a new concept, but metadata selection does not predetermine its facts.

Braintree-hosted Adyen, Stripe, Hyperwallet and Worldpay guides remain Braintree sources, not those providers' official API ownership. Forwarding and tokenization are not proof of payment execution, current destination support, authorization, settlement or funding. Preserve actual permissions, merchant/platform roles, client/server scope, SDK/version, secret-handling requirements, encryption/key qualifications and any lifecycle/security warnings found in the full raw. Treat examples as examples. Sparse pages may contain only redirect/unavailability notices.

Keep material discovered conflicts visible. C31's EUR-presentment and webhook/GraphQL tensions apply to Local Payment Methods, not automatically to this unrelated family; investigate only if a retained claim crosses that boundary. Existing account-permission versus Forward API scope tension is a known navigation lead, not evidence until the relevant authority is fully read.

Exact dated navigation targets must exist. Supporting factual authority must be fully read and declared in both raw_files and Raw Sources; unread targets go under Related raw API references. The 3–5 runtime quote slots use primary raw only. Reverse raw links derive from raw_files, never raw edits. Default concept proposals are exact-anchor purpose-only reciprocal links.

Avoid repeating the same snapshot/execution caveat across Overview, takeaways and several warnings. State each necessary qualification clearly once where useful; retain every material warning, no hard word cap. Routine field tables/code examples receive verified raw locators, not expanded specifications.

## Close and timing

Dispatch immediately after persisting orders; fill free eligible slots before routine promotion/report prose. Serial concept-before-source promotion, aggregate company/index/log/count once. One final close checks all candidates, hashes, canonical URL/ownership, evidence/navigation links, approved updates, reciprocal routes, unique exhaustive catalogs and recursive counts. Validate touched typed pages once; no code/rule changes means no unrelated unit suite. Query reports contain direct answers/routes/locators/verdicts and shared extra-read/gap notes once; no polishing.

Compare total and per-page runtime, first-pass rate, full/targeted retries, raw volume, source words and actual UTC milestones with C31. No additional timing fields or monitoring subsystem. Execution rechecks these preparation pins and baseline before runtime initialization.

Preparation is not execution, collection, GitHub work, commit or push authority.
