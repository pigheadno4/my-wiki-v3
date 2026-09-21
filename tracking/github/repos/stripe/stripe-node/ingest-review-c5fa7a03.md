# Stripe Node 22.6.2 ingest review

- Item: `github-c5fa7a0352b6764a7481`.
- Boundary: `stripe@22.6.1` -> `stripe@22.6.2`, SHA `d9d092737b4a891f0beaf47c26c222972a4c7b0f`.
- User approved inline delta and focused reading of changed behavior with mechanical checks for unchanged content. No commit/push authorization.

## Checklist

- [x] Review and grounding: full Webhooks implementation, six changed retained examples, complete diff, release records, packet and existing cumulative wiki context.
- [x] Concept audit/update before source edits: existing Stripe Node SDK concept; no new concept required.
- [x] Append source/changelog without removing history.
- [x] Company, concept reciprocity, comparison/contradiction checks: no new source/count change or cross-company comparison; historical caveats retained.
- [x] Provider index and logs; unrelated edits preserved.
- [x] Validate and complete only this item: ingested/delta.

## Reading and grounding

Both snapshots contain 68 files; all sizes/SHA256 verified. Eleven modified, 57 unchanged. Core, package.json and VERSION differ only by 22.6.1 -> 22.6.2 substitution; prior contents were read during 22.6.1. Historical changelog from the 22.6.1 heading onward is byte-identical. Current Webhooks.ts and all six retained changed examples read fully. Prior changed behavior and excluded files reviewed through the complete diff. No whole-repository read or SDK execution claimed.

Grounding quotes, relative to current snapshot files:

1. `src/Webhooks.ts`, both signature methods: `if (!secret) {`.
2. `src/Webhooks.ts`, error message: "No webhook secret value was provided. It should start with `whsec_`".
3. `examples/webhook-signing/express/main.ts`: `process.exit(1);` after the missing-secret check.
4. `examples/webhook-signing/nextjs/pages/api/webhooks.ts`: `res.status(500).send('Webhook secret is not configured');`.
5. `examples/webhook-signing/nextjs/app/api/webhooks/route.ts`: `{status: 400}` in the catch that also handles the configuration error.

## Findings

- Sync/async signature verification reject falsy secrets before HMAC calculation, after payload/header parsing. Malformed payload/header errors can therefore precede the missing-secret error; higher-level default crypto-provider setup can also fail earlier.
- No prefix enforcement or whitespace trimming: whitespace-only/non-prefixed strings are not rejected by the new guard alone. Existing signature verification still applies. WithoutVerification paths are unchanged.
- Express/Koa/snippet exit on missing environment configuration; NestJS throws from config; Next.js Pages returns 500, App Router routes it through its 400 catch. Not a uniform startup check or response contract.
- API pin, generated checkout files, runtime dependencies and prior verification/tolerance behavior unchanged. Existing historical caveats retained. CI publish configuration is maintenance-only.

## Verification

- Five edited frontmatter-bearing wiki pages pass validate_wiki. Provider index/root log keep their existing non-frontmatter format.
- validate_github_collection passes before and after completion: 121 snapshots, 106 releases, 63 comparisons, 120 work items.
- Source/changelog local evidence links resolve; previous changelog entries and retained-history section match HEAD. git diff --check passes.
- No raw modification, SDK execution, commit or push. Other tasks' changes preserved.
