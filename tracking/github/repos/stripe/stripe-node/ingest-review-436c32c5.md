# Stripe Node 22.6.0 ingest review

- Item: `github-436c32c59360977be8fa`.
- Boundary: `stripe@22.5.0` -> `stripe@22.6.0`, SHA `2f64e7ac920bd6863fdb851f4fb1fcc6190d963f`.
- User approved full mode, inline execution, a one-time focused-reading exception, and exact-SHA supplements for `src/StripeEventNotificationHandler.ts` and `src/V2Coercion.ts`. No commit/push approval.
- Snapshot remains immutable. Supplement `2026-09-21-2f64e7a-f49df03e` contains two files / 13,497 bytes and is linked through the canonical work-item attachment.

## Checklist

- [x] Finish focused evidence review and grounding; full-mode effective reading list checked under the approved exception.
- [x] Concept audit and updates before source edits: Stripe Node SDK, Payment Intents and Checkout. No new concept required.
- [x] Append cumulative source and separate changelog; preserve older versions.
- [x] Company and reciprocal concept updates; no source added/removed and company count unchanged. Source/changelog each occur once in company/provider catalogs. No provider-wide count recalculation claimed.
- [x] No cross-company comparison warranted. Context comment versus implementation and release-note versus body-error handling boundaries recorded; older contradictions preserved.
- [x] Provider index and logs; unrelated shared-file work preserved.
- [x] Validate, complete this item, and validate terminal state: ingested/full; 22.6.1 and 22.6.2 still awaiting approval.

## Reading boundary

Both cumulative wiki pages read completely. Both 68-file snapshot inventories verified by size/SHA256; 33 modified and 35 unchanged files. Changelog content from the 22.5.0 heading onward is byte-equivalent as decoded UTF-8 text. Changed runtime behavior, affected dependencies and prior diff context are reviewed; both supplemental files read completely. Generated resource changes are reviewed as hunks under the approved exception, with whitespace/OtherString-only hunks mechanically distinguished. Tests, generated test fixtures, lockfile and unrelated non-checkout domains are not implementation authorities for this ingest. No claim of reading the entire upstream repository or running its SDK/tests.

## Grounding

1. `files/src/RequestSender.ts`, `_defaultIdempotencyKey`: "Key every POST, including when maxNetworkRetries is 0."
2. `files/src/net/FetchHttpClient.ts:146`, abort timeout guard: "The signal stays armed after the headers arrive, so aborting it also".
3. Supplemental `StripeEventNotificationHandler.ts`, `handle`: "set before parsing, so that even a failed parse locks out registration."
4. Supplemental `V2Coercion.ts`: "An unrecognized discriminator passes through untouched" (comment continues on the same line).
5. `files/src/resources/PaymentLinks.ts`, update params: "There must be at least 1 line item with a recurring price to use this field." (application_fee_percent documentation).

## Findings to retain

- API pin becomes `2026-08-26.dahlia`; OpenAPI `v2442`. Keep all prior package/API identities.
- Typed thin-notification handler, one callback per type and one pre-hook; registration locks before parsing. No built-in durable deduplication or HTTP acknowledgement. Synchronous verification inside async handle limits async-only crypto compatibility.
- Source-level context risk: shallow callback client shares resources and RequestSender bound to the original client. Do not infer automatic event-context routing from its copied `_api`. Event fetch helpers explicitly pass context. No packaged-runtime reproduction claimed.
- Response-body timeouts map to StripeConnectionError; non-timeout body failures and invalid JSON remain StripeAPIError. No new body-read automatic retry. Fetch streaming releases the timer; Node stream timeout changes the surfaced error.
- V1 POST automatic idempotency now applies even with zero configured retries. Application retries still need a stable business-operation key.
- V2 discriminated union coercion throws for missing/non-string request discriminator; unknown strings pass through. This is not full schema validation or repair for numbers already rounded by JavaScript.
- Checkout funding-type restrictions; required-but-nullable response allowlists (request fields remain optional); Payment Links update-time Connect fields; Billie and cancellation feedback typings; expanded open enums and narrowed WebhookEndpoint enabled_events types.
- New sample marks deduplication before processing and omits HTTP response completion: illustrative, not production-ready.

## Verification

- `validate_wiki.py`: seven touched frontmatter-bearing pages pass. Including the provider index reports its pre-existing missing YAML frontmatter; left unchanged. Root log also retains its existing non-frontmatter format.
- `validate_github_collection.py`: passes before and after completion, 121 snapshots / 106 release records / 63 comparisons / 120 work items, no structural errors.
- Local Markdown evidence links resolve; old changelog entries and retained-history paragraphs match HEAD; company/provider source entries remain unique.
- `git diff --check` passes. Other tasks' code/rules/Braintree/shared-file changes are not this ingest and were not reverted or staged.
- No SDK build, upstream tests, runtime reproduction, commit or push performed.
