# Ingest review: direct PayPal v6 saved-method sample

- Date: 2026-10-04
- Repository: `paypal-examples/v6-web-sdk-sample-integration`
- Work item: `github-9765a512b0b7925416d4`
- Approved mode: full additive
- From: `bb23e7c63305a872326f43c3d52c5edd53e20b43`
- To: `a318bcf7cb8a458b180df553ab459db3a5a79586`
- Authorization: user selected option 1, full additive with focused reading for this item only. No standing policy or registry change.
- No package release identity is invented for this commit-tracked sample.

## Reading Scope

Complete cumulative source and changelog read before editing. All fourteen current changed/new files and twelve existing prior versions read fully, sequentially. Current paths are relative to `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-10-04-a318bcf/files/`; corresponding prior paths are under `2026-09-19-bb23e7c/files/`. The two newly added saved-method files have no prior version.

1. `client/components/paypalPayments/oneTimePayment/html/src/advanced/sandboxedIframe/.nvmrc`
2. `client/components/paypalPayments/oneTimePayment/html/src/advanced/sandboxedIframeRedirect/.nvmrc`
3. `client/components/paypalPayments/oneTimePayment/typescript/eslint.config.js`
4. `client/components/paypalPayments/oneTimePayment/typescript/package.json`
5. `client/components/paypalPayments/oneTimePayment/typescript/src/app.ts`
6. `client/components/paypalPayments/savePayment/html/src/app.js`
7. `client/components/paypalPayments/savedPaymentMethods/html/src/app.js` (added)
8. `client/components/paypalPayments/savedPaymentMethods/html/src/index.html` (added)
9. `client/index.html`
10. `client/prebuiltPages/react/package.json`
11. `server/node/src/routes/authRouteHandler.ts`
12. `server/node/src/routes/index.ts`
13. `server/node/src/routes/ordersRouteHandler.ts`
14. `server/node/src/routes/vaultRouteHandler.ts`

Affected unchanged local dependencies also read fully at the current SHA:

- `server/node/src/server.ts`
- `server/node/src/paypalServerSdkClient.ts`
- `server/node/src/productCatalog.ts`
- `server/node/package.json`
- `server/node/src/middleware/crossOriginOpenerPolicyMiddleware.ts`
- `server/node/src/middleware/errorMiddleware.ts`
- `client/components/paypalPayments/oneTimePayment/typescript/src/orders.ts`
- `client/components/paypalPayments/oneTimePayment/typescript/src/alert.ts`
- `client/prebuiltPages/react/src/App.tsx`
- `client/prebuiltPages/react/src/main.tsx`

Comparison Markdown and the complete 790-line patch reviewed. Packet/comparison JSON metadata, selected/excluded changes and identities reconciled structurally; the large unchanged path inventories were checked mechanically, not treated as new semantic evidence. Packet Markdown required-path list matches its JSON exactly. All 537 referenced paths exist. The full 537-path assignment was not semantically reread.

## Mechanical Evidence Checks

- Prior manifest: 262 retained files / 877,954 bytes; all size and SHA-256 checks passed.
- Current manifest: 264 retained files / 892,436 bytes; all size and SHA-256 checks passed.
- Two additions, twelve modifications, 250 hash-identical retained files, no deletion.
- Current exclusions: eleven files / 397,902 bytes. Changed test and lockfile remain excluded under reviewed policy.
- Comparison changed paths match actual retained hashes; pathspec inventory equals the union of both snapshots.
- Packet Markdown, comparison Markdown and patch hashes checked against their records. Raw snapshots, packet, registry and comparison remain unchanged.
- No upstream runtime library, excluded test, lockfile installation or full upstream repository read is claimed.

## Grounding Gate

Exact current-SHA excerpts extracted before writing:

- Saved-method `app.js:41`: `components: ["paypal-saved-payment-methods", "paypal-messages"],`
- Saved-method `app.js:59`: `commit: false,`
- Saved-method `app.js:210`: `if (createResult.status === "COMPLETED") {`
- `authRouteHandler.ts:31`: `? { target_customer_id: targetCustomerId }`
- `vaultRouteHandler.ts:98`: `// here is for local testing/development of the saved payment methods`

## Ingest Disposition

Concept audit and updates to PayPal Checkout/Vault preceded source edits. Added the new commit's client/token/order knowledge to the cumulative source and separate changelog; retained earlier SHA-qualified knowledge, warnings and raw references. No new cross-company comparison is warranted. Company source count stays 177. Company/provider indexes and provider/root logs updated; root analysis index updated only for the related dated frontend-gap finding.

The September 27 direct-v6 gap analysis retains its historical conclusion/table and now begins with an October 4 update based on the September 29 direct-PayPal HTML sample. Direct client-token/Orders processing is not confused with Braintree preferred-token/nonce processing; no new typed or React saved-method wrapper is inferred from dependency-range updates.

Important limits retained: either-ID instruction is not enforced; failed/ineligible reinitialization can retain an earlier visible session; overlapping initialization has no generation guard; merchant/customer ownership binding and durable persistence are absent; HTTP success and the displayed captured label are not capture-state proof; fresh request UUIDs are not stable application retry keys. These are source-review findings, not reproduced hosted-runtime defects.

## Validation

The first collection-validator run found two errors for the older server-side sample packet `github-849ba0a66c8ae04ad9da`: live shared context exceeded its historical 900,000-byte budget (900,704 bytes). This was not a new snapshot failure. Narrow correction: shorten eleven recent SDK Release root-log summaries, retaining their release findings in the linked PayPal log and cumulative source/changelog. No raw, registry, old packet or validator-policy change.

- `validate_wiki.py`: seven touched typed pages passed, no issues.
- `validate_github_collection.py`: 179 snapshots, 164 release records, 122 comparisons and 179 work items passed before completion.
- Historical source Grounding-through-update body and all earlier ledger entries are retained verbatim; previous dated analysis conclusion/table and following evidence are preserved.
- Source raw declarations and all explicit raw/tracking references resolve; company/provider catalogs have exactly one entry each for source and ledger, and company source count remains 177.
- Old packet live context now measures 899,765 bytes, under 900,000. An initial auxiliary link check treated a `:3-7` line suffix as part of a filename; after correcting only the checker's line-suffix handling, the evidence-path check passed. No evidence file correction was needed.
- `git diff --check` passed. Unrelated dirty work retained and not staged.
- Completion recorded as `ingested`; final collection-validator rerun passed with the same counts. Repository index accepts `default-branch@a318bcf`, checked 2026-10-04, next scheduled check 2026-11-04. Git staging remains empty.

No SDK execution, build, browser, account, or payment test; no commit or push authorized in this ingest turn.
