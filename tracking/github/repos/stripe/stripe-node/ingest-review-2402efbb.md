# Stripe Node 22.6.1 ingest review

- Item: `github-2402efbbc4962288beb9`.
- Boundary: `stripe@22.6.0` -> `stripe@22.6.1`, SHA `9f82c466c0a5913906ab1bf39790edd4d231ee5d`.
- User approved delta ingest inline and explicitly approved focused reading for this release. No commit/push authorization.

## Checklist

- [x] Evidence reading and grounding completed under the approved exception.
- [x] Concept audit/update before source edits: existing Stripe Node SDK concept; no new concept needed. Generated checkout contracts unchanged.
- [x] Append cumulative source and separate changelog; preserve history.
- [x] Company and reciprocal concept coverage; no new source/count change. No provider-wide count recalculation claimed.
- [x] Comparison and contradiction check: no cross-company comparison; prior warnings preserved, no claim that they are fixed.
- [x] Provider index and provider/root logs; unrelated changes preserved.
- [x] Validate, complete this item, and verify terminal state: ingested/delta; 22.6.2 remains awaiting approval.

## Reading boundary

Both cumulative wiki pages read completely. All changed retained implementation files, README, package/version records, release notes and the full 1,093-line comparison diff read. Prior affected implementation is reviewed through that diff. Snapshot inventories checked mechanically: both snapshots contain 68 files and every size/SHA256 matches; 13 modified and 55 unchanged. Historical changelog from the 22.6.0 heading onward is byte-identical (SHA256 `7a2b761e0a10221abd646fa0b9ffb393960ae9f1260f2a2a804bafdfe2897978`). New changelog entry read; unchanged history not reread. Node ESM, workflow and test changes are comparison-only evidence, not complete retained files. No upstream SDK/test execution or live integration proof.

## Grounding before wiki edits

Paths below are relative to the current snapshot's `files/` directory.

1. `src/platform/PlatformFunctions.ts`, uuid4 comment: "Deliberately throws rather than degrading to `Math.random()`."
2. `src/RequestSender.ts`, _defaultIdempotencyKey comment: "our uuid4 function needs to be cryptographically secure, but idempotency key just needs to be unique".
3. `src/utils.ts`, validatePath condition: `typeof path !== 'string' ||` followed by `!path.startsWith('/') ||` and `path.startsWith('//')`.
4. `src/StripeResource.ts`, before query/body split: "Coerce int64_string/decimal_string fields in request data".
5. `README.md`, Open and Closed Enum: "Many of Stripe API enums are open, meaning Stripe may add new values even on older API versions."

## Findings

- Secure UUID multipart boundaries replace Math.random-derived boundaries. Missing secure randomness fails upload generation; only automatic idempotency keys retain a fallback. Node uses imported crypto.randomUUID, not global crypto.
- MIME Content-Type CR/LF becomes spaces. Name/filename quote and CR/LF escaping already existed; do not attribute all header escaping to this patch.
- Shared request sink rejects non-string, missing-leading-slash and double-leading-slash paths before auth/network work; thin-event fetchEvent encodes the ID. This is a bounded guard, not full URL validation or a webhook authentication replacement.
- Schema coercion moves before GET/DELETE query/body separation. Decimal/int64 schema fields can serialize correctly in queries; bodies stay null. rawRequest does not acquire new non-POST params support.
- OtherString documentation changes only; generated checkout resources, API pin `2026-08-26.dahlia`, OpenAPI `v2442`, Node minimum and runtime dependencies unchanged.
- Existing handler-context, parser-entrypoint and retry-default caveats remain historical; this patch does not establish their resolution. No cross-company comparison warranted.

## Verification

- `validate_wiki.py`: five edited frontmatter-bearing pages pass. Provider index and root log retain their pre-existing non-frontmatter format.
- `validate_github_collection.py`: passes before and after completion, 121 snapshots / 106 release records / 63 comparisons / 120 work items.
- Local Markdown evidence links resolve. Previous changelog entries and retained-history sections match HEAD. Company/provider catalog entries remain unique; source count unchanged.
- Both snapshot file inventories pass SHA256/size checks; no raw files modified. `git diff --check` passes.
- No upstream SDK build/tests, live payment execution, commit or push. Unrelated workspace changes left untouched.
