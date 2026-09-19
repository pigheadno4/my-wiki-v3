# Ingest review: default-branch@bb23e7c

Operator checkpoint only; generated work-items.json remains state authority.

## Authorization and evidence

- User approved full additive ingest of `github-9b81f89deff88d93db88`, then explicitly chose "Use focused reading for this update". This one-time exception does not alter registry policy, immutable packet, or default full-read rules.
- Read all 65 changed/new files fully, with all 62 prior file versions, using full-context diffs; read current cumulative source/changelog and affected dependencies. Did not semantically reread all 532 assigned paths.
- Supporting complete reads: server auth handler, authorization helper, SDK client, product catalog, server entry, vault handler; React CardFields checkout and save-payment parents, utils and types; prior ACH button implementation; shared local-method README.
- SHA-256 and byte-size checks passed for all 259 old and 262 new retained files. Exactly 197 retained files are unchanged; changed set exactly matches the 65 packet entries. Packet Markdown and snapshot-manifest hashes match packet JSON.
- New capsule: 262 files / 877,954 bytes. Prior: 259 files / 864,367 bytes. Eleven exclusions remain images, lockfile, and tests. No excluded or unclassified changes in the comparison.
- Identity: `de90a89c90b06421ca34241e7162236e2b04fd79` to `bb23e7c63305a872326f43c3d52c5edd53e20b43`; commit 2026-09-17, collection 2026-09-19. This is a commit transition, not a semantic SDK release.

## Grounding before wiki writes

All locations below are under `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-09-19-bb23e7c/files/`.

1. `client/components/bankAchPayments/walletPayment/html/src/recommended/app.js:61`: `standardEntryClassCode: "WEB",`
2. Same file, line 99: `walletSession.connect("bank-ach-wallet-payments", createOrderSession);`
3. `client/prebuiltPages/react/src/hooks/useCardFieldsValidation.ts:94`: `(!fieldsState.name || fieldsState.name.isEmpty || fieldsState.name.isValid);`
4. `client/components/localPaymentMethods/idealPayments/html/src/app.js:98`: `{ presentationMode: "auto" },`
5. `server/node/src/routes/ordersRouteHandler.ts:535`: `"Storing ACH authorization (consent) record for NACHA compliance:",` is a console-log argument, not implemented persistent storage.

## Workflow checklist

- [x] Read approved focused evidence, prior versions, dependencies, and cumulative history; verify hashes and grounding.
- [x] Concept audit and updates before source edits: checkout, APM, expanded checkout, vault; new PayPal ACH concept because no matching concept existed.
- [x] Add current source findings without removing historical knowledge.
- [x] Update company; retain source count for an existing source.
- [x] Confirm reciprocal concept citations.
- [x] Comparison decision: no cross-company comparison warranted.
- [x] Record documentation/code contradictions and evidence limits.
- [x] Update PayPal index.
- [x] Update provider and root logs.
- [x] Validate and complete exactly this work item.

## Completion checks

- `validate_wiki.py`: nine touched content/log pages, no issues; provider-index/root-log links checked separately.
- Source/changelog catalog entries remain unique in PayPal company/index. Existing source_count remains 177; no source page was added.
- `validate_github_collection.py`: 110 snapshots, 95 release records, 52 comparisons, 109 work items; no structural errors before and after completion.
- `git diff --check`: clean.
- CLI approved and claimed only this item, then `complete-ingest` returned `state: ingested`, `approved_mode: full`. Prior source/changelog sections and raw snapshots retained. No commit or push performed.

## Review boundaries

ACH wallet is an HTML addition, not a React wrapper. Consent logging, missing local APPROVED-status enforcement, optional/unmodeled bank fields, and USD 100 eligibility versus USD 205 default cart are sample limitations, not proof of runtime behavior or compliance. React save-card success omits the final payment-token exchange; this is retained behavior exposed by the review, not a new regression. No live payment, merchant eligibility, or settlement tests. No commit or push authorized.
