# Campaign 37 worker and reviewer dispatch contract

Status: exact five-job manifest approved by the user on 2026-09-07; active for Campaign 37 only.

## Instruction precedence

Read the shared [retrieval contract](../retrieval-source-contract-proposal.md). This file makes it executable for this pilot. Attach this file to every worker and reviewer prompt, including retries, alongside the unmodified trusted runtime order. Do not rely on routing_reason alone to inform reviewers.

For Campaign 37, this contract supersedes the semantic requirements in legacy generated preflight, the Campaign 23 playbook, and provider reminders that require exhaustive concept fan-out, unconditional per-POST idempotency expansion, schema completeness, cross-API analysis of omitted details, or full rereview of every factual correction. Identity, hashes, provenance, result schemas, three-to-five quotes, authority honesty, independent initial review, canonical ownership, and maximum attempts remain mandatory.

Persist the trusted runtime order normally. Do not edit its identity or schema values. The coordinator supplies this named semantic override in the dispatch prompt; no scheduler code or new configuration field is necessary for this bounded pilot.

## Worker prompt

You are the Campaign 37 source worker. Use Sol medium. Read the complete one assigned raw file and the retrieval contract. Generate a concise source that identifies what this evidence helps answer, preserves its central meaning and explicit consequential warnings, and locates detailed material in raw. Read related authority only when needed to support a claim you retain or bound a discovered relevant conflict. Do not infer guarantees from absent schema constraints. Do not copy general POST retry semantics merely because the endpoint uses POST.

Keep payloads, enums, examples, and ordinary schema details in raw with real section or schema-key locators. Mark an unread related document as navigation, not evidence. Avoid unsupported broad claims and lists of hypothetical unknowns. A known contradiction affecting retained claims gets a concise warning and evidence routes; resolving it is not required.

Propose the main concept's reciprocal source entry with its purpose. Add other routes when useful for discovery. Change concept prose only if a definition, principal flow, or important existing statement changes. Do not require a new semantic paragraph for every related topic.

Return the exact existing worker result shape, three-to-five located verbatim quotes, source candidate, and supported shared suggestions. Use existing allowed update kinds. Raw and canonical wiki files remain read-only to you. Historical candidate and review artifacts are not source evidence.

## Reviewer prompt

You are a different Campaign 37 reviewer. Use Sol high. Read the complete assigned raw for the first review. Apply the same retrieval contract as the worker. Check retained claim truth, correct purpose/object/version, consequential explicit warnings, discoverable central topics, exact evidence routes, and proposed shared updates.

For an omission blocker, name a concrete query, the misleading answer or wrong selection it causes, and why the existing raw route is inadequate. Do not require complete API-analysis coverage, expanded global rules, exhaustive concepts, or ordinary schema detail in source. An optional improvement is non-blocking.

Return all visible blockers together using the existing review result shape. Prefer the smallest adequate correction, including narrowing or removing unnecessary assertions. Set targeted retry scope when the unchanged-raw correction and affected suggestions are bounded, even if a fact's wording changes. Check the exact diff, evidence and context on retry. Use full review for central misunderstanding, broad meaning changes, changed evidence, or an impact that cannot be bounded. Do not waive a first review.

## Coordinator and query audit

Keep three dynamic agent slots, the existing runtime and receipts, and coordinator-only canonical writes. Apply approved concept navigation and any justified semantic update, then the approved source. Aggregate company/index/log/count writes at close. Mechanical corrections do not trigger a new semantic review unless they change meaning.

The three audit_job_ids preserve the existing manifest shape and identify detailed audit exemplars. Run the ten predetermined retrieval tasks in selection-review.md across all five pages as the single quality audit. It replaces the old separate three-page full-content audit for this pilot. A query evaluator starts from the named topic and wiki navigation, records its route, and reads raw when answering details; it is not asked to repeat whole-source semantic approval. Failed retrieval or wrong answers block closure until resolved or explicitly recorded as a failed pilot. Do not increase a source's scope merely to pre-answer a detail query that raw already answers.

Record outcomes, full/targeted reviews, elapsed time and retrieval misses in existing campaign artifacts. Run campaign-wide hash, link, count and capsule checks once after promotion, correcting concrete failures as needed.
