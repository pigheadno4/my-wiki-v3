# Adyen Web Bounded Source Capsule

## Status

Approved concept, pending review of this written specification before implementation.

## Problem

The initial `@adyen/adyen-web@6.41.0` policy selected all of
`packages/lib/src`. That produced 1,130 eligible files after category
exclusions, exceeding the reviewed 340-file capsule limit. Raising the limit
would make mandatory full-read, serial ingest impractical.

## Approaches Considered

1. Raise the capsule limit above 1,130 files.
   Rejected because it weakens the collection safety boundary and makes full
   ingest expensive and difficult to audit.
2. Exclude stories or broad source categories until the existing policy fits.
   Rejected because stories are useful integration evidence and broad
   exclusions would not create a coherent public API capsule.
3. Keep a bounded base capsule and collect exact-SHA component supplements.
   Selected because it preserves stable release identity, useful public
   evidence, and a controlled path to deeper implementation evidence.

## Base Capsule

The focused package remains `@adyen/adyen-web`. Its base capsule will retain:

- package manifest and declared public entry targets;
- `src/index.ts`, `src/index.umd.ts`, and `src/types.ts`;
- `src/types/`;
- `src/core/`;
- `src/components/index.ts` and `src/components/types.ts`;
- `src/components/Dropin/`;
- `src/components/Card/`; and
- `src/components/ThreeDS2/`.

Tests and fixtures remain excluded. Stories inside retained component roots
remain eligible. Reviewed generated target declarations under `dist/` remain
allowed, but untracked generated output is not copied into the capsule.

The package resolver's existing internal-runtime-closure behavior may add
required tracked internal dependencies. It must not silently broaden the
selection past the configured file or UTF-8 byte budgets.

## Supplements

Payment-method implementations outside the base capsule are collected only as
immutable exact-SHA supplements. Examples include PayPal, PayPal Fastlane,
Apple Pay, Google Pay, and local payment methods.

Each supplement must:

- use the exact snapshot SHA for the relevant package release;
- contain only explicitly requested repository-relative paths;
- pass path, file-size, total-size, hash, and secret validation;
- remain separate from the accepted base snapshot; and
- be linked from the cumulative source page when ingested.

The absence of a component supplement is an explicit evidence gap, not
permission to infer implementation behavior from public registration alone.

## Collection Flow

1. Update only the Adyen Web capsule policy in the repository registry.
2. Resolve the policy against tag `v6.41.0` and record selected file count,
   UTF-8 byte count, retained stories, and excluded tests.
3. Require both capsule limits to pass without increasing them.
4. Retry existing item `github-9f56dfbe62e4e84b03c7`; do not create a new
   work-item identity.
5. Publish the immutable snapshot and release record only after all validation
   succeeds.
6. Stop at `awaiting_approval`. Do not ingest automatically.

## Failure Handling

- Missing required public paths route directly to `needs_manual_review`.
- Dependency closure exceeding either budget routes to
  `needs_manual_review`; it does not increase limits automatically.
- Secret findings, invalid Git objects, package-version mismatch, or partial
  publication remain fail-closed.
- A failed retry must preserve the current accepted wiki and publish no partial
  Adyen evidence.

## Acceptance Criteria

- Registry and capsule policy tests pass.
- The exact `v6.41.0` base capsule is at most 340 files and 3,000,000 UTF-8
  bytes.
- Tests and fixtures are absent.
- Stories under retained roots remain present when tracked.
- Public package entry points, core checkout flow, Drop-in, Card, and 3DS2
  evidence are present.
- The GitHub collection validator passes.
- Successful collection reuses the existing work-item identity and ends in
  `awaiting_approval`.
- No Adyen source-page ingest occurs without a separate user approval.
