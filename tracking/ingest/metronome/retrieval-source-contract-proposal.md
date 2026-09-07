# Retrieval-oriented source contract proposal

Status: reviewable design; not an active campaign authorization or replacement for current rules.

## Objective

Produce an accurate retrieval entry point that helps a query locate the right immutable evidence. A source is not a complete implementation specification. Quality means truthful retained claims, discoverable central topics, useful evidence routes, and explicit warnings against material misuse.

Raw immutability preserves provenance, not upstream correctness or current applicability. Queries about implementation details must read the relevant raw snapshot and check its version and scope. Known conflicts must remain discoverable.

## Worker contract

Read the entire assigned raw once. Reuse the existing candidate, quotes, suggestions, and receipt format. Retain the existing three-to-five evidence excerpts; they ground retained claims rather than impose a content quota.

Classify sections while reading; do not create a separate classifier or persisted segmentation layer:

| Raw section role | Source treatment |
| --- | --- |
| Purpose, object, intended use | Summarize accurately; retain useful search vocabulary |
| Main capability or transition | Explain briefly enough to choose the correct evidence |
| Explicit deprecation, destructive effect, consequential limit | Preserve a short warning when omission could cause wrong selection or misuse |
| Fields, enums, examples, error tables, setup steps | Name the detail category and route to the exact raw; do not reconstruct it |
| External or API-wide authority | Link to the relevant authority when useful; do not copy its full semantics into every source |

The source contains purpose, a small set of useful facts, essential warnings, raw-detail navigation, related routes, and canonical/raw provenance. These are semantic responsibilities, not mandatory long sections or numeric caps.

Do not infer organization-wide completeness from "your", guarantees from examples, or runtime behavior from omitted schema declarations. If such a detail is unnecessary for retrieval, omit the assertion rather than enumerate every unknown.

Cross-source reading is required when needed to substantiate a retained cross-source claim or investigate a discovered conflict affecting that claim. It is not an exhaustive search of every adjacent API. A known conflict may be recorded as a short scoped warning with both evidence routes; the source need not solve it. Unread related pages provide navigation only.

## Concept and link contract

Choose the concept that best represents the page purpose and propose a reciprocal source link with a one-line purpose. Additional concept routes are warranted by retrieval value, not incidental fields. Navigation links need not create duplicate semantic paragraphs.

Change concept prose only when this source changes its definition, principal flow, or an important existing claim. A navigation-only source is still discoverable through its main concept and exhaustive company/provider catalogs. The coordinator checks intended reciprocal routes, duplicate entries, and targets.

Retain `raw_files` and exact path-qualified `[[raw/...]]` links without modifying raw. Reverse raw-to-source lookup is derived by scanning `raw_files`; it does not require writing backlinks into raw. Detailed categories may use a verified heading anchor; when raw is one OpenAPI block, use the exact file plus a schema key or operation locator instead of inventing anchors.

## Reviewer contract

For the first pilot, retain a different reviewer reading the complete raw. Review against this same retrieval contract, not complete API-analysis coverage.

Block only when a retained claim is false or materially misleading; the purpose/object/version is misidentified; a central topic cannot be found; a material explicit warning is missing; a known conflict invalidating a retained claim is hidden; or a required evidence/navigation route is incorrect or absent.

Every omission blocker must state a concrete query, the wrong selection or misleading answer it would cause, and why the existing raw route does not adequately cover it. "Potentially useful for integration" alone is insufficient.

Ordinary schema detail remaining in raw, an additional tangential concept, exhaustive unknowns, optional global-rule expansion, and stylistic preferences are non-blocking. Reviewers may suggest enrichment without requiring it for approval. Accuracy remains mandatory for every claim the worker chooses to retain.

## Correction and review scope

Prefer the smallest adequate correction: remove unnecessary detail, narrow an assertion, add a warning, or repair a route. A correction need not expand the source into an implementation guide.

Use existing targeted review when the original raw hash is unchanged, prior findings define the correction, and the diff has a bounded effect. Check the edited claims, their evidence and surrounding context, affected shared suggestions, and links. A semantic wording correction is not automatically a full retry.

Repeat full review when the source's central purpose, object, lifecycle, or evidence basis was misunderstood; corrections affect meaning throughout the document; evidence changes; or the affected scope cannot be bounded. An unchanged hash alone never proves that targeted review is sufficient.

## Five-page validation proposal

Select five previously uningested pages spanning an API read, API list/schema, API mutation, concept/guide, and integration guide where the remaining corpus permits. Record exact pages in a later manifest. Use current models and dynamic slots so the contract change can be assessed without simultaneous model or scheduler changes.

For each page define one navigation question and one detail question before execution. Evaluate whether the concept/source identifies the right evidence and whether reading that evidence answers the detail question accurately. Include a scope or misuse boundary among the five detail questions. Record extra searching when the source route is insufficient.

Keep mechanical checks across all five pages. The query evaluation serves as the pilot's quality audit; do not add another audit covering the same questions. Observe first-pass approval, full and targeted reviews, total elapsed time, and retrieval misses using existing evidence files. Compare with Campaigns 34-36 cautiously because page difficulty differs.

Proceed only if retained claims and retrieval tasks pass. Better first-pass acceptance alone is not success. Faster ingest accompanied by misleading retrieval or substantially harder queries requires revision. Five pages provide calibration, not a cross-PSP production guarantee.

## Implementation boundary

Before execution, align the applicable worker and reviewer instructions together: remove mandatory per-endpoint global-rule expansion, exhaustive concept fact propagation, and automatic full rereview for every semantic correction in this pilot's scope. The current provider rules and scheduler preflight still impose those requirements; this proposal alone does not override them.

Use existing tracking and runtime structures. Preserve old sources and campaign evidence. No bulk rewrite, new registry, classifier, scheduler, or separate monitoring system is needed. Future refreshes can adopt the accepted contract incrementally while retaining historical raw provenance; a raw change should not force expanded analysis of details the source never claims.
