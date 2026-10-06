# Braintree Node 3.40.0 Ingest Review

- Date: 2026-10-06
- Item: `github-4452866907fd5ff661c9`
- Repository: `braintree/braintree_node`
- Package: `braintree@3.39.0` -> `braintree@3.40.0`
- SHA: `deb5227f1c4824b1f622115caf2ba4302134d375`
- User-approved mode: full additive with focused reading; collection packet's original delta recommendation preserved unchanged.
- No commit or push authorized or performed.

## Reading and Evidence Checks

Read cumulative source and release ledger, release record, comparison narrative and retained-source patch sections, all 19 changed non-changelog source files, affected prior implementations and unchanged helper dependencies (Address, Dispute, AdvancedSearch, exceptions, exports and error types). Read the new changelog section completely; verify the older cumulative history mechanically. Excluded test/lockfile patch sections are not the basis for implementation claims or executed-test claims.

Both snapshot manifests parsed structurally. Every retained file checked against its manifest size and SHA-256: 170 prior and 170 current files; 20 modified, 150 unchanged, no retained additions/deletions. The release manifest records an empty notes body. The older changelog suffix beginning at `## 3.39.0` is byte-identical, SHA-256 `a7bd325e13f3d5f5062e26c7975ba01831d9d6d81da50603a3514b66b4906d97`. Package manifest comparison differs only in `version`.

Grounding before wiki edits:

- `CHANGELOG.md:5`: "- Add `achType` to transaction search"
- `CHANGELOG.md:7`: "- Add support for `surchargeAmount` in `Transaction.refund()`"
- `lib/braintree/util.js:298`: `return typeof value !== "string" || !/^[A-Za-z0-9_-]+$/.test(value);`
- `lib/braintree/transaction_search.js:54`: `this.multipleValueField("achType", { allows: Transaction.AchType.All() }); // eslint-disable-line new-cap`

All locations above are under `raw/github/braintree/braintree_node/snapshots/2026-10-06-deb5227/files/`.

## Decisions and Limits

Concept audit updated `braintree-server-sdk` before source promotion. Existing source and ledger were extended; mechanical checks confirm the entire older source baseline and prior ledger entry remain verbatim. Company source count remains unchanged. No cross-provider comparison or new concept is warranted.

Path-ID/token allowlist effects include new gateway guards, TestingGateway and unchanged Address/Dispute helper callers. Preserve the distinction between local not-found errors and an HTTP 404, request-body and path IDs, and input validation and merchant authorization. Refund options forwarding already existed at 3.39.0; the 3.40.0 surcharge announcement is not a newly implemented forwarding path. ACH search is not enablement or settlement proof. Node and Ruby share a package name but not a repository history. Code samples are illustrative and unexecuted.

## Verification

- `validate_wiki.py`: five touched typed pages pass (source, ledger, concept, company, provider log).
- Provider index and root log are existing untyped catalog/log files; passing them to the typed validator reports missing YAML frontmatter. Their scoped link edits are existing resolvable source/log links; no schema conversion performed.
- `git diff --check`: pass.
- `validate_github_collection.py`: no new Node errors; two pre-existing unrelated errors remain for PayPal item `github-849ba0a66c8ae04ad9da` (packet rebuild exceeds UTF-8 budget; invalid packet).
- No SDK runtime, upstream unit/integration or live payment tests performed.

## Separate Follow-up

Future-mode discovery mixes the globally named Node and Ruby `braintree` package histories, causing Ruby 4.40.0 to suppress Node 3.40.0 selection. Exact release collection succeeded. Correct repository scoping separately; no collector or registry changes in this ingest.
